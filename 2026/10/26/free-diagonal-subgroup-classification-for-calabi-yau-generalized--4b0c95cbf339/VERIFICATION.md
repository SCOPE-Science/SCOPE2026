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

The accompanying dependency-free `verify.py` was run with Python 3 and returned `VERIFY_OK: AGL orbit counts 840/30/1; cyclic counts 280/10; free arrays and Euler -1080`.

The code explicitly enumerates full affine-group orbits of every permutation of the complete character set for \(\mathbb F_3^2\), \(\mathbb F_2^3\) and \(\mathbb F_2^2\). It checks balanced eigenvalue histograms and the exact Chern coefficient for three cubics in projective eight-space. These finite checks support but do not replace the symbolic proof for all parameters. No independent mathematical audit or external certification was performed.
