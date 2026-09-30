# Independent Audit — 2026/09/18/reciprocal-weight-periodic-paley-wiener-uniqueness--f2771af894de

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8b77cb8dd980a2dd3d9e02df7d06beea253496a3`
- Disposition: **PASSED**

## Correctness

**PASS** — The reciprocal-weight dichotomy follows from the periodic block geometry. Uniformly in t in [0,1], the fiber sum of W_L(t+k)^{-1} is comparable to 1+sum_j(2^{-j}+L(2^j))^{-1}. When this series converges, weighted Cauchy--Schwarz gives both Fourier L1 integrability and the L2 periodization estimate required in the Olevskii--Ulanovskii uniqueness construction; fiberwise absolute convergence then makes the auxiliary function continuous in the shift parameter, allowing dense shifts to force every Fourier coefficient to vanish. In the divergent case, the normalized exponential blocks R_j have disjoint translated frequency supports and weighted squared norm O(2^{-j}+L(2^j)); reciprocal-energy averaging therefore makes the interpolation correction arbitrarily small while preserving value one at the target point and finite prescribed zeros. The standard successive-correction argument then defeats every uniformly discrete set. For L(r)=log(e+r)^beta, the criterion reduces to the p-series sum j^{-beta}, yielding the exact beta>1 threshold.

## Originality

**PASS** — Olevskii--Ulanovskii prove the positive Sobolev result above alpha=1/2 for periodic gaps, and Bertolini--Florit-Simon--Liehr--Taylor prove that the power threshold is sharp for the full periodic spectrum at and below alpha=1/2. The audited theorem refines the critical endpoint by an arbitrary dyadically comparable slowly varying factor and identifies reciprocal-block summability as the exact criterion, with the logarithmic beta=1 transition. Searches for this reciprocal-weight or logarithmic endpoint theorem found no prior covering result.

## Scientific value

**PASS** — The theorem resolves a genuine second-order endpoint question left invisible by the power-scale dichotomy: logarithmic strengthening restores uniformly discrete uniqueness exactly above beta=1. More generally, the reciprocal-series criterion identifies the mechanism behind both directions and is flexible across dyadically regular critical weights. This is a substantive sharpening of the newest endpoint theorem rather than a cosmetic reformulation.

## Sources

- Universal completeness of exponentials (Susanna Bertolini; Enric Florit-Simon; Lukas Liehr; Mitchell A. Taylor): https://arxiv.org/abs/2609.20805 — Recent source proving sharpness of the alpha=1/2 Sobolev power threshold for periodic weak-gap spectra.
- Discrete Uniqueness Sets for Functions with Spectral Gaps (Alexander Olevskii; Alexander Ulanovskii): https://arxiv.org/abs/1609.04571 — Establishes uniformly discrete uniqueness under Sobolev regularity above the critical exponent for periodic gaps.

## Limitations

- The negative direction uses the full periodic spectrum A+Z and need not extend to arbitrary subsets with periodic gaps.
- Dyadic comparability of the weight is essential to the stated exact block criterion; irregular critical weights are not covered.
- The theorem is about uniqueness, not stable sampling or quantitative frame bounds, and is one-dimensional.

## Independent check

```json
{
  "implementation": "independent dyadic fiber-sum and block-energy reconstruction",
  "critical_log_series": "sum_j j^{-beta}",
  "threshold": "beta>1",
  "all_ok": true
}
```

The assignment snapshot and source-tree-check commit were compared read-only and no file under this record changed. The dated independent-audit files were verified absent and the current `VERIFICATION.md` blob guard was checked. Open-access/preprint sources were checked first; no decisive comparison required Oxford Download. GitHub was not modified.
