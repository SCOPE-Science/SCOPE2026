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

# Verification of the discrete-theta spectrum law

The exact orbit count is obtained from explicit simultaneous spectral projections and an upper-unitriangular stabilizer. Its field-independence requires only idempotency and commutation, not a characteristic restriction. The equality of the leading quadratic exponent and the deficit rate is proved by a Cauchy--Schwarz upper bound and a balanced diagonal-word lower bound. The discrete-theta limit uses a pointwise Stirling asymptotic plus a summable fixed-parameter majorant; it is a total-variation statement.

The standalone `CHECK.py` performs direct finite-field arithmetic and matrix multiplication. The run `python3 CHECK.py` from the package directory yielded `ALL_COMMUTING_IDEMPOTENT_CHECKS_PASSED 12 57836`, where 57,836 is the total number of tested ordered tuples of idempotent matrices before filtering for commutation, over twelve configurations. It exhaustively compared the predicted number at every joint diagonal-character word and the multiplicity by generated-algebra dimension. The fields checked were \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), for dimensions up to four and tuple lengths up to three.

Finite enumeration does not establish the limit as the dimension tends to infinity. No computation is used in place of the asymptotic proof. The original scalar-root-potent enumeration is credited as prior art; this verification does not certify historical priority.
