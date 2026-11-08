---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Read final RESULT.md and source verify programs. Substituting identities in the group RB law forces B(1)=1 and B(z) in {1,z} for the unique central involution z. The auxiliary group law g∘h=gB(g)hB(g)^(−1) makes B and C(g)=gB(g) homomorphisms, while its Q/Z projection agrees with ordinary multiplication. If B(z)=1, B descends from elementary abelian Q/Z and hence has central image χ; if B(z)=z, C descends similarly, yielding B(g)=g^(−1)χ(g). Each of four characters gives a valid map in each family; disjointness follows from B(z). Character orbits under Aut(Q8), duality, splitting subgroup obstruction and bijectivity are verified. Independent multiplication-table checks tested all eight maps on all 64 (g,h) pairs and confirmed images and duals, though not the full independent 8^7 enumeration claimed by the source.

## originality

PASS

Qualified best-of-knowledge originality: the exact final claim and implications were compared to the named primary statements and search results; known premises are credited, and unexamined relevant full text remains explicit in risks. No searched title or failed lookup alone was treated as proof of novelty.

## value

PASS

A complete exact small-prime group RB classification with dual bijectivity and splitting obstructions fills a naturally excluded Q8 case of odd-prime extraspecial results; these are nontrivial structural facts and a finite yet fully classified natural object, not merely a brute-force count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
