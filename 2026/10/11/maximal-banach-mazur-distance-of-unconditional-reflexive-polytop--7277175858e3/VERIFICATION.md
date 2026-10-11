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
# Verification

The general proof is symbolic. Its critical checks are:

1. The perfect-graph representation gives exactly the clique inequalities needed to infer \(s=(q_{11},\ldots,q_{dd})\in P_G\) from any inscribed ellipsoid.
2. A convex decomposition of \(s\) into stable-set indicators makes the reciprocal-weight average exactly \(d\), so some stable set has reciprocal weight at least \(d\).
3. Averaging the outer ellipsoid inequality over signs on that stable set removes off-diagonal entries of \(Q^{-1}\).
4. Positive definiteness gives \(q_{ii}(Q^{-1})_{ii}\ge1\) coordinatewise.
5. The symmetric John theorem supplies the matching universal upper bound \(\sqrt d\).

The accompanying standard-library verifier exhaustively checks all labeled graphs through five vertices, directly identifies perfect graphs by testing \(\chi=\omega\) on every induced subgraph, and for each perfect graph tests two exact-rational positive-definite ellipsoid matrices, including a non-diagonal rank-one perturbation. It scales each ellipsoid by all signed clique constraints, then checks the reciprocal-diagonal lower bound and the actual maximum signed stable-set quadratic form.

Replay output:

`VERIFY_OK unconditional-reflexive BM lower bound perfect_graphs=1087 ellipsoid_cases=2174 n=1..5`

The replay is finite corroboration only. No finite enumeration is used to justify the theorem for arbitrary dimension.
