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

The universal proof is analytic. The computational checks are finite stress tests only.

`verify_anti_forcing_crown.py` performs the following checks:

1. For every derangement through \(n=6\), it constructs the contracted digraph and computes the exact minimum feedback arc set by maximizing the number of forward arcs over all vertex orders. It compares this value with \(n(n-3)/2+c(\pi)\).
2. For every derangement through \(n=5\), it independently enumerates deleted nonmatching-edge subsets until the chosen perfect matching is the unique survivor, directly checking the anti-forcing definition.
3. For \(3\le n\le9\), it enumerates every derangement, checks the recurrence for the cycle enumerator, checks that every cycle count from \(1\) through \(\lfloor n/2\rfloor\) occurs, and checks the claimed minimum- and maximum-layer multiplicities.

Replay command:

`python verify_anti_forcing_crown.py`

Expected output:

`VERIFY_OK order_checks=320 direct_checks=55 distribution_checks=7 spectrum_checks=7 extremal_checks=14 max_order=18`

The verifier does not establish originality and does not replace the proof for untested orders.
