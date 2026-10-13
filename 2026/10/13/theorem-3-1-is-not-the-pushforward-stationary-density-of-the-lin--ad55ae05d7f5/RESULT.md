# Theorem 3.1 is not the pushforward stationary density of the linearized stochastic chemostat

## Finding

The stochastic chemostat is
\[
dS=
\left[
D(S^0-S)-\frac{mSx}{a+S}
\right]dt,
\qquad
dx=
\left(
\frac{mS}{a+S}-D
\right)x\,dt+\sigma x\,dB.
\]

Theorem 3.1 is not the pushforward stationary density even of the paper's linearized Itô approximation. Two transformations in the derivation require corrections.

First, for
\[
Z=\log\frac{x}{x^*},
\]
Itô's formula gives
\[
dZ=
\left(
\frac{mS}{a+S}-D-\frac{\sigma^2}{2}
\right)dt+\sigma\,dB.
\]
The published logarithmic equation omits
\[
-\frac{\sigma^2}{2}.
\]

Second, after solving for a Gaussian density in logarithmic coordinates, the density must be transformed back with the Jacobian
\[
\left|
\frac{\partial(Y,Z)}{\partial(S,x)}
\right|
=
\frac{1}{Sx},
\qquad
Y=\log\frac{S}{S^*}.
\]
Theorem 3.1 omits this factor.

Keeping the paper's local coefficients \(a_{11},a_{12},a_{21}\), the corrected linearized model is an affine Ornstein-Uhlenbeck process. Its stationary law is Gaussian in \((Y,Z)\), and its pushforward to \((S,x)\) is therefore bivariate lognormal, not the expression printed in Theorem 3.1.

For the paper's parameter set
\[
S^0=4,\qquad D=2,\qquad m=3,\qquad a=1,
\]
the corrected log-microorganism variable has the exact stationary approximation
\[
\log\frac{x}{2}
\sim
N\!\left(
-\sigma^2,\frac{19\sigma^2}{16}
\right).
\]
This gives closed forms for the mode, mean, normalized variance, and the skewness statistic used in the paper.

## Assumptions and scope

The SDE is interpreted in the Itô sense, as required by the paper's diffusion-limit construction and Fokker-Planck equation.

The finding grants the paper its local linearization strategy. It does not claim that the resulting affine Ornstein-Uhlenbeck stationary law is the exact stationary law of the full nonlinear stochastic chemostat.

The deterministic positive equilibrium is denoted
\[
(S^*,x^*).
\]
The local drift matrix is
\[
A=
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&0
\end{pmatrix},
\]
using the source's coefficients. The stationary formulas below require \(A\) to be Hurwitz, which holds in the positive-equilibrium regime considered by the source.

## Proof

Set
\[
Y=\log\frac{S}{S^*},
\qquad
Z=\log\frac{x}{x^*}.
\]
Because \(S\) has no diffusion term, its logarithmic transformation uses the ordinary finite-variation chain rule. For \(x\), Itô's formula gives
\[
d\log x
=
\frac{1}{x}\,dx
-\frac{1}{2x^2}(dx)^2.
\]
Since
\[
(dx)^2=\sigma^2x^2\,dt,
\]
one obtains
\[
dZ=
\left(
\frac{mS}{a+S}-D-\frac{\sigma^2}{2}
\right)dt+\sigma\,dB.
\]

At the deterministic equilibrium,
\[
\frac{mS^*}{a+S^*}=D.
\]
Therefore the first-order log-space approximation is
\[
d\binom{Y}{Z}
=
\left[
A\binom{Y}{Z}
+
\binom{0}{-\sigma^2/2}
\right]dt
+
\binom{0}{\sigma}dB.
\]

The stationary mean \(\mu\) solves
\[
A\mu+\binom{0}{-\sigma^2/2}=0.
\]
Solving gives
\[
\mu_Y=\frac{\sigma^2}{2a_{21}},
\qquad
\mu_Z=-\frac{a_{11}\sigma^2}{2a_{12}a_{21}}.
\]

The stationary covariance \(\Sigma\) solves
\[
A\Sigma+\Sigma A^T+
\begin{pmatrix}
0&0\\
0&\sigma^2
\end{pmatrix}
=0,
\]
and therefore
\[
\Sigma_{11}
=
\frac{a_{12}\sigma^2}{2a_{11}a_{21}},
\quad
\Sigma_{12}
=
-\frac{\sigma^2}{2a_{21}},
\]
\[
\Sigma_{22}
=
\frac{(a_{11}^2-a_{12}a_{21})\sigma^2}
{2a_{11}a_{12}a_{21}}.
\]

