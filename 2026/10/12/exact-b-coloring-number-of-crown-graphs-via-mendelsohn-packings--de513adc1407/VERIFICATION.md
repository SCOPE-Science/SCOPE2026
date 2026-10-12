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

The proof has two layers. The local crown-graph lemma is elementary and reconstructed in `RESULT.md`: same-colored crown edges map to pairwise composable arcs, so a color class has size at most three and a three-edge class is a directed three-cycle. The global existence layer uses the classical maximum-packing theorem for Mendelsohn triples, including the exceptional nonexistence of a system of order six and the directed two-cycle leave in the order-two modulo three case.

`verify.py` supplies finite stress tests independent of the symbolic proof. It enumerates every edge subset of size at most four for crown orders four through six and checks the structural classification directly from the B-coloring definition. It verifies explicit optimal constructions for orders four through eight. It also runs an exact-cover search over all directed three-cycles of the loopless complete digraph on six points and confirms that no full decomposition exists.

The finite search is not an exhaustive proof for all orders. The infinite construction step is exactly where the cited Mendelsohn packing theorem is used. No independent audit has been performed.
