"""Exact bounded-rank logic computation on finite set-partition posets.
Independent symbolic extension-table tests supplement a general proof.
No third-party packages are required. Run: python3 verify_partition_rank3.py.
"""
import collections
import hashlib
import random


def all_partitions(n):
    a=[(0,)]
    for _ in range(1,n):
        a=[x+(b,) for x in a for b in range(max(x)+2)]
    return a


def partition_masks(partitions):
    n=len(partitions[0]); out=[]
    for a in partitions:
        p=0;bit=0
        for i in range(n):
            for j in range(i+1,n):
                if a[i]==a[j]:p |= 1<<bit
                bit+=1
        out.append(p)
    return out


def relations(M):
    N=len(M);high=[0]*N;low=[0]*N
    for i,mi in enumerate(M):
        row=0
        for j,mj in enumerate(M):
            if mi & mj == mi:
                row |= 1<<j
                low[j] |= 1<<i
        high[i]=row
    full=(1<<N)-1
    cat=[(1<<i,low[i]^(1<<i),high[i]^(1<<i),full^(low[i]|high[i])) for i in range(N)]
    return low,high,cat


def pair_relation(i,j,low,high):
    if i==j:return 0
    if high[i]>>j&1:return 1
    if low[i]>>j&1:return 2
    return 3


def actual_extension(i,j,cat):
    mask=0
    for a in range(4):
        for b in range(4):
            if cat[i][a]&cat[j][b]:mask|=1<<(4*a+b)
    return mask


def table_extension(i,j,low,high,r,c):
    rel=pair_relation(i,j,low,high)
    s=set()
    if rel==0:
        s.add((0,0))
        if r[i]:s.add((1,1))
        if c[i]:s.add((2,2))
        if r[i] and c[i]:s.add((3,3))
    elif rel==1:
        s.update(((0,1),(2,0)))
        if r[i]:s.update(((1,1),(3,1)))
        if c[j]:s.update(((2,2),(2,3)))
        if r[j]-r[i]>=2:s.add((2,1))
        if r[i] and c[j]:s.add((3,3))
    elif rel==2:
        return sum(1<<(4*b+a) for a,b in unpack(table_extension(j,i,low,high,r,c)))
    else:
        s.update(((0,3),(3,0),(1,1),(2,2),(3,3)))
        if r[i]>=2:s.add((1,3))
        if c[i]>=2:s.add((2,3))
        if r[j]>=2:s.add((3,1))
        if c[j]>=2:s.add((3,2))
    return sum(1<<(4*a+b) for a,b in s)


def unpack(mask):
    return ((a,b) for a in range(4) for b in range(4) if mask>>(4*a+b)&1)


def run(n):
    parts=all_partitions(n);N=len(parts)
    M=partition_masks(parts)
    low,high,cat=relations(M)
    r=[n-len(set(a)) for a in parts]
    c=[len(set(a))-1 for a in parts]
    # Full tests through n=7; deterministic stratified sample at n=8.
    if n<=7:
        indices=((i,j) for i in range(N) for j in range(N))
    else:
        rng=random.Random(20260827)
        indices=((rng.randrange(N),rng.randrange(N)) for _ in range(50000))
    tests=0
    for i,j in indices:
        got=actual_extension(i,j,cat)
        expected=table_extension(i,j,low,high,r,c)
        if got!=expected:
            raise AssertionError(('extension_table',n,i,j,got,expected))
        tests+=1
    # Rank-2 rooted types: all second moves, and each possible third-move profile.
    # Only one representative per S_n-orbit on partitions is needed.
    reps={}
    for i,a in enumerate(parts):
        reps.setdefault(tuple(sorted(collections.Counter(a).values())),i)
    root_profiles={}
    for shape,i in reps.items():
        root_profiles[shape]=frozenset(
            (pair_relation(i,j,low,high),actual_extension(i,j,cat))
            for j in range(N))
    ranktypes={}
    for shape,profile in root_profiles.items():
        i=reps[shape]
        ranktypes.setdefault(profile,set()).add((min(r[i],3),min(c[i],3)))
    assert len(ranktypes)==len(set((min(r[i],3),min(c[i],3)) for i in reps.values()))
    assert all(len(cases)==1 for cases in ranktypes.values())
    theory=frozenset(root_profiles.values())
    print('n=%d Bell=%d pair_table_tests=%d rooted_types=%d theory_hash=%s' %
          (n,N,tests,len(theory),hashlib.sha256(repr(sorted(map(lambda x:sorted(x),theory))).encode()).hexdigest()[:12]))
    return theory


def main():
    theories={n:run(n) for n in range(1,9)}
    assert len(set(theories.values()))==7
    assert theories[7]==theories[8]
    for n in range(1,7):
        assert theories[n]!=theories[n+1]
    print('PASS: exact pair-extension table (n<=7), sampled at n=8; exact rank-three classes through n=8')
    print('NOTE: all n>=7 equivalence requires the independent symbolic proof, not finite checking')
if __name__=='__main__': main()
