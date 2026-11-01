---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

C PASS: On a tree, target infection probability is p^distance, hence expectation at handle vertex v_j is sum_{i=0}^L p^|i−j|+m p^(j+1). For every pendant leaf w, E_v0−E_w=(1−p)[(m−1)p+sum_{i=1}^L p^i]>0, eliminating leaves. Algebraic adjacent difference is p^(j+1)[1−p^(L−2j−1)−m(1−p)]. For positive k=L−2j−1, it is p^(j+1)(1−p)(sum_{a=0}^{k−1}p^a−m); k<=m gives strict negative, k>m produces one simple zero in (0,1) by strictly increasing geometric sum. k decreases by two along the handle, so the R unique roots obey t0<...<t_(R−1). The sign sequence of all adjacent differences is unimodal for every p interval, proving the unique global winner, not just local pairwise reversals, with one adjacent tie at each exact root. For m=2, L=2R+2 gives arbitrarily large R. Independently enumerated all edge-retention states in 18 small rational cases and checked three distinct thresholds with four winner phases; universal proof is analytical.

## originality

PASS

O PASS qualified: the epidemic expectation is exactly 1 plus standard decay centrality, not new terminology. Tsakas proves near-zero and near-one maximizer principles. The full 2018 article proves that arbitrarily complicated decay-centrality *rankings of a designated adjacent pair* can occur on constructed glued trees; importantly it does NOT imply that arbitrary many distinct global optimizers appear successively on the specifically defined one-hub broom or supply their exact ordered thresholds. The more recent generic instability theorem does not directly settle this sharp special-family characterization. Under the same best-of-knowledge bar, the exact broom global-optimum phase diagram survives; generic instability is acknowledged as prior.

## value

PASS

V PASS: The theorem gives a complete exact optimizer classification for a natural and elementary tree geometry in a standard epidemics/centrality observable, including all algebraic switching points and unboundedly many globally optimal *source locations*. This is more informative than observing that two arbitrary rankings can flip.

The dated certificate retains the supplied scientific assessment, sources and limitations.
