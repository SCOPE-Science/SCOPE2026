---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Under the precise definition of even binary length-2n words and complementary ordered length-n subsequences U,V with V=πU, for n=2..6 cyclic shifts k=0..floor(n/2) cover ALL 2^(2n-1) even words, proved by a finite exhaustive upper certificate. For lower bounds, exhausting every permutation and subsequence partition yields best one-permutation covers 6/8,28/32 at n=2,3 and best two-permutation unions 126/128,496/512 at n=4,5. At n=6 the given nine-word obstruction generates 73 distinct coverage signatures from all 720 permutations and all 924 partitions; a complete 9-bit superset DP rules out every triple of signatures. Thus m2(2..6)=(2,2,3,3,4), with no assumption that lower-bound competitors are cyclic. Independent fresh exhaustive enumeration regenerated signatures, rotation coverage for 8,32,128,512,2048 words and nine-word obstruction; a subset witness is sufficient for the lower bound, not a mistaken all-word enumeration.

## originality

PASS

Best-of-knowledge original narrow result after comparing actual mathematical implications with primary source and adjacent literature: Theorem 2 upper construction and Proposition 2 m2(2)=2 are prior; new n3..n6 lower certificates concern free choice of permutations. Papers on ordinary shuffle squares are not equivalent to minimum covering across π.

## value

PASS

The precise m_k(n) family is introduced as a natural minimal-permutation covering invariant in the original shuffle-square paper. Closing the first five binary values with explicit finite optimality certificates and locating the first order requiring four shifts is a motivated finite cutoff rather than a gratuitous small computation. It does not purport to settle all n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
