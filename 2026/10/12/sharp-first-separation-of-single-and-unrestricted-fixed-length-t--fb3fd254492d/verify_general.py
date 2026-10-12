#!/usr/bin/env python3
"""Exact finite tests of the first bounded-versus-unbounded tandem-duplication gap."""
from collections import defaultdict, Counter
from itertools import product, combinations
from math import comb


def trial(q, k):
    n = 3 * k + 1
    derivative_to_word = {}
    fibers = defaultdict(list)
    by_output = defaultdict(set)
    signatures = {}
    roots = {}
    for word in product(range(q), repeat=n):
        h=word[:k]
        z=tuple((word[i+k]-word[i])%q for i in range(n-k))
        inv=list(h)
        for z_i in z:
            inv.append((inv[len(inv)-k] + z_i)%q)
        assert tuple(inv)==word
        nonzeros=[]
        runs=[]
        c=0
        for z_i in z:
            if z_i==0: c+=1
            else:
                runs.append(c)
                nonzeros.append(z_i)
                c=0
        runs.append(c)
        r=[]
        for i,c in enumerate(runs):
            r.extend([0]*(c%k))
            if i<len(nonzeros):r.append(nonzeros[i])
        r=tuple(r)
        sig=tuple(c//k for c in runs)
        key=(h,r)
        fibers[key].append(word)
        signatures[word]=sig
        roots[word]=key
        for i in range(n-k+1):
            out=word[:i+k]+word[i:i+k]+word[i+k:]
            by_output[out].add(word)
            zz=tuple((out[j+k]-out[j])%q for j in range(len(out)-k))
            assert zz == z[:i] + (0,)*k + z[i:]
    conflicts=set()
    for preimages in by_output.values():
        for a,b in combinations(sorted(preimages),2):
            conflicts.add((a,b))
    assert all(roots[a]==roots[b] for a,b in conflicts)
    global_best=0
    global_count=1
    special=Counter()
    for (h,r),fw in fibers.items():
        sigs=[signatures[x] for x in fw]
        # All-pairs equivalence of direct channel overlaps and signature unit transfers.
        local_edges=set()
        for a,b in combinations(fw,2):
            l1=sum(abs(u-v) for u,v in zip(signatures[a],signatures[b]))
            assert ((a,b) in conflicts) == (l1==2)
            if (a,b) in conflicts:local_edges.add(frozenset((a,b)))
        best=0
        num=0
        for m in range(len(fw)+1):
            for sub in combinations(fw,m):
                if all(frozenset((a,b)) not in local_edges for a,b in combinations(sub,2)):
                    if m>best: best,num=m,1
                    elif m==best:num+=1
        if len(r)==2*k+1: expect=(1,1,1)
        elif len(r)==k+1:
            w=sum(x!=0 for x in r)
            expect=(w+1,1,w+1)
        else:
            assert len(r)==1
            expect=(1,1,1) if r[0]==0 else (3,2,1)
        assert (len(fw),best,num)==expect,(q,k,h,r,len(fw),best,num,expect)
        global_best+=best
        global_count*=num
        special[(len(r),sum(x!=0 for x in r),best,num)]+=1
    # Independent count of irreducible roots by direct pattern avoidance.
    def a(length):
        return sum(all(any(z[t+j]!=0 for j in range(k)) for t in range(length-k+1))
                   for z in product(range(q),repeat=length))
    expected=q**k*(a(2*k+1)+a(k+1)+2*q-1)
    unlimited=q**k*(a(2*k+1)+a(k+1)+q)
    expected_count=(2**((k-1)*(q-1)) * __import__('math').prod((w+1)**(comb(k+1,w)*(q-1)**w) for w in range(2,k+2)))**(q**k)
    assert global_best==expected
    assert global_best-unlimited==q**k*(q-1)
    assert global_count==expected_count
    assert special[(1,1,2,1)]==q**k*(q-1)
    print('GENERAL q=%d k=%d n=%d ambient=%d fibers=%d first_maximum=%d unlimited_maximum=%d gap=%d maxima_digits=%d direct_signature_agree=true'%(
        q,k,n,q**n,len(fibers),global_best,unlimited,global_best-unlimited,len(str(global_count)) ))


if __name__=='__main__':
    for q,k in [(2,2),(3,2),(2,3),(2,4)]:
        trial(q,k)
    print('GENERAL_VERIFY_OK q2_k2 q3_k2 q2_k3 q2_k4 checked')
