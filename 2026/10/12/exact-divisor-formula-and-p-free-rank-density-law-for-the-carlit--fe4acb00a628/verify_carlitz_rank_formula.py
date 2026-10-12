#!/usr/bin/env python3
import itertools, math

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    x=n; k=0; d=2
    while d*d<=x:
        if x%d==0:
            x//=d; k+=1
            if x%d==0: return 0
            while x%d==0: x//=d
        d += 1
    if x>1: k+=1
    return -1 if k%2 else 1

def characteristic(q):
    for p in range(2,q+1):
        if q%p==0 and all(p%d for d in range(2,int(p**0.5)+1)):
            x=q
            while x%p==0: x//=p
            if x==1: return p
    raise ValueError(q)

def vp(n,p):
    a=0
    while n%p==0:
        n//=p; a+=1
    return a

def rank_formula(q,n):
    p=characteristic(q); L=q-q//p
    num=0
    for d in divisors(n):
        inner=sum(mobius(e)*math.gcd(e,p-1)*pow(L,d//e) for e in divisors(d))
        assert inner%(p-1)==0
        C=inner//(p-1)
        assert C%d==0
        num += pow(p,vp(d,p))*(C//d)
    return num

def least_period(w):
    n=len(w)
    for d in divisors(n):
        if all(w[i]==w[i%d] for i in range(n)):
            return d
    raise AssertionError

def canonical_rotation(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def direct_rank(q,n):
    p=characteristic(q)
    E=tuple(l for l in range(q-1) if (l+1)%p != 0)
    seen=set(); r=0
    for w in itertools.product(E, repeat=n):
        c=canonical_rotation(w)
        if c in seen: continue
        seen.add(c)
        d=least_period(w)
        prod=1
        for x in w[:d]: prod=(prod*((x+1)%p))%p
        if prod==1:
            r += pow(p,vp(d,p))
    return r

def main():
    brute_cases=0
    for q,max_n in [(3,7),(4,5),(5,4),(7,3),(8,3),(9,3)]:
        for n in range(1,max_n+1):
            a=rank_formula(q,n); b=direct_rank(q,n)
            assert a==b,(q,n,a,b)
            brute_cases+=1
    table={
        3:[1,1,4,2,4,16], 4:[2,4,4,16,8,24], 5:[1,2,6,16,256],
        7:[1,3,12,54], 8:[4,16,24,256], 9:[3,9,108,162],
        16:[8,64,176], 25:[5,50], 27:[9,81], 32:[16,256], 64:[32,1024]
    }
    table_cases=0
    for q,vals in table.items():
        for n,expected in enumerate(vals,1):
            got=rank_formula(q,n)
            assert got==expected,(q,n,got,expected)
            table_cases+=1
    pp_cases=0
    for q in [3,4,5,7,8,9,16,25]:
        p=characteristic(q); L=q-q//p
        n=1
        for _ in range(4):
            assert rank_formula(q,n)==pow(L,n)//(p-1),(q,n)
            pp_cases+=1
            n*=p
    q3=[rank_formula(3,n) for n in range(1,10)]
    print(f'VERIFY_OK brute_orbit_cases={brute_cases} published_table_entries={table_cases} p_power_cases={pp_cases} q3_n1_9='+','.join(map(str,q3)))

if __name__=='__main__':
    main()
