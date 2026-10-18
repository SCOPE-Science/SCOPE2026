---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Condition on last car n in space j: its choice is any of j preferences, previous labels split into independent left and right valid parking blocks, and cross-block inversions contribute (−1)^(n−j+I(L)). Summing over label subsets gives G(n−1,j−1)=[n−1 choose j−1]_{−1}. Thus S_n=Σ_j j(−1)^(n−j)G S_{j−1}S_{n−j}. Separating even/odd coefficients gives O=E²+2zEE′ and E′=E³+8zE²E′+4z²E²E″ (formal series E0=1). Coefficient induction uses only previous positive E_i and a strictly positive E³ contribution; O follows positive convolution. Independently enumerated preference tuples n=1..6 and confirmed totals (n+1)^(n−1) and signed counts 1,1,4,11,72,335; exact recurrence/formal equations corroborated to further coefficients. Infinite positivity comes from the algebraic formal-series proof, not finite enumerations. Preference word inversion is not outcome sign.

## originality

PASS

Best-of-knowledge originality: relevant primary statement/implication comparisons do not cover the precisely stated contribution; no absolute priority certification. The signed aggregate is a nontrivial alternating sum; knowing atom weights formally determines it but does not mathematically imply strict positivity without an argument.

## value

PASS

Uniform preference sampling induces a nonuniform permutation distribution, and parity is a canonical global invariant of the resulting occupied-space order. A strict all-size direction of bias with an efficient exact signed recurrence is a substantive distributional law, beyond knowing probabilities of individual permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
