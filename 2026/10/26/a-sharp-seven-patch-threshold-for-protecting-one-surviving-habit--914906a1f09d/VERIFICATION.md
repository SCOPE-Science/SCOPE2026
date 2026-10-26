---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Exact verification record

Run `python3 verify.py > reproduced.json` from the package directory and compare the output bytes with `certificate.json`. The checker uses the Python standard library only. Every Prüfer word of length \(n-2\) for each \(2\le n\le7\) is reconstructed as a labeled tree. Every independent set of each residual graph \(T-N[v]\) is counted exactly. All root comparisons are integer coefficient comparisons, with no floating-point optimization.

The output includes counts \(1,3,16,125,1296,16807\), coefficientwise exceptions \(0,0,0,0,0,840\), and the exceptional structure's polynomial coefficients. It independently enumerates the witness's \(64\) survival configurations for each of four rational survival probabilities and exactly verifies the analytical success difference.

**Limits.** Exhaustion concerns trees of orders at most seven. The unique crossover of the exceptional tree is proved symbolically from \(t(t^2-t-1)\), not from four evaluations. Historical mathematical precedence remains uncertain where relevant publisher full texts were inaccessible. No independent scientific audit has been performed.
