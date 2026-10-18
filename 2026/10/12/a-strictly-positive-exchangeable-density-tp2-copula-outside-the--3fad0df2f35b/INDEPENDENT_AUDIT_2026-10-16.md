# Independent mathematical audit

## correctness

PASS

The reviewed checkerboard matrix P=(1/64) times rows (32,12,12,8,0,0),(12,17,17,18,0,0),(12,17,17,18,0,0),(8,18,18,20,0,0),(0,0,0,0,32,32),(0,0,0,0,32,32), equals blockdiag(A^T A,J2/2) for a product of adjacent-coordinate averaging matrices A. These and the ordered block concatenation are TP2; Cauchy–Binet maintains TP2. All row/column sums 1 and symmetry hold. Reflected contrast P23−P53−P24+P54=−1/64 gives density contrast −3/32 on I2×I3, so P fails PMI. For ε=1/100000, S=(R1…R5)^5 with R_i=I−(ε/2)(e_i−e_{i+1})(e_i−e_{i+1})^T is strictly positive, doubly stochastic and TP2, and Q=S^T P S remains so. Telescoping gives |Q_ij−P_ij|<=50ε, hence reflected contrast ≤−1/64+200ε<0. Independent SymPy exact rational computation verified every ordered TP2 minor of P and Q, positive entries, stochasticity, and Q contrast ≈−0.015601954808512043. The proof and finite 6×6 certificate establish the statement completely; no smoothness is claimed.

## originality

PASS

The foundational Fuchs–Tschimpke paper establishes a PMI density contrast and MK-TP2 counterexamples with singular components, but no absolutely continuous strictly positive exchangeable d-TP2 negative-PMI witness inspected. Since d-TP2 is strictly stronger than MK-TP2, the published singular weaker witness cannot by implication refute d-TP2⇒PMI; the new explicit positive TP2 matrix construction resolves a distinct implication. Resultary search near checkerboard dependence indices found no same nonimplication. Best-of-knowledge priority caveat remains.

## value

PASS

The d-TP2 versus PMI implication is a natural unresolved boundary in positive dependence, and the strictly positive exchangeable 6×6 exact certificate separates two properties that agreed for several standard smooth parametric families. This is a motivated structural counterexample, not merely a numerical perturbation or rephrasing of the weaker singular MK-TP2 example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
