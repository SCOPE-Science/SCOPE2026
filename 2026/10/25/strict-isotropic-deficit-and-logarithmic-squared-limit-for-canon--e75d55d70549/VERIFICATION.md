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

# Reproducibility and limits

Run `python3 verify.py` using only the Python standard library. Expected terminal line:

`VERIFY_OK exact_dirichlet_traces=60 strict_ratios=17 planar_area=2/3 planar_variance=23/432 tail_base=20`

All asserted finite comparisons use exact rational arithmetic. The checker verifies the alternative Dirichlet-coordinate formula for the covariance trace in dimensions \(1\) through \(60\). It checks all seventeen rational conditions for dimensions \(2\) through \(18\) needed to join the analytic tail. In dimension two, an independently specified polygon has exact area \(2/3\) and coordinate variance \(23/432\).

The tail proof starts from \(H_{20}^2+H_{20}^{(2)}-2>12\), \(e^3>20\), and the exact inequality \(H_6=49/20>12/5\). Its monotonicity comparison is analytical for all integers \(m\ge20\). No claim of all-dimensional formal or external certification is made. The code and proof check mathematical computations, not priority of publication; independent audit remains unperformed.
