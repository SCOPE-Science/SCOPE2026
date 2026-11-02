#!/usr/bin/env python3
"""Exact finite q-types of sunlet graphs, using their dihedral symmetry.
Canonical representatives and global structural encodings are constructed from scratch.
"""
import sys,json
from collections import defaultdict

def canon(t,n):
    if not t: return ()
    i0=t[0]%n
    f=tuple(((v%n-i0)%n)+n*(v//n) for v in t)
    g=tuple(((i0-v%n)%n)+n*(v//n) for v in t)
    return min(f,g)

def edge(v,w,n):
    a,b=v%n,w%n
    p,q=v//n,w//n
    return int((p==q==0 and (a-b)%n in (1,n-1)) or (p!=q and a==b))

def atomic(t,n):
    c=0; sh=0
    for j in range(len(t)):
        for i in range(j):
            c |= (int(t[i]==t[j]) | (edge(t[i],t[j],n)<<1)) << sh
            sh += 2
    return c

def run(max_n=11):
    ns=list(range(3,max_n+1))
    reps={n:[{()}]+[set() for _ in range(4)] for n in ns}
    for n in ns:
        for level in range(1,5):
            parent=reps[n][level-1]
            reps[n][level]={canon(t+(v,),n) for t in parent for v in range(2*n)}
            print('build',n,level,len(reps[n][level]),flush=True)
    # Global structural types use deterministic interning.
    types={n:{} for n in ns}; stage_info=[]
    for level in range(4,-1,-1):
        r=4-level
        # compute signatures globally; each pair key=(n,t), values tuples
        db={}; signatures=set()
        for n in ns:
            for t in reps[n][level]:
                a=atomic(t,n)
                if level==4:
                    sig=(a,)
                else:
                    childtypes=set()
                    for v in range(2*n):
                        childtypes.add(types[n][canon(t+(v,),n)])
                    sig=(a, tuple(sorted(childtypes)))
                db[n,t]=sig
                signatures.add(sig)
        # ids sorted global, deterministic
        ids={sig:i for i,sig in enumerate(sorted(signatures))}
        for n in ns:
            types[n]={t:ids[db[n,t]] for t in reps[n][level]}
        roots={n:types[n][()] for n in ns} if level==0 else None
        stage_info.append({'rank':r,'tuple_length':level,'distinct_types':len(ids),'total_orbits':len(db),'root_types':roots})
        print('types',level,r,'num',len(ids),flush=True)
    groups=defaultdict(list)
    for n in ns:groups[types[n][()]].append(n)
    out={'graph':'n-sunlet = C_n corona K_1','min_n':min(ns),'max_n':max(ns),'four_round_groups':list(groups.values()),'stages':stage_info}
    print('FINAL',json.dumps(out,sort_keys=True),flush=True)
    return out

if __name__=='__main__':
    out=run(int(sys.argv[1]) if len(sys.argv)>1 else 11)
    if len(sys.argv)>2:
        with open(sys.argv[2],'w') as f:json.dump(out,f,sort_keys=True,indent=2)
