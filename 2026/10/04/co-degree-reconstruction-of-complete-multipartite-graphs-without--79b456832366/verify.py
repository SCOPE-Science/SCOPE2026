from collections import Counter


def partitions_min2(n, lo=2):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        if a > n:
            break
        for tail in partitions_min2(n-a, a):
            yield (a,) + tail


def defect_counts(parts):
    n=sum(parts)
    f=Counter()
    for i,a in enumerate(parts):
        f[a] += a*(a-1)//2
        for b in parts[i+1:]:
            f[a+b] += a*b
    return f


def reconstruct(parts):
    n=sum(parts)
    f=defect_counts(parts)
    p={1:0}
    for s in range(2,n+1):
        conv=sum(p.get(a,0)*p.get(s-a,0) for a in range(2,s-1))
        corr=(s//2)*p.get(s//2,0) if s%2==0 else 0
        num=2*f.get(s,0)-conv+corr
        assert num%(s-1)==0, (parts,s,num)
        p[s]=num//(s-1)
        assert p[s]>=0 and p[s]%s==0, (parts,s,p[s])
    out=[]
    for s in range(2,n+1):
        out += [s]*(p[s]//s)
    assert tuple(out)==tuple(parts), (parts,out)
    assert sum(p.values())==n
    return tuple(out)


def direct_codegrees(parts):
    labels=[]
    for i,a in enumerate(parts):
        labels += [i]*a
    n=len(labels)
    cnt=Counter()
    for x in range(n):
        for y in range(x+1,n):
            c=0
            for z in range(n):
                if z in (x,y):
                    continue
                if labels[z]!=labels[x] and labels[z]!=labels[y]:
                    c+=1
            cnt[n-c]+=1
    return cnt

reconstructed=0
direct=0
for n in range(4,31):
    for parts in partitions_min2(n):
        if len(parts)<2:
            continue
        reconstruct(parts)
        reconstructed+=1
        if n<=12:
            assert direct_codegrees(parts)==defect_counts(parts), parts
            direct+=1
print(f"ALL CHECKS PASSED; reconstructed_types={reconstructed}; direct_types={direct}; max_order=30")
