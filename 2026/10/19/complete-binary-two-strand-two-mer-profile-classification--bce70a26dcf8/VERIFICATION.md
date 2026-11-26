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

For a single word, r positive cross-transitions determine alternating runs; either (odd r) sign is possible, and duplicating zeros or ones supplies any split of L−r loops. Zero transitions instead give a constant word. For t=±2 the strand transition counts are both positive odd, so their sum fills the even interval 2 through twice the largest odd integer ≤L. For t=0 choose opposite odd signs over that same interval and, for the remaining top row when L is even, take two even counts L. For t=±1 the positive odd and positive even count ranges add to every odd s from 3 through 2L−1; at s=1 the choices of constant strand fill the two adjacent 00-count intervals [0,L−1] and [L,2L−1]. This includes L=1 where the s≥3 interval is empty. Each positive count on both strands gives the full possible loop-count interval. Summation yields 3+L²+2L(L+1)+2(L²−1_{L even}); the optimum selects one preimage per profile. An independent last-bit/histogram DP and pooled set computation checked full sets for n=2..16 (python3 /workspace/reviews/evidence/reproduce.py 3). This tests the finite instances, not the all-length proof.

## originality

PASS

The observation model and single-strand classification are prior; the pooled two-path feasible-set enumeration, including the excluded maximal-switch imbalances, is the distinct result. The bounded checks did not establish covering prior art.

## value

PASS

The minimal nontrivial reads in this established pooled channel pose a natural exact finite-length benchmark. The result gives both attainable observations and the maximal zero-error code size for every n; in particular the parity correction identifies a constraint hidden by asymptotic rates and by treating pooled counts as unrestricted compositions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
