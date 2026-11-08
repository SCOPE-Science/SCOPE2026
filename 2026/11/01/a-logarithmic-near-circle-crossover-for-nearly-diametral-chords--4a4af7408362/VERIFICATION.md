---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Exact antipodal angle variables theta1=phi-v/2, theta2=phi+pi+v/2 give D=2a cos(v/2)sqrt(1-delta sin^2(phi)) with Jacobian one and product arclength density. For fixed 0<delta<1 the two nondegenerate maxima yield F ~ pi(1-delta)epsilon/(4a E(delta)^2 sqrt(delta)); for the circle, the exact arccos law has sqrt epsilon tail. For delta/(epsilon/a)->lambda finite, dominated convergence after v=2sqrt(epsilon/a)u gives H(lambda)=pi^-2 integral sqrt((1-lambda sin^2 phi)_+)dphi. Piecewise complete elliptic formula and DLMF endpoint series give pi^2 H(1+h)=4+h log|h|+(1-log16)h+O(h^2|log h|). Independently checked both branches of H with high-precision quadrature and two-sided cusp coefficients. The large-lambda asymptotic is not falsely used as a uniform theorem for delta/epsilon->infinity.

## originality

PASS

Distinguishes arclength-independent endpoints from established oval-interior and random-line chord sampling. Schrempp (2015) assumes a two-dimensional density, ruling out this boundary-law specialization; Mayer–Molchanov (2006) have rotation-invariant circular boundary model, not the noncircular or moving-eccentricity regime. The jointly scaled shape-tail law and nonanalytic H cusp go beyond the established circle law and DLMF function expansions. No inspected source states an equivalent simultaneous two-parameter boundary law; historical priority not proven.

## value

PASS

The distance deficit of independent boundary points changes universality class from linear for an ellipse to square-root for a circle. Its natural near-circle scaling has an explicit one-parameter law and a sharp logarithmic derivative singularity at lambda=1, a geometric transition in the dimension of maximizer sets rather than an arbitrary integral value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
