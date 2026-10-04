from math import prod

def sigma_prime_power(p,e):
    return (p**(e+1)-1)//(p-1)

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

checks=0
candidates=0
for r in range(1,8):
    A=2**(r+1)
    ps=[p for p in primes_upto(A*A) if p>A and p%2 and p<=2*A-3]
    for p in ps:
        qmax=A+(A*(A-1)-1)//(p-A)
        for q in primes_upto(qmax):
            if not (q>p and q%2):
                continue
            # Check the equivalent hyperbola/algebraic inequalities.
            K=A*(p+q-1)-p*q
            hyp=(p-A)*(q-A)
            assert (K>=1) == (hyp<=A*(A-1)-1)
            assert p<=2*A-3 and q<=A*A-1
            checks += 1
            # Corroborative search only: small exponents satisfy the exact
            # almost-perfect equation only if the theorem's inequalities hold.
            for alpha in range(1,5):
                for beta in range(1,5):
                    N=p**alpha*q**beta
                    sig=(A-1)*sigma_prime_power(p,alpha)*sigma_prime_power(q,beta)
                    if sig==A*N-1:
                        candidates += 1
                        D=(A-1)*N*p*q-(A*N-1)*(p-1)*(q-1)
                        assert D>0
                        assert D==N*K+(p-1)*(q-1)
                        assert hyp<=A*(A-1)-1
print(f"VERIFY_OK pair_checks={checks} small_exact_candidates={candidates}")
