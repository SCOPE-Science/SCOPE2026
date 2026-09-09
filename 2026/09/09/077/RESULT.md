# Exact transverse linear growth of the 5D Mahler product along the canonical unconditional ray, with falsification of the C=4 quadratic envelope

## Context

The Mahler conjecture asks whether the volume product `P(K) = vol(K) vol(K^circ)`
of a centrally symmetric convex body is minimized at the cube (value `4^n/n!`).
In the unconditional class this minimum is known qualitatively (Saint Raymond;
Meyer–Reisner: Hanner polytopes are the minimizers), and Kim–Zvavitch proved a
qualitative/linear stability version with unspecified dimensional constant.
The 3D conjecture was recently settled (Chen et al.), so dimensions 4–6 are the
first open cases. No prior source records an explicit transverse growth law,
exact directional Mahler ratios, or an explicit constant window in R^5 along a
named unconditional curve.

## Definitions

- Work in `R^5`. `P(K) = vol(K) vol(K^circ)` is the Mahler volume product.
- `C = [-1,1]^5`: `vol(C) = 32`, `vol(C^circ) = 2^5/5! = 4/15`,
  `P(C) = 128/15 = 4^5/5!`.
- Canonical unconditional curve (target-route family):
  `J_t = {x in R^5 : max_i |x_i| + t sum_j |x_j| <= 1}`, `t >= 0`.
  Hence `J_0 = C`; each `J_t` is an unconditional symmetric polytope.
  The fallback normalization `J_t^{fb} = (1+5t) J_t` is
  `{max + t·sum <= 1+5t}`; `P` and Banach–Mazur distance are
  scale-invariant, so all statements transfer verbatim.
- `R(t) = P(J_t)/P(C) = A(t) B(t)` with `A(t) = vol(J_t)/32`,
  `B(t) = vol(J_t^circ)/(4/15)`.

## Result

Let `t in [0, 1/4]` and `J_t` as above. Then:

1. **Exact volume formulas.** With `Q_t = J_t ∩ R_+^5`,
   `vol(J_t) = 32 vol(Q_t)` where
   `vol(Q_t) = (1/(120(1+5t)^5)) sum_{j=1}^5 (-1)^{5-j} C(5,j) j^5/(1+(5-j)t)`,
   so `A(0) = 1` and `A'(0) = -15`.
   The polar positive part is `R_t = J_t^circ ∩ R_+^5 = {y >= 0 : sum_i (y_i-t)_+ <= 1}`,
   whence `vol(J_t^circ) = 32 sum_{k=0}^5 C(5,k) t^{5-k}/k!`,
   i.e. `B(t) = 120t^5+600t^4+600t^3+200t^2+25t+1`, `B(0) = 1`, `B'(0) = 25`.
2. **Transverse linear-growth law.** `R(0) = 1` and `R'(0^+) = A'(0)+B'(0) = +10`.
   Numerically certified by the difference quotient `9 < dR < 11` at `h = 10^{-6}`
   (value `9.999965`), with components `A'(0) in (-16,-14)`, `B'(0) in (24,26)`.
3. **Exact rational values falsifying the C=4 envelope.**
   `R(1/1000) = 215378277437/213253198587 ≈ 1.00996505`,
   `R(1/100) = 24434731/22283226 ≈ 1.09655267`,
   `R(1/10) = 15403/9009 ≈ 1.70973471`,
   `R(1/4) = 4043/1890 ≈ 2.13915344`,
   each strictly above `1+4t^2` (excesses `0.00996`, `0.09615`, `0.66973`,
   `0.88915`). Hence the envelope `R(t) <= 1+4t^2` on `[0,1/4]` is FALSE, and
   since `R(t) = 1+10t+O(t^2)` from below, NO purely quadratic upper envelope
   `1+Ct^2` holds on any right neighbourhood of `0`.
4. **Non-Hanner certificate.** For every `t > 0`, `J_t` has exactly `3^5-1 = 242`
   nonzero vertices (the signed support-pattern points `±c 1_S`,
   `c = 1/(1+tm)`, `m = |S|`). The Hanner_5 vertex census from the recursion
   `V(l1-sum) = a+b`, `V(product) = a·b`, `V(H_1) = 2` is
   `{10,12,14,16,18,20,24,32}`; `242` is absent, so `J_t` is non-Hanner for all
   `t > 0`.
5. **Banach–Mazur vs. cube.** `d_BM(J_t,C) - 1 <= 5t`, proved by the sandwich
   `(1/(1+5t))C ⊂ J_t ⊂ C`. For `t > 0`, `d_BM(J_t,C) > 1` because `J_t` has 242
   vertices while any linear image of the 5-cube has 32 vertices and invertible
   linear maps preserve vertex count. Volume-ratio quantities
   `q(t) = A(t)^{-1/5}-1` (`0.002999`, `0.029903`, `0.292252`, `0.713367` at the
   four depths) are reported for reference only and are NOT claimed as
   Banach–Mazur lower bounds.

