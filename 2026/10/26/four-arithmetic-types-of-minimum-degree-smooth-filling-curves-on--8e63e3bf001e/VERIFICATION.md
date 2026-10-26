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
# Reproduction and evidence limits

With Python 3 and SymPy installed, run both `python verify_exact.py` and `python verify_sympy.py` in this directory. The first script implements binary polynomial arithmetic and Buchberger reduction directly, checks four affine charts for 256 fiber-normalized candidates, builds the 36 projective substitutions, and counts points over degrees one to four. It writes `smooth_masks.txt` and `exact_output.json`. The second script obtains a separate kernel basis, scans all 2047 nonzero filling forms with SymPy Gröbner bases, and compares exact accepted masks; the expected terminal output begins `independent sympy count 66 match True`.

The finite search is exhaustive because dimension 11 yields exactly 2048 filling forms, with 256 covering every smooth possibility after the proved fiber restriction. The exact Jacobian ideals, not low-degree rational-point scans, establish smoothness over an algebraic closure. The four rational-point profiles are secondary invariants; finite extension counts alone would not prove smoothness. The calculation does not classify abstract genus-six curves or constitute independent external audit.
