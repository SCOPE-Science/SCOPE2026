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

# Exact reproducibility and limits

Invoke `python3 frucht_two_independence_verify.py` with Python 3 (standard library only). It constructs the 18-edge Frucht graph and checks its standard LCF isomorphism, enumerates all 824 nonempty faces, then runs complete element matchings on the full complex and each of twelve vertex deletions. For every complex, it checks acyclicity by topological sorting the *complete* directed Hasse diagram, and checks the exact integral signed four-to-three Morse boundary. For each inclusion, it constructs integral three-cycles, reduces them into the full complex's degree-three Morse model, and checks zero versus surjective images. As a separate algebraic cross-check, it builds mod-two boundary matrices for all thirteen original simplicial chain complexes, checks every reduced Betti number, and computes each inclusion image using direct kernel/image linear algebra; these independent mod-two calculations are corroboration, not the integral proof.

Representative expected totals: full face count 824, full matching pairs 410, full signed Morse differential row (0,1), and deletion-eight row (0,1). The final output is `PASS: acyclic matchings, integral incidence and inclusion maps, and independent F2 chain matrices for all 13 complexes`.

This is a complete, finite, deterministic mathematical computation. It does not establish an infinite-family theorem or the full homotopy classes of inclusion maps. The named findings have not undergone independent external scientific audit.
