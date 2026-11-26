# Independent mathematical audit

## correctness

PASS

The Cúth–Raunig finite-tree formula applies to the real equilateral metric and evaluates each edge coefficient by a mass cut, with no distance factors other than 1. An independent exact Prüfer-code replay (python3 /workspace/checks/01_tree_certificate.py) checked all 16 trees. All cut magnitudes belong to 0,t,1−t,1,1+t,2; sorted comparison is affine on each side of t=1/2, so comparisons at 0,1/2,1 certify domination throughout and two trees realize the minimum throughout. This gives the p-th power, and the coefficient ℓ2 norm is sqrt(4+2t²). On (0,1/2) the positive numerator of the first fraction in the logarithmic derivative decreases strictly while its denominator increases strictly; the odd-in-t Euclidean derivative term t/(2+t²) increases there. The sign changes once from positive to negative and remains negative for 1/2≤t<1. The expansion is 2+t^p+o(t^p) before taking the p-th root, with the denominator changing only at order t². At p=1 the free norm is half total variation in the coefficient ℓ1 convention (half the sum of absolute masses); equality in ℓ1≤2ℓ2 forces four equal magnitudes and the zero-sum condition forces two of each sign. Permutation and scaling carry the cusp perturbation to every such extremizer. Only the specified family is optimized for p<1. The recorded floating-point diagnostics are not needed and were not used.

## originality

PASS

Credit the general tree formula and the classical p=1 benchmark to existing theory. The distinct supported claim is the analytic symmetry-breaking/unique-optimum result for this signed coefficient profile, with an exact closed cost and a cusp at the classical optimum.

## value

PASS

Four points are the natural first balanced two-source/two-sink equilateral configuration. The chosen path keeps both source masses and total sink mass fixed and varies the single sink imbalance, up to swapping the sinks. The exact shift and its positive Hölder cusp refute persistence of local optimality at every classical global extremizer for all p<1. This is useful even though it does not compute the unrestricted p<1 maximum. The finite tree calculation alone would be a routine instance, not the main value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
