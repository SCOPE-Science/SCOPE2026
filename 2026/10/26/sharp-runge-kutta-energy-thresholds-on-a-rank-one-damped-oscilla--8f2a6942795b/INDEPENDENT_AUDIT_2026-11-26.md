# Independent mathematical audit

## correctness

PASS

For the given real generator, L²+L+I=0, so each Taylor polynomial reduces to R=aI+bL. With δ=a²−ab+b²=det R and tr(RᵀR)=2δ+b², the largest singular value is (sqrt(4δ+b²)+|b|)/2. Thus the two signs 1−δ±b≥0 characterize contraction exactly. I reconstructed their factors: RK2 gives −h³(h−2)/4 and −h(h−2)(h²+4)/4; RK3 gives −h³[(h−1)³−5]/36 and −hE(h)/36; RK4 gives −h³(h−2)Q(h)/576 and −hF4(h)/576 in the record's notation. These yield the full intervals including h=0 and endpoint inclusion: E is negative up to its sole positive root, by the derivative bound on [0,2] and the strictly increasing shift beyond 2, and the cubic factor is negative up to that root (<5/2). For RK4, Q>0 and F4<0 on [0,2] and the Q factor alone rules out all h>2. Exact determinant and trace at 9/4 confirm strict RK3 contraction, RK4 norm growth, and RK4 spectral radius squared 1949353/4194304. Independent exact arithmetic: python /workspace/branches/math_checks.py 3; the printed decimal root is only a rendering. The frozen verify.py and recorded verification notes were inspected, not rerun. This is a Euclidean one-step result, not a nonlinear energy or accuracy claim.

## originality

PASS

The supported distinct finding is the global same-matrix RK3/RK4 threshold comparison and spectral-versus-energy witness, with RK2 as a baseline. The canonical matrix, qualitative strong-stability phenomena, and the RK2 slice found separately in a broader catalogue record are not credited as distinct discoveries here. No inspected stronger statement implies the RK3 and RK4 thresholds on this matrix.

## value

PASS

The minimal rank-one-damped hypocoercive benchmark occurs in strong-stability theory, and its exact semigroup strictly dissipates energy. Matching all step sizes rather than finding one failure exposes a roughly 19% larger safe step for RK3 than RK4, while 9/4 separates norm stability from eigenvalue stability in exact arithmetic. This is a meaningful fixed-matrix benchmark independent of the already covered RK2 slice, not a general method-order or accuracy claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
