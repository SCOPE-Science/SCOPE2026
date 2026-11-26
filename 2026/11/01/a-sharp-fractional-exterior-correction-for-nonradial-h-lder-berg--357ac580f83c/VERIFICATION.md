---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With the inner product linear in its first slot, the conjugate angular mode gives the sole lower off-diagonal moment 2ε B(2n+2,1+α+iτ); all diagonals are unchanged. Projection of z^n onto the lower-degree space is therefore entirely in the q_(n−1) direction. For monic norms the exact recursion t_n=1−n(n+1)|γ_n|²/t_(n−1), t_n=(n+1)h_n, and the lower bound t_n≥1−2|ε| give the quadratic leading-coefficient term with positive sign. The gamma quotient gives a_n=γ_n/h_(n−1)=A n^(−α−iτ)(1+O(n^−1+n^−(2α))). On the full exterior |1/z|≤1 and a_n→0, so the monic ratio recursion is uniformly bounded and one substitution gives the −a_n/z term with O(n^−(2α)) error. The full replacement error in Step 4 is O(n^(−α−1)+n^(−3α)), not in general just O(n^(−α−1)); both terms are absorbed by the proved remainder. Homogeneity and boundedness of (1−t^(α−iτ))/(1−t)^α on [0,1) give the Hölder extension. Gamma has no zeros, and for τ≠0 rounding exp((2πm+θ)/|τ|) gives subsequences approaching every prescribed phase; τ=0 gives the single stated limit.

## originality

PASS

The supported distinction is the sharp explicit endpoint correction, quadratic normalization and phase cluster law for a positive one-mode Hölder area weight, not the known leading Bergman asymptotic, the beta integral or the tridiagonal method.

## value

PASS

The example gives an actual obstruction to improving the rate to little-o(n^−α) from Hölder regularity and constant boundary trace alone, even at a single fixed exterior point. The separation of the leading-coefficient and exterior scales, and the optional phase oscillation, give a benchmark for endpoint claims that a generic rate estimate cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
