"""Independent aggregate equitable-refinement test on the exact parameter transition digraph."""
from collections import Counter, defaultdict

def run(q,d,t):
    types=[(a,b,t-a-b,f) for a in range(t+1) for b in range(t-a+1) for f in range(d-t+1) if q>=3 or a+b==t]
    idx={p:i for i,p in enumerate(types)}
    trans=[]
    for a,b,c,f in types:
        edges=Counter()
        changes=[((a-1,b+1,c,f),a),((a-1,b,c+1,f),a*(q-2)),((a+1,b-1,c,f),b),((a,b-1,c+1,f),b*(q-2)),((a+1,b,c-1,f),c),((a,b+1,c-1,f),c),((a,b,c,f),c*(q-3)+f*(q-2)),((a,b,c,f-1),f),((a,b,c,f+1),(d-t-f)*(q-1))]
        for p,k in changes:
            if k:
                assert k>0 and p in idx
                edges[idx[p]]+=k
        assert sum(edges.values())==d*(q-1)
        trans.append(edges)
    c=[1 if p==(t,0,0,0) else 2 if p==(0,t,0,0) else 0 for p in types]
    for round in range(d+2):
        keys=[(c[i],tuple(sorted((c[j],k) for j,k in edges.items() if k))) for i,edges in enumerate(trans)]
        # Same neighboring class may occur via multiple target profile classes; sum them.
        keys=[]
        for i,edges in enumerate(trans):
            co=Counter()
            for j,k in edges.items():co[c[j]]+=k
            keys.append((c[i],tuple(sorted(co.items()))))
        catalog={s:i for i,s in enumerate(sorted(set(keys)))}
        new=[catalog[x] for x in keys]
        if len(set(new))==len(set(c)):break
        c=new
    else: raise AssertionError('unexpected stabilization depth')
    assert len(set(c))==len(types), (q,d,t,len(set(c)),len(types))
    count=(t+1)*(d-t+1) if q==2 else (t+1)*(t+2)*(d-t+1)//2
    assert len(types)==count
    for a,b,g,f in types:
        da=b+g+f;db=a+g+f
        aa=t+f-da;bb=t+f-db;gg=da+db-t-2*f
        assert (aa,bb,gg)==(a,b,g)
    return len(types)

def main():
    cfg=0;prof=0
    for q in range(2,8):
        for d in range(1,19):
            for t in range(1,d+1):
                prof+=run(q,d,t);cfg+=1
    print('QUOTIENT_OK configurations=%s aggregate_orbit_profiles=%s'%(cfg,prof))
if __name__=='__main__':main()
