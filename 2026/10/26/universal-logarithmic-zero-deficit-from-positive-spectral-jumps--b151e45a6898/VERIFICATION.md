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

With the covariance Fourier convention exp(-i(n-m)theta), the diagonal covariance is the positive Poisson extension u divided by 1-r^2. Edelman–Kostlan uses (4*pi)^(-1) times the Euclidean Laplacian; harmonicity of u gives the negative energy term, and the radial derivative of the disk deficit is r/(4*pi) times its angular energy. The periodic jump model is -Delta_j/pi times Im log(1-z exp(-i theta_j)); subtracting these leaves Lipschitz boundary data. Its Poisson approximation error is O(epsilon log(e/epsilon)), tangential derivative is bounded, and radial derivative is O(log(e/epsilon)) by the conjugate Poisson kernel acting on the bounded boundary derivative. Near theta_j, replacing 1-r exp(is) by epsilon-is introduces a bounded error in its reciprocal because the numerator error is O(epsilon*|s|+s^2) and both denominators have modulus comparable to sqrt(epsilon^2+s^2). This checks the two gradient components and the metric factor. With u and the step profile bounded below, the integrated error from their denominators and gradients is O(log^2(e/epsilon)), radially integrable. The model jump contributes Delta_j^2/[pi*epsilon*w_-*w_+] to angular energy, since the arctangent change of variables gives pi times the integral of the squared reciprocal linear interpolation on [0,1]. Integration gives the logarithmic coefficient with O(1) remainder. At s=epsilon*x, the same estimates are compact-uniform and the factor (1-r^2)^2/(4*epsilon^2) tends to one. The case of no jumps has an integrable energy bound and a bounded deficit, and the coefficient is nonnegative for either sign of jump.

## originality

PASS

Credit the global additive logarithmic coefficient with bounded remainder for jumps between two strictly positive values, and the compact-uniform interface law in that regime. The exact Poisson covariance representation and general sign of the deficit are known. The closest same-day indexed endpoint result has a local half-plane profile of the same form at an interface with one zero side; its disk result has a different leading term and a positive logarithmic correction. It does not determine the nonlinear reciprocal jump-energy coefficient for two positive sides. The source comparisons do not establish precedence for the shared local profile mechanism.

## value

PASS

The result identifies a distinct boundary regime for Gaussian zero counts: discontinuities can cause an unbounded disk deficit even with no spectral zeros. The exact normalized coefficient separates heights and interfaces, and the compact-uniform angle law localizes the mechanism and justifies its integrated contribution with bounded error. This gives more than either a deficit inequality or the leading iid bulk term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
