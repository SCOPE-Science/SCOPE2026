#!/usr/bin/env python3
from collections import Counter
from itertools import product
from math import comb


def conv(a,b):
    out=Counter()
    for i,ai in a.items():
        for j,bj in b.items():
            out[i+j]+=ai*bj
    return out


def add_scaled(out, src, scale=1):
    for k,v in src.items():
        out[k]+=scale*v


def formula(n):
    if n%2==0:
        h=n//2+1
        p=Counter({2*k-n:comb(n,k) for k in range(h,n+1)})
        return conv(p,p)
    q=(n-1)//2
    A=Counter(); B=Counter(); C=Counter(); D=Counter()
    for k in range(2*q+1):
        c=comb(2*q,k)
        s=2*k-2*q
        wp=1+s
        wm=-1+s
        if wp>=1: A[wp]+=c
        if wp>=3: B[wp]+=c
        if wm>=1: C[wm]+=c
        if wm>=3: D[wm]+=c
    out=conv(A,A)
    add_scaled(out,conv(B,C),2)
    add_scaled(out,conv(D,D),1)
    return out


def brute(n):
    out=Counter()
    endpoint_refined=Counter()
    for vals in product((-1,1), repeat=2*n):
        L=sum(vals[:n]); R=sum(vals[n:])
        alpha=vals[0]; beta=vals[n]
        # Non-bridge vertices see their entire clique; bridge endpoints see
        # their clique plus the opposite bridge endpoint.
        ok=(L>=1 and R>=1 and L+beta>=1 and R+alpha>=1)
        if ok:
            out[L+R]+=1
            endpoint_refined[(alpha,beta,L,R)]+=1
    return out, endpoint_refined


def predicted_min(n):
    if n%2==0:
        return 4, comb(n,n//2+1)**2
    return 2, comb(n-1,(n-1)//2)**2


def structural_check(n, refined):
    # Every accepted function must obey the exact threshold criterion.
    for (alpha,beta,L,R),count in refined.items():
        if count<=0:
            raise AssertionError('nonpositive refined count')
        if not (L>=1 and R>=1 and L+beta>=1 and R+alpha>=1):
            raise AssertionError((n,alpha,beta,L,R))
    # The converse is already exercised by brute() because brute's predicate
    # is exactly the derived criterion; here check parity consequences.
    if n%2==0:
        if any(L<2 or R<2 for (_,_,L,R) in refined):
            raise AssertionError('even threshold failure')
    else:
        for (alpha,beta,L,R) in refined:
            if beta==-1 and L<3: raise AssertionError('odd left bridge failure')
            if alpha==-1 and R<3: raise AssertionError('odd right bridge failure')


def main():
    coefficient_checks=0
    total_labelings=0
    valid_functions=0
    for n in range(2,9):
        b,ref=brute(n)
        f=formula(n)
        total_labelings += 2**(2*n)
        valid_functions += sum(b.values())
        if b != f:
            raise AssertionError((n,b,f))
        structural_check(n,ref)
        coefficient_checks += len(set(b)|set(f))
        mw=min(b)
        if (mw,b[mw]) != predicted_min(n):
            raise AssertionError((n,mw,b[mw],predicted_min(n)))
    print(f'VERIFY_OK n_range=2..8 labelings={total_labelings} valid_functions={valid_functions} coefficient_checks={coefficient_checks} minimum_checks=7 max_order=16')

if __name__=='__main__':
    main()
