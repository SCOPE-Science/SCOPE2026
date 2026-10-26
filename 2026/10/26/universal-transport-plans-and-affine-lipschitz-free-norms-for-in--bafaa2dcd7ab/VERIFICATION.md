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
# Reproducibility and limits

The exact formula is proved for arbitrary real, total-mass-zero vectors and arbitrary finite partitions by the full analytic argument in `RESULT.md`. The crucial unrestricted steps are: uniqueness of a positive cluster-overload deficit; fractional Hall feasibility of cross-part transport when there is no overload; an explicit cross-plus-internal routing when there is overload; and exact one-Lipschitz potentials realizing the resulting cost lower bound. All range endpoints, singleton parts and the zero vector are addressed in the proof.

To independently check finitely many examples using only the Python standard library, run `python3 check_transport.py`. Its observed final line is:

`MULTIPARTITE_TRANSPORT_EXACT_OK cases=745 norm_affinity_checks=745`

The checker constructs positive and negative unit transport tokens, enumerates all couplings as permutations, computes their costs with rational arithmetic, and tests the formula and affine midpoint identity for five heterogeneous metric configurations and 745 zero-mass vectors. It does **not** exhaust all finite partitions, real measures or cost parameters. No full mathematical proof or independent validation is inferred from a finite experiment.

No independent mathematical audit has been performed. Optimal-plan uniqueness is not asserted. The result does not cover weighted cross edges, variable distances within one cluster or Wasserstein exponents other than one.
