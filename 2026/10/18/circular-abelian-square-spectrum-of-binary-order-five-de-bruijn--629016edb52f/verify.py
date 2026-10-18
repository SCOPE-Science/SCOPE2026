#!/usr/bin/env python3
"""Self-contained exhaustive certificate for circular Abelian squares in binary de Bruijn cycles."""
from collections import Counter
from fractions import Fraction
from math import comb

ORDER = 5
EXPECTED_HIST = {
    73:4,74:4,75:22,76:4,77:28,78:24,79:26,80:36,81:36,82:56,
    83:20,84:28,85:28,86:48,87:44,88:32,89:58,90:44,91:36,92:16,
    93:44,94:56,95:44,96:44,97:52,98:38,99:42,100:42,101:50,102:56,
    103:40,104:54,105:48,106:54,107:44,108:28,109:40,110:36,
    111:36,112:32,113:32,114:26,115:22,116:50,117:28,118:24,
    119:28,120:14,121:24,122:12,123:38,124:20,125:28,126:24,
    127:24,128:16,129:28,130:12,131:28,132:18,133:20,135:4,
    137:6,139:4,140:8,141:16,142:4,145:4,146:4,147:4,154:4,
}

def euler_cycles(n):
    """Explore all tours in the order-(n-1) binary de Bruijn graph, fixing edge 0."""
    edge_count=1<<n
    vmask=(1<<(n-1))-1
    used=[False]*edge_count
    used[0]=True
    sequence=[0]
    def visit(vertex):
        if len(sequence)==edge_count:
            if vertex==0:
                yield ''.join(str(e>>(n-1)) for e in sequence)
            return
        for e in (2*vertex,2*vertex+1):
            if not used[e]:
                used[e]=True;sequence.append(e)
                yield from visit(e&vmask)
                sequence.pop();used[e]=False
    yield from visit(0)

def switch_cycles(n):
    """Independent exhaustive test of all local bijections (incoming->outgoing)."""
    nv=1<<(n-1)
    ne=2*nv
    vmask=nv-1
    for mask in range(1<<nv):
        used=0
        e=0
        edges=[]
        while not (used>>e)&1:
            used|=1<<e
            edges.append(e)
            v=e&vmask
            incoming_bit=e>>(n-1)
            outgoing_bit=incoming_bit^((mask>>v)&1)
            e=2*v+outgoing_bit
        if e==0 and len(edges)==ne:
            yield ''.join(str(q>>(n-1)) for q in edges)

def occurrences_by_half_fast(w):
    size=len(w); doubled=w+w
    pref=[0]
    for c in doubled:
        pref.append(pref[-1]+int(c))
    return tuple(sum(pref[i+h]-pref[i]==pref[i+2*h]-pref[i+h]
                     for i in range(size))
                 for h in range(1,size//2+1))

def occurrences_by_half_direct(w):
    size=len(w); doubled=w+w
    return tuple(sum(doubled[i:i+h].count('1') ==
                     doubled[i+h:i+2*h].count('1') for i in range(size))
                 for h in range(1,size//2+1))

def distinct_count(w):
    size=len(w); doubled=w+w
    factors=set()
    for h in range(1,size//2+1):
        for i in range(size):
            a=doubled[i:i+h]
            b=doubled[i+h:i+2*h]
            if a.count('1')==b.count('1'):
                factors.add(a+b)
    return len(factors)

def canon(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def symmetry_orbit(w):
    output=set()
    for r in (w,w[::-1]):
        output.add(canon(r))
        output.add(canon(''.join('1' if x=='0' else '0' for x in r)))
    return output

def check():
    hist=Counter()
    profiles={}
    for n in range(1,ORDER+1):
        aa=list(euler_cycles(n))
        bb=list(switch_cycles(n))
        expect=1<<( (1<<(n-1))-n )
        assert len(aa)==len(bb)==expect
        assert len(set(aa))==expect and set(aa)==set(bb)
        for w in aa:
            npositions=1<<n
            assert w[:n]=='0'*n
            assert len({(w+w)[i:i+n] for i in range(npositions)})==npositions
            t=occurrences_by_half_fast(w)
            assert t==occurrences_by_half_direct(w)
            observed=sum(t)
            distinct=distinct_count(w)
            expected_difference=sum(((1<<(n-2*h))-1)*comb(2*h,h)
                                    for h in range(1,n//2+1))
            assert observed-distinct==expected_difference
            for h in range(1,n//2+1):
                assert t[h-1]==(1<<(n-2*h))*comb(2*h,h)
            if n==ORDER:
                hist[observed]+=1
                profiles[w]=t
    assert dict(hist)==EXPECTED_HIST
    assert len(profiles)==2048
    assert len(hist)==71 and min(hist)==73 and max(hist)==154
    assert {i for i in range(73,155) if i not in hist}=={134,136,138,143,144,148,149,150,151,152,153}
    minima={w for w,t in profiles.items() if sum(t)==73}
    maxima={w for w,t in profiles.items() if sum(t)==154}
    assert len(minima)==len(maxima)==4
    assert all(symmetry_orbit(w)==minima for w in minima)
    assert all(symmetry_orbit(w)==maxima for w in maxima)
    tot=sum(k*v for k,v in hist.items())
    avg=Fraction(tot,2048)
    var=Fraction(sum(k*k*v for k,v in hist.items()),2048)-avg*avg
    assert avg==Fraction(6597,64)
    assert var==Fraction(1097767,4096)
    print('VERIFY_OK orders=1..5 independent_generators=2 independent_abelian_tests=2')
    print('binary_order5_necklaces=2048 rooted_circular_windows=1048576')
    print('abelian_occurrence_extrema=73:4,154:4 attained_counts=71 gaps=11')
    print('both_extremizer_sets_single_reversal_complement_orbit=True')
    print('mean=6597/64 variance=1097767/4096')
    print('histogram='+','.join(f'{k}:{hist[k]}' for k in sorted(hist)))
    return hist,profiles

if __name__=='__main__':
    check()
