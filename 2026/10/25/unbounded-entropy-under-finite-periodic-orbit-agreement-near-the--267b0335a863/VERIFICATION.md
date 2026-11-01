---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

In the inspected RESULT.md the surgery interval I=[(2Q-2)/Q^2,(2Q-1)/Q^2], Q=2^P, has disjoint first P-1 tent iterates, and T^P(I)=[1/Q,2/Q] strictly contains I. Replacing one dyadic Markov state by odd M alternating laps of slope ±2M preserves all embedded periodic orbits of least period <P pointwise, while an M-branch F^P horseshoe gives h_top(F)>=log M/P. Cloning the primitive dyadic Markov adjacency yields a primitive Markov transition matrix, bounded inverse cylinder diameters and topological exactness. ||F-T||∞<=2/Q². Independent exact-fraction arithmetic rechecked first returns for P=3..7; these checks only supplement the all-parameter Markov/return proof.

## originality

PASS

Published interval-map full-period-spectrum rigidity concerns the complete embedded orbit collection; Sharkovskii period type concerns lengths only. Neither logically yields preservation of the *exact sets of points* of all short cycles while arbitrarily inflating entropy near one exact expanding tent map. Resultary semantic searches found nearby dynamics, but no implication to the precise statement; accessible abstracts do not prove whole-document noncoverage.

## value

PASS

The theorem proves a sharp non-identifiability phenomenon for finite spatial periodic-orbit observations inside topologically exact expanding interval maps. It complements a recent full-spectrum rigidity theorem and quantifies simultaneous arbitrary C^0 proximity and unbounded entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
