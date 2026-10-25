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

# Exact verification

The included `verify_petersen_line_square.py` requires Python 3 and uses only the standard library. `verify_integral_coinvariants.py` requires SymPy 1.14, and imports the first script from the same directory. Both scripts derive the graph from two-subsets rather than relying on external databases. The first script exhaustively enumerates 15 line vertices, 105 pairs, 1,023 simplices, 120 group permutations and all seven character classes, checking the signed simplicial Lefschetz traces and exact Specht inner products. The second explicitly creates four signed 32-by-32 integer action matrices, checks the Coxeter relations and computes the exact 32-by-128 Smith normal form.

Expected decisive outputs include `VR_RADIUS_TWO_INTEGRAL_H4_RANK 32`, `FULL_S5_INVARIANT_RATIONAL_H4_DIMENSION 2`, `SMITH_NONZERO_UNIT_FACTORS 30` and `SMITH_ZERO_FACTORS 2`. The complete genuine script outputs are in `verification_output.txt`.

The local computations establish the exact finite numerical assertions. The proof of the join decomposition, signs, module construction, representation formula and validity of the coinvariant presentation appears in `RESULT.md`. They do not amount to independent external certification, an orbit-space integral-homology calculation, or an exhaustive literature novelty proof.
