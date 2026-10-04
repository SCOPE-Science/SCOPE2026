#!/usr/bin/env python3
import json, os, math

ROOT=os.path.dirname(os.path.abspath(__file__))

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def leg5_mod_prime_candidate(x):
    r=x%5
    if r==0: return 0
    return 1 if r in (1,4) else -1

def factor_small(n):
    fs={}
    d=2
    while d*d<=n:
        while n%d==0:
            fs[d]=fs.get(d,0)+1
            n//=d
        d=3 if d==2 else d+2
    if n>1: fs[n]=fs.get(n,0)+1
    return fs

def divisors_from_factor(fs):
    ds=[1]
    for p,e in fs.items():
        cur=[]
        pe=1
        for _ in range(e+1):
            cur += [d*pe for d in ds]
            pe*=p
        ds=cur
    return sorted(set(ds))

def is_prime_trial(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def fib_pair_mod(n,m):
    if n==0: return (0,1)
    a,b=fib_pair_mod(n>>1,m)
    c=(a*((2*b-a)%m))%m
    d=(a*a+b*b)%m
    return (d,(c+d)%m) if n&1 else (c,d)

def z_prime(p):
    chi=leg5_mod_prime_candidate(p)
    B=p-chi
    for d in divisors_from_factor(factor_small(B)):
        if fib_pair_mod(d,p)[0]==0:
            return d
    raise AssertionError(("no rank",p))

def pi_prime(q):
    chi=leg5_mod_prime_candidate(q)
    B=(q-1) if chi==1 else 2*(q+1)
    for d in divisors_from_factor(factor_small(B)):
        a,b=fib_pair_mod(d,q)
        if a==0 and b==1:
            return d
    raise AssertionError(("no period",q))

with open(os.path.join(ROOT,"factor_certificate.json"),encoding="utf-8") as f:
    fc=json.load(f)
with open(os.path.join(ROOT,"candidate_certificate.json"),encoding="utf-8") as f:
    cc=json.load(f)

facts={}
for row in fc["indices"]:
    n=row["n"]
    prod=1
    fd={}
    for ps,e in row["factors"]:
        p=int(ps); e=int(e)
        assert p>1 and e>=1
        prod*=p**e
        fd[p]=e
    assert prod==fib(n), ("factor product mismatch",n)
    facts[n]=fd

expected={}
for k in range(4,101,2):
    branches=[
        ("chi_p_plus",k,1,None),
        ("chi_p_minus_chi_q_plus",k+2,-1,1),
        ("chi_p_minus_chi_q_minus",2*(k-2),-1,-1),
    ]
    for branch,n,cp,cq in branches:
        assert n in facts
        for p in facts[n]:
            if p%k!=1 or p==5: continue
            if leg5_mod_prime_candidate(p)!=cp: continue
            q=(p-1)//k
            key=(k,branch,n,p,q)
            expected[key]=(cp,cq)

seen=set()
prime_candidates=0
for row in cc["rows"]:
    k=int(row["k"]); branch=row["branch"]; n=int(row["fibonacci_index"])
    p=int(row["p"]); q=int(row["q"])
    key=(k,branch,n,p,q)
    assert key in expected, ("certificate row not reconstructed",key)
    assert key not in seen
    seen.add(key)
    cp,cq=expected[key]
    status=row["status"]
    if status=="invalid":
        assert q<3 or q%2==0 or q==5
    elif status=="composite":
        d=int(row["composite_divisor"])
        assert 1<d<q and q%d==0
    elif status=="prime_candidate":
        prime_candidates+=1
        assert is_prime_trial(p)
        assert is_prime_trial(q)
        if cq is not None:
            assert leg5_mod_prime_candidate(q)==cq
        z=z_prime(p); pi=pi_prime(q)
        assert z==int(row["z_p"])
        assert pi==int(row["pi_q"])
        assert (pi%z==0)==bool(row["z_divides_pi"])
        assert pi%z!=0, ("surviving candidate",key,z,pi)
    elif status=="prime_wrong_chi_q":
        assert is_prime_trial(q)
        assert cq is not None and leg5_mod_prime_candidate(q)!=cq
    else:
        raise AssertionError(("bad status",status))

assert seen==set(expected), ("screen mismatch",len(seen),len(expected))
assert max(facts)<=196
print(f"VERIFY_OK k_range=4..100 factor_indices={len(facts)} screened={len(seen)} prime_candidates={prime_candidates} survivors=0 max_index={max(facts)}")
