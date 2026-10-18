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

# Reproducible verification

Run `python3 verify.py` using Python 3 and the standard library. The program prints the exact compatible-pair totals for finite chain sizes \(2\le n\le12\) and finishes with `VERIFY_OK` when all assertions pass. It enumerates every ordered pair of endpoint-containing fixed-point subsets, computes four rounding maps, checks universal and existential commutation separately, verifies the equivalent gap criterion, and checks that the composites round to the common fixed-point subset. The counts are compared with the recurrence \(a_k=4a_{k-1}-2a_{k-2}\) for \(k=n-2\).

A separate direct-map search considers all pairs of unary maps on each chain of sizes \(n=2,3,4\) and retains precisely those satisfying the defining monadic Gödel equations (M1)--(M5) (with (M5) automatic in Gödel chains). It recovers exactly the endpoint-subchain rounding constructions (\(1,2,4\) survivors). The direct-map check does not assume the common-gap counting criterion.

The statements for all finite \(n\) follow from the mathematical proof, which uses the published monadic subalgebra representation, the fixed-point argument for commuting regressions, order reversal for upper roundings, and an ordinary generating-function decomposition. Neither finite execution nor a finite output log is a proof for unbounded \(n\). No external formal proof certification or independent audit is claimed.
