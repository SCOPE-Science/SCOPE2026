"""Exact finite chain check for two-point unordered configurations of complete multipartite graphs."""
from itertools import combinations, permutations
from math import comb

def data(sizes):
    parts=[]
    for i,n in enumerate(sizes): parts += [i]*n
    V=len(parts)
    edges=[(a,b) for a in range(V) for b in range(a+1,V) if parts[a]!=parts[b]]
    edge_lookup={e:i for i,e in enumerate(edges)}
    c0=list(combinations(range(V),2)); c0_idx={c:i for i,c in enumerate(c0)}
    c1=[(e,v) for e,(a,b) in enumerate(edges) for v in range(V) if v!=a and v!=b]
    c1_idx={c:i for i,c in enumerate(c1)}
    c2=[(e,f) for e,(a,b) in enumerate(edges) for f in range(e+1,len(edges)) if set((a,b)).isdisjoint(edges[f])]
    b1=[]
    for e,v in c1:
        a,b=edges[e]
        b1.append({c0_idx[tuple(sorted((b,v)))]:1,c0_idx[tuple(sorted((a,v)))]:-1})
    b2=[]
    for e,f in c2:
        a,b=edges[e];c,d=edges[f]
        b2.append({c1_idx[(f,b)]:1,c1_idx[(f,a)]:-1,c1_idx[(e,d)]:-1,c1_idx[(e,c)]:1})
    return parts, edges, c0,c1,c2,b1,b2

def rank(columns,mod):
    piv={}
    for c in columns:
        z={k:v%mod for k,v in c.items() if v%mod}
        while z:
            k=min(z)
            if k not in piv:
                inv=pow(z[k],-1,mod)
                piv[k]={i:(x*inv)%mod for i,x in z.items() if (x*inv)%mod}
                break
            fac=z[k]
            for j,v in piv[k].items():
                t=(z.get(j,0)-fac*v)%mod
                if t:z[j]=t
                elif j in z:del z[j]
    return len(piv)

def theo(sizes,fix,two):
    F=sum(fix); E=sum(fix[i]*fix[j] for i in range(len(sizes)) for j in range(i+1,len(sizes)))
    pairs=comb(E,2)-sum(fix[i]*comb(F-fix[i],2) for i in range(len(sizes)))
    c2trace=pairs-2*sum(two[i]*two[j] for i in range(len(sizes)) for j in range(i+1,len(sizes)))
    c1trace=E*(F-2)
    c0trace=comb(F,2)+sum(two)
    return E-F+1,c2trace-c1trace+c0trace-1+(E-F+1), (c0trace,c1trace,c2trace)

def celltraces(parts,edges,c0,c1,c2,p):
    ei={e:i for i,e in enumerate(edges)}
    eperm=[ei[tuple(sorted((p[a],p[b])))] for a,b in edges]
    tr0=sum(tuple(sorted((p[a],p[b])))==(a,b) for a,b in c0)
    tr1=sum(eperm[e]==e and p[v]==v for e,v in c1)
    tr2=0
    for e,f in c2:
        x,y=eperm[e],eperm[f]
        if x==e and y==f:tr2+=1
        if x==f and y==e:tr2-=1
    return tr0,tr1,tr2

def run(sizes,rank_test=True):
    parts,edges,c0,c1,c2,b1,b2=data(sizes)
    assert all(not sum(s*b1[idx].get(r,0) for idx,s in x.items()) for x in b2 for r in range(len(c0))), 'boundary composition'
    N=len(parts); E=len(edges)
    assert len(c0)==comb(N,2)
    assert len(c1)==E*(N-2)
    assert len(c2)==comb(E,2)-sum(comb(N-s,2)*s for s in sizes)
    b1expected=E-N+1
    b2expected=len(c2)-len(c1)+len(c0)-1+b1expected
    if rank_test:
        r1=rank(b1,3);r2=rank(b2,3)
        assert r1==len(c0)-1,(sizes,'r1',r1)
        assert r2==len(c1)-r1-b1expected,(sizes,'r2',r2,len(c1)-r1-b1expected)
        assert len(c2)-r2==b2expected
    # test fixed-cell signed traces for identity, transpositions, 3-cycles in each part, and simultaneous swaps
    perms=[]
    offsets=[sum(sizes[:i]) for i in range(len(sizes))]
    ident=list(range(N)); perms.append(ident)
    for off,s in zip(offsets,sizes):
        p=ident.copy();p[off],p[off+1]=p[off+1],p[off];perms.append(p)
        p=ident.copy();p[off],p[off+1],p[off+2]=p[off+1],p[off+2],p[off];perms.append(p)
    for i,j in combinations(range(len(sizes)),2):
        p=ident.copy()
        for off in (offsets[i],offsets[j]):p[off],p[off+1]=p[off+1],p[off]
        perms.append(p)
    for p in perms:
        f=[];t=[]
        for off,s in zip(offsets,sizes):
            f.append(sum(p[x]==x for x in range(off,off+s)))
            t.append(sum(p[a]==b and p[b]==a for a in range(off,off+s) for b in range(a+1,off+s)))
        h1,h2,expected=theo(sizes,f,t)
        observed=celltraces(parts,edges,c0,c1,c2,p)
        assert observed==expected,(sizes,f,t,observed,expected)
        assert h2==observed[2]-observed[1]+observed[0]-1+h1
    k=len(sizes); q=comb(k,2)
    quotient=(1,q-k+1,3*comb(k,4))
    print('case',sizes,'cells',len(c0),len(c1),len(c2),'bettiQ',(1,b1expected,b2expected),'quotientQ',quotient,'test_perms',len(perms), 'pass')

if __name__=='__main__':
    for sizes in [(3,3,3),(3,3,4),(3,3,3,3)]:run(sizes)
    print('MULTIPARTITE_TWO_PARTICLE_EXACT_CELL_CHECKS_OK')
