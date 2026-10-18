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

Run `python3 verify.py` using standard Python 3 from this directory; output must begin with `VERIFY_OK`. It checks the exact 1024 subsets of the ten proposed allowed parts and the independent integer polynomial coefficients, including the entire 137-integer interval from 65 through 201 and the seventeen indices of zero bias below 65. It separately derives coefficients of the signed partition generating series and the positive distinct-product series through degree 500. It also checks 494 initial instances of the overlap inequality.

# Proof-level scope

The infinite result is proved by the monotone symbolic inequality: for integer \(m\ge7\), the interval-overlap margin begins at \(39\) and grows by \(2m^2-4m-2>0\). Computation is used only for the finite base and supplementary identity checks. The proof does not establish an analogue for higher powers. There is no independent mathematical audit.
