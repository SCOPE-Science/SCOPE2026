"""Exact rank-three type enumerator for nonempty undirected linear forests."""
from collections import Counter, defaultdict
from hashlib import sha256
import sys
from pathlib import Path

def graph(code):
    parts=[]
    for size in range(1,8):
        count=code%4;code//=4
        parts.extend([size]*count)
    n=sum(parts)
    neighbors=[0]*n
    p=0
    for size in parts:
        for v in range(p,p+size-1):
            neighbors[v]|=1<<(v+1)
            neighbors[v+1]|=1<<v
        p+=size
    return n, neighbors

def rank3_type(n,adj):
    mask=(1<<n)-1
    rooted_types=set()
    for x in range(n):
        pair_types=0
        X=adj[x]
        for y in range(n):
            if x==y:
                other=mask^(1<<x)
                t=32 + (int(bool(X&other))) + 2*int(bool(other&~X))
            else:
                Y=adj[y]; other=mask^((1<<x)|(1<<y))
                p=(1 if other&~(X|Y) else 0)
                p+=2 if other&(X&~Y) else 0
                p+=4 if other&(~X&Y) else 0
                p+=8 if other&(X&Y) else 0
                t=p+16*int(bool(X&(1<<y)))
            pair_types|=1<<t
        rooted_types.add(pair_types)
    return tuple(sorted(rooted_types))

def main():
    bytype={}; class_totals=Counter(); histogram=Counter()
    mapping={}
    for code in range(1,4**7):
        n,adj=graph(code)
        t=rank3_type(n,adj)
        if t not in bytype or n<bytype[t][0] or (n==bytype[t][0] and code<bytype[t][1]):
            bytype[t]=(n,code)
        mapping[code]=t
    for t,(n,code) in bytype.items():histogram[n]+=1
    classes=sorted(bytype, key=lambda t:(bytype[t][0],bytype[t][1]))
    cid={t:i+1 for i,t in enumerate(classes)}
    with open(Path(__file__).resolve().parent / 'canonical_manifest.csv','w') as f:
        f.write('code,rank3_class,order\n')
        for code in range(1,4**7):
            n,_=graph(code)
            f.write(f'{code},{cid[mapping[code]]},{n}\n')
    with open(Path(__file__).resolve().parent / 'class_representatives.csv','w') as f:
        f.write('rank3_class,code,minimal_order,multiplicities_P1_to_P7,signature_hex\n')
        for t in classes:
            n,code=bytype[t]
            c=code;m=[]
            for _ in range(7):m.append(c%4);c//=4
            f.write(f'{cid[t]},{code},{n},{"".join(map(str,m))},{"-".join(hex(x)[2:] for x in t)}\n')
    print('canonical',len(mapping),'classes',len(classes),'sharp_kernel',max(histogram))
    print('histogram',dict(sorted(histogram.items())))
    return 0
if __name__=='__main__':sys.exit(main())
