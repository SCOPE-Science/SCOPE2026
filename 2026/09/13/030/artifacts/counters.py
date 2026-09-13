import itertools, collections

def is_pasch(inside):
    import collections
    pts=set(p for b in inside for p in b)
    if len(inside)!=4 or len(pts)!=6: return False
    deg=collections.Counter(p for b in inside for p in b)
    return sorted(deg.values())==[2]*6

def count_pasch_A(blocks, v=21):
    """Brute force: 6-sets whose inside-blocks form a Pasch (4 blocks, all degrees 2)."""
    n=0
    for s in itertools.combinations(range(v),6):
        ss=set(s)
        inside=[b for b in blocks if set(b)<=ss]
        if len(inside)>4: raise AssertionError(("too many",s,inside))
        if len(inside)==4 and is_pasch(inside): n+=1
    return n

def count_pasch_B(blocks):
    """Independent method: intersecting block pairs. For b1={p,x1,x2}, b2={p,y1,y2}
    (share exactly p), a Pasch containing both has form {b1,b2,{x1,y1,z},{x2,y2,z}} or
    {b1,b2,{x1,y2,z},{x2,y1,z}}. Count (pair, z, matching) witnesses; each Pasch has
    6 intersecting pairs (4 blocks, each pair intersects) and each pair extends in
    exactly 1 way, so total/6 = #Pasch."""
    import itertools as it
    bset=set(blocks); n=0
    for i in range(len(blocks)):
        for j in range(i+1,len(blocks)):
            s=set(blocks[i])&set(blocks[j])
            if len(s)!=1: continue
            p=s.pop()
            x=list(set(blocks[i])-{p}); y=list(set(blocks[j])-{p})
            V=set(p for b in blocks for p in b)
            for z in sorted(V):
                if z==p or z in x or z in y: continue
                t1=tuple(sorted((x[0],y[0],z))); t2=tuple(sorted((x[1],y[1],z)))
                if t1 in bset and t2 in bset: n+=1
                t3=tuple(sorted((x[0],y[1],z))); t4=tuple(sorted((x[1],y[0],z)))
                if t3 in bset and t4 in bset: n+=1
    assert n%6==0, n
    return n//6

def count_mitre_A(blocks):
    """Brute force over 7-sets: inside-blocks==5 and isomorphic to mitre.
    Mitre check: degree sequence must be 3,2,2,2,2,2,1? root deg 3 (abe,acf,adg -> a in 3),
    b,c,d,e,f,g degrees: b:2(abe,bcd),c:2,b? let's compute: a:3,b:2,c:2,d:2,e:2,f:2,g:2 minus... e in abe? no abe has a,b,e; efg has e,f,g -> e:2. total deg sum=15=5*3. degrees: a=3, all others 2 except... b:2,c:2,d:2,e:2,f:2,g:2 -> but that sums 3+12=15. wait g:2 (adg,efg). yes.
    Hmm but root is unique deg-3? All others deg 2. But other 5-block configs on 7 pts could share deg seq; verify structure explicitly."""
    n=0; wit=[]
    for s in itertools.combinations(range(21),7):
        ss=set(s)
        inside=[b for b in blocks if set(b)<=ss]
        if len(inside)!=5: continue
        deg=collections.Counter(p for b in inside for p in b)
        if sorted(deg.values())!=[1,2,2,2,2,3,3]:  # placeholder; refine below
            pass
        # explicit structural test
        if is_mitre(inside):
            n+=1; wit.append((s,inside))
    return n,wit

def is_mitre(five):
    pts=set(p for b in five for p in b)
    if len(pts)!=7: return False
    deg=collections.Counter(p for b in five for p in b)
    ds=sorted(deg.values())
    # mitre degrees: a:3, b,c,d,e,f,g: 2,2,2,2,2,1? recompute: abe,acf,adg,bcd,efg:
    # a: abe,acf,adg =3; b: abe,bcd=2; c: acf,bcd=2; d: adg,bcd=2; e: abe,efg=2; f: acf,efg=2; g: adg,efg=2. sum=15. so [2,2,2,2,2,2,3].
    if ds!=[2,2,2,2,2,2,3]: return False
    root=[p for p in pts if deg[p]==3][0]
    legs=[set(b)-{root} for b in five if root in b]
    if len(legs)!=3 or any(len(l)!=2 for l in legs): return False
    # legs pairwise disjoint?
    u=set()
    for l in legs:
        if u&l: return False
        u|=l
    # remaining 2 blocks must avoid root and cover pattern: one is triple inside union? bcd uses one point from each leg; efg uses one from each leg.
    rest=[set(b) for b in five if root not in b]
    if len(rest)!=2: return False
    for r in rest:
        # r must meet each leg exactly once (transversal)
        if not all(len(r&l)==1 for l in legs): return False
    return True

def count_mitre_B(blocks):
    """Root-based: for each point a and each triple of blocks through a with pairwise-disjoint
    outsides {b,e},{c,f},{d,g}, check whether {b,c,d} and {e,f,g} (up to pairing of the two
    outside points per leg) are both blocks. Each mitre has unique root (deg-3 point), counted once."""
    bset=set(blocks)
    thr=collections.defaultdict(list)
    for b in blocks:
        for p in b: thr[p].append(b)
    n=0; wit=[]
    for a in range(21):
        bl=thr[a]
        for i,j,k in itertools.combinations(range(len(bl)),3):
            legs=[set(bl[t])-{a} for t in (i,j,k)]
            u=set()
            ok=True
            for l in legs:
                if u&l: ok=False; break
                u|=l
            if not ok: continue
            L0,L1,L2=legs
            # 2^2=4 ways to choose one point per leg for the 'bcd' side (complement = other side)
            seen=set()
            for s0 in L0:
                for s1 in L1:
                    for s2 in L2:
                        t1=tuple(sorted((s0,s1,s2)))
                        t2=tuple(sorted(((L0-{s0}).pop(),(L1-{s1}).pop(),(L2-{s2}).pop())))
                        key=tuple(sorted((t1,t2)))
                        if key in seen: continue
                        seen.add(key)
                        if t1 in bset and t2 in bset:
                            n+=1; wit.append((a,(t1,t2)))
    return n,wit
