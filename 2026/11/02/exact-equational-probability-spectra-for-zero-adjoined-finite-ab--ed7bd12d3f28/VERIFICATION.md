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

The accompanying scripts use only the Python standard library and exact rational arithmetic. Run `python verify_general.py` and `python verify_elementary.py` to regenerate their respective output files. The first enumerates all assignments for 25,269 pairs of short semigroup words in seven finite abelian groups, comparing direct evaluation against a Bézout-image formula. The second independently enumerates 8,428 equation cases for elementary abelian group extensions and tests numerous rational values of the analytic bound. The recorded outputs finish in `VERIFY_OK`.

The correctness of the universal spectrum, all admissible parameter attainments, topological derived sets, minimum equality conditions, and the \(C_4\) versus \(C_2^2\) separation rests on the symbolic argument in `RESULT.md`. The finite checks cannot certify statements over all word lengths or groups; no independent validation or external certification has occurred.
