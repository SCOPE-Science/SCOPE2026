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

On the mean-zero space the gap lower bound z is a positive-semidefinite constraint. Compressing to the group contrast and taking normalized traces on the two within-group zero-sum spaces gives the three necessary bounds on totals; uniform weights realize all three compressed Rayleigh values. At fixed z the minimum normalized cost therefore reduces to a piecewise-linear function of cross weight divided by z, with breakpoints 1/(p+q), 1/p, 1/q. The slopes are pq−t(2pq−p−q)/2 and pq−tq(p−1)/2, so the claimed values and flat intervals follow; for equal groups the last two breakpoints coalesce. At all points where both internal trace bounds are tight, positivity forces both within-group zero-sum spaces into the gap eigenspace. Applied across the partition this makes every column and row constant, and within each group it makes the internal Laplacian scalar on its zero-sum space. This proves the stated unrestricted uniqueness and the full lower and balanced critical segments. Above the upper price only the larger group's bound is tight: equal rows with slightly unequal positive column weights preserve the large group's eigenvalue B/p while the other positive eigenvalues remain strictly larger by continuity. For the explicit example 5u1u2=11/80>1/9. The upper endpoint claim is only an exhibited segment, not an exhaustion. The frozen NumPy checks were inspected as supporting evidence, not run or treated as the proof.

## originality

PASS

The closest inspected priced complete-graph theorem shares the method and the upper price but changes one block's relative price and does not give the target lower transition or unrestricted rigidity. Credit the framework and shared upper-price calculation; the distinct content is the two-internal-price law and rigidity/nonrigidity classification under independent weights.

## value

PASS

The thresholds and optimizer geometry answer when scarce budget buys internal reinforcement, and when symmetry of the cost no longer forces symmetry of actual optimal weights. The equality analysis adds useful information beyond computing a symmetric optimal representative. The balanced case shows the role of group-size imbalance and bounds the scope of the asymmetry claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
