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

Run `g++ -O3 -std=c++17 verify_cubic.cpp -o verify_cubic && ./verify_cubic` to check all \(9^7\) normalized cubics, and `python3 verify_examples.py` to check the explicit cubic and Hermitian quartic by a separately written implementation. The first program returns `TOTAL_NORMAL_FORMS 4782969`, `FULL_COVERAGE 0`, `MAX_COVER 85`, `COVERAGE_GE90 0`, and `BEST_COEFF 0,1,0,0,0,0,1,`. The second finds 16 rational cubic points, distribution `(0:6,1:41,2:24,3:12,4:5,5:3)`, and the Hermitian distribution `(1:28,4:63)`. The normal-form exhaustion relies on the transitivity of \(\mathrm{PGL}_3(k)\) on rational incident point--tangent-line flags and on scaling the nonzero tangent coefficient. This is finite exact computation, not evidence about a larger field, and no independent audit has yet been conducted.
