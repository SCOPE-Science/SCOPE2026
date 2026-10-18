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

## Reproduction

Execute `python3 verify_dodecahedron.py` using Python 3.9+ standard library. The executable checks every pair of the twenty regular-dodecahedron vertices, the complete set of thirty nearest-neighbor edges, every pair of the ten antipodal axes, and each of the ninety oriented great-circle intersections. Integer-pair arithmetic in \(\mathbb Z[\sqrt5]\) determines all signs exactly. Every local four-sector sign pattern is generated and verified, and all ninety-two spherical chambers are exhaustively classified into \((20,6,6)\), \((60,3,8)\), and \((12,5,10)\) by (number of chambers, corners per chamber, planar-section sides). All chamber-angle cosine multisets are checked exactly.

## Analytical checks and limits

The exact chamber angles imply the three area expressions by the spherical excess formula. The weighted sum is exactly \(4\pi\), and the independent random-edge-crossing expectation yields \(30\arccos(\sqrt5/3)/\pi\), agreeing with the distribution's mean. Floating-point evaluations at the end of the checker confirm positivity and normalization only; no floating-point experiment is used to prove the sign classification. Verification is for generic central sections only, not offset or vertex-containing planes. This is not independent review.
