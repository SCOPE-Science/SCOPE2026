"""Independent finite checks for two-particle configuration-space character of tripartite graphs.

Usage: python verify_tripartite.py. Pure Python 3, no external packages.
"""
from itertools import combinations, permutations, product
from math import comb


def make(n):
    groups = []
    off=0
    for size in n:
        groups.append(list(range(off,off+size)));off+=size
    verts=list(range(off))
    edges=[(a,b) for i in range(3) for j in range(i+1,3) for a in groups[i] for b in groups[j]]
    c0=list(combinations(verts,2));index0={c:i for i,c in enumerate(c0)}
    c1=[(v,e) for e,(a,b) in enumerate(edges) for v in verts if v!=a and v!=b]
    index1={c:i for i,c in enumerate(c1)}
    c2=[(e,f) for e,(a,b) in enumerate(edges) for f,(c,d) in enumerate(edges) if e<f and len({a,b,c,d})==4]
    d1=[(1<<index0[tuple(sorted((v,edges[e][1])))])^(1<<index0[tuple(sorted((v,edges[e][0])))]) for v,e in c1]
    d2=[]
    for e,f in c2:
        a,b=edges[e];c,d=edges[f]
        bits=0
        for cell in [(b,f),(a,f),(d,e),(c,e)]:bits^=1<<index1[cell]
        d2.append(bits)
    def rank(columns):
        base={}
        for col in columns:
            x=col
            while x:
                k=x.bit_length()-1
                if k not in base:base[k]=x;break
                x^=base[k]
        return len(base)
    for col in d2:
        z=0
        while col:
            lsb=col&-col;i=lsb.bit_length()-1;z^=d1[i];col^=lsb
        assert z==0
    r1=rank(d1);r2=rank(d2)
    b1=len(c1)-r1-r2;b2=len(c2)-r2
    assert r1==len(c0)-1,(n,r1,len(c0))
    assert b1==len(edges)-len(verts)+2,(n,b1)
    expected_formula=comb(len(edges),2)-sum(comb(len(verts)-size,2)*size for size in n)-(len(verts)-3)*len(edges)+comb(len(verts),2)-len(verts)
    assert b2==expected_formula+1,(n,b2,expected_formula)
    return (groups,verts,edges,c0,c1,c2),(r1,r2,b1,b2)


def char_formula(f,t):
    F=sum(f);E=sum(f[i]*f[j] for i,j in combinations(range(3),2));
    fixed_pairs=comb(E,2)-sum(f[i]*comb(F-f[i],2) for i in range(3))
    return fixed_pairs-2*sum(t[i]*t[j] for i,j in combinations(range(3),2))-(F-3)*E+comb(F,2)-F+sum(t)


def char_specht(f,t):
    u=[x-1 for x in f]
    v=[comb(f[i],2)+t[i]-f[i] for i in range(3)]
    a=[comb(f[i],2)-t[i]-u[i] for i in range(3)]
    s=sum(u)+sum(a)
    for i in range(3):
        for j in range(3):
            if i!=j:s+=u[i]*(v[j]+a[j])+v[i]*a[j]
    s+=2*sum(u[i]*u[j] for i,j in combinations(range(3),2))
    s+=3*u[0]*u[1]*u[2]
    for k in range(3):
        i,j=[z for z in range(3) if z!=k]
        s+=u[i]*u[j]*(v[k]+a[k])
    return s


def finite_char(n,dat):
    groups,verts,edges,c0,c1,c2=dat
    eid={edge:i for i,edge in enumerate(edges)}
    for local in product(*[permutations(group) for group in groups]):
        pm={v:w for group,perm in zip(groups,local) for v,w in zip(group,perm)}
        f=[sum(pm[v]==v for v in group) for group in groups]
        t=[sum(1 for a,b in combinations(group,2) if pm[a]==b and pm[b]==a) for group in groups]
        index_edge={e:eid[(pm[a],pm[b])] for e,(a,b) in enumerate(edges)}
        c0trace=sum(tuple(sorted((pm[a],pm[b])))==(a,b) for a,b in c0)
        c1trace=sum(pm[v]==v and index_edge[e]==e for v,e in c1)
        c2trace=0
        for e,h in c2:
            x,y=index_edge[e],index_edge[h]
            if (x,y)==(e,h):c2trace+=1
            elif (x,y)==(h,e):c2trace-=1
        edge_trace=sum(index_edge[e]==e for e in range(len(edges)))
        first_homology_trace=edge_trace-sum(f)+1
        h2=c2trace-c1trace+c0trace-1+first_homology_trace
        predict=char_formula(f,t)
        assert h2==predict==char_specht(f,t),(n,f,t,h2,predict,char_specht(f,t))
    return True

if __name__=='__main__':
    for n in [(3,3,3),(3,3,4),(3,4,4),(4,4,4)]:
        dat,ranks=make(n)
        print('RANK_CHECK',n,'cells',tuple(map(len,dat[3:])), 'ranks/H1/H2',ranks,flush=True)
        if n in [(3,3,3),(3,3,4)]:
            finite_char(n,dat)
            print('ALL_CHARACTER_CLASSES_AND_ELEMENTS_OK',n,flush=True)
    print('VERIFY_OK_COMPLETE_TRIPARTITE_EQUIVARIANT_H2')
