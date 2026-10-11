"""Exact arithmetic checks for the seven-agent bounded-confidence switching phase diagram.

Run: python3 check.py
Uses only Python's standard library. All calculations use rational fractions.
"""
from fractions import Fraction as Q
from math import ceil, log

BASE = tuple(map(Q, [0,36,72,84,96,132,168]))
R = tuple(map(Q, [18,42,48,12,48,42,18]))
V_MINUS = tuple(map(Q, [0,2,-3,0,3,-2,0]))
V_PLUS = tuple(map(Q, [0,2,1,0,-1,-2,0]))

def exact_state(a,b,t):
    u = a*Q((-1)**t,6**t)
    v = b*Q(1,2**t)
    return tuple(BASE[i]+u*V_MINUS[i]+v*V_PLUS[i] for i in range(7))

def neighbors(x):
    return tuple(tuple(j for j in range(7) if abs(x[j]-x[i])<=R[i]) for i in range(7))

def step(x):
    return tuple(sum((x[j] for j in nei),Q(0))/len(nei) for nei in neighbors(x))

def expected_neighbors(a,b,t):
    u = a*Q((-1)**t,6**t)
    v = b*Q(1,2**t)
    center = (2,3,4) if v>=3*u else (3,)
    return ((0,), (0,1,2), (1,2,3,4), center,
            (2,3,4,5), (4,5,6), (6,))

def exact_k(a,b):
    if a==0 or (b>0 and b>=3*a): return 0
    if b==0: return None
    k=0
    while b < 3*a*Q(1,9**k):
        k+=1
    return k

def check_point(a,b,max_t):
    x=exact_state(a,b,0)
    assert neighbors(x)==expected_neighbors(a,b,0)
    for t in range(max_t):
        assert x == exact_state(a,b,t), (a,b,t,'formula')
        assert neighbors(x)==expected_neighbors(a,b,t), (a,b,t,'graph')
        x=step(x)
    k=exact_k(a,b)
    if k is not None:
        counts=sum(expected_neighbors(a,b,t)[3]!=expected_neighbors(a,b,t+1)[3]
                   for t in range(max_t))
        expected=2*k-1 if k else 0
        assert counts==expected, (a,b,counts,expected)
    return max_t

if __name__=='__main__':
    cases=set()
    for aa in [Q(0),Q(1,100),Q(1,10),Q(1,3),Q(1,2),Q(1)]:
        for bb in [Q(0),Q(1,100),Q(1,10),Q(1,3),Q(1,2),Q(1)]:
            cases.add((aa,bb))
    for j in range(0,18):
        threshold=Q(1,3**(2*j+1))
        for offset in [Q(0), Q(99,100), Q(101,100)]:
            cases.add((Q(1), min(Q(1),threshold*offset)))
    cases.add((Q(1), Q(1,3**51)))
    total=0
    for a,b in sorted(cases):
        k=exact_k(a,b)
        n=max(66, 2*k+4) if k is not None else 66
        total+=check_point(a,b,n)
    # Enumerate exact switch-tail areas for uniform a,b on [0,1]^2.
    # For k>=m, the admissible region is 0<=b<3^(3-2m)*a.
    def exact_tail(m):
        c=Q(3)**(3-2*m)
        return Q(1)-Q(1,2*c) if c>=1 else c/2
    assert exact_tail(1)==Q(5,6)
    assert exact_tail(2)==Q(1,6)
    assert exact_tail(3)==Q(1,54)
    assert Q(2)*(Q(5,6)+Q(3,16))-Q(5,6)==Q(29,24)
    print('PASS: cases=',len(cases),'exact rational update steps=',total,
          'first_switch_tail=',exact_tail(1),
          'second_switch_tail=',exact_tail(2),
          'third_switch_tail=',exact_tail(3))
