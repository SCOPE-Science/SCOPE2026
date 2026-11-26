# Independent mathematical audit

## correctness

PASS

The scalar period equals the return period of the triple state. M^13=I+3B, the two seed states are nonfixed modulo 3, and B is nonzero on both seeds modulo 3. Cubing lifts the operator, with (U^{3^m}−I)/3^{m+1}≡B mod 3; a unit multiplier therefore gives state displacement of exact 3-adic valuation m+1. This proves the least period for all k, not just the return by the proposed period. In each regular residue branch F(t)/3 has one root modulo 3 and unit increments at every higher digit, so one lift at each step. Perrin r=0 gives F(t)/3≡1 mod 3. Padovan r=9 vanishes identically modulo 9. For f=F/9 its reduction is 1+2t+binom(t,2) with roots 1,2 mod 3. For m≥1 the cubing quotient is B+3B²+3B³ mod 9, unchanged under further cubing since the further error terms are multiples of 9. Multiplication by U^t≡I+3tB mod 9 yields f(t+3^m)−f(t)≡3^m t mod 3^{m+1}. The two root classes have unit slope and lift uniquely; there are three representatives of each normalized root in the full t-window, giving six exceptional zero indices plus three regular ones for k≥3. The base moduli and claimed densities follow. Independent replay python3 -B /workspace/branches/independent_padovan_perrin.py obtained all eight coefficient rows by scalar finite differences and checked both first returns and full mod-13 counts through k=11 (767,637 positions per sequence at k=11). The all-k result uses the lifting proof, not the finite replay.

## originality

PASS

Credit the unshifted Padovan zero-count law and exceptional six-index branch, and thus the exact contrast with Perrin. Do not credit the Perrin side or the period data as distinct contributions: available catalogue records cover the Perrin law, and period values are tabulated. The decisive Padovan side is not shown covered by the inspected adjusted-value, integer-multiplicity, or period sources. This is a bounded assessment without a priority judgment.

## value

PASS

Prime three is the natural setting for a common short residue period and competing singular branches of two standard seeds. The exact Padovan branch splits into two normalized simple roots while the exceptional Perrin branch dies. This explains a persistent factor-three difference in rare-zero densities between two sequences sharing the same recurrence and exact period, an all-exponent invariant useful for recurrence valuation and distribution questions rather than another finite period table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
