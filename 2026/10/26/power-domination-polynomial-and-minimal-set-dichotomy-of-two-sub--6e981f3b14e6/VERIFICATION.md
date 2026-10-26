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

# Verification evidence

Run `python verify_power_kneser.py` with Python 3 and its standard library. The script implements the original graph-neighborhood power-domination rule and independently computes the theorem's predictions. The included `verify_power_kneser_output.json` is its actual recorded output.

All subsets were exhaustively checked for \(n=5,6,7\), totaling \(2^{10}+2^{15}+2^{21}\) cases. All subsets through size four were checked for \(n=8,9\), and through size three for \(n=10,11\). Every predicted large minimal star was checked for \(n=8,\ldots,13\) along with every single-vertex deletion; seeded random subsets supplied broader non-exhaustive checks. The recorded total is 2,278,600 checked selections/configurations, and all tests passed.

The infinite-parameter correctness guarantee is the combinatorial proof in `RESULT.md`, not an extrapolation of finite tests. Independent audit has not been performed.
