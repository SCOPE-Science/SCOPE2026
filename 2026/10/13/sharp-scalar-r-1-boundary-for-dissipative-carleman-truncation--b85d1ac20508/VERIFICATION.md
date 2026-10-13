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

The universal proof is analytic and is given in `RESULT.md`.

For the scalar lift,
\[
\dot y_j=-ja\,y_j-jb\,y_{j+1},
\]
the order-\(N\) first component is
\[
\widehat u_N(t)
=
u_0e^{-at}
\sum_{k=0}^{N-1}
[-R(1-e^{-at})]^k.
\]
Combining this finite geometric sum with
\[
u(t)=\frac{u_0e^{-at}}{1+R(1-e^{-at})}
\]
gives the exact relative error
\[
[R(1-e^{-at})]^N.
\]
This identity, rather than finite numerical sampling, proves the convergence trichotomy.

At \(R=1\), direct differentiation of
\[
\frac{x(1-x)^N}{2-x}
\]
gives
\[
N x^2-2(N+1)x+2=0,
\]
whose unique root in \((0,1)\) is the displayed \(x_N\). This proves the exact critical maximum and its \(N^{-1}\) asymptotic.

For the lifted system under the source-prescribed scaling, the alternating vector gives
\[
v^\dagger H_Nv
=
\frac N2[(c-a)N-(a+c)],
\qquad
\frac ca=\frac{1+R}{2}.
\]
Therefore every \(R>1\) eventually yields a positive Rayleigh quotient.

The bundled checker reconstructs representative finite sections directly and compares them with the closed form, verifies the critical maximizer numerically, and checks the Rayleigh identity. These calculations only replay the analytic proof.

Limits: the theorem does not determine the smallest non-dissipative truncation order, and it does not classify stronger-nonlinearity behavior outside the stated scalar family.
