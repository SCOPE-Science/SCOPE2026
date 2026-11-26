---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The fixed-point identity p[2i]=0, p[2i+1]=1−p[i] gives exactly the two parity images of every distinct half-length factor, at all starting positions. Both maps are injective; their intersection would require an all-zero image from an all-one preimage, impossible at half-length at least two. Starting from 00,01,10 gives 3N/2 distinct factors. At length 2 the two zero-count strata have endpoint census pairs (a,b)=(0,1),(1,0), for matrices [[a,b],[b,0]]. Doubling sends z to 2m−z and (a,b) to (2b,a+b); it interchanges the high and low strata, which remain floor(2m/3) and its successor. Substituting m=6q+2 or 6q+4 in the endpoint table verifies each induction transition exactly. With no 11 in an image, its number of ones is z, and the mixed-pair counts are (z,z−1), (z−1,z), or (z,z); the count of 00 is then fixed by length. The disjoint-image census gives the respective fiber sizes a+b,a+b,2b, all positive after the length-four preimage stage. Swapping the parity of the preimage exponent yields precisely the claimed odd/even multisets and the two linear asymptotics. Independently enumerating a prefix from the valuation formula for the letters and counting overlapping factors reproduced the spectra for k=3 through 10, including (170,171,171,341,341,342) at 1024. The full-length proof is the recursion, not the prefix experiment.

## originality

PASS

The number six of 2-Abelian classes at these lengths is already implied by the published complexity recurrences. The supported distinction is the full multiset of their distinct-factor cardinalities, which neither the strongest inspected literature nor the inspected catalogue overlaps supply for this word and equivalence relation.

## value

PASS

The exact cardinalities answer a distinct question from 2-Abelian complexity: how unevenly distinct factors occupy the six classes. The census distinguishes two linear size scales and exact parity corrections at every tested theorem length, and it gives the input for collision counts among distinct factors. Dyadic length is the natural self-similar scale of the binary substitution. This is a complete nontrivial invariant on that scale, not a recomputation of the six-class count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
