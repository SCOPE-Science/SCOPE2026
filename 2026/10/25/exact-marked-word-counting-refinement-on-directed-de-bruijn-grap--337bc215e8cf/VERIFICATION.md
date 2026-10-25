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

The standalone programs `verify_refinement.py`, `verify_markers.py` and `verify_operator.py` run using Python 3 and the standard library only, without network access, third-party packages, or input data. Invoke `python verify_refinement.py`, `python verify_markers.py` and `python verify_operator.py` in any directory containing these files. The corresponding `refinement_log.txt`, `markers_log.txt` and `operator_log.txt` record successful, exact integer checks. All checks were executed directly from the files embedded in this package before release.

- The single-root comparison covers 925 configurations and 153,977 evaluated graph vertices; it computes stable refinement from separate incoming and outgoing adjacency lists, checks the closed colour count, and compares with independently canonicalized stabilizer equality patterns.
- The arbitrary-marker comparison covers 1,899 marker sets and 143,895 vertices, including empty sets, all marker subsets when the graph has at most nine vertices, and deterministic seeded samples at larger sizes.
- The operator test checks 3,423 exact coordinate-recovery identities on 271 configurations by literal adjacency-vector multiplication, including all coordinate choices for each instance.

The verification constitutes finite regression evidence, not an exhaustive check of all alphabet sizes or word lengths. The all-parameter theorem follows from the symbolic adjacency-operator identity and the stable-partition argument in `RESULT.md`. The scientific literature comparison is not an independent priority certification. Independent mathematical audit has not been performed.
