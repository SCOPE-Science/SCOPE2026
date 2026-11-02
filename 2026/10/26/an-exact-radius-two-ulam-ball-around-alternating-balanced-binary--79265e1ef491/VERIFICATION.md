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

For a nonempty binary subsequence u, greedy earliest embedding in the alternating word 0101... consumes exactly |u|+e(u)+1_{u1=1} positions. Thus after exactly two deletions from a length 2m word, embeddability into w_m=(01)^m requires e(u)+1_{u1=1}<=2. One deletion can decrease equal-adjacency count by at most one, ruling out e(v)>=5. When e(v)=4 and initial bit is one, at most two deleted letters cannot both remove its initial run and the at least two further equalities needed; hence impossible. Conversely deleting nonfirst letters from repeated runs twice reduces e by two while preserving first bit (and the e<=1 cases embed after at most one appropriate deletion), yielding membership exactly e<=3 or e=4 with first zero. Balanced constant-run compositions enumerate k=0..3 as 2,2(m-1),2(m-1)^2,(m-1)^2(m-2); qualifying k=4 contributes C(m-1,2)^2, summing to (m^4-2m^3+5m^2+4)/4, m>=1. Independent dynamic-programming LCS enumeration of all 2^(2m) binary words for m=1..6 verifies the membership and balanced counts 2,6,19,53,126,262. The proof, not enumeration, handles all m.

## originality

PASS

The full original 2026 Fleischmann et al. arXiv HTML text defines jumbled neighborhoods via LCS and proves the general upper bound C(n,l)^2 l!, not the alternating-center radius-two exact membership criterion or composition-specific quartic. Kong–Hagiwara 2017 and Kong 2017/2019 concern arbitrary-center radius-one and sorted-center arbitrary-radius Ulam spheres; alternating center is not a sorted center for m>1. The indexed other binary reconstruction/RLCS records address different invariants. Best-of-knowledge PASS with possible unindexed alternating-string special cases.

## value

PASS

An alternating balanced word is a canonical maximally switching constant-composition center in deletion/translocation coding. Its exact radius-two Ulam/jumble ball size is a natural local metric-volume invariant relevant to coding bounds and neighborhood growth. The unexpectedly simple universal e(v) adjacency criterion also describes unrestricted-composition membership, giving a structural result beyond the quartic count. The theorem does not claim extremality among all centers or arbitrary-radius classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
