#!/usr/bin/env python3
"""Independent direct finite-field tests of Rota--Baxter equations on small Heisenberg Lie algebras."""
from itertools import product

def omega(v,w,mod,n):
    return sum(v[i]*w[n+i]-v[n+i]*w[i] for i in range(n))%mod

def check_direct_n1(q):
    N=0; pred=0
    e=[[1,0,0],[0,1,0],[0,0,1]]
    def bracket(x,y): return [0,0,(x[0]*y[1]-x[1]*y[0])%q]
    for x in product(range(q), repeat=9):
        P=[[x[3*i+j] for j in range(3)] for i in range(3)]
        images=[[P[i][j] for i in range(3)] for j in range(3)]
        valid=True
        for i in range(3):
            for j in range(i+1,3):
                lhs=bracket(images[i],images[j]); first=bracket(images[i],e[j]); second=bracket(e[i],images[j]); v=[(first[k]+second[k])%q for k in range(3)]
                rhs=[sum(P[k][a]*v[a] for a in range(3))%q for k in range(3)]
                if lhs != rhs: valid=False;break
            if not valid:break
        A00,A01,A10,A11=P[0][0],P[0][1],P[1][0],P[1][1]
        c=P[2][2]
        normal=(P[0][2]==0 and P[1][2]==0 and ((A00*A11-A01*A10-c*(A00+A11))%q==0))
        if valid!=normal: raise AssertionError((q,P,valid,normal))
        N+=valid;pred+=normal
    assert N==q**6,(q,N)
    print('n=1 q=',q,'brute all linear maps:',q**9,'Rota-Baxter:',N)

def form_bits(v,w):
    return ((v&1)*((w>>2)&1)+((v>>1)&1)*((w>>3)&1)+((v>>2)&1)*(w&1)+((v>>3)&1)*((w>>1)&1))&1

def check_n2_q2():
    basis=[1,2,4,8]
    c0=c1=0
    for z in range(1<<16):
        columns=[(z>>(4*j))&15 for j in range(4)]
        # Weight-zero Heisenberg equation after independent P(z)=cz proof.
        zero=one=True
        for i in range(4):
            for j in range(i+1,4):
                left=form_bits(columns[i],columns[j])
                rhs=form_bits(columns[i],basis[j])^form_bits(basis[i],columns[j])
                if left:zero=False
                if left!=rhs:one=False
        # Independently check the symplectic-shift condition.
        B=[columns[i]^basis[i] for i in range(4)]
        sp=all(form_bits(B[i],B[j])==form_bits(basis[i],basis[j]) for i in range(4) for j in range(i+1,4))
        assert sp==one
        c0+=zero;c1+=one
    assert (c0,c1)==(3376,720),(c0,c1)
    print('n=2 q=2 all 4x4 A:',1<<16,'c=0 count:',c0,'c=1 count:',c1)
    print('n=2 q=2 with 16 choices of ell:',(c0+c1)*16)
    # Demonstrate the non-closure obstruction: image isotropic, row image not.
    # A(e1)=e1, A(f1)=e2, other basis elements go to zero.
    cols=[1,0,2,0]
    assert all(form_bits(cols[i],cols[j])==0 for i in range(4) for j in range(i+1,4))
    rows=[sum(((cols[j]>>i)&1)<<j for j in range(4)) for i in range(4)]
    assert any(form_bits(rows[i],rows[j]) for i in range(4) for j in range(i+1,4))
    print('n=2 q=2 nonclosure witness: symplectically isotropic columns but not rows')

if __name__=='__main__':
    check_direct_n1(2)
    check_direct_n1(3)
    check_n2_q2()
    print('HEISENBERG_RB_GEOMETRY_OK')
