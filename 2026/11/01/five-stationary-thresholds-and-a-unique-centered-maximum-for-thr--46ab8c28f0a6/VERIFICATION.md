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

# Reproduction and verification

Run `python checker.py` from the extracted package directory. Python 3, SymPy and SciPy are required. The program verifies all nontrivial polynomial-matrix identities symbolically and checks the exact rational inequalities used to prove the strict global maximum. It also numerically evaluates Gaussian quadrature integrals for all nine matrix entries over seven thresholds, checks the differentiated formula, and computes the two nonzero positive critical values.

The rigorous infinite-set assertions rest on the proof in `RESULT.md`: Descartes' sign bound plus explicit intermediate sign changes prove the exact positive root count, the monotonicity of the transformed equation proves exactly two positive stationary thresholds, and exact rational Taylor bounds establish the global dominance of the center. A finite checker cannot establish those infinitary statements by sampling. No independent third-party validation or certification has occurred.
