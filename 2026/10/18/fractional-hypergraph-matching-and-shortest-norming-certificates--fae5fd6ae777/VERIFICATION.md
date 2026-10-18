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
# Verification of lattice-bottleneck fractional-matching formula

The file `verify.py` uses Python 3 standard library only and should be invoked with `python3 verify.py`. It computes finite **exact rational** hypergraph fractional-matching primal/dual certificates and independently constructs test vectors in their \(p\)-power coordinates to match the variational lattice norm.

The resulting completed execution reported `PASS: 1098 small graph primal-dual equalities; 84 parametric exact certificates.` The graph component enumerates all labeled graphs on two through five vertices; the other cases cover complete graphs, cycles, stars, complete uniform hypergraphs and the seven-line Fano plane. The test also checks nonnegativity, coordinate incidence capacities, vertex-cover inequalities, equality of primal and dual objectives, and equality of the test-family value with that objective.

The complete proof in `RESULT.md` is analytic and covers **all** finite nonempty hypergraphs and real exponents \(1\le p<\infty\). The finite experiment does not by itself establish any all-size conclusion or exclude equivalent prior statements. The published norm model is a stated prior mathematical input, not a new lemma. Independent audit and validation have not been performed.
