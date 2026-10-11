---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

After the scaling \(u=ax/\varepsilon\) and \(\tau=\gamma a/\varepsilon\), the iteration is exactly \(T_{\tau}(u)=u[1-\tau/(1+|u|^4)^{1/4}]\). For \(0<\tau\le2\), every nonzero point contracts strictly in magnitude, which forces the global limit zero. The local expansion gives the ordinary linear factor \(1-\tau\), the matched case \(\tau=1\) has \(T_1(u)=u^5/4+O(u^9)\), and at \(\tau=2\) one obtains \(|u_{k+1}|=|u_k|-|u_k|^5/2+O(|u_k|^9)\), hence \(|u_k|\sim(2k)^{-1/4}\). For \(\tau>2\), solving \(T_{\tau}(u)=-u\) gives the stated unique positive symmetric two-cycle and differentiating gives the two-step multiplier \((1-32/\tau^4)^2<1\). Independent arithmetic reproduced the cycle, multiplier, contraction regime, and the bundled verifier was inspected rather than treated as proof.

## originality

PASS

The closest primary source introduces exactly the \(\kappa=4\) nonlinear surrogate and analyzes it inside normalized vector/matrix preconditioned-gradient schemes, but the inspected full text does not state the autonomous unnormalized scalar quadratic map, the exact frontier \(\gamma a=2\varepsilon\), the fifth-order matched regime, the critical \(k^{-1/4}\) law, or the post-frontier attracting two-cycle. The original Polar Express paper concerns polynomial matrix-sign iteration, not this scalar gradient dynamical system. Published SCOPE search returned nearby optimization stability results but no theorem implying this phase diagram.

## value

PASS

The surrogate is explicitly motivated by a current optimizer analysis, and the exact scalar theorem identifies a sharp stability loss, a nonhyperbolic critical decay law, and the first postcritical attractor. Those are structural boundaries for a natural model of the practical nonlinear preconditioner rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
