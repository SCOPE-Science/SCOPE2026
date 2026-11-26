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

A genuine flip strictly decreases the cut size, so absorption occurs almost surely with finite mean attempted-update time (each nonabsorbing state has a positive update success rate). With fair initialization, positive polarization probability is equivalent to existence of a nonconstant weak-majority coloring, since each such absorbing state has positive initial mass. A singleton color is impossible in a connected graph. At order four the only connected possibilities with a stable 2+2 cut are P4 and C4; the former has no connected edge-deletion predecessor, and the latter's predecessors are P4 and already support polarization. Fresh exhaustive enumeration at orders 2–5 gave 1,4,38,728 connected labeled graphs and 0,0,0,90 successful marked insertions, split 30/60. An independent rational solve of the full 32-state lazy chains, including unchanged attempts, confirmed the star transition (p,T)=(0,105/16) to (7/48,355/64) and the triangle-with-two-leaves transition (0,713/96) to (31/192,545/96). Replay: python3 /workspace/branches/36868dca-19b5-4e61-bb87-3b7f55bc958b/record4_repro.py. For the star family, while the hub is fixed, ordinary dissent decreases and the linked pair can only remain both dissenting, remain both aligned, or become aligned from mixed. The hub-flip thresholds in these three cases are h−1, h+1, h. If the hub flips it cannot flip again: the disagreeing fraction drops below one half and can only decrease. A flip leads to eventual polarization only from the aligned-pair case. The equal-rate race therefore gives the two telescoping terms and the mixed recurrence; their weights are 1/4,1/4,1/2. Conditionally on J, the probability of a hub attempt before J−(h−1)+1 initially dissenting ordinary leaves align, when J≥h−1, is (J+1−(h−1))/(J+1). This bounds the flip event from above. Using the binomial mean and variance gives the stated O(m^−1/2) bound and the limit 1/4, because in the absence of a hub flip only a pair initially dissenting can stay opposed. Exact finite values through m=8 were reproduced, but the limit is analytic.

## originality

PASS

The result is distinct at the level of the exact edge-marked boundary/classification, initial-state-averaged rational p and T values, and the one-linked-pair star probability. Prior cut-potential and random-network majority results do not establish these conclusions. The closest indexed majority results have different graph families or observables and are later than the frozen record's date.

## value

PASS

It is natural to ask whether improving connectivity can stabilize disagreement instead of removing it. The sharp smallest-order boundary and complete edge-marked census show exactly how this first becomes possible. The star-family result shows it is not merely a tiny-graph anomaly: a single leaf–leaf edge leaves a tie-protected pair and creates a nonvanishing limiting probability while the unchanged star always absorbs unanimously. Exact absorption times quantify a separate observable under the same intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
