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
The analytic proof uses only the exact neighborhood structure of a complete multipartite graph. For a fixed color and a part containing that color, the same-colored neighborhood size is the total color-class size minus the number of same-colored vertices in that part. Summing the resulting majority inequalities gives the global half-order lower bound for every used color class. Equality analysis gives the forced half-splitting in every part.

The standalone `artifacts/verify.py` independently checks the original majority-neighborhood definition without assuming the theorem. It enumerates every complete-multipartite isomorphism type with at least two parts through order \(8\), all canonical surjective colorings of those graphs, and all labeled surjective two-color assignments. It compares the computed maximum number of colors with the parity formula, verifies that every valid two-coloring is balanced inside each part, and compares the exact labeled count with \(\prod_i\binom{n_i}{n_i/2}\).

Expected replay output:

`ALL CHECKS PASSED; multipartite_types=58; canonical_colorings=101632; valid_canonical_colorings=128; labeled_two_assignments=7968; valid_labeled_two_assignments=140; chi_two_types=7; max_order=8`

The finite enumeration is not an infinite proof and is not used to infer novelty. It is a bounded stress test of the universal analytic argument and the optimizer-count formula.
