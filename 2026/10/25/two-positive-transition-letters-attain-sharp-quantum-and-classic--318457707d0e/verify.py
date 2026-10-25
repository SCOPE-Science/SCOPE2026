#!/usr/bin/env python3
"""Reproducible finite-dimensional checks of reversible two-letter simulation.
No numerical experiment is used as a proof of the universal statements.
Run: python verify.py
"""
import itertools
import numpy as np


def perm(n, p):
    M=np.zeros((n,n),dtype=complex)
    for j,i in enumerate(p): M[i,j]=1
    return M


def original_to_pair(original):
    # Any m>=2 unitaries, with r=m-1 copies of the original space.
    m=len(original); d=original[0].shape[0]; r=m-1
    P=original[0]; Q=original[1:]
    A=np.zeros((r*d,r*d),complex); B=np.zeros_like(A)
    for i in range(r):
        dst=(i+1)%r
        A[dst*d:(dst+1)*d,i*d:(i+1)*d]= P if i==r-1 else np.eye(d)
        B[i*d:(i+1)*d,i*d:(i+1)*d]=Q[i]
    macros=['a'*r]
    for j in range(r): macros.append('a'*j+'b'+'A'*j)
    return A,B,macros


def pair_to_binary(A,B):
    k=A.shape[0]
    C=[np.eye(k,dtype=complex),B.conj().T,A.conj().T]
    s=np.zeros((6*k,6*k),complex)
    t=np.zeros_like(s)
    for i in range(3):
        # t sends both 3-cycles one step forward
        for offset in (0,3):
            t[(offset+(i+1)%3)*k:(offset+(i+1)%3+1)*k,(offset+i)*k:(offset+i+1)*k]=np.eye(k)
        # s switches U_i and V_(-i mod 3) with reciprocal fibers
        v=3+((-i)%3)
        s[v*k:(v+1)*k,i*k:(i+1)*k]=C[i]
        s[i*k:(i+1)*k,v*k:(v+1)*k]=C[i].conj().T
    code={'a':'stst','A':'ttstts','b':'sttstt','B':'tsts'}
    return s,t,code


def eval_word(word,maps):
    d=next(iter(maps.values())).shape[0]
    x=np.eye(d,dtype=complex)
    for c in word: x=maps[c] @ x
    return x


def test(original):
    m=len(original); d=original[0].shape[0]
    A,B,macro=original_to_pair(original)
    S,T,codes=pair_to_binary(A,B)
    AB={'a':A,'A':A.conj().T,'b':B,'B':B.conj().T}
    ST={'s':S,'t':T}
    assert np.allclose(S.conj().T@S,np.eye(6*A.shape[0]))
    assert np.allclose(T@T@T,np.eye(6*A.shape[0]))
    assert np.allclose(S@S,np.eye(6*A.shape[0]))
    assert np.allclose(eval_word(codes['a'],ST)[:A.shape[0],:A.shape[0]],A)
    assert np.allclose(eval_word(codes['b'],ST)[:A.shape[0],:A.shape[0]],B)
    for j,target in enumerate(original):
        w=macro[j]
        macroop=eval_word(w,AB)
        assert np.allclose(macroop[:d,:d],target)
        assert np.allclose(macroop[d:,:d],0)
        binary=''.join(codes[c] for c in w)
        op=eval_word(binary,ST)
        assert np.allclose(op[:d,:d],target)
        assert np.allclose(op[d:,:d],0)
        assert len(binary) <= max(4*(m-1),10*(m-2)+6)
    for w in ['','0','012','30123','010203','33320013']:
        w=''.join(str(int(c)%m) for c in w)
        ow=eval_word(w,{str(j):original[j] for j in range(m)})
        binary=''.join(''.join(codes[c] for c in macro[int(c)]) for c in w)
        bw=eval_word(binary,ST)
        assert np.allclose(ow,bw[:d,:d])
        assert np.allclose(bw[d:,:d],0)
    return 6*(m-1)*d,[len(''.join(codes[c] for c in w)) for w in macro]


def main():
    rng=np.random.default_rng(20913)
    for d in (2,3,4):
        for m in (2,3,4,5):
            base=[perm(d,rng.permutation(d)) for _ in range(m)]
            outcome=test(base)
            print('PERM',d,m,outcome)
            rotations=[]
            for _ in range(m):
                X=rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
                Q,R=np.linalg.qr(X)
                Q=Q@np.diag(np.diag(R)/np.abs(np.diag(R)))
                rotations.append(Q)
            outcome=test(rotations)
            print('UNITARY',d,m,outcome)
    print('VERIFY_OK')

if __name__=='__main__': main()
