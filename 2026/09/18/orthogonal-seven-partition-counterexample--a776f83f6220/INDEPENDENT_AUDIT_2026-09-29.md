# Independent Audit — 2026/09/18/orthogonal-seven-partition-counterexample--a776f83f6220

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `28db7302e88abb39c9f5a187a489f31eb5ee32ea`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite certificate was reconstructed independently from the 35 listed representatives and their negatives, without relying on the deposited verifier. The 70 points are distinct and no three are collinear. The projective critical set contains 2450 rays. Sampling every open chamber gives q=8 in 2351 chambers and q=9 in 99; exhaustive cutoff-tie enumeration on the critical rays gives {8} at 2331 rays, {9} at 79, and {8,9} at 40, with maximum cutoff tie size two. Since the exact reduction makes a weak orthogonal 7-partition equivalent to q=7, the displayed configuration is a valid counterexample. The reduction itself is consistent with the four sector counts (q,35-q,21+q,14-q), which equal (7,28,28,7) up to cyclic order exactly when q=7.

## Originality

**PASS** — Martínez-Sandoval's 15 September 2026 preprint gives a 96-point counterexample with target counts 8,8,40,40 and leaves the lower counterexample parameter as an explicit open problem. The present exact 70-point construction lowers that parameter to 7. Targeted searches for orthogonal 7-partitions and synonymous uneven perpendicular-line partition formulations found no earlier k=7 construction. Because the motivating preprint is only days older than the record, unindexed parallel work remains a material residual risk, but no covering prior theorem or certificate was located.

## Scientific value

**PASS** — The record directly resolves the first open parameter below the published k=8 example, lowering the known upper bound for the least counterexample parameter from 8 to 7. Its exact integer certificate is small enough to be independently reproduced and supplies a concrete benchmark for the unresolved k=2 through 6 cases.

## Sources

- Counterexamples and symmetry for uneven orthogonal mass partitions in the plane (Leonardo Martínez-Sandoval): https://arxiv.org/abs/2609.16757 — The source preprint exhibits a 96-point k=8 counterexample and motivates the lower-parameter question.

## Limitations

- The result does not determine whether counterexamples exist for k=2 through 6 or whether 70 points are minimal for k=7.
- The nonexistence proof is an exact exhaustive finite computation rather than a proof-assistant formalization.
- The source problem is extremely recent, so simultaneous or poorly indexed independent constructions remain a residual originality risk.

## Independent exact check

```json
{
  "implementation": "fresh integer-arithmetic projective-ray/chamber sweep reconstructed from the mathematical criterion",
  "points": 70,
  "critical_projective_rays": 2450,
  "open_q_counts": {
    "8": 2351,
    "9": 99
  },
  "critical_q_sets": {
    "8": 2331,
    "9": 79,
    "8,9": 40
  },
  "max_cutoff_tie": 2,
  "distinct_points": true,
  "no_three_collinear": true,
  "q7_absent": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this record.