Consequence: the admitted preset-fallback upper envelope
`P(J_t) <= (128/15)(1+4t^2)` is falsified (scale-invariant transfer), so that
fallback route as stated is closed; the uniform target (`kappa >= 1/16` for all
unconditional `K`) is not proved here. What is proved is the directional
transverse linear-growth law with exact rational certificates along a certified
non-Hanner unconditional direction.

## Proof / evidence

- **Primal volume.** `Q_t = {x >= 0 : Mx <= 1}`, `M = I + t 11^T`.
  Slicing by `S = sum x` with `u = 1-tS` and capped-simplex
  inclusion–exclusion yields the stated rational sum; at `t = 0` it reduces to
  the simplex volume `1/120`, giving `A(0) = 1`. Exact differentiation:
  with `s_j = (-1)^{5-j}C(5,j)j^5/120`, `N(0) = sum s_j = 1`,
  `N'(0) = sum s_j(-(5-j)) = 10`, and `A = N(1+5t)^{-5}` gives
  `A'(0) = N'(0) - 25N(0) = -15`.
- **Polar volume.** By LP duality / support-function computation on the
  positive orthant, `R_t = {y >= 0 : sum(y_i-t)_+ <= 1}` (verified on 5000
  random points per depth against brute-force vertex support with zero
  threshold disagreements). Conditioning on `k = #{y_i > t}` gives the
  `k`-simplex volume `1/k!` times `t^{5-k}`, summed with `C(5,k)` choices;
  hence the polynomial for `B(t)` and `B'(0) = 25`. Therefore `R'(0) = 10`
  exactly; the `h = 10^{-6}` quotient is a numerical corollary.
- **Exact fractions.** Evaluated in exact `Fraction` arithmetic; all four match
  the recorded fractions and exceed `1+4t^2`. Independent 400k-sample Monte
  Carlo primal volumes agree to `< 0.001`, and midpoint Riemann grids agree to
  within `0.02` (primal) / `0.05` (polar).
- **Vertices.** Each signed pattern point `c·(σ on S)`, `c = 1/(1+tm)`,
  satisfies `f_t = 1` and is uniquely exposed by
  `l(x) = sum_{i in S} σ_i x_i`: for any vertex `w = d·(τ on T)`,
  `<c,w> <= a/(1+tb)` with `a = |S∩T|` aligned, and
  `m(1+tb) - a(1+tm) = (m-a) + t·m·(b-a) > 0` for `t > 0` unless
  `(T,τ) = (S,σ)`. Active-constraint counting on `Q_t` shows
  `Q_t = conv(0, {c 1_S})`, so `J_t = conv` of the 242 points and the count is
  exact. The Hanner census was recomputed independently from the recursion.
- **Banach–Mazur.** `max <= f_t <= (1+5t)max` gives the sandwich and the `5t`
  upper bound via the identity map; `d_BM = 1` iff linearly equivalent
  (standard) plus the 242-vs-32 count gives qualitative strict positivity.

## Limitations

- The uniform transverse bound `kappa >= 1/16` over the full unconditional
  neighbourhood is NOT proved (single `J_t` ray only).
- No quantitative Banach–Mazur lower bound `δ(J_t) >= t/4` (full-Hanner
  infimum) is claimed; only the proved `5t` upper bound and qualitative
  positivity.
- The preset fallback upper envelope as stated is FALSIFIED, so no
  PRESET_FALLBACK claim is made.
- The `O(t^2)` remainder has no closed global bound beyond the exact point
  values plus certified slope.

## Reproducibility

Stdlib-only Python: `artifacts/verify_envelope_correction.py`
(`ENVELOPE_CORRECTION_CERTIFICATE_OK`: E1 R(0)=1; E2 slope quotient in
(9,11); E3 four exact fractions with envelope violation; E4 242-vs-Hanner
census with axial/diagonal feasibility; E5 BM upper bound plus 242-vs-32
positivity) and `artifacts/verify_jt.py` (`VERIFY_OK` with Riemann-grid
cross-checks). Replays in seconds with no dependencies.

## References

- Kim–Zvavitch, Stability of the reverse Blaschke–Santalo inequality for
  unconditional convex bodies, arXiv:1302.5719 (qualitative/linear stability,
  unspecified c(n)).
- Fradelizi–Hubard–Meyer–Roldán-Pensado–Zvavitch, Equipartitions and Mahler
  volumes of symmetric convex bodies, arXiv:1904.10765 (3D).
- Kuperberg, From the Mahler conjecture to Gauss linking integrals,
  arXiv:math/0610904 (exponential-factor global bound).
- Chen–Li–Xi–Xu, The Mahler Conjecture in Three Dimensions,
  arXiv:2605.09334 (3D solution).
- Cuevas, A Discrete KKT Variational Characterization of the Local Minimality
  of the Mahler Volume in Centrally Symmetric Polytopes, arXiv:2606.14709
  (unspecified kappa modulo GL, per admission triage).
