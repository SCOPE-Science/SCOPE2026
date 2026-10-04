---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The all-parameter theorem is established by the proof in `RESULT.md`; finite computation is not used to infer an infinite statement.

The standalone `verify.py` checker uses only the Python standard library. It checks, for every \(3\le n\le80\), the normalized continuous extremizer, its first cosine coefficient, the polynomial identity
\[
(1-2\cos(\pi/(n+2))z+z^2)B(z)=\sin(\pi/(n+2))(1+z^{n+2}),
\]
and all explicit dual contact-weight moments. It also checks, for every \(3\le n\le80\) and \(3\le N\le500\), by exact integer denominator arithmetic, that all contact roots lie on the cyclic \(N\)-grid exactly when \(2(n+2)\mid N\).

A successful replay prints
`extremizer_cases=78`,
`dual_weight_cases=78`,
`grid_divisibility_cases=38844`,
and `VERIFY_OK`.

The checker does not solve the sampled linear program for infinitely many parameters and is not offered as a novelty certificate. The strict off-mesh result instead follows analytically from linear-programming dual support, Chebyshev moment uniqueness, and the exact reduced denominators of two contact roots.
