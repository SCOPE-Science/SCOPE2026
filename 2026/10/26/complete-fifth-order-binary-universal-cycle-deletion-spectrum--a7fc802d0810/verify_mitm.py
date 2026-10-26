"""Independent meet-in-the-middle enumeration of all balanced deletions."""
from collections import defaultdict,Counter
from math import comb
V=16;E=32
T=[x>>1 for x in range(32)]
H=[x&15 for x in range(32)]

def signatures(offset):
    # Divergence v -> out minus in for each half-edge mask.
    sig=[None]*65536
    d=[0]*16
    gray_prev=0
    for i in range(65536):
        gray=i^(i>>1)
        if i:
            x=(gray ^ gray_prev).bit_length()-1
            e=offset+x
            if T[e]!=H[e]:
                v=1 if (gray>>x)&1 else -1
                d[T[e]]+=v;d[H[e]]-=v
        sig[gray]=tuple(d)
        gray_prev=gray
    return sig

def connected(z):
    # Check weak connectivity among nonisolated vertices of remaining graph.
    r=((1<<32)-1)^z
    if r.bit_count()<5:return False
    # DSU is independently different from breadth first search
    parent=list(range(16));rank=[0]*16;active=set()
    def find(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for e in range(32):
        if r>>e&1:
            a,b=T[e],H[e];active.add(a);active.add(b)
            ra,rb=find(a),find(b)
            if ra!=rb:
                if rank[ra]<rank[rb]:ra,rb=rb,ra
                parent[rb]=ra
                if rank[ra]==rank[rb]:rank[ra]+=1
    return len({find(x) for x in active})==1

if __name__=='__main__':
    one=signatures(0);two=signatures(16)
    index=defaultdict(list)
    for b,sign in enumerate(two):index[sign].append(b)
    good=Counter();balanced=Counter();n=0
    for a,sign in enumerate(one):
        rev=tuple(-v for v in sign)
        for b in index.get(rev,()):
            z=a|(b<<16);s=z.bit_count();balanced[s]+=1;n+=1
            if connected(z):good[s]+=1
    assert n==6600, n
    assert [good.get(i,0) for i in range(33)]==[1,2,2,4,8,14,26,38,56,86,126,166,199,230,254,250,240,204,168,130,98,68,51,30,20,12,9,6,0,0,0,0,0]
    print('MITM_ORDER5_UNIVERSAL_CYCLE_PASS',n,'balanced')
    print('BALANCED',*[balanced.get(i,0) for i in range(33)])
    print('VALID',*[good.get(i,0) for i in range(33)])
