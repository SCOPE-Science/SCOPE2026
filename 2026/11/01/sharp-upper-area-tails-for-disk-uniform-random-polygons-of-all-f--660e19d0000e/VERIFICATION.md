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

Run `python verify_polygon_tail.py` with NumPy, SciPy, and SymPy installed. On the tested environment, its exact symbolic checks verified \(15\) instances of the angular Gram determinant/inverse and normalization, and \(6\) Taylor-coefficient identities; the seeded near-cap importance-sampling comparisons for \(n=3,4,5,6\) at \(\varepsilon=0.001\) yielded ratios \(0.99656,0.99938,0.99764,0.99469\) to the leading prediction.

Run `python test_enlarged.py` with NumPy and SciPy installed. Its independently enlarged reference-domain simulation obtained ratios \(1.00140\pm0.00098\) and \(0.99985\pm0.00120\) at \(\varepsilon=0.001\) for \(n=3,4\) respectively (one estimated Monte Carlo standard error). The enlarged-domain test is numerical and does not prove that finite chosen enlargement encloses the entire rare event for arbitrary \(\varepsilon\); the limit follows from the analytic local bounds.

Both programs are finite consistency checks, not infinite certificates. The mathematical proof uses compact localization around the unique regular-polygon maximizers, the nondegenerate mixed linear–quadratic Taylor expansion, exact beta-ball integration, and the uniform remainder comparison. Neither a complete CDF nor a growing-order limit is established. No independent external audit was performed.
