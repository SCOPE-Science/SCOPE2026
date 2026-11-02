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
# Verification record

The finite exact-arithmetic tests are implemented in `checker.py` and use the homogeneous-coefficient Rhaly matrix. Running `python checker.py` completed successfully and printed `CHECK_OK finite rational Jordan assertions: 16`.

The tested collisions were \(q=1/2\), \(q=2/3\), and \(q=3/4\), in dimensions \(d=2,3\). At each collision the computed dimensions of the first and second generalized kernels match the theoretical geometric and algebraic multiplicities. A separate triple repeated eigenvalue in dimension two gave kernel dimensions \(5,8,9,9\) for the first four powers, consistent with blocks of sizes \(3,2,2,1,1\).

All summability, spectral inclusion, trace-determinant, and infinite-dimensional root-space claims rely on the analytic proof in `RESULT.md`. Finite tests verify representative matrix identities only. The entire singular spectrum, zero root space and general complex-parameter resonances are not exhaustively numerically tested.
