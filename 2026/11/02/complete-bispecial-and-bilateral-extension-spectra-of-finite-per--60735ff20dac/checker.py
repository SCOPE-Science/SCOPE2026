#!/usr/bin/env python3
"""Independent finite-rank brute-force check of the bispecial-extension classification."""
from collections import defaultdict

def mu(w):
    return ''.join('01' if ch == '0' else '00' for ch in w)

def predicted(k):
    q = {1:'0'}
    for j in range(2,k+1):
        q[j] = mu(q[j-1])+'0'
    v=['00'] if k>=3 else []
    for j in range(max(0,k-3)):
        v.append(mu(v[-1])+'0')
    return q, v, {''}|{q[j] for j in range(1,k-1)}|set(v)

def extensions(word):
    f = {''}
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            f.add(word[i:j])
    found = {}
    for w in f:
        if all(a+w in f for a in '01') and all(w+b in f for b in '01'):
            found[w] = {a+b for a in '01' for b in '01' if a+w+b in f}
    return found

def target_D(k,q,v,u):
    if u=='': return {'01','10'} if k==2 else {'00','01','10'}
    if u=='00': return {'01','10'}
    if u in v: return {'01','10'}
    for j in range(1,k-1):
        if u==q[j]:
            if j<=k-3: return {'00','01','10','11'}
            return {'00','01','10','11'}-{str(j%2)*2}
    raise ValueError('unexpected factor')

def check(max_k=8):
    for k in range(2,max_k+1):
        q,v,bisp=predicted(k)
        actual=extensions(q[k])
        assert set(actual)==bisp,(k,'factor mismatch',set(actual)^bisp)
        for u,d in actual.items():
            assert d==target_D(k,q,v,u),(k,'extension mismatch',u,d,target_D(k,q,v,u))
        assert len(actual)==2*k-3
        print('rank',k,'length',len(q[k]),'bispecials',len(actual),'extension_profile_ok')
    print('VERIFY_OK')

if __name__ == '__main__': check()
