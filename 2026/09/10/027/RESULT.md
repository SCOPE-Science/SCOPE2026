# Envelope-closure threshold correction for the H^1 Koranyi spectral-transfer route

## Context

The Heisenberg–Falconer program asks for dimensional thresholds guaranteeing
that the Koranyi distance set of a compact set in the first Heisenberg group
has positive Lebesgue measure. Admission qualified a fallback headline at the
natural homogeneous-dimension boundary `dim_K > 3` (`Q = 4`, `Q - 1 = 3`) via
Koranyi spherical group-Fourier decay plus Heisenberg averaging.
Prior work (Raani–Singh arXiv:2507.14917) proves only a positive-upper-density
large-distance regime plus `R_k` decay; it states no compact threshold and
explicitly leaves the energy-integral analogue as future work.

## Definitions

- `H^1 = C x R`, `(z,t).(w,s) = (z+w, t+s+1/2 Im(z \bar w))`,
  `delta_r(z,t) = (r z, r^2 t)`.
- Koranyi norm `|(z,t)|_K = (|z|^4+t^2)^{1/4}`, `d_K(x,y) = |y^{-1}.x|_K`.
- Homogeneous dimension `Q = 4`; Koranyi–Hausdorff dimension `dim_K`.
- Unit Koranyi sphere `S_K(0,1)`, normalized surface measure `sigma`,
  group Fourier `hat sigma(lambda) = sum_k R_k(lambda,sigma) P_k(lambda)`,
  spectral parameter `mu = 2(2k+1)` at `n = 1`.
- Cited input envelope (Raani–Singh Lemma 1.4, not re-proved here):
  `|R_k(lambda r^2, sigma)| <= C0 min(1, (|lambda| r^2 mu)^{-1/4})` (E),
  with `t := |lambda| mu`, `beta = 1/4`.
- Radial Mattila kernel on `0 <= r <= R0` (fixed, e.g. 2):
  `M(t) := int_0^{R0} r^6 min(1,(t r^2)^{-1/2}) dr`.
- Riesz weight exponent `alpha = 4 - s'`.

## Result

**Envelope-closure lemma (conditional on (E)).**
`M(t) <= C1 t^{-alpha}` uniformly in `t > 0` holds iff `alpha <= 1/2`,
i.e. iff `s' >= 7/2 = Q - 2 beta` (for the feasible range `s'` in `[0,4]`).
In particular the admitted `dim_K > 3` boundary (`alpha = 1`) does NOT close:
`M(t)/t^{-1}` diverges as `~t^{1/2}`. Hence neither the pinned target nor the
unpinned fallback at `dim_K > 3` closes on this `beta = 1/4` spectral-transfer
bookkeeping; its natural closure is `7/2`. Reusable criterion: a future decay
input with exponent `beta` closes at `s > Q - 2 beta`, so reaching `s > 3`
needs `beta > 1/2`.

## Proof / evidence

Analytic proof. Put `rs = t^{-1/2}` (crossover where `(t r^2)^{-1/2} = 1`).
If `rs >= R0` (`t <= R0^{-2}`): `M(t) = R0^7/7`, constant.
If `rs < R0`: since `r^6 (t r^2)^{-1/2} = t^{-1/2} r^5`,
`M(t) = rs^7/7 + t^{-1/2}(R0^6 - rs^6)/6 = t^{-7/2}/7 + t^{-1/2}(R0^6 - t^{-3})/6`.
Hence `M(t) = (R0^6/6) t^{-1/2} - t^{-7/2}/42` as `t -> infinity`, and
`M(t) -> R0^7/7` as `t -> 0`. The comparison ratio `M(t)/t^{-alpha}`
behaves as `const x t^{alpha-1/2}` at large `t`, bounded iff `alpha <= 1/2`
(for `alpha` in `[0,4]`; the endpoint `alpha = 0` gives bounded `M`).
The `iff` is independent of `C0, C1, R0`. The `r^6` weight and
squared-envelope reduction are part of the admitted route bookkeeping.

Supporting numeric consistency (not the proof of (E)):
`output/artifacts/threshold_closure.py` scans the exact closed form over
20002 log-spaced `t` in `[1e-6, 1e8]`: `alpha = 0.5` sup ratio `10.6667`
bounded; `alpha = 0.8` sup `2679.3` growing `~tmax^{0.3}`;
`alpha = 1.0` sup `106666.7` growing `~tmax^{1/2}`.
`output/artifacts/check_Rk_decay.py` evaluates `R_k` from the Raani–Singh
formula at `n = 1`: `R_k(0) = 1`, low-frequency `R ~ 1`, high-frequency worst
`|R|/rho^{-1/4} = 0.970`, consistent with (E).

## Limitations

- (E) is cited from Raani–Singh Lemma 1.4, only numerically
  consistency-checked, not re-proved (no van der Corput uniformity in `k`
  re-established here).
- No positive-Lebesgue-measure theorem is proved at `dim_K > 3` or at the
  corrected `7/2`; the full Frostman-energy argument (trace/Sobolev
  `dmu`-vs-`dx` loss, pinned uniformity) remains open.
- The `iff` concerns this radial `L^2`/Mattila envelope bookkeeping; a
  different (non-spectral-transfer) method could in principle reach `s > 3`.

## Reproducibility

Deterministic stdlib + mpmath, seconds-scale:

    python3 output/artifacts/threshold_closure.py
    python3 output/artifacts/check_Rk_decay.py

Auditor replayed both exactly and cross-checked `M(t)` by independent
Simpson quadrature.

## References

- K. S. S. Raani, R. K. Singh, Distances in sets of positive Koranyi upper
  density in Heisenberg Group, arXiv:2507.14917.
- B. Liu, Group actions, the Mattila integral and applications,
  Proc. Amer. Math. Soc. (2018), doi:10.1090/proc/14406 (Euclidean only).
- Du–Ou–Ren–Zhang, arXiv:2309.04103; Liu GAFA 2019; Eswarathasan–Iosevich–
  Taylor Adv. Math. 2011; Balogh–Fassler–Mattila–Tyson projection theory
  (per Admission triage; Euclidean/projection/density regimes only).
