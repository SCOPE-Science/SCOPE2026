# Review of exact Hilbert distortion for centrally slab-truncated cross-polytopes

## Correctness
PASS. The global Banach--Mazur optimization reduces to permutation-invariant quadratic forms by averaging both sides of a norm/ellipsoid sandwich. The slab intersection's vertices give the sharp quadratic outer extremum. All \(2^n\) sign choices in the dual \(\ell_1\) norm and the one-dimensional sum functional give the sharp inner extremum. The two branches meet at an explicitly computable quadratic parameter, and direct derivatives prove the unique invariant optimum for every real slab width, including even/odd and two-dimensional boundary cases. The checker reproduces the formula with exact rational arithmetic in 60 nonexhaustive instances.

## Originality
PASS, with residual priority risk. The closest inspected references are Kobos–Varivoda (arXiv:2305.06427v1), which treats the distance between two different endpoint bodies in small dimensions, and Vasil'eva (arXiv:2303.13147v1), which estimates Kolmogorov widths, not Banach--Mazur distance, for different ball intersections. A public exact-distortion result for quadratic \(\ell_1\)–\(\ell_\infty\) mixtures has a different norm, no sum-coordinate slab, and no implication giving these formulas. General distance-ellipsoid characterizations and the classical \(\ell_1\) endpoint do not determine the nontrivial slab-dependent law. No accessible covering result was located by the stated source, terminology, and equivalence searches, but some older convex-geometric literature may be incompletely indexed.

## Mathematical value
PASS. The one-parameter family is the canonical cross-polytope truncated by two parallel hyperplanes normal to the all-ones direction, a natural model of an \(\ell_1\) constraint with a global conservation penalty. The exact all-dimensional Banach--Mazur formula quantifies how increasingly strong conservation changes Hilbertian distortion, identifies an optimal anisotropic ellipsoid, and detects a genuine parity effect in nearly balanced sign vectors. The statement is a complete classification, not an arbitrary sample or a generic endpoint bound.

## Limitations
The uniqueness assertion applies only to permutation-invariant optimal shapes. The real-field and finite-dimensional hypotheses are essential to the stated proof. The historical-priority assessment is qualified and not an independent certification. No part of the finite checker proves the continuum or infinite family by enumeration.

Self-review: passed. Independent audit: not yet performed.
