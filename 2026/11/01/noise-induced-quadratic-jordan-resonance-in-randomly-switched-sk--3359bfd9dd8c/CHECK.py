"""Independent finite-time rational branch-integral checker for annealed tent-map correlations.
Run: python CHECK.py
No external modules are required.
"""
from fractions import Fraction as F

def integrate_product(lo, hi, A, B):
    # (x^2-1/3)*((A*x+B)^2-1/3) expanded in the initial coordinate.
    # Exact expansion: (x^2 -1/3)*(A^2*x^2+2AB*x+B^2-1/3)
    co = [-(B*B-F(1,3))/3,-2*A*B/3,B*B-F(1,3)-A*A/3,2*A*B,A*A]
    return sum(c*(hi**(j+1)-lo**(j+1))/F(j+1) for j,c in enumerate(co))

def branch_exact(law, n):
    state=[(F(0),F(1),F(1),F(0),F(1))]  # low, high, affine A,B, probability
    for _ in range(n):
        new=[]
        for lo,hi,A,B,weight in state:
            for a,wa in law:
                xcrit=(a-B)/A
                pts=[lo,hi]
                if lo<xcrit<hi:pts=[lo,xcrit,hi]
                for L,R in zip(pts,pts[1:]):
                    mid=(L+R)/2
                    if A*mid+B<a:
                        AA,BB=A/a,B/a
                    else:
                        AA,BB=-A/(1-a),(1-B)/(1-a)
                    new.append((L,R,AA,BB,weight*wa))
        state=new
    assert sum((hi-lo)*w for lo,hi,_,_,w in state)==1
    return sum(w*integrate_product(lo,hi,A,B) for lo,hi,A,B,w in state)

def formula(law,n):
    m=sum(w*a for a,w in law)
    q=sum(w*a*(1-a) for a,w in law)
    r=2*m-1
    s=1-3*q
    return F(1,180)*s**n+F(1,12)*r**n - (q/F(12))*sum(r**(n-1-j)*s**j for j in range(n))

def run():
    cases=[
        ('two-diagonalizable-resonant',[(F(1,2),F(1,4)),(F(5,6),F(3,4))],7),
        ('deterministic-resonant',[(F(2,3),F(1))],7),
        ('nonresonant-control',[(F(1,3),F(1,3)),(F(3,4),F(2,3))],6),
    ]
    checks=0
    for name, law, max_lag in cases:
        assert sum(w for a,w in law)==1
        for n in range(max_lag+1):
            exact=branch_exact(law,n)
            predicted=formula(law,n)
            assert exact==predicted, (name,n,exact,predicted)
            checks+=1
        print(name,'lags',max_lag+1,'passed')
    law=cases[0][1]
    m=sum(a*w for a,w in law)
    q=sum(w*a*(1-a) for a,w in law)
    lam=2*m-1
    assert (m,q,lam)==(F(3,4),F(1,6),F(1,2))
    assert 1-3*q==lam
    for n in range(25):
        assert formula(law,n)==(F(4,45)-F(n,36))/2**n
    assert formula(law,3)>0 and formula(law,4)<0
    for a,w in law:
        assert (2*a-1)!=(1-3*a*(1-a))
    print('25 exceptional-lag formulas and strict sign reversal passed; total full-branch integrals:',checks)
if __name__=='__main__':run()
