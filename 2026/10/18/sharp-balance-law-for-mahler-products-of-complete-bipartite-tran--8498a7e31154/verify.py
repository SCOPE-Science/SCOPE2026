"""Exact arithmetic and optional geometric checks for complete bipartite free-space Mahler products.
Run with: python3 verify.py
Optional: numpy and scipy enable polytope reconstruction for small examples.
"""
from fractions import Fraction
from math import comb, factorial


def central(k):
    return Fraction(comb(2*k,k),4**k)


def source_primal_volume(p,q):
    d=p+q-1
    coeff=sum(Fraction(comb(p-1,k)*comb(q-1,k)*comb(2*k,k),4**k)
              for k in range(min(p-1,q-1)+1))
    return Fraction(2**d,factorial(d))*coeff


def slice_primal_volume(p,q):
    d=p+q-1
    s=0
    for i in range(p):
        for j in range(q):
            s+=comb(p-1,i)**2*comb(q-1,j)**2*factorial(i+j)*factorial(d-1-i-j)
    return Fraction(2*s,factorial(p-1)*factorial(q-1)*factorial(d))


def polar_volume(p,q):
    d=p+q-1
    return Fraction(2**d*factorial(p)*factorial(q),factorial(d))


def normalized_mahler(p,q):
    d=p+q-1
    volume_product=source_primal_volume(p,q)*polar_volume(p,q)
    return volume_product / Fraction(4**d,factorial(d))


def R_alt(p,q):
    N=p+q
    return Fraction(N,comb(N,p))*sum(
        (central(k)-Fraction(1,k+1))*comb(p-1,k)*comb(q-1,k)
        for k in range(2,min(p-1,q-1)+1)) + 1


def monotonic_certificate(p,q):
    assert 2<=p and p+2<=q
    N=p+q
    D=[]
    for k in range(p+1):
        a=(p+1)*comb(p,k)*comb(q-2,k) if k<=min(p,q-2) else 0
        b=q*comb(p-1,k)*comb(q-1,k) if k<=min(p-1,q-1) else 0
        D.append(a-b)
    assert sum(Fraction(v,k+1) for k,v in enumerate(D))==0
    signs=[(1 if x>0 else -1 if x<0 else 0) for x in D]
    assert any(x<0 for x in signs) and any(x>0 for x in signs)
    assert [s for s in signs if s] == sorted([s for s in signs if s])
    weighted=sum(central(k)*D[k] for k in range(len(D)))
    assert weighted>0
    lhs=normalized_mahler(p+1,q-1)-normalized_mahler(p,q)
    rhs=Fraction(N,q*comb(N,p))*weighted
    assert lhs==rhs and lhs>0


def hull_checks():
    try:
        import numpy as np
        from scipy.spatial import ConvexHull, HalfspaceIntersection
    except ImportError:
        print('Optional SciPy hull tests unavailable')
        return 0
    count=0
    for p,q in [(1,2),(1,3),(2,2),(2,3),(3,2),(3,3),(2,4),(4,2)]:
        N=p+q
        # coordinate axes: all A except A_0, followed by B_0..B_{q-1}
        dim=N-1
        vv=[]
        HH=[]
        for ai in range(p):
            for bj in range(q):
                e=np.zeros(dim)
                if ai>0:e[ai-1]+=1
                e[p-1+bj]-=1
                vv.extend([e,-e])
                HH.extend([np.r_[e,-1.0],np.r_[-e,-1.0]])
        P=ConvexHull(np.array(vv)).volume
        Q=ConvexHull(HalfspaceIntersection(np.array(HH),np.zeros(dim)).intersections).volume
        assert abs(P-float(source_primal_volume(p,q)))<1e-7,(p,q,'primal',P,source_primal_volume(p,q))
        assert abs(Q-float(polar_volume(p,q)))<1e-7,(p,q,'polar',Q,polar_volume(p,q))
        count+=1
    return count


def main():
    exact=0
    for p in range(1,10):
        for q in range(1,10):
            assert source_primal_volume(p,q)==slice_primal_volume(p,q),(p,q,'slice')
            assert normalized_mahler(p,q)==R_alt(p,q),(p,q,'identity')
            assert normalized_mahler(p,q)==normalized_mahler(q,p)
            if min(p,q)<=2:assert normalized_mahler(p,q)==1
            else:assert normalized_mahler(p,q)>1
            exact+=1
    balanced=0
    for N in range(6,21):
        for p in range(2,(N-2)//2+1):
            q=N-p
            if q>=p+2:
                monotonic_certificate(p,q)
                balanced+=1
    geometric=hull_checks()
    print(f'PASS: {exact} exact independent-volume identities, {balanced} strict-balancing certificates, {geometric} primal/polar hull checks')


if __name__=='__main__':main()
