# Independent mathematical audit

## correctness

PASS

Checked the inverse of the compressed resolvent, not the compression of A. In the Krylov basis with first vector b/||b||, the off-diagonal of J is the positive standard deviation of r_i under b_i² weights, giving distinct nodes. Equality of a Ritz node with a spectral endpoint would require a nonzero affine function of r_i to vanish at the other two distinct levels. Affine exactness gives the coordinate multiplier as the two-node interpolant of exp[−t(r⁻¹−1)/γ]; its positive slope for t>0 and the sign test at r_min establish the global first crossing, including ties in the largest decay rate. The one- and two-level invariant cases are exact. A separate symbolic moment-pencil calculation in the basis {b,Db} gives the limiting resolvent characteristic polynomial x²−(10/21)x+1/84 and horizon 0.079671742512472362. For D=A_L the same pencil gives, after x=L−h/L, the characteristic polynomial 1/2−h+O(1/L); at x=3/2−h/L it gives h−1/2+O(1/L). These yield the stated root expansions and the logarithm 2 log L+O(1) in the polynomial horizon. The supplied floating-point checks are only corroboration.

## originality

PASS

The supported distinct result is the explicit noncollapsing stiff-limit witness and its unbounded ratio against the polynomial horizon on the same original operator. Neither the shift-and-invert algorithm nor the universal two-node sign law in isolation is credited as new: the latter is a direct time-rescaled consequence of the earlier polynomial sign theorem on a transformed operator. The Finding and prior-work section emphasize the stiff-limit comparison, which was not covered by the sources checked.

## value

PASS

A concrete stiffness counterexample distinguishes positivity failure of two established approximations applied to the same diagonal system. Ordinary Lanczos loses positivity on a time scale tending to zero, but the compressed-resolvent projection retains a quantifiable positive window without preserving positivity forever. This addresses a property not measured by general error estimates; the universal threshold by itself is a reformulation, not the main value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
