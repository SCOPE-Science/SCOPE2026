# Independent mathematical audit

## correctness

PASS

Exact line search makes rᵏ orthogonal to pᵏ⁻¹. If u is the projection of the fresh Gaussian sketch onto (pᵏ⁻¹)⊥, then the corrected direction is (u·rᵏ)u, and the residual update is the orthogonal removal of the u component. At step zero use the unprojected Gaussian. Conditional on all previous sketches, in an orthonormal basis with first vector rᵏ/‖rᵏ‖, the projected sketch has h independent standard normal coordinates, h=d first and h=d−1 thereafter. The ratio is Y/(X+Y), with independent X∼χ²₁ and Y∼χ²ₕ₋₁. For d≥3 this lies a.s. in (0,1), proving by induction that denominators remain nonzero and residuals positive at every finite step. The conditional law is deterministic, so iterated conditioning gives independence including the first factor, not merely equal marginal laws. Means follow by multiplication, and the strong law applies to the subsequent logarithms since the beta density is integrable against |log x|. The one-dimensional complement in d=2 removes the whole residual on the second step, and the first nonparallel sketch leaves a nonzero residual a.s.; d=1 takes one step. Without the correction h=d at every step. Inspected rational checks and Gaussian simulation provide supplementary evidence only; the probability proof does not use a finite simulation.

## originality

PASS

The direction recurrence, spherical projection law, and the finite-termination boundary are not new individually. The supported distinct claim relative to the inspected earlier primary texts is the independent first/later beta-factor process for rank-one Gaussian predecessor-corrected exact line search, including the exact later contraction and logarithmic rate. Two demonstrably equivalent or stronger indexed results postdate the assigned October record; those are material coverage, not evidence of earlier priority.

## value

PASS

The independent product law supplies sharp iteration-by-iteration and almost-sure rates, and distinguishes the correction's effect on the whole error process from the uncorrected method rather than merely repeating a convergence guarantee. The comparison is in exact arithmetic and counts iterations, not practical runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
