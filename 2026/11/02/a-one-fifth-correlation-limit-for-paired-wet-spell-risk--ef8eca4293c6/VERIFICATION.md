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

# Reproducibility checks

Run `python3 verify.py` from the directory holding the seven included files. This standalone standard-library program verifies polynomial coefficients, an exact Markov-chain avoidance recursion, independent enumeration up to thirteen observed days over eight rational persistence settings, the basepoint spectral identities, and illustrative long-horizon stationary points. The exact run reports `VERIFY_OK assertions=288`.

The infinite-horizon limit, existence of interior finite-horizon optima for all integers \(n\ge4\), eventual uniqueness, and the \(O(n^{-2})\) correction are justified analytically in RESULT.md. No finite experiment certifies those infinite assertions. The actual code is included, and no external data, private files, or network access are required to rerun the checks.

Historical originality comparisons rely on accessible abstracts for some archival papers. A 48-page 2022 preprint was inspected in its relevant run-waiting-time sections. This is self-review, not an independent assessment.
