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

# Exact checks and scope
Run `python3 verify.py` from the same directory as this document using Python 3 and its standard library. The checker uses polynomial arithmetic in explicit irreducible presentations of \\(\\mathbf F_5\\), \\(\\mathbf F_{25}\\), and \\(\\mathbf F_{125}\\), exhaustively counts \\(X\\)-points in each, computes all fifteen elliptic quotient traces over \\(\\mathbf F_5\\), and independently counts the genus-two quotient over \\(\\mathbf F_5\\) and \\(\\mathbf F_{25}\\). It checks the Cartier–Manin zero pattern and compares against the proposed zeta numerator.

The verified values are \\(\\#X(\\mathbf F_5)=16\\), \\(\\#X(\\mathbf F_{25})=96\\), and \\(\\#X(\\mathbf F_{125})=16\\), with \\(5\\) elliptic traces \\(2\\), \\(10\\) traces \\(-2\\), and \\(6\\) points on the genus-two quotient over each of \\(\\mathbf F_5\\) and \\(\\mathbf F_{25}\\). The script prints `VERIFY_OK` on completion.

These finite checks do not certify arbitrary extension degrees or geometric connectedness. The written valuation, Riemann–Hurwitz, character decomposition, Hasse-bound, Weil-bound and Cartier arguments provide the general proof. Independent audit is not performed.
