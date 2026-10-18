#!/usr/bin/env python3
"""Self-contained finite-field spot checks for a bipartite evolution algebra theorem.
The exhaustive tests independently scan ALL q^(d*d) matrices, not just proposed normal forms.
Standard-library Python plus NumPy; no external data or files required.
"""
import itertools
import numpy as np


def all_matrices(q, d, batch=100000):
    limit=q**(d*d)
    powers=(q**np.arange(d*d,dtype=np.int64))[None,:]
    for lo in range(0,limit,batch):
        ids=np.arange(lo,min(limit,lo+batch),dtype=np.int64)[:,None]
        a=(ids//powers)%q
        yield a.reshape((-1,d,d)).astype(np.int16)


def det_nonzero(M,q):
    d=M.shape[1]
    if d==2:
        return ((M[:,0,0]*M[:,1,1]-M[:,0,1]*M[:,1,0])%q)!=0
    if d==3:
        a,b,c=M[:,0,0],M[:,0,1],M[:,0,2]
        d_,e,f=M[:,1,0],M[:,1,1],M[:,1,2]
        g,h,i=M[:,2,0],M[:,2,1],M[:,2,2]
        return ((a*(e*i-f*h)-b*(d_*i-f*g)+c*(d_*h-e*g))%q)!=0
    raise ValueError('direct enumeration supports d=2,3')


def full_count(q,m,n):
    d=m+n
    assert d<=3
    count=0
    for T in all_matrices(q,d):
        mask=det_nonzero(T,q)
        # A=U+V with x*y=(x_V.y_V) 1_U+(x_U.y_U) 1_V.
        for i in range(d):
            side=range(m,d) if i<m else range(m)
            lhs=T[:,:,list(side)].sum(axis=2)%q
            vv=np.sum(T[:,m:,i]**2,axis=1)%q
            uu=np.sum(T[:,:m,i]**2,axis=1)%q
            mask &= np.all(lhs[:,:m]==vv[:,None],axis=1)
            mask &= np.all(lhs[:,m:]==uu[:,None],axis=1)
        for i in range(d):
            for j in range(i+1,d):
                mask &= (np.sum(T[:,:m,i]*T[:,:m,j],axis=1)%q)==0
                mask &= (np.sum(T[:,m:,i]*T[:,m:,j],axis=1)%q)==0
        count+=int(mask.sum())
    return count


def orthogonal_stabilizer(q,d):
    count=0
    for M in all_matrices(q,d):
        mask=np.all((M.sum(axis=2)%q)==1,axis=1) # M*(1,...,1)=(1,...,1)
        for i in range(d):
            for j in range(i,d):
                val=np.sum(M[:,:,i]*M[:,:,j],axis=1)%q
                mask &= val==(1 if i==j else 0)
        count+=int(mask.sum())
    return count


def orthogonal_stabilizer_f4(d):
    # F_4 = F_2[a]/(a^2+a+1), encoding 0,1,a,a+1 by binary digits.
    tab=np.zeros((4,4),dtype=np.uint8)
    for x in range(4):
        for y in range(4):
            c0=(x&1)*(y&1)
            c1=((x&1)*((y>>1)&1))^(((x>>1)&1)*(y&1))
            c2=((x>>1)&1)*((y>>1)&1)
            tab[x,y]=(c0^c2)|((c1^c2)<<1)
    count=0
    for M in all_matrices(4,d):
        M=M.astype(np.uint8)
        mask=np.all(np.bitwise_xor.reduce(M,axis=2)==1,axis=1)
        for i in range(d):
            for j in range(i,d):
                dot=np.bitwise_xor.reduce(tab[M[:,:,i],M[:,:,j]],axis=1)
                mask &= dot==(1 if i==j else 0)
        count+=int(mask.sum())
    return count


def is_automorphism(T,m,n,q):
    T=np.array(T,dtype=np.int64)%q
    d=m+n
    if np.linalg.matrix_rank(T.astype(float))!=d:
        # used only in examples where determinant nonzero over the integers iff over F_q
        return False
    def prod(x,y):
        return np.array([int(sum(x[m:]*y[m:]))]*m+[int(sum(x[:m]*y[:m]))]*n)%q
    for i in range(d):
        lhs=sum((T[:,j] for j in (range(m,d) if i<m else range(m))),np.zeros(d,dtype=np.int64))%q
        if not np.array_equal(lhs,prod(T[:,i],T[:,i])):return False
        for j in range(i+1,d):
            if any(prod(T[:,i],T[:,j])):return False
    return True


def main():
    for q,m,n,predicted in [(3,1,1,2),(5,1,1,2),(7,1,1,6),(3,1,2,2),(5,1,2,2),(3,2,1,2)]:
        actual=full_count(q,m,n)
        assert actual==predicted, (q,m,n,actual,predicted)
        print('FULL_EXHAUSTIVE_PASS',q,m,n,actual)
    for q,d,expected in [(3,2,2),(5,2,2),(5,3,12)]:
        # For d=2, stabilizer O_1(F_q) has 2 elements for q odd.
        # For d=3 over F_5, anisotropic plane of order 2(5+1)=12.
        actual=orthogonal_stabilizer(q,d)
        assert actual==expected,(q,d,actual,expected)
        print('ORTHOGONAL_EXHAUSTIVE_PASS',q,d,actual)
    assert orthogonal_stabilizer_f4(3)==60
    print('CHARACTERISTIC_TWO_F4_ORTHOGONAL_PASS',60)
    R=np.array([[4,3,4],[3,4,4],[4,4,3]],dtype=np.int64)
    assert np.array_equal(R@R%5,np.eye(3,dtype=np.int64))
    assert np.array_equal(R@np.ones(3,dtype=np.int64)%5,np.ones(3,dtype=np.int64))
    T=np.zeros((4,4),dtype=np.int64)
    T[0,0]=1;T[1:,1:]=R
    assert is_automorphism(T,1,3,5)
    assert (R!=0).all(), 'example must not be permutation-monomial'
    print('EXPLICIT_NONMONOMIAL_PASS',T.tolist())
    print('ALL_TESTS_PASSED')

if __name__=='__main__':main()
