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

# Verification of the rank-spectrum formulas

Execute `python3 verify.py` with Python 3 and no third-party packages. The deterministic marker is `VERIFY_OK`.

The script enumerates each coefficient vector over nine cyclic quandle tests with prime coefficient fields, plus three valid \(\mathbb F_4\) tests and three tests on \(C_3\times C_3\); the pairs \((A,\varphi)\) include latin, nonlatin, and trivial cases. A separate larger cyclic case checks only symbolic consistency and is explicitly marked `FORMULA_ONLY`. Each exhaustive test independently constructs the quandle multiplication table, forms the left/right multiplication matrices, calculates their ranks by finite-field elimination, and compares the full rank histograms and exact zero-product pair count against the orbit formulas. For \(\mathbb F_4\) the checker implements arithmetic modulo \(X^2+X+1\).

Key exhaustive comparisons include \(C_4\) with inversion over \(\mathbb F_3\), giving \(1089\) ordered zero-product pairs and unequal left/right rank distributions; \(C_5\) with multiplication by \(2\) over \(\mathbb F_2\), giving \(93\) pairs with a nonsplit orbit of size four; and \(C_3\times C_3\) with the diagonal automorphism \((x,y)\mapsto(x,-y)\) over \(\mathbb F_2\), giving \(38592\) pairs and respective rank supports \(\{0,1,2,3\}\) and \(\{0,3,6,9\}\).

The theorem's unbounded scope follows from the finite Fourier transform, Frobenius descent, and disjoint-fiber rank calculations in `RESULT.md`. The small-field enumerations are cross-checks rather than proof of infinitely many cases. No independent audit is claimed.
