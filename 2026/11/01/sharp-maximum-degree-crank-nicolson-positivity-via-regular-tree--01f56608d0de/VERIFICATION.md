---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Setting R=(I+sL)^-1 yields C=2R-I, with R entries strictly positive on connected graphs for s>0. Augment A by Delta-deg(v) separate stationary ports so its row sums Delta; absolute Neumann series for R has coefficients counting rooted closed port walks. Universal Delta-regular covering-tree reduced-port words inject their closed walks into the original port graph, giving R_vv >= regular-tree g_Delta(s), strictly > for each finite graph because its port system has a non-tree reduced loop (cycle or stationary port). I checked the cavity q=1/[1+sDelta-(Delta-1)s²q] and root g=1/[1+sDelta-Delta s²q], with g(sigma)=1/2 exactly for Delta=3..13 by independent rational arithmetic. g strictly decreases; regular-tree-radius balls converge coefficientwise and via dominated Neumann series to g, so any supercritical s gives a negative center diagonal in a sufficiently large finite ball. I independently enumerated all labelled connected simple graphs on 2..5 vertices, checked rational positivity at the applicable degree cap; finite checks supplement infinite comparison/limit proof. Physical h=2s, strict endpoint positivity of every finite graph holds; Delta>=3.

## originality

PASS

Published Resultary reversible-Markov-chain return-resolvent law gives C=2R-I, diagonal half-return criterion and complete-graph thresholds; these are credited. The reviewed new implication is uniform over all max-degree-Delta graphs with exact regular-tree extremal crossing; full prior text does not derive this. Faragó–Horváth gives general discrete maximum principles, while Angel–Friedman–Hoory provides universal-cover Green-function machinery. A possible older specialized method-of-lines bound is the residual risk.

## value

PASS

Maximum degree is a natural graph datum; an explicit exact worst-case positive Crank–Nicolson step for all graph sizes and topologies with matching finite-tree obstructions gives a structural uniform sharp threshold. This improves the elementary diagonal sufficient step but is not an individual-graph optimum or a norm error estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
