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

# Reproducibility

Run `python verify.py` in any standard Python 3 environment. The file uses rational-valued arithmetic for two separately assembled linear-system solutions, compares these to the closed formulas, checks positivity, conservation, asymptotic coefficients and a sample weighted-error threshold. The program prints its own assertion count and a representative pair of flux coefficients. No third-party packages, network access or external files are required.

The checked exact formula for the stage transfer is \(\delta=hav/[1+h(a+c(u+v))]\). For the output, form the averaged forward/backward reaction fluxes, solve the exact two-by-two system, and check the closed difference in the proof. The tests are finite; the universal asymptotics and nonexistence of a representation-uniform error calibration are proved algebraically in `RESULT.md`, not inferred from test counts.

Independent audit: not performed.
