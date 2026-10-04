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
The universal proof is independent of finite enumeration.

The critical structural checks are:

- nonidentity kernel conjugacy classes are free complement orbits of size \(m\);
- every nontrivial coset \(Kh^j\) is one conjugacy class because \(1-h^j\) is bijective on \(K\);
- kernel classes and outside classes separately form cliques in both the commuting and nilpotent graphs;
- a mixed pair cannot commute, and a mixed generated subgroup cannot be nilpotent because its coprime Hall factors would have to commute;
- the whole group is metabelian, so the solvable graph is complete.

The included verifier `artifacts/verify.py` constructs the scalar and split actions for \(p=7\) and \(p=13\). It enumerates all conjugacy classes and the full commuting-conjugacy-class adjacency relation, checks the predicted complete component sizes, verifies the mixed coprime-order noncommutation obstruction used for the nilpotent graph, confirms metabelianity, and counts invariant projective lines to distinguish the two semidirect products.

It returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
