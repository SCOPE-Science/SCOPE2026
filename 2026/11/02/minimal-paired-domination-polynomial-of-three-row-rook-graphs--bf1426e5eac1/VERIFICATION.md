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

The replacement at /workspace/repairs/1/RESULT.md corrects a counting error in the original proof sentence: once the doubled row's two columns are fixed, the distinct-column singleton placement has 2 assignments, not n(n-1). The latter is the count of such placements across all doubled-row column pairs, for a fixed doubled row. The original displayed polynomial was correct and is unchanged. For the final proof, domination is equivalent to occupying all rows or all columns. In the all-row case, at most three edges of a perfect matching already cover every row, so a minimal set has size four or six. No pair dominates. At size four a common singleton column allows an internal matching for the doubled row and one vertical pair. Distinct singleton columns require two vertical pairs; this gives n+2 possibilities after the doubled row and its column pair have been fixed. At size six any vertical edge in a perfect matching would give a four-vertex witness with another matching edge meeting the third row. Thus row counts are (2,2,2); any shared column would give a smaller paired set via the vertical edge and the third row's pair. Distinct columns suffice for minimality: no proper subset can cover all columns, and all-row coverage with a matching requires both cells in each row. In the empty-row case all columns are occupied. If two doubled columns exist, deleting from the same row (both row occupancies even) or from opposite rows (both odd) keeps full column coverage and makes row counts even, giving a proper paired subset. Hence the number of doubled columns is zero for even n and one for odd n. The parity counts and one-row double-count correction give 3(2^(n-1)-1) at even n; one doubled column gives 3n*2^(n-1) at odd n, with a vertical pair used just when both row counts are odd. These sets are minimal by column coverage and parity. The support at n=3,4,5,6 follows by merging coincident degrees; for n>=7 all three degrees occur. Independent finite replay: python3 /workspace/branches/rook_independent.py checks all 2,396,667 nonempty subsets for n=3..7 using direct neighborhood unions, a matching recurrence and proper-subset detection. Paired outputs by increasing degree are (81), (129), (210,240), (360,183), (567,630,1344); the frozen verifier was read, not executed. The finite check supports, but does not certify, the all-order proof. The corrected proof, unchanged claim and updated source comparison were re-audited; no supporting script or verification notes required a replacement.

## originality

PASS

The repaired submission credits the closest family-wide enumerator for all paired-dominating sets and the overlap at minimum size. The supported distinct claim is the full inclusion-minimal distribution on three-row rook graphs, including the higher-degree layers and the exact size gaps. No inspected source gives that classification or implies it by direct specialization. This is a bounded statement-level comparison, not publication-priority certification.

## value

PASS

Three rows are a natural next case beyond complete prisms and yield a nontrivial interaction between row/column coverage and induced matching. The exact classification distinguishes minimum and upper cardinality from the intervening support, proving that arbitrarily many even sizes are missing within a connected highly symmetric family. The all-set spectrum and general upper bounds do not answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
