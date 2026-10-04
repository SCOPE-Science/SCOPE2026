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
The theorem was checked in two ways. First, the proof was reconstructed from the transmission rule, including the one-use restriction on transmitting vertices, the exact characterization of size-\(N-2\) ordinary zero forcing sets, the two-step weight calculation, and the maximum-degree boundary. Second, `verify.py` performs an exact-rational exhaustive comparison between the dynamic process and the closed formula on a finite suite.

The finite suite contains all sorted three-part profiles with part sizes at most three and all sorted four-part profiles with part sizes at most two, excluding complete graphs, for \(lpha,eta\in\{1/4,1/2,3/4,1\}\). It additionally checks every omitted-part pair in three asymmetric profiles. The stored replay output is `ALL CHECKS PASSED; exact_fraction_cases=400; graph_profiles=13`.

The finite computation does not establish the infinite theorem. It is a regression and boundary check for the symbolic proof. No independent audit has been performed.
