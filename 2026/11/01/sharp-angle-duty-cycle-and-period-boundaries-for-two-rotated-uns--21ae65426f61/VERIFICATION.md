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

# Reproducibility and checks

The analytical proof in `RESULT.md` uses exact two-by-two matrix identities, positive-definite similarity, a convergent hyperbolic power series and monotone weighted power means. It derives all infinite-parameter claims including both singular angle limits and the square-root duty boundary. No finite numerical sampling is used as an exhaustive proof.

Running `python verify.py` requires Python 3, NumPy and SciPy. The script constructs the two original matrices, evaluates their matrix exponentials and eigenvalues directly, and compares the computed spectral radius with the symbolic closed formula at 525 parameter combinations. It separately checks a closed-form period cutoff and both sides of a nonzero allowable duty imbalance, orthogonal saddle cases, near-orthogonal cutoff asymptotics, and an unequal-duty unique-cutoff example. Expected output begins with `PASS: 525 direct 2x2 monodromy comparisons`.

A source comparison examined the public full text of the March 2026 mechanical-oscillator study, the relevant theorem and its derivation from a 2021 cooperative periodic-system paper, and relevant introductory and main-result material in a 2021 study of stable planar switched systems. The accessible 2004 general Floquet article was reviewed at abstract level only; no full-text exclusion claim is based on it. Independent scientific audit or validation has not been performed.
