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

# Reproducibility and checks

Run `python3 checker.py` with Python 3.9 or later and the standard library. Its output for this package is:

`ALL_CHECKS_OK bisim_valuations= 49510 profiles= 220 direct_closure_valuations= 2340`

It enumerates atomic-colour assignments and computes the greatest colour-preserving bisimulation via an independently implemented successor-signature refinement. It compares this to the local colouring criterion and exact counting formula for every positive composition up to six worlds with palette size one to four when the palette assignment count is no more than 1500. Separately, for all compositions through four worlds, it builds the actual Boolean subalgebra closed under \(\Diamond\) from four-colour atomic predicates and compares generation to the proposed condition, checking 2340 colourings. These are bounded independent checks of finite cases. The proof, not the computation, establishes the theorem for arbitrary finite parameters. No external or independent audit has been conducted.
