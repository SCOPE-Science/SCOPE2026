"""Reproducible tests for the edge-trace system of labeled Hamiltonian cycles."""
import itertools,math,collections


def edge_universe(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def cycles(n):
    ed=edge_universe(n)
    ix={e:i for i,e in enumerate(ed)}
    masks=[]
    for p in itertools.permutations(range(1,n)):
        if p[0]>p[-1]:continue
        order=(0,)+p
        bits=0
        for j in range(n):
            a,b=order[j],order[(j+1)%n]
            bits|=1<<ix[tuple(sorted((a,b)))]
        masks.append(bits)
    assert len(masks)==math.factorial(n-1)//2
    assert len(masks)==len(set(masks))
    return ed,masks


def predicted_shattered(n,S,edges):
    if not S:return True
    deg=[0]*n
    adj=[[] for _ in range(n)]
    for i in S:
        a,b=edges[i]
        deg[a]+=1;deg[b]+=1
        adj[a].append(b);adj[b].append(a)
    if len(S)<=n-3:
        # Positive compatibility required in this test separately.
        return True
    if len(S)>=n-1:return False
    # Now exactly n-2 edges. Two connected components because S subset of a cycle.
    vis=set();sizes=[]
    for v in range(n):
        if v in vis:continue
        todo=[v];vis.add(v);sz=0
        while todo:
            x=todo.pop();sz+=1
            for y in adj[x]:
                if y not in vis:vis.add(y);todo.append(y)
        sizes.append(sz)
    assert len(sizes)==2
    a,b=sorted(sizes)
    return (a==1 and b>=4) or (a>=4)


def observed_shattered(S,cycle_masks):
    ns=len(S);full=(1<<ns)-1
    pat=set()
    for c in cycle_masks:
        pat.add(sum(1<<j for j,e in enumerate(S) if (c>>e)&1))
        if len(pat)==1<<ns:return True
    return False


def exhaustive_supports(n):
    edges,C=cycles(n)
    supports=set()
    for c in C:
        inds=[i for i in range(len(edges)) if (c>>i)&1]
        for k in range(n+1):
            for x in itertools.combinations(inds,k):supports.add(x)
    tested=0;shattered=0;counts=collections.Counter()
    for S in sorted(supports):
        actual=observed_shattered(S,C)
        pred=predicted_shattered(n,S,edges)
        assert pred==actual,(n,S,actual,pred)
        tested+=1
        if actual:
            shattered+=1;counts[len(S)]+=1
    # Supports not contained in any cycle have all-positive impossibility.
    d=max(counts)
    assert d==({3:0,4:1}.get(n,n-2))
    print('EXHAUSTIVE',n,'cycles',len(C),'compatible_supports',tested,
          'shattered',shattered,'vc',d,'by_size',dict(sorted(counts.items())))
    return dict(sorted(counts.items()))


def representative_two_component(n):
    ed,C=cycles(n)
    ix={e:i for i,e in enumerate(ed)}
    results=[]
    for a in range(1,n//2+1):
        b=n-a
        S=[]
        for grp in (list(range(a)),list(range(a,n))):
            for i,j in zip(grp,grp[1:]):S.append(ix[(i,j)])
        actual=observed_shattered(S,C)
        pred=predicted_shattered(n,S,ed)
        assert pred==actual,(n,a,b,actual,pred)
        results.append(((a,b),actual))
    print('CANONICAL',n,'concepts',len(C),'two_path_shapes',results)


def main():
    for n in range(3,8):exhaustive_supports(n)
    for n in (8,9):representative_two_component(n)
    # Check the all-order maximum-support count formula against exhaustive small instances.
    for n in range(5,8):
        ed,C=cycles(n)
        count=0
        supports={tuple(x) for c in C for x in itertools.combinations([i for i in range(len(ed)) if c>>i&1],n-2)}
        count=sum(predicted_shattered(n,S,ed) for S in supports)
        expect=math.factorial(n)//2 if n<=6 else math.factorial(n)*(n-3)//8
        assert count==expect,(n,count,expect)
        print('MAX_SUPPORT_COUNT',n,count)
    print('HAMILTONIAN_SUPPORT_CLASSIFICATION_ALL_CHECKS_PASS')

if __name__=='__main__':main()
