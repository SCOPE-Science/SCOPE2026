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
# Reproduction and checked scope

Execute `python3 verify_high_branch.py` with a standard Python 3 interpreter, no network or optional packages. The checker reconstructs the full \(100\times100\) fiber matrix at \(u=969/1000\) and \(u=31/32\) via rational-function formulas, encloses powers and divisions using exact integer outward rounding at \(192\) dyadic bits, and carries out an interval Gaussian elimination with certified nonzero pivots. The recorded determinant signs are \(-1\) and \(+1\), respectively. Output diagnostics printed as floats are informative but never used as evidence for the signs. The continuity and Fourier/fiber implications are proved analytically in RESULT.md, with the general frame criterion cited from the motivating literature.

The check does not enumerate all parameters, prove root uniqueness, or independently audit the general frame criterion. No independent audit or external certification was carried out.
