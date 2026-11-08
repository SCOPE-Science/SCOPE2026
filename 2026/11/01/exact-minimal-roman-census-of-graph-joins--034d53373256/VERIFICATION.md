---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For fixed support S of two-label defenders, pointwise-minimal Roman f is uniquely canonical: two on S, zero on outside neighbors of S, ones on undominated vertices. Each two needs a private zero neighbor dominated by no other two; otherwise a one-step downward change remains feasible. In G∨H, partition S as empty (one all-ones term), one shore only (old minimal RDFs plus singleton isolated defenders in that shore), or both shores (exactly one nonuniversal defender in each shore, every remaining vertex zero). The cases are disjoint, giving R_join=R_G+R_H-z^n-z^m+z^(n+m)+i(G)s z^(n+1)+i(H)s z^(m+1)+p(G)p(H)s² z^4, with K1 convention p(K1)=0 and i(K1)=1. Independent exhaustive enumeration of every graph on each shore for sizes one to three (121 graph pairs) and every 3-labeling directly tested feasibility and all coordinate decreases, matching every bivariate coefficient. Infinite graph identity is from support proof, not finite checks; union multiplication and join recurrence give coefficient computation on cotrees.

## originality

PASS

Abu-Khzam–Fernau–Mann 2022/2024 full text proves a general private-neighbor minimal RDF characterization and enumeration methods, but no arbitrary-join bivariate closed formula; Roman Census paper treats specific graph classes. Published SCOPE complete-multipartite polynomial counts all feasible Roman RDFs or different Roman-{2} variant, not pointwise-minimal assignments on arbitrary joins. The new unrestricted join composition identity is a stronger explicit classification but close to the earlier general characterization; plausible unindexed prior formula is the main priority risk.

## value

PASS

Complete two-variable composition law for arbitrary nonempty graph joins converts pointwise-minimal Roman enumeration into factor polynomials and simple isolate/nonuniversal counts, including exact mixed-defender correction. With disjoint-union multiplication it supplies an exact polynomial cotree recurrence for cographs, a naturally motivated counting gain beyond Roman domination numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
