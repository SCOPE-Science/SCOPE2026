---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Kang's Algorithm 1 and §4.1 weight at x_k, linearize at the extrapolate, and use the stated proximal metric. The scalar subproblem derivative yields exactly D(x)Φ(x,y)=(ℓ−a)((1+β)x−βy)+ab, where D(x)=ℓ+2/(1+ρx²)>0. The proximal condition is ℓ>a; the gradient is co-coercive with respect to the scalar metric a in Kang's convention (1/a-cocoercive in the ordinary scalar convention). Fixed points give F′=0. The scaled stationarity map is odd and sign-preserving; its derivative has numerator a w²+(2a−2)w+a+2, w=ρx². Its two positive simple roots for 0<a<1/4 give the stated local maximum and minimum; at a=1/4 the derivative has isolated zeros at w=3 and the map remains strictly increasing, with cusp ordinate 3√3 in absolute value. At equilibrium the characteristic polynomial is λ²−[(1+β)c+s]λ+βc, with c=(ℓ−a)/D in (0,1), s=4ρx²/[D(1+ρx²)²]≥0. Thus 1−βc and P(−1) are positive, and P(1)=1−c−s=F″/D controls the strict Schur test. For F″<0 there is a real multiplier >1, and the other lies in [0,1); β=0 is included. At degeneracy one multiplier is 1 and no nonlinear conclusion is claimed. The witness stationary cubic factors as (x−1)(x²−8x+9); the outer roots have positive curvature. The objective gap 2+5√7/8−log(4(3+√7)) is positive since the first two terms sum to >7/2 and the logarithm is <5log 2<7/2. The local attracting neighborhood at (1,1) contains a nonempty open interval on the prescribed initialization diagonal. The symbolic checker was inspected, not executed; the universal proof is analytic.

## originality

PASS

The update is already an immediate specialization of Kang's explicit formula, and the Cauchy stationarity cubic and related convexity thresholds are prior. The distinct supported claim is the all-admissible-parameter classification of the local dynamics of that specific update, coupled to its exact multiplicity regime and a robust suboptimal basin under actual diagonal initialization.

## value

PASS

The exact two-state spectrum ties a practical failure mode to curvature rather than to the choice of inertia or proximal curvature. The stationary cubic by itself only supplies candidate equilibria; the classification shows both minimizing branches really attract and gives a constructive open set of allowed initializations that stays with the strictly worse branch. No global basin or degenerate stability assertion is needed for that conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
