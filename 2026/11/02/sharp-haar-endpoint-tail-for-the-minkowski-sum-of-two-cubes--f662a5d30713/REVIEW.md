# Independent mathematical audit

## correctness

PASS

The 20 zonotope minors split into two determinants of modulus 1 and two copies of the sum of absolute rotation entries (cofactor identity), giving V=16(1+L). Each Haar entry has mean absolute value 1/2, and the row unit norms give L>=3, with equality for signed permutations. For the maximum, repeated sign row lines give nuclear norm <=sqrt(18)<5. Normalize the first entry of each remaining sign row to +1: three distinct corners of the resulting square have one diagonal pair, so the product of the three off-diagonal Gram signs is negative. Their Gram matrix is 4I-tt^T, with singular values of the sign matrix 2,2,1. After multiplying rows by t and making the first row all positive by column signs, the other two rows each have a sole plus in different columns. Thus the column sums are ±1 and the polar formula preserves all signs strictly. Distinct sign patterns give distinct polar maximizers; there are 4*3*2*2^3=192, paired across determinant signs by reflecting one row. As a normalization cross-check, in local unit-quaternion coordinates (sqrt(1-|b|^2),b) relative to any proper maximizer, the trace against its positive polar factor gives the exact local deficit 96-V=96(b1^2+b2^2)+128b3^2. The double cover of normalized SO(3) gives density (1-|b|^2)^(-1/2)/pi^2 here. Summing the 96 local ellipsoid volumes at this density gives 1/(6 sqrt(2) pi); away from the maxima compactness gives a strict endpoint gap. The L-deficit rescales by 16. Tail integration against k t^(k-1), or the localized beta integral, multiplies its coefficient by Gamma(5/2)*5^(3/2), giving 20 sqrt(10/pi) for the stated real-k moment asymptotic.

## originality

PASS

The supported distinct finding is the sharp normalized-Haar upper-endpoint coefficient and its equivalent high-moment prefactor. The earlier entrywise-norm maximization already gives L_max=5 and hence the endpoint 96; the equality forms may also encode the optimizer count. Priority for that count is not needed or inferred.

## value

PASS

The coefficient answers a concrete probability question about two randomly oriented cubes, not merely which orientations maximize the volume. It also answers the equivalent 3x3 case of the high-moment problem explicitly motivated in the primary matrix-norm literature. The exact weights of the maximizing configurations are needed; the known endpoint alone does not locate rare-event probability at leading order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
