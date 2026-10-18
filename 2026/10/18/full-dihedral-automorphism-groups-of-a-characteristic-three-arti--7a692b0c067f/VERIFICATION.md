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

The included `verify.py` uses exact symbolic arithmetic and finite permutation groups to check:

- \(H_{U^m-V^m}=-m^2(m-1)^2(UV)^{m-2}\) and its coefficient nonzero modulo \(3\);
- \(\lambda/(x^{-m}-1)=-\lambda-\lambda/(x^m-1)\), which validates the lift \(S\);
- group relations and the exact \(6m\) group size for \(m=5,8,11,14\);
- the genus arithmetic \(2g-2=-6+4m\).

Execution produces `VERIFY_OK` after checking these cases. The theorem for *all* permitted \(m\) depends on the rigorous uniqueness-of-pencil and binary-Hessian arguments in RESULT.md; no finite enumeration proves the infinite case. There is no independent mathematical audit.
