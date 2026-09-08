# An odd Martin-type largest-denominator theorem for expansions of 1

## Context

For general Egyptian fractions (distinct unit fractions, no parity restriction),
Erdos-Graham asked which integers can occur as the largest denominator of an
expansion of 1; Martin settled the program (density-zero exceptional set, order
of growth; finitely many second-largest exceptions). For odd-distinct expansions
the counting program (Elsholtz; Chen-Elsholtz-Jiang), the odd-greedy fixed-length
taxonomy (Louwsma-Martino, finiteness open), and a general restricted-denominator
algorithm (Martin-Shi) record no theorem on which odd integers do or cannot occur
as largest denominators. This record closes that gap two-sidedly.

## Definitions

An **odd-distinct expansion of 1** is a finite set S of distinct odd integers
> 1 with sum_{d in S} 1/d = 1. Its **largest denominator** is max(S).

## Result

(a) **Realizability (infinitude).** Infinitely many odd integers occur as the
largest denominator of some odd-distinct expansion of 1. From the base

  E_0 = {3,5,7,9,15,21,27,35,63,105,135}, sum 1/d = 1,

iterating the Lemma below at the current maximum gives valid expansions E_n
with strictly increasing odd maxima

  135, 82215, 30417001335, 4163372866005888522015,
  78001531296273387817009252900320853961254035, ...

(b) **Obstruction (infinitude).** No prime power — in particular no odd prime —
occurs as the largest denominator of any (not necessarily odd) distinct
expansion of 1 with strict maximum. Hence infinitely many odd integers are
obstructed, including the infinite 3-mod-4 subfamily {3^{2j+1} : j >= 0}
= {3, 27, 243, ...}.

**Lemma (odd splitting identities).** For every odd k >= 3:

- if k = 3 mod 4 with m = (3k+1)/2: 1/k = 1/(3k) + 1/m + 1/(3km);
- if k = 1 mod 4 with m = 3(k+1)/2, c = 3k(k+1)/2: 1/k = 1/(3k) + 1/m + 1/c.

In both cases the three denominators are odd, pairwise distinct, and strictly
greater than k.

## Proof / evidence

Lemma: for k = 3 mod 4, (m+3k+1)/(3km) = 1/k iff m+3k+1 = 3m iff 3k+1 = 2m,
true by definition of m. For k = 1 mod 4, 1/(3k)+1/m+1/c = 1/k follows from
m = 3(k+1)/2, c = k*m since 1/m + 1/c = (k+1)/c = 2/(3k), and
1/(3k)+2/(3k) = 1/k. Integrality: (3k+1)/2 is integral for odd k.
Oddness: k = 4t+3 gives m = 6t+5 odd; k = 4t+1 gives (k+1)/2 = 2t+1 and
m = 3(2t+1) odd; products of odds are odd. Since k >= 3, k < m < 3k and
c = k*m > m, so children are distinct and exceed k.

(a): base sum is exact: each d divides 945 and sum 945/d =
315+189+135+105+63+45+35+27+15+9+7 = 945. Given E_n with odd max M_n,
replace 1/M_n by its three strictly larger odd children per the Lemma.
Children exceed every element of E_n, so oddness, distinctness, and sum 1
are preserved and the new max strictly exceeds M_n. Induction yields
infinitely many distinct odd realizable maxima.

(b): let S have strict max M, L = lcm(S), v = v_p(M) for prime p. If no other
d in S has v_p(d) >= v then v_p(L) = v, v_p(L/M) = 0, while v_p(L/d) >= 1
for d != M. Clearing denominators L = sum L/d gives (unit mod p) = 0 mod p,
contradiction since v >= 1 implies p | L. If M = p^k, every d < M has
v_p(d) < k, so no such S exists — with no parity assumption.

Machine evidence: `artifacts/verify_family.py` (stdlib Fraction only) replays
base sum, the identity for every odd k in [3,3999], four iterated expansions
with exact sums and strictly increasing maxima, and subset-exhaustion that no
expansion has max 3, 5, 7, or 11. Result: ALL CHECKS PASSED.

## Limitations

The obstruction is proved for the infinite set of prime powers (with the
infinite 3-mod-4 subfamily 3^{2j+1} exhibited), not for every element of a
full residue class. The identity sweep is finite ([3,3999]) supporting a
symbolically proved identity; infinitude of (a) rests on the induction proof
plus exact iteration instances. The base E_0 was found by divisor-subset
search (discovery only); the theorem does not depend on any search cap.

## Reproducibility

Run `python3 artifacts/verify_family.py` (Python 3, stdlib only). It prints
E0/max, identity-sweep confirmation, E1..E4 splits with new maxima and term
counts, subset checks for prime maxima 3,5,7,11, and ALL CHECKS PASSED.

## References

- G. Martin, Denser Egyptian Fractions, math/9811112 (Acta Arith. 95, 2000).
- C. Elsholtz, Egyptian Fractions with odd denominators, 1606.02117.
- Y.-G. Chen, C. Elsholtz, L.-L. Jiang, Egyptian Fractions with Restrictions, 1108.6118.
- J. Louwsma, J. Martino, Rational numbers with odd greedy expansion of fixed length, 2309.07280.
- G. Martin, Y. Shi, An algorithm for Egyptian fraction representations with restricted denominators, 2107.05076.
