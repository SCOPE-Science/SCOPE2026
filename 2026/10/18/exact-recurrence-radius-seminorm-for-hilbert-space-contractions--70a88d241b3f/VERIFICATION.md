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

# Verification of the Hilbert-contraction recurrence-radius theorem

The result is proved analytically for arbitrary complex Hilbert spaces; no finite enumeration or numerical convergence claim underlies its quantifiers. The indispensable nontrivial facts are (i) existence of the positive asymptotic limit for a contraction, (ii) reduction by unimodular eigenvectors, (iii) scalar spectral representation by Sz.-Nagy unitary dilation, and (iv) uniform-block squared-Fourier averaging. The last step is explicitly proved by a two-measure integral and dominated convergence, with the diagonal atom obstruction independently excluded by the Hilbert mean ergodic theorem. Exact threshold necessity and sufficiency use disjointness of a syndetic set from a uniformly Banach-density-zero set and survival of syndetic returns after deleting a uniformly sparse set, respectively.

Reproduction of finite diagnostics: run `python check_examples.py` using Python 3. This uses only the standard library. The checker verifies exact rational squared-return norms for a finite diagonal contraction, the unilateral shift on a finite-support vector, a weighted unilateral shift with a damped first edge, and the backward shift on a basis vector. These checks cannot certify the infinite-dimensional theorem; the proof is in RESULT.md.

Limits: only base-point syndetic returns and Hilbert-space contractions; no optimal gap-length constants or uniform orbit-translation statement. Publication-priority risk remains in older classical spectral recurrence theory. Independent audit has not been performed.
