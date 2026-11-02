---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For the fixed 3-path with ordered a0<=c0<=b0 and d=b0-a0>0, pure neighborhood confidence has center-to-leaf directed distances zero and leaf-to-center distances |b-a|/2; hence both leaves open or close together. Strict gate epsilon<=d/2 permanently freezes leaves; the center follows c_next=(1-rho)c+rho*A with independent fair endpoints, giving unique contracting Bernoulli convolution, mean midpoint and variance rho*d^2/[4(2-rho)], no almost-sure pointwise limit, and SLLN time average. rho=1/2 yields uniform binary expansion. For epsilon>d/2, symmetric simultaneous compromise with rho<=1/2 preserves ordered endpoints, contracts their gap and holds gates open. Conserved average and exact V contraction with spectral bound E V_t <=(1-rho*(1-rho))^t V0 imply almost-sure consensus via summability. Exact strict equality boundary checked. Independent rational history check verified 3072 length-seven edge histories and exact finite recursion moments; infinite time assertions use coupling, SLLN and Borel-Cantelli, not enumeration.

## originality

PASS

The stationary random affine-recursion mechanism including uniform binary series and variance has an exact predecessor: Acemoğlu et al Section 2.1, one regular node and two exogenously stubborn neighbors. Do not claim these formulas standalone as novel. The assessed NDW statement adds the endogenous confidence threshold that causes precisely this stubborn configuration, plus a disjoint all-responsive consensus regime for exactly the same input and model, in a uniform if-and-only-if phase classification. The primary NDW model paper simulates the general model but its inspected technical setup and conclusions do not present this exact three-path theorem.

## value

PASS

The complete threshold at exactly half the initial leaf gap demonstrates a nontrivial phase split between ergodic nonconvergent opinions and a.s. mean consensus in an endogenous directed-confidence model, including the knife-edge strict inequality. This supplies a precise small-graph analytic benchmark for a model previously explored by simulations. The known stubborn-agent recursion alone would not pass value as a new theorem; the gating dichotomy adds mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
