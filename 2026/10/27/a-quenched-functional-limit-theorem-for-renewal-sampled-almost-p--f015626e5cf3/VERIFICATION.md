---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For positive iid increments, P(S_h≤m)≤e^{am}(E e^{-aψ})^h, with E e^{-aψ}<1. This gives absolute variance summability, an integrable covariance-tail envelope, and almost surely a conditional index dependence range O(log n) by a union bound and Borel–Cantelli. At each frequency in the countably many trigonometric approximations needed, the bounded character martingale differences give the pathwise Bohr mean. For fixed h, splitting the h-step covariance innovations into residue classes modulo h+1 gives the martingale strong law for the difference from the conditional mean g_h(Y_k). Lag-continuity ensures g_h is Bohr almost periodic and the norm-continuous integral commutes with its mean. Truncating lags, prefix Cesàro convergence is uniform after division by n; omitting the last h terms of each prefix is O(H²/n) for a fixed truncation H. The ergodic collision envelope controls all longer lags simultaneously for the prefixes. Consequently conditional variances converge uniformly on the Brownian time scale to tσ², including σ²=0. Blocks of size floor(n^(1/3)) separated by O(log n) gaps are jointly independent by the setwise m-dependence assumption. Residue-class maximal inequalities make the deleted prefix sums negligible in L² after normalization. The fourth moment bound summed over normalized full blocks is O(n^(-2/3) log² n). Assign block sums to completion times: the maximal discrepancy within a block is deterministically bounded by 2K floor(n^(1/3))/sqrt(n), so the full-block conditional variance profile follows uniformly by the L² triangle inequality. The independent-array functional CLT therefore applies in J1 and uniform-probability approximation restores the original process. The separate Brownian-sign example has σ²=3−4/π at ε=0 and independent integration gives σ²≈1.8569314 at ε=1/2; these are checks of the variance formula, not the limit. The frozen script was inspected, not executed. The frozen verification metadata does not attest expert, independent, or Lean verification.

## originality

PASS

The supported distinction is the almost-sure, whole-schedule conditional J1 theorem for bounded m-dependent processes with almost-periodic lag covariances. The same variance and overlapping scalar annealed limit are prior work, not credited as new. No inspected result establishes the stronger conditional functional statement or implies it on these hypotheses.

## value

PASS

Inference or pathwise limit analysis with one realized observation schedule needs a conditional path law, not averaging over new schedules. The result handles arbitrarily close clusters without a minimum gap or a renewal moment and requires regularity only of lag covariances, not all marginal laws. The pathwise variance and clustering arguments together close a meaningful gap between the known annealed scalar result and such usage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
