---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For every m≥2 the ordered directed Hom face poset consists of compatible nonempty triples (A,B,C) with A→B→C→A. Projection to A lands in the complex N of subsets lying in an m-vertex cyclic interval; the unique enclosing minimal clockwise arc [s,t] determines exact common permitted B=[t+1,s+m] and C=[t-m,s-1] modulo 2m+1. The upper fiber contracts via (A,B,C)≥(S,B,C)≤(S,B∪{s+m},C)≥(S,{s+m},C)≤(S,{s+m},W), all terms valid because b*=s+m points to every allowed C. Quillen A dual gives |Hom|≃N. The length-m open arcs (i-m+1/2,i+1/2) form a good cover of the length-(2m+1) circle; their nonempty intersections are connected arcs containing integer points, with nerve N. Thus Hom≃S1 for all m≥2; m=1 has three points and is correctly excluded. Inspected complete verify_fibers.py and verify_chains.py; bounded m tests check identities only, not proof of the infinite family.

## originality

PASS

PASS (best knowledge): The nearest same-functor publication establishes the theory and unrelated cases; the indexed R9 result covers just one instance. The explicit all-m upper-fiber and good-cover argument supplies an unbounded family result not implied by those sources.

## value

PASS

PASS: Nontransitive regular cyclic tournaments are a canonical natural infinite family, directed triangle Hom complexes are motivated by the established reconfiguration/homotopy theory, and their dimensions grow with m. The uniform topological S1 classification and explicit contractible-fiber/nerve model resolve an open-looking family far beyond the known R9 instance; it is substantive, not an arbitrary finite benchmark or parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
