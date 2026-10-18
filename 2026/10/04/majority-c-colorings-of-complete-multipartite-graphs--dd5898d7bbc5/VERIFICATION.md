---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. For any color class A of size A meeting parts I, a vertex in part i has A−a_i same-colored neighbors and N−n_i total, so 2(A−a_i)>=N−n_i. A color cannot appear only within one part since degrees >0; summing over |I|>=2 gives (|I|−1)A >= (|I|N−sum_{i in I}n_i)/2 >= (|I|−1)N/2. Every used color uses at least N/2 vertices; thus no three colors. With two colors, both classes N/2, equality forces full part support and 2a_i=n_i for every part. Therefore all n_i even; conversely balanced half-splitting gives equality at each vertex. Independent half choices give prod binomial(n_i,n_i/2), color swap acts freely giving half that count. r>=2, all n_i>=1 guard all degrees positive; finite all parts.

## originality

PASS

PASS, bounded best-of-knowledge. Bujtás–Dettlaff–Furmańczyk–Laskowska Observation 2(v) has the exact complete-bipartite parity case only and relates majority-C coloring to satisfactory partitions; the inspected full primary HTML does not list an arbitrary complete multipartite characterization or the class-count formula. Older satisfactory/friendly partition literature supplies balanced constructions (including Edmonds thesis Theorem 20 sufficiency for multipartite equal divisible parts) but no prior necessity for all parts, no cap of two arbitrary-color majority-C classes, or complete optimizer counts in the inspected material.

## value

PASS

PASS. This is a natural complete-class exact classification in an established graph-coloring variant, simultaneously characterizing feasible palettes and enumerating every optimal two-coloring. The half-splitting rigidity handles all numbers and unequal sizes of parts; despite an elementary proof, a reusable exact family classification is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
