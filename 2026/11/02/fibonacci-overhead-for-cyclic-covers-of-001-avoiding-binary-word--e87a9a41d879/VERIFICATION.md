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

# Verification instructions

Run `python3 verify.py` using only the standard Python library. The script creates the required de Bruijn edge set for each integer order from three to eighteen, independently tallies vertex imbalances, constructs the canonical lexicographic source–sink augmentation, checks balance, runs an Euler tour and verifies that every required length-\(n\) word occurs as a cyclic window. It asserts the Fibonacci formula at each order and reports `VERIFY_OK` if all tests pass. It also enumerates all circular binary candidates below the asserted bound at orders three and four; these small brute-force tests are not a proof for arbitrary orders.

Expected rows for \(n=3,4,5,6,7,8,9,10\) have optimum lengths \(8,16,29,53,94,166,290,504\). Further rows cover orders eleven through eighteen. The proof for all orders is the imbalance/overlap argument in `RESULT.md`. Finite execution neither establishes priority nor independently certifies the infinite theorem.
