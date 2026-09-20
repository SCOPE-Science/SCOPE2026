# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof was checked along four independent mathematical
interfaces.

First, an algebraic isometry cannot have a nontrivial Jordan block: a
length-two Jordan chain at a unimodular eigenvalue would make
\(\|T^n y\|\) grow at least linearly although every power of an isometry
preserves norm.  Thus the minimal polynomial is square-free and its roots
are precisely the finitely many unimodular eigenvalues.

Second, the interpolation step forcing finite symbol order uses only
distinct points in one finite disk orbit.  If none of
\(\varphi,\ldots,\varphi^d\) is the identity, one can choose a point
outside the finite union of their fixed-point sets, interpolate a scalar
polynomial that isolates the \(d\)-th orbit point, and contradict the
minimal-polynomial identity.  No cancellation between vector-valued terms
is used.

Third, for a finite-order symbol, conjugating it to a rotation produces
the exact intertwining relation
\[
T M_\chi=\omega M_\chi T.
\]
Multiplication by the disk automorphism \(\chi\) is bounded and injective
on \(H^p(\mathcal K)\), so every eigenvalue generates a full
\(\omega\)-orbit.  Since the minimal polynomial is square-free, orbit
counting gives the divisibility \(m\mid d\) and the factorization into
\(t^m-\alpha_j\) factors.

Fourth, the construction
\(Tf(z)=A f(\omega z)\) was checked directly: it is a surjective isometry,
its symbol has the prescribed exact order \(m\), its displayed monomial
eigenvectors realize all \(d\)-th roots of unity, and \(T^d=I\).  Hence
its minimal polynomial is exactly \(t^d-1\).

The tri-circular corollary then follows because three nonzero spectral
projections with distinct coefficients force a square-free cubic minimal
polynomial.

## Originality

**PASS, to the best of our knowledge.** Searches were made for algebraic
and finite-spectrum isometries, algebraic weighted composition operators,
periodic Hardy-space isometries, generalized tri-circular projections,
and equivalent spectral/minimal-polynomial formulations.

The closest inspected current source is Kumar--Kumar--Abu Baker
(arXiv:2609.10718, 2026).  Its Theorem 3.1 treats generalized
tri-circular projections on \(H^p(\mathcal K)\) and explicitly lists
identity, order-two, and order-three disk-symbol cases.  It does not state
the arbitrary-degree divisor theorem or the spectral-orbit factorization.
The present result implies that its order-two alternative is empty under
the genuine three-spectral-subspace hypotheses.

Dutta--Abubaker (arXiv:1204.2360, 2012) obtains periodicity for generalized
\(n\)-circular projections under a separate global hypothesis on
generalized bi-circular projections.  Jiang--Han--Zhou (2020) treats
algebraic weighted composition operators only up to degree two and in a
different scalar \(H^2\) setting.

Two particularly relevant full articles were not inspected.  The
Botelho--Jamison (2015) abstract says that it studies algebraic and
topological properties of surjective isometry groups on vector-valued
function spaces.  The Botelho--Ilišević (2021) abstract says that it gives
necessary conditions for finite spectra of isometries on complex Banach
spaces.  Neither accessible abstract states the Hardy-space
disk-symbol-order divisor law or the root-of-unity orbit factorization,
but an equivalent theorem in either uninspected full text would overturn
the originality assessment.  This is the principal residual risk.

## Value

**PASS.** The result identifies an arithmetic invariant of the analytic
dynamics hidden inside an arbitrary algebraic Hardy-space isometry:
symbol order must divide minimal-polynomial degree, and the spectrum is
forced into complete root-of-unity orbits.  The result is sharp for every
divisor and supplies a reusable intertwining mechanism.  Its cubic
specialization also gives a short structural obstruction directly relevant
to a recent generalized tri-circular classification.

## Verification status

No independent validation, formal verification, or peer review is claimed.
