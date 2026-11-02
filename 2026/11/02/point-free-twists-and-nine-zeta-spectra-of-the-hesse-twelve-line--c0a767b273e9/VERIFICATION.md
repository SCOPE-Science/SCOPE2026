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

# Verification and reproducibility

Run `python3 verify_hesse.py` with Python 3 and no additional packages. It enumerates all \(432\) affine transformations on \(\mathbb F_3^2\), constructs the four finite configurations, and computes each permutation cycle decomposition. It checks that the ten signatures have sizes \(72,9,54,108,36,24,1,72,8,48\), that each determinant value occurs in \(216\) transformations, that there are exactly nine zeta signatures, and that the one point-free signature consists of precisely \(48\) affine maps with nontrivial unipotent linear part and nontrivial torsor class.

The verifier first computes the norm of every one of the \(220\) Eisenstein-integer triple determinants of the twelve geometric lines, obtaining the exact distribution \(0^{36},1^{28},3^{81},9^{72},27^3\). This rules out extra line concurrency in all characteristics greater than three. An independent geometric construction over \(\mathbb F_7\) checks twelve distinct lines, nine quadruple intersection points, twelve double intersection points, and all \(66\) line pairs. A polynomial routine using integer dictionaries computes the Hessian for each of three explicit cubics. It tests smoothness at all rational projective points, finds the rational flexes, and tests all rational projective lines for membership in the Hesse pencil by comparing the binary-cubic restrictions of the cubic and Hessian at four distinct parameter points. The results are \(0,0\), \(0,3\), and \(3,3\) for (rational flexes, rational Hesse lines), and rational cubic point counts \(6,9,6\), respectively.

The supplied `verify_output.txt` is the checked execution output and ends with `VERIFY_OK`. Exhaustion concerns a finite group and finite projective planes only; the general theorem uses the geometric configuration, Galois-torsor description, normalization, and a separate point-free linear-algebra argument. No nonreduced singularity schemes, characteristics two or three, or complete small-field realization classification are asserted. Independent mathematical validation has not been performed.
