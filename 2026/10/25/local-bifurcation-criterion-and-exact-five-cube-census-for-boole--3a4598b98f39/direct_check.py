"""Independent direct forth/back enumeration for small Boolean-to-diamond frames."""
from itertools import permutations

def monotone_truths(n):
    N=1<<n
    covers=[(a, a|1<<j) for a in range(N) for j in range(n) if not (a>>j)&1]
    for mask in range(1<<N):
        if all(not (mask>>a&1) or (mask>>b&1) for a,b in covers):
            yield mask

def test(n, a, b):
    N=1<<n
    val=[((a>>x)&1)+2*((b>>x)&1) for x in range(N)]
    if len(set(val))<4:
        return False
    for x in range(N):
        for v in range(4):
            if (val[x]&v)!=val[x]:continue
            if not any((x&z)==x and val[z]==v for z in range(N)):
                return False
    return True

def orbit_count(n, pairs):
    permlist=list(permutations(range(n)))
    group=[]
    for p in permlist:
        idx=[]
        for x in range(1<<n):
            z=0
            for j in range(n):
                if x>>j&1:z|=1<<p[j]
            idx.append(z)
        group.append(idx)
    def transform(mask,idx):
        return sum(1<<idx[x] for x in range(1<<n) if mask>>x&1)
    # Burnside check independent of the original implementation
    fixed=sum((int((transform(a,idx),transform(b,idx))==(a,b))+
               int((transform(b,idx),transform(a,idx))==(a,b)))
            for a,b in pairs for idx in group)
    assert fixed%(2*len(group))==0
    return fixed//(2*len(group))

if __name__=='__main__':
    for n in range(1,5):
        mono=list(monotone_truths(n))
        good=[(a,b) for a in mono for b in mono if test(n,a,b)]
        print(f'n={n} monotone_functions={len(mono)} direct_bounded_surjections={len(good)} independent_symmetry_orbits={orbit_count(n, good)}',flush=True)
