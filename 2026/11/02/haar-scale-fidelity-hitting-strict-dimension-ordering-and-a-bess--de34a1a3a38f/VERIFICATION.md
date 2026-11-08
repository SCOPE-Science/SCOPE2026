---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The radial generator under y=nF_(t/n) is κ[y(1-y/n)f''+(1-y)f']. The bounded-at-zero hitting ODE gives (k+1)^2 a_(k+1)=[s/κ+k+k(k-1)/n] a_k, so positivity and strict coefficient decay for k>=3 prove the Laplace ordering. Differentiation at zero yields mean sum z^k/(k k!) prod_(j=1)^(k-2)(1+j/n), whose 1/n correction is C(z)=sum_(k>=3)(k-1)(k-2)z^k/(2k k!). Uniform bounded-coefficient limits give Kummer transform, small-z rescaling yields 1/I_0(2sqrt λ), and a product dominated by K^q with q=λ/H(z) gives the large-z Exp(1) clock. Independent exact rational coefficient inequalities tested n=3,5,10,40 and k=3..13.

## originality

PASS

Tóth 2026 establishes the isotropic Brownian geometry and finite-dimensional first-passage means/spectral formulas; the assessed contribution is strict dimension-to-dimension Laplace order at Haar-scale threshold, explicit positive first correction, and two normalized endpoint laws. Classical CIR Kummer hitting transforms alone do not imply the finite-dimensional Jacobi ordering. The November 3 2026 Tóth v2 was identified but its full text could not be accessed; the closest potentially covering source is a material priority risk.

## value

PASS

The threshold z/n has fixed Haar rare-cap probability e^-z and is a natural high-dimensional fidelity normalization. The all-dimensional Laplace order and sharp finite-size delay provide quantitative benchmarks; the Bessel-to-exponential crossover distinguishes typical from rare target hitting clocks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
