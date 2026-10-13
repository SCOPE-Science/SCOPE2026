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

# Reproduction and limits

Run `python3 artifacts/verify_square_perimeter.py` from this package root with Python 3 and the standard library. The program enumerates all coprime parameter pairs in the two claimed wedges with \(9(uv)^2\le X\), constructs primitive sides, and compares the resulting set with an independent enumeration through positive divisors of \(q^4\), where \(q^2\) is the square perimeter. The second enumeration uses the independently derived identity \((2P-3a)(2P-3b)=P^2\).

For \(X=100,1000,10000,100000,1000000,10000000\), the two methods agree exactly, with respective counts \(1,1,6,16,54,165\). The final output is `SQUARE_PERIMETER_EISENSTEIN_EXACT_REGRESSION_OK`. The code uses integer arithmetic for all exact checks; the displayed asymptotic coefficient is a numerical approximation only. The infinite parametrization and \(O(X^{1/4}\log(2X))\) error require the mathematical argument in `RESULT.md`; a finite regression alone cannot verify either. Independent scientific audit has not been performed.
