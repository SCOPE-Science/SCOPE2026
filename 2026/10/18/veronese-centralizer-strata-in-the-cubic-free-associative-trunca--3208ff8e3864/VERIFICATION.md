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

The standalone verifier `verify.py` builds the length-at-most-three word basis and implements multiplication by word concatenation. It computes all \(15\times15\) adjoint matrices by finite-field elimination over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), exhausting all \(q^6\) possible degree-one and degree-two coefficient combinations. The central nine coordinates are proved to have no effect. Recorded histograms were: for \(q=2\), \((1,3,12,48)\); for \(q=3\), \((1,8,72,648)\); for \(q=5\), \((1,24,600,15000)\); and for \(q=7\), \((1,48,2352,115248)\), in rank order \((0,1,2,4)\).

Replay with `python verify.py`. The script uses only the Python standard library. No finite computation establishes the formulas for all finite fields or establishes the geometric singular-locus claims; those follow from the proof in RESULT.md. Independent audit remains unperformed.
