# Virial–gradient lock and quadratic gap: no-go evidence for the Q⁺-push Glassey route near Q (radial 3D cubic NLS)

## Context

The Kenig–Merle / Holmer–Roudenko / Duyckaerts–Roudenko / Nakanishi–Schlag / Miller program asks which radial H¹ data for the focusing 3D cubic NLS scatter versus blow up, in particular strictly above the mass–energy threshold. Below threshold (ME < M_Q E_Q) Holmer–Roudenko prove a sharp G < 1 (scatter) versus G > 1 (blowup) dichotomy. At threshold (ME = 1) Duyckaerts–Roudenko exhibit e^{it}Q, Q⁺, Q⁻ and classify dynamics. Slightly above threshold Nakanishi–Schlag prove nine nonempty regions (blowup / scatter to 0 / scatter to ground-state family) via an implicitly located center-stable manifold; Miller gives non-constructive Kato/variance criteria for above-threshold scatter and blowup. No prior work names an explicit above-threshold datum with G < 1 and V' ≥ 0 that blows up in finite time, nor the virial numbers of such a datum.

The admitted target and preset fallback both required a single-datum certificate on u_* = (1+a_*)Q⁺(−T_*): ME > 1, G < 1 in the hard 1−G ≪ 1 regime, V'_{R_*}(0) ≥ 0, V''_{R_*}(0) ≤ −μ_* < 0, and a finite Glassey bound T_b. Executing that plan's Step 3 on the single ansatz returned an empty (ε,a) scan, leading to the finding below. The target and fallback are therefore **not claimed**; obstruction evidence is reported instead.

## Definitions

- Equation: i u_t + Δu + |u|²u = 0 on R³, radial.
- Mass M = ∫|u|², kinetic K = ‖∇u‖², P₄ = ‖u‖₄⁴, energy E = K/2 − P₄/4.
- Scale-invariant gradient G(u) = √(M(u)K(u))/√(M_Q K_Q); mass–energy product ME(u) = M(u)E(u).
- Full virial second derivative V''(u) = 8K − 6P₄. Q is the radial ground state ΔQ − Q + Q³ = 0 with Pohozaev identities K_Q = 3M_Q, P_Q = 4M_Q, hence V''(Q) = 0.
- F = 1 − MK/(M_Q K_Q), so {G = 1} = {F = 0} for positive data.
- Y = p + iq: Duyckaerts–Roudenko radial unstable mode ((−L₋L₊)p = e₀²p); Z = P₂ + iQ₂ its Lyapunov–Perron second-order correction ((2e₀I − JL)(P₂,Q₂) = −N₂(Y)).
- Model surface u(a,ε) = (1+a)(Q + εY + ε²Z) (true heteroclinic to second order, plus amplitude lift).
- Exact Holmer–Roudenko localized virial V''_R with standard C⁴ cutoff ζ (analytic piecewise-polynomial derivatives in verifier); R_* = 2.45 is the least R with exterior Q-mass ≤ |P₀|/16.

## Result

**Lemma 1 (proved, exact).** At u = Q, for every real direction v,
dV''[v] = −(4/M_Q)·d(MK)[v], equivalently dV'' = 4K_Q·dF.
Hence {G = 1} and {V'' = 0} are tangent at Q in every direction; to first order G < 1 ⟺ V'' < 0 is infeasible near Q.

**Theorem 2 (numerically-indicated local emptiness, no interval proof).** On u(a,ε), the zero-curves a_G(ε) (G = 1) and a_V(ε) (V'' = 0) satisfy a_G = g₁ε + g₂ε² + O(ε³), a_V = v₁ε + v₂ε² + O(ε³) with g₁ = v₁ ≈ 0.2671 (agree at two step sizes to ~10⁻⁴ relative), g₂ ≈ 1.203, v₂ ≈ 2.171, gap v₂ − g₂ ≈ +0.968 > 0 (0.96800 and 0.96787 at two step sizes; direct zero-crossing gap/ε² → +1.1…1.4 under refinement, same sign), and exact Q_{F,aa} = −12 recovered to 7 decimals. Hence a_V − a_G = +0.968·ε² + O(ε³) > 0 is numerically indicated: V'' reaches zero strictly after G exceeds 1. Gap sign plus an empty 36-point (ε,a) grid give numerically-indicated local emptiness of {ME > M_QE_Q, G < 1, V'' < 0} near Q on this surface.

**Proposition 3 (replayed computation).** Symplectic unstable projection λ₊ satisfies dλ₊/dε = 1, dλ₊/da ≈ −1.738, so reaching the blowup side (λ₊ = 0) from the Q⁺ branch needs lift slope k_c ≈ 0.575 > g₁ ≈ 0.267: the lift required to cross sides breaks G < 1 first.

