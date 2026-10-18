---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Reconstructed the exact x,y,z equations from Hu--Sang--Wang original PDF equation (2.2). With dτ/dt=e^(x/3), Y=y e^(-x/3), Z=z e^(-2x/3), direct differentiation yields x_τ=Y, Y_τ=Z-Y²/3, Z_τ=d/2-2YZ/3+E with E=-cZ e^(-x/3)-b²Y e^(-2x/3)+(eps-a x)e^(-x)-(d/2)e^(-2x). At h=(9d/4)^(1/3), k=h²/3, limiting planar field has equilibrium (h,k). For 0<η<1/3 the rectangular lower/upper Y face signs are k(η/2-η²)>0, -k(η/2+η²)<0 and lower/upper Z signs (d/2)(η/2+3η²/2)>0, (d/2)(-η/2+3η²/2)<0. Independently checked strict signs at η=.01,.1,.2,.3; uniform E->0 above finite Xη gives an invariant tube with Y>=h(1-η)>0. This gives τ-global forward motion with x linear in τ, finite original T=int e^(-x/3)dτ and exact upper/lower time bounds. For u=Y-h,v=Z-k, W=(2h²/9)u²+v² obeys Wdot=-(4h/3)W-(2K/3)u³-(4/3)u v²+2vE; on tube Young inequality gives Wdot<=-γW+γ^-1 E², γ=2h(1-η)/3, and E decays exponentially in τ. Therefore Y->h,Z->k, while q=e^(-x/3) satisfies qdot=-Y/3, q/(T-t)->h/3. Exact constants x=-3 log(T-t)+log(12/d)+o(1), (T-t)y->3 and (T-t)^2 z->3 follow; reflection negates all three for negative escape after changing eps to -eps. All a,eps real and b,c,d>0 are included; negative divergence -c does not prevent finite escape. Finite algebra checks supplement but do not replace asymptotic argument.

## originality

PASS

The full 2022 paper introduces exactly this jerk field, proves local bifurcations and illustrates bounded attractors, and explicitly infers ultimate confinement from negative divergence (p15719). That implication does not follow from volume contraction and is contradicted on the new finite-escape open sets. The closest published same-equation compact recurrence result was read in full and restricts its own conclusion to bounded complete/forward orbits, leaving unbounded trajectories untreated. Hoang homogeneous-dominant-vector-field blow-up theory does not directly cover exponential positional forcing. New open invariant escaping tubes, finite physical lifetime and universal constants are not logical consequences of those older statements.

## value

PASS

Showing open sets of actual finite-time escape in a dissipative five-parameter flow corrects a mathematically consequential misuse of negative divergence as a global confinement guarantee. The invariant tube and universal logarithmic rate give precise stable mathematical structure for this natural published jerk system, contrasting bounded chaotic regimes without claiming their destruction. The sharp constants and two-sided survival-time scale can matter in singular trajectory analysis and numerical detection; neither accuracy of simulations nor symbolic verification alone is counted as value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
