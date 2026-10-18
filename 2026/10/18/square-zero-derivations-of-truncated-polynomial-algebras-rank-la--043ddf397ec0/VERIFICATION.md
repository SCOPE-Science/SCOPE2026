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
# Verification

The accompanying `verify_derivation_rank.py` independently generates every allowable coefficient vector \(f=D(t)\) and constructs the matrix \(D_f\). Its test for \(D_f^2=0\) is literal field-matrix multiplication; ranks come from independent finite-field elimination rather than the valuation formulas. All coefficients for \(27\) exhaustive cases over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) matched; totals and the characteristic-two maximal-rank and even/odd pairing checks also matched. The program ends with `ALL_EXACT_CHECKS_PASSED 27 exhaustive field/length cases`.

Reproduction: `python verify_derivation_rank.py` with standard Python 3. No external libraries or datasets. Beyond finite dimensions tested, validity rests on the written proof; the computation cannot rule out mistakes at larger truncation lengths or establish novelty. Geometric decomposition means the reduced point locus only. Independent audit is not performed.
