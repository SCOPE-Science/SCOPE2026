# First two exceptional primes in the two-digit binomial supercongruence

## Finding
For every odd prime \(p\le71\) and every integer \(t\ge3\), define
\[
B=\frac{p-1}{2},\qquad H=\frac{p^2-1}{2},\qquad A_t=\frac{p^t-1}{2},
\]
\[
S_p(t)=1-\binom{A_t}{B}+\binom{A_t}{pB}-\binom{A_t}{H}.
\]
Then \(S_p(t)\ne0\) and
\[
\nu_p(S_p(t))=\begin{cases}3,&p\in\{7,71\},\\2,&p\notin\{7,71\}.\end{cases}
\]
In particular, \(7\) and \(71\) are the first two odd primes for which the generic two-digit congruence is strictly stronger than divisibility by \(p^2\); its improvement is exactly one extra prime factor, uniformly at all truncation lengths \(t\ge3\).

## Assumptions and scope
The exponent \(t\) is an integer at least three. The prime \(p\) ranges over all nineteen odd primes from \(3\) through \(71\) inclusive. The valuation \(\nu_p\) is the exact exponent of \(p\) dividing a nonzero integer. Here the number of variable base-\(p\) digit positions is two; all other specialized parameters are fixed as above. The case \(t=2\) is excluded because complementary binomial terms cancel identically. No statement is asserted for \(p>71\), more digit positions, other digit choices, or the associated Gaussian polynomial.

## Proof
Write \(K\in\{B,pB,H\}\). Observe \(0<K<p^2\). For every integer \(h\ge0\), every \(0\le j\le K\), and every \(j\ge1\), the elementary identity
\[
j\binom{p^5h}{j}=p^5h\binom{p^5h-1}{j-1}
\]
implies \(\nu_p(\binom{p^5h}{j})\ge5-\nu_p(j)\ge4\) whenever \(h>0\); if \(h=0\), the summand vanishes. Vandermonde's identity consequently gives
\[
\binom{X+p^5h}{K}\equiv\binom{X}{K}\pmod{p^4}
\]
for all nonnegative integers \(X,h\) and every such \(K\).

For \(t\ge5\), we have \(A_t=A_5+p^5h\) with \(h=(p^{t-5}-1)/2\) a nonnegative integer, so
\[
S_p(t)\equiv S_p(5)\pmod{p^4}.
\]
It therefore suffices to evaluate the exact integers \(S_p(3)\), \(S_p(4)\), and \(S_p(5)\) modulo \(p^4\). Every one of these is nonzero. The complete prime-by-prime witness table below lists \(S_p(t)/p^2\) modulo \(p\), for \(t=3,4,5\), respectively. The final column gives \(S_p(3)/p^3\) modulo \(p\) when the first quotient vanishes. All numbers are ordinary least nonnegative residues.

| \(p\) | \(t=3\) | \(t=4\) | \(t=5\) | Exceptional unit |
|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 2 | - |
| 5 | 3 | 3 | 3 | - |
| 7 | 0 | 0 | 0 | 1 |
| 11 | 4 | 4 | 4 | - |
| 13 | 3 | 3 | 3 | - |
| 17 | 7 | 7 | 7 | - |
| 19 | 3 | 3 | 3 | - |
| 23 | 2 | 2 | 2 | - |
| 29 | 28 | 28 | 28 | - |
| 31 | 24 | 24 | 24 | - |
| 37 | 36 | 36 | 36 | - |
| 41 | 32 | 32 | 32 | - |
| 43 | 16 | 16 | 16 | - |
| 47 | 15 | 15 | 15 | - |
| 53 | 5 | 5 | 5 | - |
| 59 | 48 | 48 | 48 | - |
| 61 | 4 | 4 | 4 | - |
| 67 | 13 | 13 | 13 | - |
| 71 | 0 | 0 | 0 | 5 |

For every nonexceptional prime in the table all three quotients are units, yielding exact valuation two. For \(p=7\), all three first quotients vanish, but the quotients by \(7^3\) are each \(1\pmod7\). For \(p=71\), the corresponding quotients by \(71^3\) are each \(5\pmod{71}\). Hence every listed valuation is three and not four for the two exceptional primes, and exactly two for all others. The displayed congruence extends this classification from \(t=3,4,5\) to every \(t\ge5\). This proves the claimed infinite-in-truncation classification.

The finite residue table is reproducible without trusting rounded numerical data: `VERIFY.py` computes the four binomial terms exactly with Python's integer arithmetic and independently modulo \(p^4\) with \(p\)-free numerator/denominator products. It verifies both methods, all fifty-seven cases, all valuations, the exceptional units, and the completeness of the prime list. The input-output table is `CERTIFICATE.tsv`.

## Verification
From the same directory, run `python3 VERIFY.py`. The script has no external dependencies and checks exactly the nineteen odd primes \(p\le71\) and the three required truncations. It compares each exact integer result with an independent multiplicative modular computation modulo \(p^4\). The latter separates the powers of \(p\) from every numerator and denominator, so all modular inverses are taken only of units. The run completes with the literal message `PASS: 19 odd primes through 71; 57 exact signed sums; 57 independent modular evaluations; all valuation and exceptional-unit witnesses agree`. Each check is finite and exhaustive over the stated finite parameters. The unbounded \(t\)-range is covered by the proved Vandermonde reduction, not by extrapolating finite experiments.

## Relationship to prior work
Oscar Gonzalez, *A q-analogue of a binomial supercongruence* (arXiv:2609.36109v1, first public September 28, 2026), Corollary 2.6, proves divisibility by \(p^n\) for a digit-restricted alternating sum. Setting the number of digit positions to two, taking digit choices \(0,p-1\), coefficient index \(i=0\), and truncation length \(t\ge3\) produces exactly \(S_p(t)\) and proves \(p^2\mid S_p(t)\), but does not determine the precise valuations or the exceptional prime set. Ichino and Prasanna, *Representations of \(\mathrm{GL}_2\) over \(\mathbb{Z}/p^n\mathbb{Z}\) and congruences for binomial coefficients* (arXiv:2503.20727v1, first public March 26, 2025), establish broader divisibility congruences, including this specialization, but do not report the present sharpness classification. The new result is about exact valuations and the first two exceptional primes, not a claim of first discovery of the original congruence.

## Limitations
The finding is a genuine finite-prime classification coupled to an infinite truncation parameter; it is not a classification of exceptional primes globally. The threshold \(71\) is mathematically selected as the location of the second exceptional prime, not presented as a universal natural limit. The exact exceptional-prime pattern beyond this second example is unknown here. The proof does not supply a representation-theoretic interpretation of the exceptional behavior or derive higher digit-depth sharpness. An unindexed equivalent classification could exist despite the literature comparisons; no independent audit has been performed.

## References
1. O. Gonzalez, *A q-analogue of a binomial supercongruence*, arXiv:2609.36109v1 (2026-09-28), https://arxiv.org/html/2609.36109v1.
2. A. Ichino and K. Prasanna, *Representations of \(\mathrm{GL}_2\) over \(\mathbb{Z}/p^n\mathbb{Z}\) and congruences for binomial coefficients*, arXiv:2503.20727v1 (2025-03-26), https://arxiv.org/html/2503.20727v1.
