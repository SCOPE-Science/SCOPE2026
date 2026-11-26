# Independent mathematical audit

## correctness

PASS

For the specified coordinates the six squares have area 2 each and the eight hexagons area 3 sqrt(3) each. Cauchy's formula and the two cases x>=y+z versus x<=y+z in ordered nonnegative coordinates give the stated brightness and the support-vector orbits A=(14,2,2) and D=(8,8,8), with all signs and permutations. The maximal orbit follows by the Euclidean support bound. For x<=y+z, if s=x+y+z, every coordinate is at most s/2, so 1<=s^2/2 with equality only at (s/2,s/2,0) up to permutation. For x>=y+z set q=y+z: x^2+q^2>=1, and on the normalized arc the concave function 14 cos(theta)+2 sin(theta) is minimized at theta=pi/4, giving the same 12 minimizing directions. The mean is one quarter of total area. For t>=14 only the 24 norm-sqrt(204) vectors can contribute caps. Mixed dominant-coordinate pairs have dot at most 60; for matching dominant coordinate and sign the only two separations are one or two minority-sign flips, giving products 196 and 188 with counts 24 and 12, and no triangle of 196-edges. The contact bound is the norm of the pair midpoint, so for t>=10 sqrt(2) caps are disjoint in area, and down to 14 only the 24 first-contact lenses contribute. The lens angles follow from the spherical triangle of the two centers and a boundary intersection; Gauss–Bonnet subtracts the two small-circle geodesic-curvature integrals from twice the interior angle. Thus the claimed CDF correction has the positive inclusion–exclusion sign. At tangency the scaled lens is 2|a|+(t_c/2)b^2<1, giving area (4/3)sqrt(2/t_c) per lens at scale eps^(3/2). At each isolated minimum the leading increment is 8|b|+6(sqrt(2)|a|-|b|)_+, a coercive cone with unit area 7 sqrt(2)/192; for 0<=b<=1/8 its positive-a extent is (1-2b)/(6 sqrt(2)). Rescaling and using the tangent Jacobian tending to 1 proves both asymptotic constants. Replay: python3 /workspace/reproduction/frozen_checks.py 3, yielding the complete pair-product histogram, exact nearest-pair triangle absence and independent lens-area quadrature by latitude, with normalized cusp 0.9999998589 at eps=10^-7. Independent projected-vertex hull comparisons also support the directional formula. The frozen checker was read, not executed; its second-largest-product test at the comma is an assertion message rather than a second condition, but the independent enumeration verifies the needed fact. Finite computations do not replace the continuum arguments.

## originality

PASS

Abas already gives the same pointwise brightness up to edge-scale conversion and its first moments. Its spherical co-area and aperture rules also apply to brightness; this is substantive prior coverage of the implicit distribution and general evaluation framework. A published Resultary entry additionally gives the same extrema and equality directions. Credit is limited to the claim's explicitly evaluated two terminal branches, sharp extent of the linear branch, first-overlap cusp and lower endpoint coefficient. The inspected prior coverage does not evaluate this geometry for the same projected-area law.

## value

PASS

The space-filling Archimedean solid is canonical and planar projected area is a natural stereological observable. The two evaluated high-brightness regimes and the exact local exponents and coefficients furnish useful benchmarks for random shadows. The maximal linear branch ends for a geometric reason (first cap contact), whereas the lower power is controlled by a genuinely different cone of directions. The value is in the quantitative distributional evaluation, not in recomputing the classical mean or repeating a general co-area formula. No elementary middle-CDF result is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
