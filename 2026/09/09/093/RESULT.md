# Uniform castle-residual bound for one Joseph allosteric lamplighter cell

## Context

Kerr's dynamical Toms–Winter programme asks whether almost finiteness,
dynamical comparison, and finite tower dimension coincide for amenable-group
actions. Joseph (arXiv:2301.07616) gave the first minimal, topologically free,
mean-dimension-zero actions of amenable groups with dynamical comparison that
are not almost finite, via allostery (topologically free but not essentially
free). The failure was qualitative: some stabilizer set has positive measure,
so almost finiteness fails (Lemma 2.2), but no uniform castle-residual number
and no named-pair stabilizer-mass constant were published. Gardella et al.
(arXiv:2405.04343) proved qualitative Z-stability for these actions with no
number; Hirshberg–Wu (arXiv:2308.12504) bound nuclear dimension from above via
long-thin covers, not a residual lower bound.

## Definitions

- `G0 = (Z/2) wr Z = (direct-sum_Z C2) ⋊ Z`, lamplighter; `a = (δ_0,0)` lamp
  at 0, `t = (0,1)` cursor shift; `G0 = ⟨a,t | a^2=e, lamp conjugates commute⟩`.
- Named involution `g1 := a ≠ e` (base lamp at cursor 0, order 2).
- Window `S0 = {e, t, t^{-1}, t^2, t^{-2}, a}`, symmetric, generating,
  containing `g1^{±1}`.
- Subgroup `S = {e, g1}` (Joseph §4 subgroup, order 2); hence
  `{S ≤ Stab} = Fix(g1)`.
- Chain: enumerate `G0∖{e}` by weight `w=|δ|+|supp|+diam` (fixed before
  computation); `ε_i = 2^{-(i+3)}` (sum `1/8`, tail `≥7` = `1/512`);
  `N_i = p_i^{k_i}` distinct odd prime powers, `p=(3,5,7,11,13,17,…)`,
  `k_i` minimal with `N_i ≥ max(ℓ_i/ε_i, 2·diam_i+2, |δ_i|+1)`,
  `ℓ_i = |supp(g_i)|+1`; `Λ_i = N_i·Z`; `E_i ⊂ Z/N_iZ`, `|E_i|=ℓ_i`,
  covering `supp(g_i)` residues; `A_i = {f : Σ_{x∈q} f(x)=0 mod 2 ∀q∈E_i}`;
  `Γ_i = A_i ⋊ Λ_i`; `H_n = ∩_{i≤n} Γ_i = A^{(n)} ⋊ L_n·Z`,
  `L_n = ∏_{i≤n} N_i`.
- `X0 = lim←_n G0/H_n` (profinite Cantor limit),
  `μ0` = inverse limit of uniform measures.
- An `(S0,1/8)`-castle is a family of towers `{(V_j,S_j)}` with clopen bases,
  pairwise-disjoint levels `sV_j`, and `|S0·S_j ∖ S_j| < |S_j|/8`.
  Its union is `U`, residual `R = X0 ∖ U` (clopen).

## Result

For this fixed cell `W0 = (G0,X0,μ0)` with the above `S0`, `g1`:

1. `μ0(Fix(g1)) = ∏_{i≥1} (N_i − ℓ_i)/N_i ≥ ∏(1−ε_i) ≥ 1 − Σ ε_i = 7/8`
   (hence `≥ 1/8`).
2. Every `(S0,1/8)`-castle covers at most `1/4` of `X0` in `μ0`-measure
   (hence at most `3/4`); its residual satisfies
   `μ0(R) ≥ μ0(Fix(g1)) − 1/8 ≥ 7/8 − 1/8 = 3/4 ≥ 1/4`,
   and upper Banach density of `R` equals `μ0(R)`.

Finite data: `N = (27,125,343,1331,2197,4913)` for `i=1..6`,
`P6 = 8921337686592/9476449507525 ≈ 0.9414`,
global lower bound `P6·(511/512) ≈ 0.9396 ≥ 7/8`.
Sample box `B = {(f,k) : supp f ⊆ [−24,24], k ∈ [−24,24]}`,
`|B| = 49·2^49`, right-boundary `6·2^49`, ratio `6/49 < 1/8`;
`S = B^{−1}` is left-`(S0,1/8)`-Følner.

