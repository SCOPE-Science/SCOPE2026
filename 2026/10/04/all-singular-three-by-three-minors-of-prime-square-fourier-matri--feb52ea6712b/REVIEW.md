# Review

## Correctness
PASS. The proof reduces the problem to the three residue-occupancy types modulo \(p\). Type A is covered by the prime-power full-spark theorem. For type B columns, a direct row subtraction gives a nonzero product in the type-B row case and an exact rank-two collapse in the type-C row case. Type \((C,C)\) factors as an outer product and has rank one. These cases exhaust all possibilities. The counting formulas follow from disjoint residue choices and lift choices. Exact cyclotomic replay for \(p=3\) and \(p=5\) agrees with every predicted rank.

## Originality
PASS. The closest inspected primary source, Alexeev--Cahill--Mixon, characterizes when an entire selected-row harmonic frame is full spark for prime-power order. It does not state which individual three-by-three minors vanish for the non-full-spark row types, nor their ranks or total counts. Searches for singular three-by-three Fourier minors, prime-square DFT minors, and residue-class classifications did not locate an implication-equivalent statement. A prior principal-minor classification is only the diagonal slice \(R=C\) and does not imply the off-diagonal type-pair census.

## Value
PASS. The theorem converts the first non-prime prime-power obstruction to Fourier full spark into a complete local incidence law: singularity, rank, and multiplicity are all explicit. This is useful for exact sparse-recovery and uncertainty-diagram calculations because it distinguishes a non-full-spark row set from the much smaller family of column triples that actually make it singular.

The main residual risk is terminological: an equivalent count could be hidden in older generalized-Vandermonde or harmonic-frame literature under a different formulation. The inspected prime-power full-spark theorem is broader in one direction but does not subsume this local classification.

Same-model review: passed. Independent audit: not yet performed.
