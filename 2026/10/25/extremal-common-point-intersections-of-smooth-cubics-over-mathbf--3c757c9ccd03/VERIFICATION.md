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

# Reproducibility and limits

`verify_rank.py` is a standalone Python 3 program requiring only the standard library. It exhausts all 1023 nonzero homogeneous cubic coefficient vectors over the field of two elements. It tests smoothness using rank 15 of the degree-four span of the three Jacobian quadrics and counts pairwise rational masks. It verifies 336 smooth cubics, the point-count distribution, the six-entry pair histogram, the 32 interpolating forms and two smooth forms for the selected five-point configuration, and the 56,280 unordered pairs.

`verify_groebner.py` requires Python 3 and SymPy. It independently computes geometric smoothness through affine-chart Jacobian Gröbner bases, counts the same 336 smooth cubics, uses binomial moments over all 128 subsets of the seven rational points to reconstruct the pair histogram, and independently checks the two extremal representative encodings. Exact expected output is in `reference_output.txt`.

For geometric multiplicity five at the distinguished rational point, inspect the factorization and three line restrictions in `RESULT.md`; both the length-nine Bézout sum and the absence of nonrational points follow algebraically. The two scripts do not purport to be independent scholarly review and do not inspect the full mathematical literature.
