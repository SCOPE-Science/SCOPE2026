#!/usr/bin/env python3
"""Exact finite first-order types of sunlet graphs: full tuple enumeration."""
import itertools,json,sys

def graph(n):
    a=[0]*(2*n)
    for j in range(n):
        v=j
        for w in (((j+1)%n),((j-1)%n),j+n):
            a[v]|=1<<w
            a[w]|=1<<v
    return a

def signature(t,a):
    z=0
    for k in range(len(t)):
        for j in range(k):
            z=4*z+(2 if (a[t[j]]>>t[k])&1 else 0)+(1 if t[j]==t[k] else 0)
    return z

def calculate(nmax):
    ns=range(3,nmax+1)
    mats={n:graph(n) for n in ns}
    stage_next={}
    levels=[]
    for length in (4,3,2,1,0):
        current={}
        pool={}
        for n in ns:
            M=mats[n]; count=2*n
            local={}
            for t in itertools.product(range(count),repeat=length):
                atom=signature(t,M)
                if length==4: key=(atom,)
                else:
                    key=(atom,frozenset(stage_next[n][t+(v,)] for v in range(count)))
                x=pool.get(key)
                if x is None:
                    x=len(pool)
                    pool[key]=x
                local[t]=x
            current[n]=local
        levels.append((length,len(pool),sum(len(d) for d in current.values())))
        print('direct_level',length,'number_of_types',len(pool),'tuples',levels[-1][-1],flush=True)
        stage_next=current
    roots={n:stage_next[n][()] for n in ns}
    groups={}
    for n,z in roots.items():groups.setdefault(z,[]).append(n)
    result={'graphs':list(ns),'four_round_groups':list(groups.values()),'levels':levels}
    print('DIRECT_FINAL',json.dumps(result,sort_keys=True),flush=True)
    return result

if __name__=='__main__':
    x=calculate(int(sys.argv[1]) if len(sys.argv)>1 else 11)
    if len(sys.argv)>2:
        with open(sys.argv[2],'w') as f:json.dump(x,f,sort_keys=True,indent=2)
