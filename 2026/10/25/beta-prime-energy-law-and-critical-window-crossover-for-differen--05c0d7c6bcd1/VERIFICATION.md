---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed the exact monomial weights w_m(gamma) by beta integration and the matrix coefficient (n+1)/(n+k+1) from the integral kernel. Gamma ratio asymptotics give the uniform row summand Gamma(alpha+4+epsilon)Gamma(-alpha)n^(-1-epsilon)+O(n^(-2-epsilon)). Summing n up to N with epsilon=lambda/logN yields logN*Phi(lambda)+O(1), uniformly for bounded signed lambda. The truncated column k>N tail is O(1) because alpha<0; this handles the noncompact half of the compression. The two-dimensional limiting measure is obtained by k/n Riemann sums of x^(alpha+1)/(1+x)^2 and logarithmic n-sums; small/large x and near-end t tails control extension to all bounded continuous tests. The same row estimate summed to infinity with epsilon>0 gives 1/epsilon+O(1). Independent finite alpha=-1/2 computations at N=90,240,600 are consistent with an O(1) cutoff correction but cannot prove any limit.

## originality

PASS

Best-of-knowledge originality for the joint logarithmic index-ratio distribution and the signed compact critical-window O(1) crossover. Li–Zhou provide boundedness/compactness/Schatten membership and the exact matrix coefficients used here; that prior work is not novel. Their accessible abstract gives no finite-section signed crossover or joint beta-prime law. Full Li–Zhou source unavailable in this run; this is explicitly a nonzero priority risk, not proof of coverage or grounds alone for an O FAIL.

## value

PASS

The natural compactness/Schatten threshold creates a mathematically motivated signed 1/logN critical window. The theorem gives an exact crossover constant and a two-scale beta-prime energy distribution rather than re-testing known boundedness; it separates weak entrywise energy from singular values and identifies an explicit limiting probability profile after normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
