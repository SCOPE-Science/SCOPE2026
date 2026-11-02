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

# Verification of idempotent Nijenhuis orbit classification

The attached `check_nijenhuis.py` uses elementary finite-field arithmetic; for \(q=9\), arithmetic is explicitly carried out in \(\mathbb F_3[z]/(z^2+1)\). It reconstructs the original Lie brackets, tests the idempotence equation and Nijenhuis torsion for each proposed projection, enumerates every two-dimensional Lie-subalgebra plane and every complementary projective line, and checks the Borel-stabilizer orbit partition. For \(q=3,5\), it additionally constructs every projective two-by-two invertible matrix and directly computes the complete eight-orbit partition by conjugation of the three-by-three operators. It also independently exhausts every one of the \(3^9\) ambient three-by-three endomorphisms for \(q=3\), proving computational completeness in that single field.

Run `python3 check_nijenhuis.py` in a directory containing this file. The corresponding observed output is included verbatim as `verification_output.txt` and ends with:

`SL2_NIJENHUIS_PROJECTION_CHECKS_OK 4_FIELDS 1_AMBIENT_EXHAUSTIVE 2_FULL_GROUP_ORBIT_CHECKS`

The four checked fields are \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\). The tests exhaust the projection candidates in all four cases, but only the first case exhausts all arbitrary ambient matrices. The complete arbitrary-odd-field classification is established by the separate mathematical proof; code alone cannot certify it. These checks do not establish historical priority, global scheme reducedness, or coverage beyond the stated fields.
