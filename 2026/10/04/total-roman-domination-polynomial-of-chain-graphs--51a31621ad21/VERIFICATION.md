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
The proof is symbolic and applies to every finite connected chain graph in the stated canonical form. The critical checks are:

1. Boundary support: for every Roman dominating function, the positive induced subgraph is isolate-free exactly when both extreme twin classes \(A_p\) and \(B_1\) contain a positive label.
2. Label permissions: once the largest \(A\)-index carrying label \(2\) and smallest \(B\)-index carrying label \(2\) are fixed, the nested neighborhoods determine exactly which twin classes may contain label \(0\) and label \(2\).
3. Case partition: no label \(2\), label \(2\) only on \(A\), label \(2\) only on \(B\), and label \(2\) on both sides are disjoint and exhaustive.
4. Minimum: the four cases have minima \(N\), \(|A|+2\), \(|B|+2\), and \(4\), respectively, and explicit functions attain each bound.

The accompanying `verify.py` independently constructs adjacency and enumerates every labeling for all positive canonical twin-class profiles of total order at most \(9\). It directly checks the Roman condition, the isolate-free positive-support condition, the boundary criterion, every coefficient of the formula, and the minimum-weight corollary.

Replay output:

`VERIFY_OK profiles=255 labelings=3023307 valid_functions=1117507 criterion_checks=3023307 coefficient_checks=3347 gamma_checks=255 max_order=9`

Finite enumeration is corroborative only and is not used to infer the infinite theorem.
