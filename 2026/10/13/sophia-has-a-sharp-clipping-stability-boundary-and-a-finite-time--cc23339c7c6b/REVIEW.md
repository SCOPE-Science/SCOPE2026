# Independent mathematical audit

## correctness

PASS

The practical update divides h_i x_i by γh_i under the floor inequality (ties do not change the quotient). In signed coordinates x has the starting sign before first entry; from x_0>γ it decreases by η until the first integer N_i for which x_0−N_iη≤γ. The landing point is greater than γ−η>−γ. This proves the exact ceiling even if the final saturated step changes sign: the proof's informal magnitude wording should be read as subtraction in the starting signed coordinate. Negative starts follow by odd symmetry. The core is invariant because |1−η/γ|<1. Outside it, 0<η<2|x| gives strict decrease of |x|; positive curvatures give strict objective decrease away from zero. At and above η=2γ the signed points ±η/2 are exchanged, including equality. At η=γ the shrinkage law subtracts γ from the magnitude up to zero; its exact iteration gives the first all-zero iterate. The common linear multiplier after max N_i squares in the quadratic objective.

## originality

PASS

The practical algorithm and scalar gradient-clipping map class are known, as are the qualitative transient/contraction split and soft-thresholding. The supported distinct claim is the exact joint calibration for practical diagonal quadratic Sophia: an all-start iff stability range with explicit obstruction throughout the excluded range, the clipped-core first passage law and exact resonance hitting time. The compared known analyses of the same scalar recurrence as clipped gradient descent bound accuracy or transient overhead, rather than giving that all-start description. Closest indexed analogue AGC behaves differently beyond a second outer threshold.

## value

PASS

For the concrete optimizer update, this determines the stable parameter range uniformly over positive diagonal curvature spectra, gives a simple failure witness for every excluded step, and gives an exact time to stop clipping and an exact hitting prediction at the matched step. This is a useful calibration and implementation benchmark under explicitly idealized hypotheses. The value lies in the exact finite trajectory and sharp stability test together, not in the soft-threshold identity or generic local linearization alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
