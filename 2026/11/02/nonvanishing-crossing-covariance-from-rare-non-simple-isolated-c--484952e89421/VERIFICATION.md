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

# Exact verification and boundaries

Run `python verify.py` with a standard Python 3 interpreter. The script enumerates all \(146{,}598\) perfect matchings for \(2\le n\le7\), directly counts crossing pairs and isolated chords of each admissible short-arc gap, and compares exact rational means and covariances against the closed formulas. It also checks binomial versus double-factorial normalization and the first positive-gap formulas for every \(4\le n\le150\). The completed independent enumeration passed **6,194 exact assertions**.

This finite exhaustive check does not establish the theorem for every \(n\). The infinite part is justified by the partition into independent arc matchings, exact indicator-covariance summation, and the ratio estimate for \(r_{m,s}\). The full positive-gap tail contribution is \(O(n^{-1})\) in covariance, and the \(s=1\) stratum determines the limit \(-1/3\).

The result assumes a uniform fixed-size perfect matching. It does not claim an independence law, nonlinear conditional independence, or identical behavior for nonuniform chord weights. No independent audit or formal certification was performed.
