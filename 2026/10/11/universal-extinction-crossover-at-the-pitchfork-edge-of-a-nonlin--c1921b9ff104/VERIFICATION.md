---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The final theorem is restricted to the positive fixed-total-population simplex N=S+I+R=N0=b/d, k1=(d+gamma)/N0, k2=k1(1+gamma/(d+nu))/N0-epsilon/N0, 0<=epsilon<k1(1+gamma/(d+nu)), with all parameters positive and a single interior initial state fixed as epsilon->0. Direct independent symbolic expansion of the original ODE yields the exact system I′=-D_epsilon(I)-B_epsilon(I)w, w′=-(rho-aB_epsilon)w+aD_epsilon, w=R-aI, D=I^2(epsilon+C_epsilon I)/(1+alpha I^2), C_epsilon=C0-(1+a)epsilon/N0, B=I(k1+k2I)/(1+alpha I^2). At equilibrium w=0, D>0 for I>0 excludes all endemic equilibria; positively invariant compact simplex, planar index/Poincare-Bendixson and local one-sided attracting zero/negative center drift imply global convergence to disease-free point (boundary omega-limits force the same equilibrium). Independent differentiation confirms G′(z)=-1/[z^2(1+z)] and dG/dtau=-I′/[I^2(epsilon+C0 I)] for z=C0 I/epsilon, tau=epsilon^2t/C0. The stable fast w equation and Gronwall/variation of constants yield |w(t)| <= transient exponential + K(epsilon I^2+I^3), uniformly close to epsilon=0; this controls fixed-epsilon limits tI=1/epsilon and, at epsilon=0, tI^2=1/(2C0). Integrating G with a uniform entrance time T_delta for fixed interior initial data and a scaled transient error O(epsilon^2/I(T_delta)^2) proves locally uniform convergence to G^{-1}(tau) on compact subintervals tau>0. Independent exact sympy calculation confirms all key algebra, and a rational parameter integration gives supplementary numerical consistency only. Infinite-time and parameter-uniform results rely on analytic estimates, not verifier output or finite sampling.

## originality

PASS

Best-of-knowledge qualified PASS for the combined, parameter-family, physical-time, globally seeded singular crossover, not for basic extinction, disease-free global stability, pitchfork bifurcation, or either elementary fixed-parameter center-decay mechanism. Original Zhang--Li 2023 model Eq.2, Theorem 3 and Theorem 4 were read in their full original 24-page CC BY manuscript and already give global extinction in the no-endemic regime and qualitative R0=1 pitchfork center degeneracy. The inspected source contains no locally-uniform epsilon->0 crossover with fixed positive initial data, physical-time C0/epsilon^2 normalization and infinite-scaled-amplitude entrance G^{-1}. The full nearby published 2026 mathematical findings concern distinct multiple-exposure S,I or predator-prey fields, not the exact SIRS family. A generic cubic-quadratic normal form suggests the limiting function, but converting it to the full global basin and nonuniform time scale needs the stated fast-variable estimates. The title/wording and lack of search hits are not novelty proofs, and an older implicit general singular-perturbation theorem is residual risk.

## value

PASS

The codimension-two meeting of R0=1 and the source pitchfork edge is a natural dynamical boundary in an established nonlinear SIRS epidemiological model. The result quantifies a previously qualitative transition with exact original-time extinction constants, a nontrivial epsilon^-2 crossover time scale, and an initial-data-independent inverse-log scaling profile for any fixed infected interior state; it remains useful for testing asymptotic dynamics at infection prevalence O(epsilon). The difficult feature is validating the entrance from an O(1) global initial seed on times diverging as epsilon^-2 in a fast-slow three-compartment system, not elementary inversion of a scalar normal form alone. This is a specific motivated mathematical classification, not a universal epidemiological forecast; no general theorem or noise extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
