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

The universal theorem is analytic. The bundled `verify.py` supplies a finite cross-check that does not invoke the proof's threshold lemma when evaluating a subset: it explicitly constructs each complete multipartite graph, tests whether every outside vertex has a neighbor in the candidate set, and counts each selected vertex's outside neighbors.

The exhaustive range is every complete-multipartite isomorphism type of order \(3\) through \(11\), with every integer \(k\) satisfying \(1\le k<\Delta(G)\). For each parameter case, every vertex subset is inspected and the minimum feasible size is compared with the theorem. Additional checks compare the general formula with the published complete-bipartite formula and with the balanced closed form.

This finite computation cannot establish the universal theorem by itself; it is a stress test for definitions, boundary cases, and algebra. The proof in `RESULT.md` is the evidence for all graph orders.

Run with:

`python3 verify.py`
