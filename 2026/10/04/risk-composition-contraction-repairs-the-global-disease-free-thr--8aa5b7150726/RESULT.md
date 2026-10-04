# Risk-composition contraction repairs the global disease-free threshold in a two-susceptibility SLEIRS model

## Finding

Consider the normalized SLEIRS model
\[
\begin{aligned}
\dot S&=\mu\rho+\sigma\rho R-\alpha S(E+I)-\mu S,\\
\dot L&=\mu(1-\rho)+\sigma(1-\rho)R-\beta L(E+I)-\mu L,\\
\dot E&=(\alpha S+\beta L)(E+I)-(\delta+\mu)E,\\
\dot I&=\delta E-(\gamma+\mu)I,\\
\dot R&=\gamma I-(\sigma+\mu)R,
\end{aligned}
\]
on
\[
\Omega=
\left\{(S,L,E,I,R)\ge0:S+L+E+I+R=1\right\}.
\]
Assume
\[
0<\rho<1,\qquad \alpha>\beta>0,
\]
with all other rates positive. Write
\[
a_0=\alpha\rho+\beta(1-\rho)
\]
and
\[
\mathcal R_0
=
a_0\frac{\gamma+\mu+\delta}
{(\delta+\mu)(\gamma+\mu)}.
\]

The published proof of global disease-free stability uses the pointwise matrix comparison obtained by replacing
\[
\alpha S(t)+\beta L(t)
\]
with
\[
a_0.
\]
That comparison is not valid on all of \(\Omega\).

For the paper's own parameter set
\[
\alpha=0.2,\quad
\beta=0.1,\quad
\rho=0.3,\quad
\delta=0.15,\quad
\gamma=0.8,\quad
\mu=0.005,
\]
one has
\[
a_0=0.13
\]
and
\[
\mathcal R_0\approx0.9949909838<1.
\]
At the admissible state
\[
(S,L,E,I,R)=(0.9,0,0.1,0,0),
\]
the effective susceptibility is
\[
\alpha S+\beta L=0.18>a_0.
\]
Consequently the actual first component of the infected subsystem is
\[
\dot E=(0.18-0.15-0.005)(0.1)=0.0025,
\]
while the comparison used in the paper gives
\[
(0.13-0.15-0.005)(0.1)=-0.0025.
\]
Thus the printed pointwise inequality reverses sign at this valid state.

The global threshold theorem can nevertheless be repaired without strengthening the condition \(\mathcal R_0<1\). Define
\[
q(t)=\frac{S(t)}{\rho}-\frac{L(t)}{1-\rho}.
\]
Then
\[
\dot q
=
-(\mu+\beta(E+I))q
-(\alpha-\beta)(E+I)\frac{S}{\rho}.
\]
It follows that
\[
q_+(t)\le q_+(0)e^{-\mu t}.
\]
The effective susceptibility has the exact decomposition
\[
\alpha S+\beta L
=
a_0(S+L)
+
(\alpha-\beta)\rho(1-\rho)q.
\]
Since \(S+L\le1\),
\[
\alpha S(t)+\beta L(t)
\le
a_0+
(\alpha-\beta)\rho(1-\rho)q_+(0)e^{-\mu t}.
\]
Hence any initial excess of the high-risk susceptible share above its disease-free composition vanishes at least at the demographic rate \(\mu\).

If \(\mathcal R_0<1\), this shrinking excess is enough to recover the exact published threshold: after a finite transient, the infected subsystem is dominated by a constant Hurwitz Metzler matrix with effective susceptibility still below threshold. Therefore \(E\) and \(I\) decay exponentially, followed by
\[
R(t)\to0,\qquad
S(t)\to\rho,\qquad
L(t)\to1-\rho.
\]
The disease-free equilibrium
\[
(\rho,1-\rho,0,0,0)
\]
is therefore globally asymptotically stable for every initial condition in \(\Omega\) when \(\mathcal R_0<1\).

## Assumptions and scope

