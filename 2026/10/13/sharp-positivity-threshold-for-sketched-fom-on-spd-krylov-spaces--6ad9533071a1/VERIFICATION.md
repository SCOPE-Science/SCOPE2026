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

## Reproduction

Run `python3 verify.py` from the directory containing this document and the standalone verifier. The script requires only the Python standard library. Its expected successful final line is `EXACT_CHECKS_PASS 25308`.

All sample values are exact `fractions.Fraction` values. The script checks endpoint spectral cases of the angle inequality, the rational sharpness formula, exact equality cases, and embedding quadratic forms over a finite integer grid. The counterexample includes a genuine two-row sketch of a three-dimensional system.

## Proof-dependent checks and limits

The universal matrix and complex-eigenvalue arguments are proved in RESULT.md, not inferred from finite enumeration. In particular the key nonstandard step is the sharp turning-angle estimate \(x^*Ax/(\|x\|\|Ax\|)\ge 2\sqrt{\mu L}/(\mu+L)\) for positive-definite \(A\); RESULT.md includes a direct polynomial spectral bound and minimization proof. The finite verifier does not certify novelty, probabilistic sketching guarantees, or floating-point stability.

No independent audit has been conducted.
