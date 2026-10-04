# A 50,000 prime-support injectivity cutoff for the fifth Jordan totient
## Finding
Let \(J_5(n)=n^5\prod_{{p\mid n}}(1-p^{{-5}})\). If distinct positive integers \(m,n\) satisfy \(J_5(m)=J_5(n)\), then the largest prime divisor of \(mn\) is greater than \(50000\). Equivalently, \(J_5\) is injective on the positive integers all of whose prime divisors are at most \(50000\).

## Assumptions and scope
All variables are positive integers. For a collision \(m\ne n\), write \(S\) for the primes dividing \(m\) but not \(n\), and \(T\) for the primes dividing \(n\) but not \(m\). The case \(S=T=\varnothing\) cannot occur for distinct \(m,n\), because equality of the Jordan totients would then force equality of the fifth-power factors contributed by the exponents of their common prime support.

The bound concerns the largest prime divisor, the same natural support-size invariant used in the recent noninjectivity study of Jordan totients. It does not decide whether \(J_5\) is globally injective.

## Proof
Using
\[
J_5(n)=\left(\frac{{n}}{{\operatorname{{rad}}(n)}}\right)^5\prod_{{p\mid n}}(p^5-1),
\]
and cancelling the factors from primes common to \(m\) and \(n\), a collision implies
\[
\frac{{\prod_{{p\in S}}(p^5-1)}}{{\prod_{{p\in T}}(p^5-1)}}\in (\mathbb Q^\times)^5.
\]
Hence, for every prime \(\ell\),
\[
\sum_{{p\in S}} v_\ell(p^5-1)-\sum_{{p\in T}}v_\ell(p^5-1)\equiv0\pmod 5.
\]

Let \(A_0\) be the set of all primes at most \(50000\). Repeatedly apply the following deletion rule. If \(p\in A\) admits a prime \(\ell\) such that \(v_\ell(p^5-1)\not\equiv0\pmod5\) while \(v_\ell(q^5-1)=0\) for every other \(q\in A\), delete \(p\). Such a \(p\) cannot belong to the support of any signed vector with coefficients in \(\{-1,0,1\}\) satisfying all valuation congruences modulo \(5\): the \(\ell\)-coordinate would otherwise be nonzero.

The attached exact certificate starts with all \(5133\) primes at most \(50000\). Four simultaneous deletion rounds remove respectively \(5074,51,5,3\) primes, leaving the empty set. Therefore no nonzero signed support \(S\sqcup T\subseteq A_0\) can satisfy the necessary fifth-power condition. A collision whose prime divisors are all at most \(50000\) is impossible.

## Verification
`certificate.json` gives the complete prime factorization of \(p^5-1\) for every prime \(p\le50000\), together with one uniqueness witness for every deleted prime. `verify.py` independently checks that the keys are exactly the \(5133\) primes up to \(50000\), that every displayed factor is prime, that every factorization multiplies back exactly, and that each deletion witness is unique among the active primes at its round.

All certificate prime factors are below \(2^{{64}}\); the largest is \(6154180859137036001\). The verifier therefore uses the deterministic seven-base Miller--Rabin criterion for the full unsigned 64-bit range. Running `python verify.py` returns:

`VERIFY_OK cutoff=50000 primes=5133 rounds=[5074, 51, 5, 3] prime_factors=8367 max_factor=6154180859137036001`

## Relationship to prior work
Hang Fu's September 20, 2026 preprint *On the noninjectivity of Jordan's totient functions* proves noninjectivity for \(J_3,J_4,J_6\). Its Theorem 1.1 uses the largest prime factor of \(mn\) as a quantitative invariant, giving exact small-support results for \(k=3,4\) and a lower bound for \(k=6\). Its Section 2 also gives the valuation-vector reduction and a general recursive elimination algorithm. The exponent \(k=5\) is not covered by the theorem.

The present result applies that general reduction to the untreated fifth Jordan totient and supplies a complete exact factorization/deletion certificate through prime support \(50000\). OEIS A059378 tabulates values of \(J_5\) but does not provide this prime-support collision cutoff.

## Limitations
The result is finite and does not prove that \(J_5\) is injective, nor does it exhibit a collision. The cutoff \(50000\) is a certified lower bound, not claimed optimal. Literature searches found no matching \(k=5\) support cutoff, but unindexed or differently phrased prior computations remain a residual originality risk.

## References
1. Hang Fu, *On the noninjectivity of Jordan's totient functions*, arXiv:2609.23901v1, first submitted 2026-09-20.
2. OEIS A059378, *Jordan function \(J_5(n)\)*.
