# Independent mathematical audit

## correctness

PASS

At a projective gradient zero, a zero coordinate would force every coordinate to vanish. In characteristic 2 the gradient is the cyclic list of squares; otherwise multiplying the nonzero-coordinate gradient equations forces 33=0. In characteristic 3, normalizing X_0=1 gives (1,t,t^-1,t^3,t^-5) with t^11=1, and the cubic itself is 5t=2t, not zero. In characteristic 11 the second affine gradient equation forces a,b to be units, and the first then forces s to be a unit. Eliminating with the first, second and fourth gives a=5s^2, b=s^-2, c=5s^-5, and the third gives s^11=4; the fifth is then automatic. This establishes an isomorphism of quotient rings, not just solution-set equality. Euler's identity eliminates the cubic equation from the homogeneous gradient ideal in the chart; equivalently adjoining the cubic to the four affine derivatives recovers the fifth homogeneous derivative. Thus the algebra is k[s]/((s-4)^11) after algebraic closure and the geometric support is P. The rank of the quadratic form is 3, also seen from the one-dimensional tangent to this singular scheme and the affine Hessian at P. Reducibility or nonreducedness would give a positive-dimensional singular locus, and the integral hypersurface satisfies S2 and R1, hence is normal. In centered projective coordinates the equation is X_0 Q(u)+C(u); projection from P has inverse [-C(u):Q(u)u] where Q is nonzero. A direction with Q nonzero contributes one nonvertex point, one with Q=0 and C nonzero contributes none, and Q=C=0 contributes q. A separate finite replay in branches/1cdf91fe-b44d-486d-9f0f-6f8e0fa60d78/check_record3.py confirmed rank 3, 16105 projective representatives and 1464 cubic points over F_11, and the two direction counts 133 and 12 giving the same total. These finite checks are not the proof of geometric uniqueness or of smoothness at other primes.

## originality

PASS

Credit the exact description of bad reduction of the literal integral model and the prime-field point-count identity as a global package. The characteristic-11 point was known, and classical projection from the singular point is not distinct. The matched formal-normal-form catalogue entry gives stronger coverage of the local rank and Tjurina-algebra assertions; they are not credited as separate catalogue-distinct achievements on the basis of file dates. The normal-form result does not cover the characteristic-wise geometric assertion or the exact point count.

## value

PASS

This is a natural fixed integral cubic and its only bad prime, singled out by the gradient equations rather than by selecting a number after computation. The exact degeneration and the prime-field count are useful data for studying its bad fiber; the count agreeing with projective space is not a consequence of its rationality. No priority or scientific value is assigned separately to the known point or standard rational projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
