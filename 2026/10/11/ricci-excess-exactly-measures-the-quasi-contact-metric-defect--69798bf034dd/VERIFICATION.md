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

The analytic proof uses two source identities:
\[
B:=d\eta-2\Phi=-2g(\phi h\,\cdot,\cdot)
\]
for Killing characteristic field, and
\[
\operatorname{Ric}(\xi,\xi)=2n+\|h\|_{\mathrm{HS}}^2.
\]

For a skew-adjoint endomorphism \(K\), the two-form
\[
\omega_K(X,Y)=g(KX,Y)
\]
satisfies
\[
\|\omega_K\|^2=\frac12\|K\|_{\mathrm{HS}}^2.
\]
Since \(\phi\) is orthogonal on \(\ker\eta\),
\[
\|B\|^2=2\|h\|_{\mathrm{HS}}^2.
\]
The quasi-contact type decomposition gives
\[
B\perp\Phi,
\qquad
\|\Phi\|^2=n.
\]
These facts imply
\[
\|d\eta\|^2
=
4n+2\|h\|_{\mathrm{HS}}^2
=
2\operatorname{Ric}(\xi,\xi).
\]

The packaged checker replays these scalar consequences symbolically and checks the source's five-dimensional family using an exact horizontal matrix model. It does not infer the arbitrary-dimensional theorem from finite examples; that theorem is the analytic norm computation above.
