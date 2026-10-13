# Prime powers are the exact pointwise-injectivity locus for the additive transform
## Finding
Let the additive transform \(\Phi_f\) of an arithmetic function \(f\) be defined by
\[
\Phi_f(p^a)=f(p^a)
\]
for every prime power \(p^a\), together with
\[
\Phi_f(mn)=m\Phi_f(n)+n\Phi_f(m)
\]
whenever \(\gcd(m,n)=1\). Fix \(n\ge2\). Then
\[
f(n)=g(n)\iff\Phi_f(n)=\Phi_g(n)
\]
holds for every pair of multiplicative arithmetic functions \(f,g\) if and only if \(n\) is a prime power. If \(n\) has at least two distinct prime divisors, both directions fail separately even for positive real-valued completely multiplicative functions.

## Assumptions and scope
Arithmetic functions take values in \(\mathbb C\). The claim is pointwise at one fixed integer \(n\); it does not concern injectivity of the full operator on all function values.

## Proof
If \(n=p^a\) is a prime power, the defining condition gives \(\Phi_f(n)=f(n)\) and \(\Phi_g(n)=g(n)\), so the equivalence holds for arbitrary arithmetic functions.

Suppose instead that \(n\) has at least two distinct prime divisors. Write its prime-power blocks as \(P_i=p_i^{a_i}\). Theorem 2.1 of the source gives
\[
\frac{\Phi_f(n)}{n}=\sum_i\frac{f(P_i)}{P_i}.
\]
Choose distinct blocks \(P=p^a\) and \(Q=q^b\). Let \(g(r)=1\) for every prime \(r\), extended completely multiplicatively.

First define a positive completely multiplicative \(f\) by
\[
f(p)=2^{1/a},\qquad f(q)=2^{-1/b},\qquad f(r)=1
\]
for other primes. Then \(f(n)=g(n)=1\), but
\[
\frac{\Phi_f(n)-\Phi_g(n)}{n}=\frac1P-\frac1{2Q}\ne0.
\]
Indeed, \(P=2Q\) is impossible for powers of distinct primes: if \(p\) is odd the parities differ, and if \(p=2\) unique factorization forces \(q=2\).

For the reverse implication choose two blocks with \(P>Q\), and define
\[
f(p)=2^{1/a},\qquad f(q)=\left(1-\frac QP\right)^{1/b},\qquad f(r)=1
\]
for other primes. Then
\[
\frac{\Phi_f(n)-\Phi_g(n)}{n}=\frac1P-\frac1P=0,
\]
while
\[
f(n)=2\left(1-\frac QP\right)\ne1=g(n),
\]
because equality would again force \(P=2Q\). Hence both implications fail at every mixed-support integer, proving the characterization.

For a concrete sanity check at \(n=6\), the first construction may take \(f(2)=2\), \(f(3)=1/2\), giving \(f(6)=g(6)=1\) but \(\Phi_f(6)=7\ne5=\Phi_g(6)\). The reverse construction may take \(f(2)=1/3\), \(f(3)=2\), giving \(\Phi_f(6)=\Phi_g(6)=5\) but \(f(6)=2/3\ne1=g(6)\).

## Verification
`verify.py` checks both algebraic templates with exact rational arithmetic for every \(2\le n\le10000\). The replay output is in `verification_output.txt`. This finite computation is regression evidence only; the proof above is unbounded.

## Relationship to prior work
E. En-naoui, *Additive transform of an arithmetic function: Part I*, arXiv:2312.08929v1, first posted 13 December 2023, introduces the transform. Definition 2.1 gives the defining rules, Theorem 2.1 gives the prime-power-block formula, and Proposition 2.4 states that for multiplicative \(f,g\), \(f(n)=g(n)\iff\Phi_f(n)=\Phi_g(n)\) for every positive integer \(n\). The present result determines the exact maximal validity locus of that pointwise assertion and shows that each direction fails on every excluded integer.

Exact-phrase, correction/erratum, injectivity, prime-power-locus, and semantic searches against the focal preprint, general web indexes, and a public mathematical-results index found no checked correction or equivalent boundary theorem. The closest indexed findings concern unrelated injectivity questions and do not imply this claim.

## Limitations
The result is pointwise and does not analyze analytic properties or full-operator injectivity. An unindexed later comment or independent note could contain the same correction.

## References
1. E. En-naoui, *Additive transform of an arithmetic function: Part I*, arXiv:2312.08929v1, 13 December 2023. MSC 2020: 11A25. See Definition 2.1, Theorem 2.1, and Proposition 2.4.
