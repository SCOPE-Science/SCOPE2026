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

The provided `verify_filling_census.py` is the complete reproducible checker. It requires Python 3 and SymPy (tested with version 1.14), with no additional input data files. It constructs the polynomial basis over \(\mathbb F_2\), evaluates gradients at all \(15\) rational points for all \(2^{16}\) quartic classes, and then uses four exact affine Gröbner unit-ideal tests for each of the \(288\) surviving masks. The attached `CENSUS.json` stores all smooth and excluded masks and the canonical monomial supports for the quotient basis.

Actual runs partitioned the \(288\) survivors into intervals \([0,45)\), \([45,105)\), \([105,165)\), \([165,225)\), and \([225,288)\). Smooth counts were respectively \(23,30,30,29,32\); excluded counts were \(22,30,30,31,31\). All \(144\) geometrically smooth cases had computed rank \(19\) for the Frobenius matrix and its stable iterate. The four-chart Gröbner checks certify emptiness of each singular ideal over an algebraic closure, not merely over \(\mathbb F_2\).

The explicit coefficient formula for the Frobenius action is derived from the Koszul resolution of a \((3,4)\) complete intersection and the characteristic-two action on the Cech Laurent-monomial basis. The rank computation is finite and exact, and is interpreted as the Jacobian \(2\)-rank only for geometrically smooth complete intersections. There has been no independent external audit or validation. The finite census concerns only the specified fixed cubic over \(\mathbb F_2\).
