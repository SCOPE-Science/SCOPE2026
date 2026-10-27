"""Independent symbolic polynomial verification of tame rational maps over F2.
Requires SymPy; enumerates all coprime pairs in degrees 2, 4, and 6.
"""
from collections import Counter
from itertools import product
from math import comb
from sympy import Poly, symbols, factor_list
x=symbols('x')

def polynomial(a):
    return Poly(sum(((a>>j)&1)*x**j for j in range(a.bit_length())),x,modulus=2)

def jet(a,j):
    return Poly(sum(((a>>i)&1)*(comb(i,j)&1)*x**(i-j) for i in range(j,a.bit_length())),x,modulus=2)

def crit_profile(A,B,d):
    ts=[jet(A,j)*polynomial(B)-polynomial(A)*jet(B,j) for j in range(d+1)]
    if ts[1].is_zero: return None
    prof=[]
    for p,exponent in factor_list(ts[1].as_expr(),x,modulus=2)[1]:
        q=Poly(p,x,modulus=2)
        e=next(j for j in range(2,d+1) if not ts[j].rem(q).is_zero)
        prof.append((q.degree(),e))
    ar=sum(((A>>j)&1) <<(d-j) for j in range(d+1))
    br=sum(((B>>j)&1) <<(d-j) for j in range(d+1))
    jt=[jet(ar,j)*polynomial(br)-polynomial(ar)*jet(br,j) for j in range(d+1)]
    einf=next(j for j in range(1,d+1) if jt[j].eval(0)%2)
    if einf>1:prof.append((1,einf))
    return tuple(sorted(prof))

def audit(d):
    result=set(); count=0;prof=Counter()
    for A,B in product(range(1<<(d+1)),repeat=2):
        if not (((A|B)>>d)&1):continue
        if polynomial(A).gcd(polynomial(B)).degree():continue
        count+=1
        v=crit_profile(A,B,d)
        if v and all(e%2 for _,e in v):result.add((A,B));prof[v]+=1
    return count,result,prof

if __name__=='__main__':
    for d in (2,4):
        n,got,p=audit(d)
        print(d,n,len(got),p,flush=True)
        assert n==6*4**(d-1)
        assert not got
    # Independent symbolic Hasse-jet test on the complete 72-pair candidate certificate.
    pairs={tuple(map(int,row.split())) for row in open('tame_d6_pairs.txt')}
    assert len(pairs)==72
    for A,B in pairs:
        assert polynomial(A).gcd(polynomial(B)).degree()==0
        assert ((A|B)>>6)&1
        v=crit_profile(A,B,6)
        assert v==((1,3),(1,5),(2,3)),(A,B,v)
    print('Symbolic check: 72 degree-six candidate pairs have certified tame profile (1,3),(1,5),(2,3)')
    print('INDEPENDENT SYMBOLIC PASS')
