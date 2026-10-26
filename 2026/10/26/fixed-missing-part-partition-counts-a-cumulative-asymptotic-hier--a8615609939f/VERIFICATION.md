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

The standalone `verify.py` recomputes the exact finite bivariate product through \(n=120\), \(0\le m\le4\), and independently enumerates all partitions through \(n=16\). The program returns `VERIFY_OK` when the finite identities agree. The infinite asymptotic is proved analytically using the exact source generating function, an explicit Riemann-sum constant, a complex-sector estimate, and Ingham’s cumulative theorem. Finite computation does not prove asymptotics or priority.
