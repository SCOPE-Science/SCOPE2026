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

# Reproducibility and verification

Run `python3 check.py` using Python 3.9 or later; no third-party libraries or network connection are required. The checker uses exact `fractions.Fraction` for the Green entries, row sums, signs, Laplacian identities and norm polynomials for every integer \(3\le n\le250\). It performs a separately coded rational Gauss–Jordan inverse of \(L_n+J/n\) and subtracts \(J/n\) for \(3\le n\le12\). For the exact radical expression it uses finite-precision numerical comparisons as cross-checks, not certification of an algebraic identity. Expected message: `PASS: 64381 finite assertions (248 cycle orders, independent rational inversions for orders 3-12).`

The proof, not code, establishes all \(n\ge3\), exact equality of operator norms, uniform asymptotic estimates and equidistribution of fractional phases. An independent mathematical or bibliographic audit has not been performed.
