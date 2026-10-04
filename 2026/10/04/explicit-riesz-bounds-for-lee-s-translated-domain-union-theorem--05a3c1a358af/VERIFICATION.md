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

The claim is analytic. No finite experiment or external certificate is used.

For the lower Riesz estimate, define \(q=p_1+p_2\). The lattice condition on \(\Lambda_2\) gives \(p_2(x+a)=p_2(x)\). Because \(S_1\) and \(S_1+a\) are disjoint subsets of \(S_1\cup S_2\),
\[
\int_{S_1}|q(x+a)-q(x)|^2\,dx\le 2\|q\|_{L^2(S_1\cup S_2)}^2.
\]
The lower Riesz bound on \(S_1\), after multiplying coefficients by \(e^{2\pi i a\cdot\lambda}-1\), gives the factor \(A_1m^2\). The subsequent estimate of \(p_2=q-p_1\) on \(S_2\) uses exactly the cross Bessel bound \(C_{12}\). Algebraic addition yields
\[
L=\frac{A_1A_2m^2}{2(A_2+A_1m^2+2C_{12})}.
\]

For the upper estimate, \(p_1\) contributes at most \((B_1+C_{12})\|c_1\|_2^2\). Periodicity transfers the \(S_1\) energy of \(p_2\) into \(S_1+a\subset S_2\), so its total contribution is at most \(2B_2\|c_2\|_2^2\). Cauchy--Schwarz then gives
\[
U=B_1+C_{12}+2B_2.
\]

Completeness was checked independently: an orthogonal \(f=f_1+f_2\) gives, after translating \(f_1\) into \(S_2\), a function orthogonal to \(E(\Lambda_2)\); it is therefore zero. The remaining \(\Lambda_1\) Fourier coefficients are multiplied by the nonzero phase factor \(1-e^{-2\pi i a\cdot\lambda}\), so completeness of \(E(\Lambda_1)\) forces \(f_1=0\) and then \(f_2=0\).

Limits: the constants are sufficient rather than optimal; a numerical application needs an estimate of \(C_{12}\); the proof does not cover the source's multi-coset variants.
