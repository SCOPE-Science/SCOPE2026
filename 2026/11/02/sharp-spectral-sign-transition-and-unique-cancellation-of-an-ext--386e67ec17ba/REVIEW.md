# Independent mathematical audit

## correctness

PASS

For every SPD symmetric A and nonzero fixed terminal v, diagonalization gives Δ=1/2 Σc_j(z_j^2−1)>0 and D=1/4 Σc_j(z_j−1)(z_j−3), where c_j=λ_j|v_j|²,z_j=e^(hλ_j)>1. Thus D/Δ is a positive modal-drop-weighted mean of increasing r(hλ)=(e^(hλ)−3)/(2(e^(hλ)+1)), proving sharp eigenvector-attained bounds. For fixed v, write M=Σ c(z−1)²/Σ c(z−1). Each y_j=z_j−1 and logarithmic growth ℓ_j=y_j′/y_j increase with λ_j; differentiating M yields Σ p_j y_j′+Cov_p(y,ℓ)>0. Since M(0+)=0 and M(infinity)=infinity, exactly one positive h solves M=2, between ln3/b_active and ln3/a_active with strict interior if distinct active rates. Independent exact witness A=diag(1,2),h=ln2,v=(sqrt6,1) gives E(v)=4,E(w)=28,E(2v−w)=4 so D=0 and Δ=24.

## originality

PASS

PASS best of knowledge: Shergill-Williams arXiv 2610.30454 full primary §3.1 Eq (7) defines the very same symmetric energy, Proposition 1 gives a first-order O(h) dissipation linkage; its later algorithms concern adaptive SSAV-BDF2 and do not state the global exactly-sampled SPD spectral ratio envelope, unique all-h fixed-terminal zero, or two-mode exact cancellation. The source owns the monitor; only the new finite-lookback classification is assessed as original.

## value

PASS

PASS: a sharp negative-to-positive sign transition and an exact zero-with-positive-loss counterexample reveal a meaningful finite-lookback limitation of a practically motivated energy monitor. The all-spectrum fixed-terminal uniqueness law and eigenvalue bounds are useful as calibration and benchmark facts without implying numerical scheme failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
