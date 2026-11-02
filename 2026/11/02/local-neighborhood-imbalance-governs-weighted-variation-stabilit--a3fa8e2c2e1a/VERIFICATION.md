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

# Reproducibility and boundaries

Run `python verify_gossip_variation.py` with Python 3.11 or later and the dependency from `requirements.txt`. The exact-rational tests enumerate all indicator cuts in each selected small graph; for independent cross-checking, separate minimum-cut computations are performed on further samples. The random seeds, construction, and sample counts are contained in the script. An observed success is a finite diagnostic, not a replacement for the proof's layer-cake reduction or local weighted displacement lemma.

The analytical proof covers all finite connected simple undirected graphs with strictly positive edge variation weights, at least three vertices, real signals, and \(0\le\theta\le1\). The two-vertex boundary case has norm \(|1-2\theta|\) and is deliberately excluded from the formula containing a baseline one. No external or independent audit has been performed.
