#!/usr/bin/env python3
from collections import defaultdict
import base_verify as bv

P = 3

def rotv(v,k):
    return (v+k)%8 if v<8 else 8+((v-8+k)%8)

def rotmask(m,k):
    out=0
    for v in range(16):
        if (m>>v)&1: out |= 1<<rotv(v,k)
    return out

def orientation_sign(m,k):
    vs=[v for v in range(16) if (m>>v)&1]
    imgs=[rotv(v,k) for v in vs]
    pos={x:i for i,x in enumerate(sorted(imgs))}
    p=[pos[x] for x in imgs]
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def rref(A,p):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0; piv=[]; rr=0
    for c in range(n):
        q=next((i for i in range(rr,m) if A[i][c]%p),None)
        if q is None: continue
        A[rr],A[q]=A[q],A[rr]
        inv=pow(A[rr][c]%p,-1,p)
        A[rr]=[(x*inv)%p for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[rr][j])%p for j in range(n)]
        piv.append(c); rr+=1
        if rr==m: break
    return A,piv

def boundary(bydim,d,p):
    src=bydim[d]; tgt=bydim[d-1]; idx={m:i for i,m in enumerate(tgt)}
    A=[[0]*len(src) for _ in tgt]
    for j,m in enumerate(src):
        vs=[v for v in range(16) if (m>>v)&1]
        for q,v in enumerate(vs):
            A[idx[m^(1<<v)]][j]=(1 if q%2==0 else -1)%p
    return A

def null_basis(A,p):
    R,piv=rref(A,p); n=len(A[0]); free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        x=[0]*n; x[f]=1
        for i,c in enumerate(piv): x[c]=(-R[i][f])%p
        out.append(x)
    return out

def col_basis(A,p):
    _,piv=rref(A,p)
    return [[row[j]%p for row in A] for j in piv]

def in_span(cols,v,p):
    if not cols: return all(x%p==0 for x in v)
    M=[[cols[j][i] for j in range(len(cols))] for i in range(len(v))]
    rank=len(rref(M,p)[1]); rank2=len(rref([M[i]+[v[i]%p] for i in range(len(v))],p)[1])
    return rank==rank2

def scalar_on_h4(bydim,k,p):
    D4=boundary(bydim,4,p); D5=boundary(bydim,5,p)
    K=null_basis(D4,p); B=col_basis(D5,p)
    assert len(K)-len(B)==1
    z=next(z for z in K if not in_span(B,z,p))
    idx={m:i for i,m in enumerate(bydim[4])}; gz=[0]*len(z)
    for j,m in enumerate(bydim[4]):
        if z[j]%p:
            jj=idx[rotmask(m,k)]
            gz[jj]=(gz[jj]+orientation_sign(m,k)*z[j])%p
    vals=[]
    for a in (1,p-1):
        if in_span(B,[(gz[i]-a*z[i])%p for i in range(len(z))],p): vals.append(a)
    assert len(vals)==1
    return vals[0]

def main():
    # Replays the complete exact Morse certificate and homology checks first.
    bv.main()
    E=bv.graph_edges(); adj=bv.adjacency_masks(E); faces=bv.enumerate_independent_faces(adj)
    bydim=defaultdict(list)
    for m in faces:
        if m: bydim[m.bit_count()-1].append(m)
    for d in bydim: bydim[d].sort()
    # Verify r is an order-eight graph automorphism.
    eset=set(E)
    for k in range(8):
        mapped={tuple(sorted((rotv(a,k),rotv(b,k)))) for a,b in E}
        assert mapped==eset
    assert all(rotv(v,8)==v for v in range(16))
    # Exact signed simplicial-chain traces and Lefschetz numbers.
    chain_traces=[]; lefs=[]
    for k in range(8):
        tr=[]
        for d in range(8):
            s=sum(orientation_sign(m,k) for m in bydim[d] if rotmask(m,k)==m)
            tr.append(s)
        chain_traces.append(tr)
        lefs.append(sum(((-1)**d)*tr[d] for d in range(8)))
    assert lefs==[-2,0,2,0,-2,0,2,0]
    # The complete Morse certificate above proves H_4(Z)=Z and H_3(Z)=Z^4.
    # Determine the rank-one H_4 action modulo two odd primes; this distinguishes +1 from -1.
    h4=[]
    for k in range(8):
        a3=scalar_on_h4(bydim,k,3); a5=scalar_on_h4(bydim,k,5)
        assert (a3,a5)==((1,1) if k%2==0 else (2,4))
        h4.append(1 if k%2==0 else -1)
    assert h4==[1,-1,1,-1,1,-1,1,-1]
    # Lefschetz: L(r^k)=1-tr(H3)+tr(H4), since all other positive homology vanishes.
    h3=[1+h4[k]-lefs[k] for k in range(8)]
    assert h3==[4,0,0,0,4,0,0,0]
    trivial=[1]*8; sign=h4; v4=[2,0,-2,0,2,0,-2,0]
    assert [trivial[k]+sign[k]+v4[k] for k in range(8)]==h3
    print('EQUIVARIANT_VERIFY_OK')
    print('lefschetz_rotation_powers:',lefs)
    print('H3_character_rotation_powers:',h3)
    print('H4_character_rotation_powers:',h4)
    print('H3_QC8_decomposition: trivial + sign + V4(x^2+1)')
    print('H4_QC8_decomposition: sign')

if __name__=='__main__': main()
