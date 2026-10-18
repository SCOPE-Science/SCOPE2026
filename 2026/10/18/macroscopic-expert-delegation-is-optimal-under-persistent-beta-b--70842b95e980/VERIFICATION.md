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

# Reproducibility and limits

Execute `python verify.py` with a standard Python 3 installation. No third-party package or external data is needed. The test uses exact rational arithmetic for positive integer beta shapes and checks the derivation of the one-delegation difference against two complete beta-binomial tail sums. It also tests the entire optimum set in the \(\mathrm{Beta}(3,2)\), \(q=7/10\) case through \(k=29\), and the independent novice comparison using \(p=3/5\).

Expected outcome: `Exact rational assertions passed: 418`, followed by selected exact-rational success-probability evaluations printed as decimals for convenience. The test does not derive an analytical uniqueness result from enumeration or certify asymptotic behavior by finite sampling. Those claims are established separately by the symbolic pivotal-event identity, the strict product monotonicity, and the harmonic-sum limit in the result document.

The source model and priority comparisons are documented in the result and scientific review. One later relevant research paper was available in abstract only; publication-priority assessment remains subject to independent literature verification.
