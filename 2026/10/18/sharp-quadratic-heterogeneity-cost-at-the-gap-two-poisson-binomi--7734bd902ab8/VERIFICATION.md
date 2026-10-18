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

# Reproducibility and scope

Run \(\texttt{python check.py}\) using Python 3.10 or later with only the standard library. The code uses 80-digit decimal arithmetic and checks finite distribution identities against directly convolved binomial and nonidentical Bernoulli laws. It reports 438 passing assertions: 425 tests over 85 levels, five constrained-Hessian comparisons, and eight asymptotic-shape checks.

The proof is analytic. The checker does not certify all natural numbers, the local implicit-function theorem, or the inherited boundary-tie theorem. The crucial nonstandard premise is I. Kleiner, arXiv:2610.10664v1, Theorem 1 and Proposition 7, verified against the first-version full text. The coefficient expressions and derivative are reconstructed explicitly in RESULT.md. The strict sign is confined to \(k\ge1\) as required by the reference. No independent validation is asserted.
