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

# Reproducible checks

From this directory, run `python3 verify_transfer.py > computed.json` and compare `computed.json` with `CERTIFICATE.json`. Run `python3 verify_direct.py` and compare its output with `direct_verification.txt`. Both programs use only the Python standard library.

The first implementation enumerates the entire finite closure of realized rank-one profile sets under the exact one-letter append maps. It asserts that profiles recomputed directly from a shortest witness word agree with the transferred state at every edge. It reports 32,541 states (including the empty word), 32,530 realized with both colours, a maximum minimal length of 24 and exactly 16 classes achieving it. It computes a deterministic SHA-256 of sorted fixed-width bitmasks for the *entire* state set.

The second implementation separately enumerates, for every point, the five possible relative-position categories of each witness and uses immutable sets of witnessed atomic profiles; it does not import or call the packed-state transfer implementation. It independently reproduces the complete minimal-length histogram.

The accompanying proof shows why the finite state closure is exhaustive over all lengths and why profile equality is the exact logical equivalence criterion. Neither a finite prefix enumeration nor a digest alone would prove the all-length statement. No independent expert review or formal proof assistant certification is asserted.
