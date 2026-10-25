---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The two equivalence relations each with two-element classes and singleton intersections define a simple bipartite incidence graph whose E- and F-class vertices each have degree two. Every component is an even alternating cycle with 2k edges (k>=2). Isomorphism types at n=2t correspond exactly to partitions of t into parts >=2, count p(t)-p(t-1). Joint E,F atomic neighbourhood counts at every x equal (1,1,1,n-3) so 1-WL remains uniform; explicit C² sentences enforce n, both class-size-two conditions and |E(x)cap F(x)|=1, making the fibre exact relative to arbitrary pairs of equivalences. Side-preserving automorphisms are edge-transitive within each cycle length and can permute like components; vertex-orbit count equals number distinct partition parts. First unequal sizes (2,3) at t=5 yields n=10 orbit sizes 4,6. Distinct-part minimal weight d(d+3)/2 gives sharp D(n)=floor((sqrt(4n+9)-3)/2) with constructive extremizers. Independent partition enumeration through t=27 plus inspected side-coloured graph isomorphism and first-orbit automorphism scripts support boundaries without substituting for proof.

## originality

PASS

Classical correspondence of C² with 1-WL on finite relational structures and general identification criteria are known. The new statement is an explicit *whole* equivalence fibre for each even size, indexed and counted by restricted partitions, plus exact automorphism-orbit spectrum and sharp first split. Previously known eight-point non-isomorphic cases are credited.

## value

PASS

Pairs of named size-two equivalences are the minimal regular relational structure where 1-WL/C² cannot recover global connectivity. The theorem determines the entire logical ambiguity fibre at every admissible size, the exact first nonautomorphic split at ten points, and the maximal number of hidden orbit types, useful concrete boundary data in finite-model identification. Natural full classification, not an arbitrary graph slice or mere known partition table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
