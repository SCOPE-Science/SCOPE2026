# Independent mathematical audit

## correctness

PASS

For the standard polar of cube plus cross-polytope, chambers with sorted positive coordinates map triangularly to a standard Dirichlet simplex, with 2^d d! congruent chambers. This yields volume 2^d/(d+1)!, covariance v_d I with v_d=[2(d+1)-H_(d+1)^2-H_(d+1)^(2)]/[d(d+1)(d+2)], and L=[(d+1)!]^(1/d)*sqrt(v_d)/2. The cross-polytope ratio obeys R_d^2=(d+1)^(2/d)*(1-c_(d+1)/(2d)), c_m=H_m^2+H_m^(2)-2. Fresh exact rational checks verify all 150 dimension-by-dimension independent Dirichlet moment formulas and comparisons d=2..25 (the proof only needs d=2..18). At m=20 the exact base inequality c_m>4log m and the positive increment for m>=6 prove strictness for d>=19, with equality d=1. Harmonic-number asymptotics imply 1-R_d~(log d)^2/(4d); numerical scaled ratios at d=100,1000,10000 corroborate but do not prove the limit. A separate d=2 polygon computation has area 2/3, covariance coordinate 23/432. Normalizations are for uniform volume, not vertices.

## originality

PASS

Black–De Loera provide the actual cube-plus-crosspolytope polar realization/combinatorics; Kipp supplies the affine-invariant isotropic normalization and general local-extremal criteria, not the exact canonical body moments. Two complete published research records were read: one measures radii and vertex shells of precisely the same canonical body, another gives Hanner-class sharp isotropic bounds. Neither entails its uniform interior covariance or strict ratio, as the canonical signohedron for d>=2 is not Hanner (has 3^d-1 vertices, compared to at most 2^d for Hanner). Best-of-knowledge originality PASS, with the possibility of older L1+L∞ norm-ball moment formulas.

## value

PASS

The canonical signohedron is an independently studied symmetric polytope family; its affine-invariant isotropic constant is a natural interior measure invariant. The exact all-dimensional harmonic formula and strict, sharp asymptotic gap relative to the cross-polytope are nontrivial, not determined by the previously classified face/vertex/radius data. Future work on isotropic optimization of explicit polar Minkowski sums could use this benchmark; the claim does not assert global extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
