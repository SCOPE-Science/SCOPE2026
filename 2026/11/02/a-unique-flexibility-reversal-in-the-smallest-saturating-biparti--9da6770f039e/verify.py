#!/usr/bin/env python3
"""Exact finite graph-polynomial certificate for the saturating-flexibility law.
No nonstandard Python dependencies.  Run: python3 verify.py
"""
from itertools import permutations
from math import comb
from fractions import Fraction
import json
from pathlib import Path

# Polynomials in (p,q) or (u,v,w), integer coefficients.
def add(A,B,scale=1):
    ans=A.copy()
    for mon,c in B.items():
        ans[mon]=ans.get(mon,0)+scale*c
        if ans[mon]==0: del ans[mon]
    return ans

def mul(A,B):
    out={}
    for mon,c in A.items():
        for mon2,d in B.items():
            m=tuple(x+y for x,y in zip(mon,mon2))
            out[m]=out.get(m,0)+c*d
    return {m:c for m,c in out.items() if c}

def power(A,n):
    r={(0,)*len(next(iter(A))):1}
    for _ in range(n): r=mul(r,A)
    return r

P_VAR={(1,0):1}; Q_VAR={(0,1):1}; ONE={(0,0):1}

def maximum_matching(n,mask):
    # Exhaustively searches all partial injections, with memoized subset recursion.
    cache={}
    def best(i,used):
        if i==n: return 0
        key=i,used
        if key not in cache:
            found=best(i+1,used)
            for j in range(n):
                if not (used>>j)&1 and (mask>>(i*n+j))&1:
                    found=max(found,1+best(i+1,used|(1<<j)))
            cache[key]=found
        return cache[key]
    return best(0,0)

def matching_independent(n,mask):
    # Independent exhaustive test by all row-to-column permutation matchings.
    return max(sum((mask>>(i*n+perm[i]))&1 for i in range(n)) for perm in permutations(range(n)))

def edge_level(i,j,frow,fcol):
    return 'q' if i in frow or j in fcol else 'p'

def expected(n,frow,fcol):
    # Each graph on K_{n,n} has probability monomial based on independent edges.
    total={}
    classes={}
    for mask in range(1<<(n*n)):
        val=maximum_matching(n,mask)
        assert val==matching_independent(n,mask), ('matching conflict',n,mask)
        pa=pb=qa=qb=0
        for i in range(n):
            for j in range(n):
                on=(mask>>(i*n+j))&1
                if edge_level(i,j,frow,fcol)=='p':
                    pa+=on;pb+=1-on
                else:
                    qa+=on;qb+=1-on
        counts=pa,pb,qa,qb
        classes[counts]=classes.get(counts,0)+val
    for (pa,pb,qa,qb),coef in classes.items():
        if not coef:continue
        term=mul(mul(power(P_VAR,pa),power(add(ONE,P_VAR,-1),pb)),
                 mul(power(Q_VAR,qa),power(add(ONE,Q_VAR,-1),qb)))
        total=add(total,{m:c*coef for m,c in term.items()})
    return total

# Polynomial obtained by collecting all 512 compatibility graph states on K_{3,3}.
P_TERMS={
 (3,5):6,(3,4):-25,(3,3):34,(3,2):-22,(3,1):8,(3,0):-2,
 (2,5):-15,(2,4):55,(2,3):-64,(2,2):35,(2,1):-12,(2,0):3,
 (1,5):9,(1,4):-31,(1,3):31,(1,2):-12,(1,1):3,(1,0):-1,
 (0,5):-3,(0,4):11,(0,3):-14,(0,2):8,(0,1):-3,(0,0):1}

TWO=add(Q_VAR,P_VAR,-1)
D3=add(expected(3,{0,1},set()),expected(3,{0},{0}),-1)
assert D3==mul(TWO,P_TERMS), 'exact K_{3,3} polynomial mismatch'
D2=add(expected(2,{0,1},set()),expected(2,{0},{0}),-1)
assert D2==mul(mul(TWO,add(ONE,Q_VAR,-1)),add(add(mul({(0,1):2},Q_VAR),{(0,1):-1}),( {(0,0):1}))), 'K_{2,2} formula mismatch'
# The last product is (q-p)(1-q)(2q^2-q+1).

def evaluate(A,p,q):
    return sum(Fraction(c)*p**i*q**j for (i,j),c in A.items())
for den in range(2,13):
    for pn in range(den+1):
        for qn in range(pn,den+1):
            p,q=Fraction(pn,den),Fraction(qn,den)
            d=evaluate(D3,p,q)
            assert d==(q-p)*evaluate(P_TERMS,p,q)
            assert evaluate(D2,p,q)==(q-p)*(1-q)*(2*q*q-q+1)
            if 0<p<1 and q==1:
                assert d==-p*(1-p)**3

# To prove strictly monotone P(p,q) in q on 0<=p<=q<=1,
# express -dP/dq in Bernstein-simplex coordinates
# u=p/L, q=(u+v)/L, L=u+v+w, multiplied by L^8.
U={(1,0,0):1};V={(0,1,0):1};W={(0,0,1):1}
L=add(add(U,V),W);UV=add(U,V)
H={}
for (i,j),c in P_TERMS.items():
    if j==0:continue
    term=mul(mul(power(U,i),power(UV,j-1)),power(L,8-i-(j-1)))
    H=add(H,{mon:-j*c*coeff for mon,coeff in term.items()})
assert len(H)==43, ('unexpected Bernstein certificate support',len(H))
assert all(c>0 for c in H.values()), ('nonpositive derivative coefficient',[(m,c) for m,c in H.items() if c<=0])
assert min(H.values())==3
# Boundary identities: P(p,p)>0 for p<1, and P(p,1)<0 for p>0.
for den in range(1,15):
    for num in range(den+1):
        p=Fraction(num,den)
        assert evaluate(P_TERMS,p,p)==(1-p)**2*(3*p*p-2*p+1)*(1+2*p*p*(1-p)*(3-p))
        assert evaluate(P_TERMS,p,Fraction(1))==-p*(1-p)**2

certpath=Path(__file__).with_name('bernstein_certificate.json')
certificate={
    'description':'Homogeneous degree-eight expansion of -L^8 (partial P/partial q)(u/L,(u+v)/L) with L=u+v+w; all coefficients nonnegative, with exactly two zero corner coefficients.',
    'coefficient_order':'u^i v^j w^k, i+j+k=8',
    'coefficients':[{'i':i,'j':j,'k':k,'value':H.get((i,j,k),0)} for i in range(8,-1,-1) for j in range(8-i,-1,-1) for k in [8-i-j]],
}
assert len(certificate['coefficients'])==45
if certpath.exists():
    assert json.loads(certpath.read_text())==certificate
else:
    certpath.write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n')
print('PASS: K2=16 graphs and K3=512 graphs under two independent match algorithms; exact symbolic polynomial identities; 43 positive Bernstein coefficients and 2 zero corner coefficients (minimum positive 3); exact rational boundary checks.')
