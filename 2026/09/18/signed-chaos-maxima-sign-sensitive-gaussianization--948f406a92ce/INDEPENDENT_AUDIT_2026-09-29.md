# Independent audit — Sharp sign-sensitive Gaussianization thresholds for equal-spectrum second-chaos maxima

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/signed-chaos-maxima-sign-sensitive-gaussianization--948f406a92ce`  
**Audited tree:** `7f1b47d0436f80dd5930880c1b24a93c7805e675`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The cumulant and moderate-deviation calculations check out. The positive flat spectrum is a standardized Gamma law with shape m/2; Bose–Dasgupta–Maulik's growing-shape Gamma theorem applies when log p=o(m), and expanding its centering gives the stated (4/3)(log p)^(3/2)/sqrt(m) Gumbel-scale shift. For the balanced spectrum the exact cumulant generating function is -(m/4)log(1-2t^2/m); independent Legendre expansion gives I_m(x)=x^2/2-x^4/(2m)+4x^6/(3m^2)+O(x^8/m^3), hence the 2(log p)^2/m shift. The displayed Kolmogorov profile is the exact distance between a Gumbel law and its translate.

## Originality

**PASS.** Cai–Hu establish a general effective-rank-driven Gaussian-chaos phase transition and a sufficient high-dimensional bound, while Bose–Dasgupta–Maulik supply the positive Gamma extreme-value input. Targeted searches did not locate the paired equal-r4 comparison showing different log-cubic versus log-quadratic sharp thresholds, nor the two explicit critical Kolmogorov profiles. The ingredients are classical, so the originality claim is confined to this paired sign-sensitive synthesis and sharp benchmark.

## Scientific Value

**PASS.** The record gives an explicit counterexample to treating fourth-order effective rank as a complete sharp phase coordinate: two spectra with identical r4 and fourth cumulant have thresholds separated by a logarithmic power. This is a useful calibration benchmark for recent high-dimensional chaos approximation work.

## Independent checks

- Re-expanded K_+(t) and K_0(t); recovered kappa_3(Q_m^+)=2sqrt(2)/sqrt(m), kappa_3(Q_m^0)=0 and kappa_4=12/m in both cases.
- Independently expanded the balanced Legendre transform through x^8 and obtained x^2/2-x^4/(2m)+4x^6/(3m^2)-5x^8/m^3+..., matching the record through the claimed order.
- At x^2~2 log p, converted the cubic and quartic rate corrections to Gumbel-scale shifts 4/3*(log p)^(3/2)/sqrt(m) and 2*(log p)^2/m.
- Verified analytically that sup_y |exp(-exp(-(y-delta)))-exp(-exp(-y))| equals the displayed D(delta).
- Checked Bose–Dasgupta–Maulik Theorem 2.1: its hypothesis alpha/log n -> infinity and normalization match alpha=m/2, n=p after standardizing the Gamma variables.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.20529 — Cai and Hu (2026), general signed Gaussian-chaos approximation and effective-rank phase transition; no exact paired flat-spectrum thresholds found.
- https://arxiv.org/abs/0803.3518 — Bose, Dasgupta and Maulik (2008), growing-shape Gamma triangular-array maxima; Theorem 2.1 covers the positive-spectrum regime log p=o(m).
- https://doi.org/10.1214/aoap/1043862420 — Anderson, Coles and Hüsler (1997), older triangular-array extreme-value methods underlying the Gamma argument.

## Limitations

- The sharp equivalences are only inside m/log p -> infinity and for independent coordinates with flat equal-magnitude spectra.
- The balanced tail step uses a standard analytic saddle-point/moderate-deviation estimate; this audit checked its expansion and regime but does not claim a new general theorem for arbitrary signed spectra.
- Older Cramér-series literature may contain equivalent ingredients; no exact fixed-r4 paired comparison was located.

## Repository identity

The assigned source-tree SHA `7f1b47d0436f80dd5930880c1b24a93c7805e675` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
