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

# Reproducible finite checks

Run `python3 check_rook_super.py` using Python 3.9 or later and the standard library only. The program computes adjacency in each rook graph directly and tests the defining super domination property without assuming the structural theorem. It separately checks the incidence criterion and generates every complement in the claimed optimal families.

On nine boards, from \(2\times2\) through \(4\times5\), it examines all \(1{,}152{,}848\) vertex subsets, verifies equivalence of the direct and structural predicates, checks the optimum size, and compares the entire family of actual minimum-super-domination complements with the family generated from the theorem.

On \(5\times5\), it independently checks all \(657{,}800\) omitted-cell subsets of size six or seven, checking that exactly the claimed 400 six-element configurations work and none of the seven-element configurations does. It does **not** claim to enumerate all subsets of the 25-vertex graph. The total of 1,810,648 direct-definition subset tests passed. Run output is provided in `check_rook_super_output.txt`.

The infinite theorem depends on the written proof's universal incidence bound and equality characterization; finite verification cannot replace those arguments.
