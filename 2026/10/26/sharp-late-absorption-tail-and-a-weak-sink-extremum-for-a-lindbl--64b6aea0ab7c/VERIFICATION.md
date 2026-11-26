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

The decaying root recurrence gives the free boundary resolvent −2q^m/Ω; the rank-one sink multiplies it by (1−iηq)⁻¹. On the upper rim of the band q=e^{ik}, and the denominator has real part 1+η sin k>0, including at η=1. Differentiating f(q)=q^m/(1−iηq) gives d_m=f′(1) and f′(−1)=(−1)^{m−1}conj(d_m). The Puiseux terms at Laplace frequencies 0 and −2iΩ are proportional to the square roots with phases −π/4 and +π/4 before inversion, respectively; inverse Laplace transformation gives the displayed conjugate phase factors in K_m. With smooth edge cutoffs, analytic terms are smooth and the next singular order is 3/2; the smooth complement is rapidly decaying by repeated integration by parts (even for m=1 its derivatives at large energy are integrable). Thus the amplitude error is O(t⁻⁵ᐟ²) for fixed parameters. In κ|K_m|² the constant part is 2C_m/t³; the interference oscillates with nonzero frequency and its integrated contribution is O(t⁻³). This yields the exact defective tail and both moment statements. Plancherel on the causal boundary resolvent gives the eventual absorption integral: the band gives the term invariant under η↦1/η and the two real-q exterior intervals give the finite-distance term. Differentiating gives the positive total-absorption slope. The tail derivative numerator m²−3(2m−1)η²−(m−1)²η⁴ is strictly decreasing in η², and its signs at η=1/√3 and η=1 locate the unique root, with equality at the first endpoint only for m=1. Expansion gives η_tail=1−1/m+O(m⁻²). For the atom at infinity, the free-sine-transform interaction picture converges since K_m is integrable; its limit is proportional to [sin(mk)−iη sin((m−1)k)]/(1−iηe^{ik}), nonzero in L², so some mass indeed escapes.

## originality

PASS

The exact model, resolvent, propagator and total-absorption formula are existing, and the slope of total absorption at matching loss is already implied by Riberi's integral and appears explicitly in a matching catalogue record. The distinct supported claim is the fixed-site integrated late-time coefficient and its sharp moment and loss-optimization consequences; the comparison of opposite response signs depends on that new tail calculation, not a new total-absorption theorem.

## value

PASS

The exact defective late-mass amplitude makes quantitative a rare-event objective that the total absorption integral cannot answer. It resolves how the two interfering band edges enter late probabilities, sets the sharp scale of the truncated second moment, and separates the loss optimizing unusually late absorption from local improvement of total detection. The exception-free fixed-parameter result at η=1 is useful where a boundary mode meets the continuum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
