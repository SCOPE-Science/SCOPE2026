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

For a full-systematic E:S_n→S_{n+r}, standardizing after deletion gives one of n! outcomes when r=1. Disjoint decks for n! messages would force every selected word to have exactly one descendant. Two adjacent deletions agree exactly when their neighboring values are consecutive; equality along all positions makes the word a Hamiltonian path in 1–...–(n+1), necessarily monotone, so just two singleton-deck words exist. Thus n!>2 forbids r=1 for n≥3; r=0 has (n-1)! outputs for n! messages. The explicit n=2 encoder and n=3,4 codebooks were read from the actual codebooks.json at Git blob a1a19606711ac3f9d281d06e2da01dafb4cf6f59 and independently exhaustively checked for full messages, standardized descendant disjointness and deck totals 18 (six n=3 words) and 90 (24 n=4 words). This proves only r(2)=1, r(3)=r(4)=2, and r(n)≥2 for n≥3, not a general two-marker construction.

## originality

PASS

Best-of-knowledge mathematical statement-and-implication comparison of the exact reviewed final theorem with relevant primary literature, published-record searches, and recognized prior ingredients. Search failure is not novelty proof; priority risks remain specified.

## value

PASS

The minimum number of full-systematic redundancy markers for a single standardized-label deletion is a natural engineering and extremal coding invariant, distinct from label-preserving deletion. Finding the first nontrivial exact cases n=3,4 and explicit optimal codes addresses a concrete coding-design gap; the general one-marker impossibility supplies a meaningful all-length obstruction. A complete finite codebook is a legitimate result here, not an arbitrary slice of a tabulation; it should not be misrepresented as an arbitrary-n construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
