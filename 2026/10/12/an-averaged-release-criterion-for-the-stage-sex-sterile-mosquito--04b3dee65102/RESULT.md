# An averaged release criterion for the stage–sex sterile-mosquito model

## Finding

Consider the nonautonomous scalar equation for wild adult females
\[
F'
=
\frac{A F^2}
{(BF+C)\left[DF+HM_s(t)(BF+C)\right]}
-\delta_FF.
\]
Write its per-capita birth term as
\[
q(F,M)
=
\frac{AF}
{(BF+C)\left[DF+HM(BF+C)\right]}.
\]

For each fixed sterile-male abundance \(M\ge0\), the exact upper envelope over the wild-female state is
\[
Q(M)
=
\sup_{F>0}q(F,M)
=
\frac{A}
{C\left(\sqrt{D+BHM}+\sqrt{BHM}\right)^2}.
\]
Therefore
\[
\frac{F'}{F}
\le
Q(M_s(t))-\delta_F
\]
and every positive solution satisfies
\[
F(t)
\le
F(0)
\exp\!\left(
\int_0^t
[Q(M_s(\tau))-\delta_F]\,d\tau
\right).
\]

It follows that
\[
\limsup_{T\to\infty}
\frac1T
\int_0^T Q(M_s(t))\,dt
<
\delta_F
\]
is a sufficient condition for global exponential extinction.

For a periodic release profile of period \(P\), this reduces to the one-period condition
\[
\frac1P\int_0^P Q(M_s(t))\,dt<\delta_F.
\]

Using the parameter values displayed by He, Li, and Liu and their construction of the egg carrying capacity, the source's intermediate sinusoidal case
\[
M_s(t)
=
1.2\times10^5
\left(
1.3+\sin\frac{\pi t}{8}
\right)
\]
has
\[
\frac1{16}
\int_0^{16}
Q(M_s(t))\,dt
\approx
0.0382217709502678042
<
0.04
=
\delta_F.
\]
Hence the global extinction displayed numerically in the source's Figure 2(a) follows analytically from this averaged criterion even though the release profile repeatedly falls below the source's constant-release threshold.

For the source's second crossing-threshold profile,
\[
M_s(t)
=
6\times10^4
\left(
1.3+\sin\frac{\pi t}{8}
\right),
\]
the average is
\[
0.0737501718144166751>0.04.
\]
The criterion therefore makes no extinction claim in that case, consistent with the source's observed bistability.

For this sinusoidal family, the numerical crossing of the sufficient envelope condition is
\[
s_{\rm env}
\approx
114458.945543703.
\]

## Assumptions and scope

The model parameters
\[
A,B,C,D,H,\delta_F
\]
are positive, and the sterile-male profile satisfies
\[
M_s(t)\ge0.
\]
The state is considered for positive initial data
\[
F(0)>0.
\]

The theorem is a sufficient extinction result. It does not assert that failure of the averaged inequality implies persistence or bistability.

The quantity
\[
s_{\rm env}
\]
is the crossing point of this sufficient criterion for the stated sinusoidal family. It is not claimed to be the sharp extinction threshold of the original nonautonomous nonlinear equation.

The numerical application uses the parameter values printed by the source and computes the carrying capacity from the same equilibrium identities used in its numerical section.

## Proof

Set
\[
x=\frac{BF}{C},
\qquad
u=BHM.
\]
Then
\[
q(F,M)
=
\frac{A}{C}
\frac{x}
{(x+1)\left[(D+u)x+u\right]}.
\]
The denominator of the rational factor is
\[
(D+u)x^2+(D+2u)x+u.
\]
Differentiating gives a numerator proportional to
\[
u-(D+u)x^2.
\]
For \(M>0\), the unique positive maximizer is therefore
\[
x_*=
\sqrt{\frac{u}{D+u}}.
\]
Writing
\[
a=\sqrt{D+u},
\qquad
b=\sqrt u,
\]
one has
\[
x_*=\frac ba
\]
and direct substitution yields
\[
\frac{x_*}
{(x_*+1)\left[(D+u)x_*+u\right]}
=
\frac1{(a+b)^2}.
\]
Thus
\[
Q(M)
=
\frac{A}
{C\left(\sqrt{D+BHM}+\sqrt{BHM}\right)^2}.
\]
When \(M=0\), the same expression gives the supremum as \(F\downarrow0\).

The differential equation now gives
\[
F'
=
F\left[q(F,M_s(t))-\delta_F\right]
\le
F\left[Q(M_s(t))-\delta_F\right].
\]
Integration of this scalar differential inequality gives
\[
F(t)
\le
F(0)
\exp\!\left(
\int_0^t
[Q(M_s(\tau))-\delta_F]\,d\tau
\right).
\]

If the limsup time average of \(Q(M_s)\) is strictly smaller than \(\delta_F\), choose
\[
\varepsilon>0
\]
so that eventually
\[
\frac1T\int_0^T Q(M_s(t))\,dt
\le
\delta_F-\varepsilon.
\]
The preceding bound then gives exponential decay at rate at least \(\varepsilon\), up to a fixed finite-time prefactor.

For a \(P\)-periodic \(M_s\), the long-time average is exactly the one-period average.

The source's pointwise theorem requires the asymptotic lower envelope of \(M_s\) to exceed its constant-release threshold. In the \(s=1.2\times10^5\) sinusoid, the minimum is
\[
0.3s=36000,
\]
far below the source's reported threshold near
\[
9.5\times10^4.
\]
Hence that theorem does not apply, while the averaged envelope inequality does.

## Verification

The bundled `verify.py` reconstructs the source parameters using exact rational arithmetic:
\[
\nu=\frac{49}{100},
\quad
\beta_E=10,
\quad
\nu_E=\frac1{20},
\quad
\delta_E=\frac3{100},
\quad
\delta_F=\frac1{25},
\quad
\delta_M=\frac1{10},
\quad
\gamma_s=1.
\]
It also reconstructs the carrying capacity from the source's equilibrium calculation with
\[
M^*=F^*=5106.
\]

The script checks the algebraic maximizer symbolically, evaluates the period averages at 80-digit precision, and independently repeats them with a high-resolution composite Simpson rule. The two numerical methods agree well beyond the precision needed to determine the signs relative to
\[
\delta_F=0.04.
\]

It verifies
\[
\overline Q(1.2\times10^5)
\approx
0.0382217709502678042
\]
and
\[
\overline Q(6\times10^4)
\approx
0.0737501718144166751.
\]

The general extinction theorem is analytic; numerical quadrature is used only to apply it to the source's displayed sinusoidal examples.

## Relationship to prior work

He, Li, and Liu derive the nonautonomous stage–sex suppression equation and prove a global extinction condition based on an asymptotic pointwise lower bound for the sterile-male population. They explicitly note that their pointwise conditions are sufficient rather than necessary and leave two profiles that cross the constant-release threshold to numerical simulation. Their Figure 2(a) displays global extinction for the \(1.2\times10^5\) sinusoidal scale, whereas Figure 2(b) displays bistability at \(6\times10^4\).

Earlier sterile-insect literature contains periodic and impulsive release analyses for different models. Huang, Liu, and Song study a higher-dimensional two-sex, stage-structured model with impulsive releases and derive threshold conditions for a mosquito-free periodic solution. A later delayed stage–sex model by Huang, Liu, and Song also studies periodic releases and stability according to the relation between release period and sterile-male sexual lifespan.

A 2020 one-sided competition model also contains periodic mass-release extinction conditions. Those models and release mechanisms differ from the scalar nonautonomous equation treated here.

The present result is therefore not a general novelty claim about periodic sterile-insect control. It is a source-specific analytic closure of the explicit gap left between the pointwise sufficient theorems and the source's crossing-threshold numerical profiles.

## Limitations

The averaged condition is sufficient, not necessary. In particular, its failure at the \(6\times10^4\) profile does not prove bistability.

The envelope
\[
Q(M)
\]
maximizes instantaneous per-capita birth over all positive wild-female states. This state-independent maximization is what makes the criterion global, but it can be conservative.

The later periodic-compensation paper was available only through bibliographic metadata and its abstract during this comparison, so it remains a residual literature risk for a more specialized periodic-release theorem.

The source's rounded constant-release threshold differs slightly from the value obtained by recomputing all displayed parameters without intermediate rounding. The accepted result does not depend on that discrepancy.

## References

1. J. He, D. Li, S. Liu, “Global dynamics of a mosquito population suppression model with stage and sex structure,” AIMS Mathematics 8 (2023), 14027–14046. DOI: 10.3934/math.2023717.
2. M. Huang, S. Liu, X. Song, “Study of the sterile insect release technique for a two-sex mosquito population model,” Mathematical Biosciences and Engineering 18 (2021), 1314–1339. DOI: 10.3934/mbe.2021069.
3. M. Huang, S. Liu, X. Song, “Modeling of periodic compensation policy for sterile mosquitoes incorporating sexual lifespan,” Mathematical Methods in the Applied Sciences 46 (2023), 5725–5741. DOI: 10.1002/mma.8864.
4. “A One-Sided Competition Mathematical Model for the Sterile Insect Technique,” Complexity (2020), Article 6246808. DOI: 10.1155/2020/6246808.
