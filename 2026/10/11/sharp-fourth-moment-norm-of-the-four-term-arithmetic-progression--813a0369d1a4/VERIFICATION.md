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

`python3 artifacts/verify.py` requires SymPy and performs exact symbolic checks. It reconstructs the convolution identity for the fourth moment, verifies the elementary boundary parabola, recomputes the lexicographic Gröbner basis for the interior Lagrange equations, and checks exact back-substitution relations for every elimination factor.

For the degree-eight branch, the verifier obtains rational isolating intervals for all four positive roots and proves by Sturm root counts that the back-substitution polynomials do not change sign on those intervals; at each root one of the required positive coordinates is negative. It then eliminates the unique positive cubic root \(\tau\) from the attained ratio and verifies that the resultant is \(104(208X^3-1224X^2+2268X-1323)\). Rational isolation identifies the relevant largest root and confirms that it lies strictly above the complete boundary bound \(15/7\).

The printed decimals are derived only after the exact assertions pass. No finite sample is used to certify the global maximum.
