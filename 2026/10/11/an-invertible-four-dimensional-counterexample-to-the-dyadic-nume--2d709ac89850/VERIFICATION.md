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

Run `python3 verify.py` with standard Python 3. No dependencies beyond the standard library are required.

The script reproduces rational bounds for \(\varepsilon=1/10000\), checks exact matrix multiplication and the fourth-power binomial expansion of \(S+\varepsilon I_4\), and verifies the elementary inequality \(5>(11/5)^2\). These checks are deterministic. The analytic proof separately establishes that the dyadic *infinite* series is bounded by a geometric tail and that the numerical radius is bounded below by a normalized path-sine eigenvector. A computer-checked finite list is not asserted to prove the infinite-series comparison without those analytic estimates.

The result is same-model reviewed only; no independent external audit or machine-checked formal certificate is claimed.
