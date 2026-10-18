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

# Verification of the orientation character

The proof rests on the exact integer recurrence for the signed independence-set sum, the published forest sphere theorem and dimension relation, the packing argument for domination number, and the signed fixed-face Hopf trace for tree branch swaps. The formula is proved for all \(b\ge2\), \(h\ge0\); finite computations below are cross-checks and are not substitutes for that proof.

Run `python3 verify_orientation.py` and `python3 verify_simplices.py` using only Python's standard library. The first checks all heights through thirty, branching factors through ten, and all local-generator positions in the noncontractible cases; 2,700 generator assertions pass. The second explicitly builds the simplicial complex and graph permutations for the parameter pairs \((2,1),(2,2),(2,3),(3,1),(3,2),(4,1)\), then computes reduced mod-two boundary ranks and signed fixed-face traces; 17 generator assertions pass. Both programs complete without errors.

The general topology conclusion uses Ehrenborg–Hetyei's forest theorem and Marietti–Testa's dimension formula, verified against their published proofs. No computer enumeration of arbitrary height is asserted; no independent human audit has been performed. The presence of nontrivial orientation characters does not by itself give an equivariant homotopy classification.
