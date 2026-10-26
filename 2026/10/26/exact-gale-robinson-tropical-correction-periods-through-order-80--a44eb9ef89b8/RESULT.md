# Exact Gale–Robinson tropical correction periods through order 80

## Finding

For every ordered triple of positive integers \(1\le p<q<r\) with \(\gcd(p,q,r)=1\) and \(m=p+q+r\le80\), define
\[
N=\gcd(p,q)r^2+\gcd(p,r)q^2+\gcd(q,r)p^2+pqr.
\]
Let \((k_n)_{n\ge1}\) be the integer sequence with \(k_1=\cdots=k_{m-1}=0\), \(k_m=1\), and
\[
k_{n+m}+k_n=\max\{k_{n+p}+k_{n+m-p},\ k_{n+q}+k_{n+m-q},\ k_{n+r}+k_{n+m-r}\},\quad n\ge1.
\]
Then **for every integer \(n\ge1\)**,
\[
k_n=\frac{n^2+c_n}{2N},\qquad c_{n+N}=c_n.
\]
Here \(c_n=2Nk_n-n^2\) is an integer sequence and **\(N\) is its least positive period**. There are exactly **11,052** eligible triples, including **10,977** outside the previously proved \((p,q)=(1,2)\) subfamily. This is a finite-parameter, infinite-time theorem; it does not prove the same formula for all triples without the order restriction.

## Assumptions and scope

All quantities are integers. Indices start at \(1\). The symbol \(\gcd(p,q,r)\) denotes the greatest common divisor of the three parameters; \(m\) denotes the order of the tropical recurrence, not an iteration bound. The primitive condition and strict ordering select each parameter triple exactly once. The recurrence has one uniquely determined forward solution because the right-hand side uses only indices strictly smaller than \(n+m\). The positive integer \(N\) is even: if all three parameters are odd, the four terms defining \(N\) are odd, and if one or two are odd, its terms group into an even sum modulo \(2\); all-even triples are excluded.

## Proof

**Finite affine-shift lemma.** Fix any admissible parameter triple and an even proposed value \(N\). Suppose the recurrence values computed through index \(N+m\) satisfy the following \(m\) finite equalities:
\[
k_{N+i}=k_i+i+\frac N2,\qquad 1\le i\le m.\tag{1}
\]
Define \(\ell_n=k_{n+N}-n-N/2\) for \(n\ge1\). If \(k\) satisfies the recurrence, so does \(\ell\): in each term on the right-hand side the sum of the two indices is \(2n+m\), which is also the sum of the two indices on the left. Subtracting the same affine function at every index therefore subtracts the common amount \(2n+m+N\) from every two-term expression. By (1), \(\ell_i=k_i\) for \(1\le i\le m\). The deterministic forward recurrence now gives \(\ell_n=k_n\) for every \(n\ge1\), proving
\[
k_{n+N}-k_n=n+\frac N2,\qquad n\ge1.\tag{2}
\]
Consequently
\[
2Nk_{n+N}-(n+N)^2=2Nk_n-n^2,
\]
so the correction \(c_n\) has period \(N\), proving the claimed quadratic expression at every index.

**Optimal period.** If the integer-valued correction has a positive period \(d\), then
\[
k_{n+d}-k_n=\frac{dn}{N}+\frac{d^2}{2N}\in\mathbb Z
\]
for all \(n\ge1\). Subtracting this expression at successive values of \(n\) shows \(d/N\in\mathbb Z\). Thus \(N\mid d\). Since (2) gives period \(N\), this is its least positive period.

**Exhaustive finite-parameter certificate.** The accompanying standalone `verify.py` enumerates every eligible triple twice by different loop organizations and asserts agreement. For each such triple, it computes \(N\), checks its parity, sets \(k_1,\ldots,k_m\), evaluates the recurrence exactly for \(n=1,\ldots,N\), and checks each equality in (1). Since exactly those finitely many assertions were checked for every eligible triple, the affine-shift lemma proves the desired infinite-time assertion simultaneously for all of them. The certificate uses exact integer arithmetic only, and no floating-point approximation, unexamined tail, or random sampling.

The enumeration has 11,052 triples. Of these, 75 satisfy \((p,q)=(1,2)\) and \(3\le r\le77\); hence 10,977 lie outside that infinite family. Independent enumeration orders agree on the entire set of triples. The sum of all proposed periods is 84,412,414. The largest period is 36,556 at \((p,q,r)=(13,26,41)\), of order 80.

## Verification

Run `python3 verify.py` with an ordinary Python 3 installation. Expected first output line: `VERIFY_OK`. The remaining lines report the 11,052 triple count, 10,977 outside-family count, total proposed periods, maximal-period tuple, and a reproducible SHA-256 digest of parameter and checkpoint records:

`d95345c93044969f924f10fe37245a3424b72994f639951da7ff37365777058c`

The exact algorithm is fully specified and executable in the accompanying source, and checks only a finite number of integer operations for each of finitely many triples. The shift lemma, not extrapolation from large indices, establishes the infinite-time statements. A failure or incomplete execution cannot be interpreted as establishing the theorem.

## Relationship to prior work

Can's *Degree Growth of Rational Maps with Laurent Property*, Conjecture 1, proposes the above quadratic-plus-periodic formula for all primitive three-term Gale–Robinson parameters; Theorem 3 proves it for \((p,q)=(1,2)\) and all \(r\ge3\). His proof also employs affine-shift invariance, which is used and credited here, but does not state this comprehensive bounded-order certificate or the least-period deduction. Galashin and Pylyavskyy's *R-systems*, Proposition 11.4, gives general quadratic degree-growth estimates through combinatorial methods rather than the same exact all-index periodic correction for this finite parameter domain. Earlier Somos and Gale–Robinson studies treat individual instances or related enumerative formulations; these are not claimed here as new. The added fact is a rigorously reproducible, fully parameter-exhaustive bound for \(m\le80\), and the forced minimality of the conjectured correction period whenever the formula holds.

## Limitations

The theorem covers only the specific tropical recurrence, fixed initial values, strictly ordered primitive triples, and \(m\le80\). It does not prove Can's conjecture for \(m>80\), nor assert independent verification of a general Laurent-map degree formula beyond the tropical recurrence. The exhaustive claim requires executing the supplied finite integer-arithmetic certificate; this report does not present handwritten tables for all parameter instances. Possible equivalent older results under ultradiscrete or tropical Somos nomenclature, especially an older relevant source whose full text was not accessible, remain a historical-priority risk. No independent audit has been performed.

## References

1. M. E. Can, *Degree Growth of Rational Maps with Laurent Property*, arXiv:2610.21627v1, first publicly posted 15 October 2026, especially Conjecture 1, Theorem 3, and §4.2. https://arxiv.org/html/2610.21627v1
2. P. Galashin and P. Pylyavskyy, *R-systems*, arXiv:1709.00578, 2017, especially Proposition 11.4. https://arxiv.org/abs/1709.00578
3. M. A. Romanov, *Tropical sequences associated with the Gale–Robinson sequences*, 2021, DOI:10.47910/FEMJ202121. Full text was not accessible for comparison.
4. M. Bousquet-Mélou, J. Propp and J. West, *Perfect Matchings for the Three-Term Gale–Robinson Sequences*, Electronic Journal of Combinatorics 16 (2009), R125, DOI:10.37236/214.
