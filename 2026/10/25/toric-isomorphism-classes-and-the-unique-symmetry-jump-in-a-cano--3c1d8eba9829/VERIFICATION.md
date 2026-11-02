---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For every integer a,b, the source fan has eight primitive rays and twelve listed maximal cones. Every toric isomorphism gives a ray permutation preserving these twelve triples; full enumeration of all 8! permutations yields exactly eight candidates. Rays 1,2,4 form an integral unimodular basis, so the unique forced lattice matrix for each candidate is obtained from their images. Independent symbolic Gröbner elimination of all 24 ray-coordinate constraints gives the unit ideal for six candidates and only a−b=0 (identity) or a+b+4=0 (nonidentity). The explicit matrix U_a=[[-1,0,0],[-a−2,0,−1],[-a−2,−1,0]] has determinant +1, sends the rays as required and obeys U_{−a−4}U_a=I. Hence toric isomorphism iff b=a or -a-4, with unique parameter representative a≥−2, and exactly at a=−2 a second fan automorphism. This classifies only toric isomorphisms and fan-preserving lattice maps, not abstract automorphisms.

## originality

PASS

The exact classification of lattice-fan equivalences among the Z''13(a,2,a+2,a+1) specialization is a more refined question than the prior discovery of its nonprojective tensor-generating property. The highly relevant four-parameter fan description in Fujino–Sato supplies the data but not the two-way parameter equivalence or unique special fan symmetry. Ito–Zeng–Zeng's October 2026 primary full PDF could not be retrieved through OA/arXiv; the authorized institutional downloader returned vpn_disconnected, so no paper-wide exclusion can be claimed for it. Accessible statements indicate a family construction, not a pairwise equivalence theorem. The numerical/parameter alias is matched to fan isomorphism up to GL3(Z), not to title wording; residual risk explicitly retained.

## value

PASS

A one-parameter family used to exhibit a geometric property does not establish an infinite collection of distinct toric classes. Classifying exactly its parameter redundancies and unique lattice symmetry jump is a natural structural question; this supplies canonical a≥−2 representatives and a genuine exceptional automorphism at a=−2. No claim about full abstract automorphism groups or tensor-generation novelty is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
