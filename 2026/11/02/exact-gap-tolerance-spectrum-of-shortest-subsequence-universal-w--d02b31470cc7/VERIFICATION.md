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

The shortest length is qk: constant targets require k copies of each label, and k permutation blocks suffice. For necessity, cut greedily at the first full-alphabet prefix of each remaining suffix. The sequence of last-to-appear symbols forces any embedding of that sequence to reach at least the corresponding cuts; if there are fewer than k cuts, appending a symbol missing in the remainder obstructs universality. At length qk this forces k blocks of length q. Each constant target has a unique embedding, so all forward displacements are witnessed as jumps q+p_(i+1)(a)-p_i(a). Conversely, earliest-match embedding starts in the first block and advances at most one block per match. For a cross-block step to b from offset r, p_i(b)≤r, so the jump is no larger than the corresponding constant-target jump. Same-block jumps are below q and the maximal forward displacement is nonnegative by summing over labels. For a fixed block the nested allowed new positions give d+1 choices on each of the first q−d rows and d! choices on the remainder; the count is the same from every block. Subtraction gives the exact spectrum, d=0 forces repeated permutations, and the ratio at d=q−2 to unrestricted choices is (q−1)/q per transition. These are maximum index differences, not skipped-position counts, and each target may choose its embedding.

## originality

PASS

Pass for the bottleneck-radius bridge and the resulting distribution on all indexed shortest hosts, not for arch factorization, permutation-block structure, or the restricted-permutation count. No inspected strong match gave or implied this bridge. Same-day matches were compared without inferring publication order.

## value

PASS

The worst-target best-embedding problem appears to require testing q^k targets and choices of embeddings. The exact witness-and-greedy bridge reduces it to linear scanning of adjacent blocks, and yields the entire labeled-host spectrum and sharp extremizers, rather than an example, a sampling estimate, or only a decision bound. Minimum length is the natural rigidity regime for this question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
