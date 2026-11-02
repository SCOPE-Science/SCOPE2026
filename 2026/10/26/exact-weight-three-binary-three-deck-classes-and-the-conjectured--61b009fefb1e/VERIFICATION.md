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

For ones at a<b<c, directly counted X_011=2a+b-1, X_110=3n-b-2c-4, X_001=C(a,2)+C(b-1,2)+C(c-2,2). These three statistics determine the other five scattered triple multiplicities using the fixed number of zeros and the first two power sums of zeros preceding each one. Equal decks imply (a,b,c) maps to (a+s,b-2s,c+s); equality of X_001 gives s(3s-(b-a-(c-b)))=0, so there is at most one nontrivial partner and it swaps the two inter-one gaps. Orient x>y to count each pair exactly once; admissible starting positions are 0<=a<=n-1-2y-4s, giving max(0,n-2y-4s) pairs. Summing the finite-at-each-coefficient geometric generating functions proves the rational all-length identity, including n<3 and n<7 boundaries. Independently enumerated all length-three decks for all weight-three words at n=3..17, checked every deck class size and exact collision count.

## originality

PASS

Chrisnata et al. Section 5.3 Conjecture 1 explicitly gives precisely the proposed rational generating function only as a conjecture, with 20 coefficients verified; the source’s Theorem 27 gives a lower bound and the first collision is known. The present quadratic collision argument proves all lengths and class sizes. General k-deck papers and unrelated deletions are not equivalent.

## value

PASS

This proves an explicit published enumeration conjecture for a natural scattered-subsequence reconstruction channel and gives the complete fibre classification rather than another finite census. The exact all-blocklength codebook count can be used in subsequent fixed-composition reconstruction bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
