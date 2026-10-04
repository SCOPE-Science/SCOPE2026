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

The proof was checked at the level of definitions, quantifiers, normalizations, and limiting operations.

The source matrix entry
\[
-\iint_{\mathbb R_-^2}\frac{\psi_{n,-k}(x)\psi_{m,-\ell}(y)}{x+y}\,dx\,dy
\]
becomes
\[
\iint_{\mathbb R_+^2}\frac{\psi_{n,k-1}(u)\psi_{m,\ell-1}(v)}{u+v}\,du\,dv
\]
after \(x=-u\), \(y=-v\) and the source reflection identity. This is the Carleman matrix element with no leftover sign or scale factor.

The external non-elementary input was checked against the published Carleman diagonalization. Under the Mellin transform its quadratic form multiplier is
\[
\frac{\pi}{\cosh(\pi\xi)},
\]
so the operator is positive and has norm \(\pi\).

For the lower bound, the dilation
\[
(D_ag)(x)=a^{-1/2}g(x/a)
\]
is unitary and satisfies \(CD_a=D_aC\). Its integral is exactly \(a^{1/2}\int g\). Subtracting this integral times \(2\mathbf 1_{[1/2,1]}\) therefore changes the \(L^2\) vector by a quantity tending to zero while forcing zero mean on \((0,1)\). The standard Haar wavelets of nonnegative scale span precisely the mean-zero subspace on \((0,1)\), and every finite subset of those wavelets occurs in some \(V_{N,K}\).

Boundedness of \(C\) makes Rayleigh quotients continuous under these \(L^2\) approximations. Thus the argument proves the infinite quantifier required by Conjecture B; numerical convergence data are not used as a certificate.

Limits: no explicit convergence rate in \(N,K\) is proved, and the separate fixed-\(K\) Fourier-symbol maximization conjecture is not addressed.