The result applies to the normalized five-compartment ODE printed in Pan and Tang (2024), with
\[
0<\rho<1,\qquad \alpha>\beta>0,\qquad \mu>0.
\]
The remaining transition rates are nonnegative, and the strict threshold statement uses the paper's positive-rate regime.

The finding has two parts: the source's displayed global comparison is false on its stated invariant simplex, and a different exact composition identity repairs the theorem at the same threshold.

No claim is made here about the critical case \(\mathcal R_0=1\), the endemic equilibrium for \(\mathcal R_0>1\), or the paper's parameter-estimation procedure.

## Proof

Set
\[
H=E+I.
\]
From the two susceptible equations,
\[
\frac{\dot S}{\rho}
=
\mu+\sigma R
-\alpha\frac{S}{\rho}H
-\mu\frac{S}{\rho},
\]
and
\[
\frac{\dot L}{1-\rho}
=
\mu+\sigma R
-\beta\frac{L}{1-\rho}H
-\mu\frac{L}{1-\rho}.
\]
Subtracting gives
\[
\dot q
=
-\mu q
-H\left(
\alpha\frac{S}{\rho}
-
\beta\frac{L}{1-\rho}
\right).
\]
Because
\[
\alpha\frac{S}{\rho}
-
\beta\frac{L}{1-\rho}
=
\beta q
+
(\alpha-\beta)\frac{S}{\rho},
\]
we obtain
\[
\dot q
=
-(\mu+\beta H)q
-(\alpha-\beta)H\frac{S}{\rho}.
\]
Whenever \(q>0\),
\[
\dot q\le-\mu q.
\]
The scalar comparison principle therefore yields
\[
q_+(t)\le q_+(0)e^{-\mu t}.
\]

Next,
\[
q=
\frac{S-\rho(S+L)}
{\rho(1-\rho)},
\]
so
\[
S
=
\rho(S+L)+\rho(1-\rho)q.
\]
Hence
\[
\begin{aligned}
\alpha S+\beta L
&=\beta(S+L)+(\alpha-\beta)S\\
&=a_0(S+L)
+(\alpha-\beta)\rho(1-\rho)q.
\end{aligned}
\]
Since \(S+L\le1\),
\[
a(t):=\alpha S(t)+\beta L(t)
\le
a_0+Cq_+(0)e^{-\mu t},
\]
where
\[
C=(\alpha-\beta)\rho(1-\rho)>0.
\]

The infected vector
\[
y=(E,I)^T
\]
satisfies
\[
\dot y=A(a(t))y,
\]
where
\[
A(a)=
\begin{pmatrix}
a-\delta-\mu&a\\
\delta&-\gamma-\mu
\end{pmatrix}.
\]
Define
\[
K=
\frac{\gamma+\mu+\delta}
{(\delta+\mu)(\gamma+\mu)}.
\]
Then
\[
\mathcal R_0=Ka_0<1.
\]
Choose
\[
\varepsilon
=
\frac12\left(\frac1K-a_0\right)>0.
\]
The decay of \(q_+\) gives a finite time \(T\) such that
\[
a(t)\le \bar a:=a_0+\varepsilon<\frac1K
\qquad(t\ge T).
\]
The matrix \(A(\bar a)\) is Metzler. Its determinant is
\[
\det A(\bar a)
=
(\delta+\mu)(\gamma+\mu)
-
\bar a(\gamma+\mu+\delta)>0,
\]
and its trace is negative because
\[
\bar a
<
\frac{(\delta+\mu)(\gamma+\mu)}
{\gamma+\mu+\delta}
<
\delta+\gamma+2\mu.
\]
Thus \(A(\bar a)\) is Hurwitz.

For \(t\ge T\),
\[
A(a(t))\le A(\bar a)
\]
entrywise. The cooperative linear comparison theorem therefore gives
\[
0\le y(t)
\le
e^{A(\bar a)(t-T)}y(T),
\]
so \(E(t)\) and \(I(t)\) decay exponentially.

