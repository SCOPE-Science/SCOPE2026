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

Split the two part-vectors into constant and zero-sum components, then into equal and opposite signs across the parts. The four Laplacian eigenvalues are 0,u=na,v=(n−2)a+2b,and u+v, valid even when u=v. The Gauss scalar factor is positive everywhere on the nonnegative axis, so the diagonal is positive, and the zero mode fixes the row sums. Write f(z)=12z/(z²+6z+12). Up to a factor 1/(2n), the same-part numerator is f(uh)+f(vh)−f((u+v)h), positive for h>0 because f(z)/z is strictly decreasing. The two cross numerators are f(uh)−f(vh)+f((u+v)h) and (n−1)(f(vh)−f(uh))+f((u+v)h). With t=uh, r=v/u and denominators A=t²+6t+12, B=r²t²+6rt+12, C=(1+r)²t²+6(1+r)t+12, clearing the common positive factor gives Y=BC−rAC+(1+r)AB and X=(n−1)(rAC−BC)+(1+r)AB. Expansion yields the stated quartics. The positive lower coefficients of Y leave only the sign of r²+r−1. In X the constant and linear coefficients are nonnegative since nr≥n−2; the quadratic coefficient divided by 12 is increasing in r and equals 4(n−2)(n−1)/n² at r=(n−2)/n. The quartic sign is that of (n−1)(1−r²)+r. Its positive zero lies below n/(n−2), because that expression at n/(n−2) equals −[3(n−1)²+1]/(n−2)². Hence the cubic coefficient of X is positive up through the quartic's zero. Above that zero there is one coefficient sign change regardless of the cubic sign. In either exterior regime the failing polynomial starts positive for sufficiently small t>0 and goes negative at infinity; Descartes' rule gives one positive root. The other cross type remains positive since the two exterior regimes are disjoint. Identity at h=0 and positive lower coefficients at each closed boundary verify the endpoint rules. At b=0 the golden-ratio test is met exactly for integer n≥6, and expansion of the upper root gives limiting b/a=5/4. The numerical examples agree with the spectral entry formulas. The source verification note and exact-rational checker were inspected, not executed; finite matrix checks are not the all-parameter proof.

## originality

PASS

The supported distinction is the sharp two-sided interval in a continuous perfect-matching conductance, both exterior horizons and the all-size crown transition. The homogeneous K(n,n) line and the six-cycle crown endpoint are already covered by independent exact statements; the latter is an exact uncredited overlap at n=3,b=0, not new here. Neither of those results, nor the inspected general Padé sufficient conditions, supplies the two-sided anisotropic if-and-only-if result.

## value

PASS

The classification gives the exact admissible conductance imbalance for a familiar fourth-order scheme, rather than merely asserting possible positivity failure. The two opposite edge-type failures and unique finite horizons yield actionable timestep restrictions, and the size-six crown transition is a natural structural consequence. These are useful beyond the known homogeneous case and previously solved six-cycle cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
