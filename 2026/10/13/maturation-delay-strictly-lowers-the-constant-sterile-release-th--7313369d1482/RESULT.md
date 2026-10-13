# Maturation delay strictly lowers the constant sterile-release threshold

## Finding

For the constant-release model
\[
\dot w(t)=
\frac{a\,w(t-\tau)^2}{w(t-\tau)+g(t-\tau)}
-
\bigl(\mu_1+\xi_1(w(t)+g(t))\bigr)w(t),
\]
\[
\dot g(t)=
b-\bigl(\mu_2+\xi_2(w(t)+g(t))\bigr)g(t),
\qquad
a=a_0e^{-\mu_0\tau},
\]
the critical constant release rate is strictly decreasing with maturation delay.

If
\[
N=w+g
\]
at a positive equilibrium, then
\[
b=
B_a(N)
=
\frac{N(\mu_2+\xi_2N)(a-\mu_1-\xi_1N)}{a},
\]
so for \(a>\mu_1\),
\[
b_0(\tau)
=
\max_{0<N<(a-\mu_1)/\xi_1}B_a(N).
\]

When \(a_0>\mu_1\), define
\[
\tau_c
=
\frac1{\mu_0}\log\frac{a_0}{\mu_1}.
\]
Then \(b_0(\tau)\) is strictly decreasing on
\[
0\le\tau<\tau_c,
\]
and no positive wild-mosquito equilibrium exists for any \(b\ge0\) once
\[
\tau\ge\tau_c.
\]
Near this endpoint,
\[
b_0(\tau)
=
\frac{\mu_1\mu_2\mu_0^2}{4\xi_1}
(\tau_c-\tau)^2
+
O\!\left((\tau_c-\tau)^3\right).
\]

For the source's Figure 1 parameters,
\[
a_0=10,\quad
\mu_0=0.1,\quad
\mu_1=0.5,\quad
\mu_2=0.4,\quad
\xi_1=0.5,\quad
\xi_2=0.4,
\]
the correct threshold at \(\tau=0.2\) is
\[
b_0(0.2)\approx21.0432928772.
\]
The caption instead gives \(21.93\), which is the zero-delay value
\[
b_0(0)\approx21.9375160204.
\]

With the caption's release \(b=21\), the unique threshold-crossing delay is
\[
\tau_b\approx0.209892963.
\]
Hence positive equilibria no longer exist for \(\tau>\tau_b\). In particular,
\[
b_0(1.5)\approx16.04165880,
\qquad
b_0(4.9)\approx7.81905967,
\]
both below \(21\). The positive-equilibrium curves displayed in Figure 2 at those delays therefore cannot be equilibria of system (6) if the other Figure 1 parameters are held fixed as stated in its caption.

## Assumptions and scope

All demographic, density-dependence, and release parameters are positive. The model's maturation-survival parameter is
\[
a=a_0e^{-\mu_0\tau}
\]
exactly as printed.

The monotonicity result concerns equilibrium existence under the constant-release strategy. It does not modify the source's local stability classification for equilibria that actually exist.

The numerical correction concerns Figures 1–2 and their captions. It does not reconstruct unavailable simulation code.

## Proof

At a positive equilibrium, delay disappears from the state arguments but remains in
\[
a=a_0e^{-\mu_0\tau}.
\]
The source derives the cubic
\[
P(N)
=
\xi_1\xi_2N^3
-
\bigl((a-\mu_1)\xi_2-\xi_1\mu_2\bigr)N^2
-
(a-\mu_1)\mu_2N
+
ab.
\]
Setting \(P(N)=0\) and solving for \(b\) gives
\[
b
=
\frac{
N(\mu_2+\xi_2N)(a-\mu_1-\xi_1N)
}{a}.
\]
A positive release and positive equilibrium therefore require
\[
a>\mu_1
\]
and
\[
0<N<\frac{a-\mu_1}{\xi_1}.
\]
The saddle-node threshold is exactly the maximum of this release function over that interval.

For fixed admissible \(N\),
\[
B_a(N)
=
N(\mu_2+\xi_2N)
\left(
1-\frac{\mu_1+\xi_1N}{a}
\right).
\]
Hence
\[
\frac{\partial B_a(N)}{\partial a}
=
\frac{
N(\mu_2+\xi_2N)(\mu_1+\xi_1N)
}{a^2}
>0.
\]
If \(a_2>a_1>\mu_1\), the admissible interval for \(a_1\) is contained strictly in that for \(a_2\), and evaluating \(B_{a_2}\) at an optimizer for \(a_1\) gives
\[
b_0(a_2)>b_0(a_1).
\]
Since \(a_0e^{-\mu_0\tau}\) decreases strictly in \(\tau\), \(b_0(\tau)\) decreases strictly until \(a=\mu_1\).

