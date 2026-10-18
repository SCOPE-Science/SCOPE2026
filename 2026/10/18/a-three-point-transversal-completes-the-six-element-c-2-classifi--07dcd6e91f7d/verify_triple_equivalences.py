import itertools,collections,sys

def partitions(n):
    if n==0: return [()]
    P=[(0,)]
    for i in range(1,n):
        P=[p+(j,) for p in P for j in range(max(p)+2)]
    return P

def get_objs(n):
    pp=partitions(n); idx={p:i for i,p in enumerate(pp)}
    perm=list(itertools.permutations(range(n)))
    def trans(p,t):
        r=tuple(p[t[i]] for i in range(n)); ids={}; a=[]
        for x in r:
            if x not in ids:ids[x]=len(ids)
            a.append(ids[x])
        return idx[tuple(a)]
    T=[tuple(trans(p,t) for p in pp) for t in perm]
    # Enumerate the orbits of the first partition under all relabelings.
    allperm=tuple(range(len(perm)))
    Eids=sorted({min(T[t][i] for t in allperm) for i in range(len(pp))})
    objs=[]; counts=[]
    for ei in Eids:
        stabE=[t for t in allperm if T[t][ei]==ei]
        freps=sorted({min(T[t][i] for t in stabE) for i in range(len(pp))})
        sub=0
        for fi in freps:
            stabEF=[t for t in stabE if T[t][fi]==fi]
            greps=sorted({min(T[t][i] for t in stabEF) for i in range(len(pp))})
            sub+=len(greps)
            objs.extend((ei,fi,gi) for gi in greps)
        counts.append((pp[ei],len(freps),sub))
    return pp,objs,counts

def wl(pp,objs,n):
    N=len(objs); colors=[[0]*n for _ in range(N)]
    P=[]
    for ei,fi,gi in objs:
        p=[pp[ei],pp[fi],pp[gi]]
        masks=[]
        for x in range(n):
            masks.append(tuple(((1 if p[0][x]==p[0][y] else 0)| (2 if p[1][x]==p[1][y] else 0)| (4 if p[2][x]==p[2][y] else 0)) for y in range(n)))
        P.append(masks)
    for rnd in range(n+1):
        sigs={}; nxt=[]
        for i in range(N):
            out=[]; old=colors[i]
            for x in range(n):
                sig=(old[x],tuple(sorted((P[i][x][y],old[y]) for y in range(n) if y!=x)))
                c=sigs.setdefault(sig,len(sigs));out.append(c)
            nxt.append(out)
        # labels assigned on encounter; deterministic; equals globally for every structure
        colors=nxt
        buckets=collections.defaultdict(list)
        for i in range(N): buckets[tuple(sorted(colors[i]))].append(i)
        multi=[g for g in buckets.values() if len(g)>1]
        print('  round',rnd+1,'colors',len(sigs),'C2 classes',len(buckets),'non-singleton classes',len(multi),'paired_types',sum(len(g) for g in multi),flush=True)
    return buckets

if __name__=='__main__':
 for n in range(1,int(sys.argv[1])+1):
    pp,objs,counts=get_objs(n)
    print('n',n,'Bell',len(pp),'iso_classes',len(objs),'partition_E_type_breakdown',[(str(p),f,c) for p,f,c in counts],flush=True)
    b=wl(pp,objs,n)
    iso_expected={1:1,2:8,3:37,4:285,5:2150,6:21205}
    c2_expected={1:1,2:8,3:37,4:285,5:2150,6:21197}
    assert len(objs)==iso_expected[n] and len(b)==c2_expected[n]
    ms=[v for v in b.values() if len(v)>1]
    assert (not ms if n<6 else len(ms)==8 and all(len(g)==2 for g in ms))
    if ms:
        print('COLLISIONS',len(ms), 'class_size_counts',dict(collections.Counter(map(len,ms))),flush=True)
        for grp in ms[:15]: print(' ',[[pp[x] for x in objs[i]] for i in grp],flush=True)
    print('DONE',n,flush=True)
