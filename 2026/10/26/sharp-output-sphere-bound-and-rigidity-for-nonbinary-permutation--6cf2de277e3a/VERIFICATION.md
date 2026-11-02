---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Each nonidentity output has a unique changed-support interval with length 2..k. Every endpoint-changing anagram of an interval is realizable by a containing length-k window since n>=k. Inclusion-exclusion for multinomial anagrams counts H(u) exactly. If a block repeats, H<=m!/2<c_m for m>=4, with direct m=2 and m=3 boundary checks; pairwise-distinct blocks attain c_m. Termwise strictness proves sharpness and iff rigidity, and q!/(q-k)! then q-k+1 choices at each extension give the exact population. Independent direct-output checks covered 12,176 words; finite tests are not the infinite proof.

## originality

PASS

Best-of-knowledge PASS: exact arbitrary-k nonbinary maximal output sphere and all-maximizer rigidity are not implied by accessible statements of Chen–Milenkovic (single-burst channel but redundancy/coding results), published limited-permutation covers, Ulam translocations, or the reported earlier k=3 specialization. The closest primary full article was not readable here; retain concrete priority risk rather than asserting noncoverage of the whole paper.

## value

PASS

The worst-case number of distinguishable outputs is a natural precise ambiguity invariant of the local permutation channel, including DNA-motivated q=k=4. The result gives a sharp closed formula, a full rigidity criterion and exact extremizer census simultaneously for arbitrary window lengths and input lengths, not a new decoder or code-size bound. These are substantive structural facts not mechanically implied by the accessible binary redundancy bounds or prior k=3 specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
