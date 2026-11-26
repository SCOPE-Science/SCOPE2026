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

For each arrival, root adjacency is an independent Bernoulli with parameter 2/(t−1)−1/(t−1)². A rooted simple triangle requires exactly the two ordered choices for each distinct earlier root neighbour. This gives the conditional birth probability 2D/(t−1)², with no births from double edges. A birth forces a unit increase in D; averaging the future independent increments gives the exact two-arrival identity. For s<t its brace is bounded by a constant times (1+log t)², so summing the product of the two reciprocal-square factors on the quadrant gives O(log² N/N²). Countable Bonferroni thus replaces the expected number of post-cutoff births by their union probability at this cost. The q=t−1 harmonic expansion and integral from N of log(q)/q² give the displayed constant, including +4. Summability gives almost-sure finiteness and the positive leading tail gives the moment cutoff. The two convergent sums for the count are Euler's ζ(2,1)=ζ(3) and ζ(2,2)=3ζ(4)/4. Independent bounded code (audit_root_triangle.py) checked 32 marginals, 496 pairs and the union bounds by exact rationals for N=8 through M=40; this corroborates, but does not prove, the infinite theorem. The frozen standard-library-only description is inaccurate: verify.py lines 103–109 import SciPy and NumPy for the optional truncated numerical diagnostics; the exact finite checks and proof require neither. The frozen script was not executed.

## originality

PASS

Same-model studies of root inference and global cycle counts overlap the ingredients but did not establish the late-arrival law for the last root-marked simple triangle. The distinct claim is the two-term extreme tail and its moment boundary, not a novelty claim for Euler sums or global cycle counts.

## value

PASS

A natural root-local motif has finite expected total abundance but an infinite expected stabilization time. The sharp late-arrival law resolves that distinction in the canonical two-parent model and says precisely which time moments exist. It quantifies a root-inference-relevant phenomenon not visible in the usual global triangle counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
