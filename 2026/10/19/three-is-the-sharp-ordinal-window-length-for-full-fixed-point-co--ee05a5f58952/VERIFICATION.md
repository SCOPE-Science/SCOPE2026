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

# Computation and analytic verification

The full rank and covariance theorem is proved in `RESULT.md` by conditioning on a labeled fixed point, hypergeometric set counting, an exact adjacent-difference determinant, and row-span inclusion. The standalone `verify_patterns.py` uses Python 3's standard library and exact `fractions.Fraction` arithmetic.

Executed command: `python verify_patterns.py`.

Observed output: `PASS exact_covariance_cells=482297 rank_cases=41 determinant_cases=124251`.

The checker enumerated all permutations of size \(2\) through \(8\), including every local order pattern and every fixed-point coordinate. It separately computed ranks over rationals for \(k=1,2,3,4\) (as applicable) at all sizes \(2\) through \(12\), and verified the closed determinant with exact integers for \(3\le n\le500\). The infinite parameter range is justified by the symbolic proof, not the enumerations. These are same-model computations and do not constitute independent validation.

Scientific limits: uniform permutation law only; full column rank means covariance injectivity of the fixed-point linear span, not probabilistic independence, per-sample reconstruction, numerical conditioning, or distributional recovery.
