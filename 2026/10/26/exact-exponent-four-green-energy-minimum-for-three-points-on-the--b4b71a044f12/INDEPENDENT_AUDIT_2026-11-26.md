# Independent mathematical audit

## correctness

PASS

With probability area on the unit sphere, each factor exp(4U) is e²(1−ξ·v)²/4. Write u,v,w for the three off-diagonal Gram entries. In the expansion of the resulting integral T, the even degrees 0, 2, 4, 6 contribute respectively 1, 1+(4/3)Σu, [3+2Σu²+4Σu+8Σuv]/15, and [1+2Σu²+8uvw]/105 (Σuv runs over the three unordered pairs of entries). These follow from the normalized even moments, with denominators 3, 15 and 105. This gives precisely equation (1). Independently, review_evidence/reproduce.py 3 integrates Cartesian monomials on 20 rational unit triples and checks the full rank-five coefficient reconstruction. Substitution of a=u+1/2 and its cyclic analogues gives the deficit 98t+26t²−10Q+8abc. The two independent inequalities are |abc|≤(max|a,b,c|)Q/3≤Q/2 and Q=Σ(S·v_j)²−t²≤6t−t², since t=||S||²/2. They yield 105T−33≥14t+40t², including repeated points. Zero minimum deficit forces S=0; then all three mutual inner products equal −1/2, and conversely that Gram matrix attains 33/105. Its rank-two realizations are congruent by a proper rotation, because the action on the normal line can be chosen to fix the determinant. Multiplication by e⁶/64 gives the exact minimum and the claimed stability coefficients. The finite reproduction tests the polynomial, not the universal bound, which is analytic. No sharpness of individual stability coefficients is claimed.

## originality

PASS

Best-of-knowledge pass for the exponent-four optimum, its equality classification, and the explicit global centroid deficit. The prior three-point exponent-two theorem and even-exponent norm reduction are credited, as is the equilateral candidate. They leave the optimization at exponent four unresolved.

## value

PASS

This is the first even exponent after two in the explicit three-point problem posed by the motivating paper. It converts a numerical candidate into a sharp global theorem and bounds the energy penalty by a geometric imbalance. The particular exponent and cardinality have a prior mathematical motivation, and the deficit offers usable information beyond the minimizing value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
