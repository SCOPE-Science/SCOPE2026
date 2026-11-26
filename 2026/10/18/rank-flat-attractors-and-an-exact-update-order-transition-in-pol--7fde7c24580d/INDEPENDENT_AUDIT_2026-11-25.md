# Independent mathematical audit

## correctness

PASS

Use the initial orthogonal singular-vector pairs with signed coefficients y, even for repeated singular values; the partial polar factor acts by sign(y), with sign(0)=0, in these pairs. For q>0 the post-step positive radii follow |qs−τ|, and the reverse triangle inequality gives contraction to δ=τ/(1+q) for every mode that stays nonzero. Zero is absorbing and is not governed by the positive-radius formula. More explicitly the first positive zero preimage is τ/q>τ, and every radius >τ has exactly one positive preimage (radius+τ)/q. The exceptional radii are therefore τ∑_(i=1)^j q^−i, j≥1. All surviving radii eventually satisfy qs<τ; then the post signed modes flip for α>0 and preserve sign for α<0, yielding the stated antipodal limits or the fixed matrix. Pre equals post for α>0. For α<0 pre always flips on nonzero modes and has radial map qs+τ, converging to τ/(1−q). In the nonresonant rank-r comparison the Frobenius factors √r cancel, giving ηa/(2−ηa); the post objective is 3rλ²/(2a) when α<0. The critical step has post zero and pre an exact cycle after one step. The prox radii decrease by at least τ while positive, so they hit the unique minimizer in finitely many steps. The normalized nonzero spectrum becomes uniform on the surviving rank, proving the effective-rank assertion. The nonzero rank-r and Frobenius-ratio claims are read with the nonresonance condition in Finding and Limitations (not for every positive-rank initialization); for example α=−1/2, τ=1, y₀=2 gives post zero and pre nonzero.

## originality

PASS

Pass the supported distinct comparison of three constant-step rules on the centered isotropic quadratic, especially the pre/post asymptotic order split and diverging norm ratio. The rules themselves are known, and the post-only rank/floor/phase theorem overlaps materially with a distinct later-dated catalogue finding. Treat neither the post-only theorem nor classical soft thresholding as a separately substantiated novelty here.

## value

PASS

The comparison is a motivated counterbenchmark for reading an additive polar correction as rank reduction or a proximal step, and for reading a one-step order bound as long-run robustness. Above the critical step the two methods exhibit qualitatively different matrix attractors, with an exact dimension-independent nonresonant ratio that diverges at the stability boundary. That comparative result is the useful contribution, not textbook proximal thresholding by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
