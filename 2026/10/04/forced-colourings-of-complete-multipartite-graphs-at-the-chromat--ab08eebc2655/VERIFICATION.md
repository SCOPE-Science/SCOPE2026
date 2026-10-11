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

A proper r-colouring of a complete r-partite graph must assign one distinct colour to each part. If at most r-2 parts are initially represented, no uncoloured vertex can see r-1 distinct neighbour colours, so no first force exists. If exactly r-1 parts are represented compatibly, every vertex in the missing part is forced to the unique unused colour, after which every remaining uncoloured vertex is forced; the all-r-parts case is immediate. For a fixed proper colouring, each seeded part contributes a nonempty subset and an unseeded part contributes the all-uncoloured state, giving the displayed product formulas without overcount because any forcing domain determines the unique missing colour. Fresh independent direct forcing enumeration on four representative multipartite types exactly matched the structural coefficient formulas.

## originality

PASS

Farr's primary paper defines exactly the iterative local rule, proves the two-colour connected-bipartite formula and lists small three-colour examples, but the inspected material contains no complete-multipartite theorem; a direct full-PDF text search found no occurrence of 'multipartite'. The audited theorem gives a structural iff and both an all-domain enumerator and probability polynomial for every complete r-partite graph at the chromatic palette size. Resultary returned nearby complete-multipartite colouring parameters but no implication-equivalent forced-colouring theorem.

## value

PASS

Complete multipartite graphs at their chromatic palette size are a canonical test family for a newly introduced forcing polynomial. The theorem gives the full forcing-set support and both exact enumerators for arbitrary part sizes, rather than an isolated small case, and cleanly extends the known two-colour boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
