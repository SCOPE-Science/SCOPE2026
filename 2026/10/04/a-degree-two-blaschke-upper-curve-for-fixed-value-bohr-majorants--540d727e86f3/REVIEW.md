# Review of A degree-two Blaschke upper curve for fixed-value Bohr majorants

## Correctness

PASS. The witness
\[
B_\rho(z)
=
\left(
\frac{z-\sqrt{\rho}}
{1-\sqrt{\rho}\,z}
\right)^2
\]
is a Schur function with the required fixed value. Its Taylor coefficients have the exact form
\[
c_n
=
\rho^{(n-2)/2}(1-\rho)
\left(
n(1-\rho)-(1+\rho)
\right).
\]
For
\[
0<\rho\le1/3,
\]
only the linear coefficient is negative, so the coefficient majorant is obtained exactly from the real value by one sign reversal. Subtracting the disk-automorphism majorant reduces the comparison to the sign of the explicit cubic \(Q_s\).

The proof verifies \(Q_s(1/3)>0\), \(Q_s(1)<0\), and \(Q_s'<0\) throughout the interval. Hence there is exactly one crossing and the same explicit witness violates the universal comparison at every larger radius. The source lower theorem supplies the matching left endpoint \(1/3\).

## Originality

PASS. The current primary source was inspected through its Schur-algorithm proof, fixed-value corollary, and final open problem. It gives a lower validity range but no upper curve for a prescribed nonzero value. The degree-two Blaschke family and its cubic crossing are not stated there.

The Bhowmik--Das predecessor is cited by the primary source for the radius-\(1/3\) subordinate-majorant comparison, again a lower guarantee. Khasyanov's full 2023 article was inspected around its fixed-initial-coefficient definition and main convolution theorem; it studies comparison with a uniform norm bound for operator pairs, not the present automorphism-majorant target.

Candidate-specific database and literature searches using the source identifier, fixed-value Schur majorants, squared automorphisms, and degree-two Blaschke products found no implication-equivalent statement. The closest indexed findings concern different Bohr-radius problems, including powered shifts and constrained section radii.

## Value

PASS. Brevig's note explicitly leaves the fixed-value radius as its closing open problem. The finding gives a natural, fully explicit upper obstruction on an entire parameter interval rather than at an arbitrary isolated value. It converts a simple inner function into a computable algebraic upper curve and gives a concrete numerical bracket at the transition value \(\rho=1/3\).

The result is intentionally a boundary theorem, not a claimed full solution: it narrows a newly stated extremal problem and identifies a reproducible degree-two obstruction that future sharper candidates must beat.

Same-model review: passed. Independent audit: not yet performed.
