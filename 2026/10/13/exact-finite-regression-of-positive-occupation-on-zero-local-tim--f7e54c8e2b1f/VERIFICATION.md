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

The theorem is analytic for every integer \(n\ge1\).

`checker.py` exhaustively enumerates all \(2^{2n}\) paths for \(1\le n\le8\). It verifies the exact mean and variance of zero local time, its covariance with strict positive occupation, and the conditional mean given each realized value of zero local time.

The same enumeration groups paths by the full reflected trajectory and checks the stronger identity
\[
\mathbb E[A_{2n}\mid\mathcal R_{2n}]
=
n-\frac12Z_{2n}
\]
on every reflected-path fiber.

A separate exact-rational calculation verifies the central-binomial telescoping identity, the return-probability convolution, and the closed variance formula through \(n=2000\). The asymptotic statement is proved from the standard central-binomial expansion and is not inferred from finite computation.
