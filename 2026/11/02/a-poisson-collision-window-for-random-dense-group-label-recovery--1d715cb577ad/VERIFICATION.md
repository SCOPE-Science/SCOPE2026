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

# Reproducibility and evidence

Run `python3 checker.py` using a standard Python 3 installation. The expected deterministic output is recorded in `checks.txt`. The program uses `fractions.Fraction`, independent brute-force enumeration of short sample sequences, exact first and second collision moments, and seeded Monte Carlo comparisons at fixed fractions. The exact tests verify identities for several finite choices of \(n,k,t\), including \(\Pr(Q_{\mathrm I}\le3\mid n=4,k=2)=8/9\) and \(\Pr(Q_{\mathrm I}\le4\mid n=5,k=2)=96/125\).

The program reports 39 explicitly counted check assertions and prints diagnostic numerical comparisons for three fractions and three sizes. The scientific theorem is **not** inferred solely from these finite tests; the infinite Poisson law uses the graph-indexed factorial-moment bound, and the expectation estimate uses the exact collision variance displayed in RESULT.md. No independent or external proof certification is asserted.
