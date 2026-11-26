# Independent mathematical audit

## correctness

PASS

With a ≥ b ≥ 0 for the normal (a,b), integrating the uniform square cap gives the triangular cap fraction (a+b−q)^2/(8ab) up to b/a and thereafter the trapezoid fraction (a−q)/(2a) up to half the area. Maximizing the linear functional on the downwards first-quadrant hyperbola gives the same threshold, either at the axis endpoint or at the stated tangent point; reflection extends the support check to all directions. This candidate is convex (the first-quadrant graph is concave and decreases, and reflections yield a convex unconditional set). On the triangular branch the support is f(s)=s−2√α√(s²−1), s=a+b, strictly convex. Its critical point lies beyond the switch b/a=2α when α≤1/8: its sin(2θ)=4α/(1−4α) exceeds 4α/(1+4α²) at the switch. It reaches the diagonal at 1/8. After that f decreases up to the diagonal, including when α≥1/4 and the formal stationary point ceases to exist. The circumradius maximizes (x+y−1)^2+1−4α on the hyperbolic arc and hence occurs on axis or diagonal; their only tie in the open range is α*=3/2−√2, and strict convexity gives no additional contacts. To exclude translations, apply the inner and outer support inequalities to both u and −u; symmetry of the body yields a centered sandwich of the same shape and factor. Linear inner constraints on the positive-definite shape matrix and convex outer inverse-matrix constraints persist under averaging over the dihedral group. Convexity of xᵀM⁻¹x follows also by writing it as sup_y(2xᵀy−yᵀMy). The averaged matrix is scalar. The profile decreases up to α*, increases to 1/8, and above 1/8 factors exactly to √α+1/√2, strictly increasing. The exact minimum evaluated independently at high precision is 1.02216216905878774068. Affine equivariance follows because all cap areas and the original area scale by the same determinant. The frozen checker was inspected, not executed; the proof covers every allowed depth and affine sandwich, whereas the sampled checks cannot do so.

## originality

PASS

The credited square contour and general affine-optimality principles are not new. No verified earlier statement or stronger quantitative theorem in the inspected evidence determines the full disk-distance profile, optimizing cap fraction and ordered inner/outer transitions. This is a comparison of the retained optimization only, not historical-priority certification.

## value

PASS

The least affinely distorted central region in a depth filtration is a natural and invariant question. This result gives the whole profile for the affine class of parallelograms, rather than just a numerical best depth, and identifies two separate changes of contact pattern. The sharper information distinguishes the optimal trimming level from the inradius transition and shows why optimizing in a fixed square normalization is nevertheless affine-sharp. It does not extend to general polygons by this argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
