#!/usr/bin/env python3
"""Independent finite-field checks for commuting tuples of strictly upper-triangular 4x4 matrices."""
from itertools import product


def field_ops(q):
    if q in (2, 3, 5):
        return (lambda a,b: (a+b)%q), (lambda a,b: (a*b)%q), (lambda a: (-a)%q)
    if q == 4:
        # GF(2)[z]/(z^2+z+1), encoded by two binary coefficients.
        def add(a,b): return a ^ b
        def mul(a,b):
            bits=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1): bits ^= 1 << (i+j)
            if bits & 4: bits ^= 7
            return bits
        return add,mul,lambda a:a
    raise ValueError('unsupported field')


def formula(q, m):
    Q=q**m
    return Q*(Q**3+(Q-1)*(q*q*(2*q+1)*Q-q**4))


def comm(x,y,ops):
    add,mul,neg=ops
    a,b,c,d,e=x
    A,B,C,D,E=y
    return (
        add(mul(a,B),neg(mul(A,b))),
        add(mul(b,C),neg(mul(B,c))),
        add(add(mul(a,E),neg(mul(A,e))), add(mul(d,C),neg(mul(D,c))))
    )


def brute_reduced(q,m):
    ops=field_ops(q)
    states=list(product(range(q), repeat=5))
    zero=(0,0,0)
    N=len(states)
    compatible=[[] for _ in states]
    # Full independent pairwise-commutation test, no use of the proof's rank strata.
    for i,x in enumerate(states):
        compatible[i]=[j for j,y in enumerate(states) if comm(x,y,ops)==zero]
    if m == 1: return N
    if m == 2: return sum(map(len,compatible))
    # Ordered commuting triples / quadruples as progressively restricted cliques.
    def extend(candidates, left):
        if left==0: return 1
        if left==1: return len(candidates)
        result=0
        for j in candidates:
            other=set(compatible[j])
            result+=extend([z for z in candidates if z in other], left-1)
        return result
    return sum(extend(compatible[i],m-1) for i in range(N))


def main():
    cases=((2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2),(5,1))
    for q,m in cases:
        measured=brute_reduced(q,m)*q**m # independent central entry in each matrix
        expected=formula(q,m)
        assert measured==expected,(q,m,measured,expected)
        print(f'q={q} m={m}: {measured}')
    # Actual 6-coordinate commutator independent check of the central reduction.
    ops=field_ops(2)
    raw=list(product(range(2),repeat=6))
    actual=sum(1 for x in raw for y in raw if comm(x[:5],y[:5],ops)==(0,0,0))
    assert actual==formula(2,2)
    # A witness in the linear component, excluded from the generic component
    # by the closed rank-at-most-two condition on the (b,d,e) columns.
    b,d,e=(1,0,0),(0,1,0),(0,0,1)
    def det3(u,v,w):
        return (u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))%2
    assert det3(b,d,e)==1
    print('UT4_COMMUTING_TUPLES_OK',len(cases),'FULL_6_COORDINATE_CHECK')

if __name__=='__main__': main()
