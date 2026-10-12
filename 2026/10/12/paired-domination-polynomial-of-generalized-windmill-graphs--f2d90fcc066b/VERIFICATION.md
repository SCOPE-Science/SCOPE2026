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

The analytic proof establishes the classification for every integer \(k\ge2\) and \(m\ge2\). The finite computation is a corroborating check only.

The packaged checker constructs \(W_{k,m}\) from the definition, independently tests domination, searches recursively for a perfect matching in each induced selected subgraph, and compares every subset against the stated parity criterion. It also reconstructs the coefficient vector from the even/odd subset polynomials and checks that vector against exhaustive counts.

Checked parameter pairs are \((k,m)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2)\). The \(m=1\) cases are deliberately outside the stated scope and serve only as boundary stress tests. The largest tested graph has order \(10\). The finite checks do not constitute the general proof.

Replay command: `python artifacts/verify_paired_windmill.py`

Expected leading line:
`VERIFY_OK parameter_pairs=8 subset_checks=2360 minimum_checks=8 max_order=10`
