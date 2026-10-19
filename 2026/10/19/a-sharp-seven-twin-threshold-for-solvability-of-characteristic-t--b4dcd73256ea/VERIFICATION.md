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

# Reproducible exact checks

From the directory containing the package files, run `python3 check.py` and `python3 crosscheck.py` using Python 3. No third-party dependencies are required.

The first script generates all exact \(\mathbf F_2\) Lie structure constants for symmetric zero-row-sum matrices and successively computes commutator spans for sizes one through seven; it also verifies the seven-distinct-vertex four-cycle bracket formula. Its terminal status is `EXACT_LIE_SERIES_OK` and `SEVEN_VERTEX_COMMUTATOR_IDENTITY_OK`.

The second constructs actual binary matrices, computes each matrix commutator and independently reconstructs the derived series for sizes one through seven. Its terminal status is `INDEPENDENT_MATRIX_BRACKET_CHECK_OK` and `EXACT_LIE_SERIES_OK`.

The finite rank calculations certify the listed small cases over all characteristic-two fields, because their defining matrices have entries in the prime field and linear ranks are stable under field extensions. They do not prove the all-size statement unaided; the general argument uses a four-cycle bracket identity for seven arbitrary distinct indices.
