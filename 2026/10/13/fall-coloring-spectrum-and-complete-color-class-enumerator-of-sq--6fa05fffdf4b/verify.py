#!/usr/bin/env python3
"""Exact finite-state and direct-coloring checks for the cycle-square fall-coloring theorem."""
from itertools import product
from math import factorial

Q = [(a,b,c,d) for a,b,c,d in product(range(4), repeat=4)
     if len({a,b,c}) == 3 and len({b,c,d}) == 3]
assert len(Q) == 48
position = {q: k for k, q in enumerate(Q)}
out = [[] for _ in Q]
for i, (a,b,c,d) in enumerate(Q):
    for e in range(4):
        if e not in (c,d) and len({a,b,c,d,e}) == 4:
            out[i].append(position[(b,c,d,e)])
assert sorted({len(v) for v in out}) == [1,2]

def multiply_by_T(P):
    R = [[0]*48 for _ in range(48)]
    for i,row in enumerate(P):
        target = R[i]
        for j,val in enumerate(row):
            if val:
                for k in out[j]:
                    target[k] += val
    return R

P = [[int(i==j) for j in range(48)] for i in range(48)]
traces = [48]
for n in range(1,65):
    P = multiply_by_T(P)
    traces.append(sum(P[i][i] for i in range(48)))

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return r

factors=[([1,-1],5),([1,-1,-1],1),([1,1,1],4),
         ([1,-1,0,1],3),([1,1,0,1],2),
         ([1,1,2,2,1,0,1],3)]
D=[1]
for poly,powr in factors:
    for _ in range(powr): D=mul(D,poly)
assert len(D)==49
# Newton identities give det(I - t T), independently of symbolic factorization.
c=[1]
for k in range(1,49):
    s=sum(c[k-j]*traces[j] for j in range(1,k+1))
    assert s%k==0
    c.append(-s//k)
assert c==D,(c,D)

def direct_four(word):
    n=len(word)
    return all(word[i]!=word[(i+d)%n] for i in range(n) for d in (1,2)) and all(
        len({word[(i+d)%n] for d in range(5)})==4 for i in range(n))

def count_by_direct(n):
    # S_4 acts freely: any labeled four-color fall coloring has 24
    # relabelings and unique representative starting (0,1,2).
    count=0
    def visit(word):
        nonlocal count
        if len(word)==n:
            count+=direct_four(word)
            return
        for x in range(4):
            if x!=word[-1] and x!=word[-2]:
                visit(word+[x])
    visit([0,1,2])
    return 24*count

for n in range(7,17):
    assert count_by_direct(n)==traces[n], (n,count_by_direct(n),traces[n])
for n in range(7,65):
    assert (traces[n]==0)==(n in (7,11)), (n,traces[n])
for n,word in {8:'01203123',9:'012031023',10:'0120310213',15:'012031021320123'}.items():
    assert len(word)==n and direct_four([int(x) for x in word])
assert traces[8:16]==[168,72,120,0,744,312,840,480]
for n in range(7,65):
    assert traces[n]%factorial(4)==0
print('VERIFY_OK states=48 characteristic_degree=48 matrix_trace_orders=1..64'
      ' independently_bruteforced_orders=7..16 exceptional_orders=7,11'
      ' witnesses=8,9,10,15')
