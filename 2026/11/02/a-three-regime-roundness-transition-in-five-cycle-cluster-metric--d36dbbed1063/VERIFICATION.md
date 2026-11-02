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

# Reproducibility and scientific verification

Run `python verify_five_cluster.py` with Python 3.10+ and NumPy 2.x, as recorded in `requirements.txt`. The checker reconstructs distances for each of the \(5m\) labelled points independently of the tensor eigenvalue formula. It performs exact integer/rational tests of the block quadratic-form identity, checks the entire numerical spectrum against the Fourier decomposition for several sizes and all three scaling regimes, and inspects the eigenvalue signs on both sides of the defining root.

Actual executed output:

```text
EXACT_BLOCK_QUADRATIC_DECOMPOSITION_OK 725
FULL_MATRIX_EIGENVALUES_OK 210
SHARP_BOUNDARY_AND_CRITICAL_RANK_OK 48
PERSISTENT_NONZERO_EXPONENT_AND_FIRST_CORRECTION_OK
CRITICAL_INVERSE_SQUARE_ROOT_BRANCHING_OK
SUPRACRITICAL_INVERSE_LINEAR_BRANCHING_OK
EXACT_GRAPH_BLOWUP_ENDPOINTS_OK
ALL_FIVE_CLUSTER_ROUNDNESS_CHECKS_OK
```

The 725 exact identities use rational distances and integer zero-sum test vectors. The 210 full spectra use direct NumPy symmetric diagonalization of independently built powered-distance matrices. The 48 boundary tests evaluate the claimed critical multiplicity and sign change. Large-\(m\) asymptotic checks assess the correct constants and rates, including the first correction when \(s<s_c\).

**Analytic coverage:** The universal assertions are proved by the exact tensor identity, explicit circulant eigenvalues, strict convexity, and Taylor/implicit-function expansions. The finite code does not certify every positive real \(s\), every \(m\), or every exponent. In particular, its numerical root approximations are not independent certificates of uniqueness; uniqueness follows from the proof.

**Scope of validation:** Self-review only. No independent mathematical audit has been performed.
