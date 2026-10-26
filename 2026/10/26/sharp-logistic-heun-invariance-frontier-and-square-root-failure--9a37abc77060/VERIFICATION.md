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

Run `python3 verify.py` using the packaged standalone source. The observed result on the packaged files is `VERIFY_OK 2071` with `critical_r=4.40366947504161`, `tangency_x=0.47847351489411`, and `width_coefficient=0.49704877376326`.

The checker uses exact fractions for 2,071 algebraic/finite-grid assertions, including the cubic discriminant identity, Heun predictor normalization, carrying-capacity factorization and finite rational test cases. Floating-point checks verify the critical double root and trends for the near-critical interval widths. It uses Python's standard library only.

The universal statements are proved analytically in `RESULT.md`; finite tests cannot establish global quantifiers or asymptotics. Limits: no interval-arithmetic certificate is supplied, and no independent external audit has been performed.
