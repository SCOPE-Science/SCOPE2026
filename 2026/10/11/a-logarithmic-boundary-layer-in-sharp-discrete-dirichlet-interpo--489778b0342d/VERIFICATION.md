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

Run `python check_halfline.py` with Python 3, NumPy, SciPy, and SymPy. The script checks the exact one-site algebra, computes the unique scalar optimizer for ten positive sites by bracketed root finding, checks discrete quadratic forms of reflected geometric extremizers after long finite truncation, performs 960 random finite-vector inequality tests, and evaluates the large-distance normalization at five sites. It reports `PASS 1007 checks`.

Independent analytic ingredients in `RESULT.md` are: the strictly positive resolvent reproducing bound, the image-kernel formula for the half-line Dirichlet Laplacian, uniqueness of the scalar maximum, the stationarity identity matching the actual energy ratio, and the asymptotic expansion of the stationarity equation. No finite calculation verifies the claim for every sequence or for arbitrarily large sites; those are mathematical consequences of the proof. Numerical optimizations are corroborative only.
