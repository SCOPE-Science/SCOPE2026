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

# Reproduction and scientific limits

Run `python verify.py` from the directory containing `requirements.txt` with NumPy (>=1.24) and SciPy (>=1.10). The program terminates only when each check passes and prints `ALL_SIMPLEX_SECTION_SHADOW_CHECKS_PASSED`.

The independent geometric reconstruction projects each canonical simplex onto the perpendicular hyperplane and computes the true convex-hull volume for 480 generic directions across dimensions \(N=3,4,5,6\). It separately constructs crossed simplex edges, verifies counts, and checks the sharp deterministic upper and lower bounds, including two-level equality classes for each positive/negative sign split through \(N=19\). Spherical absolute-product moments are independently checked by numerical quadrature. First and second exact area moments are checked against random Haar directions in dimensions \(N=3,4,8,20,100\). The limiting variances, zero asymptotic correlation and chi-square deficit are checked empirically for \(N=300,1000\).

The analytic proof uses the facet-area normalization, Cauchy's projection formula, a strict sign-class norm bound, connectedness of sign chambers, the correlated Gaussian absolute-product identity, and a bivariate central limit theorem after centering by the sample mean and self-normalization by the Gaussian norm. For the moving-threshold count, a grid and variance bound justify the \(o_p(1)\) error. For the projected volume, a local absolute-value remainder and a law of large numbers for squared Gaussian norm justify the \(o_p(1)\) linearization. Parity of the two Gaussian influence functions makes the bivariate limit independent.

No finite sample simulation establishes an infinite-dimensional theorem or historical priority. The exact joint density at finite dimension, convergence rates, nonregular simplices and general oblique projections are not determined. The nearest prior section-only results and the relevant brightness literature are cited in RESULT.md and REVIEW.md. No independent audit has been performed.
