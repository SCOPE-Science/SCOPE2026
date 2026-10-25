import math,itertools
from functools import lru_cache
from fractions import Fraction
import sympy as sp

def weighted_count(m,a,q):
    M=sp.Matrix(q+1,q+1,lambda r,c: math.comb(c+a-1,a-1) if r+c<=q else 0)
    return int(sp.trace(M**m))

def poly_interpolation_difference(m,a):
    t=sp.Symbol('t'); d=m*a
    vals={q:weighted_count(m,a,q) for q in range(2*d+2)}
    E=sp.interpolate([(q,vals[q]) for q in range(0,2*(d+1),2)],t)
    O=sp.interpolate([(q,vals[q]) for q in range(1,2*(d+1)+1,2)],t)
    return sp.factor(E-O)

def difference_cone_formula(m,a):
    t,z=sp.symbols('t z'); D=m*(a-1)
    B=sp.eye(m)
    for i in range(m):B[i,(i+1)%m]+=1
    V=B.inv()
    zero=(0,)*m
    def mul(f,g):
        ans={}
        for p,b in f.items():
            for r,c in g.items():
                ix=tuple(p[i]+r[i] for i in range(m))
                if max(ix)<a:
                    ans[ix]=ans.get(ix,0)+b*c
        return {x:sp.expand(y) for x,y in ans.items() if y!=0}
    def linear(col):
        o={}
        for i in range(m):
            ix=tuple(int(j==i) for j in range(m))
            o[ix]=-V[i,col]
        return o
    log_series=sp.series(1/(1+sp.exp(z)),z,0,D+1).removeO().expand()
    coeff=[log_series.coeff(z,k) for k in range(D+1)]
    f={zero:sp.Integer(1)}
    for j in range(m):
        lin=linear(j); pp={zero:sp.Integer(1)}; factor={zero:sp.Integer(0)}
        for k in range(D+1):
            if coeff[k]:
                for mon,c in pp.items():factor[mon]=factor.get(mon,0)+coeff[k]*c
            pp=mul(pp,lin)
        f=mul(f,factor)
    for j in range(m):
        e={tuple(int(i==j)*k for i in range(m)):(t/sp.Integer(2))**k/sp.factorial(k) for k in range(a)}
        f=mul(f,e)
    W=sp.prod((z+k) for k in range(1,a))/sp.factorial(a-1)
    coeff_w=[sp.expand(W).coeff(z,j) for j in range(a)]
    ans=sum(c*sp.prod(coeff_w[k]*sp.factorial(k) for k in ix) for ix,c in f.items())
    return sp.factor(ans)

def direct_vector_count(m,a,q):
    count=0
    for x in itertools.product(range(q+1),repeat=m*a):
        levels=[sum(x[i*a:(i+1)*a]) for i in range(m)]
        if all(levels[i]+levels[(i+1)%m]<=q for i in range(m)):
            count+=1
    return count

if __name__=='__main__':
 for m,a,maxq in [(3,1,5),(5,1,3),(3,2,3)]:
    for q in range(maxq+1):
      assert direct_vector_count(m,a,q)==weighted_count(m,a,q),(m,a,q)
 for m,a in [(3,1),(5,1),(7,1),(3,2),(5,2),(3,3)]:
    p=poly_interpolation_difference(m,a)
    f=difference_cone_formula(m,a)
    top=sp.Rational(1,2**(m*a)*math.factorial(a-1)**m)
    t=sp.Symbol('t')
    assert sp.simplify(p-f)==0,(m,a,p,f)
    assert sp.degree(p,t)==m*(a-1)
    assert sp.LC(sp.Poly(p,t))==top
    print('verified',m,a,'difference',p)
 print('ODD_CYCLIC_BLOCK_PERIOD_CERTIFIED')
