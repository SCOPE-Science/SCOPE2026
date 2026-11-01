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

The accompanying standalone `verify_m7.py` enumerates all simplex sets of the matching complex of the complete graph on seven vertices. It checks the chain relation, exact ranks of the mod-three boundaries, and the sign of the action on the unique mod-three degree-one cohomology class. It explicitly confirms that all 105 facets possess an odd relabeling fixing each matching edge of that facet, so the oriented 2-chain representation cannot admit the one-dimensional sign representation in characteristic three.

Execute with `python verify_m7.py` (Python 3 and NumPy). The expected last line is `VERIFY_OK`; `verification_output.txt` records the actual output. The finite checks independently corroborate, but do not substitute for, the published integral theorem that the first homology is cyclic of order three. The asserted nonsplitting is proved by the stabilizer argument in `RESULT.md`, without extrapolation from finite examples.

The independent audit was not performed. No mathematical certification by another party is asserted.
