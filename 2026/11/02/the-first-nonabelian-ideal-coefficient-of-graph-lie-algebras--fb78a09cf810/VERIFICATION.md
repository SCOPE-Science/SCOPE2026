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

# Direct finite verification

The standalone `verify.py` constructs the finite-field bracket table, enumerates every subspace of codimension three in reduced-row-echelon form, and tests ideal closure by bracketing with every vertex generator. This is mathematically independent of counting Heisenberg quotient maps. A separate routine computes the complement-graph connected-component sum and compares exact integer results.

Command: `python3 verify.py`

Recorded output starts with `VERIFY_OK cases=21` and lists every checked configuration. Exhaustive instances cover all simple graphs with three vertices for field orders 2 and 3, the two-vertex single edge for both orders, and three four-vertex graphs for order 2. In total, 21 exhaustive instances were checked.

The proof applies to all prime powers, including extensions of prime fields. The verification program supports the two tested prime fields and does not establish the infinite domain by enumeration. Independent audit is not performed.
