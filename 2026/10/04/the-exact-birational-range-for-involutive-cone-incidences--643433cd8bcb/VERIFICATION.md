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

The verifier checks the arithmetic identities and inequalities used in the reduction.

For \(m\ge3\), it checks
\[
G_n(m+1,m)-D_n(m)
=
\binom{m+2n-3}{m-1}-(2n-1)
\]
and verifies strict positivity throughout a broad finite range.

For \(m=2\), it checks the closed form
\[
G_n(4,2)-D_n(2)
=
\frac{2(n-1)(n+1)(2n-3)}{3},
\]
so monotonicity gives the strict sufficient criterion for every \(d\ge4\).

For the cubic-quadric case it checks
\[
D_n(2)=(n-1)(2n+1),
\]
\[
A_n(3,2)-H_0=D_n(2)+2n-2,
\]
and
\[
A_n(3,2)-H_2=D_n(2),
\]
together with
\[
2n-1<D_n(2),
\qquad
4n-4<D_n(2)
\]
for \(n\ge4\).

The script is not a proof of the infinite theorem. Monotonicity, rank bounds, irreducibility of the restricted quadric, restriction-map dimensions, and the incidence argument are proved in `RESULT.md`.

The saved replay output ends in `VERIFY_OK`.
