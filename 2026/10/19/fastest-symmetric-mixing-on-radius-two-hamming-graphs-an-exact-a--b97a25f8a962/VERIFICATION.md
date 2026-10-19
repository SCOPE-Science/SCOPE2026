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

# Reproducibility and verification limits

The exact theorem concerns integer alphabet size \(q\ge2\), integer dimension \(d\ge2\), symmetric nonnegative row-stochastic kernels on the graph of Hamming distances one or two, and the largest absolute nontrivial eigenvalue. The displayed candidate is globally optimal without an initial edge-orbit assumption. Only orbit-invariant uniqueness is asserted, except in the complete-graph case.

Execute `python verify_hamming2.py` with the optional dependencies listed in `requirements.txt`. The exact-rational part independently evaluates all \(d+1\) character-indexed eigenvalues for every integer pair \(2\le d\le36\), \(2\le q\le32\). Additional tests solve a three-variable linear program using SciPy across further dimensions and alphabets, and build full stochastic matrices to recompute small-case eigenvalues with NumPy. The completed check passed 5,172 assertions with no failures.

The program verifies finite instances; it is not an infinite-family proof. The proof in `RESULT.md` supplies the analytic spectral identities, the global symmetry reduction, the lower certificates, and every-case upper spectral bounds. Reproduction relies on the included standalone script; no external data or previously saved computations are required.

Literature originality remains subject to unresolved full-text comparison with the 1993 hypercube walk paper and possible unindexed equivalents. This package contains a self-review only; no independent audit has been performed.
