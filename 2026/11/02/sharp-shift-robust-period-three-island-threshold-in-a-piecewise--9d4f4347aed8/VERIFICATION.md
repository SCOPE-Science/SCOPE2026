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

The analytical derivation in `RESULT.md` proves the full domain claims; no independent audit has been performed. The supplementary `verify_period3.py` is self-contained and uses only Python standard-library exact rational arithmetic.

Running `python3 verify_period3.py` produces:

`PASS: 8 derivative words; 552 exact area/positivity comparisons; 3168 exact three-step orbit tests; exact shift extrema`

The checker evaluates all eight length-three derivative words, compares independent rational polygon clipping and cardinal-spline area formulas over \(23\times24=552\) rational parameter pairs, verifies admissible strict-upper-branch orbits, and checks sharp fixed-width extrema. It does not sample all real parameters or classify dynamics outside the three-cycle islands. No external review or formal infinite certification is claimed.
