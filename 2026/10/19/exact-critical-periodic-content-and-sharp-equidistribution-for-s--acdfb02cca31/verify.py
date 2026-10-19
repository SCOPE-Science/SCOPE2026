"""Standalone finite checks for constrained star-shift periodic orbit theorem.
Uses Python standard library only. Run: python verify.py
Finite checks complement rather than certify the universal analytic proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def allowed(w):
    return all(x == 0 or y == 0 for x, y in zip(w, w[1:]))


def trace(n, q):
    # lambda^n + tau^n obeys P_0=2, P_1=1, P_n=P_(n-1)+q P_(n-2).
    a, b = 2, 1
    for _ in range(n):
        a, b = b, b + q*a
    return a


def graph(n, q):
    assert n >= 2
    verts = [w for w in product(range(q+1), repeat=n-1) if allowed(w)]
    edge_at = defaultdict(list)
    good = set()
    for w in product(range(q+1), repeat=n):
        if not allowed(w):
            continue
        if w[0] and w[-1]:
            continue
        u, v = w[:-1], w[1:]
        assert u in verts and v in verts
        edge_at[u].append((v,w))
        good.add(w)
    return verts, edge_at, good


def euler_cycle(n, q):
    verts, edges, good = graph(n,q)
    for v in verts:
        degree_out = len(edges[v])
        degree_in = sum(1 for w in good if w[1:] == v)
        assert degree_out == degree_in and degree_out > 0, (n,q,v)
    # Iterative Hierholzer traversal with labeled edges.
    graphcopy = {v:list(e) for v,e in edges.items()}
    start = tuple([0]*(n-1))
    stack=[(start,None)]
    visited=[]
    while stack:
        v, lab=stack[-1]
        if graphcopy[v]:
            nextv, word=graphcopy[v].pop()
            stack.append((nextv,word))
        else:
            stack.pop()
            if lab is not None:
                visited.append(lab)
    visited.reverse()
    assert len(visited)==len(good)
    assert set(visited)==good
    assert all(visited[i][1:]==visited[(i+1)%len(visited)][:-1] for i in range(len(visited)))
    cyc=tuple(w[0] for w in visited)
    windows=[tuple(cyc[(i+j)%len(cyc)] for j in range(n)) for i in range(len(cyc))]
    assert windows==visited and len(set(windows)) == len(cyc)
    return cyc


def check(q,n):
    cyc=euler_cycle(n,q)
    assert len(cyc)==trace(n,q)
    counts=[Counter(tuple(cyc[(i+j)%len(cyc)] for j in range(k)) for i in range(len(cyc))) for k in (n-1,n)]
    assert max(counts[1].values())==1
    assert max(counts[0].values())>=2
    # Exact empirical cylinders compared to transfer matrix powers.
    M=q+1
    A=[[int(i==0 or j==0) for j in range(M)] for i in range(M)]
    def mul(A,B):
        return [[sum(A[i][t]*B[t][j] for t in range(M)) for j in range(M)] for i in range(M)]
    def mpow(k):
        z=[[int(i==j) for j in range(M)] for i in range(M)]
        for _ in range(k):z=mul(z,A)
        return z
    for k in range(1,min(n,5)+1):
        counts=Counter(tuple(cyc[(i+j)%len(cyc)] for j in range(k)) for i in range(len(cyc)))
        P=mpow(n-k+1)
        for u in product(range(M), repeat=k):
            expected=P[u[-1]][u[0]] if allowed(u) else 0
            assert counts[u]==expected, (q,n,u,counts[u],expected)
    return len(cyc)


def exhaustive_primitive_upper(q,n,maxperiod):
    # Small finite exhaustive check of arbitrary cyclic closed trails, including bad n-words.
    N=trace(n,q)
    for length in range(2,maxperiod+1):
        for cyc in product(range(q+1),repeat=length):
            if not allowed(cyc + cyc[:1]):continue
            if any(all(cyc[i]==cyc[(i+j)%length] for i in range(length)) for j in range(1,length)):
                continue
            windows=[tuple(cyc[(i+j)%length] for j in range(n)) for i in range(length)]
            if len(set(windows))==length:
                assert length <= N, (q,n,cyc)


def main():
    z=0
    for q in (2,3,4):
        for n in range(2,7):
            n_orbit=check(q,n)
            print('checked',q,n,'orbit=',n_orbit)
            z+=1
    for n in range(2,5):
        exhaustive_primitive_upper(2,n,8)
        z+=1
    # Exact first-coordinate cylinder bias identity for q=2 via rational matrices:
    # mu_n([0])=(2**(n+1)+(-1)**(n+1)/? recheck via recurrence exact below).
    q=2
    for n in range(2,11):
        L=trace(n,q)
        # (A^n)_{0,0} via A^0=I and A^1=A
        a,b=1,1
        for _ in range(n):
            a,b=b,b+q*a
        num=a
        mass=Fraction(num,L)
        target=Fraction(2,3)
        sign_expected=(-1)**n
        assert (mass-target)*sign_expected <= 0
    print('VERIFICATION_OK, finite combinations:',z,'plus rational spectral signs')

if __name__=='__main__':main()
