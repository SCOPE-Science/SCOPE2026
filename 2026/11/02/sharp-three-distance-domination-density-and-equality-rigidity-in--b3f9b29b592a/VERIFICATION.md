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

Run `python3 support/verify.py` from the directory containing the six reports. The verifier has only standard-library dependencies and reads the **bundled** `support/potential.json`. It checks the \(4096\) potential entries and all \(15376\) arcs without floating-point calculations. It checks the exact dual-potential inequalities, tightness, all SCCs of the tight subgraph, the seven-period witness and its fourteen row-swap/shift patterns. It independently calculates shortest-path distances in the actual Cartesian-product prism for \(n=7,8,9,10\), then enumerates every subset for \(n=7,8,9\).

Recorded exact checker summary:

`VERIFY_OK states= 4096 arcs= 15376 tight_arcs= 3583 cyclic_SCCs= [7, 7] witnesses_per_period= 14 primal_metric_n=7..10 bruteforce= [(7, 3, 14), (8, 4, 36), (9, 5, 72)]`

The finite potential inequalities are the certificate for the unbounded lower bound: telescoping them over *arbitrary length* closed walks proves the result. The two cyclic SCCs similarly certify the equality classification for all multiples of seven. Exhaustive direct subset checks for \(7\le n\le9\) are corroboration only, not the infinite proof. No claim of an independently audited proof or formal-system certification is made.
