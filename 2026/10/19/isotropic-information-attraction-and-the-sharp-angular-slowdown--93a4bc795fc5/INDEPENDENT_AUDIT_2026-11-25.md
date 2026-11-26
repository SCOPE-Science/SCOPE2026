# Independent mathematical audit

## correctness

PASS

Normalize M=(1-lambda)R/rho². In the orthogonal [V,W] basis, the full calibrated update G has blocks (I_q, C-BᵀA^{-1}B) and no off-diagonal term. Hence G and its average with M are SPD, including q=d (empty Schur block). Subtracting tr-logdet divergences with the block determinant factorization gives exactly tr A-logdet A-q+tr(BᵀA^{-1}B), zero iff MV=V. Convexity for the average and spectral compactness of the divergence sublevel set make the decrements summable, force A-I and B to vanish uniformly in the varying ranks, and give both (M-I)V→0 and vanishing matrix increments. The fixed-length frame bound now controls the full error: replace each M in a window by its first iterate at o(1) cost and sum the squared errors on the subspaces; the sum is at least beta times the squared Frobenius error. This proves the stated limits including inverse convergence. The derivative at I is lambda E+(1-lambda)W E W for W=I-VVᵀ. For the two lines in Sym(2), the Frobenius overlap of the rank-one unit projectors is cos²(theta). Their relaxed product is lambda² on the perpendicular line and has trace T and determinant lambda² on their span, giving the two roots and a simple stable dominant root r_+. For a sufficiently small initial error epsilon in its dominant direction, use an eigenbasis norm for the epoch map to bound the iterates by O(epsilon q^m) with r_+<q<sqrt(r_+). The dominant left projection after division by r_+^m has sum of nonlinear corrections O(epsilon²) since q²/r_+<1. It therefore has nonzero asymptotic coefficient; the other components divided by r_+^m tend to zero, proving attainment in the nonlinear SPD recursion. Differentiating the larger root in T at T=1+lambda² gives 1/(1-lambda²), yielding the stated small-angle coefficient. The ordinary forgetting two-cycle has phases with swapped weights 1 and lambda; each has condition number governed by trace 1+lambda and determinant lambda sin²(theta), giving the stated comparison.

## originality

PASS

Credit the exact prior SIFt recursion, the undamped block BFGS/LogDet map, and the exact relaxed-two-projection linear spectrum. The original claim that remains is the deterministic equal-strength isotropic limit for the averaged nonlinear SPD recursion with a uniform subspace frame, together with its calibrated sharp nonlinear epoch rate and the directional-conditioning comparison. The linearized formula by itself is not credited as original.

## value

PASS

The limit determines the selected information matrix from arbitrary SPD starts for nonperiodic varying-rank frames, strengthening the interpretation of uniform bounds in this special equal-strength regime. A sharp nonlinear local rate explains why eventual isotropy can coexist with arbitrarily slow equilibration at near-parallel excitation, while ordinary forgetting retains anisotropy. The practical mathematical distinction survives even after crediting the prior projection spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
