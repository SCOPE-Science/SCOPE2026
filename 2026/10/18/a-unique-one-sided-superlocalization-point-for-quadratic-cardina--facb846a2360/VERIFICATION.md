---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Direct piecewise B-spline integration independently recovered Gram entries g0=11/20,g±1=13/60,g±2=1/120, with strictly positive symbol (cos²θ+13cosθ+16)/30≥2/15. Quartic Q=z⁴+26z³+66z²+26z+1 has two distinct interior negative roots r,s, and Laurent inverse coefficients A r^{|k|}+C s^{|k|}, verifying infinite-mode decomposition by contour residues. Substituting the three nonzero translates on each side gives exact two-mode formula on y=m+t for m≥3. F_r(x) has exactly one zero in (0,1) at (sqrt(−r)−r)/(1−r), F_s there nonzero; max |Phi_z|=(1+z)/2. Uniform-in-t limiting supremum and the exact exceptional formula follow. Independent 36 kernel evaluations agreed to numerical precision. The theorem is one-sided and pointwise fixed x: no two-sided or arbitrary-knot statement.

## originality

PASS

Best-of-knowledge: compared mathematical objects, parameter ranges, equivalent transforms, prior stronger results and available exact tables; the specific final theorem is not known to follow from the inspected primary and Resultary findings. General exponential kernel localization and inverse-banded decay bounds do not describe the exact root F_r(x*) or faster subdominant root. An older exact cardinal inverse-matrix identity might, and is retained as a risk. A band-inverse decay theorem permits O(|r|^m), but no strict improvement at an exceptional x follows without vanishing leading coefficient and a nonvanishing next coefficient. These are verified by distinct analytic cancellations.

## value

PASS

Exponential localization of orthogonal spline projection kernels is a central approximation-theory issue. An exact unique evaluation site where the principal inverse-Gram pole is suppressed and the one-sided localization base is approximately tenfold smaller supplies an independently useful sharp exception to generic decay estimates, with a complete all-cell identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
