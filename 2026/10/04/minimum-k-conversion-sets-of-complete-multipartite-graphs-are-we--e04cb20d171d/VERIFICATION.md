---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every deficient vertex has degree below \(k\) and is forced into any seed set. In the nontrivial case \(d<k\), a minimum set has exactly \(k\) seeds. Before an incomplete part \(i\) activates, one of its unseeded vertices sees exactly \(k-s_i+U\) active neighbours, where \(U\) is the accumulated number of newly activated vertices outside that part; hence activation is exactly \(U\ge s_i\). Sorting incomplete parts by \(s_i\) turns the dynamics into the stated greedy parking recurrence, proving necessity and sufficiency. The binomial count then follows independently within parts. The bundled exhaustive program checks the literal dynamics through order eight but is not used as the infinite proof.

## originality

PASS

The prior complete-multipartite theorem gives the scalar optimum \(\max\{|X|,k\}\) and constructs one optimum, but its inspected theorem section does not classify every optimum seed placement or enumerate them. The audited weighted-parking inequalities give a necessary-and-sufficient profile test and exact binomial count. Resultary returned the assigned theorem as the direct hit and no stronger published target-set theorem covering the all-minimum-set refinement.

## value

PASS

Minimum cardinality alone leaves a genuine intervention-design ambiguity because optimum-size placements can fail. The theorem resolves that ambiguity completely on a canonical dense family, supplies a fast membership test and counts all optimal placements exactly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
