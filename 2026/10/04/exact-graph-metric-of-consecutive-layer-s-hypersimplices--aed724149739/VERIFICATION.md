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

The proof is analytic and valid for every integer \(d\ge2\) and \(0\le a<b\le d\). The finite program is a separate stress test, not a replacement for the proof.

The packaged script `artifacts/verify_interval_metric.py` constructs the graph directly from the edge criterion specialized to consecutive layers. For every interval in dimensions \(2\) through \(8\), it runs breadth-first search from every vertex and checks both the closed all-pairs distance formula and the diameter \(\min\{b,d-a\}\).

Replay command:

`python artifacts/verify_interval_metric.py`

Observed output:

`VERIFY_OK consecutive-layer S-hypersimplex metric intervals=119 ordered_pairs=1382942 max_d=8`

The checked finite range does not certify the theorem in unbounded dimension. The unbounded statement rests on the explicit route constructions and the one-Lipschitz lower-bound argument in `RESULT.md`.
