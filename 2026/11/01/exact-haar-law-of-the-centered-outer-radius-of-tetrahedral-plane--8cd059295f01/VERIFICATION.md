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

# Reproducibility of the tetrahedral section-radius law

Run `python verify_tetra.py` using Python 3.10+ and only its standard library. The script reconstructs every section-edge intersection from the tetrahedron's four vertices; checks exact rational identities and seven rational ratio thresholds for generic integer normal vectors; compares two independent spherical-triangle area evaluations; checks the Haar partition normalization and the transition; and simulates 150,000 independent Gaussian normals (whose directions are Haar-uniform).

Recorded run: `PASS 7236 exact and structural assertions plus 150000 Haar-random plane samples`.

Sample comparisons (analytic versus observed unconditional CDF): at radius \(1.1\), 0.140839807 vs. 0.140900000; at radius \(\sqrt{3/2}\), 0.275100171 vs. 0.275413333; at radius \(1.5\), 0.663619276 vs. 0.663553333. Every assert passed. The Monte Carlo comparison allows an absolute deviation of 0.009; it is not an exact infinite verification. The displayed analytic proof, not random testing, handles all orientations and parameters.

The test program and all data necessary for its execution are embedded in the same record. No remote code execution, network access, or specialist mathematical package is required.
