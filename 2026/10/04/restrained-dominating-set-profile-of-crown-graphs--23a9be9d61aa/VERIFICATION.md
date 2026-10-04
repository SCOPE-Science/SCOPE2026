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

The proof is analytic. The finite checker is a separate consistency test.

`verify_crown_restrained.py` constructs \(\operatorname{Cr}_n\) directly for every \(3\le n\le9\), tests every vertex subset against the definition of restrained domination, tests the stated profile criterion independently, and compares every \((\alpha,\beta)\) profile count with the closed coefficient formula. It also checks that the minimum size is two and that exactly the \(n\) deleted-matching pairs are minimum restrained dominating sets.

The finite range is not an exhaustive proof for arbitrary \(n\). The general proof in `RESULT.md` derives the four boundary conditions from exact neighbor counts and derives the enumerator by a disjoint case count.

Actual replay output:

`VERIFY_OK n_range=3..9 subset_checks=349504 criterion_checks=349504 valid_sets=329555 coefficient_checks=371 minimum_checks=7 max_order=18`
