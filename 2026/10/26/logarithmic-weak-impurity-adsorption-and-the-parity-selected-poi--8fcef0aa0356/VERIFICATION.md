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

# Reproducibility checks

The self-contained \`verify.py\` uses Python 3 standard-library modules and requires no third-party package. Run \`python verify.py\` from the directory containing the file.

Completed checks: 24 exact rational comparisons between a reduced \((k,A)\) rate recursion and an independent labeled-edge recursion, 30 exact identities/support assertions for the two-impurity even-size product, and 18 finite-size normalization and numerical-consistency assertions against the limiting law. All 72 grouped assertions passed. Numeric comparisons use \(n=10000\) or \(10001\) with two, three, and four fixed impurity sites; they are intentionally consistency tests only.

The mathematical proof relies on the conditional exponential holding moments, the \(O(K_n^{-1})\) exposure-mesh estimate, independent exponential hazard thresholds, the harmonic bound on intermediate impurity captures, and the exact \(k=1\) selection rule. These steps are written in RESULT.md. Finite calculations cannot independently validate the asymptotic theorem, the historical originality assessment, or model extensions not claimed there.
