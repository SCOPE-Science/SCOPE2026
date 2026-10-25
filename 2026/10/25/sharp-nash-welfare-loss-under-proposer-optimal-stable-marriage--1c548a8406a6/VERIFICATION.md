---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python verify.py` with the standard-library Python interpreter. The script implements men-proposing deferred acceptance, checks blocking pairs over all possible bijections, and computes Nash products using exact integers and exact rational ratios. It does not read any external data or require third-party packages.

It exhausts the complete labeled strict-preference domains for \(n=2\) (\(16\) profiles) and \(n=3\) (\(46656\) profiles). For each, it compares every stable matching to the men-proposing stable matching and checks the bound with the exact number of changed partners. It obtains a maximum product ratio of \(1\) at \(n=2\), a maximum of \(8\) at \(n=3\), \(5424\) strict-gain profiles at \(n=3\), and exactly \(12\) extreme profiles at \(n=3\). It also verifies the sharp cyclic example for each \(2\le n\le14\) and each admissible moved-set size \(2\le k\le n\).

These are finite verification statements, not a machine proof that the result holds for all \(n\). The latter follows from the analytical rank-utility factor bound and the explicit arbitrary-size construction in `RESULT.md`. No independent audit is asserted.
