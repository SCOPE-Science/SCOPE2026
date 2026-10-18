"""Finite tests for Euclidean Rips complexes of type-A root configurations.

Requires only Python 3 standard library. General homotopy statements rely on the
symbolic arguments in the accompanying mathematical exposition.
"""
from itertools import permutations, combinations
from collections import Counter
from math import comb, factorial

def roots(n):
    return [(i,j) for i in range(n) for j in range(n) if i!=j]

def sqdist(a,b,n):
    z=[0]*n
    for i,s in ((a[0],1),(a[1],-1),(b[0],-1),(b[1],1)):
        z[i]+=s
    return sum(t*t for t in z)

def scale_faces(n,scale):
    V=roots(n)
    if scale==2:
        maximal=[tuple(k for k,v in enumerate(V) if v[0]==i) for i in range(n)]
        maximal += [tuple(k for k,v in enumerate(V) if v[1]==i) for i in range(n)]
    elif scale==4:
        maximal=[]
        for mask in range(1,(1<<n)-1):
            S={i for i in range(n) if mask>>i&1}
            maximal.append(tuple(k for k,(i,j) in enumerate(V) if i in S and j not in S))
    else:
        raise ValueError('Only the two intermediate clique stages are enumerated')
    faces=set()
    for facet in maximal:
        for d in range(1,len(facet)+1):
            faces.update(combinations(facet,d))
    face_lists={d:sorted(f for f in faces if len(f)==d) for d in range(1,max(map(len,faces))+1)}
    return V,face_lists

def rank_mod_p(boundary_rows, p):
    basis={}
    for vec in boundary_rows:
        col=dict(vec)
        while col:
            j=min(col)
            if j not in basis:
                inv=pow(col[j],-1,p)
                basis[j]={k:(v*inv)%p for k,v in col.items() if (v*inv)%p}
                break
            mul=col[j]
            for k,v in basis[j].items():
                r=(col.get(k,0)-mul*v)%p
                if r:col[k]=r
                else:col.pop(k,None)
    return len(basis)

def betti_mod_p(face_lists,p):
    N={d:len(x) for d,x in face_lists.items()}
    ranks={1:0}
    for d in range(2,max(N)+1):
        ids={f:i for i,f in enumerate(face_lists[d-1])}
        cols=[]
        for f in face_lists[d]:
            cols.append({ids[f[:i]+f[i+1:]]:(-1 if i%2 else 1)%p for i in range(d)})
        ranks[d]=rank_mod_p(cols,p)
    ranks[max(N)+1]=0
    betti={d-1:N[d]-ranks[d]-ranks[d+1] for d in N}
    return betti,ranks

def inversion_parity(a):
    return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def character_lefschetz(V,faces,perm,flip):
    index={v:i for i,v in enumerate(V)}
    image=[index[(perm[j],perm[i]) if flip else (perm[i],perm[j])] for i,j in V]
    total=0
    for d,flist in faces.items():
        phase=(-1)**(d-1)
        for face in flist:
            mapped=[image[i] for i in face]
            if set(mapped)==set(face):
                order={v:i for i,v in enumerate(face)}
                total+=phase*inversion_parity([order[t] for t in mapped])
    return total

def transpositions_count(perm):
    return sum(i<perm[i] and perm[perm[i]]==i for i in range(len(perm)))

def main():
    for n in (4,5,6):
        V=roots(n)
        d2=Counter(sqdist(V[i],V[j],n) for i in range(len(V)) for j in range(i+1,len(V)))
        assert set(d2)=={2,4,6,8}
        assert d2[8]==comb(n,2)
        print('n',n,'vertices',len(V),'pair distances',dict(sorted(d2.items())))
        for s in (2,4):
            V,faces=scale_faces(n,s)
            counts=[len(faces[d]) for d in sorted(faces)]
            euler=sum((-1)**(d-1)*len(fl) for d,fl in faces.items())
            if s==2:
                betti=n*n-3*n+1
                expected_euler=1-betti
            else:
                expected_euler=1+(-1)**(n-2)
            assert euler==expected_euler,(n,s,euler,expected_euler)
            if n<=5:
                for p in (2,3):
                    b,_=betti_mod_p(faces,p)
                    expected={0:1}
                    expected[1 if s==2 else n-2]=(betti if s==2 else 1)
                    assert all(b.get(d,0)==expected.get(d,0) for d in set(b)|set(expected)),(n,s,p,b,expected)
                print('   squared threshold',s,'f-vector',counts,'integral expected',expected, 'mod2/mod3 exact')
            else:
                print('   squared threshold',s,'f-vector',counts,'Euler checked')
        if n==5:
            a=scale_faces(n,2)
            b=scale_faces(n,4)
            for perm in permutations(range(n)):
                f=sum(perm[i]==i for i in range(n))
                t2=transpositions_count(perm)
                sg=inversion_parity(perm)
                for flip in (0,1):
                    T2=(f*f-3*f+1) if not flip else (1-2*t2)
                    L2=character_lefschetz(*a,perm,flip)
                    assert L2==1-T2,(perm,flip,2,L2,T2)
                    T4=sg*((-1)**((n-1)*flip))
                    L4=character_lefschetz(*b,perm,flip)
                    assert L4==1+((-1)**(n-2))*T4,(perm,flip,4,L4,T4)
            print('n 5 all 240 symmetry Lefschetz characters checked')
    print('VERIFY_OK')

if __name__=='__main__':main()
