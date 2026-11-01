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

Install the declared `sympy==1.14.0` dependency from `requirements.txt` before running `python verify.py`. The standalone `verify.py` regenerates the seventh-power Cartier matrix for \(y^3=x^5+a x^2+b\), after reducing to \(b=1\) by weighted coordinate scaling, from exact multinomial coefficient extraction. It proves the crucial finite-degree polynomial identity over \(\mathbb F_7[u]\): the greatest common divisor of the nonzero \(2\times2\) minors of the semilinear second iterate is \(u^4(u^{10}-1)\). Since smoothness excludes \(u^5=-1\), this certifies the only rank-drop loci in the parameter line.

Over \(\mathbb F_7\), the exact Cartier iterate ranks at \(u=0\) are \(2,1,0,0\) and at \(u=1\) are \(2,1,1,1\). Every \(u\) with \(u^5=1\) is algebraically equivalent by scaling to \(u=1\); all \(u=0\) models are identical after normalization. The proof of stable generic rank two uses stabilization of the second image, not finite-field sampling. Jacobian \(a\)-number two follows from rank two of Cartier on the regular differential basis throughout the smooth parameter locus.

These checks establish the specified family, not every genus-four cyclic trigonal curve, and they are not an independent scientific audit.
