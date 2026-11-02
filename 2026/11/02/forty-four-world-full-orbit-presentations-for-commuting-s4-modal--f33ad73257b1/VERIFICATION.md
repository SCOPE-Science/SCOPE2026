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

The standalone `checker.py` implements exhaustive enumeration of all reflexive, antisymmetric, transitive relations through four worlds, all commuting ordered pairs, and all valuations of one proposition. It evaluates the three unary generators by a least-closed-set queue, without any formula-depth cutoff. It also validates the explicit four-world witness, all orbit-size counts, and the forty isomorphism orbits.

Execution produced `ALL_CHECKS_OK` with the four-world counts: 219 orders, 22735 commuting ordered pairs, 960 full-orbit triples, and 40 isomorphism classes. The finite exhaustive certificate proves the four-world counts conditional only on the transparently implemented definitions. The sharp minimal carrier size follows separately from a powerset cardinality bound and the witness. The proof does not establish historical priority or results for larger carrier sizes. Independent audit has not been performed.
