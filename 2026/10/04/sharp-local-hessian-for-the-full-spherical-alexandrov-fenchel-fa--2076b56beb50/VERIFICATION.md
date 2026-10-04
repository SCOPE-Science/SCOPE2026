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

The analytic proof uses the source first-variation identity
\[
\delta A_{j-1}=d_j\int uE_j\,d\mu
\]
and the exact source formula for \(f_j'(R)\). At a geodesic sphere, the standard variation of the Weingarten map and area form gives the second variation used in `RESULT.md`.

`verify.py` was executed from the packaged artifact path. It checks exact rational instances of every algebraic cancellation for dimensions \(2\le n\le12\), every \(-1\le\ell<k\le n-1\), and several positive rational values of \(c^2\). It also verifies the harmonic factorization and that degree two is the smallest positive shape factor after degrees zero and one.

The checker is not a proof by enumeration. The universal conclusion follows from the symbolic identities written in `RESULT.md` and the exact round-sphere Laplace spectrum. No global stability radius, nonlinear sharp remainder, or independent validation is claimed.
