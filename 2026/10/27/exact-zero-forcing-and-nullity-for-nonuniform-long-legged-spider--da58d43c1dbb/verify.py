#!/usr/bin/env python3
"""Exact integer verification for graph-power spider nullity and forcing witnesses."""
from itertools import combinations, product


def instances(lengths, power):
    arms = [[(i, a) for a in range(1, length + 1)] for i, length in enumerate(lengths)]
    names = [('c', 0)] + [x for arm in arms for x in arm]
    pos = {v: t for t, v in enumerate(names)}
    def dist(u, v):
        if u == v:
            return 0
        if u[0] == 'c':
            return v[1]
        if v[0] == 'c':
            return u[1]
        if u[0] == v[0]:
            return abs(u[1] - v[1])
        return u[1] + v[1]
    n = len(names)
    adjacency = [[int(0 < dist(u, v) <= power) for v in names] for u in names]
    X = [[0] * n for _ in range(n)]
    for i, li in enumerate(lengths):
        for a in range(1, li + 1):
            p = pos[(i,a)]
            X[0][p] = X[p][0] = int(a <= power)
            for j, lj in enumerate(lengths):
                for b in range(1, lj + 1):
                    q = pos[(j,b)]
                    C = int(a+b <= power)
                    if i != j:
                        X[p][q] = C
                    else:
                        RGram = sum(int(s <= a <= s+power and s <= b <= s+power)
                                    for s in range(1, li-power+1))
                        X[p][q] = RGram+C
    for p in range(n):
        for q in range(n):
            if p != q:
                assert (X[p][q] != 0) == bool(adjacency[p][q]), (lengths, power, p, q)
            assert X[p][q] == X[q][p]
    # Basis for each sliding-window nullspace, given independent initial values.
    W = []
    for li in lengths:
        b = []
        for t in range(power):
            vec = [int(j == t) for j in range(power)]
            for j in range(power, li):
                vec.append(-sum(vec[j-power:j]))
            assert len(vec) == li
            assert all(sum(vec[s:s+power+1]) == 0 for s in range(li-power))
            b.append(vec)
        W.append(b)
    vectors=[]
    m=len(lengths)
    for i in range(m-1):
        for t in range(power):
            v=[0]*n
            for arm,sign in [(i,1),(m-1,-1)]:
                for a,z in enumerate(W[arm][t],1):
                    v[pos[(arm,a)]] += sign*z
            assert all(sum(row[j]*v[j] for j in range(n)) == 0 for row in X)
            vectors.append(v)
    # Independent because the first 'power' entries on the first m-1 arms
    # are the standard basis, ordered by (arm,initial coordinate).
    for i in range(m-1):
        for t in range(power):
            for j in range(m-1):
                for s in range(power):
                    assert vectors[i*power+t][pos[(j,s+1)]] == int(i==j and t==s)
    initial = {pos[(i,a)] for i,li in enumerate(lengths[:-1])
               for a in range(li-power+1,li+1)}
    assert len(initial)==(m-1)*power
    forces=[]
    for i,li in enumerate(lengths[:-1]):
        for a in range(li-power,0,-1):
            forces.append(((i,a+power),(i,a)))
    forces.append(((0,power),('c',0)))
    for a in range(1,power):
        forces.append(((0,power-a),(m-1,a)))
    forces.append((('c',0),(m-1,power)))
    for a in range(power+1,lengths[-1]+1):
        forces.append(((m-1,a-power),(m-1,a)))
    black=set(initial)
    for u,v in forces:
        p,q=pos[u],pos[v]
        assert p in black and q not in black, (lengths,power,'state',u,v)
        white_neighbors=[z for z in range(n) if adjacency[p][z] and z not in black]
        assert white_neighbors == [q], (lengths,power,'forcing',u,v,white_neighbors)
        black.add(q)
    assert len(black)==n
    return n, len(vectors),len(forces), adjacency


def exhaustive_small(adjacency, expected):
    n=len(adjacency)
    masks=[sum((1<<j) for j in range(n) if row[j]) for row in adjacency]
    full=(1<<n)-1
    def closure(init):
        black=init
        while True:
            added=0
            for i in range(n):
                if (black>>i)&1:
                    white=masks[i]&(~black)
                    if white and not white&(white-1):
                        added|=white
            if not added:
                return black==full
            black|=added
    for s in range(expected):
        for tup in combinations(range(n),s):
            if closure(sum(1<<t for t in tup)):
                raise AssertionError(('smaller zero-forcing set',n,expected,tup))


def main():
    checked=0; null_vectors=0; moves=0; exhaustive=0
    examples=[]
    for m in range(2,6):
        for k in range(1,5):
            examples.extend([
                (tuple(k+1+(i%3) for i in range(m)),k),
                (tuple(k+1+(2*i+1)%4 for i in range(m)),k),
                (tuple(k+1+(m-i)%2 for i in range(m)),k),
            ])
    for lengths,k in examples:
        n,d,f,A=instances(lengths,k)
        checked+=1;null_vectors+=d;moves+=f
    for lengths,k in [((2,3),1),((2,3,4),1),((3,4,5),2),((3,3,4),2),((4,5),3),((4,4,5),3)]:
        n,d,f,A=instances(lengths,k)
        if n<=13:
            exhaustive_small(A,d)
            exhaustive+=1
    print('VERIFY_OK', 'heterogeneous_cases='+str(checked),
          'explicit_null_vectors='+str(null_vectors),
          'verified_forces='+str(moves),'exhaustive_cases='+str(exhaustive))


if __name__=='__main__':
    main()
