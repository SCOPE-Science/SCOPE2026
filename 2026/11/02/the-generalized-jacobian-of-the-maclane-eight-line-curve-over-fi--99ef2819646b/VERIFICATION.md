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

The exact standalone check is `python3 verify.py`; no optional libraries are needed. Replayed in the completed directory, the verifier returned `VERIFY_OK`, with 8 zero and 48 norm-three triple determinants, 8 triple points, 4 double points, 32 normalization branches, rank 13 for the incidence-cycle lattice, and an integral basis determinant of +1. The two Frobenius branch-orbit counts are independently reconstructed from the incidence labels. Direct projective enumeration in the five prime fields of sizes 2, 5, 7, 11, and 13 gives respectively 6, 12, 44, 24, and 92 points, agreeing with the formulas.

The algebraic deductions not established solely by the script are: the local normalization-unit calculation giving one additive dimension at each triple point, the standard normalization exact sequence for the connected Picard group, and splitting of its finite abelian rational-point group into coprime p-primary and prime-to-p factors. These are proved in `RESULT.md`. The theorem excludes characteristic three, where the degree-eight equation is nonreduced. No independent audit or external formal certification has been performed.
