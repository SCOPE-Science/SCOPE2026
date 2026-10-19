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

The analytic proof is in `RESULT.md`; `verify.py` independently evaluates algebraic, integral and numerical identities. Run it with Python 3 and `mpmath` (tested with version 1.3.0): `python verify.py`.

The code checks 616 exact rational fractional-map compositions, compares the chi-square integral to an erfc expression at six allocation ratios, verifies the differentiated scalar expression, tests gamma dimension ordering and uniqueness-bracketing signs for several dimensions, and integrates nine exact noncentral Gaussian two-step risks. All 704 checks passed. Numeric checks are finite and are not the proof of any universal statement.

The scalar optimizer is determined by a unique positive root of an explicit complementary-error-function equation. The value printed by the verifier is \(0.6048675421548876022483401965\ldots\), with normalized mean-square ratio \(0.6804153100377522917794446514\ldots\). The relationship to prior work and acknowledged material-reading limitations are recorded in `REVIEW.md` and `AUDIT.json`.
