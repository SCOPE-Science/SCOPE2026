---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For 0<s<t the standardized Brownian pair has correlation r=sqrt(s/t), so splitting the time square converts variance into 2∫_0^1r[G_z(r)-G_z(0)]dr for the bivariate normal square probability G_z. Differentiation of the Gaussian density in correlation equals mixed spatial differentiation; evaluating four corners gives G_z′(r)=[exp(-z²/(1+r))-exp(-z²/(1-r))]/(pi sqrt(1-r²)). Integration by parts yields the stated positive one-dimensional variance formula. With r=(1-t²)/(1+t²), k=z²/2, the derivative has sign C(k)-A(k), where A,C are positive Laplace-type integrals. A(0)=pi/8-1/4<C(0)=pi/8+1/4; the logarithmic slope of A/C is E_C[1+t^-2]-E_A[1+t²]>0 on 0<t<1, and A/C→infinity using compact subinterval bounds. Hence a unique crossing and unique global variance maximum. Near z=0, singular substitution in W′(a),a=z², yields W′=2/pi-2sqrt(2/pi)sqrt(a)+o(sqrt(a)), so V=2z²/pi-(4/3)sqrt(2/pi)z³+o(z³). At z→infinity, boundary-layer scaling y=z²(1-r), dominated by sqrt(2y)exp(-y/4), gives V~8 phi(z)/z³~4 delta/z². Independent two distinct quadratures agreed for ten thresholds; scalar root k*=0.344054851601727 and V*=0.08135656185520389; small/large asymptotic numerical checks corroborate but do not prove the limits.

## originality

PASS

Full matching primary article confirms the Brownian functional, second moment and numerical peak were known. The exact single-crossing analytic law and both sharp asymptotic constants remain nontrivial new refinements under best-of-knowledge comparison.

## value

PASS

The fractional time coverage of ordinary confidence intervals is a motivated inferential statistic whose limiting variance materially affects monitoring interpretation. A unique worst-variability coverage threshold and sharp extreme-confidence decay law answer natural exact questions that the source numerical table and PDE do not determine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
