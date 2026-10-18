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

The attached `verify_mckinsey_rank.py` runs the actual Kripke clauses at every world and every full propositional valuation for the smaller instances, and uses the mathematically sufficient root/leaf evaluation for larger cases. The run completed with:

`PASS: 62 rank-one, 1099 graph, 1042 rank-three hypergraph instances; 410 marked connectivity reductions`

Every labelled singleton-edge hypergraph on 1–5 vertices was checked; every simple graph on 1–5 vertices was checked; every simple rank-three hypergraph on 3–5 vertices was checked. The construction reducing undirected reachability to graph nonbipartiteness was tested on all 410 marked graph cases having up to four input vertices, with independent connectivity calculations. The enumeration covers **all combinatorial instances within those sizes** but does not prove general complexity-completeness claims by experiment. The unrestricted reasoning is the mathematical proof in `RESULT.md`; independent verification or external audit has not been performed.
