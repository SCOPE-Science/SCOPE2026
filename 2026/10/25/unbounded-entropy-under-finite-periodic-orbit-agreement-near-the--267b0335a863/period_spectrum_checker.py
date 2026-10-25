"""Exact rational finite checks for the localized tent-map construction.

Run: python period_spectrum_checker.py
These finite tests supplement, rather than replace, the general proof.
"""
from fractions import Fraction as F


def tent(x):
    return 2*x if x <= F(1,2) else 2*(1-x)


def data(H):
    P=H+1
    Q=1 << P
    a=F(2*Q-2,Q*Q)
    b=F(2*Q-1,Q*Q)
    return P,Q,a,b


def build(H,M):
    assert H>=1 and M>=3 and M%2==1
    P,Q,a,b=data(H)
    ell=b-a
    k=(2*Q-2)
    grid=Q*Q
    # Each interval carries the original dyadic atom index.
    atoms=[]
    for j in range(grid):
        if j == k:
            for t in range(M):
                atoms.append((a+F(t,M)*ell,a+F(t+1,M)*ell,j))
        else:
            atoms.append((F(j,grid),F(j+1,grid),j))
    def f(x):
        if not (a < x < b):
            return tent(x)
        v=(x-a)*M/ell
        j=v.numerator//v.denominator
        t=v-j
        low=tent(a); high=tent(b)
        return low+(high-low)*(t if j%2==0 else 1-t)
    return P,Q,a,b,atoms,f


def fixed_tent(n):
    answer=set()
    for j in range(1 << n):
        l=F(j,1 << n)
        r=F(j+1,1 << n)
        fl,fr=l,r
        for _ in range(n):
            fl,fr=tent(fl),tent(fr)
        slope=(fr-fl)/(r-l)
        x=(fl-slope*l)/(1-slope)
        if l<=x<=r:
            answer.add(x)
    return sorted(answer)


def check(H,M):
    P,Q,a,b,atoms,f=build(H,M)
    ell=b-a
    assert F(1,Q)<=a<b<=F(2,Q)
    assert 2*a>b
    for j in range(1,P):
        il=2**j*a
        ir=2**j*b
        assert il>b and ir<=1
        if j<P-1:
            assert ir<=F(1,2)
        else:
            assert il>=F(1,2)
    assert F(1,Q)<=a and b<=F(2,Q)
    for n in range(1,P):
        for x in fixed_tent(n):
            y=x
            for _ in range(n):
                y=f(y)
            assert y==x,(H,M,n,x,y)
            assert not a<=x<=b
    # Verify the exact Markov graph and old-state cloning description.
    origins=[j for _,_,j in atoms]
    orig=[]
    for j in range(Q*Q):
        l,r=F(j,Q*Q),F(j+1,Q*Q)
        yl,yr=sorted((tent(l),tent(r)))
        orig.append({t for t in range(Q*Q) if F(t,Q*Q)>=yl and F(t+1,Q*Q)<=yr})
    successors=[]
    for l,r,old in atoms:
        yl,yr=sorted((f(l),f(r)))
        actual={i for i,(u,v,_) in enumerate(atoms) if yl<=u and v<=yr}
        predicted={i for i,j in enumerate(origins) if j in orig[old]}
        assert actual==predicted,(H,M,old)
        successors.append(actual)
    # Each original dyadic atom maps onto the whole interval after 2P steps.
    # Cloning preserves the exact graph at that same horizon.
    for s in range(len(atoms)):
        states={s}
        for _ in range(2*P):
            states=set.union(*(successors[v] for v in states))
        assert len(states)==len(atoms),(H,M,s,len(states))
    # Images of the modified interval return over it for the first time at P.
    img=(a,b)
    for j in range(1,P+1):
        vals=[]
        for v in img:
            vals.append(f(v))
        img=tuple(sorted(vals))
        if j<=H:
            assert img[0]>b
        else:
            assert img[0]<=a and img[1]>=b
    return len(atoms),sum(map(len,successors))

if __name__=='__main__':
    for h in (1,2,3,4):
        for m in (3,5,9):
            n,e=check(h,m)
            print('PASS H=%s M=%s atoms=%s edges=%s' % (h,m,n,e))
    print('CHECKS_PASS')
