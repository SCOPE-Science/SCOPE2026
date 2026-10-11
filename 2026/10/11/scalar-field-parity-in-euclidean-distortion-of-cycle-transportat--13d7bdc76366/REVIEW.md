# Scientific review: Euclidean distortion of cycle transportation spaces

## Correctness — PASS
Finite-cycle edge increments identify the dual with a zero-sum \(\ell_\infty\) section. Averaging an arbitrary positive quadratic (or Hermitian) form over all permutations preserves both norm-comparison inequalities and makes its restriction a scalar multiple of coordinate \(\ell_2\). The minimum squared coordinate norm on the unit sup-sphere is exactly \(n/(n-1)\). The real maximum follows from a full vertex classification and is \(n\) for even \(n\), \(n-1\) for odd \(n\); the complex maximum is \(n\) by roots of unity. These steps prove the formulas at every integer \(n\ge3\). The executable checks cover only a finite range and do not supply the general proof.

## Originality — PASS, with residual risk
The arXiv papers by Godard (0904.3178), Alexander et al. (1911.10642), and Ostrovska–Ostrovskii (2112.02689) cover the underlying graph-free-space models, tree classification, and cycle-space quotient, rather than the field-sensitive all-dimensional Hilbert-distance constants. The most relevant published finite-cycle computation, “Numerical-index parity law for Lipschitz-free spaces over cycles,” contains the real cube-section vertex patterns used here, but its theorem computes numerical index, not Euclidean distortion or complex scalar behavior. The real four-cycle distance is a known special case and is excluded from individual novelty claims. An unindexed classical hyperplane-section formula remains a bibliographic risk, and an independent literature audit remains outstanding.

## Value — PASS
This computes a canonical geometric invariant for **every cycle size**, not one tuned finite-dimensional example. It detects a scalar-field anomaly precisely at odd cycle lengths: real odd cycles fall strictly below the dimension-based Hilbert-distance extremum, whereas even real and all complex cycles attain it. The result gives a complete natural family classification, useful as a benchmark for Banach–Mazur geometry of graph transportation spaces. It does not rely on experiments to establish the infinite family.

Same-model review: passed. Independent audit: not yet performed.
