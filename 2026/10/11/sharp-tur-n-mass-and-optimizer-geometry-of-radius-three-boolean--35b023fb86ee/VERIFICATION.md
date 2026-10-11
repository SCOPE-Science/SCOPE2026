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
The script `check_hamming_radius3.py` is standalone Python 3.9+ (stdlib only). Run `python3 check_hamming_radius3.py` in the same directory. Its output includes `VERIFY_OK` after exact rational Walsh inversions and modular ranks, without numerical tolerances. The proof of the all-dimensional bounds, the two-slice interpolation lemma and the optimizer classifications appears in `RESULT.md` and does not depend on this finite verification.

The constructions were checked for all dimensions \(3\le d\le11\), including every odd simplex vertex and three parameter values for each even radial family. This is not an exhaustive check of all functions in those spaces. The rank computations are exact modulo the prime \(1000003\); in the proof the nullspaces are established algebraically for all dimensions. The independent mathematical audit has not been performed.
