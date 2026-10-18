# Scientific review: sharp three-moment Hardy multiplier design

## Correctness — PASS
For every integer \(n\ge2\), vanishing first moments make the truncated Hermitian Toeplitz moment matrix block-diagonal except for one \(6\times6\) contraction block. The classical truncated trigonometric moment theorem proves that this matrix characterization is exhaustive. The Herglotz and Schur transforms identify the first three nonzero moments with the first three Taylor coefficients of a Schur function; the restriction \(n\ge2\) is needed to prevent lower-order cross terms. A two-variable scalar optimization yields the exact constant \((7+14\sqrt7)/27\), with strict uniqueness of the optimal magnitudes. Equality in Schwarz--Pick forces a degree-one disk automorphism, which gives the complete family of unique atomic measures. Boundary angular derivatives prove positivity and the explicit weights. The finite numerical and exact symbolic checks in `verify.py` agree with these calculations, but the analytic argument establishes the general theorem.

## Originality — PASS (best-knowledge comparison)
The 2022 full-text approximation-preserving operator theorem characterizes admissible Hardy multipliers through a positive-real-part condition, and discusses two-coefficient Landau bounds; its inspected theorem and applications do not state the optimized joint three-free-coefficient law or the exact equality quadrature. Classical Schur--Carathéodory--Toeplitz theory *already implies the general feasibility mechanism* and is credited explicitly; it is not claimed as a new foundational theorem. Positive quadrature through quasi-paraorthogonal polynomials is also prior art. The more specific exact aggregate optimum and complete realization by a two-phase family of \(n+2\)-point positive measures were not located in the checked primary sources or mathematical-record comparisons. An older equivalent result formulated as a three-coefficient Schur majorant or a Bohr-type sum is a substantive unresolved bibliographic risk.

## Mathematical value — PASS
The first three unconstrained coefficients of a normalized approximation-preserving multiplier are a canonical finite-dimensional design quantity: they control the earliest deviations of the multiplier from its forced zero pattern. A full body of feasible triples, a sharp algebraic maximum, *every* extremal phase choice, and the smallest positive realization supply more than a normalization or illustrative example. Each degree admits an explicit node polynomial and strictly positive interpolation weights. No general theorem about all coefficient sums or approximation-error stability is claimed.

## Closest sources and limitations
- Abdullayev--Savchuk--Savchuk, arXiv:2206.11841v1 (2022): general BAP criterion and individual/weighted Hardy coefficient applications, used as starting point.
- Bultheel--Cruz-Barroso--Díaz Mendoza, arXiv:2110.10460 (2021): positive unit-circle quadrature and quasi-paraorthogonality, not an exact three-moment sum in inspected material.
- Classical Schur algorithm and truncated trigonometric moment theorem: general coefficient-feasibility tools which may already make equivalent versions discoverable under other terminology.

The present theorem requires \(n\ge2\). It does not quantify conditioning of the quadrature nodes or solve more than three free moments. The numerical tests supplement rather than replace the proof. The originality classification is best-knowledge, not a proof of uniqueness in the worldwide literature.

Self-review: passed. Independent audit: not yet performed.
