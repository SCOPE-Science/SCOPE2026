# Independent Audit — 2026/09/20/bb-interval-objective-monotonicity-frontier--7866f4762b53

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `693e01d1706bca627b45425a9a426a8122dc9701`
- Disposition: **PASSED**

## Correctness

**PASS** — The worst-case bound and sharpness are correct. Both BB endpoints lie in [1/L,1/mu], so every interval selector does. In an eigenbasis, F_{k+1}/F_k is bounded by max_{lambda in [mu,L]}|1-eta lambda|^2; over eta in [1/L,1/mu] the largest possible magnitude is kappa-1, giving the uniform (kappa-1)^2 bound. For A=diag(1,kappa) and g_0=(1,sqrt(r)), the exact-line-search warm-up gives the displayed BB1/BB2 endpoints, both converging to 1 as r->0. Substitution independently reproduces the endpoint formulas and the selector-uniform limit (kappa-1)^2. Numerical checks at kappa=1.5,2,3,10 confirm the transition and sharp limit. Thus kappa<=2 is exactly the universal objective-monotonicity frontier for the whole contemporaneous BB interval.

## Originality

**PASS** — Classical BB literature establishes the two steplengths, nonmonotonicity, and global/R-linear convergence; recent 2026 work sharpens asymptotic rates and nonlinear dynamics. Targeted searches for the exact one-step factor (kappa-1)^2, a kappa=2 universal descent frontier, and a uniform obstruction for every selector between BB2 and BB1 found no covering statement. The upper bound is elementary once the interval containment is observed, so the novelty claim is intentionally limited to the sharp interval-class frontier and its exact-line-search sharpness construction.

## Scientific value

**PASS** — The theorem cleanly separates convergence from descent and gives an exact condition-number phase transition for an entire family of spectral-gradient choices, including convex blends. The uniform two-dimensional obstruction shows that adaptive selection inside the BB interval cannot restore a worst-case descent guarantee beyond kappa=2, which is a useful design limitation even though it does not improve asymptotic complexity.

## Sources

- **Two-Point Step Size Gradient Methods** — Jonathan Barzilai; Jonathan M. Borwein. https://doi.org/10.1093/imanum/8.1.141 — Original BB steplength source.
- **A family of spectral gradient methods for optimization** — Y.-H. Dai; Y. Huang; X.-W. Liu. https://doi.org/10.1007/s10589-019-00107-8 — Prior convex-combination/spectral-gradient family lying between the BB endpoints.
- **On a Faster R-Linear Convergence Rate of the Barzilai-Borwein Method** — Dawei Li; Ruoyu Sun. https://arxiv.org/abs/2101.00205 — Prior strongly-convex quadratic convergence-rate theorem, distinct from one-step objective monotonicity.

## Limitations

- Finite-dimensional real SPD quadratics and exact arithmetic only.
- The theorem concerns objective-gap monotonicity for selectors inside the contemporaneous BB2-BB1 interval; globalization or out-of-interval rules are outside scope.
- The bound is a worst-case one-step statement and does not imply typical trajectories are nonmonotone when kappa>2.

## Independent checks

```json
{
  "rayleigh_interval_bound_checked": true,
  "sharpness_formulas_rederived": true,
  "selector_uniform_limit_checked": true,
  "numeric_kappa_values": [
    1.5,
    2,
    3,
    10
  ],
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence. The assigned source tree was unchanged between the inventory commit and source-tree-check commit. Open-access/preprint sources were checked before any institutional retrieval attempt. No inaccessible text is claimed as read.
