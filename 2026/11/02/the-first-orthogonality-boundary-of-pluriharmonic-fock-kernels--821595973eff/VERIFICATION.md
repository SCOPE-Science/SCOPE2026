---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Under Gaussian measure (πα)^(-n)exp(-||z||²/α), the orthogonal splitting into holomorphic Fock plus conjugate vanishing-at-zero functions yields kernel Kph=2Re exp(<z,w>/α)-1. Put u=<z,w>/α, |u|≤R²/α. For r≤log2<1 the minimum of Re exp(u) over |u|≤r is e^(-r), uniquely at u=-r, proving nonvanishing below sqrt(α log2) and antipodal equality at it. For fixed t>log2 in one dimension, F(t,θ)=2exp(tcosθ)cos(t sinθ)-1 is positive at θ0 and negative at π; partition t∈(log2,1], (1,π/2), [π/2,∞) proves first root simple. Its phase q=θ+t sinθ lies in (π/2,π), giving Θ′(t)=cos q/(t sin q)<0. Expansion about π gives the sharp square-root onset; y=t sinΘ=π/2+O(exp(-t)) gives Θ=π/(2t)+π³/(48t³)+O(t^-5), and chord π/(2√t)+π³/(64t^(5/2))+O(t^-9/2). Independently calculated nine least roots and both limiting regimes; those finite tests support but do not prove the symbolic statements.

## originality

PASS

Looi and Fulsche establish the pluriharmonic kernel identity and holomorphic/antiholomorphic decomposition, which are credited premises. The new claim optimizes the first zero on a bounded origin ball, locates equality, proves one-dimensional first-angle monotonicity and sharp endpoint expansions. Retrieved primary Looi paper addresses Toeplitz Schatten classes, not zero location, and related polyanalytic Fock kernels have a different Laguerre zero structure. Published Resultary Fock kernels concern different Toeplitz/Gram invariants.

## value

PASS

The first orthogonality of evaluation kernels is a natural geometric invariant controlling how close strongly oscillatory reproducing-kernel vectors can be. The dimension-free sharp contact radius and one-dimensional full least-root motion with asymptotic chord length are motivated analytical boundary results, rather than a routine renamed operator norm. It distinguishes pluriharmonic from zero-free holomorphic kernels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
