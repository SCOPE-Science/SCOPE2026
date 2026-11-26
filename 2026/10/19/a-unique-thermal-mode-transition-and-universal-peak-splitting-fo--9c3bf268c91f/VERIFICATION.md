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

The symmetric beta stationary input follows from zero total active flux: the orientation densities are (1±u)f(u)/2 and [(1−u²)f]'=−2au f, so f∝(1−u²)^(a−1). The independent Gaussian term has dimensionless variance t. With z=1/(2t), Kummer's ODE gives q'=1/2−q+[q²+(1/2−a)q]/z, and at q=1/2 the slope is (1−a)/(2z). For 0<a<1, the small-z and large-z signs oppose (the latter follows by expanding (1−S)^(a−1) at S=0), and every crossing is upward. Increasing a lowers the tilted mean of S strictly by monotone likelihood ratio. The transverse root is analytic and has the stated endpoint limits by the tilted atom at a=0 and the centered curvature of a Gaussian-smoothed uniform law at a=1. The smooth beta approximants have exactly three derivative sign changes. The Laplace variation proof is valid for these nonzero derivatives: multiplication by (u−c) eliminates a sign change before applying Rolle's theorem to the scaled transform. Local uniform convergence then transfers the sign-change bound, not a count of every derivative zero. Oddness, the tail derivative sign and analyticity suffice to locate all true maxima; isolated derivative tangencies do not imply extra modes. For a>1 the integrable input derivative has only one sign change, and a=1 follows directly. At the threshold, the heat equation and transverse curvature give P''''(0)/P(0)=−2(1−a)/t_c². Solving the analytic equation P'(x)/x=0 in y=x² gives y' at t_c equal to −3, yielding the stated pointwise remainder. Independent weighted adaptive quadrature confirms, for example, t_c(0.5)=0.316464340348 and m²/(t_c−t)=2.998623867 at gap 0.0003; five threshold and quartic-sign checks passed. Replay: python /workspace/calculations/reproduce_frozen.py (check thermal_modes). These checks do not establish exhaustiveness or endpoint-uniform scaling.

## originality

PASS

Best of current knowledge for the frozen finding: the convolution, transition equation, qualitative phase diagram, and general one-dimensional Gaussian modal noncreation are prior. The supported distinction is a transverse, strictly ordered analytic phase boundary with verified quartic nondegeneracy, giving the exact onset amplitude in this beta family. Distinct indexed findings with later publication dates demonstrably duplicate most of the result (including the exact leading coefficient), and one adds an exact peak-to-center contrast. The overlap is real and is credited; these later findings are not evidence the frozen result was already covered when recorded, nor proof of authorship priority.

## value

PASS

The exact phase boundary is a naturally motivated observable of the stationary model. The distinction between a curvature plot and a globally exhaustive modal transition matters, and proving nondegeneracy gives a quantitative calibration of the physical peak location. Strict ordering across reversal rates is information that a generic one-dimensional scale-space theorem does not supply. No experimental universality beyond the stated symmetric harmonic model is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
