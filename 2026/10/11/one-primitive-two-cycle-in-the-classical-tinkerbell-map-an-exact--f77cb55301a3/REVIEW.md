# Independent mathematical audit

## correctness

PASS

At the assigned Git tree read full RESULT.md and verification/check.py. The complex midpoint/half-difference substitution for F(z)=z^2+Az+B conjugate(z) reduces genuine unordered prime-two orbits to t on the unit circle with P(t)>0 real. The excluded point t=-1 has nonzero imaginary part. Independently recomputed P((1+iu)/(1-iu)) in exact SymPy rational arithmetic: Im(P)=-Q/[50000000(1+u^2)^3] for the displayed sextic Q. Sturm exact rational counting found exactly two real roots, one each in (-123/50,-49/20) and (-183/1000,-181/1000). At the first root Re(P)=+1.726719..., at the second -0.986974..., so only one physical unordered orbit. Direct independent substitution of the displayed two cycle points gave residual norms below 1e-14; exact rational root isolation in supplied verification/check.py covers signs over the intervals. Independently computed the two-step Jacobian with trace 13.7495779 and determinant 73.6865871, with negative discriminant, hence a repelling complex-conjugate multiplier pair. The theorem is whole-plane for one exact rational coefficient tuple, not merely orbit detection inside an attractor.

## originality

PASS

Prior studies by Davidchack et al. (2001) discuss numerical detection of unstable Tinkerbell periodic points and say the rigorous component has a numerical-evidence boundary; Goldsztejn et al. (2011) prove chaos and shadowing by different orbits; Yuan et al. discuss bifurcation windows. Their available statements do not imply a complete algebraic whole-real-plane period-two count. The original 2001 full text and historical monograph are major residual sources, not declared definitively NOT_COVERING merely on abstracts. The self-hit in Resultary was ignored; related period-two classifications concern other maps.

## value

PASS

An exact global real two-cycle count for a standard chaotic polynomial map at its classical rational parameters closes the gap between numerically detected unstable periodic points and provable root completeness. The accompanying strictly repelling return spectrum adds a dynamical classification. The natural invariant is all least-period-two orbits of that specific frequently studied map, not an arbitrary small numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
