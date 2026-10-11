---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The singleton Möbius faces give the exact 1/t tail. Because rho_12=0, the (1,2) face is an independent two-Pareto convolution and contributes exactly 2 w_1 w_2 log(t)/t^2+O(t^-2). For each strictly negative Gaussian pair, simultaneous lower-tail extremes have exponent 2/(1+rho)>2; after separating the fixed-width boundary strips, conditional Gaussian tails give an integrable dominated-convergence bound on the cooperative core, so the whole pair face is O(t^-2). On the trivariate lower corner, R is a Stieltjes matrix, hence R^{-1} is entrywise nonnegative with diagonal at least one; for nonnegative Gaussian quantiles the copula density is therefore bounded, and the three-face reciprocal integral is O(t^-2). If one p-value is outside that corner, its reciprocal score is bounded and the triple increment is supported in fixed-width singleton/pair shells, also O(t^-2). Summing the faces yields the claimed expansion. Direct tail inversion gives the stated quantile shift and size correction. A fresh sanity check verified positive definiteness/inverse positivity for a representative mixed matrix and the coefficient subtraction; the infinite asymptotic proof is analytic.

## originality

PASS

Liu's full primary paper explicitly states Open Problem A.12 for one-sided nonpositive Gaussian dependence and says that a uniform theorem covering mixed zero and negative correlations remains to be written. The audited theorem solves the minimal genuinely mixed reciprocal case by proving the missing negative-edge and three-face remainder controls and identifies the surviving critical logarithm. Current Resultary and web searches found no earlier theorem with this exact mixed Gaussian coefficient. This is a direct positive open-problem comparison, not novelty inferred from search failure.

## value

PASS

The theorem resolves a specifically identified open dependence regime at the smallest dimension where zero and strict-negative Gaussian edges coexist, and quantifies exactly how much logarithmic second-order inflation disappears relative to independence. This is a motivated calibration boundary result rather than a generic asymptotic exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
