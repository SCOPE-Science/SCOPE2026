from itertools import combinations


def integer_partitions(n):
    out=[]
    def rec(rem, cap, cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(min(cap,rem),0,-1):
            rec(rem-x,x,cur+[x])
    rec(n,n,[])
    return out


def rgs_partitions(m):
    if m==0:
        return
    a=[0]*m
    def rec(i, mx):
        if i==m:
            yield tuple(a)
            return
        for x in range(mx+2):
            a[i]=x
            yield from rec(i+1,max(mx,x))
    yield from rec(1,0)


def valid(parts, subset, labels):
    color=dict(zip(subset,labels))
    for v,c in color.items():
        p=v[0]
        closed=[u for u in subset if u==v or u[0]!=p]
        same=sum(color[u]==c for u in closed)
        if 2*same < len(closed):
            return False
    return True


def brute(parts):
    vertices=[(i,j) for i,n in enumerate(parts) for j in range(n)]
    N=len(vertices)
    best=0
    checks=0
    structural_checks=0
    for mask in range(1,1<<N):
        subset=[vertices[i] for i in range(N) if (mask>>i)&1]
        for labels in rgs_partitions(len(subset)):
            checks += 1
            if not valid(parts,subset,labels):
                continue
            q=max(labels)+1
            best=max(best,q)
            if q>=3:
                occ={i:sum(v[0]==i for v in subset) for i in range(len(parts))}
                Lh=max(occ.values())
                largest=[i for i,a in occ.items() if a==Lh]
                # The theorem says there exists a largest occupied part met by every class;
                # the proof actually permits any chosen largest part. Check all of them.
                for p in largest:
                    for c in range(q):
                        assert any(v[0]==p and labels[t]==c for t,v in enumerate(subset)), (parts,subset,labels,p,c)
                        structural_checks += 1
    return best, checks, structural_checks


def main():
    profiles=0
    color_partitions=0
    structural_checks=0
    for N in range(2,8):
        for parts in integer_partitions(N):
            profiles += 1
            got,c,s=brute(parts)
            color_partitions += c
            structural_checks += s
            want=max(max(parts),2)
            assert got==want, (parts,got,want)
    print(f'ALL CHECKS PASSED; multipartite_profiles={profiles}; partial_color_partitions={color_partitions}; structural_class_checks={structural_checks}; max_order=7')

if __name__=='__main__':
    main()
