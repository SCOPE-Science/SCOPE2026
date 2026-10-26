#!/usr/bin/env python3
"""Exact checks for GH excitation on wheel graphs; standard Python only."""
from itertools import product
from collections import Counter
from fractions import Fraction


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def tracepower(A, n):
    Z=eye(len(A))
    for _ in range(n):Z=mm(Z,A)
    return sum(Z[i][i] for i in range(len(A)))

def charpoly(A):
    # Faddeev–LeVerrier; coefficients of det(tI-A) over exact rationals
    N=len(A); B=eye(N); out=[1]
    for k in range(1,N+1):
        D=mm(A,B)
        c=-Fraction(sum(D[i][i] for i in range(N)),k)
        assert c.denominator==1
        out.append(int(c))
        B=[[D[i][j]+(c if i==j else 0) for j in range(N)] for i in range(N)]
    return out

def matrices():
    pairs=list(product(range(3),repeat=2))
    P=[[0]*9 for _ in range(9)]
    for j,(a,b) in enumerate(pairs):
        for c in range(3):
            allowed = b==2 or (b==0 and (a==1 or c==1)) or (b==1 and (a==2 or c==2))
            if allowed:P[j][pairs.index((b,c))]=1
    B=[[int(not ((a,b) in ((1,2),(2,1)))) for b in range(3)] for a in range(3)]
    return P,B

def update(s):
    hub, *rim=s
    n=len(rim)
    h2=2 if hub==1 else 0 if hub==2 else int(1 in rim)
    return (h2,)+tuple(
        (z+1)%3 if z else int(hub==1 or rim[(j-1)%n]==1 or rim[(j+1)%n]==1)
        for j,z in enumerate(rim))

def direct(n):
    # Exhaustive state graph, no external dynamics theorem assumed.
    state=list(product(range(3), repeat=n+1))
    nexts={s:update(s) for s in state}
    group={}; num_cycles=Counter(); recurrent={}; failed=0
    for s in state:
        if s in group:continue
        path=[];lookup={}; cur=s
        while cur not in group and cur not in lookup:
            lookup[cur]=len(path);path.append(cur);cur=nexts[cur]
        if cur in lookup:
            cycle=path[lookup[cur]:]
            period=len(cycle)
            num_cycles[period]+=1
            recurrent[cur]=period
            if period not in (1,3):failed+=1
            label=period
        else:
            label=group[cur]
        for x in path:group[x]=label
    return num_cycles, Counter(group.values()), failed

def main():
    P,B=matrices()
    # Explicit expected x^4 (x^2+x+1)(x^3-2x^2-1)
    exp=[1]
    for q in ([1,1,1], [1,-2,0,-1],[1,0,0,0,0]):
        exp=[sum(exp[i]*q[j] for i in range(len(exp)) for j in range(len(q)) if i+j==k)
             for k in range(len(exp)+len(q)-1)]
    assert charpoly(P)==exp,(charpoly(P),exp)
    assert charpoly(B)==[1,-3,1,1] # (x-1)(x^2-2x-1)
    s=[3,2,4]
    for n in range(3,15):s.append(2*s[n-1]+s[n-3])
    pell=[2,2]
    for n in range(2,15):pell.append(2*pell[n-1]+pell[n-2])
    print('char_P',charpoly(P))
    print('char_B',charpoly(B))
    for n in range(3,11):
        periodic_cycles=s[n]+(2 if n%3==0 else -1)-1
        extinct=3*(pell[n]+1)
        assert periodic_cycles==tracepower(P,n)-1
        assert extinct==3*tracepower(B,n)
        cycles, basin, bad=direct(n)
        assert bad==0,(n,cycles)
        assert cycles==Counter({1:1,3:periodic_cycles}),(n,cycles,periodic_cycles)
        assert basin[1]==extinct,(n,basin,extinct)
        assert basin[3]==3**(n+1)-extinct
        print(f'n={n} states={3**(n+1)} fixed_basin={extinct} 3_cycles={periodic_cycles} 3cycle_basin={basin[3]}')
    print('all exact checks PASS')
if __name__=='__main__':main()
