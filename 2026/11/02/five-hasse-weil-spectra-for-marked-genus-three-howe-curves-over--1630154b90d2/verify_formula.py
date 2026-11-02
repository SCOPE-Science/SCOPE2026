"""Exact pure-Python F9 census for a genus-three palindromic octic family.
Elements a+bi, i^2=2 in F3, encoded a+3b.
"""
from collections import Counter

def plus(x,y):
    return ((x%3+y%3)%3) + 3*((x//3+y//3)%3)

def minus(x,y):
    return ((x%3-y%3)%3) + 3*((x//3-y//3)%3)

def times(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c+2*b*d)%3) + 3*((a*d+b*c)%3)

def power(x,n):
    z=1
    while n:
        if n&1:z=times(z,x)
        x=times(x,x);n//=2
    return z

assert {power(x,2) for x in range(1,9)}=={1,2,3,6}
squares={power(x,2) for x in range(1,9)}
def character(t):return 0 if t==0 else (1 if t in squares else -1)

def trace_quartic(A,B,k):
    s=0
    for u in range(9):
        u2=power(u,2)
        if k==0:
            rhs=times(minus(u2,minus(A,1)),minus(u2,minus(B,1)))
        elif k==1:
            rhs=times(minus(u2,plus(A,1)),minus(u2,plus(B,1)))
        elif k==2:
            rhs=times(plus(minus(u2,times(A,u)),1),plus(minus(u2,times(B,u)),1))
        else:raise ValueError(k)
        s+=character(rhs)
    # quartic has two rational points above infinity, leading coefficient 1
    return -1-s

def count_curve(A,B):
    s=0
    for x in range(9):
        z=power(x,2); q=power(x,4)
        s+=character(times(plus(minus(q,times(A,z)),1),
                           plus(minus(q,times(B,z)),1)))
    return 11+s

zeta=Counter(); points=Counter(); rank=Counter(); ordered=[]
for A in range(9):
    for B in range(9):
        if A in (1,2) or B in (1,2) or A==B:continue
        ts=tuple(sorted(trace_quartic(A,B,k) for k in range(3)))
        zeta[ts]+=1
        N=count_curve(A,B)
        assert N==10-sum(ts),(A,B,N,ts)
        points[N]+=1
        s=plus(A,B); c=plus(times(A,B),2)
        ordinary=(s not in (1,2) and c!=0)
        p_rank=3 if ordinary else 2
        rank[p_rank]+=1
        assert p_rank==sum(t%3!=0 for t in ts)
        ordered.append((A,B,ts))
assert len(ordered)==42
assert zeta==Counter({(-6,-2,-2):6,(-6,2,2):4,(-2,-2,2):12,
                     (-2,-2,6):8,(-2,2,2):12}),zeta
assert points==Counter({8:20,12:16,20:6}),points
assert rank==Counter({2:18,3:24}),rank
# For every q=3^n, q>=9, elementary counting gives (q-2)(q-3) smooth,
# 3(q-3) nonordinary and (q-3)(q-5) ordinary ordered pairs.
print('FORMULA_VERIFY_OK: 42 triples, five zeta types, p-rank (2:18,3:24), N9 (8:20,12:16,20:6)')
