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

In the orthogonal drift eigenbasis the exact, balanced and symmetrized forcing weights are the inner product, geometric mean of squared norms, and arithmetic mean of squared norms of the two exponentials on [0,h]. Both inequalities are strict precisely for unequal rates. The shared accumulated propagation weights are positive and the initial term cancels, giving the Frobenius inequality including its strictness, repeated-rate, and commuting cases. Balanced covariance positivity is by congruence (rank preservation refers to the forcing increment). The symmetric defect is half the integral of the squared difference of the exponentials, with leading coefficient (a_i-a_j)^2 h^3/6. For the balanced defect divide the two-function Gram determinant by the sum of the exact and balanced weights: the determinant starts at (a_i-a_j)^2 h^4/12 and the denominator at 2h, giving 1/24. The smooth exponential left Riemann sum has O(h) error, giving the claimed fixed-T expansions, and the limiting defect matrix cannot vanish in the noncommuting case. In two modes the determinant gives exactly the correlation cutoff, with an increasing diagonal-weight ratio from 1 to b/a and thus a decreasing cutoff, including the two endpoint regimes. The exact increment is positive definite by strict Cauchy–Schwarz. The independent high-precision quadrature check brackets the example's crossing in (.28,.31) and gives defect ratio 3.9999000032933 at h=0.00001; it is not the universal proof.

## originality

PASS

Best-of-knowledge pass for the specific balanced scheme's simultaneous cone preservation, strict all-step comparison and asymptotic constant relative to symmetrized METD1, and the full normalized correlation frontier. Neither original METD1, Gramian positivity, nor the independently overlapping rank-one endpoint is credited as a distinct finding here.

## value

PASS

The cone requirement is inherent to covariance stepping, not an arbitrary parameter slice. For the symmetrized method the exact frontier decides when an output ceases to be a covariance even in the simplest noncommuting case, and the balanced method preserves the cone while reducing rather than trading away Frobenius accuracy. All-step strictness and the fixed-time 4:1 comparison make the structural contrast quantitative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
