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
Run `python verify.py` with Python 3 and the standard library. The program constructs the dual-number arithmetic for \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), independently enumerates all matrices and idempotent–nilpotent pairs, then checks both ordered multiplication maps against the eight-stratum theorem. It also checks the overall number of idempotents, nilpotents, product pairs, and positive-fiber targets.

Completed results: \(q=2\): \(256\) matrices, \(1664\) pairs, \(112\) positive targets. \(q=3\): \(6561\) matrices, \(80190\) pairs, \(1377\) positive targets. \(q=4\): \(65536\) matrices, \(1318912\) pairs, \(7936\) positive targets. Both factor orders matched every predicted fiber, and the checker terminated with `VERIFY_OK`.

These exact finite computations support the theorem but are not a substitute for the general rank-one projection counting proof. No independent audit is represented here.
