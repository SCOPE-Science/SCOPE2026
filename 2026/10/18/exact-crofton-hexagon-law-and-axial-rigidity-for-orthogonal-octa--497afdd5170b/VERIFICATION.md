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

Run `python3 octahedron_crofton_check.py` with NumPy installed. The checked copy was executed as a standalone file and returned `OCTAHEDRON_CROFTON_CHECK_OK` after 1,200,000 independently sampled normal-offset planes across six aspect-ratio triples, with all sampled section counts in \(\{4,6\}\). Its estimator applies the correct support-width weight; merely averaging offset-conditional samples over uniform normals would sample the wrong Crofton distribution. The maximum formula/sample discrepancy was below \(0.0017\); the regular-axis formula agrees algebraically to floating tolerance with \(\pi/\arccos(1/3)-2\).

The proof is exact for all strictly positive semiaxes; the finite checker is not a replacement for the edge-count, spherical-integration, Steiner, or derivative arguments. Standard identities in the proof, including mean width as an exterior-edge-angle sum, have transparent constants checked independently with the cube as a normalization test. No external certificate or independent scientific audit has been performed.
