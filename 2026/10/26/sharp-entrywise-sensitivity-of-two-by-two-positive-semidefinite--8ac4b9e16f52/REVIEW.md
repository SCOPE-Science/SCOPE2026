# Review of the sharp entrywise PSD-repair sensitivity theorem

## Correctness — PASS
The proof fixes the Frobenius projection and independent entrywise measurement norm. A mixed-sign \(2\times2\) derivative is the convex combination of \(RHR\) and \(H-QHQ\). The first endpoint has induced entrywise norm at most \((3+2\sqrt2)/4\), strictly below \(3/2\); the second has norm \(3/2\), with exact polynomial-factor proof. Integration along matrix line segments proves the global strict inequality, and the determinant-identically-zero rank-one line case is handled explicitly. A positive/negative-eigenvalue family approaches the sharp value. Replayed exact arithmetic and sample numerical checks passed 2,711 assertions; universal quantifiers are certified by the written analytic argument, not by the sample enumeration.

## Originality — PASS within examined evidence
Higham (1988) supplies the spectral positive-part operation; Malick and Sendov (2006), and Šilhavý (2015), supply broader derivative formulas. None of the inspected theorem material asserts the optimized \(3/2\) entrywise global Lipschitz constant together with nonattainment. Semantic database searches for covariance/PSD clipping, anisotropic metrics, Lorentz-cone representations, exact Jacobian row sums and the purported constant produced only adjacent, mathematically different projection claims. The general derivative formula is carefully distinguished from the present optimized global statement. Historical uniqueness is **not** proved.

## Value — PASS
Unweighted componentwise perturbations are natural for individual covariance entries, and Frobenius spectral clipping is their canonical PSD repair. The exact amplification factor and the fact that it is not attained by any fixed finite pair give a structural robustness benchmark for the smallest nonpolyhedral PSD cone. This is more than a routine positive-part identity: the proof depends on a sharp rotation-sensitive optimization and a global strictness argument.

## Closest prior work and risks
Higham's original paper was accessible through its abstract and an author-written explanation, not its full text. Malick–Sendov and Šilhavý were inspected in their relevant primary full-text theorem sections. An equivalent older Lorentz-cone norm calculation or semidefinite perturbation estimate could exist; bibliographic priority requires further independent checking. The statement is restricted to real symmetric order-two matrices and unweighted maximum-entry measurement.

Self-review: passed. Independent audit: not yet performed.
