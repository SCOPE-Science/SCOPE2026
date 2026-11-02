# Independent mathematical audit

## correctness

PASS

For odd n=2m+1, alpha=pi/n, c=cos(alpha), s=sin(alpha), area(P)=nsc. For the edge from (c,-s) to (c,s), normals from edge interiors meet the polygon in the strip |y|<=s. The upper omitted cap has vertices v_0,...,v_(m-1), q=(-1+s²/c,s) on the final edge, with shoelace area 2C=(s/c)(2(m-1)c²-2c+1); the lower cap is congruent. This yields U_E=(s/c)(3c²+2c-1). Hann planar identity, reproduced in Domokos--Langi Remark 1, equates total vertex and edge active areas, giving mean=2n U_E/(nsc)=6+4/c-2/c²=8-2(sec(alpha)-1)² for all odd n>=3. Since sec(pi/n)-1 decreases with n and sec(x)-1=x²/2+O(x⁴), the claimed strict increase, n=3 value 6, and quartic asymptotic follow. An independently written clipping code matched formula for odd n=3,5,7,9,11,13,17,31,51,101 to ~1e-14 and a 100,000-interior-point Monte Carlo face-normal census corroborated n<=17. These finite checks are not the general proof.

## originality

PASS

Best-of-knowledge PASS, with specific historical access risks. Three materially inspected primary full texts supply the general identity, parity-specific known equality and triangle special case, but none of those statements implies the full odd n>=5 formula and quartic deficit. The complete family requires an independent polygonal active-strip cap-area computation. Resultary and exact-form/decimal searches found no independent priority match, which is not itself proof of novelty.

## value

PASS

The mean number of boundary normals is a natural classical Santaló invariant. Odd regular n-gons form the canonical non-centrally-symmetric counterparts to even regular polygons known to have mean 8. The exact full-family computation identifies a nontrivial quartic deficit 8-mean=pi^4/(2n^4)+O(n^-6), supplying a rigorous benchmark for planar extremal investigations. It is not a table recomputation or a trivial substitution: it requires evaluating active strip geometry for all odd orders. This does not resolve whether arbitrary convex bodies can have mean >8.

The dated certificate retains the supplied scientific assessment, sources and limitations.
