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

The theorem is proved symbolically in `RESULT.md`; no finite census is used to establish the quantified statement.

The critical finite-space mechanism is the following. If an open motion-planning domain contains two distinct maximal pairs, then after choosing the coordinate in which they differ and slicing at any base point, the domain contains a two-top suspension. A local path section makes the slice inclusion null-homotopic. The explicit retraction from the full join onto that two-top suspension would therefore contract the suspension, contradicting the known noncontractibility of the two-top suspension of a noncontractible base.

`artifacts/verify.py` checks the purely order-theoretic part of this mechanism on three representative noncontractible bases and upper-antichain sizes \(2,3,4\). It verifies the \(n^2\) maximal-pair count, every collapse-to-two-tops retraction, and a nontrivial Stong core for each sampled two-top suspension. Replay with `python3 artifacts/verify.py` must reproduce `artifacts/verify_output.txt` and end with `VERIFY_OK`.

These finite checks are consistency tests only. They do not prove the general noncontractibility statement or replace the symbolic argument and cited two-point suspension theorem.
