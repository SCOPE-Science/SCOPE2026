#!/usr/bin/env python3
import json, math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
CERT=HERE/'certificate.json'

def primes_upto(n):
    s=bytearray(b'\x01')*(n+1)
    s[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if s[p]: s[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if s[i]]

def is_prime_64(n):
    if n<2: return False
    small=(2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if n%p==0: return n==p
    d=n-1; r=0
    while d%2==0: r+=1; d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        a%=n
        if a==0: continue
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x=(x*x)%n
            if x==n-1: break
        else: return False
    return True

def main():
    z=json.loads(CERT.read_text())
    assert z['schema_version']==1 and z['k']==5 and z['cutoff']==50000
    ps=primes_upto(z['cutoff'])
    assert len(ps)==z['prime_count']==5133
    assert set(map(str,ps))==set(z['factorizations'])
    pcache={}
    fmap={}
    maxq=0
    for p in ps:
        fs=z['factorizations'][str(p)]
        prod=1; dd={}
        for q,e in fs:
            assert q<2**64 and e>=1
            maxq=max(maxq,q)
            if q not in pcache: pcache[q]=is_prime_64(q)
            assert pcache[q], (p,q)
            assert q not in dd
            dd[q]=e
            prod*=q**e
        assert prod==p**5-1, p
        fmap[p]=dd
    active=set(ps); removed=[]
    for rnd in z['elimination_witnesses']:
        before=set(active)
        rps=[p for p,q in rnd]
        assert len(rps)==len(set(rps)) and set(rps)<=before
        for p,q in rnd:
            e=fmap[p].get(q,0)
            assert e%5!=0
            for other in before:
                if other!=p:
                    assert fmap[other].get(q,0)==0, (p,q,other)
        active.difference_update(rps); removed.extend(rps)
    assert not active and len(removed)==len(ps) and len(set(removed))==len(ps)
    assert z['final_active']==[]
    print(f'VERIFY_OK cutoff=50000 primes={len(ps)} rounds={list(map(len,z["elimination_witnesses"]))} prime_factors={len(pcache)} max_factor={maxq}')
if __name__=='__main__': main()
