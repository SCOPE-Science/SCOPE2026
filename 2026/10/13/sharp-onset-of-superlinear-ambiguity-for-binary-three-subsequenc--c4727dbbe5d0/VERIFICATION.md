---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n=3,...,16 the eight-component scattered length-three deck is enumerated for all 2^n distinct labeled binary words, not sampled. The append recurrence C_{abt}+=B_{ab}, B_{at}+=A_a, A_t++ has a bijection with all scattered increasing triples. Independently written exhaustive enumeration reproduced max fiber sizes (1,1,1,1,2,2,3,3,4,4,6,10,14,20), 36,649 different n=16 decks, and the full 16-length fiber histogram, totaling 65,536 words. The exactly two size-20 spectra are (56,85,82,85,57,82,57,56) and (56,57,82,57,85,82,85,56); independently recomputed those spectra by direct triple iteration on all forty maximal words. At n<=15 every maximum <=n, while at 16 maximum=20>16. This proves only the stated finite threshold, not any behavior at n>=17.

## originality

PASS

The directly relevant k-binomial-equivalence literature discusses class-count complexity and algorithms, and the enumerated D_3(16)=36649 count is already known. A class-count total does not determine individual preimage multiplicities: many histograms sum to 36,649. The inspected finite-word class paper treats mostly binary k=2, whereas the contribution here is the exact k=3 multiplicity histogram, two maximizers and first superlinear threshold. No broader published table giving these exact values was located in the inspected materials; earlier unindexed computations remain possible.

## value

PASS

The number of distinct words compatible with a given subsequence deck is a natural reconstruction ambiguity and inverse-list parameter. Its maximum, first superlinear length, and complete first extremal histogram answer specific finite combinatorial questions relevant to binomial-equivalence classes; these are not arbitrary chosen outputs or just a re-tabulation of the distinct-deck count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
