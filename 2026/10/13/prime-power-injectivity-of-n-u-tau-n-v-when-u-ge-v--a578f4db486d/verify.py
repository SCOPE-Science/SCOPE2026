from sympy import primerange

def F(p,a,u,v):
    return (p**(a*u))*((a+1)**v)

assert 2**6 * 7**3 == 7**3 * 4**3 == 21952
boundary_ray_checks=0
for t in range(1,11):
    assert F(2,6,t,3*t) == F(7,3,t,3*t) == 21952**t
    boundary_ray_checks += 1

primes=list(primerange(2,100))
cases=0
pair_checks=0
for u in range(1,7):
    for v in range(1,u+1):
        seen={}
        for p in primes:
            last=0
            for a in range(1,21):
                val=F(p,a,u,v)
                assert val>last
                last=val
                cases+=1
                if val in seen:
                    raise AssertionError((u,v,seen[val],(p,a),val))
                seen[val]=(p,a)
        pair_checks += len(seen)

ineq_checks=0
for a in range(1,101):
    assert 2**a >= a+1
    if a>1:
        assert 2**a > a+1
    ineq_checks+=1

print(f"VERIFY_OK parameter_pairs={sum(range(1,7))} prime_power_values={cases} stored_values={pair_checks} inequality_checks={ineq_checks} boundary_ray_checks={boundary_ray_checks} base_collision=21952")
