# Independent mathematical audit

## correctness

PASS

For fixed 0<p<1, the invariant measure is normalized Lebesgue measure on R_p, not on the whole torus including the untwisted complement. Starting on the overlap, the horizontal iterates stay outside the vertical strip until the first horizontal return; the last horizontal shear and first vertical shear count as one full step. Subsequent vertical iterates stay outside the horizontal strip until the first full return. This gives T=G_S∘F_S, τ=a+b−1 and derivative V_{b/p}U_{a/p}. Conditional rotation Kac gives E a=E b=1/p, with preservation of overlap measure under F_S needed for the second equality. The cone v≥u/p≥0 is invariant since v′−u′/p=(b−1)u/p+[1+a(b−1)/p²]v. Within it the mass fraction on v is at least 1/(1+p), yielding expansion both by ab/[p²(1+p)] and by the minimal-matrix column bound 1+p^(−2)+1/(1+p). Positive products tested on (1,1) give the top ℓ¹ growth up to a factor 2. For each j≥1, conditioning on x makes x+j(y/p) mod 1 uniform; the probability of a horizontal hit at that time is p, whether or not other hit events are dependent. Union bounding the integers j<e^(−t)/p gives P(pa<e^(−t))≤e^(−t), and integrating proves E log a≥log(1/p)−1; symmetry gives the same bound for b. The two shear norms bound expansion above by (1+a/p)(1+b/p); Jensen and the Kac means give the stated upper bound. Ergodicity on the invariant union is the imported hypothesis verified for this family in the primary literature. Return-time normalization follows directly along the return subsequence from Birkhoff and the full-time almost-sure exponent. After division by 2/p−1, the lower thin-width branch has error −p+O(p²log(1/p)) and the upper error is O(p²log(1/p)), proving the claimed coefficient; the other lower branch proves positivity at every fixed p. verify.py was inspected as supplementary evidence, not run or used to prove the infinite-parameter inequality. No claim is made at the degenerate endpoint p=0 or for exceptional orbits.

## originality

PASS

The supported distinct contribution is the sharp thin-strip law and matching all-width enclosure, not the return formalism, Kac factor, positivity, or the pointwise minimal-cone bound alone. The prior paper treats exactly the same family, but its partition-based estimators stop at positive widths and the available pointwise-minimum estimate loses a factor of two in the leading lower coefficient.

## value

PASS

The law determines the actual rate of vanishing of the typical full-time exponent even though the individual shears diverge. The all-width enclosure is usable below the earlier return-partition cutoff, and the leading coefficient distinguishes typical return-size growth from the weaker estimate based only on the smallest possible return.

The dated certificate retains the supplied scientific assessment, sources and limitations.
