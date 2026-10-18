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

# Verification

Run `python3 verify.py` with the standard Python 3 library. The file checks \(1972\) exact rational equalities or inequalities. In particular, the covariance-numerator factorizations for the three-terminal and noncrossing four-terminal cases, together with the four-terminal crossing Bernstein expansion, are checked at all coordinates in \(\{0,1/2,1\}\). Since each expression has degree at most two separately in each parameter, equality on this grid proves the underlying polynomial identity by interpolation. The Bernstein coefficients are nonnegative, and their basis functions are nonnegative on the unit interval.

The program additionally enumerates all spanning forests of single cycles with three to seven vertices, a two-cycle cactus and a three-cycle cactus with a bridge, using exact integer weights and testing all pairs of vertex-connectivity events. Those finite experiments are secondary consistency checks, not a substitute for the general proof. The general theorem is completed by the conditional-Bernoulli law, the block-cut path product, and blockwise independence established in `RESULT.md`.

No check is claimed for arbitrary overlapping-cycle graphs or random-cluster measures with positive \(q\). No external or independent audit has been performed.
