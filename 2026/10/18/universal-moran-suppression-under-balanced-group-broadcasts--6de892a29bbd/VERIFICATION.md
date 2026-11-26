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

For a mixed edge with a mutants and b residents the two count increments are +b and −a, with edge-parent probabilities ar w_e/(dW) and b w_e/(dW), W=rM+N−M. This gives exactly the displayed defect for Y=r^(−M). The geometric-series factorization has the sign of r−1 inside the bracket, strictly so when ab>0 and a+b>=3; unmixed and pair edges contribute zero. Connectivity gives a positive-probability monotone route to consensus from every mixed state. Finiteness makes the block absorption probability uniformly positive, so the accumulated bounded drift is integrable. At consensus E[Y]=1−rho*(1−r^(−N)), which yields exactly the stated sign and denominator on both sides of r=1. For strictness fix a large edge. If it is monochromatic, expand the opposite type along crossing edges until a large edge is already mixed or until a size-two step puts the opposite type inside the chosen edge, which then remains mixed. That finite path has positive probability and reaches a positive drift before consensus. At r=1 use the martingale M, not the constant Y; all-pair edges give exact equality. Independent exact finite-state calculations verify the accumulated defect and comparisons in one weighted mixed-rank example and a weighted pair-only control at r=1/2,1,2.

## originality

PASS

The broadcast update, Moran benchmark, and suppression in selected unweighted examples are prior. An exact local-mirror match also covers the unweighted incidence-regular all-large-edge subclass with the same exponential drift proof, so do not credit that subclass or the method alone. The principal distinct contribution is the weighted-balanced all-initial-set result with pair edges allowed, the strict characterization when higher-order edges exist even if they are initially monochromatic, and the explicit cumulative defect in this scope.

## value

PASS

The theorem identifies when topology preserves the Moran benchmark and when larger broadcasts strictly suppress selection. It upgrades selected or averaged examples to a pointwise structural rule, even for configurations with no local strict drift at the first step. The exact nonnegative cumulative defect explains how mixed higher-order events, not just a degree count or placement average, produce the fixation gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
