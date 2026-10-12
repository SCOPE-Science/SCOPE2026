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

Run `python3 verify.py` (Python 3.9+; standard library only). The verifier reads no external files. It derives all twelve conic-line intersection pairs from the supplied line coefficient triples, computes eleven rational singular points per arrangement, reconstructs exact component incidences, and computes the supports of all cross-product contents for point/line collisions. Its exact prime support outputs are \(\{2,3,5,7,11\}\), \(\{2,3,5\}\) for the two point sets and \(\{2,3,7\}\), \(\{2,3\}\) for their line sets.

For \(p=7\) the script enumerates the full finite projective plane, identifies the two coinciding pairs of lines, and verifies the reduced arrangement's five singular points of branch multiplicities \((2,2,1)\) in orders double, triple, quadruple. For \(p=11\) it checks six separate lines, ten singular points of branch-count profile \((5,3,2)\), and gradient proportionality proving conic-line tangency at \([1:2:8]\). It independently verifies regular profiles for the second arrangement at \(p=7,11\) and both arrangements at \(p=13,17,19,23,29\).

The infinity of primes is covered mathematically by the complete rational intersection census and the exact cross-product prime-support identity, not by sampling. The finite-field counts suffice geometrically because the complete line-line and conic-line intersections are rational after reduction. Nothing in these checks establishes positive-characteristic Jacobian syzygies, near-freeness, or model-independent minimal bad reduction. Independent audit has not been performed.
