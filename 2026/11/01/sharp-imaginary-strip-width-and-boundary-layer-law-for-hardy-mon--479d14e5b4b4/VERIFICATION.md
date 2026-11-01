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

# Reproducibility and limits

The mathematical proof is in `RESULT.md`. Its critical steps are the normalized Hardy kernel identity, algebraic radius of each circular fiber, strictly increasing root map, Taylor expansion at the compact/isometric transition, and the exact phase/radial characterization of escaping extremizers.

The standalone `verify.py` program uses Python 3 and SciPy. Running `python3 verify.py` returned `PASS 45527 supplementary assertions`. It independently optimizes the logarithmic circle radius, tests exact imaginary extrema, samples off-extremal points, tests complex symbol phases, and compares both asymptotic regimes. All these are finite tests; they do not constitute an exhaustive numerical or external formal certification of the theorem.

The 2026 primary paper on Hardy Berezin ranges could not be inspected beyond its accessible abstract and metadata. That gap is a publication-priority limitation, not a proof limitation. Independent audit is not yet performed.
