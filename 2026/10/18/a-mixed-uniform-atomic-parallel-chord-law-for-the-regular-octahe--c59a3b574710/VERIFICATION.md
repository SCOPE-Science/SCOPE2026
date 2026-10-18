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

# Verification record

The included `verify.py` was executed from the delivered scientific package with Python 3 and SymPy. It checks every nonsingular triple among the eight supporting planes and interval-wide feasibility, verifies the twelve affine vertices, counts two six-vertex and six four-vertex facets, independently checks their exact shoelace areas, and confirms the volume polynomial and the chord density/atom weights. The geometric proof explains why a finite plane-intersection enumeration is exhaustive for all real parameters in the interval.

Numerical halfspace intersections at multiple parameter values were independently compared with the resulting polynomial as a sanity check only. Numerical samples do not establish the infinite-parameter statement. Independent external mathematical audit has not been performed.
