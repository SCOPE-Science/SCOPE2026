#!/usr/bin/env python3
"""Independent finite checks of 3-Abelian Cantor-like factor classes."""
from collections import defaultdict


def substitution(q, h):
    w = '1'
    for _ in range(h):
        w = ''.join(('1'+'0'*(q-2)+'1') if c == '1' else '0'*q for c in w)
    return w


def via_digits(q, h):
    m=q**h
    def bit(v):
        for _ in range(h):
            if v % q not in (0,q-1):return '0'
            v//=q
        return '1'
    return ''.join(bit(i) for i in range(m))


def three_sigs(seq,n):
    assert n>=3
    cs=[0]*8
    for i in range(n-2):cs[int(seq[i:i+3],2)]+=1
    ans=set()
    for i in range(len(seq)-n+1):
        a=seq[i:i+2];b=seq[i+n-2:i+n]
        ans.add((a,b,tuple(cs)))
        if i+n>=len(seq):break
        cs[int(seq[i:i+3],2)]-=1
        cs[int(seq[i+n-2:i+n+1],2)]+=1
    return ans


def expected(q,k):
    R=2**k
    x={(0,'00','00'),(R,'10','01')}
    pairs={('00','00'),('00','01'),('00','10'),('01','00'),('10','00')}
    for z in range(1,R):
        for a,b in pairs:
            if q==4 and z==R-1 and a==b=='00':continue
            x.add((z,a,b))
    return x


def signatures_to_labels(sigs):
    got={}
    for pre,suf,c in sigs:
        K=sum(c[i] for i in range(8) if i&2)+int(pre[0])+int(suf[-1])
        key=(K,pre,suf)
        if key in got:assert got[key]==c,('duplicate 3-sig',key)
        got[key]=c
    return set(got)


def verify():
    n_cases=0
    for q in (4,5,6,7,8):
        for k in range(1,7):
            if q**(k+1)>200000:continue
            w=substitution(q,k+1)
            assert w==via_digits(q,k+1)
            actual=signatures_to_labels(three_sigs(w,q**k))
            pred=expected(q,k)
            assert actual==pred,(q,k,actual-pred,pred-actual)
            assert len(actual)==(5*2**k-(4 if q==4 else 3)),(q,k)
            n_cases+=1
    print('VERIFY_OK cases='+str(n_cases))


if __name__ == '__main__':verify()
