---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Independently cancelled the coboundary for V=log x+y/(1-a) on x>0: V(F)-V=(c-c*)/(1-a)-Phi(x/x*), Phi(u)=u-1-log u>=0 and x*=(1-a)/(1-a+b). Compact exact invariance F(K)=K gives bounded bi-infinite histories; below the fold a positive history would force V arbitrarily large backwards despite compact upper bound. The axis x=0 has only the one bounded entire affine orbit. On x>0, any point with sufficiently small x in the support of a compact invariant measure shrinks x by at least 1/2 forward forever, so is nonrecurrent; Poincare recurrence removes mass near x=0, justifying otherwise problematic integrability of log x. Integration yields exact expectation. At equality, Phi=0 forces x=x* and the x equation forces y=x*-log x*. Nonzero x>0 component plus the invariant axis exhaust invariant probability support (no negative x has invariant mass). The concentration bound follows from convex defect monotonicity and Markov. Equilibrium fold is verified from strictly convex qx-t log x, but known prior art.

## originality

PASS

Chialvo 1993/1995 explicitly establishes the positive-equilibrium fold and stable quiescent states; neither the inspected exact model/fold and phase-plane sections nor the 2023 finite-resolution parameter study gives the exact global compact two-sided recurrence obstruction and all-compact-stationary-measure convex activation budget. The exact stationary law survives as the independent target beyond the known fold. A highly relevant 2006 same-map study remains incompletely accessible and an important priority risk.

## value

PASS

Distinguishing nonrecurrent transients from real compact recurrent activity is intrinsic to the neuronal map. A known fixed-point fold cannot itself rule out nonfixed compact recurrent sets in a nonlinear noninvertible plane map; the exact logarithmic cocycle upgrades it to a global threshold and gives an independently useful stationary defect statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
