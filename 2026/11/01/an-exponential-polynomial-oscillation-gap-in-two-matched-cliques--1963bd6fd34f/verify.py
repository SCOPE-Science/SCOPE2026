#!/usr/bin/env python3
"""Exact finite checks for synchronous majority on two matching-joined cliques.

Self-contained reproducibility companion. Finite checks support but cannot replace
parameter-uniform proofs in the accompanying mathematical text.
"""
from collections import Counter
from math import comb, factorial


def step_bits(state,n):
    mask=(1<<n)-1
    A=state&mask;B=(state>>n)&mask
    def side(X,Y):
        population=X.bit_count()
        result=0
        for i in range(n):
            old=(X>>i)&1
            positives=population-old+((Y>>i)&1)
            if 2*positives>n or (2*positives==n and old):
                result |= 1<<i
        return result
    return side(A,B)|(side(B,A)<<n)


def step_formula(state,n):
    mask=(1<<n)-1
    A=state&mask; B=state>>n
    def side(X,Y):
        k=X.bit_count()
        m=n//2
        if n%2==0:
            return 0 if k<m else mask if k>m else Y
        if k<m:return 0
        if k==m:return ((~X)&Y)&mask
        if k==m+1:return ((~X)|Y)&mask
        return mask
    return side(A,B)|(side(B,A)<<n)


def profile_step(profile,n):
    # Order 00, 01, 10, 11, recording the two opinions of matched pairs.
    a=profile[2]+profile[3]; b=profile[1]+profile[3]
    m=n//2
    def side(x,y,k):
        if n%2==0:
            return 0 if k<m else 1 if k>m else y
        if k<m:return 0
        if k==m:return (1-x)*y
        if k==m+1:return max(1-x,y)
        return 1
    out=[0]*4
    for code,mult in enumerate(profile):
        x=code//2;y=code%2
        new=2*side(x,y,a)+side(y,x,b)
        out[new]+=mult
    return tuple(out)


def expected_fixed(n):
    if n%2==0:return 4+comb(n,n//2)
    return 4


def expected_cycle_states(n):
    if n%2==0:
        c=comb(n,n//2)
        return c*c-c
    m=n//2
    return 2*(m+2)*comb(n,m)


def expected_cycle_basin(n):
    if n%2==0:return expected_cycle_states(n)
    m=n//2
    return 2*(m*m+2*m+2)*comb(n,m)


def expected_transient(n):
    if n==2:return 1
    if n==3:return 2
    if n%2==0:return 2
    return 3


def multiplicity(u,v,w,z):
    n=u+v+w+z
    return factorial(n)//(factorial(u)*factorial(v)*factorial(w)*factorial(z))


def profile_representative(u,v,w,z):
    A=0;B=0;i=u
    for _ in range(v):B |= 1<<i;i+=1
    for _ in range(w):A |= 1<<i;i+=1
    for _ in range(z):A |= 1<<i;B |= 1<<i;i+=1
    return A|(B<<i)


def check_profiles(n):
    totals=Counter()
    for u in range(n+1):
        for v in range(n+1-u):
            for w in range(n+1-u-v):
                z=n-u-v-w
                p0=(u,v,w,z)
                state=profile_representative(u,v,w,z)
                # Representatives use n paired positions even when there are
                # no 11-pairs; reconstruct upper bits with fixed n shift.
                state=(state & ((1<<n)-1)) | ((state >> (u+v+w+z))<<n)
                path=[state]
                for _ in range(8):path.append(step_formula(path[-1],n))
                T=next(t for t in range(7) if path[t]==path[t+2])
                assert T<=expected_transient(n),(n,p0,T)
                periodic=(T==0)
                period=1 if path[T]==path[T+1] else 2
                weight=multiplicity(u,v,w,z)
                totals[(period,'basin')]+=weight
                totals[(period,'periodic')]+=int(periodic)*weight
                totals[('transient',T)]+=weight
    assert totals[(1,'periodic')]==expected_fixed(n),(n,'fixed',totals)
    assert totals[(2,'periodic')]==expected_cycle_states(n),(n,'cycle',totals)
    assert totals[(2,'basin')]==expected_cycle_basin(n),(n,'basin',totals)
    assert totals[('transient',expected_transient(n))]>0,(n,'sharp',totals)
    assert totals[(1,'basin')]+totals[(2,'basin')]==4**n
    return totals


def check_independent_vertex_simulation(n):
    count=1<<(2*n)
    for s in range(count):
        f=step_bits(s,n)
        assert f==step_formula(s,n),(n,s,'step')
        path=[s]
        for _ in range(6):path.append(step_bits(path[-1],n))
        assert path[expected_transient(n)]==path[expected_transient(n)+2],(n,s,'cutoff')
        initial_is_two=(path[2]==path[0] and path[1]!=path[0])
        ultimate_is_two=(path[-1]!=path[-2])
        assert (not ultimate_is_two or (path[1]==path[3] and path[1]!=path[2])),(n,s,'basin')
        assert (not ultimate_is_two or next(t for t in range(5) if path[t]==path[t+2])<=1),(n,s,'basin_depth')
    return count


def main():
    checked=0
    for n in range(2,41):
        t=check_profiles(n)
        if n<=8:
            checked+=check_independent_vertex_simulation(n)
        if n in (2,3,4,5,6,7,8,9,10,20,40):
            print('n',n,'fixed',t[(1,'periodic')],
                  'primitive_two_orbits',t[(2,'periodic')]//2,
                  'sharp_transient',expected_transient(n),
                  'oscillation_probability',f'{t[(2,"basin")]}/{4**n}')
    print('independent_full_vertex_configs',checked)
    print('profile_sizes_checked',39,'range_n=2..40')
    print('TWO_CLIQUE_MAJORITY_PARITY_VERIFY_OK')

if __name__=='__main__':main()
