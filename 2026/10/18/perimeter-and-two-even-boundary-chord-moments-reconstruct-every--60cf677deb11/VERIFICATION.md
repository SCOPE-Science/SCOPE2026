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

# Reproducibility and verification

With the declared SymPy dependency, execute `python checker.py` alongside `requirements.txt`. The executable regenerates the elementary conditional integrals for independent uniform endpoints on individual sides, reconstructs the full second/fourth moment formulas through exact symbolic arithmetic, verifies the exact polynomial identities underlying the sharp ratio inequality, and tests reconstruction of rational triangle side triples. Four independently generated Euclidean triangle endpoint-sampling experiments (60,000 pairs each) compare the predicted moments with observed moments.

The executable completed successfully and printed `TRIANGLE_BOUNDARY_CHORD_MOMENTS_OK`, preceded by four section PASS messages. These finite simulations are calibration checks only: the proof of the ratio range, equality classification and fixed-area isosceles envelopes is given in `RESULT.md` by elementary inequalities, calculus and the geometry of a fixed-product level set. No computational experiment proves a universal theorem, and the packaged code does not claim independent mathematical validation.

A separate published result verifies the earlier-known second boundary-distance moment for arbitrary triangles; its equivalence to the present \(M_2\) expression was compared. The fourth moment and reconstruction use the new direct integral derivation. A relevant 1982 random-chord triangle-recognition article was available only via its abstract; full-text priority comparison remains incomplete. Literature-based originality remains fallible.
