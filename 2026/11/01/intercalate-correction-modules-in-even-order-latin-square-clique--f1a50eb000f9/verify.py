"""Standalone finite tests for Latin-square clique-complex translation characters.
No external dependencies. Run with Python 3.10+.
"""
from itertools import product, combinations
from math import comb, prod, pi
import cmath


def add(a,b,moduli):
    return tuple((x+y)%m for x,y,m in zip(a,b,moduli))

def structure(moduli):
    A=list(product(*(range(m) for m in moduli)))
    zero=(0,)*len(moduli)
    table={a:i for i,a in enumerate(A)}
    n=len(A)
    V=list(product(A,A))
    def edge(x,y):
        return x[0]==y[0] or x[1]==y[1] or add(x[0],x[1],moduli)==add(y[0],y[1],moduli)
    adj=[set() for _ in V]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if edge(V[i],V[j]):adj[i].add(j);adj[j].add(i)
    lines=[]
    for component in range(3):
        for x in A:
            if component==0:S=[i for i,(r,c) in enumerate(V) if r==x]
            elif component==1:S=[i for i,(r,c) in enumerate(V) if c==x]
            else:S=[i for i,(r,c) in enumerate(V) if add(r,c,moduli)==x]
            assert len(S)==n
            lines.append(tuple(S))
    triangles=set()
    tetra=set()
    faces_by_dim={i:set() for i in range(n)}
    for L in lines:
        for s in range(1,n+1):
            faces_by_dim[s-1].update(combinations(L,s))
    rainbow=set()
    for r,c,h in product(A,A,A):
        if h==zero:continue
        triangle=tuple(sorted((V.index((r,c)),V.index((r,add(c,h,moduli))),V.index((add(r,h,moduli),c)))))
        rainbow.add(triangle)
        faces_by_dim[2].add(triangle)
    torsion=[h for h in A if h!=zero and add(h,h,moduli)==zero]
    intercalates=set()
    for h,r,c in product(torsion,A,A):
        cell=(r,c)
        verts=tuple(sorted(V.index(z) for z in [cell,(r,add(c,h,moduli)),(add(r,h,moduli),c),(add(r,h,moduli),add(c,h,moduli))]))
        intercalates.add(verts)
    assert len(intercalates)==len(torsion)*n*n//4
    for f in intercalates:
        for s in range(1,5):faces_by_dim[s-1].update(combinations(f,s))
    # Independently enumerate every triangle and 4-clique from the graph.
    tri=set()
    for i in range(len(V)):
        for j in sorted(q for q in adj[i] if q>i):
            for k in adj[i].intersection(adj[j]):
                if k>j:tri.add((i,j,k))
    assert tri==faces_by_dim[2], (moduli,len(tri),len(faces_by_dim[2]))
    four=set()
    for i,j,k in tri:
        for l in adj[i].intersection(adj[j],adj[k]):
            if l>k:four.add((i,j,k,l))
    assert four==faces_by_dim[3],(moduli,len(four),len(faces_by_dim[3]))
    # Higher cliques must lie in one line (the primary structural theorem).
    for d in range(4,n):
        for f in faces_by_dim[d]:assert any(set(f)<=set(L) for L in lines)
    assert len(rainbow)==n*n*(n-1)
    assert len(faces_by_dim[0])==n*n
    assert len(faces_by_dim[1])==3*n*n*(n-1)//2
    assert len(faces_by_dim[2])==3*n*comb(n,3)+n*n*(n-1)
    assert len(faces_by_dim[3])==3*n*comb(n,4)+len(intercalates)
    return A,V,faces_by_dim,torsion,intercalates


def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def trace_face_action(faces, vperm):
    result=0
    for face in faces:
        changed=tuple(vperm[i] for i in face)
        if tuple(sorted(changed))!=face:continue
        result+=parity(changed)
    return result

def gf2_rank(columns):
    basis={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k in basis:v^=basis[k]
            else:basis[k]=v;break
    return len(basis)

def boundary_rank(faces_lower,faces_upper):
    index={f:i for i,f in enumerate(faces_lower)}
    cols=[]
    for f in faces_upper:
        vec=0
        for omitted in range(len(f)):
            sub=f[:omitted]+f[omitted+1:]
            vec^=1<<index[sub]
        cols.append(vec)
    return gf2_rank(cols)

def check(moduli):
    A,V,faces,torsion,inter=structure(moduli)
    n=len(A)
    zero=(0,)*len(moduli)
    index={v:i for i,v in enumerate(V)}
    kappa=1+len(torsion)
    chis={}
    for u,v in product(A,A):
        vperm=[index[(add(r,u,moduli),add(c,v,moduli))] for r,c in V]
        chi=sum((-1)**d * trace_face_action(faces[d],vperm) for d in faces)-1 # H2 = chiEuler-1
        expected=prod(n*int(x==zero)-1 for x in (u,v,add(u,v,moduli)))
        correction=n*n//4*sum(1 for h in torsion if (u,v) in ((zero,zero),(h,zero),(zero,h),(h,h)))
        expected-=correction
        assert chi==expected,(moduli,u,v,chi,expected)
        chis[(u,v)]=chi
    # Brute Fourier transform of all characters, independently of the dimension formula.
    def pairing(char,x):return cmath.exp(2j*pi*sum(z*w/m for z,w,m in zip(char,x,moduli)))
    mul=[]
    for alpha,beta in product(A,A):
        value=sum(chis[(u,v)]*(pairing(alpha,u)*pairing(beta,v)).conjugate() for u,v in product(A,A))/(n*n)
        exp=n-len({zero,alpha,beta})
        exp-=sum(pairing(alpha,h).real>0.5 and pairing(beta,h).real>0.5 for h in torsion)
        assert abs(value-exp)<1e-7,(moduli,alpha,beta,value,exp)
        assert exp>=0
        mul.append(exp)
    assert sum(mul)==(n-1)**3-len(inter)
    assert mul[0]==n-kappa
    rows=[sorted(faces[d]) for d in range(4)]
    r2=boundary_rank(rows[1],rows[2]); r3=boundary_rank(rows[2],rows[3]);betti2=len(rows[2])-r2-r3
    assert betti2==(n-1)**3-len(inter),(moduli,betti2,len(inter))
    print('PASS',moduli,'order',n,'involutions',kappa-1,
          'intercalates',len(inter),'faces0123',[len(v) for v in rows],
          'boundary_ranks_2_3',(r2,r3),'H2',betti2,
          'translation-invariants',mul[0],
          'Lefschetz tests',n*n,'Fourier tests',n*n)

if __name__=='__main__':
    for ms in ((6,),(8,),(4,2),(2,2,2)):
        check(ms)
    print('ALL_CHECKS_PASS')
