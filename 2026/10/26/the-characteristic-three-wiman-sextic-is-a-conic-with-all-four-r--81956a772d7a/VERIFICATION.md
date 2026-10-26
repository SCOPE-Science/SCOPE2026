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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 (standard library only). The checker directly multiplies the four line forms with the conic over \(\mathbb F_3\), compares every degree-six monomial coefficient to the Wiman polynomial, enumerates projective \(\mathbb F_3\) points, identifies the rational tangencies and the six distinct pairwise tangent-line intersections, verifies no unexpected incidence, and checks the local-length, genus, and point-count formulas. Expected output begins with `PASS:`.

These are finite checks. Geometric completeness is proved using smoothness, Bézout, the smooth dual conic, and local complete-intersection equations in `RESULT.md`. The tacnode Tjurina algebra is the formal quotient \(k[[u,v]]/(u(u-v^2),2u-v^2,-2uv)\simeq k[[v]]/(v^3)\). The normalization defect at a contact follows from agreement of branch sections modulo \(v^2\). No curve-stability or stable-model calculation has been performed. The documented scientific review is not an independent audit.
