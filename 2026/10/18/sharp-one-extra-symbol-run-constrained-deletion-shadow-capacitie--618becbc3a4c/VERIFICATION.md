---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The last-occurrence recurrence subtracts exactly the subsequences ending in the appended symbol that one can already embed using its most recent old occurrence. For cyclic run labels, repeats of physical spacing q contribute one loss each at degree q, the adjacent duplicate contributes z(1+z)^(r-1) through that degree, and repeats spanning the insertion with spacing q+1 contribute nothing through degree q. The left and right counts are (j-q)_+ and (r-j-q+1)_+, and their sum is minimized precisely between q and r-q+1 inclusive, in either endpoint order. The cited cyclic-label reduction applies to fixed run lengths. Independently, a direct upper bound avoids this citation: count leftmost greedy embeddings by discarding all deletion sets that remove the first copy but retain the second copy of the doubled letter. This discards binom(r-1,t-1). At t=q, split the word into the prefix ending at the first copy and the suffix starting at the second. Every (q+1)-window in either stretch contains a repeated letter. Delete the whole window except the later occurrence of such a pair; that retention is not leftmost. Each set contains the window start as its least deleted index, so the sets from different windows are distinct. The only possible overlap with the baseline is the prefix window ending at the first copy when that copy is deleted. In this case swap its deletion to the second copy; the earlier repeat still witnesses non-greediness, the least deleted index is unchanged, and the new set is no longer a baseline deletion. This gives exactly the needed lower bound on losses for every j. The cyclic construction attains the bound by the recurrence. The supplied finite checker was inspected as corroboration only. The statement about positions classifies cyclic maximizers, not all maximizing words.

## originality

PASS

The supported distinct contribution is the exact loss and position law at t=q. The t<q formula is a baseline, explicitly covered by a broader later Resultary theorem and not credited as a distinct contribution here. The closest inspected collision thresholds, general upper bounds and counting recurrences do not supply the t=q global maximum and position profile. This is a best-of-knowledge comparison, not a priority certificate.

## value

PASS

The first nondivisible length and first alphabet-size deletion order form a natural boundary: the collision-free run-pattern bound ceases to describe the answer uniformly over positions. Resolving the exact loss for every alphabet and both end versus interior placements is useful beyond recomputing the known short-deletion baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