Thus \((Y,Z)\) has a Gaussian stationary density. The inverse logarithmic transformation has Jacobian
\[
\left|
\frac{\partial(Y,Z)}{\partial(S,x)}
\right|
=
\frac{1}{Sx}.
\]
Consequently
\[
p_{S,x}(S,x)
=
\frac{1}{2\pi Sx\sqrt{\det\Sigma}}
\exp\!\left[
-\frac12
(\ell-\mu)^T\Sigma^{-1}(\ell-\mu)
\right],
\]
where
\[
\ell=
\binom{\log(S/S^*)}{\log(x/x^*)}.
\]

The omitted \(1/(Sx)\) cannot be absorbed into a normalization constant. Hence the source's formula is not the pushforward density of the Gaussian law it derives.

For
\[
S^0=4,\quad D=2,\quad m=3,\quad a=1,
\]
the deterministic positive equilibrium is
\[
(S^*,x^*)=(2,2),
\]
and the source coefficients simplify to
\[
a_{11}=-\frac83,\qquad a_{12}=-2,\qquad a_{21}=\frac23.
\]
Substitution gives
\[
\mu=\binom{3\sigma^2/4}{-\sigma^2},
\]
\[
\Sigma=
\sigma^2
\begin{pmatrix}
9/16&-3/4\\
-3/4&19/16
\end{pmatrix}.
\]

Therefore
\[
Z\sim N\!\left(-\sigma^2,\frac{19\sigma^2}{16}\right).
\]
The marginal \(x=2e^Z\) is lognormal, with
\[
\operatorname{mode}(x)
=
2\exp\!\left(-\frac{35\sigma^2}{16}\right),
\]
\[
\mathbb E[x]
=
2\exp\!\left(-\frac{13\sigma^2}{32}\right).
\]

The normalized variance defined in the source is
\[
V_x
=
\frac{\mathbb E[x^2]}{\mathbb E[x]^2}-1
=
\exp\!\left(\frac{19\sigma^2}{16}\right)-1.
\]
Its skewness statistic is
\[
S_x
=
\frac{\mathbb E[x^3]}{\mathbb E[x]^3}
-3V_x-1
=
\exp\!\left(\frac{57\sigma^2}{16}\right)
-3\exp\!\left(\frac{19\sigma^2}{16}\right)
+2.
\]
Both are strictly increasing for \(\sigma>0\).

## Verification

The bundled `verify.py` applies Itô's formula symbolically, solves the affine Ornstein-Uhlenbeck mean equation and covariance Lyapunov equation, and verifies the inverse Jacobian.

For the source parameters it reproduces
\[
\mu_Y=\frac{3\sigma^2}{4},
\qquad
\mu_Z=-\sigma^2,
\]
and
\[
\Sigma_{22}=\frac{19\sigma^2}{16}.
\]

At
\[
\sigma=0.15,
\]
it returns
\[
\operatorname{mode}(x)\approx1.9039457257,
\qquad
\mathbb E[x]\approx1.9818020470.
\]

The verification concerns the linearized approximation only; no claim about an exact nonlinear stationary density is inferred from it.

## Relationship to prior work

The motivating paper derives a Gaussian stationary density after logarithmic transformation and local linearization, then converts that expression back to substrate and microorganism concentrations and uses it for marginal densities, variance, and skewness.

Density-function calculations around deterministic equilibria are established in stochastic population and epidemic modeling. For example, Liu and Chen study Fokker-Planck density functions around an endemic equilibrium for a different stochastic SEIS model. That broader literature supplies methodology, not the source-specific correction here.

The new content is the exact reconstruction of the two transformations in this chemostat paper: the Itô drift correction in the logarithm and the nonconstant \(1/(Sx)\) Jacobian in the pushforward density. The resulting corrected affine approximation gives explicit lognormal statistics for the paper's numerical parameter set.

Searches by DOI, exact title, Itô-correction terminology, logarithmic-change-of-variable terminology, Jacobian terminology, and correction or erratum terminology did not locate a published repair of Theorem 3.1.

## Limitations

The corrected formulas are stationary formulas for the paper's local affine approximation, not an exact stationary law for the nonlinear SDE.

The qualitative conclusion that the source's normalized variance and skewness increase with noise survives in the corrected affine approximation.

The paper's plotted densities and numerical moments may have been generated by implementation choices not recoverable from the article; the finding establishes what follows from the published derivation.

## References

1. J. Yang, Z. Zhao, X. Song, “Statistical property analysis for a stochastic chemostat model with degenerate diffusion,” AIMS Mathematics 8 (2023), 1757–1769. DOI: 10.3934/math.2023090.
2. Q. Liu, Q. Chen, “Density function analysis for a stochastic SEIS epidemic model with non-degenerate diffusion,” Discrete and Continuous Dynamical Systems - B 26 (2021), 4359–4373. DOI: 10.3934/dcdsb.2020291.
