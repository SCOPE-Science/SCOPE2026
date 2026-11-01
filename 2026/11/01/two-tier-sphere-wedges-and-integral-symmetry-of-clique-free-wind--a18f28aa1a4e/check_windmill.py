"""Independent finite simplicial-chain and signed-Lefschetz checks for clique-free windmills."""
from itertools import combinations, permutations
from math import comb
from collections import defaultdict

def vertices(block_sizes):
    blocks=[]
    i=1
    for n in block_sizes:
        blocks.append(tuple(range(i,i+n)))
        i+=n
    return blocks

def faces(block_sizes,t):
    blocks=vertices(block_sizes)
    n=1+sum(block_sizes)
    result=defaultdict(list)
    for mask in range(1<<n):
        root=bool(mask&1)
        bound=t-2 if root else t-1
        if all(sum(bool(mask&(1<<v)) for v in b)<=bound for b in blocks):
            size=mask.bit_count()
            if size: result[size-1].append(mask)
    return result

def gf2_rank(columns):
    pivots={}
    for c in columns:
        while c:
            i=c.bit_length()-1
            if i not in pivots:
                pivots[i]=c
                break
            c^=pivots[i]
    return len(pivots)

def bettis(block_sizes,t):
    fs=faces(block_sizes,t)
    ranks={}
    for d in sorted(fs):
        if d==0:
            ranks[d]=1 if fs[d] else 0 # unreduced degree-zero rank = 1
        else:
            idx={mask:i for i,mask in enumerate(fs[d-1])}
            cols=[]
            for mask in fs[d]:
                col=0
                x=mask
                while x:
                    b=x&-x
                    col^=1<<idx[mask^b]
                    x-=b
                cols.append(col)
            ranks[d]=gf2_rank(cols)
    result={}
    for d in sorted(fs):
        h=len(fs[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if h: result[d]=h
    return result

def expected(block_sizes,t):
    if min(block_sizes)<=t-2:
        return {}
    r=len(block_sizes)
    low=1
    high=1
    for a in block_sizes:
        low*=comb(a-1,t-2)
        high*=comb(a-1,t-1) if a>=t else 0
    out={}
    if low: out[r*(t-2)]=low
    if high: out[r*(t-1)-1]=high
    return out

def lef(block_sizes,t,p):
    n=1+sum(block_sizes)
    fs=faces(block_sizes,t)
    out=-1
    for d,facesd in fs.items():
        for mask in facesd:
            image=sum(1<<p[i] for i in range(n) if mask>>i&1)
            if image!=mask: continue
            seen=set(); cycles=0
            for i in range(n):
                if mask>>i&1 and i not in seen:
                    cycles+=1; j=i
                    while j not in seen:
                        seen.add(j); j=p[j]
            out+=(-1)**(cycles-1)
    return out

def wedge_aug_char(p,k):
    # g is a permutation of local a elements; char of exterior k of augmentation
    a=len(p)
    seen=set(); polynomial=[1]
    for i in range(a):
        if i in seen: continue
        j=i; cyc=[]
        while j not in seen:
            seen.add(j);cyc.append(j);j=p[j]
        l=len(cyc)
        nxt=polynomial+[0]*l
        for d,c in enumerate(polynomial):nxt[d+l]-=(-1)**l*c
        polynomial=nxt
    # divide by (1+z)
    quot=[0]*(len(polynomial)-1)
    for i in range(len(quot)): quot[i]=polynomial[i]-(quot[i-1] if i else 0)
    return quot[k] if 0<=k<len(quot) else 0

def char(block_sizes,t,p,degree_type):
    blocks=vertices(block_sizes)
    block_index={v:(b,j) for b,B in enumerate(blocks) for j,v in enumerate(B)}
    rho=[]
    for b,B in enumerate(blocks):
        dst=block_index[p[B[0]]][0]
        assert all(block_index[p[v]][0]==dst for v in B)
        rho.append(dst)
    assert sorted(rho)==list(range(len(blocks)))
    k=(t-1) if degree_type=='high' else (t-2)
    product=1;seen=set()
    for i in range(len(blocks)):
        if i in seen: continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=rho[j]
        source=blocks[cyc[0]]
        local=[]
        for a,v in enumerate(source):
            u=v
            for _ in range(len(cyc)):u=p[u]
            local.append(source.index(u))
        product*=(-1)**(k*(len(cyc)-1))*wedge_aug_char(local,k)
    return product

def predicted_lef(block_sizes,t,p):
    r=len(block_sizes)
    if min(block_sizes)<=t-2:return 0
    low=char(block_sizes,t,p,'low')
    high=char(block_sizes,t,p,'high')
    return (-1)**(r*(t-2))*low+(-1)**(r*(t-1)-1)*high

def auto_test(block_sizes,t):
    B=vertices(block_sizes);n=1+sum(block_sizes)
    tests=[list(range(n))]
    for b in B:
        if len(b)>1:
            p=list(range(n));p[b[0]],p[b[1]]=p[b[1]],p[b[0]];tests.append(p)
        if len(b)>2:
            p=list(range(n));p[b[0]],p[b[1]],p[b[2]]=p[b[1]],p[b[2]],p[b[0]];tests.append(p)
    for i in range(len(B)):
        for j in range(i+1,len(B)):
            if len(B[i])==len(B[j]):
                p=list(range(n))
                for a,b in zip(B[i],B[j]): p[a]=b;p[b]=a
                tests.append(p)
                if len(B[i])>=2:
                    p=list(p);p[B[i][0]],p[B[i][1]]=p[B[i][1]],p[B[i][0]]
                    tests.append(p)
    for p in tests:
        observed=lef(block_sizes,t,p)
        predicted=predicted_lef(block_sizes,t,p)
        assert observed==predicted,(block_sizes,t,p,observed,predicted)
    return len(tests)

def main():
    examples=[((2,2),3),((3,3),3),((4,3),3),((3,2,3),3),((2,2,2),3),((1,3),3),((3,3),4),((4,4),4),((3,3,3),4),((4,3,3),4),((4,4,4),4),((5,4),4)]
    total=0
    for sizes,t in examples:
        observed=bettis(sizes,t);anticipated=expected(sizes,t)
        assert observed==anticipated,(sizes,t,observed,anticipated)
        n=auto_test(sizes,t);total+=n
        print(f'PASS sizes={sizes}, t={t}, reduced_betti={observed}, automorphisms_tested={n}')
    print(f'PASS {len(examples)} mod-two chain computations and {total} signed Lefschetz checks.')

def all_automorphisms(sizes):
    blocks=vertices(sizes)
    n=1+sum(sizes)
    for sigma in permutations(range(len(sizes))):
        if any(sizes[i]!=sizes[sigma[i]] for i in range(len(sizes))):continue
        from itertools import product
        for pis in product(*(permutations(range(sizes[i])) for i in range(len(sizes)))):
            p=list(range(n))
            for i,b in enumerate(blocks):
                tgt=blocks[sigma[i]]
                for src,j in zip(b,pis[i]):p[src]=tgt[j]
            yield p

def full_group_checks():
    totals=0
    for sizes,t in [((3,3),3),((2,2,2),3),((3,3,3),4)]:
        count=0
        for p in all_automorphisms(sizes):
            observed=lef(sizes,t,p)
            pred=predicted_lef(sizes,t,p)
            assert observed==pred,(sizes,t,p,observed,pred)
            count+=1
        totals+=count
        print(f'PASS all {count} root-preserving automorphisms for sizes={sizes}, t={t}.')
    print(f'PASS {totals} exhaustive group-element Lefschetz comparisons.')

if __name__=='__main__':
    main()
    full_group_checks()
