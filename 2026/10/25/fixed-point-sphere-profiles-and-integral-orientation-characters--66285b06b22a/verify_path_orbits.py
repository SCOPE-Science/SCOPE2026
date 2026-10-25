"""Finite checks for fixed-point and orientation formulas of directed path-avoidance complexes."""
from itertools import permutations
from collections import defaultdict

def has_path(n, arcs, selected):
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(arcs):
        if selected>>i&1: adj[u].append(v)
    reach={0};todo=[0]
    while todo:
        u=todo.pop()
        for v in adj[u]:
            if v==n-1:return True
            if v not in reach:reach.add(v);todo.append(v)
    return False

def par(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def orbits(p):
    remaining=set(range(len(p)));res=[]
    while remaining:
        j=min(remaining);cycle=[];k=j
        while k in remaining:
            remaining.remove(k);cycle.append(k);k=p[k]
        res.append(cycle)
    return res

def check(n,arcs,p):
    m=len(arcs);idx={e:i for i,e in enumerate(arcs)}
    ep=[idx[(p[u],p[v])] for u,v in arcs]
    vorbits=orbits(p);eorbits=orbits(ep)
    # Quotient arc set retains multiplicity of different edge orbits.
    qv={v:i for i,O in enumerate(vorbits) for v in O}
    qa=[(qv[arcs[O[0]][0]],qv[arcs[O[0]][1]]) for O in eorbits]
    s=qv[0];t=qv[n-1]; assert s!=t
    # Reindex with source first and sink last to use the same reachability routine.
    perm=[s]+[j for j in range(len(vorbits)) if j not in (s,t)]+[t]
    ren={v:j for j,v in enumerate(perm)}
    qa=[(ren[u],ren[v]) for u,v in qa]
    Q=len(qa);fo=po=0
    all_edges=(1<<m)-1
    for choice in range(1<<Q):
        lift=sum((1<<i) for j,O in enumerate(eorbits) if choice>>j&1 for i in O)
        hasq=has_path(len(vorbits),qa,choice)
        hasg=has_path(n,arcs,lift)
        assert hasq==hasg, ('quotient PF',n,arcs,p,choice)
        hasqcomplement=has_path(len(vorbits),qa,((1<<Q)-1)^choice)
        hasgcomplement=has_path(n,arcs,all_edges^lift)
        assert hasqcomplement==hasgcomplement, ('quotient PM',n,arcs,p,choice)
        fo+= (-1)**(choice.bit_count()-1) if not hasq else 0
        po+= (-1)**(choice.bit_count()-1) if hasqcomplement else 0
    vprime=len(vorbits)-1 # since every vertex except t a nonsink
    assert fo==(-1)**(vprime-2), ('PF quotient euler',n,arcs,p,fo,vprime)
    assert po==(-1)**(Q-vprime-1), ('PM quotient euler',n,arcs,p,po)
    dpf=n-3;dpm=m-n
    assert (-1)**dpf*fo==par([p[i] for i in range(n-1)]), ('PF character',n,arcs,p)
    assert (-1)**dpm*po==par(ep)*par([p[i] for i in range(n-1)]), ('PM character',n,arcs,p)
    # Independent computation: sum signed fixed oriented faces, no quotient reduction.
    lf_pf=lf_pm=0
    for mask in range(1<<m):
        if any(((mask>>i)&1)!=((mask>>ep[i])&1) for i in range(m)):continue
        chosen=[i for i in range(m) if mask>>i&1]
        pp=[chosen.index(ep[i]) for i in chosen]
        contribution= (-1)**(len(chosen)-1)*par(pp) if chosen else -1
        if not has_path(n,arcs,mask):lf_pf+=contribution
        if has_path(n,arcs,all_edges^mask):lf_pm+=contribution
    assert lf_pf==fo and lf_pm==po,('Lefschetz',n,arcs,p,lf_pf,fo,lf_pm,po)


def run():
    checked=0;graphs=0
    for n in range(3,7):
        possible=[(u,v) for u in range(n) for v in range(u+1,n)]
        for flags in range(1<<len(possible)):
            arcs=[e for j,e in enumerate(possible) if flags>>j&1]
            if not arcs or (n==6 and len(arcs)>7) or not has_path(n,arcs,(1<<len(arcs))-1):continue
            paths=[]
            def dfs(u,P):
                if u==n-1:paths.append(P);return
                for e in arcs:
                    if e[0]==u:dfs(e[1],P+[e])
            dfs(0,[])
            if set(arcs)!=set(e for P in paths for e in P):continue
            if any(not any(e[0]==v for e in arcs) for v in range(n-1)):continue
            graphs+=1
            for mid in permutations(range(1,n-1)):
                p=(0,)+mid+(n-1,)
                if any((p[u],p[v]) not in arcs for u,v in arcs):continue
                check(n,arcs,p);checked+=1
        print('n',n,'cumulative essential graphs',graphs,'automorphisms checked',checked,flush=True)
    print('PATH_FREE_PATH_MISSING_FIXED_POINT_CHARACTERS_OK',checked,graphs)
if __name__=='__main__':run()


def layered_group_test():
    n=6
    arcs=sorted([(0,a) for a in (1,2)]+[(a,b) for a in (1,2) for b in (3,4)]+[(b,5) for b in (3,4)])
    ident=tuple(range(6));sa=(0,2,1,3,4,5);sb=(0,1,2,4,3,5);sab=(0,2,1,4,3,5)
    for H in [[ident],[ident,sa],[ident,sb],[ident,sab],[ident,sa,sb,sab]]:
        # Orbits under all elements of a subgroup.
        def orbit_partition(N):
            left=set(range(N));ans=[]
            while left:
                v=min(left);O={v}
                while True:
                    Nxt=O|{p[x] for p in H for x in O}
                    if Nxt==O:break
                    O=Nxt
                left-=O;ans.append(sorted(O))
            return ans
        V=orbit_partition(6)
        ix={e:i for i,e in enumerate(arcs)}
        arcperms=[tuple(ix[(p[u],p[v])] for u,v in arcs) for p in H]
        left=set(range(len(arcs)));E=[]
        while left:
            v=min(left);O={v}
            while True:
                Nxt=O|{pp[x] for pp in arcperms for x in O}
                if Nxt==O:break
                O=Nxt
            left-=O;E.append(sorted(O))
        qv={v:j for j,O in enumerate(V) for v in O}
        qarc=[(qv[arcs[O[0]][0]],qv[arcs[O[0]][1]]) for O in E]
        s=qv[0];t=qv[5];vv=[s]+[j for j in range(len(V)) if j not in (s,t)]+[t]
        ren={j:i for i,j in enumerate(vv)}
        qarc=[(ren[u],ren[v]) for u,v in qarc]
        total=(1<<len(arcs))-1
        for mask in range(1<<len(E)):
            lifted=sum(1<<i for k,O in enumerate(E) if mask>>k&1 for i in O)
            assert has_path(n,arcs,lifted)==has_path(len(V),qarc,mask)
            assert has_path(n,arcs,total^lifted)==has_path(len(V),qarc,((1<<len(E))-1)^mask)
        chiF=sum((-1)**(mask.bit_count()-1) for mask in range(1<<len(E)) if not has_path(len(V),qarc,mask))
        chiM=sum((-1)**(mask.bit_count()-1) for mask in range(1<<len(E)) if has_path(len(V),qarc,((1<<len(E))-1)^mask))
        assert chiF==(-1)**(len(V)-3) and chiM==(-1)**(len(E)-len(V)),(H,V,E,chiF,chiM)
        print('subgroup_order',len(H),'vertex_orbits',len(V),'arc_orbits',len(E),'PF_fixed_sphere_dim',len(V)-3,'PM_fixed_sphere_dim',len(E)-len(V),flush=True)
    print('LAYERED_NETWORK_SUBGROUP_FIXED_POINTS_OK')
if __name__=='__main__':layered_group_test()
