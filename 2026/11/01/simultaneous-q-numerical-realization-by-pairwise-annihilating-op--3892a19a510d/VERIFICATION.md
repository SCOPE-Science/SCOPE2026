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

The proof of the square-zero coefficient bound is analytical. Its only optimization is a scalar constrained maximum followed by the largest eigenvalue of a real symmetric two-by-two matrix. The construction uses diagonal multiplication on \(\ell_2(K)\), a norm-continuity argument from compact equicontinuity, and an absolutely summable coefficient representation. The reverse inclusion uses an explicit optimizing two-coordinate pair.

For supplementary reproduction, run `python3 VERIFY.py` with Python 3 and NumPy. The checker reports `PASS 35789 supplementary deterministic assertions`. Its finite tests sample complex constrained pairs, verify two-parameter products vanish, test operator norms and coefficient bounds, and verify equality examples. Finite checks are not a substitute for the proof's infinite quantifiers or the arbitrary topological domain.

The result requires norm-compact absolutely convex targets. The construction does not assert separability, minimal dimension, or extension to nonbalanced targets. Independent verification and publication-priority certification have not been performed.