Then
\[
\dot R=\gamma I-(\sigma+\mu)R
\]
implies \(R(t)\to0\). Finally,
\[
\dot S+\mu(S-\rho)
=
\sigma\rho R-\alpha SH
\]
and
\[
\dot L+\mu(L-(1-\rho))
=
\sigma(1-\rho)R-\beta LH.
\]
The right-hand sides tend to zero, so stable scalar variation-of-constants formulas yield
\[
S(t)\to\rho,\qquad L(t)\to1-\rho.
\]

For local stability, the disease-free Jacobian has three immediately stable directions with eigenvalues
\[
-\mu,\qquad -\mu,\qquad -(\sigma+\mu),
\]
and the infected block is \(A(a_0)\), which is Hurwitz exactly when \(\mathcal R_0<1\). Therefore the disease-free equilibrium is locally asymptotically stable. Combining local stability with the global attraction just proved gives global asymptotic stability.

## Verification

The bundled checker symbolically reconstructs the differential identity for \(q\), the exact decomposition of \(\alpha S+\beta L\), and the determinant threshold for the infected block.

It also evaluates the source-parameter counterexample exactly:
\[
a_0=\frac{13}{100},
\]
\[
\mathcal R_0
=
\frac{13}{100}
\left(
\frac1{31/200}
+
\frac{3/20}{(31/200)(161/200)}
\right)
\approx0.9949909838,
\]
while at
\[
(S,L,E,I,R)=\left(\frac9{10},0,\frac1{10},0,0\right)
\]
the actual and claimed-bound first infected derivatives are
\[
\frac1{400}=0.0025
\]
and
\[
-\frac1{400}=-0.0025,
\]
respectively.

The checker is not used to infer the infinite-time result; the global convergence proof is analytic.

## Relationship to prior work

Pan and Tang (2024), DOI 10.3934/math.20241032, introduce the exact SLEIRS model studied here. Their Theorem 1 states global asymptotic stability of the disease-free equilibrium for \(\mathcal R_0<1\). The local Jacobian calculation is compatible with that threshold, but the global step replaces the time-dependent effective susceptibility \(\alpha S+\beta L\) by the disease-free weighted value \(\alpha\rho+\beta(1-\rho)\) pointwise. The explicit state above shows that this comparison is not valid on the full invariant simplex.

Ibrahim et al. (2022), DOI 10.3390/vaccines11010003, study a different COVID-19 model with separate high-risk and low-risk susceptible populations and prove global stability using Lyapunov techniques. Their recruitment and intervention structure differs from the Pan–Tang model, and their results do not give the composition variable \(q\) or the exponential relaxation identity used here.

Katriel (2012), DOI 10.1007/s00285-011-0460-2, analyzes epidemic size under heterogeneous susceptibility in a substantially more general susceptibility-distribution setting. That work motivates the importance of susceptibility composition but does not imply this source-specific contraction identity or repair the displayed comparison in the 2024 SLEIRS proof.

## Limitations

The result does not analyze \(\mathcal R_0=1\). At the critical value the constant comparison matrix loses strict Hurwitz stability and the present exponential-domination argument no longer applies directly.

The proof uses the source assumption \(\alpha>\beta\), which makes infection preferentially deplete the more susceptible class. If the ordering is reversed, the sign in the composition equation changes and the argument must be reconsidered.

The finding repairs the disease-free global-stability theorem; it does not validate the source's endemic-equilibrium formula, empirical parameter estimates, or forecast accuracy.

## References

1. X. Pan, L. Tang, “A new model for COVID-19 in the post-pandemic era,” AIMS Mathematics 9 (2024), 21255–21272. DOI: 10.3934/math.20241032.
2. A. Ibrahim, U. W. Humphries, A. Khan, S. I. Bala, I. A. Baba, F. A. Rihan, “COVID-19 Model with High- and Low-Risk Susceptible Population Incorporating the Effect of Vaccines,” Vaccines 11 (2023), 3. DOI: 10.3390/vaccines11010003.
3. G. Katriel, “The size of epidemics in populations with heterogeneous susceptibility,” Journal of Mathematical Biology 65 (2012), 237–262. DOI: 10.1007/s00285-011-0460-2.
