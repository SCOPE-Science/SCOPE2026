# Independent mathematical audit

## correctness

PASS

From kσ(n)=(k+1)n+kr follows k|n; writing n=kA and injecting divisors Ak|n gives A(σ(k)−k−1)≤r. If composite k=ph with p least prime divisor and h≥p, the proper divisor h forces Ah≤r and p≤r, so n=pAh≤r². If k=p is prime and n=p^a N, p∤N, T=σ(N)−N, multiplicativity yields (p^{a−1}−1)N+(p^{a+1}−1)T=r(p−1). For a=1, T=1 gives precisely r=p+1, N=q≠p prime, the infinite pq family; T≥2 yields n≤r² by smallest-divisor bound N≤T². For a≥2,T≥1 the equation separately bounds p^aT≤r and N≤r, yielding n≤r². For T=0, N=1 and r=1+p+…+p^{a−2}; a=2 gives r=1,p², while a≥3 implies p^a≤(r−1)^3, with equality for a=3. Thus outside pq, n≤max(r²,(r−1)^3), equal to (r−1)^3 when r≥4. Complete r=1,2,3 follow by finite checking after proven bounds, including (2,8),(9,9) and odd-prime 2q for r=3. Independent divisor-sieve regression for n≤25000 and r≤45 found no counterexample; the unbounded proof is algebraic.

## originality

PASS

Sándor (2022) studies the identical shifted σ equation; Theorem 5 gives only qualitative “finitely many exceptions and/or prime-indexed solutions.” It does not state the all-support (r−1)^3 exception cutoff, the iff infinitude test, or infinitely many sharp prime-cube witnesses. The original already treats small offsets and the semiprime phenomenon; those are properly credited. Exact article comparison, not failed title search, supports additional original quantitative information.

## value

PASS

The source theorem gives only a qualitative fixed-offset finiteness/prime-family statement for the same divisor-sum equation. The reviewed result determines exactly which fixed offsets admit infinitely many n, and provides an explicit sharp polynomial cutoff for all other possibilities without restricting prime support. This turns an ineffective qualitative classification into a finite search domain; the prime-cube witnesses demonstrate a genuinely necessary cubic scale. A full finite exceptional census is not required for this theorem to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
