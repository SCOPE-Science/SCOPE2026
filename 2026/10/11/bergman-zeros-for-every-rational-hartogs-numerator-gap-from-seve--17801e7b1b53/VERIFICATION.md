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
# Reproducibility and verification

Run `python3 verify_hartogs_gaps_7_to_17.py` with the Python 3 standard library; no third-party dependencies, floating-point arithmetic, or downloaded datasets are needed.

The executed checker reconstructs all coefficient arrays from the explicit Bergman numerator formula, verifies reciprocity, calculates the angular Chebyshev transforms, proves the asserted quadratic/cubic terms by exact rational coefficient equality after using the analytically proved degree-three interpolation principle, and checks Bernstein positivity for all 84 residue families on the intervals specified in RESULT.md. It additionally verifies the polynomial identity at parameter values 4 and 13 independently of the four interpolation nodes. Its output ends `PASS: exact certificate, 84 reduced-residue families, all positive.`

The checker alone cannot certify the infinitely many parameter values: that inference uses the separate endpoint-summation degree argument in RESULT.md. The reduction of numerator roots to actual Bergman-kernel zeros uses the source's geometric kernel criterion. Results for gaps 18 and above, irrational exponents, or individual zero multiplicities are not established. No independent audit has been performed.
