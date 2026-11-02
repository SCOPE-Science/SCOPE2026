#!/usr/bin/env python3
"""Finite checks for a preconditional T/F separation criterion.

No external dependencies. Checks the algebraic axioms directly, not using
candidate classifications as verification oracles.
"""
from itertools import product


def make_lattice(leq):
    n = len(leq)
    assert all(leq[x][x] for x in range(n))
    assert all(not (leq[x][y] and leq[y][x]) for x in range(n) for y in range(n) if x != y)
    assert all(not(leq[x][y] and leq[y][z]) or leq[x][z]
               for x in range(n) for y in range(n) for z in range(n))
    meet, join = [[None]*n for _ in range(n)], [[None]*n for _ in range(n)]
    for a, b in product(range(n), repeat=2):
        low = [x for x in range(n) if leq[x][a] and leq[x][b]]
        high = [x for x in range(n) if leq[a][x] and leq[b][x]]
        mm = [x for x in low if all(leq[y][x] for y in low)]
        jj = [x for x in high if all(leq[x][y] for y in high)]
        assert len(mm) == len(jj) == 1
        meet[a][b], join[a][b] = mm[0], jj[0]
    bottoms = [x for x in range(n) if all(leq[x][y] for y in range(n))]
    tops = [x for x in range(n) if all(leq[y][x] for y in range(n))]
    assert len(bottoms) == len(tops) == 1
    zero, one = bottoms[0], tops[0]
    atoms = [a for a in range(n) if a != zero and
             all(x in (zero, a) for x in range(n) if leq[x][a])]
    return (leq, meet, join, zero, one, atoms)


def check(lattice, tab):
    leq, meet, _, zero, one, _ = lattice
    n = len(leq)
    f = lambda a,b: tab[a][b]
    failures = []
    if any(not leq[f(one,a)][a] for a in range(n)):
        failures.append('P1')
    if any(not leq[meet[a][b]][f(a,b)] for a,b in product(range(n),repeat=2)):
        failures.append('P2')
    if any(not leq[f(a,b)][f(a,meet[a][b])] for a,b in product(range(n),repeat=2)):
        failures.append('P3')
    if any(not leq[f(a,meet[b][c])][f(a,b)] for a,b,c in product(range(n),repeat=3)):
        failures.append('P4')
    if any(not leq[f(a,f(meet[a][b],c))][f(meet[a][b],c)]
           for a,b,c in product(range(n),repeat=3)):
        failures.append('P5')
    if failures:
        return failures, False, False
    T = all(f(a,a)==one and meet[a][f(a,zero)]==zero for a in range(n))
    F = T and all(leq[a][f(f(a,zero),zero)] for a in range(n))
    return failures, T, F


def witness(lattice, p, q):
    leq, meet, _, _, one, _ = lattice
    n = len(leq)
    assert p != q and meet[p][q] == lattice[3]
    return [[one if leq[a][b] else (q if a==p else meet[a][b])
             for b in range(n)] for a in range(n)]


def count_b2():
    n = 4
    leq = [[(a&b)==a for b in range(n)] for a in range(n)]
    L = make_lattice(leq)
    assert L[5] == [1,2]
    choices=[]
    for up,uq in product((0,2),(0,1)):
        tab = [[3 if (a&b)==a else (up if a==1 else (uq if a==2 else a&b))
                for b in range(4)] for a in range(4)]
        fails,T,F = check(L,tab)
        assert not fails and T
        choices.append(((up,uq),F))
    assert len(choices)==4 and sum(f for _,f in choices)==2
    print('BOOLEAN_4_T=4_F=2', choices)


def count_chains():
    for n in range(2,4):
        leq = [[a <= b for b in range(n)] for a in range(n)]
        L = make_lattice(leq)
        Ts=Fs=0
        for entries in product(range(n), repeat=n*n):
            tab = [entries[a*n:(a+1)*n] for a in range(n)]
            _,T,F = check(L,tab)
            Ts+=T; Fs+=F
        assert Ts==Fs
        print('CHAIN',n,'T=F=',Ts)


def labeled_posets(n):
    pairs = [(i,j) for i in range(n) for j in range(n) if i!=j]
    for bits in range(1<<len(pairs)):
        leq=[[i==j for j in range(n)] for i in range(n)]
        for k,(i,j) in enumerate(pairs):
            if bits&(1<<k): leq[i][j]=True
        if any(leq[i][j] and leq[j][i] for i in range(n) for j in range(i+1,n)):
            continue
        if any(leq[i][j] and leq[j][k] and not leq[i][k] for i,j,k in product(range(n),repeat=3)):
            continue
        yield leq


def ideal_lattice(poset):
    n=len(poset)
    ideals=[bits for bits in range(1<<n) if
            all(not(bits&(1<<i)) or not poset[j][i] or (bits&(1<<j))
                for i in range(n) for j in range(n))]
    leq=[[(a&b)==a for b in ideals] for a in ideals]
    return make_lattice(leq)


def all_ideals_test():
    totals=0; nonprime=0; prime=0
    for n in range(1,5):
        for poset in labeled_posets(n):
            L=ideal_lattice(poset)
            totals+=1
            if len(L[5])>=2:
                nonprime+=1
                tab=witness(L,L[5][0],L[5][1])
                fails,T,F=check(L,tab)
                assert not fails and T and not F, (n,L[5],fails,T,F)
            else:
                prime+=1
                leq,meet,_,zero,one,_=L
                # Any semicomplement of a nonzero is forced to be zero.
                assert all(meet[a][b]!=zero for a in range(len(leq))
                           for b in range(len(leq)) if a!=zero and b!=zero)
    assert totals==1+3+19+219
    print('IDEAL_LATTICES',totals,'two_or_more_atoms',nonprime,'one_atom',prime)


def nondistributive_test():
    # M3: 0, three atoms, 1.
    n=5
    leq=[[i==j or i==0 or j==4 for j in range(n)] for i in range(n)]
    L=make_lattice(leq)
    assert len(L[5])==3
    tab=witness(L,1,2)
    assert check(L,tab)==([],True,False)
    print('M3_NONDISTRIBUTIVE_WITNESS_OK')

if __name__=='__main__':
    count_b2()
    count_chains()
    all_ideals_test()
    nondistributive_test()
    print('ALL_CHECKS_OK')
