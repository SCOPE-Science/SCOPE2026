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

# Reproducibility and scope

Run `python3 verify.py` in a directory containing this file and the standalone `verify.py` included in the same result package. Only the Python standard library is required.

For each integer \(1\le m\le8\), the program enumerates all \(2^{2m+1}\) binary profiles on the friendship graph. Its `step` function calculates each vertex's next color directly from its neighbors and tie retention, independently of the run-type proof. It then tests that every second iterate is fixed, counts exact individual attraction basins, counts fixed states, forms the terminal-blue histogram, checks the formula for two-update profiles, and checks monochromatic consensus counts. All tested identities hold.

The test evaluates a total of \(174{,}760\) starting profiles and checks all \(131{,}072\) possible starting profiles on the largest tested graph (eight triangles). The infinite family theorem rests on the elementary decomposition and counting proof in RESULT.md; the finite enumeration does not certify untested values of \(m\). No independent mathematical audit or external mathematical validation is claimed.
