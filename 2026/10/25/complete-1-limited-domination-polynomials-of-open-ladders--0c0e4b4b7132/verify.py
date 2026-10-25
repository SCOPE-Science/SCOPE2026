#!/usr/bin/env python3
"""Exact checks for the ladder 1-limited-domination polynomial.
Requires only Python's standard library; execute: python3 verify.py.
"""
from collections import defaultdict
from itertools import product

# A column is the pair of vertex-membership bits, encoded as 0,1,2,3.
def bit(s, r):
    return (s >> r) & 1

def wt(s):
    return bit(s, 0) + bit(s, 1)

def condition(value, neighbors):
    return (sum(1 - x for x in neighbors) <= 1 if value
            else sum(neighbors) >= 1)

def left_boundary(a, b):
    return all(condition(bit(a, r), [bit(a, 1-r), bit(b, r)])
               for r in (0, 1))

def middle(a, b, c):
    return all(condition(bit(b, r),
                         [bit(a, r), bit(b, 1-r), bit(c, r)])
               for r in (0, 1))

# Polynomials represented as dicts exponent -> integer coefficient.
def add_to(P, k, v):
    P[k] = P.get(k, 0) + v

def normalized(P):
    return {i:c for i,c in P.items() if c != 0}

def shift(P, j, m=1):
    return {i+j:c*m for i,c in P.items()}

def linear_sum(terms):
    ans = {}
    for mul, power, P in terms:
        for k,c in P.items():
            add_to(ans, k+power, mul*c)
    return normalized(ans)

def transfer_polynomials(N):
    if N < 2:
        return {1:{1:2, 2:1}}
    state = {(a,b):{wt(a)+wt(b):1}
             for a in range(4) for b in range(4) if left_boundary(a,b)}
    out={1:{1:2, 2:1}}
    for n in range(2,N+1):
        q={}
        for (a,b),P in state.items():
            if left_boundary(b,a):
                for k,c in P.items():
                    add_to(q,k,c)
        out[n]=normalized(q)
        nxt={}
        for (a,b),P in state.items():
            for c in range(4):
                if middle(a,b,c):
                    tgt=nxt.setdefault((b,c),{})
                    for k,val in P.items():
                        add_to(tgt,k+wt(c),val)
        state=nxt
    return out

def graph_brute(n):
    neighbor=[[] for _ in range(2*n)]
    for i in range(n):
        for r in range(2):
            v=2*i+r
            neighbor[v].append(2*i+1-r)
            if i: neighbor[v].append(2*(i-1)+r)
            if i+1<n:neighbor[v].append(2*(i+1)+r)
    poly={}
    minima=[]
    for states in product(range(4), repeat=n):
        flags=[bit(s,r) for s in states for r in range(2)]
        if any(not condition(flags[v],[flags[w] for w in neighbor[v]])
               for v in range(2*n)):
            continue
        k=sum(flags)
        add_to(poly,k,1)
        if k==n:
            minima.append(states)
    return poly,minima

def predicted_minima(n):
    base=[(1,)*n,(2,)*n]
    if n%2==0:
        pattern=tuple(0 if ((i//2)%2==0 and i%2==0) or
                           ((i//2)%2==1 and i%2==1) else 3 for i in range(n))
        # This is 0,3,3,0,0,3,3,0,...
        base += [pattern,tuple(3-x for x in pattern)]
    return set(base)

# This recurrence is encoded by the claimed denominator.
# Q(t,z)=1-z^2*t-z^3*t^2-(z^5+2*z^4)*t^3
#        -(z^6+z^5+z^4)*t^4-z^6*t^5.
def recurrence_residual(n, F):
    return linear_sum([(1,0,F[n]),(-1,2,F[n-1]),
        (-1,3,F[n-2]),(-1,5,F[n-3]),(-2,4,F[n-3]),
        (-1,6,F[n-4]),(-1,5,F[n-4]),(-1,4,F[n-4]),
        (-1,6,F[n-5])])

# Claimed numerator t*z*[(z+2)+(2z^2+4z)t+
# (z^4+3z^3+2z^2)t^2+(z^5+2z^4+4z^3)t^3+2z^5*t^4].
NUM={1:{1:2,2:1},2:{2:4,3:2},
     3:{3:2,4:3,5:1},4:{4:4,5:2,6:1},5:{6:2}}

def main():
    F=transfer_polynomials(26)
    for n in range(1,10):
        actual, minima=graph_brute(n)
        assert actual==F[n],(n,actual,F[n])
        if n>=2:
            assert set(minima)==predicted_minima(n),(n,minima,predicted_minima(n))
    print('DIRECT_GRAPH_ENUMERATION n=1..9: PASS')
    print('MINIMUM_CONFIGURATION_CLASSIFICATION n=2..9: PASS')
    # For n=1..5, the coefficient of t^n in Q(t,z)*F(t,z) equals NUM[n].
    for n in range(1,6):
        # Define missing F[0] and all F[j<1] as zero explicitly.
        terms=[(1,0,F[n])]
        Q={1:[(2,1)],2:[(3,1)],3:[(5,1),(4,2)],
           4:[(6,1),(5,1),(4,1)],5:[(6,1)]}
        for h,mons in Q.items():
            if n-h>=1:
                terms += [(-mul,degree,F[n-h]) for degree,mul in mons]
        assert linear_sum(terms)==NUM[n],(n,linear_sum(terms),NUM[n])
    print('RATIONAL_NUMERATOR_COEFFICIENTS n=1..5: PASS')
    # One extra base case (n=6) verifies recurrence involving F[1].
    assert recurrence_residual(6,F)=={},recurrence_residual(6,F)
    # In a 16-state transfer representation, for n=j+7 this residual is
    # u^T T^j P(T)v. Cayley-Hamilton implies that checking j=0..15
    # suffices to prove vanishing for ALL j>=0.
    for n in range(7,23):
        assert recurrence_residual(n,F)=={},(n,recurrence_residual(n,F))
    print('16_CAYLEY_HAMILTON_CERTIFICATE_POLYNOMIAL_IDENTITIES j=0..15: PASS')
    for n in range(2,27):
        P=F[n]
        assert min(P)==n
        assert P[n]==(4 if n%2==0 else 2)
        assert sum(P.values())>0
    print('ALL_CARDINALITY_POLYNOMIAL_TRANSFER_CHECKS n=2..26: PASS')
    print('TOTAL_COUNTS n=1..12:', [sum(F[n].values()) for n in range(1,13)])
    print('SAMPLE_POLYNOMIAL n=5:',dict(sorted(F[5].items())))
    print('VERIFY_OK')

if __name__=='__main__':main()
