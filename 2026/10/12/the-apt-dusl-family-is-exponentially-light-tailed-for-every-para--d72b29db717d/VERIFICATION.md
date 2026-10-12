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
Let
\[
S_L(x)
=
\left(
1+\frac{\xi x}{1+\xi}
\right)e^{-\xi x}.
\]
For the DUS-Lindley CDF \(H\),
\[
1-H(x)
=
\frac{e\{1-e^{-S_L(x)}\}}{e-1}
\sim
\frac{e}{e-1}S_L(x).
\]

For the alpha-power transformation, define
\[
c(\alpha)
=
\begin{cases}
\dfrac{\alpha\log\alpha}{\alpha-1},&\alpha\ne1,\\[4pt]
1,&\alpha=1.
\end{cases}
\]
Then
\[
1-F(x)
\sim
c(\alpha)\{1-H(x)\}.
\]
Therefore
\[
1-F(x)
\sim
c(\alpha)\frac{e}{e-1}\frac{\xi}{1+\xi}
x e^{-\xi x}.
\]

The density has the corresponding asymptotic
\[
f(x)
\sim
c(\alpha)\frac{e}{e-1}\frac{\xi^2}{1+\xi}
x e^{-\xi x},
\]
so
\[
h(x)\to\xi.
\]

The tail-integral identity for exponential moments then gives
\[
\mathbb E[e^{tX}]<\infty
\quad\Longleftrightarrow\quad
t<\xi.
\]

The included checker evaluates the exact transformed CDF and PDF and confirms the survival ratio, density ratio, limiting hazard, and boundary integrand for several parameter pairs.
