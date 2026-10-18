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

# Reproduction and scope

Run `python3 verify_box_slices.py` using a standard Python 3 interpreter. The program contains all needed integer and rational operations in Python's standard library and prints `VERIFY_OK` only after every asserted finite check succeeds.

It reconstructs exact vertices of six hyperplane-box slices, computes singular-basket counts independently from subsets, checks exact integral minors of all proper fan faces at every subset-sum singular vertex, and checks nearby slice perturbations and finite graded pieces of the rank-one matrix semigroup. For cap vector \((1,1,1,2,2,3)\) at level \(3\), the output includes `TORUS_FIXED 24 SINGULAR 7 BASKET {(2, 4, 4): 6, (3, 3, 6): 1}`. Tests cover examples only, not all parameters.

The symbolic proof in `RESULT.md` supplies the complete vertex exhaustion, lattice-normalization argument, full semigroup presentation, all proper-face regularity, arithmetic enumeration, multiplicity and Gorenstein criteria. Independent validation has not been performed.
