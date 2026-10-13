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

# Reproducibility and proof checks

The included `verify_photon.py` is a self-contained Python 3 / NumPy finite-dimensional verifier. Execute `python verify_photon.py` from the folder containing it. It constructs \(N=3,4,5\) families whose internal states span \(N-1\) dimensions with full-support dependence, and compares the coincidence probability from the explicit ordered internal tensor against the independent double sum using the permutation Gram matrix. For each dimension it uses an identity, a Householder unitary and a QR-derived unitary. It separately inserts a proportional internal-state pair and an embedded balanced beamsplitter, testing exact suppression for all three dimensions. For a three-photon full-support family it checks numerically that the permutation-Gram kernel has one zero eigenvalue, its complement has positive gap, and the derived lower bound is respected. It also checks the elementary factorial inequality at a finite set of dimensions.

The actual program output was:

`VERIFY_OK direct_tensor_gram=12 HOM_boundary=3 positive_orbit_quotient=passed finite_factorial_gap=passed`

These tests are not exhaustive and no program result is used as a proof that no zero occurs for every unitary or arbitrary photon number. The infinite claim follows from the explicit determinant identity, linear independence of tensor words of a basis, algebra of three exchanged spatial assignments, characterization of the unique alternating kernel, and the classical Egorychev–Falikman permanent bound. For full-support dependence, \(\lambda_*(J)\) is calculated from the actual finite-dimensional Gram matrix of the given internal states; the theorem does not assert a state-independent positive spectral lower bound. Finite precision also cannot certify arbitrarily small gaps near the proportional-pair boundary.

The physical model assumes independent single-photon pure inputs, an ideal internal-mode-preserving lossless \(N\)-port, and full collision-free detection, and explicitly excludes nonideal spectral filters, entangled/mixed preparations, other output occupations, or rank at most \(N-2\). The initial public posting date for the primary motivating arXiv work is 2014-10-06, not the later revision date. Independent external review has not been performed.
