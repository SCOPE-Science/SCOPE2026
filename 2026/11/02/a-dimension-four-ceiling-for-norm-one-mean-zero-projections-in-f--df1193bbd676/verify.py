"""Exact rational checks for norm-one projections in finite weighted Lorentz spaces.

This script uses only the Python standard library. All computations are rational.
"""
from fractions import Fraction as F
from itertools import product


def norm(x, w):
    return sum(a*b for a,b in zip(w, sorted(map(abs,x),reverse=True)))


def centering(x):
    m=sum(x)/len(x)
    return [z-m for z in x]


def finite_formula(w):
    n=len(w)
    best=F(-1)
    witness=None
    for k in range(1,n+1):
        den=sum(w[:k])
        for a in range((k+1)//2,k+1):
            m=F(2*a-k,n)
            vals=[1-m]*a+[-1-m]*(k-a)+[-m]*(n-k)
            val=norm(vals,w)/den
            if val>best:
                best=val; witness=(k,a)
    return best,witness


def all_sign_vertices(w):
    n=len(w)
    best=F(0)
    for k in range(1,n+1):
        for sg in product((-1,0,1), repeat=n):
            if sum(z!=0 for z in sg)!=k: continue
            val=norm(centering([F(z) for z in sg]),w)/sum(w[:k])
            best=max(best,val)
    return best


def theoretical_one(w):
    n=len(w)
    if n==2: return True
    if n==3: return w[0]==w[1]+w[2]
    if n==4: return w[0]==w[1]+w[2] and w[3]==0
    return False


def run():
    count=0
    grid=(F(0),F(1,4),F(1,2),F(3,4),F(1))
    from itertools import combinations_with_replacement
    for n in range(2,8):
        for rev_weights in combinations_with_replacement(grid,n):
            w=tuple(reversed(rev_weights))
            if w[0]==0: continue
            f,witness=finite_formula(w)
            if n<=5:
                e=all_sign_vertices(w)
                assert f==e,(n,w,f,e)
            assert (f==1)==theoretical_one(w),(n,w,f,witness)
            count+=1
    examples=[((F(1),F(3,5),F(2,5)),F(1)),
              ((F(1),F(3,5),F(2,5),F(0)),F(1)),
              ((F(1),F(1,2),F(1,2),F(0),F(0)),F(11,10))]
    for w,v in examples:
        got,_=finite_formula(w)
        assert got==v,(w,got,v)
    print('PASS: '+str(count)+' nonincreasing rational weight profiles in dimensions 2..7')
    print('PASS: complete ternary indicator comparison through dimension 5')
    print('PASS: exact 3-,4-,5-dimensional boundary examples')

if __name__=='__main__': run()
