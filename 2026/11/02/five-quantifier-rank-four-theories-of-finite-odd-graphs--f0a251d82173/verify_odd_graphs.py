"""Reproducible exact finite checks for bounded-depth theories of odd graphs.

No finite experiment is used as a proof of the uniform dimension theorem:
the uniform case follows from the inequalities established in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def orbital_signature(k):
    n = 2*k+1
    pairtypes = defaultdict(set)
    for u in range(k):
        for v in range(k):
            for w in range(k):
                low = max(0,u+v-k,u+w-k,v+w-k)
                high = min(u,v,w,u+v+w-k+1)
                for t in range(low,high+1):
                    regions = (1-k+u+v+w-t, k-u-v+t, k-u-w+t,
                               u-t, k-v-w+t, v-t, w-t, t)
                    assert min(regions)>=0
                    available = [n-sum(regions[mask] for mask in range(8)
                                       if mask & S) for S in range(8)]
                    possible = 0
                    for A in range(8):
                        rem = 7 ^ A
                        sub = rem
                        count = 0
                        while True:
                            available_count = available[A | sub]
                            if available_count>=k:
                                count += (-1)**sub.bit_count()*comb(available_count,k)
                            if sub==0: break
                            sub = (sub-1) & rem
                        pairints = ((k,u,v),(u,k,w),(v,w,k))
                        for i in range(3):
                            mask = sum(1<<j for j in range(3)
                                       if j!=i and pairints[i][j]==0)
                            if mask==A: count-=1
                        assert count>=0
                        if count: possible|=1<<A
                    atom = (u==0,v==0,w==0)
                    pairtypes[u].add((atom,possible))
    return {u:(u==0, frozenset(pairtypes[u])) for u in range(k)}


def direct_signature(k):
    n = 2*k+1
    vertices = [sum(1<<i for i in s) for s in combinations(range(n),k)]
    size = len(vertices)
    universe=(1<<size)-1
    neighbors=[]
    for x in vertices:
        neighbors.append(sum(1<<j for j,y in enumerate(vertices) if x & y==0))
    X=vertices[0]
    reps={}
    for j,Y in enumerate(vertices):
        if j: reps.setdefault((X&Y).bit_count(),j)
    answer={}
    for u,j in sorted(reps.items()):
        types=set()
        for h,Z in enumerate(vertices):
            if h in (0,j):continue
            atom=((X&vertices[j])==0,(X&Z)==0,(vertices[j]&Z)==0)
            neigh=(neighbors[0],neighbors[j],neighbors[h])
            possible=0
            for A in range(8):
                matching=universe
                for t,mask in enumerate(neigh):
                    matching &= mask if A>>t&1 else universe^mask
                matching &= universe^((1<<0)|(1<<j)|(1<<h))
                if matching:possible|=1<<A
            types.add((atom,possible))
        answer[u]=(u==0,frozenset(types))
    return answer


def profile(k,u):
    categories = ([0], range(1,k-1), [k-1])
    return tuple(''.join('1' if any(
        abs(v-w)<=k-u and k-u-1<=v+w<=k+u
        for v in categories[i] for w in categories[j]
    ) else '0' for j in range(3)) for i in range(3))


def main():
    prior=[]
    for k in range(1,13):
        orbital=orbital_signature(k)
        root=frozenset(orbital.values())
        expected=min(k,5)
        assert len(root)==expected,(k,len(root),expected)
        if k<=6:
            direct=direct_signature(k)
            assert orbital==direct,(k,'independent vertex calculation differs')
            print(f'DIRECT_ORBIT_AGREEMENT k={k} vertices={comb(2*k+1,k)}')
        if k>=6:
            assert root==prior[-1],k
        prior.append(root)
        print(f'RANK4_TYPES k={k} count={len(root)}')
    for k in range(5,61):
        rows=[profile(k,u) for u in range(k)]
        assert rows[0]==profile(5,0)
        assert rows[1]==profile(5,1)
        assert all(rows[u]==profile(5,2) for u in range(2,k-2))
        assert rows[k-2]==profile(5,3)
        assert rows[k-1]==profile(5,4)
        assert len(set(rows))==5
    print('PROFILE_CROSSCHECK k=5..60')
    print('EXACT_FINITE_CHECKS_OK')

if __name__=='__main__':main()
