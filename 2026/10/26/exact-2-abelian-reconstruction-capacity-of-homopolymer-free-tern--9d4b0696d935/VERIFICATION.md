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

The six directed nonloop digram counts form an Euler trail on the bidirected triangle. One-letter counts recover the starting letter from outdegrees, so each observation equals a feasible arc vector with its starting vertex. Balanced flow differences a=b=c=t have three choices of starts except positive 2-vertex support (two) and zero support (three singletons). Six signed unit-imbalance endpoint pairs contribute 6A(z) with A(z)=(z+z²)/[(1-z³)(1-z²)^3]. Balanced contribution is 3B(z)-3z²/(1-z²), B=(1+z³)/[(1-z³)(1-z²)^3]. Summation simplifies to 3/[(1-z)^4(1+z)^2]-3z²/(1-z²). The coefficient at n-1 gives C_n and n³/8 leading growth. Independent brute-force word observations through length 10 matched all coefficients; the Euler-trail derivation is the unrestricted proof.

## originality

PASS

Best-of-knowledge originality: the exact stated constrained theorem is not mathematically implied by the inspected antecedents, with identified stronger-framework and inaccessible-source risks; negative searches alone are not novelty proof.

## value

PASS

Exact capacity under a natural no-homopolymer constraint for the two-abelian observation channel, including a nontrivial two-vertex support correction and all lengths; useful independent of an encoding algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
