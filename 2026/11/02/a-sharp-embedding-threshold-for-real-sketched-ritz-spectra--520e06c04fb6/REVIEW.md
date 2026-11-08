# Independent mathematical audit

## correctness

PASS

From AV=VB+R, V^TR=0, and sketch Gram G with spectrum in [1-eps,1+eps] on span(V,AV), H-B=M^-1 CT. The orthogonal cross-block norm is bounded by max_{t in [1-eps,1+eps]}sqrt(eps²-(t-1)²)/t =eps/sqrt(1-eps²). B is real diagonalizable symmetric with simple gap Delta, so disjoint disks of radius <Delta/2 retain exactly one root each under continuous real homotopy; conjugate pairs cannot occur, yielding real simple H roots. Explicit SPD 4x4 A and positive sketch Gram with (G-I)^2=eps²I attain the bound, and the resulting skew-symmetric 2x2 coupling develops a defective real double root and nonreal pair at eps*=delta/sqrt(delta²+gamma²). All claims require joint subspace embedding and exact real arithmetic; k=1 trivial.

## originality

PASS

Best-of-knowledge PASS for an exact attained distortion-to-residual norm bound coupled with a sharp real/nonreal all-Ritz transition under joint-subspace embedding. Liu–Liu 2026 discusses nonreal sketched Ritz and local selected-characteristic-subspace real Schur analysis. Nakatsukasa–Tropp 2024 notes sketched Ritz can have complex estimates and obtains other perturbation results; neither inspected theorem states this complete minimax threshold or the explicit defective transition. The cross-block norm and disk argument may be implicit in classical oblique projection literature, recorded as a priority risk.

## value

PASS

Nonreal eigenvalues for a nonsymmetric compressed approximation to a symmetric problem are an algorithmically motivated instability. An optimal computable sufficient condition in terms of actual Ritz residual, spectral gap and embedding distortion, with a sharp four-dimensional witness and exceptional point, is a meaningful quantitative boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
