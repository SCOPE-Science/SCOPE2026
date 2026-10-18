#!/usr/bin/env python3
"""Recompute the crown graph two-independence complex on small parameter values."""
from itertools import combinations, permutations
from math import comb

def direct_faces(n):
    verts=range(2*n)
    out=[]
    for mask in range(1,1<<(2*n)):
        vv=[i for i in verts if mask>>i&1]
        rem=set(vv);maxcomp=0
        while rem:
            st=[rem.pop()];size=0
            while st:
                v=st.pop();size+=1
                for w in list(rem):
                    if (v<n)!=(w<n) and (v%n)!=(w%n):
                        rem.remove(w);st.append(w)
            maxcomp=max(maxcomp,size)
        if maxcomp<=2:out.append(mask)
    return out

def predicted_faces(n):
    faces=set()
    def all_subsets(vv):
        for r in range(1,len(vv)+1):
            for ss in combinations(vv,r):faces.add(sum(1<<v for v in ss))
    all_subsets(range(n));all_subsets(range(n,2*n))
    for i,j in combinations(range(n),2):
        all_subsets([i,j,i+n,j+n])
    return sorted(faces)

def gf2rank(cols):
    basis={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:
                basis[p]=x;break
    return len(basis)

def fbetti(n,faces):
    bydim={}
    for m in faces:bydim.setdefault(m.bit_count()-1,[]).append(m)
    ranks={}
    for d in range(1,max(bydim)+1):
        rows={m:i for i,m in enumerate(bydim.get(d-1,[]))}
        cols=[]
        for face in bydim.get(d,[]):
            s=0
            for v in range(2*n):
                if face>>v&1:s^=1<<rows[face^(1<<v)]
            cols.append(s)
        ranks[d]=gf2rank(cols)
    bettis={d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0) for d,fs in bydim.items()}
    return [len(bydim.get(d,[])) for d in range(max(bydim)+1)],bettis

def lefschetz(n, faces, sigma, swap):
    total=0
    for m in faces:
        seq=[v for v in range(2*n) if m>>v&1]
        mapped=[sigma[v%n]+(n*((v>=n)^bool(swap))) for v in seq]
        if set(mapped)!=set(seq):continue
        inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        total+=(-1)**(len(seq)-1+inv)
    return total

def check_characters(n,faces):
    for sigma in permutations(range(n)):
        fixed=sum(sigma[i]==i for i in range(n))
        fixed2=sum(sigma[sigma[i]]==i for i in range(n))
        predicted=((fixed-1)**2-(fixed2-1))//2
        for swap in (0,1):
            observed=lefschetz(n,faces,sigma,swap)-1
            assert observed == (1-2*swap)*predicted,(n,sigma,swap,observed,predicted)
    print(f'n={n} checked={2*__import__("math").factorial(n)} equivariant rational character tests')

def main():
    for n in range(2,7):
        a=sorted(direct_faces(n));p=predicted_faces(n)
        assert a==p,(n,len(a),len(p),set(a)^set(p))
        f,b=fbetti(n,a)
        expected={0:1}
        if n>=3:expected[2]=comb(n-1,2)
        assert all(b.get(d,0)==expected.get(d,0) for d in b),(n,b)
        if n>=3:check_characters(n,a)
        print(f'n={n} faces={len(a)} fvector={f} integral_rank_prediction={comb(n-1,2)} mod2_betti={b}')
    print('PASS: exhaustive face and mod-two homology checks, n=2..6')
if __name__=='__main__':main()
