"""Standalone finite checks for cycle-bouquet independence homology.

Reproducibility only. Uses standard Python and exact bitset arithmetic over F_2,
plus signed simplicial Lefschetz computations over Z.
The mathematical all-parameter statement is established by the proof, not this code.
"""
from itertools import permutations, product
from collections import defaultdict


def graph(m,L):
    nv=1+m*(L-1)
    edges=[]
    for j in range(m):
        vs=[0]+list(range(1+j*(L-1),1+(j+1)*(L-1)))
        edges.extend(tuple(sorted((vs[i],vs[(i+1)%L]))) for i in range(L))
    return nv, edges


def all_faces(m,L):
    n,edges=graph(m,L)
    adj=[0]*n
    for a,b in edges:
        adj[a]|=1<<b;adj[b]|=1<<a
    faces=[[] for _ in range(n+1)]
    def rec(available,selected):
        if not available:
            faces[selected.bit_count()].append(selected)
            return
        bit=available&-available
        v=bit.bit_length()-1
        rec(available^bit, selected)
        rec((available^bit)&~adj[v], selected|bit)
    # generate each independent subset just once via include/exclude recursion
    rec((1<<n)-1,0)
    return faces


def rank_mod2(faces):
    ranks=[]
    for k in range(1,len(faces)):
        basis={}; lower={s:i for i,s in enumerate(faces[k-1])}; r=0
        for s in faces[k]:
            c=0
            v=s
            while v:
                b=v&-v;v^=b
                c^=1<<lower[s^b]
            while c:
                p=c.bit_length()-1
                if p in basis:c^=basis[p]
                else:
                    basis[p]=c;r+=1;break
        ranks.append(r)
    return ranks


def reduced_betti_mod2(faces):
    rs=rank_mod2(faces)
    # from augmented complex: boundary C_0 -> C_{-1} has rank 1
    betti={}
    for k in range(len(rs)):
        if not faces[k+1]:break
        rk=rs[k]; rkplus=rs[k+1] if k+1<len(rs) else 0
        b=len(faces[k+1])-rk-rkplus
        if b:betti[k]=b
    # above indexing: rs[k]=rank ∂_k, so b_k = faces[k+1]-rs[k]-rs[k+1]
    return betti


def signed_trace(faces,p):
    total=-1  # reduced empty face trace
    for k in range(1,len(faces)):
        for s in faces[k]:
            vs=[i for i in range(len(p)) if s>>i&1]
            transformed=[p[i] for i in vs]
            if set(transformed)!=set(vs):continue
            inv=sum(transformed[i]>transformed[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
            total+=(-1)**(k-1+inv)
    return total


def action(m,L,sigma,flips):
    n=1+m*(L-1)
    p=list(range(n))
    for i in range(m):
        for u in range(1,L):
            v=L-u if flips[i] else u
            p[1+i*(L-1)+u-1]=1+sigma[i]*(L-1)+v-1
    return p


def predict(m,L,sigma,flips):
    q,r=divmod(L,3)
    inv=sum(sigma[i]>sigma[j] for i in range(m) for j in range(i+1,m))
    f=sum(flips)
    if r==0:
        assert q>=2
        return {m*q-1:(-1)**(q*inv+((q+1)//2)*f), m*(q-1):(-1)**((q-1)*inv+((q-1)//2)*f)}
    if r==1:
        return {m*q-1:(-1)**(q*inv+(q//2)*f)}
    return {m*q:(-1)**(q*inv+((q+1)//2)*f)}


def do(m,L):
    faces=all_faces(m,L)
    betti=reduced_betti_mod2(faces)
    expected={j:1 for j in predict(m,L,tuple(range(m)),(0,)*m)}
    assert betti==expected,('betti',m,L,betti,expected)
    nops=0
    for sigma in permutations(range(m)):
        for flips in product((0,1),repeat=m):
            p=action(m,L,sigma,flips)
            T=signed_trace(faces,p)
            P=sum((-1)**j*v for j,v in predict(m,L,sigma,flips).items())
            assert T==P,(m,L,sigma,flips,T,P)
            nops+=1
    print('CHECKED',{'petals':m,'cycle_vertices':L,'simplices':sum(map(len,faces))-1,'mod2_reduced_betti':betti,'group_elements':nops})


def run():
    for case in ((2,4),(2,5),(2,6),(2,7),(2,8),(3,5),(3,6)):
        do(*case)
    print('BOUQUET_CYCLE_HOMOLOGY_AND_SIGNED_CHARACTER_CHECKS_OK')

if __name__=='__main__':run()
