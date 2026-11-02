---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For any faithful module, S_v=sum incoming arrow images is killed by outgoing arrows because J^2=0; each m_uv-dimensional arrow space acts through Hom(M_u/S_u,S_v), forcing t_u*s_v>=m_uv and nonzero active s_v,t_u. Nonzero vertex idempotents force dim M_v>=1, so objective is a lower bound (inactive outgoing quotient may be set zero for optimization). Conversely choose split spaces S_v^0 and T_v^0, with isolated one-dimensional spaces, and assign distinct matrix units from T_u^0 to S_v^0 to individual arrows; products of arrows are zero and all idempotents+arrows linearly independent, over every field incl F2. For m<=2 every doubled arrow requires upgrade of tail t_u or head s_v, giving a vertex-cover constraint and unit cost, minimized by bipartite König matching. Independently checked exact brute integer optimum vs matching for 12501 one-, two- and three-vertex multiplicity matrices (entries 0..2), and constructed K_rr examples through r=4; infinite/all-field proof is algebraic not empirical.

## originality

PASS

Best-of-knowledge exact field-independent minimum faithful degree optimization and its bipartite matching formula for m<=2, distinct from general module inequalities and derived-category correspondences. Strongest residual risk is an equivalent earlier separated-quiver embedding theorem under different terminology.

## value

PASS

Minimum faithful module dimension is a natural algebraic invariant measuring smallest unital matrix embedding. The all-field exact integer criterion and tractable matching formula for two-parallel-arrow quivers provide genuinely useful global structure and explicit quadratic-to-linear compression, not just restating representation-theoretic definitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
