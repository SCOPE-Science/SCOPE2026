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

# Verification and reproducibility

Run `python checker.py` from this directory using Python 3. The checker was executed successfully with signal `CHORD_SUCCESSOR_MATCHING_EXACT_OK 11445 39`.

The test enumerates all perfect matchings on \(8\), \(10\) and \(12\) cyclically ordered points: respectively \(105\), \(945\) and \(10{,}395\), totalling \(11{,}445\). It checks \(33\) exact joint falling-factorial moment identities for three short chord lengths by direct enumeration and independent compatible-chord prescriptions. It checks \(6\) exact expectation identities for two specified coloured four-edge cycle types. Every comparison uses integer or exact rational arithmetic, not tolerance-based floating point comparisons.

These finite checks test enumerative premises only. They do not constitute a proof of the joint Poisson limits, the effective first-order logical reduction or the density theorem. Those conclusions follow from the proof in RESULT.md, including an explicitly invoked standard bounded-degree locality theorem. No independent external audit was performed.
