#!/usr/bin/env python3
"""Exhaustive verifier for cyclic binary composition-spectrum collisions.

Uses integer masks to enumerate every binary word of lengths 1..15.
Computes complete histograms by independent direct slicing and rolling sums,
and checks dihedral orbit coverage and exact collision fibers.
Requires Python 3 standard library only.
"""
from collections import defaultdict
from math import gcd

EXPECTED_COUNTS = {
    1:(2,2), 2:(3,3), 3:(4,4), 4:(6,6), 5:(8,8),
    6:(13,13), 7:(18,18), 8:(30,30), 9:(46,46),
    10:(78,78), 11:(126,126), 12:(224,223),
    13:(380,380), 14:(687,686), 15:(1224,1220),
}
EXPECTED_PAIRS = {
    12:{('001011001101','001011010011')},
    14:{('00101011001101','00101011010011')},
    15:{
        ('000100101001101','000100110100101'),
        ('000100110001101','000100110100011'),
        ('001011010111011','001011101101011'),
        ('001011100111011','001011101100111'),
    },
}

def orbit(w):
    n=len(w)
    return {z[i:]+z[:i] for z in (w,w[::-1]) for i in range(n)}

def canonical(w):
    return min(orbit(w))

def invert(w):
    return ''.join('0' if ch=='1' else '1' for ch in w)

def profile_direct(w):
    n=len(w); ww=w+w
    # Rows for lengths 1,..,n; row k holds counts for weights 0,..,k.
    return tuple(tuple(sum(sum(ch=='1' for ch in ww[i:i+k])==j
                           for i in range(n)) for j in range(k+1))
                 for k in range(1,n+1))

def profile_rolling(w):
    n=len(w); a=[int(ch) for ch in w]; rows=[]
    for k in range(1,n+1):
        s=sum(a[:k]); h=[0]*(k+1)
        for i in range(n):
            h[s]+=1
            s+=a[(i+k)%n]-a[i]
        assert s==sum(a[:k]), 'rolling sum should close after one cycle'
        rows.append(tuple(h))
    return tuple(rows)

def reduced_profile(w):
    p=profile_rolling(w);return (w.count('1'),p[:len(w)//2])

def autocorrelation(w):
    n=len(w); a=[int(ch) for ch in w]
    return (sum(a),)+tuple(sum(a[i]*a[(i+d)%n] for i in range(n))
                           for d in range(1,n//2+1))

def totient(x):
    return sum(gcd(j,x)==1 for j in range(1,x+1))

def bracelet_formula(n):
    rotations=sum(totient(d)*(1<<(n//d)) for d in range(1,n+1) if n%d==0)
    reflections=(n*(1<<((n+1)//2)) if n%2 else (n//2)*((1<<(n//2+1))+(1<<(n//2))))
    assert (rotations+reflections)%(2*n)==0
    return (rotations+reflections)//(2*n)

def run():
    all_fibers={}
    for n in range(1,16):
        fibers=defaultdict(list)
        autocorr_fibers=defaultdict(list)
        total_orbit_members=0
        for mask in range(1<<n):
            w=format(mask, '0{}b'.format(n))
            if canonical(w)!=w:
                continue
            total_orbit_members+=len(orbit(w))
            direct=profile_direct(w)
            rolling=profile_rolling(w)
            assert direct==rolling, (n,w,'independent histogram computations differ')
            m=w.count('1')
            # The complementary window proves the long-window histograms.
            for k in range(1,n):
                for j in range(k+1):
                    if 0<=m-j<=n-k:
                        assert direct[k-1][j]==direct[n-k-1][m-j],(n,w,k,j)
            fibers[reduced_profile(w)].append(w)
            autocorr_fibers[autocorrelation(w)].append(w)
        assert total_orbit_members==1<<n,(n,total_orbit_members)
        assert len(fibers)==EXPECTED_COUNTS[n][1],(n,len(fibers))
        bracelets=sum(map(len,fibers.values()))
        assert bracelets==EXPECTED_COUNTS[n][0]==bracelet_formula(n)
        pairs=set()
        for members in fibers.values():
            if len(members)==2: pairs.add(tuple(sorted(members)))
            else: assert len(members)==1,(n,members)
        assert pairs==EXPECTED_PAIRS.get(n,set()),(n,pairs)
        if n<15:
            for a,b in pairs: assert canonical(invert(a))==b,(n,a,b)
        else:
            for a,b in pairs: assert canonical(invert(a))!=b,(n,a,b)
        all_fibers[n]=fibers
        print('n={:2d} bracelets={:4d} jumbled_profiles={:4d} autocorrelation_profiles={:4d} pairs={}'.format(
            n,bracelets,len(fibers),len(autocorr_fibers),len(pairs)))
    p=EXPECTED_PAIRS[15]
    # The two weight-six pairs are conjugate under complement to the two weight-nine pairs.
    base=sorted((a,b) for a,b in p if a.count('1')==6)
    assert len(base)==2
    for a,b in base:
        mates=tuple(sorted((canonical(invert(a)),canonical(invert(b)))))
        assert mates in p
        assert canonical(a)!=canonical(b)
        assert canonical(invert(a))!=b
        assert a.count('1')==b.count('1')==6
        for mul in range(1,7):
            aa=a*mul;bb=b*mul
            assert profile_direct(aa)==profile_direct(bb),mul
            assert canonical(aa)!=canonical(bb)
            assert canonical(invert(aa))!=canonical(bb)
    print('VERIFY_OK')

if __name__=='__main__': run()
