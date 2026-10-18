"""Standalone finite-field checks for the Fourier idempotent census of odd dihedral quandle algebras.

Run: python verify.py
Uses only Python's standard library. Finite tests supplement, not replace, the proof.
"""
from itertools import product
from math import gcd, prod


def orbits_and_exponents(n):
    assert n >= 3 and n % 2 == 1
    unused = set(range(1, n))
    out = []
    while unused:
        seed = min(unused)
        orbit = {seed}
        stack = [seed]
        while stack:
            x = stack.pop()
            for y in ((-x) % n, (2*x) % n):
                if y not in orbit:
                    orbit.add(y)
                    stack.append(y)
        unused.difference_update(orbit)
        d = n // gcd(n, seed)
        t = 1
        y = 2 % d
        while y != 1:
            y = (2*y) % d
            t += 1
        minus_in_doubling = (t % 2 == 0 and pow(2, t//2, d) == d-1)
        exponent = (2**(t//2)+1) if minus_in_doubling else (2**t-1)
        assert len(orbit) == (t if minus_in_doubling else 2*t)
        assert exponent % d == 0
        out.append((seed, frozenset(orbit), t, exponent))
    return out


def predicted_count(n, q):
    assert (q-1) % n == 0
    return 2 * prod(1 + gcd(q-1, row[3]) for row in orbits_and_exponents(n))


def primitive_root(p):
    assert p >= 3
    ds=[]; m=p-1;f=2
    while f*f<=m:
        if m%f==0:
            ds.append(f)
            while m%f==0:m//=f
        f+=1
    if m>1:ds.append(m)
    for g in range(2,p):
        if all(pow(g,(p-1)//d,p)!=1 for d in ds):return g
    raise AssertionError('primitive root not found')


def direct_product(a,b,n,add,mul):
    out=[0]*n
    for i,ai in enumerate(a):
        if ai==0:continue
        for j,bj in enumerate(b):
            if bj:
                k=(2*j-i)%n
                out[k]=add(out[k],mul(ai,bj))
    return tuple(out)


def prime_direct_brute(n,p):
    count=0
    for a in product(range(p),repeat=n):
        if direct_product(a,a,n,lambda x,y:(x+y)%p,lambda x,y:(x*y)%p)==a:
            count+=1
    return count


def check_gf4():
    # F_4 = F_2[t]/(t^2+t+1); elements 0,1,t,t+1 encoded 0..3.
    def add(a,b):return a^b
    def mul(a,b):
        c=0
        for i in range(2):
            if a & (1<<i):
                for j in range(2):
                    if b & (1<<j):c ^= (1<<(i+j))
        if c&8:c ^= (8|4|2)   # general guard; degree cannot exceed 2
        if c&4:c ^= (4|2|1)
        return c
    got=sum(1 for a in product(range(4),repeat=3) if direct_product(a,a,3,add,mul)==a)
    assert got==predicted_count(3,4)==8,(got,predicted_count(3,4))
    print('GF4_FULL_IDEMPOTENTS',got)


def split_field_replay(n,p):
    assert (p-1)%n==0
    g=primitive_root(p)
    omega=pow(g,(p-1)//n,p)
    assert pow(omega,n,p)==1 and all(pow(omega,k,p)!=1 for k in range(1,n))
    rows=orbits_and_exponents(n)
    options=[]
    for seed,orbit,t,M in rows:
        roots=[u for u in range(1,p) if pow(u,M,p)==1]
        assert len(roots)==gcd(M,p-1)
        opts=[{}]
        for u in roots:
            data={}; a=u; k=seed
            for _ in range(t):
                data[k]=a
                data[(-k)%n]=pow(a,-1,p)
                a=(a*a)%p;k=(2*k)%n
            assert k==seed and a==u
            assert len(data)==len(orbit)
            for j,v in data.items():assert (data[(-j)%n]*data[(2*j)%n])%p==v
            opts.append(data)
        options.append(opts)
    result=set()
    for choices in product(*options):
        A=[0]*n
        for item in choices:
            for k,v in item.items():
                assert A[k]==0
                A[k]=v
        for zero_frequency in (0,1):
            A[0]=zero_frequency
            # Inverse finite Fourier transform.
            invn=pow(n,-1,p)
            coeff=tuple((invn*sum(A[k]*pow(omega,(-k*j)%n,p) for k in range(n)))%p for j in range(n))
            assert coeff not in result
            result.add(coeff)
            assert sum(coeff)%p==zero_frequency
            assert direct_product(coeff,coeff,n,lambda x,y:(x+y)%p,lambda x,y:(x*y)%p)==coeff
    target=predicted_count(n,p)
    assert len(result)==target,(n,p,len(result),target)
    print('FOURIER_TO_NATIVE_IDEMPOTENTS',n,p,target)



def general_orbit_factors(n,q):
    """Arithmetic descent factors without assuming the n-th roots lie in F_q."""
    assert n>=3 and n%2==1 and gcd(n,q)==1
    gamma=orbits_and_exponents(n)
    index={k:i for i,(_,O,_,_) in enumerate(gamma) for k in O}
    unseen=set(range(1,n)); out=[]
    s=1; x=q%n
    while x!=1:
        x=x*q%n; s+=1
    while unseen:
        k=min(unseen)
        full={k}; todo=[k]
        while todo:
            v=todo.pop()
            for w in ((-v)%n,(2*v)%n,(q*v)%n):
                if w not in full:
                    full.add(w);todo.append(w)
        unseen.difference_update(full)
        d=n//gcd(n,k)
        t=next(t for seed,O,t,M in gamma if k in O)
        M=next(M for seed,O,t_,M in gamma if k in O)
        j=1; v=q*k%n
        while index[v]!=index[k]:
            j+=1;v=v*q%n
        assert s%j==0
        b=next((eps*2**b for eps in (1,-1) for b in range(t)
                if (eps*2**b*k-v)%n==0),None)
        assert b is not None
        g=gcd(M,q**s-1,abs(q**j-b))
        assert len(full)==j*len(gamma[index[k]][1])
        out.append((k,len(full),j,M,b,g))
    return out


def general_count(n,q):
    return 2*prod(1+x[-1] for x in general_orbit_factors(n,q))


def non_split_prime_checks():
    count=0
    for n,p in ((3,2),(5,2),(7,2),(9,2),(11,2),
                (5,3),(7,3),(11,3),(3,5),(7,5)):
        predicted=general_count(n,p)
        if p**n<=200000:
            brute=prime_direct_brute(n,p)
            assert predicted==brute,(n,p,predicted,brute)
            print('NON_SPLIT_FULL_BRUTE',n,p,brute)
        else:
            print('NON_SPLIT_COUNT',n,p,predicted)
        count+=1
    assert general_count(3,4)==8
    assert general_count(11,23)==24
    assert general_count(11,67)==68
    print('NON_SPLIT_FORMULA_CHECKS_PASSED',count)

def main():
    for n in range(3,80,2):
        rows=orbits_and_exponents(n)
        covered=set().union(*(r[1] for r in rows))
        assert covered==set(range(1,n))
    print('ORBIT_PARTITIONS_PASSED 39')
    check_gf4()
    for n,p in ((3,7),(5,11)):
        got=prime_direct_brute(n,p)
        expected=predicted_count(n,p)
        assert got==expected,(n,p,got,expected)
        print('DIRECT_EXHAUSTIVE_IDEMPOTENTS',n,p,got)
    for n,p in ((3,7),(5,11),(7,29),(9,19),(11,23),(11,67),(13,53),(15,31),(17,103)):
        split_field_replay(n,p)
    non_split_prime_checks()
    print('ALL_QUANDLE_IDEMPOTENT_CHECKS_PASSED')


if __name__=='__main__':main()
