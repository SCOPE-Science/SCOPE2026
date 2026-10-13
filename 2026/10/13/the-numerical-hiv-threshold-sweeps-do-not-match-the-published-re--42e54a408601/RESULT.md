# The numerical HIV threshold sweeps do not match the published reproduction number

## Finding

Example 6.2 gives
\[
\mathcal R_0=
\left[
\frac{\alpha\xi}{\alpha+\delta_L}e^{-m_1\tau_1}
+
(1-\xi)e^{-m_2\tau_2}
\right]
\left(
\frac{N\beta_1\Lambda}{cd}
+
\frac{\beta_2\Lambda}{\delta_I d}
\right).
\]

Using the parameters printed immediately below that formula in Table 1 gives
\[
\frac{N\beta_1\Lambda}{cd}
+
\frac{\beta_2\Lambda}{\delta_I d}
=
\frac{508}{23}.
\]

For Figure 1, where
\[
\tau_1=\tau_2=\tau,\qquad
m_1=m_2=1,\qquad
\xi=0.001,
\]
the formula reduces exactly to
\[
\mathcal R_0(\tau)
=
\frac{444373}{20125}e^{-\tau}.
\]
Consequently
\[
\mathcal R_0(0.5)\approx13.39258876,
\qquad
\mathcal R_0(1.75)\approx3.83704092.
\]
The published caption instead labels those cases \(8.1268\) and \(0.6690\). The equal-delay threshold occurs only at
\[
\tau_c
=
\log\!\left(\frac{444373}{20125}\right)
\approx3.09470148.
\]
Thus the displayed delay increase to \(1.75\) days does not cross the threshold under the published formula and parameters.

For Figure 2 the source fixes
\[
\tau_1=\tau_2=1.75
\]
and varies the latency fraction. The same formula becomes
\[
\mathcal R_0(\xi)
=
\frac{508}{23}
\left(1-\frac{2\xi}{7}\right)e^{-7/4}.
\]
It gives
\[
\mathcal R_0(0.05)\approx3.783306997,
\qquad
\mathcal R_0(0.025)\approx3.810722266.
\]
The caption instead reports \(1.4686\) and \(0.7188\). The sign of the reported effect is also reversed:
\[
\frac{d\mathcal R_0}{d\xi}<0,
\]
so decreasing \(\xi\) raises \(\mathcal R_0\).

Indeed, throughout the full admissible range
\[
0\le\xi\le1,
\]
the Figure 2 delay setting satisfies
\[
\mathcal R_0(\xi)
\ge
\frac{2540}{161}e^{-7/4}
\approx2.74152681>1.
\]

Therefore neither numerical sweep crosses \(\mathcal R_0=1\) under the model data printed alongside the figures.

## Assumptions and scope

The calculation uses only the reproduction-number formula displayed for system (6.2), the parameter values in Table 1, and the parameter changes stated in the Figure 1 and Figure 2 captions.

For Figure 1 all Table 1 parameters are used, including
\[
\xi=0.001.
\]
For Figure 2 the caption explicitly replaces \(\xi\) by \(0.05\) and \(0.025\), while the text fixes
\[
\tau_1=\tau_2=1.75.
\]

The finding does not infer which numerical values were supplied to unavailable simulation code. It establishes an inconsistency among the published formula, parameter table, captions, and threshold interpretation.

## Proof

From Table 1,
\[
\Lambda=10000,\qquad
d=\frac1{100},\qquad
\beta_1=\frac{24}{10^9},\qquad
\beta_2=\frac1{10^6},
\]
\[
\alpha=\frac1{100},\qquad
\delta_I=\frac1{20},\qquad
\delta_L=\frac1{250},\qquad
N=2000,\qquad
c=23.
\]
Thus
\[
\frac{N\beta_1\Lambda}{cd}
+
\frac{\beta_2\Lambda}{\delta_I d}
=
\frac{508}{23}.
\]
Also
\[
\frac{\alpha}{\alpha+\delta_L}
=
\frac57.
\]

