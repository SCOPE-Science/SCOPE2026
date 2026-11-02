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

## Reproduction

Run `python3 verify_sparse_fair.py` with Python 3.9+ and no external dependencies. From the embedded script, the complete domain of normalized one-or-two-approver approval-type multisets with 3 agents and degree up to 4, and 4 agents and degree up to 3 was checked. The script prints the exact nine bin counts and `VERIFY_OK`; 362 profiles of incidence multiplicities were verified, together with 18 tiny direct complete-allocation enumerations. It also verifies graph-edge orientation utility and EF1 constraints for all exact-two-approval families in that census, a complete \(K_4\) example, and the two-agent boundary.

## Logical verification

The proof's non-computational obligations are the generalized Hall criterion for matching identical copies of each agent, the rank-two incidence count, existence of a nonapprover per leftover good when \(n\ge3\), the EF1 inequality, the double-counting identity \(m=nd/2\) in regular two-approval graphs, and Euler orientation after auxiliary pairing of odd vertices. Each step appears in RESULT.md. The enumeration is finite evidence, **not** an infinite proof. The exact common utility and Pareto claims depend on these arguments, and no external or independent audit has been performed.
