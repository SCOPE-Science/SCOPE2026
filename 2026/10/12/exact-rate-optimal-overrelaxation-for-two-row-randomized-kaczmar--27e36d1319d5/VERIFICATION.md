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
# Reproducibility and boundaries

The included `verifier.py` is a standalone Python 3 program requiring the public SymPy package. Run `python verifier.py` to reproduce the algebraic covariance identities, the rank-one determinant/secular identity, the differentiation identity, 6,240 exact-rational test cases, and representative numerical eigenvalue and optimization comparisons. During preparation, it completed with `SYMBOLIC_OK`, `RATIONAL_CASES_OK 6240`, and `VERIFY_OK`.

These computational checks are supporting consistency evidence, not an exhaustive numerical verification for uncountably many row geometries and stepsizes or infinitely many iterations. The domain-general assertions instead follow from the exact analytic proof in `RESULT.md`. The strongest literature-related limitation is that some early specialized relaxation and exact-MSE work could not be read fully; absence of a discovered match is not mathematical proof of novelty. No outside reviewer or independent audit has validated this result.
