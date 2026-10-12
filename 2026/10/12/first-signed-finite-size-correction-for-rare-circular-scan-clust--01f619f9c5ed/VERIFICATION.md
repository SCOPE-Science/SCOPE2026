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

# Analytic and computational verification

The complete proof in RESULT.md derives the Gamma\((k-1,1)\) coefficient \(-(k-1)/k!\), the adjacent-window beta integral coefficient \(2/k!\), and hence the cluster-start correction \(-(k+1)/k!\). A bounded-dependence Chen–Stein estimate gives \(O(N^{-1}+N^{-2/(k-1)})\) error. The normalization concentration sandwich works because \(k\ge4\) permits \(1/(k-1)<a<1/2\).

Run `python verify_rare_scan.py` using Python 3 standard library. The script makes 145 exact rational checks across the first 29 admissible integers \(k\). The finite checks are supportive algebraic smoke tests, not a proof of the all-\(k\) or limiting statements. No independent scientific validation has been performed.
