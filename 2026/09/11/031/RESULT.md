# Complete multiplier-class transversal spectrum over DCLS(11)

## Context

Diagonally cyclic Latin squares of prime order can be parameterized by normalized orthomorphisms. For order 11 the classical scalar counts are already known: there are 3441 normalized complete mappings/orthomorphisms, and the cyclic group square has 37851 transversals. Those values are used here only as checks. The result below is the finer class-by-class transversal spectrum after quotienting by the natural multiplier action.

## Definitions

Work in Z_11. A normalized orthomorphism is a map theta with theta(0)=0 such that theta and d -> theta(d)-d are permutations. It defines the diagonally cyclic Latin square

  L_theta(i,j) = theta(j-i)+i (mod 11).

Two seeds are multiplier-isomorphic when theta^a(d)=a theta(a^{-1}d) for a in F_11^*. A transversal is a set of 11 cells meeting every row, column and symbol exactly once.

## Result

The 3441 normalized orthomorphisms form exactly 363 multiplier classes, with orbit-size distribution

  10^336, 5^12, 2^6, 1^9.

Across the 363 canonical multiplier representatives, the exact numbers of transversals have spectrum

  {3333: 33, 3443: 33, 3476: 66, 3553: 66, 3597: 9,
   3795: 36, 3949: 66, 4389: 36, 4411: 9, 37851: 9}.

Thus the order-11 multiplier quotient has ten transversal-count strata. The maximum 37851 occurs in nine classes represented by the nontrivial linear maps theta(d)=c d. The values 3441 and 37851 themselves are classical and are not claimed as new; the contribution is the complete 363-class quotient and its exact transversal spectrum.

## Proof and reproducibility

A normalized-orthomorphism backtrack enumerates all 3441 seeds using simultaneous injectivity of theta and theta-id. Taking the lexicographic minimum under the ten multipliers gives 363 classes and the stated orbit sizes.

For each canonical representative, two distinct exact transversal counters were archived: a row-ordered column/symbol bitmask search and a generic 33-column exact-cover search. Their counts agree on all 363 representatives. A replay independently re-enumerates the normalized orthomorphisms in reverse value order, verifies the multiplier quotient, checks Latinness, checks the stored count logs, and spot-recounts representatives with a third traversal.

A fresh independent exhaustive counter, separate from the archived implementations, re-enumerated all 3441 normalized orthomorphisms, recovered the 363 canonical representatives and counted transversals of every representative; it reproduced the spectrum above exactly.

The archived universal mate M(i,j)=j-i and its transversal decomposition are correct elementary consequences of the orthomorphism model, but they are background consistency checks rather than part of the originality claim.

## Limitations

The equivalence relation is multiplier isomorphism exactly as defined above. Broader isotopy or paratopy can identify additional representatives and is outside the claim. The result is a finite exhaustive classification, not a statement about all order-11 Latin squares.

## References

- Ian Wanless, Diagonally cyclic latin squares, European Journal of Combinatorics (2004), doi:10.1016/j.ejc.2003.09.014.
- Ian Wanless, Transversals in Latin Squares (survey); classical order-11 values 3441 and 37851.
- Ian Wanless, Data on transversals in Latin squares.
- OEIS A003111 and A006717 for the classical complete-mapping/transversal totals.
