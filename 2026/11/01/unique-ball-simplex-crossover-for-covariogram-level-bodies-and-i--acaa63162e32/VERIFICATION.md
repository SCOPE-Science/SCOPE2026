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
The derivation checks the cap overlap formula by direct slicing, the continuity/strict monotonicity of the associated beta integral, the Brunn–Minkowski concavity of its level-set radii, and the endpoint derivative comparison for all integral dimensions at least two. Integration by parts proves the uniform Laplace expansion used in the high-dimensional limit.

The reproducibility program `CHECK.py` requires `scipy` as documented in `requirements.txt`. Executing it in Python from the directory containing the files produced `PASS 749 independent integration, derivative, transition and asymptotic comparisons`. Checks covered integral dimensions 2 through 20, additional dimensions 40, 80, 100, 200 and 500, independent cap quadrature, planar arccosines, inverse-beta crossover brackets and the asymptotic correction. The proof, not those finite checks, supports the infinite-dimensional-parameter assertions. Definitive historical priority and independent validation have not been established.
