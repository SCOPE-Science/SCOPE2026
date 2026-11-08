---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For one positions p<q<r, patterns with two ones recover L=2p+q and T=r−p; one-one patterns recover Q=p²+q²+r². At fixed n the complete deck is equivalent to (L,T,Q). With q=L−2p and r=p+T, Q is quadratic 6p²+(2T−4L)p+L²+T², permitting at most two p; the mate is p+(a−b)/3 and interchanges positive gaps a,b. Requiring integer in-bounds distinct mate gives a−b divisible by 3 and a != b. Orient a=b+3h, h>=1; pair count U(n)=Σ_{b,h>=1}max(0,n−2b−4h). Summing geometric series yields z³/(1−z)^4−z⁷/((1−z)²(1−z²)(1−z⁴)). New literal triple-deck grouping and formula checks exhaustively agree at each n=3..18. Infinite theorem follows from quadratic and sum, not from finite instances.

## originality

PASS

Chrisnata et al explicitly proposed exactly this generating function as Conjecture 1, based on initial twenty coefficients, and established only Θ(n³). The present algebraic gap-swap and all-length fiber classification prove that conjecture. Related 2026 total-deck asymptotics address all weights, not this exact fixed-weight formula.

## value

PASS

Resolves a named published exact enumeration conjecture and classifies every ambiguity fiber in a natural deletion/subsequence reconstruction channel, yielding an explicit optimal zero-error code size at each length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
