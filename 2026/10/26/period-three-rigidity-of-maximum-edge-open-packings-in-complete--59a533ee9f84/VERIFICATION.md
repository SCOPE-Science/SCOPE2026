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

The embedded `verify_eop_tree.py` uses only Python 3.9+ standard libraries. Execute `python3 verify_eop_tree.py` in a directory containing this file. Its actual output is saved as `VERIFIER_OUTPUT.txt`.

The direct checker constructs \(T_{b,h}\) and determines forbidden pairs by scanning all potential **distinct third edges** joining their endpoints; it exhaustively examines all edge subsets for 11 parameter pairs, including \((b,h)=(4,2)\) with 1,048,576 subsets. All 1,069,183 checked subsets agree with the formula and unique layered optimizer. The independent root-boundary recursion checks 162 pairs with \(2\le b\le10\) and \(1\le h\le18\), including all \(2(b+1)\) boundary states at each pair. Its multiplicity tracker verifies uniqueness of the optimal root state.

These are finite checks. The all-height result is certified mathematically by the displayed recurrence, its explicit all-state inductive solution and the strict root-state inequalities, not by an extrapolation from tested heights. The checker does not validate bibliographic novelty or establish independent review.
