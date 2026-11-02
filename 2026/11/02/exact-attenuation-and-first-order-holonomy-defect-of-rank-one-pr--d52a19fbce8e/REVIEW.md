# Scientific review: exact rank-one projected-transport loop

## Correctness

**PASS (self-review).** The tangent normal is a unit rank-one projector, the symmetric and skew tangent factors form an explicit orthonormal frame, and the frame overlaps give a single constant \(2\times2\) transfer matrix. Its negative characteristic discriminant for all integers \(N\ge3\), determinant \(\cos^2(\pi/N)\), and Cayley–Hamilton power formula prove the exact spectral and singular-value statements. Direct differentiation gives the exact continuous holonomy, while Taylor expansions give the sharp operator-norm coefficient. The supplemental standard-library checker compares independently formed moving frames, direct matrix powers, exact rational cases, and large-grid limits. All claims concern the specified smooth curve, exact projectors, and homogeneous equation, with no extrapolation to forced or inexact-state problems.

## Originality

**PASS (self-review; incomplete historical priority).** Section 5.2.1 of Carrel–Vanzan, arXiv:2610.29554v1, explicitly proposes projected-Euler covariant transport and proves a first-order global estimate, but the inspected full section and nearby analysis do not give an exact closed-loop amplification spectrum, finite-grid singular values, or sharp error coefficient. Standard projected vector transports are described in Boumal's 2023 textbook, and exact continuous parallel transport is addressed by Nguyen–Sommer (2024), without this discrete rank-one-loop calculation in the material inspected. Louis and coauthors (2018) give another parallel-transport scheme based on Jacobi fields; the accessible abstract concerns a different method. Public mathematical record searches for rotating tangent projectors, rank-one transport and discrete monodromy returned no covering claim. A broader older theorem on cyclic products of orthogonal projections might imply the special algebra; that unresolved priority risk remains explicit, and a missing exact match is not treated as proof of uniqueness.

## Mathematical value

**PASS (self-review).** A closed loop removes endpoint-frame mismatch while exposing algorithmic dissipation and geometric phase. The exact spectral radius, nonnormal singular-value correction, and sharp \(1/N\) global-error constant give a reproducible, parameter-free benchmark for numerical covariant transport inside low-rank algorithms. In particular, the spectral damping factor alone would underestimate worst-case norm loss because the finite-grid map is nonnormal. This is more informative for assessing an integrator than a generic order-one statement; no claims are made about full optimal-control gradient accuracy.

## Closest sources and limitations

The closest source is B. Carrel and T. Vanzan, *Dynamical low-rank approximations for the optimal control of matrix ODEs*, 2026-10-21, arXiv:2610.29554v1, §5.2.1. The mathematical technique of tangent projection is known. The precise claim is the finite-grid loop spectrum/singular values and sharp error constant for a concrete rank-one curve. Residual risks include unlocated classical closed forms for products of rotating orthogonal projections and lack of independent examination. Verification of finitely many grids supports, but does not prove, the universal formula or asymptotics.

Self-review: passed. Independent audit: not yet performed.
