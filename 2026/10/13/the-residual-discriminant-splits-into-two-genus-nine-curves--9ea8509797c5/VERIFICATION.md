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

The exact verifier reconstructs
\[
A(v),\ B(v),\ C(v),\ a,\ b,\ c
\]
and Burek's residual polynomial
\[
R=(dq^2+pq+h)^2-k^3q^2.
\]
It verifies exactly that
\[
R=d^2F_+F_-
\]
for the two displayed factors.

For each factor it checks
\[
\operatorname{disc}_q(F_\pm)=4\lambda_\pm^2A^3.
\]
It also verifies
\[
A=H_+H_-,
\qquad
C=\frac{H_+^3+H_-^3}{2},
\qquad
C\pm6i\sqrt3 B^2=H_\pm^3,
\]
and checks the square-freeness and coprimality used by the irreducibility argument.

The source transition
\[
w=v^{-1},\qquad t'=w^3t
\]
is replayed symbolically and gives the same weight for both factors.

The common-zero calculation verifies
\[
\operatorname{Res}_q(F_+,F_-)
=
\text{nonzero constant}\cdot B^4J,
\]
with \(J\) square-free of degree \(24\) and coprime to \(ABC\). Modulo \(J\), the common root is
\[
q=C/c.
\]
Thus the \(24\) source roots of \(J\) have four nonzero \(t\)-lifts each.

The divisor arithmetic is checked from the source intersection data:
\[
E^2=96,\qquad
K_{\mathcal B}\cdot E=-16,\qquad
p_a(E)=41.
\]
The eight simple \(A\)-roots give \(32\) cusps on each factor, and therefore
\[
g(\widetilde D_\pm)=41-32=9.
\]

The replay output ends in `VERIFY_OK`. The verifier checks the algebraic identities and finite exact arithmetic; the interpretation of local singularity type uses the initiating paper's proven node, cusp and boundary-smoothness results.
