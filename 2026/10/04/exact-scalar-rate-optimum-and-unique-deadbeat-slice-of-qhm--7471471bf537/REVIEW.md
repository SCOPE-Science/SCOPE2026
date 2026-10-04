# Review

## Correctness

PASS. The scalar QHM state matrix has trace \(1+\beta-s(1-\nu\beta)\) and determinant \(\beta[1-s(1-\nu)]\). The complete quadratic Jury conditions give the exact stable interval. For \(0<\nu<1\), the discriminant has two explicit roots; the right repeated-root point gives the candidate optimum. A determinant lower bound excludes every smaller step, while a radius-scaled Jury inequality excludes every larger step. The endpoint cases \(\nu=0\) and \(\nu=1\) reduce to explicit plateaus. The unique zero of the interior rate formula is \(\nu=\beta\), and at the corresponding step both trace and determinant vanish, so Cayley-Hamilton gives exact two-step nilpotence.

Risk: the result is scalar and spectral; it is not a uniform multimode or transient-norm theorem.

## Originality

PASS. The defining QHM paper gives the update, its two-state operator representation, and the identity \(\nu=\beta\) with Nesterov momentum, but does not state the exact scalar learning-rate optimum or deadbeat uniqueness. A 2024 two-step momentum paper is algebraically equivalent at the level of the scalar characteristic polynomial after an explicit parameter change and therefore already covers the stability inequality; that part is treated as prior coverage rather than novelty. Its inspected analysis does not state the fixed-\((\beta,\nu)\) closed-form scalar rate floor or identify the QHM Nesterov slice as the unique nilpotent interpolation.

Focused searches over QHM, scalar quadratics, spectral radius, repeated roots, critical damping, and finite-time annihilation found no source implying the complete rate-optimal statement.

## Value

PASS. QHM was introduced to decouple historical averaging from immediate-gradient weighting. The exact scalar formula shows that the same immediate-discount parameter also controls deterministic critical damping in a sharply quantifiable way. The unique zero at \(\nu=\beta\) gives a structural explanation for the Nesterov slice inside QHM: on a perfectly known scalar curvature it is the only nondegenerate interpolation capable of deadbeat two-step state annihilation. This is a motivated characterization of QHM's extra degree of freedom, not a routine restatement of its stability range.

Same-model review: passed. Independent audit: not yet performed.
