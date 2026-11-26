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

The normalization and complex-valued convention matter. In one odd cyclic coordinate the two grid contacts at ±(n−1)/2 bound the real part of f(1); equality makes both nonnegative Fourier values zero, and the sine term then forces the imaginary part to vanish. For n even the antipodal contact fixes Re f(1)=1/2, leaving a nonzero interval |Im f(1)|≤(1/2)tan(π/n) as imposed by the closest samples to π. For products, marginal sums and restrictions are positive definite. Bounding the mass by successively marginalizing all coordinates outside an axis shows that at full equality each axis must reach its one-factor bound. Each odd-axis Fourier contact is a zero average of nonnegative full Fourier coefficients, so all coefficients on the corresponding frequency hyperplane vanish. Inverting in the other coordinates gives two linear equations on each spatial triple; subtraction, using a nonzero sine, forces the two outer entries equal and their value to be the central one divided by 2cos(π/n). Applying this in every odd coordinate gives the stated tensor when all are odd, including n=3. Its transform factors with exactly two deleted grid frequencies per axis. When an even side occurs its interval of phases tensors with fixed maximizing factors to give distinct normalized maximizers. A separate direct DFT check corroborated the small-grid, product and even-phase cases.

## originality

PASS

The scalar product law and the corresponding one-dimensional real-even mass are prior knowledge and receive no originality credit. The inspected closest theorem gives product values, not a classification of arbitrary complex maximizers. The additional finding is rigidity precisely in the all-odd case, with an exact Fourier support and a phase continuum otherwise.

## value

PASS

Extremal mass and a complete rigidity test are different information. Here the test works in all dimensions and detects instability of uniqueness from any even side in the complex-valued problem. The forced Fourier zeros also determine the exact Fourier support and furnish a short equality-propagation argument rather than a case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
