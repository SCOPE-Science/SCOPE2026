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
# Verification

## Analytical check
Use the negative-edge force in [1] with a self-loop denominator to obtain the exact two-camp recursion. The sign of \(1-\eta\) yields the three cases without approximation. The statement concerning all finite times explicitly requires \(\eta<1\). For \(\eta\geq1\), cross edges are absent from time one onward, so the active-edge denominator changes and the recurrence is no longer applied after that time.

## Executable check
Run `python verify_signed.py` using Python 3 standard library. The program evaluates the update from all active signed edges rather than inserting the reduced recurrence in its update implementation, comparing exact fractions for 30 connected instances, for sizes \(m=2\) through \(m=11\) and three distinct signed graph families. The final test output is `PASS: 30 exact rational signed-graph configurations, 22 synchronous steps each; all 3 phases and m=2..11`.

## Limits
The numerical and rational checks do not establish claims for all graph orders. The proof covers arbitrary finite realizable sign-biregular graphs by invariance of the two-camp homogeneous state. Independent audit is not performed.
