---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Renewal at a fixed reset point makes final-success mark/time law proportional to e^{-Dq^2t}f_x(t)S_y(t) and its swapped counterpart. Subtracting the unconstrained one-axis Laplace weight e^{-qx} gives positive corner deficit; Gaussian first-passage density plus exact Mills representation m(u)=int_0^infty exp(-w-w^2/(4u^2))dw supplies 0<=1-m<=1/(2u^2). Two positive Bessel integral identities yield the global K0/K1 inequality with exact constants. R_q=sqrt(2)a+O(q^-2) and K0 asymptotics give the sharp normalized corner coefficient, while the normalized inverse-Gaussian tilt has mean d/(2Dq), variance d/(4D^2q^3), and Gaussian characteristic-function limit; omitted-opposite-axis mass is exponentially small. This establishes the joint Bernoulli(logistic(z))-Gaussian limit for fixed a,D,z and the final *successful excursion* only.

## originality

PASS

The direct wedge-reset paper derives finite-rate boundary currents and splitting probabilities, including qualitative high-reset side bias and bisector symmetry; these are explicitly prior. The new scope is the all-parameter quantified Bessel enclosure and first sharp correction together with a coupled marked final-success excursion Gaussian limit. Mere specialization of the old currents does not state these bounds or the final-success excursion time law; possible derivability from their complete kernels is recorded as a genuine implication risk.

## value

PASS

The high-reset competition between two absorbing sides has a concrete unresolved observation scale: offsets q^-1 yield neither side certain. Explicit switching width, logistic profile, first globally bounded corner-screening error, and the final-success duration CLT are natural measurable boundary-layer features, not arbitrary finite samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
