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

Conditionally on a single occurrence of i, an adjacent pair has equality probability ((n−2)/n)h_i: its two locations must miss the uniformly placed occurrence and then have the same letter under the normalized law off i. This proves Eq. (1) after weighting by np_i(1−p_i)^(n−1) and summing. At n=1 the covariance is zero; for n≥2 the binary sign is that of 1−na(1−a), with exactly one reversal in nonzero signs, and the equal-mass formulas agree. Adding a letter of mass ε preserves the finite previous sample of strict signs by continuity. The new letter has h=S and bracket 2S+n[−2Sε+(S+1)ε²]; at the two integer lengths floor(ε^(−1/2)), floor(2/ε) its contributions are respectively 2S√ε+o(√ε) and −4Se^(−2)+o(1). The old letters have uniformly bounded coefficient parameters and contributions O(n²(1−δ)^n) for some fixed δ>0, negligible at both scales. Thus each new positive mass appends two strict signs beyond the old lengths; the binary seed gives 2q−3 reversals for some fixed law on each q. An independent bounded integer dynamic program also verifies the ternary witness: the exact covariances are 65160/130321, −46035365796/6131066257801, 36283702577400/42052983462257059, and −3465336136509778177512/1978419655660313589123979 at lengths 2, 8, 11 and 19, respectively.

## originality

PASS

The supported distinct claim is the unbounded lower bound across alphabet sizes on sign reversals as n varies at a fixed law. General composition/run generating functions already encode any fixed-length hapax/run joint moment; the finite covariance identity is not the novelty. Closest indexed sign-window, run-count, and occupancy results differ in which statistics or parameters vary, or use dependent draws.

## value

PASS

This rules out any alphabet-uniform one-switch or finite-switch principle for the dependence between an occupancy statistic and an adjacent-run statistic of the same iid word. The rare-letter scales explain the mechanism; the strictly contrasted binary case and explicit first possible higher-alphabet example make it more than a collection of computed moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
