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
# Reproduction and limits

The mathematical theorem is proven for every integer \(d\ge3\) and positive integers \(\alpha,\beta\) in the fixed orthogonal embedding. Execute `python3 check.py` in the directory containing the code. Python's standard-library `fractions.Fraction` verifies each stated equality and strict contact inequality at every vertex for \(3\le d\le10\), \(1\le\alpha,\beta\le7\), yielding 107,408 exact assertions and 105,056 vertex comparisons. With NumPy and SciPy available, the optional independent numerical SLSQP comparison verifies 66 epigraph minimax problems for the same four vertex-orbit distance functions, without using the proposed radius formula in its objective. These finite computations are corroboration, not proof of all parameter cases.

The proof's infinite-domain steps are the symmetry reduction, the exact orbit-mean minimax lemma, the strict endpoint-screening bounds, the cube-affinity argument, and the discriminant-based dimension threshold. The only independent audit status represented here is `not_performed`; no outside certification or priority assertion is made.
