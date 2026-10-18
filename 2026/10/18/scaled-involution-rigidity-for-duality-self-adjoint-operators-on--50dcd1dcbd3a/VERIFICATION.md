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

# Verification record

The analytic proof in `RESULT.md` derives the two-coordinate identity directly from the normalized duality map and verifies its differing asymptotic consequences on either side of \(p=2\). Above \(p=2\), the explicit second derivative formula has a nonnegative variance term and controls every overlapping coordinate. Below \(p=2\), the fractional-power coefficient forces vanishing overlap. The remaining row/column argument establishes the exact monomial structure and equal weight moduli, and direct substitution proves the converse.

Run `python3 checker.py` using the Python standard library. It completes 480 constructive-family examples with complex phases and 960 excluded-family examples across six non-Hilbert exponents, in dimensions two, three, five, and eight. This finite diagnostic script is not an exhaustive verification of infinite-dimensional statements.

Scientific scope: \(1<p<\infty\), \(p\ne2\), at least two coordinates, real or complex \(\ell_p\), every bounded linear operator and every input vector. The 2020 reference was not available in full; priority verification is consequently subject to that residual risk. No independent audit or independent validation has been performed.
