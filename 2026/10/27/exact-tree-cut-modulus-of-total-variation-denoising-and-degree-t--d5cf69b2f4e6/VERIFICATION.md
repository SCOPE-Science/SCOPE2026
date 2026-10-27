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
# Verification and limits

Execute `python3 CHECKER.py` in a standard Python 3 environment. The test is deterministic and uses exact `fractions.Fraction` operations. It enumerates all labeled trees on two through six vertices (1,441 graphs), every possible fused-edge subset and all edge-cut step directions, independently computes their variation norms and compares with the claimed connected-subtree maximum. Additional star/path/comb checks use exact arithmetic. On the four-leaf star and the four-spine comb it constructs explicit pairs and verifies all KKT stationarity equations, dual bounds and signs exactly; it obtains respective sensitivity quotients `3/2` and `2`.

Exhaustive finite checks are not proofs of universal quantifiers. The analytic proof applies to all finite trees and all positive regularization parameters. The code does not verify originality, arbitrary weighted graphs, or independent scientific audit.
