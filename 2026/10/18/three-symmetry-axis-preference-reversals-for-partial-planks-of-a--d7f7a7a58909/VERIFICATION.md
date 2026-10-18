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

The exact proof is in `RESULT.md`. The standalone `check_octagon.py` uses SymPy and standard Python geometry, does not require external network access, and can be run from a clean directory with `python check_octagon.py` after installing SymPy. It checks five symbolic endpoint identities, the exact third root, the middle polynomial identity, root-order isolations, endpoint sign intervals, direct independent polygon-clipping areas over 2,001 half-widths for each of two axes, and 1,599 strict orientation preferences away from the three crossings. All these tests passed when run on the packaged source. The full-width quantifiers are supplied by the displayed piecewise-integral proof and quadratic sign analysis, not by the finite checks. This is not an independent scientific audit.
