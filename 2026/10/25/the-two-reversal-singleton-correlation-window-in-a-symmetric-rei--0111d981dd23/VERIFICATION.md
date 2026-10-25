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

Run `python3 verify.py` from this directory with standard Python 3. The checker uses exact `fractions.Fraction` arithmetic and enumerates 373,343 equiprobable weak compositions across 116 integer parameter pairs. It compares the enumerated single- and double-singleton frequencies against the proposed formulas and checks the covariance factor and its sign. An additional 997 exact polynomial parameter checks test the finite sign-regime boundary, and numerical asymptotic diagnostics examine four large sample-size scales. It reports `OK (116, 373343)` on success.

The finite checks do **not** prove the universal root classification or the limiting constants; those are proved in RESULT.md using counting, polynomial sign analysis, asymptotic expansion, and root bracketing. The checker requires no external data or libraries. Historical originality is not experimentally certifiable; relevant prior literature and unresolved access are described separately in REVIEW.md.
