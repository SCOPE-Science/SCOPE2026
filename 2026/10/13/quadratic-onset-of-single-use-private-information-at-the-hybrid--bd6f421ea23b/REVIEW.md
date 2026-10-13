# Self-review

## Correctness
PASS. The final claim is an analytic local theorem. The threshold curvature is \(A(p)=F(a)/a\), the critical fourth derivative is positive, and the strict convexity away from \(z=0\) guarantees that the only emerging nonconvex region is central. The symmetric lower convex envelope is therefore flat between the two nearby minima, which makes the maximum gap occur at \(z=0\). Taylor expansion then gives the stated square-root contact law and quadratic private-information law.

The exact leading coefficient is
\[
K_*=
\frac{6F'(a_*)^2}{3-6a_*^2+3a_*^4-2a_*^6},
\]
and the denominator is positive. The numerical checker only evaluates these exact formulas and finite-deficit ratios; it is not used to turn finite data into an infinite statement.

## Originality
PASS. The 2020 primary source identifies the same threshold equation and uses a numerical second-derivative check to establish convexity above it. The 2026 anchor supplies the convex-envelope identity, an analytic second derivative, a sufficient global convexity lemma, a certified rational nonadditivity point, and finite-grid rates. Neither inspected full text states the quadratic onset, the coefficient \(K_*\), or the square-root contact law. Focused searches under threshold, convex-envelope, critical-exponent, and more-capable aliases found no statement implying the final claim.

## Value
PASS. Near the hybrid wiretap threshold, the single-use benchmark is the quantity against which finite-block nonadditivity is measured. Showing that it vanishes quadratically, while the optimal pooling interval opens only at square-root scale, gives a structural explanation for the sharp near-threshold suppression visible in numerical data. The coefficient is exact and tied to the channel's critical curvature rather than to an arbitrary numerical slice.

## Closest literature and limitations
The closest sources are arXiv:2002.06580v2 and arXiv:2610.03580v1. The former locates the threshold; the latter provides the analytic curvature machinery used here. arXiv:2401.14214v1 studies convex-envelope channel comparison for a classical \(\mathrm{BSC}/\mathrm{BEC}\) pair and does not cover the pure-state adversarial output in the present claim.

The result is local to \(p\uparrow p_*\) on the one-parameter hybrid line. It does not state a multi-use or private-capacity asymptotic.

Self-review: passed. Independent audit: not yet performed.
