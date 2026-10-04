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

The verification uses only the finite part of the primary lower-bound construction.

For
\[
\chi_N
=
\frac1N\sum_{j=1}^N\varphi_{Q_j},
\]
each packet is nonnegative and has integral one, hence
\[
\|\chi_N\|_1=1.
\]

The modulation block used in the proof is
\[
\Theta_N^0
=
\left[
A_1^{-1}2^{N^2/2},
A_1 2^{3N^2/4}
\right]\cap2^{\mathbb N}.
\]
Its exponent interval has length
\[
N^2/4+O(1),
\]
so
\[
|\Theta_N^0|\asymp N^2.
\]

The source Bohr-set argument constructs
\[
|E_N|\gtrsim N
\]
and, for each \(x\in E_N\), chooses
\[
\lambda_0\in\Theta_N^0
\]
for which the stationary harmonic sum is at least
\[
c\frac{\log N}{N}.
\]
The source error terms are chosen smaller than a fixed fraction of this level. Therefore
\[
\inf_{x\in E_N}
\mathcal C_{2,\Theta_N^0}\chi_N(x)
\gtrsim
\frac{\log N}{N}.
\]

It follows immediately that
\[
\|\mathcal C_{2,\Theta_N^0}\|_{L^1\to L^{1,\infty}}
\gtrsim
\log N.
\]

For an arbitrary sufficiently large integer \(M\), choose
\[
N=\lfloor\sqrt M\rfloor
\]
and enlarge the source block to exactly \(M\) consecutive dyadic powers. Pointwise maxima are monotone under enlargement of the parameter set, while
\[
N\asymp\sqrt M,
\qquad
\log N\asymp\log M.
\]
This gives the stated \(M\)-parameter level set and weak norm.

No finite numerical experiment, extrapolation, or infinite limiting argument is used.
