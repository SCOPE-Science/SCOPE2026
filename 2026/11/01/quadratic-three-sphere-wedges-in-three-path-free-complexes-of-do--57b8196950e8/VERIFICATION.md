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

# Verification notes

From the included source package, run `python3 verify.py`. The checker constructs the graph edges from the four spine vertices plus both labeled leaf classes and independently characterizes faces as those avoiding every induced three-vertex path. It computes the full face sets, the deletion and link at the second spine vertex, all exact boundary ranks over the two-element field, and the reduced Euler characteristic. It tests all 16 parameter pairs with \(1\le a,c\le4\) and five larger asymmetric or symmetric pairs. It is expected to print `VERIFY_OK` on success.

The theoretical claim for all positive integer leaf counts is established in `RESULT.md` by star-complex homotopy pushouts, exact face decomposition of the vertex link, and nullhomotopy of the attaching map. Checking mod-two ranks cannot establish integral torsion-freeness, higher homotopy, or the result for untested parameters. No independent audit or external mathematical validation has been performed.
