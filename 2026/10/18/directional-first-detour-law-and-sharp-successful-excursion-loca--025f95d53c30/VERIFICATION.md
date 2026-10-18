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

Execute the accompanying script using a standard Python interpreter:

`python3 verify.py`

It checks exact first-hit counts by enumerating all permissible finite paths up to the next-shortest length, verifies coordinate labels independently, recomputes selected coefficients by exact rational Bessel-series/renewal algebra in dimensions up to 100, and tests the Gamma crossing calculation. Its expected final report is `PASS: 360 independent finite exact/comparison checks`.

The proof is in RESULT.md. In particular, neither finite enumeration nor truncated generating functions prove the infinite-dimensional or infinite-reset limits. Those require the geometric tail, nonnegative first-hit coefficients, dominated Bessel-integral asymptotics, and analytic Gamma-density crossing established there. The numerical large-d comparison is a finite diagnostic and does not certify asymptotic error constants.

The scientific literature comparison is reported in REVIEW.md and AUDIT.json. No independent scientific audit has been performed.
