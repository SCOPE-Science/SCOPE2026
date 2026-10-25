---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

At the stated compatible metric, only coded coordinates 0 and 1 exceed threshold 1/2. Under the explicit conjugacy x -> ((x_j,x_{j+d}))_j, a time n detects exactly differences in n+F_d with F_d={0,1,d,d+1}; singleton discrepancies show A winning iff A+F_d=Z. Any covered interval of N-d-1 interior sites requires at least (N-d-1)/4 observation times, uniformly in the interval start, establishing lower Banach density >=1/4. In every block I of length 2d+1, its last d sites J can be covered only by translates starting in I. Every triple of distinct offsets in F_d spans at least d, so each translate meets J in at most two sites, requiring at least ceil(d/2) observation times per block. This gives lower density >=ceil(d/2)/(2d+1). For even d, residues 0,2,...,d-2 modulo 2d cover all sites via the two adjacent pairs, density 1/4. For odd d, residues 0,2,...,d-1 modulo 2d+1 cover [0,d] and [d,2d], density (d+1)/(4d+2). Both are periodic schedules, so the stated uniform bounds are sharp. The d=1 overlap F_1={0,1,2} is handled by the odd-block argument; no false four-distinct-element count is used. This proves all integer d>=1 without numerical extrapolation.

## originality

PASS

The all-separation closed formula for the disconnected sensor shape F_d=(1+x)(1+x^d) is a specific uniform classification. Its reduction to integer translate covering is classical, and small contiguous-window cases d=1 and d=2 are subsumed by prior examples; those are not independently novel. Bollobás–Janson–Riordan supplies general optimal periodic covering/finite minimum-cycle-mean machinery (Theorem 5.1) but not a uniform symbolic even/odd law or the matching local certificate for this family in inspected Sections 5–7 and tables. Ferrari defines the same observation cost and a general witness-pattern obstruction, with exact contiguous-window full-shift examples. The accessible publisher introduction does not state the evaluated separated two-frame family, but full theorem sections could not be read; priority for an unindexed equivalent there remains a material residual risk. Li–Offner–Ye establishes minimum PACKING density for a different four-point set, which does not imply the claimed COVERING density. The self-indexed identical Resultary record was excluded as independent prior evidence. On actually inspected sources and statement-level implications, the uniform parity formula survives best-of-knowledge novelty; neither failed search nor limited full-text access is treated as proof of uniqueness.

## value

PASS

The set {0,1,d,d+1} is a natural two-sensor/two-consecutive-time observation geometry for a symbolic shift, not an arbitrary hand-picked four-site slice. Exact observation density matters because a schedule must distinguish every pair and a single-site discrepancy is adversarially decisive. The all-separation law gives a genuine phase-by-parity phenomenon: even gaps tile with rate 1/4 while odd gaps require a sharp penalty of 1/(8d+4), with both bounds constructively attained and a local obstruction explaining the difference. A finite catalogue or an existence algorithm alone does not provide this uniform structural explanation. The precise fact is plausibly useful as a benchmark for sparse observation, covering efficiency and metric-dependent symbolic dynamics. It is not asserted to solve arbitrary subshift observations or provide a conjugacy-invariant cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
