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

For linear decay the stages give v₂/v₀=1+(14/9)z+(28/81)z² and hence the stated recurrence. With an exact input pair at t_n the stage offsets at which f is evaluated are (7/9)h and (11/9)h. Taylor substitution into the endpoint gives y(t_n)+hy′(t_n)+(h²/2)y″(t_n)+O(h³), and the roots at z=0 are 1 and 1/3, so the method is zero-stable. Along the real decay axis the three strict Jury inequalities reduce to −1≤T<4/3, giving (−9/2,0). When T≤0 both recurrence coefficients are nonnegative and not both zero. When T>0 the roots are simple and positive; evaluating the characteristic polynomial at 1/3 gives 5(3T−4)/252<0, so the smaller root is below 1/3. Implicit differentiation then gives dλ_−/dT>0. On the left lobe λ_− decreases strictly with z while e^z increases, with opposite orders at the two ends; on the right lobe e^z exceeds 1/3. In the two-positive-root region, factoring out the smaller root's nth power shows that E≥λ_− is necessary and sufficient for positive iterates, including the sign case E>λ_+. Equality kills the dominant mode and proves exactness. Otherwise there is one transition, possibly through a single zero, and the first strictly negative index is floor(ν)+1. The difference λ_−−e^z vanishes linearly with a strictly negative z derivative at the root. Substitution in the exact index formula gives the logarithmic coefficient. Independent bisection gives z*≈−3.762080033887951 and log(λ_+/λ_−)≈3.21552426430; direct stage iteration at offsets 10^−2, 10^−4, 10^−6 and 10^−8 below this threshold gives first negative indices 2,3,5,6, matching the formula. This small numerical check is corroboration, not the positivity proof.

## originality

PASS

The specific Chebyshev construction and recurrence are established prior work. The inspected results do not give the global exact-startup endpoint sign threshold for this specialization, its smaller-root resonance, or the corresponding logarithmic first-negative law. A distinct two-step construction exhibits closely related resonances and logarithmic delay, so the mechanism is not credited as distinct in general. Full text of a plausible 2024 follow-up could not be inspected and remains a substantive access limitation, not a negative finding.

## value

PASS

For a damped method designed to take stable steps on the negative real axis, the actual interval of positive scalar endpoint values is a natural and strictly smaller diagnostic. A sharp, globally proved internal boundary of the stability interval shows both a useful isolated exponential exactness phenomenon and why a finite run near the boundary can miss eventual sign failure. This information is neither an ordinary stability radius nor a coefficient table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
