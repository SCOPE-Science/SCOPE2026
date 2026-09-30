#!/usr/bin/env python3
import itertools, json, math

def edge_masks(n):
    return [sum(1<<i for i in t) for t in itertools.combinations(range(n),3)]

def valid_extension(fam, seen, e):
    new=[e]
    new += [e|a for a in fam]
    new += [e|a|b for a,b in itertools.combinations(fam,2)]
    return None if len(set(new))<len(new) or any(u in seen for u in new) else new

def search(n,target,count_all=False):
    E=edge_masks(n); first=(1<<0)|(1<<1)|(1<<2); fi=E.index(first)
    fam=[first]; seen={first}; count=0; witness=None; nodes=0
    def rec(start):
        nonlocal count,witness,nodes
        nodes+=1
        if len(fam)==target:
            count+=1
            if witness is None: witness=fam.copy()
            return not count_all
        need=target-len(fam)
        if len(E)-start<need: return False
        for j in range(start, len(E)-need+1):
            e=E[j]
            new=valid_extension(fam,seen,e)
            if new is None: continue
            fam.append(e); seen.update(new)
            stop=rec(j+1)
            fam.pop()
            for u in new: seen.remove(u)
            if stop: return True
        return False
    rec(fi+1)
    return {"count_containing_012":count,"witness":witness,"nodes":nodes}

def mask_to_tuple(m,n): return tuple(i for i in range(n) if (m>>i)&1)

rows=[]
for n in range(4,10):
    upper=search(n,n-1,False)
    assert upper["count_containing_012"]==0
    ext=search(n,n-2,True)
    assert ext["count_containing_012"]==3
    total=math.comb(n,3)*3//(n-2)
    assert total==math.comb(n,2)
    S={0,1}
    star=[sum(1<<i for i in (*S,x)) for x in range(n) if x not in S]
    # Direct union check for the construction.
    unions={}
    for k in range(1,min(3,len(star))+1):
        for I in itertools.combinations(range(len(star)),k):
            u=0
            for i in I: u|=star[i]
            assert u not in unions
            unions[u]=I
    rows.append({
        "n":n,
        "U3_n_3":n-2,
        "upper_search_nodes":upper["nodes"],
        "extremals_containing_012":3,
        "labeled_extremals":total,
        "extremal_type":"all triples containing a fixed 2-set",
        "sample_star":[mask_to_tuple(m,n) for m in star],
    })
print(json.dumps({"schema_version":1,"result":"VERIFY_OK","rows":rows},sort_keys=True,separators=(",",":")))
