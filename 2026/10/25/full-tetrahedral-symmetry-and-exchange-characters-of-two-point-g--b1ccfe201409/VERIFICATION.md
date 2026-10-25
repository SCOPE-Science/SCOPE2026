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

# Reproducible scientific verification

Run `python3 verify.py` with Python 3 and only the standard library. The script builds the twelve-vertex eighteen-edge graph directly from ordered distinct labels. It reconstructs the complete ordered two-particle cubical model and verifies the signed boundary, the 214-pivot modular rank bound, twenty independent exact integer product-cycle boundaries, all forty-eight signed symmetry operations on the kernel, and both irreducible character decompositions. The resulting actual stdout appears in `verification_output.txt` and ends with `VERIFY_OK`.

The verification of rational rank is a two-sided proof using independent integer cycles, not an inference from a sole modular test. Exact characters are lifted from residues using the trace bound of dimension twenty for a finite-order integral action. The graph-configuration deformation-retraction theorem and ordinary finite-dimensional rational representation theory are used as stated in `RESULT.md`; the program does not re-prove those general theorems. No independent audit has been performed.
