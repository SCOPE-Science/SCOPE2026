# Independent mathematical audit

## correctness

PASS

The frozen method definition uses I both for the lower cumulative quadrature (first row zero) and for the identity in all three solves, an ambiguity that makes the literal sweep inconsistent for x0≠0. The corrected RESULT separates these matrices and matches the identity in the frozen checker. For the corrected, intended method, the lower block of Q²−Xvv is H. The initial velocity-column error is −c+O(z) and the position-column error is O(z). Propagating and applying the endpoint functional gives the asserted z^(k+1) bottom-right perturbation; the top-right perturbation enters the determinant with a further factor O(z). The exact collocation determinant is one. The Cayley–Hamilton recurrence checks the first four signs exactly; conjugation sqrt(3)↦−sqrt(3) makes the conjugate of qH^k c positive, eliminating the potentially unclassified zero. The other conjugate of 2cos(2θ) is below −2, so the phase is irrational. Schur’s other two inequalities have positive leading terms z and 4, and both signs occur on half the circle, separately also on each parity subsequence. This rechecks the final corrected claim without requiring any numerical extrapolation.

## originality

PASS

The final repaired claim explains the published finite-sweep examples through a solver-specific exact determinant coefficient and an all-sweep-count small-step stability theorem. Neither the founding scheme and table nor the closest indexed phase-law record gives this result or implies it without the new compression and determinant argument. Distinctness is assessed on the statement, not on a presumed priority based on catalogue dates.

## value

PASS

In a published oscillator benchmark with unexplained behavior as the correction count varies, the coefficient pinpoints the first loss of symplecticity and explains why neither odd nor even sweep counts reliably inherit local stability. The all-k density and parity conclusion go beyond a small-instance table and concern a commonly used method with precisely specified initialization and output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
