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

The attached \(\texttt{verify.py}\) is self-contained and uses Python 3.10 or newer, with no third-party packages. Extract it alongside the other files and run \(\texttt{python3 verify.py}\). A successful run prints \(\texttt{VERIFY_OK 10007}\), together with a numerical value of the positive noise threshold and corresponding neutral step.

Checks include exact fractions for the single-step amplifier coefficient identity and the averaged quartic, 6,171 rational parameter-sign equalities, direct matrix-versus-complex updates across 2,520 combinations, explicit enumeration of all sign sequences of lengths 1 through 8 for five input pairs, and critical-root/phase-region spot checks. The proof of independence across arbitrary \(n\), the strict sign classification for every allowed \(\epsilon\) and \(\vartheta\), and uniqueness of the positive cubic root appear in the accompanying mathematical argument, not in a finite-test certificate.

The randomness model shares one independent two-point perturbation within a step, *including* the evaluation at the intermediate stage. A different correlation model changes the moment polynomial and must not be inferred to share this threshold. No independent mathematical validation has been performed.
