# Independent mathematical audit

## correctness

PASS

Reconstructed the map from the coordinate updates in RESULT.md lines 23–46. A single step has trace 2(1−r), determinant 1−r and discriminant −4r(1−r). The two-step map has trace 2−4r+4r²−rU and determinant (1−r)². In its real monic quadratic the Schur expressions 1−det and p(1) are strictly positive, respectively r(2−r) and r(U+2−3r); p(−1) is F_U(r). A zero of p(−1) yields distinct multipliers −1 and −(1−r)². If p(−1)<0 there is one root below −1 and a stable complementary eigenline. The intervening phase is fixed and invertible, so the convergence and generic growth conclusions extend to the full trajectory. Independently minimizing the boundary U=5r−6+4/r gives its unique minimum 4√5−6 at the interior r=2/√5; only this r is marginal at q=q*. The quadratic roots are positive, F_U(1)=3−U, and the vertex for U*<U≤3 lies inside (0,1); this recovers all root/interval cases. Phase reversal gives similar products. Exact multiplication at (r,q,t)=(4/5,3,4/5) gives P entries (−7/5,16/25;−4/15,7/75) and p(−1)=−4/15. The exact identities above and RESULT.md lines 30–60 are replay paths. Inspected VERIFICATION.md and verify.py (not executed); the recorded 1,941 checks supplement, not prove, the continuum result. Scope is the declared scalar bilinear, primal-first, fixed-unit-extrapolation, two-periodic schedule in exact arithmetic.

## originality

PASS

The prior qualitative warning and general Schur tools are not new. The inspected primary sources and corpus comparators did not cover the particular two-parameter frontier and its sharp global contrast cutoff for the declared update. This is a bounded statement-level judgment, not a priority certification.

## value

PASS

Reciprocal step balancing keeps the usual product constraint fixed while changing the primal–dual scales. The exact interior most vulnerable product and sharp uniform contrast cutoff quantify when that operation is safe, and separate marginal from unstable trajectories. This adds information beyond a numerical witness or the prior qualitative warning; no extension to adaptive or arbitrary switching is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
