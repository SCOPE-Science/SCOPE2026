"""Full labeled census of simple spanning rank-3 matroids on 8 points
via K8 clique partitions (= linear spaces), minus the single-line.
Writes census_summary.json. stdlib only."""
import json, time, sys
from collections import Counter

N=8
def ebit(i,j):
    if i>j: i,j=j,i
    return 1<<(i*8+j)
ALL=0
for i in range(8):
    for j in range(i+1,8):
        ALL|=ebit(i,j)
BIT2EP={}
for i in range(8):
    for j in range(i+1,8):
        BIT2EP[ebit(i,j)]=(i,j)
# pointmask -> edgemask, popcount
EM=[0]*256
for m in range(256):
    pts=[i for i in range(8) if m>>i &1]
    e=0
    for a in range(len(pts)):
        for b in range(a+1,len(pts)):
            e|=ebit(pts[a],pts[b])
    EM[m]=e
PC=[bin(m).count("1") for m in range(256)]

sys.setrecursionlimit(10000)
count=0
groups={}  # sig -> [leafcount, repblocks]
t0=time.time()
def leaf(blocks):
    global count
    count+=1
    sizes=tuple(sorted(PC[b] for b in blocks))
    pen=[]
    for p in range(8):
        pen.append(tuple(sorted(PC[b] for b in blocks if b>>p &1)))
    pen=tuple(sorted(pen))
    sig=(sizes,pen)
    g=groups.get(sig)
    if g is None: groups[sig]=[1,list(blocks)]
    else: g[0]+=1

def rec(cover, blocks):
    if cover==ALL:
        # exclude single 8-block (non-spanning)
        if len(blocks)>1:
            leaf(blocks)
        else:
            global count
            count+=1  # count it separately? track
        return
    # least uncovered edge
    free=(~cover)&ALL
    lsb=free&(-free)
    a,b=BIT2EP[lsb]
    # candidate partners
    X=[x for x in range(8) if x!=a and x!=b and (cover&ebit(a,x))==0 and (cover&ebit(b,x))==0]
    # iterate subsets of X, larger first
    nx=len(X)
    for sub in range(1<<nx):
        pm=(1<<a)|(1<<b)
        ok=True
        tl=[X[k] for k in range(nx) if sub>>k &1]
        for k in range(len(tl)):
            pm|=1<<tl[k]
            for l in range(k):
                if cover&ebit(tl[k],tl[l]):
                    ok=False; break
            if not ok: break
        if not ok: continue
        rec(cover|EM[pm], blocks+(pm,))

rec(0,())
dt=time.time()-t0
print("labeled leaves(incl single-line):",count,"time",round(dt,1),"groups:",len(groups))
json.dump({"n_labeled":count,"n_groups":len(groups),"time":dt,
 "groups":[{"sig_sizes":list(k[0]),"sig_pen":[list(p) for p in k[1]],"count":v[0],"rep":v[1]} for k,v in groups.items()]},
 open("output/artifacts/census_summary.json","w"))
