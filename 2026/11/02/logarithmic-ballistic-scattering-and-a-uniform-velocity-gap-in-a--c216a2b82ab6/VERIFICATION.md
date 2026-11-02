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

# Verification record

The proof in `RESULT.md` supplies the infinite-time certificate: exact positive recurrence, summable rational gain, two-stage tail expansion, geometric strip-crossing lower bound, and invariant-measure recurrence. The standalone `verification.py` has been executed from this package's own source. Its three exact rational cases verify the normalized recurrence and sign invariance. Its five high-precision decimal runs (12000 iterates per case) verify consistency of estimated \(X\) and renormalized \(C\) at two and three observation depths, and check the velocity gap, including an initial displacement of magnitude \(10^{-12}\).

Reproduce using `python3 verification.py` under Python 3 with no external libraries. Finite precision diagnostics cannot certify the limits or invariant-measure statement; these are covered by the written proof. No independently authored mathematical validation has occurred.
