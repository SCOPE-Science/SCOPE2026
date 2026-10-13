#!/usr/bin/env python3
import json, itertools, math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
CERT=json.loads((HERE/'classification_certificate.json').read_text(encoding='utf-8'))

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    for d in range(3,math.isqrt(n)+1,2):
        if n%d==0:return False
    return True

labels=[('1',(0,0,1)),('2',(0,0,2)),('p',(1,0,0)),('q',(0,1,0)),('2p',(2,0,0)),('2q',(0,2,0))]
rows=[]; sols=[]; factor_checks=0; direct_checks=0
for comb in itertools.combinations(labels,4):
    names=[x[0] for x in comb]
    A=sum(x[1][0] for x in comb); B=sum(x[1][1] for x in comb); c=sum(x[1][2] for x in comb)
    u=3+B; v=3+A; K=u*v+c+3
    admiss=[]
    for d in divisors(K):
        factor_checks += 1
        p=u+d; q=v+K//d
        if p<q and p%2 and q%2 and isprime(p) and isprime(q):
            delta=p*q-3*p-3*q-3
            vals={'1':1,'2':2,'p':p,'q':q,'2p':2*p,'2q':2*q}
            if sum(vals[z] for z in names)==delta:
                admiss.append({'d':d,'p':p,'q':q,'n':2*p*q}); sols.append(2*p*q)
    rows.append({'subset':names,'A':A,'B':B,'c':c,'K':K,'admissible_prime_pairs':admiss})
regen={'schema_version':1,'claim':CERT['claim'],'patterns':rows,'solutions':sorted(set(sols))}
assert regen==CERT
assert CERT['solutions']==[238,310,322]
# Directly confirm divisor sums and existence of exactly four displayed deficient divisors.
for n in CERT['solutions']:
    ps=[]; m=n
    for p in range(2,n+1):
        if m%p==0 and isprime(p):
            ps.append(p)
            while m%p==0:m//=p
        if m==1:break
    assert len(ps)==3 and ps[0]==2
    p,q=ps[1],ps[2]
    sigma=(1+2)*(1+p)*(1+q)
    delta=2*n-sigma
    proper=[d for d in divisors(n) if d<n]
    witnesses=[]
    for S in itertools.combinations(proper,4):
        direct_checks += 1
        if sum(S)==delta:witnesses.append(S)
    assert witnesses
print(f'VERIFY_OK patterns={len(rows)} factor_checks={factor_checks} direct_checks={direct_checks} solutions={CERT["solutions"]}')
