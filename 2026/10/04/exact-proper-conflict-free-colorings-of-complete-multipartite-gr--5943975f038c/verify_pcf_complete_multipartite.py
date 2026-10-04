from functools import lru_cache
from itertools import combinations
from math import factorial

@lru_cache(None)
def set_partitions_tuple(items):
    items=tuple(items)
    if not items:
        return ((),)
    first=items[0]
    out=[]
    for rest in set_partitions_tuple(items[1:]):
        # new block
        out.append(((first,),)+rest)
        # insert into existing block; canonical block ordering by minimum element
        for j in range(len(rest)):
            b=tuple(sorted((first,)+rest[j]))
            nr=list(rest); nr[j]=b
            nr=tuple(sorted(nr, key=lambda x:x[0]))
            if nr not in out:
                out.append(nr)
    # dedupe canonical
    seen=[]; st=set()
    for p in out:
        cp=tuple(sorted((tuple(sorted(b)) for b in p), key=lambda x:x[0]))
        if cp not in st:
            st.add(cp); seen.append(cp)
    return tuple(seen)

def int_partitions(n, min_part=1):
    if n==0:
        yield ()
        return
    for a in range(min_part,n+1):
        for tail in int_partitions(n-a,a):
            yield (a,)+tail

def build_parts(sizes):
    parts=[]; v=0
    for s in sizes:
        parts.append(tuple(range(v,v+s))); v+=s
    return parts

def proper_partitions(sizes):
    parts=build_parts(sizes)
    choices=[set_partitions_tuple(tuple(P)) for P in parts]
    def rec(i, blocks):
        if i==len(choices):
            yield tuple(blocks); return
        for p in choices[i]:
            yield from rec(i+1, blocks+list(p))
    yield from rec(0,[])

def pcf_by_definition(sizes, blocks):
    parts=build_parts(sizes)
    part_of={v:i for i,P in enumerate(parts) for v in P}
    color_of={v:c for c,B in enumerate(blocks) for v in B}
    N=sum(sizes)
    for v in range(N):
        neigh=[u for u in range(N) if part_of[u]!=part_of[v]]
        counts={}
        for u in neigh:
            counts[color_of[u]]=counts.get(color_of[u],0)+1
        if not any(c==1 for c in counts.values()):
            return False
    return True

def witness_parts(sizes, blocks):
    parts=build_parts(sizes)
    part_of={v:i for i,P in enumerate(parts) for v in P}
    wp=set()
    for B in blocks:
        i=part_of[B[0]]
        assert all(part_of[v]==i for v in B)
        if len(B)==1: wp.add(i)
    return wp

def W(n):
    return 1 if n==2 else n

def formula_chi(sizes):
    r=len(sizes); s=sum(1 for n in sizes if n==1)
    return r+max(0,2-s)

def formula_opt_unlabeled(sizes):
    s=sum(1 for n in sizes if n==1)
    non=[i for i,n in enumerate(sizes) if n>=2]
    if s>=2:
        return 1
    if s==1:
        return sum(W(sizes[i]) for i in non)
    return sum(W(sizes[i])*W(sizes[j]) for i,j in combinations(non,2))

def run(max_order=10):
    types=0; proper_profiles=0; pcf_profiles=0; opt_profiles=0
    for N in range(2,max_order+1):
        for sizes in int_partitions(N):
            if len(sizes)<2: continue
            types+=1
            min_k=None; opt=0
            for blocks in proper_partitions(sizes):
                proper_profiles+=1
                bydef=pcf_by_definition(sizes,blocks)
                wp=witness_parts(sizes,blocks)
                structural=(len(wp)>=2)
                if bydef!=structural:
                    raise AssertionError((sizes,blocks,bydef,wp))
                if bydef:
                    pcf_profiles+=1
                    k=len(blocks)
                    if min_k is None or k<min_k:
                        min_k=k; opt=1
                    elif k==min_k:
                        opt+=1
            if min_k!=formula_chi(sizes):
                raise AssertionError(('chi',sizes,min_k,formula_chi(sizes)))
            if opt!=formula_opt_unlabeled(sizes):
                raise AssertionError(('count',sizes,opt,formula_opt_unlabeled(sizes)))
            opt_profiles+=opt
    print(f'ALL CHECKS PASSED; multipartite_types={types}; proper_partitions={proper_profiles}; pcf_partitions={pcf_profiles}; optimal_unlabeled_partitions={opt_profiles}; max_order={max_order}')

if __name__=='__main__':
    run()
