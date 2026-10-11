#!/usr/bin/env python3
from itertools import combinations

# Sparse integer linear maps on the explicit H_3 basis used in the proof.
# A map is a list of columns; each column is {row: coefficient}.

def basis(n):
    U=[('U',i) for i in range(n)]
    W=[('W',a,b) for a in range(n) for b in range(a+1,n)]
    V=[('V',a,b,c) for a in range(n) for b in range(a+1,n) for c in range(b+1,n)]
    return U+W+V

def ident(d): return [{j:1} for j in range(d)]

def add(A,B,sa=1,sb=1):
    C=[]
    for ca,cb in zip(A,B):
        z={}
        for r,v in ca.items(): z[r]=z.get(r,0)+sa*v
        for r,v in cb.items(): z[r]=z.get(r,0)+sb*v
        z={r:v for r,v in z.items() if v}
        C.append(z)
    return C

def compose(A,B): # A after B
    C=[]
    for cb in B:
        z={}
        for mid,c in cb.items():
            for r,a in A[mid].items(): z[r]=z.get(r,0)+a*c
        C.append({r:v for r,v in z.items() if v})
    return C

def equal(A,B): return A==B

def perm_part(n,i):
    B=basis(n); pos={b:k for k,b in enumerate(B)}; cols=[]
    for b in B:
        if b[0]=='U':
            a=b[1]; aa=i+1 if a==i else i if a==i+1 else a
            cols.append({pos[('U',aa)]:1})
        elif b[0]=='W':
            a,c=b[1:]
            mm=[i+1 if x==i else i if x==i+1 else x for x in (a,c)]
            cols.append({pos[('W',)+tuple(sorted(mm))]:1})
        else:
            supp=list(b[1:]); mm=[i+1 if x==i else i if x==i+1 else x for x in supp]
            inv=sum(mm[p]>mm[q] for p in range(3) for q in range(p+1,3))
            cols.append({pos[('V',)+tuple(sorted(mm))]:(-1 if inv%2 else 1)})
    return cols

def tau(n,i):
    B=basis(n); pos={b:k for k,b in enumerate(B)}; S=perm_part(n,i); T=[dict(c) for c in S]
    for j,b in enumerate(B):
        if b[0]=='W':
            a,c=b[1:]
            if (i+1 in (a,c)) and (i not in (a,c)):
                r=a if c==i+1 else c
                vr=pos[('V',)+tuple(sorted((i,i+1,r)))]
                T[j][vr]=T[j].get(vr,0)-2
                if T[j][vr]==0: del T[j][vr]
    return T

def tau_inv(n,i):
    # If T=S+C with S^2=I and (SC)^2=0, then T^{-1}=S-SCS.
    T=tau(n,i); S=perm_part(n,i); C=add(T,S,1,-1)
    return add(S,compose(compose(S,C),S),1,-1)

def pure_A(n,i,j):
    # Standard A_{ij}=tau_{j-1}...tau_{i+1} tau_i^2 tau_{i+1}^{-1}...tau_{j-1}^{-1}
    d=len(basis(n)); M=ident(d)
    word=[]
    for k in range(j-1,i,-1): word.append((k,1))
    word += [(i,1),(i,1)]
    for k in range(i+1,j): word.append((k,-1))
    # Same convention as matrix product used in the paper: append on the right.
    for k,e in word:
        X=tau(n,k) if e==1 else tau_inv(n,k)
        M=compose(M,X)
    return M

def map_diff(A): return add(A,ident(len(A)),1,-1)

def zero_map(d): return [{} for _ in range(d)]

def sum_maps(ms,d):
    z=zero_map(d)
    for M in ms: z=add(z,M)
    return z

def sparse_rank_mod(columns,p=1000003):
    # columns are dict coordinate -> integer; exact rational rank is >= modular rank.
    piv={}
    rank=0
    for col in columns:
        v={k:(x%p) for k,x in col.items() if x%p}
        while v:
            k=min(v)
            if k not in piv:
                a=pow(v[k],p-2,p)
                v={r:(c*a)%p for r,c in v.items() if (c*a)%p}
                piv[k]=v; rank+=1; break
            q=v[k]
            base=piv[k]
            for r,c in base.items():
                nv=(v.get(r,0)-q*c)%p
                if nv: v[r]=nv
                elif r in v: del v[r]
    return rank

def vec_sparse(M,d):
    z={}
    for c,col in enumerate(M):
        for r,v in col.items(): z[r+d*c]=v
    return z

def check(n):
    B=basis(n); d=len(B); I=ident(d); Z=zero_map(d)
    Ts=[tau(n,i) for i in range(n-1)]
    for i,T in enumerate(Ts):
        Ti=tau_inv(n,i)
        assert equal(compose(T,Ti),I) and equal(compose(Ti,T),I)
    for i in range(n-2):
        assert equal(compose(compose(Ts[i],Ts[i+1]),Ts[i]), compose(compose(Ts[i+1],Ts[i]),Ts[i+1]))
    for i in range(n-1):
        for j in range(i+2,n-1): assert equal(compose(Ts[i],Ts[j]),compose(Ts[j],Ts[i]))
    pairs=list(combinations(range(n),2))
    Ns=[map_diff(pure_A(n,*e)) for e in pairs]
    # Pure generators are square-zero transvections whose cross-products vanish.
    for A in Ns:
        assert equal(compose(A,A),Z)
    for A in Ns:
        for C in Ns:
            assert equal(compose(A,C),Z)
    # The unique global relation is sum_e N_e=0.
    assert equal(sum_maps(Ns,d),Z)
    cols=[vec_sparse(N,d) for N in Ns]
    rank=sparse_rank_mod(cols)
    assert rank==len(pairs)-1
    return d,len(pairs),rank

if __name__=='__main__':
    rows=[]
    for n in range(2,9): rows.append((n,)+check(n))
    for n,d,g,r in rows:
        print(f'n={n} H3_basis={d} pure_generators={g} nilpotent_offset_rank={r}')
    print('VERIFY_OK all_cases=2..8 formula=binom(n,2)-1')
