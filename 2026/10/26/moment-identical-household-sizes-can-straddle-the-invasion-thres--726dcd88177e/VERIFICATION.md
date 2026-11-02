---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For P_m with uniform index, E[Z_m]=1+(2/m)sum_{d=1}^{m-1}(m-d)2^-d from ordered seed-target distances. Values m=1..4 are 1,3/2,11/6,33/16. Externally infected households are size-biased m q_m/E[M], giving R*=beta sum q_m m H_m / E[M]. Both q have E[M]=2 and E[M^2]=5 and hence variance1. Substitution gives 13 beta/8 and 77 beta/48, with exact strict opposite sides for the nonempty given beta interval and 403/400 versus 2387/2400 at 31/50. Independently computed all with Fraction. Requires independent bond edges, path contact topology, uniform arrival individual and early-phase branching; no empirical epidemic assertion.

## originality

PASS

A general household reproduction formula based on size-biased entry and within-household epidemic size is classical, and is not claimed new. Dönges et al. derive a first-two-moment identity under their size-only attack-rate law, while Barlow et al. use full household mixing. The present exact moment-matched path-contact threshold witness is not the known affine case; no exact prior witness found. Novelty best-of-knowledge is confined to this explicit model boundary, not the general R* formula.

## value

PASS

The pair shows a qualitative reversal of the invasion decision for an open beta interval despite identical commonly reported household-size mean and variance. Explicit path topology demonstrates precisely when size-only aggregation can be misleading; this is motivated epidemiological-model identifiability rather than claiming a new threshold theory or significance of a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
