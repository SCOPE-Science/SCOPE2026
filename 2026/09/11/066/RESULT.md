# Disproof of the quantitative MOTS eigenvalue vanishing law λ₁A ≤ 8δ near extremal Kerr

## Context

The area–angular-momentum inequality A ≥ 8π|J| for stable marginally outer trapped surfaces (MOTS) in axisymmetric vacuum maximal asymptotically flat initial data (Dain–Reiris), together with the rigidity statement that equality A = 8π|J| is never attained on regular apparent horizons and holds only for extreme Kerr-throat spheres (Reiris), leaves open a quantitative spectral question: must the Andersson–Mars–Simon principal stability eigenvalue λ₁ ≥ 0 vanish at a controlled linear rate as the dimensionless deficit δ = A/(8π|J|) − 1 tends to zero? The admitted target conjectured the explicit near-extremal law λ₁A ≤ 8δ for 0 < δ ≤ 1. The only available MOTS spectra for Kerr covered the slowly rotating regime |a| ≪ M (Bussey–Cox–Kunduri), far from the near-extremal window, so the conjectured rate was genuinely untested.

## Definitions

- Initial data (Σ, γ, K) is the t = const Boyer–Lindquist slice of Kerr with mass M = 1 and spin a = 99/100: vacuum, axisymmetric, asymptotically flat with two ends, and maximal (tr K = 0 since the shift is N = N^φ∂_φ with ∂_φN^φ = 0).
- Σ = {r̂ = r̂₊} is the outer-horizon section, a closed axisymmetric MOTS (θ₊ = 0) with respect to the r̂ → ∞ end.
- Komar angular momentum J = aM = 0.99 ≠ 0; area A = 4πS₂ with S₂ = r₊² + a² = 2Mr₊; deficit δ = S₂/(2a) − 1 = A/(8π|J|) − 1.
- L(a) is the MOTS stability operator of Bussey–Cox–Kunduri formula (22); λ₁ denotes its Andersson–Mars–Simon principal eigenvalue (smallest-real-part eigenvalue, real; stable iff λ₁ ≥ 0).

## Result

The conjectured law is false. For the Kerr cell M = 1, a = 99/100, the horizon MOTS satisfies every hypothesis with

- A ∈ [28.67730, 28.67822],
- δ ∈ [0.1525932, 0.1525934] ⊂ (0, 1],
- 8δ ≤ 1.220747,
- λ₁ ≥ 0.0823037 (hence strictly stable),
- λ₁A ≥ 2.360250 > 1.220747 ≥ 8δ.

Thus λ₁A/(8δ) ≥ 1.93, i.e. λ₁A/δ ≥ 15.4 versus the claimed ≤ 8. The constant C = 8 linear vanishing law fails, and indeed any constant C < ~15.4 fails at this deficit.

## Proof and evidence

The operator L(a) commutes with rotations R_α: ψ(θ,φ) ↦ ψ(θ,φ+α). By Andersson–Mars–Simon/Krein–Rutman theory the principal eigenvalue λ_p is real and simple with a strictly positive eigenfunction φ > 0; rotation invariance plus simplicity forces R_αφ = φ, so φ is axisymmetric and λ_p equals the ground energy of the self-adjoint axisymmetric Sturm–Liouville reduction H = L̃(a) = −d/dz[((1−z²)/R)d/dz] + V(R) on L²(dz), z = cosθ, R = r₊² + a²z², with potential V(R) = c₀ + c₃/R³ + c₂/R² + c₁/R as stated in the draft. Hence any lower bound on the ground energy of H bounds the full λ₁; no mode-by-mode comparison is needed.

The lower bound is a rigorous Temple certificate with trial function u(z) = 89 + 33z²:

1. Gap point ν ≤ λ₂(H): since R ∈ [r₊², S₂] and (1−z²)/R ≥ (1−z²)/S₂, H bounded below in form by −(1/S₂)d/dz[(1−z²)d/dz] + Vmin; dV/dR has numerator N(R) < 0 on all of [r₊², S₂] (verified on 64 exact interval panels), so V decreases in R and Vmin = V(S₂) ∈ [−0.3145592, −0.3145582]; Legendre eigenvalues give λ₂(H) ≥ 2/S₂ + Vmin ≥ 0.5618132 =: ν.
2. Rayleigh quotient μ = ⟨u,Hu⟩/⟨u,u⟩ ∈ [0.0852044, 0.0852166] < ν, with all integrals reduced to J_k = ∫R^{−k} (k ≤ 6) via J₁ = 2atan(a/r)/(ar) and the recursion J_{k+1} = 1/(kr₊²S₂ᵏ) + ((2k−1)/(2kr₊²))J_k.
3. Residual ⟨Hu − μu, Hu − μu⟩ ≤ 27.9156651, σ² ≤ 0.0013825.
4. Temple: λ₁ ≥ μ − σ²/(ν − μ) ≥ 0.0852044 − 0.0013825/0.4765967 ≥ 0.0823037 > 0.

All interval endpoints are exact rationals (Python Fractions); the only transcendental steps are √199 (enclosed by squaring), π ∈ [3.1415, 3.1416], and atan via alternating Taylor series with rigorous remainder. The script asserts every inequality and prints ALL CHECKS PASSED. Independent audit cross-checks confirm consistency: direct quadrature gives μ ≈ 0.08521 and residual norm ≈ 24.2 inside certified intervals, the J-recursion matches quadrature to ~5×10⁻¹⁰, and a Neumann finite-difference discretization gives ground energy ≈ 0.0847 inside the certified [0.0823, 0.0853] window.

## Limitations

This disproves the stated constant C = 8 (indeed any C below ~15.4 at this deficit); it does not rule out a vanishing law with a larger constant or a different power such as √δ. The certificate covers one Kerr cell (M = 1, a = 0.99); the worsening numerical trend toward extremality (Richardson-converged ratios λ₁A/(8δ) ≈ 1.37, 1.62, 1.99, 2.19 at a = 0.90, 0.95, 0.99, 0.999) is supporting evidence only. Maximality and the symmetry/simplicity lemma cite standard results (BCK operator formula; AMS/Krein–Rutman).

## Reproducibility

Run `python3 output/artifacts/verify_counterexample.py` (stdlib only, exact rational-interval arithmetic). Expected output ends with `CERTIFIED: lam1*A > 2.3603 > 1.2207 >= 8*delta` and `ALL CHECKS PASSED`.

## References

- Bussey–Cox–Kunduri, Eigenvalues of the MOTS stability operator for slowly rotating Kerr, arXiv:2010.01682 (operator (22), reduction (26)).
- Andersson–Mars–Simon, Stability of MOTS and existence of MOT tubes, Adv. Theor. Math. Phys. 12 (2008) (principal eigenvalue real, simple, positive eigenfunction).
- Dain–Reiris, Area–angular-momentum inequality; Reiris, extreme Kerr throats (base inequality and rigidity context; no eigenvalue rate).
