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

# Reproducibility and verified scope

The self-contained program `verify.py` uses Python's `fractions.Fraction` and no third-party packages. Run `python3 verify.py` in the directory containing this file. It enumerates all sampled component signs and refresh choices exactly, computes their covariance map, and compares it with two independent symbolic identities stated in the proof. It also checks positive-definiteness of the auxiliary matrices and of the covariance reachable from the actual shared initialization, tests the fixed-probability specialization, and verifies the exact rational stable/unstable witness.

A direct run completed \(1{,}710\) rational parameter configurations. These finite checks are transcription and calculation safeguards, not an exhaustive proof of infinite-time convergence. The strict matrix inequalities and the degree-two polynomial root argument in `RESULT.md` are the proof for all admissible real parameters. At the critical point the proof establishes nondecay; the verifier does not purport to certify independence, priority, higher-dimensional behavior, or external scientific review.
