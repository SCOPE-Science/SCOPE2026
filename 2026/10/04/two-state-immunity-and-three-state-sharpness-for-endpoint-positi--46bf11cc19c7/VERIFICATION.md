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
The analytic verification consists of two exact reductions. In two states, \(Q=-s(I-\Pi)\) with \(\Pi^2=\Pi\), so two midpoint half-steps give \(R_h(Q)=\Pi+r^2(I-\Pi)\), where \(r=(1-hs/4)/(1+hs/4)\). This yields an explicitly nonnegative stochastic matrix for every \(h\ge0\). In the three-state pure-birth witness, direct triangular inversion gives the exact endpoint matrix displayed in `RESULT.md`; its unique sign-changing entry is \(16h(4-h)/(h+4)^3\).

`verify.py` uses exact rational arithmetic to reconstruct the midpoint solves directly, compare them with the closed forms, verify unit row sums, and test the sign transition at \(h=4\). Running `python3 verify.py` returns `VERIFY_OK`.

The finite replay is corroborative. It is not used to infer the all-parameter theorem. No claim is made about floating-point positivity, intermediate-stage positivity, time-dependent generators, or methods other than the stated SSP-SDIRK2(2) scheme.
