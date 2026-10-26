#!/usr/bin/env python3
"""Exact marked characteristic-five Ciani rank census: independent finite-field checks.
Requires Python 3 standard library only. This is a finite test supplement to the proof.
"""
from collections import Counter


def build_field(n):
    # F5, F25 = F5[u]/(u²-2), F125 = F5[u]/(u³+u+1).
    q=5**n
    assert n in (1,2,3)
    elems=list(range(q))
    digs=[[ (z//5**i)%5 for i in range(n)] for z in elems]
    def pack(v):return sum((x%5)*(5**i) for i,x in enumerate(v))
    add=[[pack([a[i]+b[i] for i in range(n)]) for b in digs] for a in digs]
    mult=[]
    for a in digs:
        row=[]
        for b in digs:
            c=[0]*(2*n-1)
            for i in range(n):
                for j in range(n):c[i+j]+=a[i]*b[j]
            if n==2:
                c[0]+=2*c[2]
            elif n==3:
                c[1]-=c[3]; c[0]-=c[3]
                c[2]-=c[4]; c[1]-=c[4]
            row.append(pack(c[:n]))
        mult.append(row)
    neg=[pack([-a[i] for i in range(n)]) for a in digs]
    return q,add,mult,neg


def census(n):
    q,add,mul,neg=build_field(n)
    sq=[mul[x][x] for x in range(q)]
    ranks=Counter()
    T1=T2=T3=0
    for r in range(q):
        r2=sq[r]
        for s in range(q):
            s2=sq[s]
            rs=mul[r][s]
            for t in range(q):
                t2=sq[t]
                rst=mul[rs][t]
                R=add[add[r2][s2]][t2]
                Delta=add[add[4][rst]][neg[R]]
                if r2==4 or s2==4 or t2==4 or Delta==0:
                    continue
                # H_r = r²-rst+s²t²+2s²+2t²+2; cyclic analogues.
                def H(first2,second2,third2):
                    return add[add[add[first2][neg[rst]]][mul[second2][third2]]][add[mul[2][add[second2][third2]]][2]]
                h0=H(r2,s2,t2)
                h1=H(s2,r2,t2)
                h2=H(t2,r2,s2)
                k=(h0==0)+(h1==0)+(h2==0)
                ranks[3-k]+=1
                if h0==0:T1+=1
                if h0==0 and h1==0:T2+=1
                if h0==h1==h2==0:T3+=1
    eps=(-1)**n
    U=q**3-7*q*q+18*q-17
    E={
      0:4*(1+eps),
      1:6*q-36-18*eps,
      2:3*(q*q-10*q+30+(15-2*q)*eps),
      3:q**3-10*q*q+42*q-75+(6*q-31)*eps,
    }
    eT1=q*q-6*q+10+(7-2*q)*eps
    eT2=2*(q-4-eps)
    eT3=4*(1+eps)
    assert dict(ranks)=={k:v for k,v in E.items() if v!=0},(q,ranks,E)
    assert sum(ranks.values())==U
    assert (T1,T2,T3)==(eT1,eT2,eT3),(q,(T1,T2,T3),(eT1,eT2,eT3))
    print(f'F_{q}: ranks {dict(sorted(ranks.items()))}, smooth={U}, single={T1}, double={T2}, triple={T3}: PASS')

if __name__=='__main__':
    for n in (1,2,3):census(n)
    print('FINITE FIELD CHECKS PASS; universal proof is separate.')
