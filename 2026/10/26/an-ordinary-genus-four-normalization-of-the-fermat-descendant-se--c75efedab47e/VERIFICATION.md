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
# Reproducible verification

Run `python verify.py` using a standard Python interpreter. The program implements the prime-field arithmetic and explicit degree-two and degree-three irreducible extensions in characteristic three, enumerates all projective points of the indicated sextic and Hesse cubic, and counts all points of the elliptic Weierstrass model. For each nonzero parameter in \(\mathbb F_3\), it checks the genus-four Weil-trace identity across \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\) and checks the number of rational singular points. It asserts ordinarity of both elliptic factors over the prime field via traces not divisible by three.

Expected terminal marker: `VERIFY_OK`.

The check does not certify geometric integrality, genus, nonzero arbitrary-field parameters, the Kummer-cover idempotent decomposition, or arbitrarily high extension degrees; these follow from the proof in RESULT.md. Computations are exact finite checks, not a substitute for those proofs. No independent audit was performed.
