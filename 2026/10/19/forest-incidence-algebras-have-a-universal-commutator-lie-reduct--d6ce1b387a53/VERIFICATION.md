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

The proof is independent of finite search. Multiplication in a height-one incidence algebra gives \([D+X,E+Y]_e=(d_u-d_v)y_e-(e_u-e_v)x_e\). The forest edge-incidence difference map is onto and has one-dimensional kernel for each component. This supplies explicit Lie generators with brackets \([h_e,r_f]=\delta_{ef}r_f\) and a central basis; ranks of joint commutators become sums of ranks of independent \(s\)-by-\(2\) matrices. Their finite-field rank counts follow from choosing nonzero vectors and their one-dimensional spans.

The included `verify.py` is standalone Python 3 (standard library only). Running `python3 verify.py` performs direct finite-field Gaussian elimination on matrices built from the original incidence-algebra multiplication, not from the claimed abstract rank polynomial. It exhausts \(q=2\) star and alternating-path examples with \(s=1,2\), a \(q=3\) fork with \(s=2\), and a \(q=2\) fork with \(s=3\). It separately checks commuting-tuple counts and verifies the Lie-basis coordinate construction over prime fields \(2,3,5\). The run ends in `VERIFY_OK`.

Over \(\mathbb F_2\), for the star and fence on four vertices and \(s=2\), the rank-count sequence is \((4,108,1044,4212,6264,3888,864)\) and the commuting-pair count is \(4000\). Over \(\mathbb F_3\), for the fork and \(s=2\), the rank-count sequence is \((9,576,10080,27648,20736)\), with \(9801\) commuting pairs. These are finite test instances, not a certificate of an infinite statement. The tree hypothesis, height-one hypothesis and independent-audit limitation are essential scope conditions. Independent audit has not been performed.
