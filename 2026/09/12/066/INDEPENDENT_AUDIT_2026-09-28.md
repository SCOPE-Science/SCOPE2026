# Independent Audit — 2026/09/12/066

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `11d6a794629caba209ac8235407d4d4abb241397`  
**Disposition:** **PASSED**

## Correctness
I independently enumerated all 9-subsets of S16 and S20. S16 has zero 9-term zero-sums; all 65 one-point extensions acquire one. S20 has exactly 1832 9-term zero-sums; their bitmasks are pairwise intersecting, so no disjoint pair exists; and for every one of the 61 outside points, exhaustive enumeration of 8-subsets summing to the negative new point finds a new 9-sum disjoint from an old one. Thus g(C9^2)>=17 and the record’s two-disjoint exact-exponent predicate satisfies g2(C9^2)>=21, with both displayed witnesses extension-maximal. The lemma g2(H)<=g(H)+exp(H) follows immediately by extracting one exp(H)-sum and applying g(H) to the remainder.

## Originality
The one-fold numerical lower bound 17 is classical in scale and is not treated as the novelty. The nearby 2022 “k-Harborth constant” literature uses k to denote the required subset size, not the number of disjoint exponent-length zero-sums, while multi-wise Davenport constants concern sequences and unrestricted zero-sum lengths. The submitted contribution is the explicit squarefree exact-9 two-fold witness S20, its complete 1832-sum intersecting census, and extension-maximality; these are not consequences of the cited neighboring definitions.

## Scientific value
An explicit 20-point obstruction to two disjoint exponent-length zero-sums, together with a complete intersecting-family census and maximality certificate, gives a concrete lower bound and reusable extremal object for a natural multi-zero-sum variant. The result is narrow but the certificate is exact and nontrivial.

## Literature
- https://arxiv.org/abs/2209.14784 — its `g^k(G)` fixes the zero-sum subset cardinality `k`; it is not the submitted two-disjoint-sum predicate.
- https://arxiv.org/abs/1407.1966 — multi-wise Davenport constants require disjoint zero-subsums in sequences, without the squarefree exact-exponent constraint used here.

## Independent checks
A fresh exhaustive implementation reproduced `#9-sums(S16)=0`, `#9-sums(S20)=1832`, pairwise intersection of all S20 zero-sums, zero bad extensions of S16, and zero bad extensions of S20. Current main blobs match the assignment snapshot and repository comparison shows no changes under this path. No GitHub writes were made.
