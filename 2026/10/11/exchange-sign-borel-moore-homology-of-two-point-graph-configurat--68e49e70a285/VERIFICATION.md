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

# Reproducibility checks
The file `verify.py` is self-contained Python 3. Run `python3 verify.py`. The executed script returned `EXACT_CELLULAR_CASES 109`, `BOUNDARY_SQUARE_ZERO_AND_Q_F2_HOMOLOGY_OK`, and `VERIFY_OK`. For each chosen finite connected graph, the verifier constructs cellular boundaries on the quotient of the square after diagonal subdivision and checks both choices of the exchange character. It verifies zero composite boundary and rational/mod-two ranks.

The general integral calculation does not follow from finite enumeration: its proof is the equivariant relative-pair reduction to a rose and the transfer identifications. Integral torsion is excluded in the sign case by the explicit zero differential over integers in that rose model, not by rational ranks. The untwisted coefficient model has degree-two boundaries twice degree-one generators, consistent with the source theorem. No independent audit has been performed.
