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

The cyclic incidence map identifies the vertex-phase quotient with the edge torus because the only compatibility condition for integrating the differences is closure. The real stationarity equations have common flux s; strict descent in the claimed interval excludes additional modular fixed points. At s=0 the even number of pi entries gives eight points. At nonzero s the three unit-weight angles each equal a or pi−a; the two mixed branch counts require (t−1)sin a=0, while the two pure branch counts are the same set under a↔pi−a. The triple-angle identity then gives sin² a=(3t+1)/(4t), impossible below 1 and giving exactly four distinct solutions above 1. For the Boolean two-pi points, let d_i=−w_i cos z_i. The constrained Hessian determinant in coordinates u4=−u1−u2−u3 is (product d_i)(sum 1/d_i)=sign(d1)(1−t), and the two sign pairs yield both signs of the form. Translation by pi on all four coordinates reverses the Hessian, pairing the six non-extremal Boolean points by index. For a non-Boolean point the form is c[(2t+1)u1²−u2²−u3²−u4²], c=cos a≠0: its sign on u1=0 is opposite its sign on (−3,1,1,1). This gives the stated indices and a unique minimum. Reflection exchanging the endpoint pair of the special edge and the opposite pair gives Laplacian blocks [[1,−1],[−1,1]] and [[2t+1,−1],[−1,3]], yielding the stated spectral bound. The vertex potential's Hessian is bounded in operator norm by that Laplacian norm, giving the descent inequality by Taylor integration; summability gives vanishing gradients and increments. A finite omega-limit set with vanishing increments is a singleton. The nonminimum local null-basin argument also works at a zero stable multiplier: in a small coordinate ball the derivative splits into stable norm <1 and unstable least expansion >1, with a sufficiently small Lipschitz nonlinear remainder. A difference in the unstable cone (unstable norm at least stable norm) stays in the cone and expands, so two orbits trapped in the ball cannot have a difference in that cone. The trapped set is a Lipschitz graph over a subset of stable coordinates and is null. The analytic Jacobian is nonzero at the all-zero point, hence has a null zero set, and countable local inverse charts off that set ensure null sets have null preimages. This proves almost-everywhere selection including noninvertible updates. At antiphase the multipliers are 1−h lambda; strict linear attraction holds exactly in the claimed interval for positive h. Neither t=1 nor nonlinear behavior at the upper step endpoint is asserted. Replay: RESULT.md lines 19–58 and the determinant, block and cone checks above. The finite NumPy checker and verification notes were read, not executed, and do not prove exhaustiveness.

## originality

PASS

Prior work covers the unit-weight rings, the general descent and finite-critical-set convergence argument, generic complex root counts and a signed-edge 12-real-root example. The distinct claim is the exact positive one-edge detuning census and its indices, yielding a unique attracting minimum throughout the descent range even where global invertibility is not available. No inspected stronger theorem gives the full census or that weighted specialization.

## value

PASS

Detuning one edge is a natural way to resolve the critical circles of the symmetric four-cycle, and the direction of detuning produces a genuine change by four equilibria with explicit inertia. The exact census explains the unique attracting pattern without discarding saddles. The weighted full descent interval is useful because it includes possibly noninvertible updates and gives an explicit sharp linear threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
