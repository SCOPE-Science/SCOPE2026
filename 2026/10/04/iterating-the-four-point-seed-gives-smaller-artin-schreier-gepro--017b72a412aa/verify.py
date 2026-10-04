import math

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

def reg(ds):
    return sum(d-1 for d in ds)

def new_odd_type(p,n):
    return [2,2]+[p**i for i in range(1,n-2)]

def old_odd_type(p,n):
    return [3]+[p**i for i in range(1,n-1)]

def new_two_type(n):
    return [2,2]+[2**i for i in range(2,n-1)]

def old_two_type(n):
    return [3]+[2**i for i in range(2,n)]

odd_checks=0
for p in [q for q in primes_upto(97) if q>=3]:
    for n in range(4,31):
        ds=new_odd_type(p,n)
        old=old_odd_type(p,n)
        assert len(ds)==len(old)==n-1
        assert all(a<b for a,b in zip(ds,old))
        r=reg(ds)
        assert r == 2 + sum(p**i-1 for i in range(1,n-2))
        assert r <= p**(n-2)-1
        count=math.prod(ds)
        old_count=math.prod(old)
        assert count == 4*p**((n-3)*(n-2)//2)
        assert old_count == 3*p**((n-1)*(n-2)//2)
        assert old_count*4 == count*3*p**(n-2)
        odd_checks += 1

two_checks=0
for n in range(4,31):
    ds=new_two_type(n)
    old=old_two_type(n)
    assert len(ds)==len(old)==n-1
    assert all(a<b for a,b in zip(ds,old))
    r=reg(ds)
    assert r == 2 + sum(2**i-1 for i in range(2,n-1))
    assert r == 2**(n-1)-n+1
    assert r <= 2**(n-1)-1
    count=math.prod(ds)
    old_count=math.prod(old)
    assert count == 2**(((n-2)*(n-1))//2+1)
    assert old_count == 3*2**(n*(n-1)//2-1)
    assert old_count == count*3*2**(n-3)
    two_checks += 1

# Base-step checks.
assert reg([2,2]) == 2
for p in [q for q in primes_upto(97) if q>=3]:
    assert p-1 >= 2
assert 4-1 >= 2

print(f"odd_prime_dimension_checks={odd_checks}")
print(f"characteristic_two_dimension_checks={two_checks}")
print("base_seed_regularitiy=2")
print("odd_family_cardinality_formula=ok")
print("two_family_cardinality_formula=ok")
print("coordinatewise_strict_improvement=ok")
print("VERIFY_OK")
