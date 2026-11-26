---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The spherical parametrization gives the displayed log-energy formula, with m(z) the tilted first-coordinate mean (zero at zero, strictly between zero and one for z>0). Differentiating the Bessel formula gives m'=1-m²-(d-1)m/z. At contact with g=1-c/z for z>c=d-1≥1, m'-g'=c(z-1)/z²>0; m(c)>0 rules out downward crossing. The radial derivative minus the center-radius derivative is c/r-2λ(s-r)(1-m); this is at least c/r for s≤r, and at least c/s for s>r by the bound (the zero-center and zero-parameter cases use the continuous angular formula). In the affine interpolation of centers and radii, |s'|≤R-r a.e., the center-radius derivative is nonnegative, and max{s_t,r_t}≤M. Integration gives the stated gap, including internal tangency or passage through the origin. Tonelli preserves the common multiplicative factor; the moment assumption gives finite positive energies. At zero parameter and zero centers the ratio reduces to log(R/r), giving uniform sharpness as r approaches R. For negative λ the concentric log derivative is c/r+2λr, eventually negative. Inspected RESULT.md §§1–5 and checker.py: angular quadrature and barrier tests are finite floating-point checks, reported but not rerun.

## originality

PASS

The supported distinction is the sharp quantitative log-energy comparison for moving centers without an origin-containment condition, in every d≥2, and its positive-mixture form. The Bessel barrier is not new, mixture closure is a corollary, and several nearby qualitative statements are already known. None of the compared geometric results gives the required combination of gap, unrestricted nested-ball centers and dimension.

## value

PASS

Origin-free inclusion is false in the ambient class of arbitrary convex bodies. This identifies a natural subfamily with an explicit, uniformly optimal strict gap, controls simultaneous center motion and radius growth, and distinguishes precisely the permissible exponential signs. The gap is not just qualitative monotonicity or a concentric special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
