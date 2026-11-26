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

Polar integration with t=|z|² gives Gaussian moments k!. For the C²-valued pair, the pointwise squared gap g−f is (t−1)(t−3)² and the squared Fock norms are 21 and 23, respectively; the same pair works on every smaller exterior with R≥1. For arbitrary s=R²>0, if u is perpendicular to all polynomials in L²((1+t)e^(−t)dt), its weighted Laplace transform is analytic for Re w<1/2 by Cauchy–Schwarz (also after differentiation on compact subsets); all derivatives at zero vanish. Its restriction to the imaginary axis is the Fourier transform of an L¹ density, so u=0. A nonzero real function compactly supported in (0,s) has negative signed quadratic integral against (t−s)e^(−t)dt. Polynomial approximation preserves this strict inequality by Cauchy–Schwarz and |t−s|≤max(1,s)(1+t). Splitting the real coefficients of (t−s)p² between orthogonal vector monomials gives exactly the nonnegative exterior gap and negative full Fock gap. The result also holds on the closed boundary, and uses only finitely many coordinates for each radius.

## originality

PASS

The supported contribution is the vector-valued failure, including the two-coordinate polynomial obstruction at the scalar sharp radius, and the realization of an arbitrary-radius moment obstruction by finite-coordinate polynomial pairs. The scalar principle and general moment-localization techniques are not claimed as new.

## value

PASS

The sharp scalar conclusion fails in the first larger Hilbert dimension at radius one, even for cubic polynomials, and the infinite-dimensional version loses every positive radius despite admitting finite-coordinate tests. These are structural limitations on scalar-to-vector transfer, not just altered constants in a scalar statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
