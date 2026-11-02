# Independent mathematical audit

## correctness

PASS

PASS: At the simplex barycenter exact away-step minimization is interior, and the derivative of each vertex step on H is P_j=I−n/(n−1)w_jw_j^T, an orthogonal projection. The scalar partial-sum recurrence yields B_n(z)=(1+(n−1)z)^n−n^n z^(n−1); B_n has exactly a double root at 1, n−2 simple nonunit roots, plus one simple zero. Projection-norm strictness proves all nonunit roots have modulus<1. Analytic zero convergence and first nonreal Lambert W branch yield the spectral-radius limit 0.1238303227… and sharp uniform local linear rate. Independent exact rational charpolys n=3..8 reconstruct the same closed form. Boundary n=3 gives {0,−1/8}, n=4 nonreal pair; the theorem is explicitly local and requires away steps.

## originality

PASS

Best-of-knowledge original: exact evaluated local Jacobian spectrum and Lambert-W limit for the original away-step simplex sweep, distinct from the published generic PolyCDwA convergence theorem and classical cyclic-projection machinery.

## value

PASS

PASS: An explicit sharp spectrum and limiting rate for a canonical, original nontrivial vertex-cyclic algorithm are useful for estimating sweep speed and distinguishing local from global bounds. It is more than the known qualitative linear-convergence statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
