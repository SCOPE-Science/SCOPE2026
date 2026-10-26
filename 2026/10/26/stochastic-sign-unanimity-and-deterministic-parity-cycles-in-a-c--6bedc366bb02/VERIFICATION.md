---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The supplied `verify.py` runs with Python 3 and no additional packages. It checks exact rational deterministic parity-window classifications at sizes 2--8, and, for each size 2, 3, 4, 7 and 15, 100 reproducible independent-uniform sample paths. On every simulated update it checks the average-increment identity and verifies the source's delayed confidence-eligibility test using the previous expressed opinions. All tested trajectories reach strict sign unanimity; largest observed hitting step and maximum confidence gap are printed by the program.

Finite sample-path checks do not establish almost-sure absorption, the infinite-time velocity, or the geometric tail. Those claims are established by an invariant high-confidence bound, a conditional 12-step event minorization, and the strong law of large numbers. The tail constant is an analytically sufficient bound rather than a measured estimate. Deterministic constant-amplitude two-cycles are compared as a distinct (nonrandom) amplitude rule, not as positive-probability realizations of continuous uniform noise.
