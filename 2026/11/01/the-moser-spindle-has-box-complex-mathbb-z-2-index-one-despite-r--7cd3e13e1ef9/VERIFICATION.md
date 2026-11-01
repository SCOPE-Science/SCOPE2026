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

# Verification steps and limits

Run `python3 verify_moser_box.py` in the same directory as the embedded files. The program is self-contained (Python 3 standard library) and reconstructs the finite certificate from the eleven stated graph edges. It verifies every closed set and face, all eight involution-orbit collapse pairs at their actual stages, residual and quotient graph ranks, the free action, and three- versus four-colorability. Successful output is `MOSER_BOX_INDEX_VERIFY_OK`.

The logical step from a connected free equivariant graph model to index one, and the published equivalence of the standard box and Lovász complexes, are proved/referenced in RESULT.md. No numerical extrapolation, independent verification or priority certification is asserted.
