# Independent mathematical audit

## correctness

PASS

Testing (1+lambda)c-C inside lambda C on the two bases is sufficient by convexity. At q=1+lambda, set x=q(1-t), y=qt. The endpoint heights require x,y>=1; the slice support tests for the two directions +/-u give exactly q|u.z| <= x h_K+y h_L-2 max(h_K,h_L). These tests also imply c is in C, by expressing it as a convex combination of a point and its scaled reflected image in C. Zero translation is feasible precisely when the right side is nonnegative in every direction. Minimization therefore reduces to the two inequalities of RESULT.md (78) in U=x-1,V=y-1; in directions where a ratio is truncated at 1 the corresponding constraint is redundant. In each corner region the binding constraint forces the stated unique optimum, including equality on the phase boundary. In the mixed region the positive dual coefficients and the nonzero active determinant certify uniqueness, and the doubly symmetric case alpha=beta=1 gives the origin of the LP. Axis tests are necessary for aligned boxes; summing the coordinate bounds and bounding the maximum of the sums by the sum of the maxima proves sufficiency. The crossed boxes give (3-epsilon)/(1+epsilon) and common factors extend sharpness to base dimension at least two. The upper bound 3 is not attained. These arguments are universal; the 1,320 exact LP profiles and sampled directions in VERIFICATION.md are author-recorded finite corroboration, not rerun or needed for the proof.

## originality

PASS

The supported distinct part is the ratio/phase law and full center set for arbitrary, possibly nonhomothetic, centrally symmetric bases sharing a horizontal space. Standard reflection calculus and the overlapping homothetic case are not credited as original. No equivalent or stronger covering claim was identified in the inspected evidence; this is a best-of-knowledge decision, not a priority certification.

## value

PASS

This is a complete optimizer law for a natural convex-body invariant on a broad class, not an isolated polytope computation. It reduces an all-directions minimization to two measurable containment ratios while still recovering every possible center. Crossed and near-nested examples show distinct behavior, including nonunique horizontal centers; both exact attainment conditions and the sharp unattained uniform cap are geometrically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
