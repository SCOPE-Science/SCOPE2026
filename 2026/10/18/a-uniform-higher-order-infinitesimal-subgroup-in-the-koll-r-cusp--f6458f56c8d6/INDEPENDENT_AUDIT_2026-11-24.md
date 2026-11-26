# Independent mathematical audit

## correctness

PASS

The affine right-hand side X^(q+2)+X has derivative 1, so is not a square in k(X) and gives an irreducible purely inseparable polynomial in Y. The partial derivatives and tangent cone give the unique geometric singular point [0:1:0] and tangent Z=0. For geometric points one may therefore use the flag-preserving form in the proof: the X^2 Z^q, X^q Z^2 and Z^(q+2) coefficients successively kill the three off-diagonal entries, with the first two monomials distinct because q>=4. The remaining diagonal is (1,lambda^2,lambda), lambda^(q+1)=1. The dual-number coefficient map is Z^q(Z delta X+X delta Z); proportionality to F forces zero coefficient of proportionality, then delta X and delta Z are common scalar multiples of X and Z. Modulo scalars the entire middle row remains, giving dimension three. Over arbitrary k-algebras the middle-row changes preserve F by Frobenius with a^q=b^q=0 and c^q=1. Multiplication is (a,b,c)(a',b',c')=(a+c a',b+c b',cc'); conjugation by the reduced diagonal scales a,b by lambda^2,lambda and fixes c. The product embeds by the explicit projective representative with X-coordinate coefficient 1 and Z-coordinate multiplier lambda: these coordinates recover both factors, and the finite image is closed. The connected coordinate algebra has q^3 basis monomials using a,b,c-1, so the semidirect product has length q^3(q+1). G_q is finite by finite type and its finite geometric point set. The embedded subgroup exhausts points and tangent directions only, not necessarily the scheme. The independent check `python3 /workspace/audit_recompute.py 5` reproduced the F4 coefficient census 1,3,1 and Lie-map rank 5 for q=4,8,16. These finite checks do not certify higher-order subgroup structure; the arbitrary-base symbolic identity does.

## originality

PASS

Pass only the explicit higher-order length-q^3(q+1) semidirect subgroup and ensuing lower bound. The family, cusp, reduced group and Lie dimension are prior facts and not credited as new. No checked stronger or equivalent result constructs this subgroup or gives a covering calculation of the full scheme for this family.

## value

PASS

The subgroup simultaneously extends every prior tangent direction through Frobenius height n and includes the full reduced part. Its explicit multiplication and quantitative bound give usable scheme data for an embedded family of unbounded degree, where points and tangent dimension otherwise conceal the extent of nonreducedness. This is a concrete invariant and lower bound, not a claim to have computed the full stabilizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
