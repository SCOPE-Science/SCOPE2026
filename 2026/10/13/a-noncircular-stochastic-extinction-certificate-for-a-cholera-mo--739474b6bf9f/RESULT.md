# A noncircular stochastic extinction certificate for a cholera model

## Finding

Consider the stochastic cholera system
\[
\begin{aligned}
dS&=\left[\Lambda-\frac{\beta_cSB}{K+B}-\beta_hSI-\mu S\right]dt-\xi SI\,dW,\\
dI&=\left[\frac{\beta_cSB}{K+B}+\beta_hSI-(\alpha+\mu+\epsilon)I\right]dt+\xi SI\,dW,\\
dR&=(\alpha I-\mu R)dt,\\
dB&=(\sigma I-\omega B)dt+\zeta B\,dY.
\end{aligned}
\]
Write
\[
H=\frac{\Lambda}{\mu},
\qquad
\mu_1=\mu+\alpha+\epsilon.
\]

The source introduces a positive Lyapunov weight \(g\), sets
\[
u=I+gB,
\]
and obtains a noise coefficient
\[
k(g)
=
\xi^2\frac{\zeta/g}
{\sqrt{(\zeta/g)^2+(H\xi)^2}}.
\]
It then defines
\[
R^*
=
R_0\frac{\mu_1}{\mu_1+kH^2/2}
\]
before fixing \(g\). Later, in the proof of the extinction theorem, \(g\) is chosen from an inequality that already involves \(k\). Thus the printed \(R^*\) is not a model invariant unless the proof weight is fixed first.

The dependence is substantial. Since \(k(g)\) decreases continuously from \(\xi^2\) to \(0\) as \(g\) increases from \(0\) to infinity,
\[
R_0\frac{\mu_1}{\mu_1+\xi^2H^2/2}
<
R^*(g)
<
R_0.
\]
The same physical model can therefore make this printed scalar lie on either side of one by changing only the auxiliary proof weight.

There is an exact noncircular repair inside the same Lyapunov framework. Define
\[
g_0=\frac{\beta_cH}{\omega K}
\]
and
\[
\Phi(g)
=
\max_{0\le s\le H}
\left(
\beta_hs-\frac{k(g)}2s^2
\right).
\]
Then
\[
\Phi(g)=
\begin{cases}
\beta_hH-\dfrac{k(g)}2H^2,
&
k(g)H\le\beta_h,\\[2mm]
\dfrac{\beta_h^2}{2k(g)},
&
k(g)H>\beta_h.
\end{cases}
\]

There exists a weight \(g>g_0\) for which both coefficient bounds in the source's \(\log(I+gB)\) calculation are strictly negative if and only if
\[
\boxed{
\Phi(g_0)+g_0\sigma<\mu_1
}.
\]
Whenever this holds, the same martingale argument used by the source yields almost-sure exponential extinction of \(I\) and \(B\).

For the parameter set used in Section 6.3, the repaired condition holds with a substantial margin:
\[
\Phi(g_0)+g_0\sigma
=
0.9069481218\ldots
<
1.0152548
=
\mu_1.
\]
At the boundary weight,
\[
R^*(g_0)=0.9053382105\ldots,
\]
which explains the paper's reported \(0.905\). Thus its numerical extinction example remains valid after replacing the circular threshold by the noncircular feasibility test.

## Assumptions and scope

All parameters are positive and the solution remains in the source's positive region with
\[
S(t)\le H.
\]
The result concerns the coefficientwise Lyapunov certificate based on
\[
u=I+gB.
\]
The condition derived here is necessary and sufficient for feasibility of that particular proof architecture; it is not claimed to be necessary for actual stochastic extinction of the model.

The Brownian motions are those in the source. The repair does not change the stochastic differential equations, the deterministic reproduction number, or the data-fitting section.

## Proof

The source's logarithmic Lyapunov calculation gives
\[
L\log u
=
\left(\beta_hS+g\sigma-\mu_1\right)\frac Iu
+
\left(\frac{\beta_cS}{K+B}-g\omega\right)\frac Bu
-
E,
\]
and its quadratic-variation estimate implies
\[
E
\ge
\frac{k(g)}2S^2\frac Iu.
\]
Therefore
\[
L\log u
\le
\left(
\beta_hS-\frac{k(g)}2S^2+g\sigma-\mu_1
\right)\frac Iu
+
\left(
\frac{\beta_cS}{K+B}-g\omega
\right)\frac Bu.
\]

