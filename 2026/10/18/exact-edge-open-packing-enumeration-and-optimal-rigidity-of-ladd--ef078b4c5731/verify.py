"""Standalone exact checks for edge-open-packing sets of finite ladders.
Usage: python3 verify.py   (place rational_certificate.json beside this file)
No third-party packages required.
"""
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path

S=(0,1,2,3,4,5)
PAIRS1=((1,1),(1,2),(1,4),(2,4),(4,2))
PAIRS2=((2,1),(2,2),(4,1),(4,4))

def compatible(a,b,pairs):
    return all(not (a&u and b&v) for u,v in pairs)

def trans(a,b,c):
    return compatible(b,c,PAIRS1) and compatible(a,c,PAIRS2)

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if not out[k]: del out[k]
    return out

def monomial(a,px,pz,scale=1):
    return {(i+px,j+pz):scale*v for (i,j),v in a.items()}

def unpack(entries):
    return {(int(i),int(j)):int(v) for ((i,j),v) in entries}

def verify_rational():
    source=Path(__file__).with_name('rational_certificate.json')
    data=json.loads(source.read_text(encoding='utf8'))
    states=[tuple(q) for q in data['state_masks']]
    assert states==sorted((a,b) for a in S for b in S if compatible(a,b,PAIRS1))
    ns=[unpack(q) for q in data['numerators']]
    d=unpack(data['denominator'])
    assert d.get((0,0))==1
    assert d=={(0,0):1,(1,0):-1,(2,1):-2,(3,1):-1,(3,2):-5,(3,3):-1,(4,3):-1,(5,3):1,(5,4):-1}
    expected={(1,0):1,(1,1):1,(2,1):3,(2,2):4,(3,1):1,(3,2):5,(3,3):2,(4,4):1,(5,3):-1,(5,4):1}
    assert ns[states.index((0,0))]==expected
    ids={v:i for i,v in enumerate(states)}
    for i,(a,b) in enumerate(states):
        rhs={}
        for c in (0,1):
            if trans(a,b,c):rhs=add(rhs,monomial(d,1,c))
        for c in S:
            if trans(a,b,c):rhs=add(rhs,monomial(ns[ids[(b,c)]],1,c.bit_count()))
        assert ns[i]==rhs,('rational identity',states[i])
    return len(states)

def exact_polynomials(n):
    dp={(0,0):{0:1}}
    for i in range(n):
        nxt=defaultdict(dict)
        for (a,b),p in dp.items():
            for c in S:
                if i==n-1 and (c&6):continue
                if not trans(a,b,c):continue
                q=nxt[(b,c)]
                for k,v in p.items():q[k+c.bit_count()]=q.get(k+c.bit_count(),0)+v
        dp=nxt
    result={}
    for q in dp.values():
        for k,v in q.items():result[k]=result.get(k,0)+v
    return result

def brute_poly(n):
    e=[]
    for i in range(n):
        e.append((2*i,2*i+1))
        if i<n-1:e.extend(((2*i,2*i+2),(2*i+1,2*i+3)))
    E={frozenset(v) for v in e}
    conflicts=set()
    for i,j in combinations(range(len(e)),2):
        conflict=any(a!=b and frozenset((a,b)) in E and frozenset((a,b)) not in (frozenset(e[i]),frozenset(e[j])) for a in e[i] for b in e[j])
        if conflict:conflicts.add((i,j))
    out={}
    for k in range(len(e)+1):
        cnt=0
        for ind in combinations(range(len(e)),k):
            chosen=set(ind)
            if not any(i in chosen and j in chosen for i,j in conflicts):cnt+=1
        if cnt:out[k]=cnt
    return out

def potential(a,b):
    if b:return b.bit_count()-1
    return 0 if a in (0,3,5) else -1

def verify_potential():
    states=sorted((a,b) for a in S for b in S if compatible(a,b,PAIRS1))
    assert potential(0,0)==0
    for a,b in states:
        for c in S:
            if trans(a,b,c):assert c.bit_count()-1<=potential(b,c)-potential(a,b)
    for a,b in states:
        if b in (0,1):assert potential(a,b)<=0
    return len(states)

def optimum_count_formula(n):
    if n==1:return 1
    return 4 if n%3==2 else 2

def verify_optimum():
    for n in range(1,201):
        p=exact_polynomials(n)
        assert max(p)==n
        assert p[n]==optimum_count_formula(n),n
    return 200

def verify_recurrence():
    # Specialization at z=1: generating denominator 1-t-2t²-7t³-t⁴.
    a=[0]
    for n in range(1,40):a.append(sum(exact_polynomials(n).values()))
    for n in range(5,40):assert a[n]==a[n-1]+2*a[n-2]+7*a[n-3]+a[n-4]
    return a[1:7]

if __name__=='__main__':
    states=verify_rational()
    potential_states=verify_potential()
    combinations_count=0
    for n in range(1,7):
        combinations_count+=2**(3*n-2)
        assert exact_polynomials(n)==brute_poly(n)
    cap=verify_optimum()
    totals=verify_recurrence()
    print('VERIFICATION_OK rational_states=%d potential_states=%d brute_subsets=%d orders=1..6 optimum_orders=1..%d totals=%s' % (states,potential_states,combinations_count,cap,','.join(map(str,totals))))
