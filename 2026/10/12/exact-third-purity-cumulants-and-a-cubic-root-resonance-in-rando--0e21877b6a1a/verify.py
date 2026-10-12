#!/usr/bin/env python3
"""Reproduce third fixed-cut purity cumulants for independent root-of-unity phases.
Only uses the Python standard library. Finite checks support but do not prove the general formula.
"""
from itertools import product, combinations
from math import comb
from fractions import Fraction

def counts(u,v):
    r=comb(u,2)*comb(v,2)
    t=comb(u,2)*comb(v,3)+comb(u,3)*comb(v,2)
    return r,t

def expectations(u,v,q):
    # exact expectation of each phase monomial, obtained from the exponent rule
    # E(exp(2 pi i k/q))=1 when k divisible by q, otherwise 0.
    rect=[]
    for i,j in combinations(range(u),2):
        for c,d in combinations(range(v),2):
            mon={(i,c):1,(j,d):1,(i,d):-1,(j,c):-1}
            rect.append(mon)
    def iszero(ms,signs):
        power={}
        for m,s in zip(ms,signs):
            for cell,val in m.items():power[cell]=power.get(cell,0)+s*val
        return all(val%q==0 for val in power.values())
    val2=0
    val3=0
    for a in rect:
        for b in rect:
            for x,y in product((1,-1),repeat=2):
                val2 += iszero((a,b),(x,y))
            for c in rect:
                for s in product((1,-1),repeat=3):
                    val3+=iszero((a,b,c),s)
    # (Re z)^k is 2^-k times the ordered signed exponential expansion
    R,T=counts(u,v)
    expected2=4*R if q==2 else 2*R
    expected3=48*T if q==2 else 12*T+(2*R if q==3 else 0)
    assert val2==expected2,(u,v,q,'second',val2,expected2)
    assert val3==expected3,(u,v,q,'third',val3,expected3)
    return val2,val3

def matrix_purity(u,v,vals,q):
    # Separately calculate tr[(SS^dagger/(uv))^2] from its Gram matrix.
    # The implementation does not construct or refer to a rectangle list.
    import cmath, math
    root=cmath.exp(2j*math.pi/q)
    z=[root**k for k in vals]
    total=0.0
    for i in range(u):
        for j in range(u):
            gram=sum(z[i*v+c]*z[j*v+c].conjugate() for c in range(v))
            total+=abs(gram)**2
    return total/(u*v)**2

def states(u,v,q):
    r,t=counts(u,v)
    cells=u*v
    # Exactly 2*Re omega^k is integral for q in {2,3,4}.
    assert q in (2,3,4)
    cos2=((2,-2) if q==2 else ((2,-1,-1) if q==3 else (2,0,-2,0)))
    tuples=[(i*v+c,j*v+d,i*v+d,j*v+c) for i,j in combinations(range(u),2) for c,d in combinations(range(v),2)]
    n=0; s1=s2=s3=0
    for vals in product(range(q),repeat=cells):
        z=0
        for ac,bd,ad,bc in tuples:z+=cos2[(vals[ac]+vals[bd]-vals[ad]-vals[bc])%q]
        n+=1;s1+=z;s2+=z*z;s3+=z*z*z
        # Direct Gram-matrix identity, independently of plaquette enumeration.
        if (u,v) in ((2,2),(2,4)) or (u,v,q)==(4,4,2) and n%577==0:
            P_from_rectangle=float(Fraction(u+v-1,u*v)+Fraction(2*z,(u*v)**2))
            P_from_gram=matrix_purity(u,v,vals,q)
            assert abs(P_from_rectangle-P_from_gram)<2e-11, (u,v,q,n,P_from_rectangle,P_from_gram)
    assert s1==0,(u,v,q,'mean',s1)
    E2=Fraction(s2,n)
    E3=Fraction(s3,n)
    target2=(4*r if q==2 else 2*r)
    target3=(48*t if q==2 else (12*t+2*r if q==3 else 12*t))
    assert E2==target2,(u,v,q,'variance',E2,target2)
    assert E3==target3,(u,v,q,'third',E3,target3)
    # 2*Re plaquette sum has E2 = 4R for q=2 or 2R for q>=3.
    return n, E2, E3

def main():
    symbolic=0
    for u,v in ((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)):
        for q in (2,3,4,5,6):
            expectations(u,v,q)
            symbolic+=1
    statechecks=0
    for u,v,q in ((2,2,2),(2,2,3),(2,2,4),(2,4,2),(2,4,3),(4,4,2)):
        n,_,_=states(u,v,q)
        statechecks+=n
    print('VERIFY_OK', symbolic,'exact monomial tests;',statechecks,'complete phase-array state comparisons')

if __name__=='__main__':main()
