"""Finite checks of the full row-column symmetry H2 theorem for two particles on K_{m,n}.
Independent finite cellular boundary ranks and signed Lefschetz characters.
Only Python standard library; tests sample every conjugacy class in both groups.
"""
from itertools import combinations,permutations
from collections import defaultdict
from math import comb

def parts(n,top=None):
    if n==0:yield ();return
    if top is None:top=n
    for k in range(min(n,top),0,-1):
        for t in parts(n-k,k):yield (k,)+t

def representative(part):
    o=0;p=[]
    for k in part:
        p.extend(o+i+1 for i in range(k-1));p.append(o);o+=k
    return tuple(p)

def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def perm_module_character(cycles,sizes):
    d={(0,)*len(sizes):1}
    for k in cycles:
        dd=defaultdict(int)
        for blocks,num in d.items():
            for i,limit in enumerate(sizes):
                if blocks[i]+k<=limit:
                    new=list(blocks);new[i]+=k;dd[tuple(new)]+=num
        d=dd
    return d.get(tuple(sizes),0)

def specht_character(shape,cycles):
    if not shape or shape[0]<max(shape[1:],default=0):return 0
    answer=0
    for p in permutations(range(len(shape))):
        sizes=tuple(shape[i]-i+p[i] for i in range(len(shape)))
        if min(sizes)<0:continue
        answer+=sign(p)*perm_module_character(cycles,sizes)
    return answer

def V(p):
    n=sum(p)
    return specht_character((n-2,2),p) if n>=4 else 0

def W(p):
    n=sum(p)
    return specht_character((n-2,1,1),p) if n>=3 else 0

def lattice(m,n):
    vertices=list(combinations(range(m+n),2)); idx0={v:i for i,v in enumerate(vertices)}
    edges=[(a,m+b) for a in range(m) for b in range(n)]
    cells1=[(v,e) for v in range(m+n) for e in edges if v not in e]
    idx1={c:i for i,c in enumerate(cells1)}
    cells2=[(e,f) for e,f in combinations(edges,2) if not set(e)&set(f)]
    b1=[]
    for v,(a,b) in cells1:
        b1.append({idx0[tuple(sorted((v,a)))]:-1,idx0[tuple(sorted((v,b)))]:1})
    b2=[]
    for (a,b),(c,d) in cells2:
        b2.append({idx1[(b,(c,d))]:1,idx1[(a,(c,d))]:-1,idx1[(d,(a,b))]:-1,idx1[(c,(a,b))]:1})
    return vertices,edges,cells1,cells2,b1,b2

def rank_mod(columns,p=1000003):
    pivots={}
    for col in columns:
        v={k:(a%p) for k,a in col.items() if a%p}
        while v:
            i=min(v);a=v[i]
            if i not in pivots:
                inv=pow(a,-1,p);pivots[i]={k:t*inv%p for k,t in v.items()};break
            for k,t in pivots[i].items():
                new=(v.get(k,0)-a*t)%p
                if new:v[k]=new
                else:v.pop(k,None)
    return len(pivots)

def traces(m,n,pl,pr,lat):
    verts,edges,cells1,cells2,*_=lat
    p=tuple(pl)+tuple(m+i for i in pr)
    tr0=sum(tuple(sorted((p[a],p[b])))==(a,b) for a,b in verts)
    trV=sum(p[i]==i for i in range(m+n))
    trE=sum((p[a],p[b])==(a,b) for a,b in edges)
    tr1=sum(p[v]==v and (p[e[0]],p[e[1]])==e for v,e in cells1)
    tr2=0
    for e,f in cells2:
        e2=(p[e[0]],p[e[1]]);f2=(p[f[0]],p[f[1]])
        if e2==e and f2==f:tr2+=1
        elif e2==f and f2==e:tr2-=1
    h2=tr2-tr1+tr0+trE-trV
    return h2, (tr0,tr1,tr2,trE,trV)

def check():
    cases=[(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6)]
    for m,n in cases:
        lat=lattice(m,n);vertices,edges,cells1,cells2,b1,b2=lat
        r1=rank_mod(b1);r2=rank_mod(b2)
        ranks=(len(vertices)-r1,len(cells1)-r1-r2,len(cells2)-r2)
        expect=(1,(m-1)*(n-1),m*(m-3)//2*comb(n-1,2)+comb(m-1,2)*n*(n-3)//2)
        assert ranks==expect,(m,n,ranks,expect)
        count=0
        for ml in parts(m):
            for nr in parts(n):
                t,_=traces(m,n,representative(ml),representative(nr),lat)
                want=V(ml)*W(nr)+W(ml)*V(nr)
                assert t==want,(m,n,ml,nr,t,want)
                count+=1
        print('RECTANGULAR_PASS',m,n,'betti',ranks,'cells',(len(vertices),len(cells1),len(cells2)),
              'boundary_ranks',(r1,r2),'character_class_pairs',count)
    print('VERIFY_OK_RECTANGULAR_BIPARTITE_CONFIGURATION_H2')

if __name__=='__main__':check()
