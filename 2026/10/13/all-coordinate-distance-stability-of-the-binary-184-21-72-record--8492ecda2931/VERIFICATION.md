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

The bundled `verify.py` reconstructs the published binary \( [184,21,72] \) code from its quasi-cyclic factorization, polynomial and tail data. It enumerates all \(2^{21}-1\) nonzero messages, checks the complete published weight distribution, extracts all 9,826 minimum words, computes the coordinate-incidence spectrum, and checks \(0<r_j<9826\) for all 184 coordinates. The calculation is exhaustive for this finite code; it is not evidence for any unenumerated family or for multi-coordinate modifications.
