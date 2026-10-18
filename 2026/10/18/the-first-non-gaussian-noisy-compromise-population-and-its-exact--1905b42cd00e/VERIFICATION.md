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

The mathematical argument derives a strict Wasserstein contraction on the centered opinion subspace, the exact stationary second-moment recursion, a Gaussian-mixture rank obstruction, and a closed fourth-moment recursion for three agents. Neither numerical iteration nor a finite verification loop substitutes for those proofs.

Reproduction: run `python3 check.py` in the directory containing this file. Only the Python 3 standard library is needed. This checks exact rational identities used in the second/fourth-moment arguments for several population sizes and learning rates, including the \(63/20\) three-agent standardized fourth moment at \(\mu=1/2\). The script does not simulate an infinite process or purport to determine historical priority.

The uncentered mean opinion is a random walk and has no invariant probability measure. The non-Gaussian classification is for the centered invariant **joint** law, not a claimed closed form for its full density. The model has no confidence cutoff and constant utility; results under state-dependent interaction and nonconstant utility remain open.
