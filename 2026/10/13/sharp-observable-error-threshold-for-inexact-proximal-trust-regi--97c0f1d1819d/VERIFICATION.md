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

Let s=u−x and let p minimize H. Comparing the Type-1 upper bound on H(u)−H(p) with strong convexity at x gives 2rQ≤ε²−‖p−x‖²−‖s‖². Strong convexity at u gives ‖u−p‖≤ε, so the computed-step test implies ‖p−x‖≥(1−κ)‖s‖ for κ<1. Substitution gives exactly −(1−κ)‖s‖²/r. The zero-step case is harmless. For φ=0, r=1, x=0, u=1 and p=1−κ the gap is κ²/2 and the bound is attained. At κ=1, taking p positive arbitrarily close to zero defeats any uniform positive coefficient even on nonstationary instances. Negative p=1−κ for κ>1 gives ascent. For the algorithmic claim, ε≤κ‖p−x‖/(1+κ) suffices for termination of geometric refinement at a nonstationary step. With c=1−κ and Ψ=‖s‖/r, choose a feasible segment fraction α=min{1,Δ/‖s‖,c/[r(1+‖B‖)]}; convexity of φ and the directional curvature bound give a decrease at least (c/2)Ψ min{rΨ,Δ,cΨ/(1+‖B‖)}, proving the claimed FCD constant. Theorem 10's first assertion applies under the stated outer hypotheses. On its vanishing-Ψ subsequence, the exact model residual is at most (1+κ)Ψ; proximal-length comparison and the vanishing reference-oracle error transfer this to the reference approximate residual. Nonexpansivity and the gradient-error assumption then give the exact true-gradient residual tending to zero; proximal-length comparison covers every fixed positive length on that subsequence.

## originality

PASS

Supported for the sharp computed-step coefficient, its sharp boundary, and the stated conditional transfer for the modified trust-region tolerance. The Type-1 gap definition, observable computed-step test itself, and outer convergence framework are prior. In particular BKM already uses the computed step in Algorithm 2, but restricts κ<1/2, proves a weaker descent constant, and states its separate true stationarity implication with an exact-step-relative test. Other relative-error work has genuine criterion-level overlap without the sharp universal affine decrease or the specific transfer.

## value

PASS

The exact constant is operationally meaningful: a practitioner can stop using an observable step, with a certified descent coefficient and convergence transfer even when the allowable relative error exceeds the printed half threshold. Endpoint and ascent examples identify a real boundary for universal certification rather than an arbitrary parameter change. The proof retains the required outer stability guarantees and separates model stationarity from the true residual.

The dated certificate retains the supplied scientific assessment, sources and limitations.
