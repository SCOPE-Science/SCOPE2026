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

# Verification and limits

The proof derives the all-parameter result through exact sheaf sequences on the K3 and the exceptional rational curve. The standalone script `verify_rao.py` recomputes the \((-2)\)-curve cohomology recurrence for \(m=1,\ldots,64\), verifies every integer twist \(-3\le t\le2m\), checks the exceptional canonical endpoint and spin parity, and prints `VERIFY_OK` on success.

The computational check does **not** certify the underlying algebro-geometric exact sequences, the existence of the K3 surface or curve, nor historical priority; those premises are documented in the proof and primary references. The calculation is not extended to \(t>2m\). Independent mathematical audit has not been performed.