When
\[
m_1=m_2=1
\]
and
\[
\tau_1=\tau_2=\tau,
\]
the delay-latency factor is
\[
\left(\frac57\xi+1-\xi\right)e^{-\tau}
=
\left(1-\frac{2\xi}{7}\right)e^{-\tau}.
\]

For Figure 1,
\[
\xi=\frac1{1000},
\]
so
\[
1-\frac{2\xi}{7}
=
\frac{3499}{3500},
\]
and hence
\[
\mathcal R_0(\tau)
=
\frac{508}{23}\frac{3499}{3500}e^{-\tau}
=
\frac{444373}{20125}e^{-\tau}.
\]
Substitution at
\[
\tau=\frac12
\]
and
\[
\tau=\frac74
\]
gives the two corrected values in the finding. Since this is a strictly decreasing exponential, the unique crossing is
\[
\tau_c
=
\log\!\left(\frac{444373}{20125}\right).
\]

For Figure 2,
\[
\tau=\frac74.
\]
At
\[
\xi=\frac1{20},
\]
the latency factor is
\[
\frac{69}{70},
\]
while at
\[
\xi=\frac1{40},
\]
it is
\[
\frac{139}{140}.
\]
This gives the exact values
\[
\frac{762}{35}e^{-7/4}
\]
and
\[
\frac{17653}{805}e^{-7/4}.
\]

Differentiating with respect to \(\xi\) gives
\[
\frac{d\mathcal R_0}{d\xi}
=
-\frac{1016}{161}e^{-7/4}<0.
\]
Finally, because
\[
1-\frac{2\xi}{7}\ge\frac57
\]
for
\[
0\le\xi\le1,
\]
\[
\mathcal R_0(\xi)
\ge
\frac{508}{23}\frac57e^{-7/4}
=
\frac{2540}{161}e^{-7/4}
>1.
\]

## Verification

The bundled `verify.py` evaluates all rational prefactors exactly and checks the exponential inequalities at high precision.

It verifies the four corrected reproduction numbers, the sign of the latency-fraction derivative, the exact critical delay, and the uniform lower bound for the Figure 2 sweep.

It also checks that the ratio of the two Figure 1 reproduction numbers must be
\[
e^{5/4},
\]
whereas the ratio of the two published caption labels is not equal to that value.

No numerical integration of the delay system is used to establish the finding.

## Relationship to prior work

The motivating article derives a threshold formula for a general delayed HIV model and then specializes it in Example 6.2. The numerical section states that the figures illustrate the effect of delay and latency fraction on the threshold.

The 2017 latent-HIV predecessor by Wang, Tang, Song, and Rong uses a closely related two-route delayed model. Its reproduction number also contains exponential survival factors for the intracellular delays, and its numerical section varies delays while keeping the formula and parameter set explicit. That paper supplies model-family context but does not contain or imply the numerical labels in the motivating source.

Exact-title, DOI, figure-label, reproduction-number, correction, erratum, and threshold-inconsistency searches did not locate a published correction of the two numerical captions.

## Limitations

The finding does not reconstruct the simulation program.

The plotted trajectories could have been generated from undocumented parameter choices. The claim is therefore restricted to reproducibility from the formula, Table 1, and captions as published.

The calculation does not challenge the analytic threshold theorems themselves.

## References

1. X. Jiang, “Threshold dynamics of a general delayed HIV model with double transmission modes and latent viral infection,” AIMS Mathematics 7 (2022), 2456–2478. DOI: 10.3934/math.2022138.
2. X. Wang, S. Tang, X. Song, L. Rong, “Mathematical analysis of an HIV latent infection model including both virus-to-cell infection and cell-to-cell transmission,” Journal of Biological Dynamics 11 (2017), 455–483. DOI: 10.1080/17513758.2016.1242784.
