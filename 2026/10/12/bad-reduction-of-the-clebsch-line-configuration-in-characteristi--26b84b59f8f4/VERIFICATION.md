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

Run `python verification/verify_clebsch_mod5.py` with Python 3.

The verifier is exact and uses only arithmetic modulo \(5\). It enumerates all \(806\) two-planes in \(\mathbf F_5^4\), checks which give lines on the cubic, verifies the \(21=15+6\) split, checks the explicit reductions of the fifteen diagonal and twelve golden-ratio line formulas, and exhausts the coordinate-permutation \(S_5\)-action. It also verifies the nonzero determinant of the quadratic tangent form at the unique singular point.

Expected terminal line:

`VERIFY_OK planes=806 lines=21 line_orbits=6+15 through_node=6 away=15 golden12_to_6_pairwise stabilizers=20,8 unique_A1_node=true all_lines_F5=true`

Limit: the script's finite-field enumeration proves that \(21\) distinct \(\mathbf F_5\)-lines exist and verifies their structure. The assertion that there are no additional geometric lines over extensions uses the standard theorem that a one-nodal cubic surface has exactly \(21\) geometric lines.