Since
\[
0\le S\le H
\]
and
\[
K+B\ge K,
\]
the environmental-virus coefficient is bounded above by
\[
\frac{\beta_cH}{K}-g\omega.
\]
It is strictly negative exactly when
\[
g>g_0=\frac{\beta_cH}{\omega K}.
\]

The infected coefficient is bounded above by
\[
\Phi(g)+g\sigma-\mu_1.
\]
The function \(k(g)\) is strictly decreasing. For every fixed \(s\), the expression
\[
\beta_hs-\frac{k(g)}2s^2
\]
is therefore nondecreasing in \(g\), so \(\Phi(g)\) is nondecreasing. Because \(\sigma>0\),
\[
F(g)=\Phi(g)+g\sigma
\]
is strictly increasing.

Consequently, there exists some
\[
g>g_0
\]
with
\[
F(g)<\mu_1
\]
if and only if
\[
F(g_0)<\mu_1.
\]
This proves the boxed criterion.

If the criterion holds, continuity gives a \(g>g_0\) for which both coefficient upper bounds are at most a common negative constant \(-c\). Since
\[
\frac Iu+g\frac Bu=1,
\]
the two weighted terms yield a uniform negative drift after rescaling the second coefficient by \(g\). The martingale strong-law step in the source then gives
\[
\limsup_{t\to\infty}\frac1t\log(I(t)+gB(t))<0
\]
almost surely, and hence exponential extinction of both \(I\) and \(B\).

Finally,
\[
k(g)
=
\xi^2\frac{\zeta}
{\sqrt{\zeta^2+(gH\xi)^2}}
\]
after multiplying numerator and denominator by \(g\). Thus
\[
k(g)\downarrow0
\]
as \(g\to\infty\) and
\[
k(g)\uparrow\xi^2
\]
as \(g\downarrow0\). Substitution into the printed \(R^*\) formula proves the displayed interval.

## Verification

The bundled checker evaluates the Section 6.3 parameter set and verifies:

- the value of \(g_0\);
- the value and branch of \(k(g_0)\);
- the exact quadratic maximum \(\Phi(g_0)\);
- the strict margin in the repaired certificate;
- the source's rounded value \(R^*(g_0)\approx0.905\);
- monotonic decrease of \(k(g)\) and monotonic increase of \(\Phi(g)+g\sigma\) over a wide numerical grid.

Those calculations corroborate the analytic proof; the universal monotonicity and feasibility equivalence are established symbolically above.

## Relationship to prior work

The motivating paper derives \(k\) from a lower bound on the quadratic variation after introducing an arbitrary positive weight \(g\), then writes \(R^*\) as though it depended only on model parameters. Its extinction theorem subsequently selects \(g\) after using an inequality containing \(k\), which creates the circular dependence repaired here.

An earlier stochastic SEIRS paper by Witbooi develops a related Lyapunov extinction threshold, but its stochastic threshold is expressed in terms of fixed model/noise quantities rather than an auxiliary weight selected later in the proof. It therefore does not supply the source-specific repair above.

Targeted searches using the cholera article title, DOI, stochastic-threshold notation, Lyapunov-weight terminology, and correction terminology did not locate a published correction or another result stating this exact feasibility condition.

## Limitations

The boxed inequality is an exact criterion for the coefficientwise \(\log(I+gB)\) certificate family, not a necessary condition for true extinction of the stochastic system.

The numerical replay uses the rounded parameter values printed in the article. It verifies consistency with the reported \(R^*=0.905\) but does not reconstruct unpublished simulation code.

An unindexed correction or author note could contain the same repair.

## References

1. P. J. Witbooi, G. E. Muller, M. B. Ongansie, I. H. I. Ahmed, K. O. Okosun, “A stochastic population model of cholera disease,” Discrete and Continuous Dynamical Systems - S 15 (2022), 441–456. DOI: 10.3934/dcdss.2021116.
2. P. J. Witbooi, “An SEIRS epidemic model with stochastic transmission,” Advances in Difference Equations 2017, Article 109. DOI: 10.1186/s13662-017-1166-6.
