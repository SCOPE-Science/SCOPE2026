"""Exact-arithmetic checks for induced-open-triple/triangle covariance in G(n,m)."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial

def falling(x,j):
    y=1
    for i in range(j):y*=x-i
    return y

def vals(n,m):
    N=comb(n,2)
    def a(j):return F(falling(m,j),falling(N,j))
    C=comb(n,3); B=3*C
    ET=C*a(3); EP=B*a(2)
    ET2=C*(a(3)+3*(n-3)*a(5)+(C-1-3*(n-3))*a(6))
    EP2=B*(a(2)+(4*n-10)*a(3)+(B-4*n+9)*a(4))
    ETP=C*(3*a(3)+6*(n-3)*a(4)+(B-6*n+15)*a(5))
    covTP=ETP-ET*EP
    covTW=covTP-3*(ET2-ET*ET)
    EW=EP-3*ET
    return ET,EW,covTW,ET2-ET*ET,EP2-EP*EP+9*(ET2-ET*ET)-6*covTP

def factored(n,m):
    N=comb(n,2); C=comb(n,3)
    if m<=2 or m>=N-1:return F(0)
    K=m*(n*n-3*n-8)+n**3-2*n*n-3*n+4
    return -F(C*falling(m,3)*6*(N-m)*(N-m-1)*K,falling(N,3)*(n+1)*(n+2)*(N-5)*(N-4)*(N-2))

def brute(n,m,edges):
    c0=cT=cW=cTW=cT2=cW2=0
    triples=list(combinations(range(n),3))
    for sample in combinations(edges,m):
        es=set(sample)
        T=W=0
        for a,b,c in triples:
            k=((a,b) in es)+((a,c) in es)+((b,c) in es)
            T+=(k==3)
            W+=(k==2)
        c0+=1;cT+=T;cW+=W;cTW+=T*W;cT2+=T*T;cW2+=W*W
    return (F(cT,c0),F(cW,c0),F(cTW,c0)-F(cT*cW,c0*c0),F(cT2,c0)-F(cT*cT,c0*c0),F(cW2,c0)-F(cW*cW,c0*c0))

def main():
    checks=0
    for n in range(4,7):
        edges=list(combinations(range(n),2))
        for m in range(len(edges)+1):
            x=vals(n,m)
            y=brute(n,m,edges)
            assert x==y,(n,m,x,y)
            assert x[2]==factored(n,m),(n,m,x[2],factored(n,m))
            if 3<=m<=len(edges)-2:assert x[2]<0
            else:assert x[2]==0
            checks+=1
    # Independent independent-edge model: symbolic summation of all fixed-edge strata.
    from sympy import Symbol,expand,factor,Rational
    p=Symbol('p');n=5; N=comb(n,2); C=comb(n,3)
    ETT=EWW=ETW=0
    for m in range(N+1):
        t,w,c,_,_=vals(n,m)
        weight=comb(N,m)*p**m*(1-p)**(N-m)
        ETT+=Rational(t.numerator,t.denominator)*weight
        EWW+=Rational(w.numerator,w.denominator)*weight
        ETW+=Rational((c+t*w).numerator,(c+t*w).denominator)*weight
    explicit=3*C*p**4*(1-p)*(2*(n-3)-(3*n-8)*p)
    assert expand(ETW-ETT*EWW-explicit)==0
    # Universal rational identity and asymptotic coefficients are verified symbolically.
    import sympy as S
    nn,mm,pp=S.symbols('n m p',positive=True)
    NN=nn*(nn-1)/2;CC=nn*(nn-1)*(nn-2)/6;BB=3*CC
    ff=lambda x,k:S.prod(x-i for i in range(k))
    aa=lambda k:ff(mm,k)/ff(NN,k)
    tt=CC*aa(3);ww0=BB*aa(2)
    vt=CC*(aa(3)+3*(nn-3)*aa(5)+(CC-1-3*(nn-3))*aa(6))-tt**2
    vp=BB*(aa(2)+(4*nn-10)*aa(3)+(BB-4*nn+9)*aa(4))-ww0**2
    ctp=CC*(3*aa(3)+6*(nn-3)*aa(4)+(BB-6*nn+15)*aa(5))-tt*ww0
    ctw=ctp-3*vt
    k=mm*(nn**2-3*nn-8)+nn**3-2*nn**2-3*nn+4
    closed=-CC*aa(3)*6*(NN-mm)*(NN-mm-1)*k/((nn+1)*(nn+2)*(NN-5)*(NN-4)*(NN-2))
    assert S.cancel(ctw-closed)==0
    for expr,expected in [
        (ctw,-pp**4*(1-pp)**2),
        (vt,pp**3*(1-pp)**2*(1+2*pp)/6),
        (vp+9*vt-6*ctp,pp**2*(1-pp)**2*(1-3*pp+6*pp**2)/2)]:
        limit=S.factor(S.limit(S.cancel(expr.subs(mm,pp*NN)/nn**3),nn,S.oo))
        assert S.simplify(limit-expected)==0,(limit,expected)
    print('VERIFY_OK',checks,'exact fixed-edge strata; independent-edge polynomial; universal factorization; three dense limits')

if __name__=='__main__':main()
