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
The symbolic input is the Veronese polar vector
\[
\delta_i
=
\binom{n+1}{i+1}e^i(e-1)^{n-i}.
\]

For
\[
N=n+1,
\qquad
a_k=\delta_{k-1},
\]
the exact gcd proof is prime-wise. A prime not dividing \(e\) is excluded by
\[
a_N=e^{N-1}.
\]
For a prime dividing \(e\),
\[
\nu_p(a_k)
=
\nu_p\binom Nk+(k-1)\nu_p(e)
\]
and
\[
\nu_p\binom Nk\ge\nu_p(N)-\nu_p(k),
\]
so all terms have valuation at least \(\nu_p(N)\), with equality at \(k=1\).

The bundled checker independently compares the closed polar vector with the Chern-class summation, verifies the gcd theorem over a broad finite parameter grid, and checks the generic Euclidean-distance-degree sum. These finite checks are regression evidence only.

Limits: complex Veronese varieties, the complete polar vector, and the standard projective polar-degree convention.
