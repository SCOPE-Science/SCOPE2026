"""Finite sanity checks for the path-power C2 identification threshold.
No finite test replaces the all-parameter proof in RESULT.md.
Requires only Python 3 standard library.
"""
from collections import Counter

def edges(n,k):
    return {frozenset((i,j)) for i in range(n) for j in range(i+1,n) if j-i<=k}

def modified(n,k):
    E=edges(n,k).copy()
    a=frozenset((0,2)); b=frozenset((n-1,n-3))
    c=frozenset((0,n-3)); d=frozenset((n-1,2))
    assert a in E and b in E and c not in E and d not in E
    E.difference_update((a,b)); E.update((c,d))
    return E

def adj(n,E):
    a=[[] for _ in range(n)]
    for e in E:
        u,v=tuple(e);a[u].append(v);a[v].append(u)
    return a

def colours(n,E,F):
    X=adj(n,E);Y=adj(n,F)
    c=[[0]*n,[0]*n]
    for t in range(n+2):
        types=[]
        for a,old in ((X,c[0]),(Y,c[1])):
            types.extend((old[i],tuple(sorted(Counter(old[j] for j in a[i]).items()))) for i in range(n))
        names={z:i for i,z in enumerate(sorted(set(types)))}
        nxt=[[names[x] for x in types[:n]],[names[x] for x in types[n:]]]
        assert Counter(nxt[0]) == Counter(nxt[1]), (n,t)
        if nxt==c:return c,t
        c=nxt
    raise AssertionError('no stabilization')

def triangle_witness(n,E):
    cells=[(i,n-1-i) for i in range(3)]
    return sum(all(frozenset((x,y)) in E for x,y in ((a,b),(a,c),(b,c)))
               for a in cells[0] for b in cells[1] for c in cells[2])

def partition_degree(n,k):
    e=edges(n,k);d=[sum(i in x for x in e) for i in range(n)]
    if n<=k+1:
        assert len(set(d))==1 and d[0]==n-1;return
    t=n-k-1
    assert 1<=t<=3
    assert all(d[i]==d[n-1-i]==k+i for i in range(t))
    assert all(d[i]==n-1 for i in range(t,n-t))
    assert len(set(d))==t+(n>2*t)
    for i in range(t):
        for j in range(i+1,t):
            values=[sum(frozenset((x,y)) in e for y in (j,n-1-j)) for x in (i,n-1-i)]
            target=2 if i+j>=t else 1
            assert values==[target,target],(n,k,i,j)
    matching=[(i,j) for i in range(t) for j in range(i+1,t) if i+j<t]
    assert len(matching)<=t-1,matching

small=large=0
for k in range(1,25):
    for n in range(1,85):
        if k==1 or n<=k+4:
            if k>=2:partition_degree(n,k)
            small+=1
        else:
            E=edges(n,k);F=modified(n,k)
            c,_=colours(n,E,F)
            for i in range(3):
                assert c[0][i]==c[0][n-1-i] and c[0][i]!=c[0][(i+1)%3]
            assert triangle_witness(n,E)==2 and triangle_witness(n,F)==0
            large+=1
print('VERIFY_OK',{'nonexceptional_parameter_tests':small,'twist_ambiguity_tests':large,'smallest_obstruction':(7,2)})
