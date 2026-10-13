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

For \(\operatorname{Cr}_n\), a zero-zero edge \(a_i b_j\) with \(i\ne j\) has neighborhood union equal to all vertices except \(a_j\) and \(b_i\). The checker therefore tests the defining inequality directly, without using the polynomial formula as the feasibility oracle.

`verify.py` exhaustively enumerates all ternary labelings for \(3\le n\le6\), compares every weight coefficient with the theorem, and verifies that the weight-\(2\) minima are precisely the deleted matching pairs labeled \((1,1)\). It separately checks the closed invalid-count formulas for the low-weight pattern classes through \(n=30\).

Reproduction command:

`python3 verify.py`

Expected output:

`ALL CHECKS PASSED; exhaustive_orders=[3, 4, 5, 6]; exhaustive_labelings=597780; low_weight_orders=28; minimum_functions_checked=18`

The finite computation is a stress test only. The infinite theorem follows from the exact neighborhood-union reduction and symbolic classification of every possible failure at weights at most \(5\). No independent audit or external validation is claimed.