**Proposition 4 (replayed computation).** At the rule radius, V''_{R_*}(0) ≈ +5.558 versus full V''(0) ≈ +5.530 (truncation error O(10⁻²), no sign leverage); R → ∞ recovers 8K − 6P to 2% (0.6% in verifier). No truncated-virial rescue.

**Consequence.** The snapshot-plus-lift truncated-Glassey blowup route is numerically indicated not to close near Q. Any {G < 1, V' ≥ 0} finite-time blowup datum above threshold (if one exists) is pushed by this evidence to lie O(1) away from Q or to blow up by a non-Glassey mechanism — that stronger global statement is not proved.

## Proof / evidence

**Lemma 1 proof.** V'' = 8K − 6P₄ gives dV''[v] = 16⟨∇Q,∇v⟩ − 24⟨Q³,v⟩. d(MK)[v] = 2K_Q⟨Q,v⟩ + 2M_Q⟨∇Q,∇v⟩. The weak form of ΔQ − Q + Q³ = 0 (L₋Q = 0) gives ⟨∇Q,∇v⟩ + ⟨Q,v⟩ = ⟨Q³,v⟩. Substituting and using K_Q = 3M_Q, P_Q = 4M_Q yields both sides equal to −8⟨Q³,v⟩ − 16⟨Q,v⟩. ∎ (Discrete lock ratios match K_Q to 1–5×10⁻⁴ at two scales; independent rerun confirms.)

**Theorem 2 / Props 3–4 evidence (computation, not proof).** `output/artifacts/verify.py` (stdlib + numpy only) rebuilds Q (Petviashvili), spectrum (e₀), unstable pair, second-order correction, lock ratios, corrected ½-weighted normal form, Prop-3 projection, Prop-4 localized virial, and grid scan. Independent audit rerun: **VERIFY_OK, 23/23 PASS** (~1–3 min; dense 1400² eigensolve). Headline numbers: M_Q ≈ 18.8907, K_Q ≈ 56.6896, E_Q ≈ 9.4497, e₀ ≈ 5.503 (main-run spectral.json: 5.50225), λ₁(L₊) ≈ −15.298, L₋ ground ≈ 0 (phase null), R_* = 2.45, V' orientation ≥ 0 on ε > 0 branch (V'(0) ≈ +0.88–0.96 at ε = 0.02). Numerical hygiene logged: two symmetrization/ordering bugs fixed (W^{1/2}LW^{−1/2} similarity; M₁ = −L₋L₊ order); Pohozaev defect 1.6–3.1×10⁻⁴ (R = 25 → 40, N = 1400 → 5600 stable); QFaa = −12 cross-check; nonlinearity coefficient −(2(p−1)/(p+1)) = −1 for p = 3 verified by R → ∞ limit (an earlier −2 gave spurious −440); second-order ½-factors corrected (g₂ ≈ 1.203, v₂ ≈ 2.171, gap ≈ +0.968, band 0.9–1.4).

## Limitations

- Gap coefficient +0.968 is a finite-difference value at fixed discretization, not an interval proof; Theorem 2 claims numerically-indicated local emptiness only, with no proved neighborhood-emptiness radius.
- Lemma 1 is exact in the exact-Q limit; discrete match is Pohozaev-scale (1–5×10⁻⁴).
- Obstruction is local (near Q on snapshot-plus-lift surface) plus a rule-radius computation; far-from-Q {G < 1} blowup data and non-virial mechanisms remain explicitly open.
- u(a,ε) is a second-order heteroclinic model, not the exact Q⁺ flow snapshot; background Q⁺/manifold theory used for framing only.

## Reproducibility

Run `python3 output/artifacts/verify.py` (requires Python 3 + numpy; loads `output/artifacts/Q_profile.npz` coarse seed, rebuilds everything, dumps `output/artifacts/consolidated_numbers.json`). Expect 23/23 PASS and VERIFY_OK. All headline numbers are in `consolidated_numbers.json`.

## References

- Holmer–Roudenko, sharp scattering for radial 3D cubic NLS (ME < 1 dichotomy). https://arxiv.org/abs/math/0703235
- Duyckaerts–Roudenko, threshold solutions at ME = 1 (Q⁺, Q⁻). https://arxiv.org/abs/0806.1752
- Nakanishi–Schlag, global dynamics above ground-state energy (nine regions, implicit manifold). https://arxiv.org/abs/1007.4025
- Miller, scattering and blowup above ground state (non-constructive criteria). https://arxiv.org/abs/2412.06962
- Holmer–Platte–Roudenko, blowup criteria (Gaussian V_t < 0 data). https://arxiv.org/abs/0911.3955
