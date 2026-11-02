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

The standalone `verify.py` uses Python 3 standard-library code. It reconstructs all binary input-pair/carry transitions, performs an exhaustive breadth-first traversal of all reachable determinized automaton configurations together with the modulo-three and bit-position tracker, and verifies that the ten-state table is closed under both input symbols. It asserts the equivalence between nondeterministic acceptance and divisibility by three at every reachable state, establishing an infinite-language identity rather than extrapolating finite tests. A second, independent direct enumeration checks all integers \(0\le n<16384\), confirms each multiple of three has a two-summand representation, and confirms none of the remaining integers does.

Run `python3 verify.py` from the package directory. Expected terminal line: `VERIFY_OK`. This is an arithmetic and finite-state check, not an independent scientific audit. The proof covers arbitrary nonnegative integers, and does not assert positive summands, unique representations or results for other run-length divisibility conditions.
