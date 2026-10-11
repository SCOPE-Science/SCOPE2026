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

The standalone `verify.py` reconstructs all open-neighborhood complexes for orders 13 through 36 and executes every claimed simplicial collapse orbit, then compares the remaining tetrahedra with five explicit templates. Each local link is checked for the expected icosahedral combinatorics. The lifted height-section f-vector, both hemisphere links, and orientation signs are checked separately.

The finite computations do not themselves prove an infinite-parameter theorem: the manuscript gives the separate finite-width, PL noncritical-level, and monodromy proofs. The checks require Python 3 standard library only. Reproduction: `python3 verify.py`.

The scientific status is same-model reviewed; no independent external audit has been performed.
