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

# Mathematical verification

The finite expectation and covariance follow from the indicator expansion in `RESULT.md`; the only negative local overlap arises when the two sampled labels in an equality event are the same two labels constrained to *different* endpoints by one triangle. This proves the all-parameter formula without enumerating random graph states.

Run `python verify.py` with Python 3 and its standard library. It exhaustively constructs ten small state spaces, with \(n\in\{2,3,4,5,6\}\) and \(m\in\{2,3,4\}\) in the explicit cases listed by the script. For each state it counts the two-cycles by equality among outgoing labelled endpoint choices, and counts triangles as products of edge multiplicities on triples of vertices. Exact `Fraction` calculations test that covariance agrees with the claimed sum; the total enumeration covers 30,377 equiprobable attachment outcomes. Successful output concludes with `VERIFY_OK`.

The independent enumeration is a finite consistency check, not an infinite proof. The \(\zeta(2)-\zeta(3)\) limit is the convergent-series identity \(\sum_{q\ge2}(q^{-2}-q^{-3})\), and the separate \(\Theta(\log n)\) three-cycle variance estimate is cited from the existing literature rather than newly computed. There is no independent audit.
