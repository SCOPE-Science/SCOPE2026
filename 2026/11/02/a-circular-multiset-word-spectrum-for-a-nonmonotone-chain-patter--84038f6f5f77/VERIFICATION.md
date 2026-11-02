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

# Reproduction

Run `python3 verification/cyclic_patterns_check.py` using the standard Python library. The program independently counts cyclic pattern occurrences by direct word enumeration for six content vectors and both patterns, computes marked coefficients of the claimed rooted-cycle formula by exact rational dynamic programming, and checks overlap relation consistency for chains with up to six marked occurrences. Expected final line: `VERIFY_OK cyclic_exact_graphic_marked_formula total_direct_words 447720 induced_overlap_orders_r_to_6 126`.

The verifier is finite and cannot certify all lengths. Universal correctness rests on the explicit overlap-chain decomposition, total-order property, exclusion of closed marked chains and the formal cycle-counting identity. An independent scientific review has not been conducted.