The equality \(a=\mu_1\) occurs at
\[
\tau_c
=
\frac1{\mu_0}\log\frac{a_0}{\mu_1}.
\]
When \(a\le\mu_1\), the factor
\[
a-\mu_1-\xi_1N
\]
is negative for every \(N>0\), so no positive equilibrium can satisfy \(b\ge0\).

For the endpoint asymptotic write
\[
\delta=a-\mu_1
\]
and set
\[
N=\frac{\delta}{\xi_1}y,
\qquad
0<y<1.
\]
Then
\[
B_a(N)
=
\frac{\delta^2}{a\xi_1}
y(1-y)
\left(
\mu_2+\frac{\xi_2\delta}{\xi_1}y
\right).
\]
The maximizing \(y\) tends to \(1/2\), so
\[
b_0
=
\frac{\mu_2}{4a\xi_1}\delta^2
+
O(\delta^3)
=
\frac{\mu_2}{4\mu_1\xi_1}\delta^2
+
O(\delta^3).
\]
If
\[
h=\tau_c-\tau,
\]
then
\[
a
=
\mu_1e^{\mu_0h}
\]
and
\[
\delta
=
\mu_1\mu_0h+O(h^2).
\]
Substitution yields
\[
b_0(\tau)
=
\frac{\mu_1\mu_2\mu_0^2}{4\xi_1}h^2
+
O(h^3).
\]

For the Figure 1 parameters, direct maximization of the exact \(B_a(N)\) gives
\[
b_0(0.2)\approx21.0432928772.
\]
The positive equilibrium roots at \(\tau=0.2\) are approximately
\[
N_1\approx11.90646320,
\qquad
N_2\approx12.57277568,
\]
which give
\[
(w_1,g_1)\approx(7.83873379,4.06772941),
\]
\[
(w_2,g_2)\approx(8.70473857,3.86803711).
\]
These match the caption's rounded equilibrium coordinates and therefore confirm that the delayed value of \(a\) was used there even though the threshold label was not updated.

Strict monotonicity gives a unique solution of
\[
b_0(\tau)=21,
\]
namely
\[
\tau_b\approx0.209892963.
\]
The stated values at \(1.5\) and \(4.9\) then exclude positive equilibria at the fixed release \(b=21\).

## Verification

The bundled `verify.py` reconstructs the factorization of the source's equilibrium cubic, proves the positive derivative of \(B_a(N)\) with respect to \(a\), and checks the endpoint scaling symbolically.

It also evaluates the Figure 1 parameter set at high precision, reproduces the two printed equilibrium coordinates from the delayed value
\[
a=10e^{-0.02},
\]
and computes the corrected release thresholds.

The numerical root for \(\tau_b\) is only a replay of the unique crossing guaranteed analytically by strict monotonicity.

## Relationship to prior work

The motivating article extends earlier sterile-mosquito release models by including maturation delay. For constant release it derives the threshold \(b_0(\tau)\), classifies equilibrium existence, and proves that the stability types of the equilibria do not switch as delay varies.

The earlier nondelayed model of Cai, Ai, and Li supplies the corresponding constant-release saddle-node structure at fixed reproductive parameter. It has no maturation-survival factor
\[
a_0e^{-\mu_0\tau}
\]
and therefore does not imply the delay monotonicity or critical-delay law above.

Later delayed sterile-mosquito models also establish release thresholds under different biological assumptions. Those results do not imply the exact variational identity, strict delay monotonicity, quadratic endpoint law, or Figure 1–2 numerical correction for the present model.

Searches by DOI, title, threshold notation, maturation-survival factor, critical-delay terminology, and Figure 1 threshold value did not locate an equivalent correction or sharpening.

## Limitations

The result concerns equilibrium existence under constant continuous release.

It does not analyze the proportional-release model, periodic release, residual fertility, or sex-structured extensions.

The critical-delay conclusion is a mathematical consequence of the model's exponential immature-survival factor and should not be interpreted as a standalone field recommendation.

## References

1. L. Cai, S. Ai, G. Fan, “Dynamics of delayed mosquitoes populations models with two different strategies of releasing sterile mosquitoes,” Mathematical Biosciences and Engineering 15 (2018), 1181–1202. DOI: 10.3934/mbe.2018054.
2. L. Cai, S. Ai, J. Li, “Dynamics of Mosquitoes Populations with Different Strategies for Releasing Sterile Mosquitoes,” SIAM Journal on Applied Mathematics 74 (2014), 1786–1809. DOI: 10.1137/13094102X.
3. J. Yu, J. Li, “Dynamics of interactive wild and sterile mosquitoes with time delay,” Journal of Biological Dynamics 13 (2019), 606–620. DOI: 10.1080/17513758.2019.1682201.
