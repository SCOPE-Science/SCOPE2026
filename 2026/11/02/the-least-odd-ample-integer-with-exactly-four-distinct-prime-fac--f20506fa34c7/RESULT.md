# The least odd ample integer with exactly four distinct prime factors

## Finding
Define the recursive-divisor function by \(a(1)=1\) and
\[
a(n)=1+\sum_{\substack{d\mid n\\d<n}}a(d)\quad(n>1).
\]
An integer \(n\) is **ample** when \(a(n)>n\). Among all positive odd ample integers with **exactly four distinct prime factors**, the unique least integer is
\[
N=3^{11}5^5 7^3 11^2=22975412315625,
\qquad a(N)=24786437787648>N.
\]
No smaller odd integer with exactly four distinct prime factors is ample.

## Assumptions and scope
Only positive integers with four *distinct* odd prime divisors, with arbitrary positive exponents, are considered. Repeated primes count once for support cardinality. The finding does not concern the least odd ample integer with unrestricted prime support or with exactly four prime factors counted with multiplicity.

## Proof
**Prime-support reduction.** Writing \(n=\prod_{j=1}^4p_j^{e_j}\), with \(p_1<p_2<p_3<p_4\) odd primes and all \(e_j\ge1\), the defining divisor recursion shows by induction on \(e_1+\cdots+e_4\) that \(a(n)\) depends only on \((e_1,e_2,e_3,e_4)\) and not on which primes occur. Replacing the four ordered primes by \(3,5,7,11\) preserves \(a(n)\) but does not increase \(n\). Therefore any ample integer below \(N\) on four odd prime supports would produce an ample integer of the form \(3^u5^v7^w11^t\le N\) with all four exponents positive.

**Exhaustive finite reduction.** Any such product below or equal to \(N\) has the coordinate bounds
\[
1\le u\le22,\qquad 1\le v\le15,\qquad1\le w\le13,\qquad1\le t\le10.
\]
Indeed, each bound is obtained by fixing the other three prime factors to their minimum exponent one, then taking the largest allowed power under the exact inequality \(3^u5^v7^w11^t\le N\). The algorithm below evaluates every exponent tuple in this rectangular box and tests all candidates satisfying the product bound. Precisely \(2757\) positive-exponent tuples pass the product cutoff.

Let \(A(e)\) be the common value \(a(\prod p_i^{e_i})\) on four ordered prime supports, and put \(S(e)=\sum_{0\le f_i\le e_i}A(f)\). The initial value is \(A(0,0,0,0)=1\). For every exponent vector, define by inclusion-exclusion
\[
T(e)=\sum_{\emptyset\ne J\subseteq\{i:e_i>0\}}(-1)^{|J|+1}S(e-\mathbf1_J).
\]
This equals the sum of \(A(f)\) over every proper sub-vector \(0\le f_i\le e_i\), so the exact recurrence is
\[
A(e)=1+T(e),\qquad S(e)=1+2T(e).
\]
Each sub-vector on the right has at least one coordinate strictly smaller, making evaluation in nested increasing-coordinate order exact. The standalone `verify.py` implements precisely this recurrence with arbitrary-precision integers, enumerates all \(2757\) bounded candidates, and reports exactly one ample candidate, the boundary tuple \((11,5,3,2)\), with \(A(11,5,3,2)=24786437787648\). It separately reconstructs every proper-divisor recurrence on all \(864\) sub-vectors of the boundary tuple, without relying on the prefix-sum formula. This is a finite exhaustive proof after the unlimited support and exponent cases have been eliminated by the preceding reductions.

## Verification
Run `python3 verify.py` using standard Python 3. The program asserts the exact minimum and coefficient value, the completeness of the bounded exponent search, and all \(864\) direct proper-divisor-recurrence cross-checks. It prints `VERIFY_OK candidate_tuples=2757 direct_subvectors=864` upon success. All arithmetic is integer-exact. Its assertions are only an exhaustive finite certificate of the mathematically bounded domain; no finite sampling is used to infer an unbounded assertion.

## Relationship to prior work
Fink introduced ample integers in arXiv:2008.10398v1 (24 August 2020), Section 3.3, and determined the smallest unrestricted odd ample integer, which has five distinct odd prime factors. The present theorem determines the different extremal invariant for **exactly four** distinct odd prime factors, between the already-studied unrestricted five-support and previously determined three-support cases. The exact four-support minimum does not follow from the unrestricted minimum or the three-support minimum. Literature and mathematical-record searches found no equivalent four-support extremum in the inspected sources. No claim of absolute priority or independent verification is made.

## Limitations
The theorem does not classify all four-support ample integers, supply a density, or concern other functions of the divisors. It relies on a finite exhaustive integer certificate for the bounded exponent search. An unindexed table or an inaccessible earlier computation may already contain the exact minimum; this residual originality risk is explicitly retained.

## References
1. T. Fink, *Recursively abundant and recursively perfect numbers*, arXiv:2008.10398v1 (first posted 24 August 2020), especially Section 3.3 and the recursive-divisor definition.
2. arXiv:2307.09140v1 (related ordered-factorization context; its title is not used as evidence for this theorem).
3. OEIS A067824, recursive divisor count (definition/database context; a database entry is not treated as proof of the minimizer).