## Proof / evidence

- Non-membership `γ_i ∉ Γ_i`: cursor/mixed via `N_i > |δ_i|`
  (`δ_i ∉ N_i·Z`); lamp via a covered singleton residue carrying value 1
  (parity 1); `N_i > diam_i` separates residues. Distinctness and covering of
  residues replayed in `verify.py`.
- Transitive finite levels give minimality + unique ergodicity
  (Joseph Lemma 3.1, chain case) and comparison (Joseph Lemma 2.4);
  identity thread has trivial stabilizer, spread by minimality to a dense
  `G_δ`, giving topological freeness.
- Fixed-point ratio: conjugate of `g1` by `(f,k)` is the lamp at `−k`;
  membership in `A^{(n)}` depends only on cursor class `k mod L_n`;
  fibre size `M_n` cancels. CRT over coprime odd `N_i` gives good-class
  count `∏(N_i−ℓ_i)`, so `r_n = ∏_{i≤n}(N_i−ℓ_i)/N_i ≥ ∏(1−ε_i)`.
  Decreasing clopen preimages with measures `r_n` intersect to `Fix(g1)`;
  continuity from above gives the infinite product; Weierstrass
  `∏(1−ε_i) ≥ 1−Σε_i = 7/8`.
- Tower blocking (quantitative Joseph Lemma 2.2, one-sided): if
  `x = sv ∈ Fix(g1) ∩ S_jV_j` then `g1·sV_j ∩ sV_j ≠ ∅`, so
  `s ∈ S_j ∩ g1^{−1}S_j`; with `g1^{−1}=g1`,
  `Fix(g1) ∩ S_jV_j ⊆ ⊔_{s∈S_j∖g1S_j} sV_j`, hence
  `μ0(Fix(g1) ∩ S_jV_j) ≤ |S_j∖g1S_j|·μ0(V_j) ≤ μ0(S_jV_j)/8`
  since `g1 ∈ S0` and `|S_j∖g1S_j| = |g1S_j∖S_j| ≤ |S0S_j∖S_j| < |S_j|/8`.
  Summing towers: `μ0(Fix(g1) ∩ U) ≤ μ0(U)/8`, residual inequality follows.
  `R` clopen ⇒ upper Banach density `= μ0(R)` by unique ergodicity.
- Sample castle: boundary counts `|Bt^{±1}∖B| = 2^49` each,
  `|Bt^{±2}∖B| = 2·2^49` each, `Ba = B`; ratio `6/49 < 1/8`;
  `S = B^{−1}` transfers by inversion (`S0` symmetric). Finite `S^{−1}S`
  meets `H_n` trivially eventually (`∩H_n = {e}`) with index `≥ 4|S|`,
  giving an existential disjointness level `n*`.

## Limitations

- Profinite data are one explicit chain cofinal in Joseph's directed family;
  the CRT product uses only coprime odd cursor moduli with fibre
  cancellation, not Joseph's coprime-base-fibre statement.
- Castle disjointness level `n*` is existential, not numerically evaluated;
  the uniform bound does not depend on it.
- Constants `7/8`, `3/4` are properties of this chain, not canonical
  invariants of all Joseph cells.
- Qualitative facts (minimality/unique ergodicity/comparison/topological
  freeness mechanism) cite Joseph Lemmas 3.1/2.4 and Thm 3.2.

## Reproducibility

`python3 output/artifacts/verify.py` → `VERIFY_OK` (stdlib only, exact
`Fraction` arithmetic; checks ε sums, prime-power moduli, per-type
non-membership data, ratios, `P6`/global `≥ 7/8`, residual arithmetic,
`6/49 < 1/8`).

## References

- M. Joseph, Amenable wreath products with non almost finite actions of mean
  dimension zero, arXiv:2301.07616.
- E. Gardella et al., Essential freeness, allostery and Z-stability of crossed
  products, arXiv:2405.04343.
- I. Hirshberg, J. Wu, Long thin covers and nuclear dimension,
  arXiv:2308.12504.
- C. Bönicke, K. Li, Nuclear dimension of subhomogeneous twisted groupoid
  C*-algebras and dynamic asymptotic dimension, arXiv:2309.17178.
- D. Kerr, G. Szabó, Almost finiteness and the small boundary property,
  arXiv:1807.04326.
