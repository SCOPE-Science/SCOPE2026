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

# Reproducibility

Execute `python verify.py` using Python 3.10 or newer; the captured output is `verification_output.txt`. The verification reconstructs adjacency from generated rooted-tree parent lists, computes each power by integer bit-vector XOR, and compares the exact coefficient formula for every applicable source, destination and time. It also confirms the penultimate rank-one map and final nilpotence, checks the half-of-initial-configurations identity by full enumeration for permitted small trees, and samples nonuniform child multiplicities.

For the deterministic included run: 145 unlabelled rooted even-branching shapes (through 13 vertices); 14,238 exact source-time columns from the shape census; 6,858 initial configurations exhausted on shapes through nine vertices; 120 seeded nonuniform additional trees and 16,978 sampled source-time columns. The printed summary is independently reproducible from the embedded program. Exact arithmetic is used throughout.

**Limits:** finite enumeration does not certify all trees or all sizes. Universal correctness rests on the complete three-case formal-power-series proof in `RESULT.md`. The script checks neither historical originality nor alternative rule families. The historical-literature assessment remains bounded; no independent audit has been performed.
