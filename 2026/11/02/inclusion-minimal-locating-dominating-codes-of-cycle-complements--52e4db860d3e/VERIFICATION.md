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

The code `verify.py` was run with `density_potential.json` present and completed with `VERIFY_OK`. It compares actual graph-neighborhood locating-domination and inclusion-minimality against the gap criterion for every subset at orders \(7\) through \(14\), totaling \(32{,}640\) subsets. The separately implemented transfer walk counts through order \(20\), and agrees with the graph oracle at all eight directly tested orders. The density certificate gives integer potentials at \(64\) states and checks all \(136\) allowed directed edges. It also checks \(31\) explicit extremal-witness gap words.

The all-order results follow from the classification proof, the transfer identity, an exact finite potential inequality certificate and the explicit witness family. The computation is not offered as empirical proof of any unbounded statement. No independent audit or independent external validation is asserted.
