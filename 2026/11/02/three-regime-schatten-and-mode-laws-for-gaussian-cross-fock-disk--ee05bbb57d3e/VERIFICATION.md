---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the normalized Gaussian monomial bases the pairing is diagonal between the two spaces, and its nth coefficient is t^n times the lower regularized gamma integral of shape n+1, hence t^n P(Pois(x)>=n+1). Bounding the integral by x^(n+1)/(n+1)! gives compactness and all positive Schatten powers at fixed x. Positive-term summation of the random finite geometric sum gives the nuclear formula also at t=1 by its continuous limit. Normalizing the Poisson tail by its first mass gives a positive series strictly increasing in x and decreasing in n. The successive ratios therefore strictly decrease in degree, and for fixed degree increase continuously from 0 to t as x increases; this yields exactly the claimed threshold crossings at fixed t>1. For t<1, domination is geometric. For t=1, Poisson concentration gives a bracket at (1±δ)x, with the infinite upper tail bounded by a summable Chernoff geometric series even after raising to any fixed p>0. For t>1, write m=n+1 and λ=tx. On each fixed √λ window the Poisson tail divided by its first mass converges uniformly to t/(t-1), giving d_n=(1+o(1))e^((t-1)x) Pois(λ){m}/(t-1). For m below (1+δ)x the crude bound t^n is exponentially negligible if (1+δ)log t<t-1. Above this cutoff the same normalized d_n is bounded by a constant times Pois(λ){m}. Stirling gives a Gaussian bound up to m=2λ using the quadratic lower bound on y log y-y+1 on a compact interval, and an exponentially summable bound beyond 2λ using its tangent there. This justifies the discrete Gaussian integral (and the supremum) after taking a growing window, giving the 1/√p constant and the normalized modal profile. Finally, the exact critical squared Hilbert–Schmidt norm is E min(X,Y) for independent equal-mean Poisson variables; the Skellam/Bessel sum telescopes to the displayed expression and gives the stated remainder. The supplied checks/verify.py was inspected, not executed. Its recorded finite quadrature and grid checks supplement rather than establish the uniform estimates. The limit is for fixed t and p, not a joint transition limit.

## originality

PASS

Credit is for the complete fixed-p Schatten regime theorem for the mismatched disk pairing, in particular the sharp t>1 asymptotic for the entire p-power sum, not for radial diagonalization, the critical Bessel identity, or the overlapping modal and operator-norm laws taken alone. The strongest distinct Resultary record gives the same operator family and much of the modal theorem; its catalogue date is later and does not settle priority. The exact equal-weight Bessel identity is demonstrably covered in the Ginibre literature. Neither comparison supplies the full three-regime Schatten law with its all-fixed-p constants in the inspected statements.

## value

PASS

A fixed weight mismatch can change not just the norm but the aggregate spectral mass from a finite geometric limit, to growth proportional to disk area, to amplification on a moving band of order √x modes. The full Schatten constants quantify that change for every positive p, including small powers that are sensitive to the tails. This is useful information about a natural compressed Gaussian transfer beyond a leading norm or an isolated known critical identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
