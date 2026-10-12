from itertools import combinations, permutations
from collections import Counter, defaultdict
from fractions import Fraction


def pairs(n):
    return list(combinations(range(n), 2))


def outsets(n, mask):
    out=[set() for _ in range(n)]
    for k,(i,j) in enumerate(pairs(n)):
        if (mask>>k)&1:
            out[i].add(j)
        else:
            out[j].add(i)
    return out


def copeland_degree(out):
    ds=[len(s) for s in out]
    m=max(ds)
    return frozenset(i for i,d in enumerate(ds) if d==m)


def copeland_matrix(out):
    n=len(out)
    score=[]
    for i in range(n):
        s=0
        for j in range(n):
            if j!=i and j in out[i]:
                s += 1
        score.append(s)
    m=max(score)
    return frozenset(i for i,s in enumerate(score) if s==m)


def uncovered_cover(out):
    # x covers y iff x beats y and every vertex beaten by y is also beaten by x.
    n=len(out)
    covered=[False]*n
    for y in range(n):
        for x in range(n):
            if x==y: continue
            if y in out[x] and out[y] <= out[x]:
                covered[y]=True
                break
    return frozenset(i for i,c in enumerate(covered) if not c)


def uncovered_kings(out):
    # In a tournament the uncovered vertices are precisely the 2-kings.
    n=len(out)
    ans=[]
    for v in range(n):
        reach={v}|set(out[v])
        for u in out[v]:
            reach |= out[u]
        if len(reach)==n:
            ans.append(v)
    return frozenset(ans)


def top_cycle(out):
    n=len(out)
    ans=[]
    for v in range(n):
        reach={v}
        frontier=[v]
        while frontier:
            a=frontier.pop()
            for b in out[a]:
                if b not in reach:
                    reach.add(b); frontier.append(b)
        if len(reach)==n:
            ans.append(v)
    return frozenset(ans)


def permute_mask(n, mask, p):
    out=outsets(n,mask)
    op=[set() for _ in range(n)]
    for i in range(n):
        for j in out[i]:
            op[p[i]].add(p[j])
    res=0
    for k,(i,j) in enumerate(pairs(n)):
        if j in op[i]: res |= 1<<k
    return res


def canonical(n,mask):
    return min(permute_mask(n,mask,p) for p in permutations(range(n)))


def orbit(n,mask):
    return {permute_mask(n,mask,p) for p in permutations(range(n))}


def oriented_edges(n,mask):
    out=outsets(n,mask)
    return tuple((i,j) for i in range(n) for j in sorted(out[i]) if i<j or j<i)


# Exhaustive verification.
summary={}
for n in range(1,6):
    m=n*(n-1)//2
    diff=[]
    unique_c=[]
    decisive=[]
    for mask in range(1<<m):
        out=outsets(n,mask)
        c1=copeland_degree(out)
        c2=copeland_matrix(out)
        assert c1==c2
        u1=uncovered_cover(out)
        u2=uncovered_kings(out)
        assert u1==u2
        # Classical containment, independently checked.
        assert c1 <= u1
        if c1 != u1:
            diff.append(mask)
        if len(c1)==1:
            unique_c.append(mask)
            if c1 != u1:
                decisive.append(mask)
    summary[n]=(1<<m,len(diff),len(unique_c),len(decisive))

assert summary == {
    1:(1,0,1,0),
    2:(2,0,2,0),
    3:(8,0,6,0),
    4:(64,24,32,0),
    5:(1024,640,600,280),
}, summary

# First set-level disparity at 4: all are (2,3) and one isomorphism class.
n=4
first4=[]
for mask in range(1<<(n*(n-1)//2)):
    out=outsets(n,mask); c=copeland_degree(out); u=uncovered_cover(out)
    if c!=u:
        first4.append(mask)
        assert (len(c),len(u))==(2,3)
assert len(first4)==24
can4=defaultdict(list)
for mask in first4: can4[canonical(4,mask)].append(mask)
assert len(can4)==1
canon4=next(iter(can4))
assert len(orbit(4,canon4))==24

# First decisive disparity at 5: unique Copeland winner but a larger uncovered set.
n=5
dec=[]
by_uc=Counter()
for mask in range(1<<(n*(n-1)//2)):
    out=outsets(n,mask); c=copeland_degree(out); u=uncovered_cover(out)
    if len(c)==1 and c!=u:
        dec.append(mask)
        by_uc[len(u)] += 1
        assert sorted(len(x) for x in out)==[1,2,2,2,3]
        assert top_cycle(out)==frozenset(range(5))
assert len(dec)==280
assert by_uc==Counter({3:120,4:120,5:40}), by_uc
assert Fraction(len(dec),1024)==Fraction(35,128)
assert Fraction(len(dec),600)==Fraction(7,15)

classes=defaultdict(list)
for mask in dec: classes[canonical(5,mask)].append(mask)
assert len(classes)==3
class_data=[]
for can,masks in sorted(classes.items()):
    orb=len(orbit(5,can))
    out=outsets(5,can); c=copeland_degree(out); u=uncovered_cover(out)
    assert set(masks)==orbit(5,can)
    class_data.append((can,orb,tuple(sorted(c)),tuple(sorted(u)),tuple(len(x) for x in out),tuple(sorted(len(x) for x in out))))
assert sorted(x[1] for x in class_data)==[40,120,120]
assert sorted(len(x[3]) for x in class_data)==[3,4,5]

# Canonical masks and exact sets are fixed to catch canonicalization drift.
assert [x[0] for x in class_data]==[12,40,41], class_data
expected={
    12:(120,(4,),(0,2,4),(2,1,2,2,3)),
    40:(40,(4,),(0,1,2,3,4),(1,2,2,2,3)),
    41:(120,(4,),(0,2,3,4),(2,1,2,2,3)),
}
for can,orb,c,u,degs,_ in class_data:
    assert (orb,c,u,degs)==expected[can]

print('VERIFY_OK')
print('summary n:(total,diff,unique_copeland,unique_copeland_diff)',summary)
print('n4_diff',len(first4),'n4_classes',len(can4),'canon',canon4,'orbit',len(orbit(4,canon4)))
print('n5_unique_copeland',600)
print('n5_decisive_diff',len(dec),'unconditional','35/128','conditional_unique','7/15')
print('n5_uc_size_hist',dict(sorted(by_uc.items())))
print('n5_classes',[(c,o,C,U,d) for c,o,C,U,d,_ in class_data])
