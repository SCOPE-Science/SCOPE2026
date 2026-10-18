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

Independently formed all 64 distinct exact length-four descendant sets by survivor-coordinate enumeration and the 522-edge compatibility graph. Independent NetworkX maximal-clique enumeration gave 217 maximal 2-cliques, 276 maximal 3-cliques and exactly 16 maximal 4-cliques, none larger. Intersecting maxima yields 000000,111111; the other two words in every maximum have weight three. Exact descendant-set inclusion tests give three nondominant (basic) maxima; reversal and complement give seven all-optimum orbits of sizes 1,1,2,2,2,4,4 and two basic orbits. This finite exhaustive graph calculation proves precisely the bounded parameter, not any all-length assertion.

## originality

PASS

Kolev explicitly motivates classification of distinct optimal codes and basic maxima, but the inspected paper does not enumerate the binary (6,2) equality cases. Weindel–Heckel give the related same-parameter conflict graph (1,494 edges, complementary to these 522) and code-size results for other lengths, not the 16 equality cases or the dominance/orbit census. Genuine priority risk remains for Landjev–Haralambiev (2007) full text.

## value

PASS

The complete small-parameter equality-case and nondominant-basic census answers a natural concrete instance of a recognized deletion-code classification problem, not merely a nonsharp numerical upper bound. Precise optimal codebooks and orbit representatives are independently useful finite coding invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
