"""Independent exact checks for the singleton three-rainbow prism enumerator.

Run: python3 verify.py
No third-party packages required.
"""
from itertools import combinations, product
from math import comb


def predicted(n):
    a = 12 if n % 6 == 0 else 0
    b = 12*n if n%2 else (36*n if n%6==0 else 0)
    if n%2:
        c = 36*n*(2*n-3)
    elif n%6==0:
        c = 108*n*(n-2)
    elif n%6==2:
        c = 18*n*(3*n-5)
    else:
        c = 18*n*(3*n-1)
    return (a,b,c)


def neighbors(n):
    # Vertex identifiers are 2*i+row.
    return [tuple(sorted({2*((i-1)%n)+r,2*((i+1)%n)+r,2*i+1-r}))
            for i in range(n) for r in (0,1)]


def is_valid(f,adj):
    for i,x in enumerate(f):
        if x == 0 and {f[j] for j in adj[i]} != {1,2,3}:
            return False
    return True


def direct_function_count(n):
    adj=neighbors(n)
    out=[0,0,0]
    for f in product((0,1,2,3),repeat=2*n):
        k=sum(x!=0 for x in f)
        if n<=k<=n+2 and is_valid(f,adj):
            out[k-n]+=1
    return tuple(out)


def independent_sets_by_holes(n,h):
    # Every uncolored vertex excludes its rung-mate. Generate the at-most-two
    # empty rungs, then independently alternate the two rows on each run.
    if h==0:
        if n%2==0:
            for orient in (0,1):
                yield {2*i+((orient+i)%2) for i in range(n)}
        return
    for holes in combinations(range(n),h):
        hole_set=set(holes)
        runs=[]
        for j in holes:
            row=[];x=(j+1)%n
            while x not in hole_set:
                row.append(x);x=(x+1)%n
            if row:runs.append(row)
        for orientations in product((0,1),repeat=len(runs)):
            U=set()
            for row,orient in zip(runs,orientations):
                for k,i in enumerate(row):U.add(2*i+((orient+k)%2))
            yield U


def proper_3_colorings_of_triangle_constraints(n,U):
    adj=neighbors(n)
    C=[v for v in range(2*n) if v not in U]
    ix={v:i for i,v in enumerate(C)}
    ar=[set() for _ in C]
    for u in U:
        for a,b in combinations(adj[u],2):
            x,y=ix[a],ix[b]
            ar[x].add(y); ar[y].add(x)
    def recurse(dom):
        unset=[i for i,v in enumerate(dom) if v.bit_count()!=1]
        if not unset:return 1
        i=min(unset,key=lambda j:(dom[j].bit_count(),-len(ar[j])))
        answer=0
        for bit in (1,2,4):
            if not dom[i]&bit:continue
            ds=dom[:];ds[i]=bit
            pending=[i];ok=True
            while pending and ok:
                x=pending.pop()
                for y in ar[x]:
                    if ds[y]&ds[x]:
                        ds[y] &= ~ds[x]
                        if ds[y]==0:
                            ok=False;break
                        if ds[y].bit_count()==1:pending.append(y)
            if ok:answer+=recurse(ds)
        return answer
    return recurse([7]*len(C))


def exact_support_count(n,h):
    return sum(proper_3_colorings_of_triangle_constraints(n,U)
               for U in independent_sets_by_holes(n,h))


def segment_kernel(n):
    # Enumerates all internal labels and prescribed terminal colors.
    ans=[[0]*3 for _ in range(3)]
    for x in product((0,1,2),repeat=n+2):
        valid=True
        # The interior colored companion labels are x[1:n+1];
        # x[0], x[n+1] are boundary-neighbor labels.
        for j in range(1,n+1):
            if len({x[j-1],x[j],x[j+1]}) !=3:
                valid=False;break
        if valid:ans[x[0]][x[-1]]+=1
    return ans


def test():
    for n in range(1,9):
        expect=[[2 if a==b else 0 for b in range(3)] for a in range(3)] \
            if n%3==2 else [[int(a!=b) for b in range(3)] for a in range(3)]
        assert segment_kernel(n)==expect,(n,segment_kernel(n),expect)
    print('SEGMENT_KERNEL_OK lengths=1..8')

    for n in range(3,6):
        actual=direct_function_count(n)
        assert actual==predicted(n),(n,actual,predicted(n))
        print('DIRECT_LABELINGS_OK',n,actual)

    for n in range(3,25):
        actual=tuple(exact_support_count(n,h) for h in range(3))
        assert actual==predicted(n),(n,actual,predicted(n))
        print('SUPPORT_COLORING_OK',n,actual)
    print('VERIFY_OK')

if __name__=='__main__':
    test()
