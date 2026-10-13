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

# Verification record

Run `python verify.py` with Python 3.10+ and SymPy 1.14. The script recomputes the polynomial transfer matrix and row-flip permutation from the explicit four-mask local rule, checks their commutation and 41 admissible weighted arcs, constructs the 10-dimensional and 6-dimensional symmetry blocks, and checks the two symbolic determinants exactly. This finite algebraic identity is a proof component. It further enumerates all labeled vertex subsets for rung counts three to ten (1,398,080 total subsets), checks every coefficient, uses a sparse walk dynamic program to check twisted traces through 32 rungs, and checks maximum-size coefficients through 100 rungs.

Expected terminal marker: `VERIFY_OK flip_states=16 symmetry_dims=10+6 arcs=41 block_determinants=exact brute_orders=3..10 brute_masks=1398080 trace_orders=3..32 Lucas_top_orders=3..100`.

The general validity for every integer rung count at least three follows from the combinatorial bijection, exact finite determinant identity and formal generating-function manipulations given in the proof. Exhaustive checks at finitely many orders cannot establish infinitely many cases. No independent audit has been performed.
