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

# Computational and analytical verification

The accompanying programs reconstruct the derivatives and prove signs with exact arithmetic. Run `python check_derivatives_landau.py` (SymPy required) and `python check_landau.py` (standard library only). Both were run successfully on the actual included source files before packaging.

The rational interval program encloses the unique root in \((1.1429918,1.1429919)\) and proves \(3.2305076<F^{(6)}(0)<3.2306338\). The symbolic program implements exact angular moments and the differentiation operator, checking the quadratic, quartic and sextic formulas identically. The infinite-temperature-range uniqueness rests on the analytical positive coefficients \(d_n\) for every integer \(n\ge2\), not on a finite numerical scan. The local field law rests on the Taylor remainder of a real-analytic potential near the origin. The program does not certify the global phase diagram or independent reproducibility.
