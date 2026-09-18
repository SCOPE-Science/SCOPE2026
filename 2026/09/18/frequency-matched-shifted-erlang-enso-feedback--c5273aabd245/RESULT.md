# Frequency-matched normalization for shifted-Erlang ENSO feedback

## Result

Consider the shifted-Erlang distributed-delay Ghil–Zaliapin–Thompson (GZT) equation studied by Steele, Keane and Krauskopf,
\[
\dot h(t)=-A\tanh\!\left(\kappa\int_0^\infty g^n(s)h(t-s)\,ds\right)+c\cos(\omega_f t),
\]
where \(g^n\) is the order-\(n\) shifted Erlang density with scale \(\Delta>0\) and minimum delay \(\tau_m\). Its frequency response is
\[
G(i\omega)=e^{-i\omega\tau_m}(1+i\omega\Delta)^{-n}.
\]
Write
\[
q(\omega)=|G(i\omega)|=(1+(\omega\Delta)^2)^{-n/2}.
\]

The source introduces
\[
\alpha(n,\Delta)=q(\omega_f)^{-1}
\]
at the annual forcing frequency \(\omega_f=2\pi\), then replaces the feedback coefficient \(a\) by
\[
\widetilde a=\frac{a}{\alpha}=a\,q(\omega_f)
\]
to account for the attenuation caused by the distributed delay.

At the linear-filter level used to motivate this normalization, this scaling has the opposite direction from amplitude compensation. Linearizing \(-A\tanh(\kappa x)\) at \(x=0\), a sinusoidal component at frequency \(\omega\) is multiplied in magnitude by
\[
A\kappa q(\omega).
\]
Hence the source scaling gives, at \(\omega=\omega_f\),
\[
\widetilde a\,\kappa q(\omega_f)
=a\kappa q(\omega_f)^2,
\]
so the attenuation is applied twice rather than cancelled. The unique scalar amplitude normalization that matches the constant-delay small-signal feedback magnitude \(a\kappa\) at a chosen frequency \(\omega\) is instead
\[
\boxed{A_{\rm amp}(\omega)=\frac{a}{q(\omega)}
=a(1+(\omega\Delta)^2)^{n/2}.}
\]

There is also an unavoidable phase mismatch if comparison is made at fixed mean delay. The phase of \(G(i\omega)\) is
\[
-\omega\tau_m-n\arctan(\omega\Delta),
\]
so its frequency-equivalent phase delay is
\[
\boxed{\tau_{\rm ph}(\omega)
=\tau_m+\frac{n}{\omega}\arctan(\omega\Delta).}
\]
The mean delay used in the source is
\[
\tau_{\rm eff}=\tau_m+n\Delta.
\]
For every \(\omega,\Delta>0\),
\[
\boxed{\tau_{\rm eff}-\tau_{\rm ph}(\omega)
=n\left(\Delta-\frac{\arctan(\omega\Delta)}{\omega}\right)>0.}
\]
Thus mean-delay matching and phase-delay matching cannot both hold for a nonzero-width Erlang kernel.

Consequently, the exact complex frequency match to a constant-delay feedback factor
\[
a e^{-i\omega\tau_0}
\]
at one chosen frequency \(\omega>0\) is
\[
\boxed{
A=\frac{a}{q(\omega)},\qquad
\tau_m=\tau_0-\frac{n}{\omega}\arctan(\omega\Delta),
}
\]
provided the resulting minimum delay is nonnegative. Equivalently,
\[
\tau_{\rm eff}
=\tau_0+n\left(\Delta-\frac{\arctan(\omega\Delta)}{\omega}\right).
\]
This is a frequency-matched normalization; it is distinct from matching the mean of the delay distribution.

## Numerical size for the parameters used in the source

The paper fixes \(n=3\) and compares \(\Delta=1/15\) and \(\Delta=2/15\), with annual forcing \(\omega_f=2\pi\). At this frequency:

- For \(\Delta=1/15\),
  \[
  q=0.784672478417,\qquad q^{-1}=1.274417068912.
  \]
  The source coefficient \(\widetilde a=a q\) therefore leaves a post-filter linear gain equal to \(0.615710898385\,a\kappa\). The mean delay exceeds the phase-equivalent delay by \(0.010601772283\) yr, about \(3.87\) days.

- For \(\Delta=2/15\),
  \[
  q=0.450424982227,\qquad q^{-1}=2.220125524690.
  \]
  The source coefficient leaves a post-filter linear gain equal to \(0.202882664614\,a\kappa\). The mean delay exceeds the phase-equivalent delay by \(0.067042812370\) yr, about \(24.49\) days.

The discrepancy is therefore not negligible at the wider kernel used in the comparison.

## Exact autonomous Hopf anchor

The same transfer function gives an exact check on the unforced boundary \(c=0\). The equilibrium \(h=0\) has characteristic equation
\[
\lambda+a\kappa e^{-\lambda\tau_m}(1+\lambda\Delta)^{-n}=0.
\]
For a purely imaginary root \(\lambda=i\Omega\), \(\Omega>0\), the amplitude and phase conditions are
\[
\boxed{
\Omega(1+(\Omega\Delta)^2)^{n/2}=a\kappa,
}
\]
and
\[
\boxed{
\Omega\tau_m+n\arctan(\Omega\Delta)
=\frac{\pi}{2}+2\pi m,\qquad m\in\mathbb Z_{\ge0}.
}
\]
The amplitude equation has exactly one positive solution \(\Omega=\Omega_H(\Delta)\), since its left-hand side is strictly increasing. The corresponding neutral curves are
\[
\tau_{m,m}
=
\frac{\frac{\pi}{2}+2\pi m-n\arctan(\Omega_H\Delta)}
{\Omega_H},
\]
whenever this is nonnegative, or in mean-delay coordinates
\[
\boxed{
\tau_{{\rm eff},m}
=
\frac{\frac{\pi}{2}+2\pi m+n(\Omega_H\Delta-\arctan(\Omega_H\Delta))}
{\Omega_H}.
}
\]

For the source values \(a=1\), \(\kappa=11\), \(n=3\), the first calculations are:

\[
\begin{array}{c|c|c|c}
\Delta & \Omega_H & \tau_{m,0} & \tau_{{\rm eff},0}\\ \hline
0 & 11 & 0.142799666072 & 0.142799666072\\
1/15 & 7.727648837642 & 0.018589253688 & 0.218589253688
\end{array}
\]

At \(\Delta=2/15\), the formal \(m=0\) value has \(\tau_m=-0.064062652510\) and is physically inadmissible; the first admissible branch is \(m=1\), with
\[
\tau_m=1.052280519454,\qquad
\tau_{\rm eff}=1.452280519454.
\]
For \(n=3\), \(a\kappa=11\), the \(m=0\) branch loses physical admissibility exactly when
\[
\Delta>\frac{8}{99}\approx0.08080808.
\]
This follows from the boundary condition \(3\arctan(\Omega\Delta)=\pi/2\), which gives \(\Omega\Delta=1/\sqrt3\).

These formulas do not by themselves determine the periodically forced resonance tongues, but they provide an exact spectral anchor showing that delay width changes both gain and phase. A normalization at the annual forcing frequency cannot simultaneously preserve the mean delay, the complex frequency response, and the autonomous Hopf spectrum.

## Interpretation

The bifurcation computations in the source remain computations for the parameter family that was actually continued. The correction concerns their interpretation as a like-for-like compensation for delay-distribution attenuation. With the printed definition \(\widetilde a=a/\alpha\), increasing width weakens the linear feedback once through the kernel and a second time through the coefficient.

A frequency-matched comparison should instead use \(A=a/q(\omega)\) if the intended invariant is the small-signal magnitude at frequency \(\omega\), and should use \(\tau_{\rm ph}(\omega)\), rather than the mean alone, if phase is also to be matched. If the modelling objective is specifically to hold the physical mean delay fixed, then the residual phase shift is real and should be treated as part of the effect of broadening the distribution rather than removed by normalization.

## Relation to prior work

General stability-crossing theory for shifted gamma-distributed delays predates the source paper. In particular, Morărescu, Niculescu and Gu (SIAM J. Applied Dynamical Systems, 2007) characterize stability crossing curves for linear systems with gamma-distributed delay and a gap. The transfer-function algebra and the existence of gain and phase effects are therefore not claimed as new general theory.

The new claim here is deliberately source-specific: for the normalization printed in arXiv:2609.08127v1, the stated attenuation compensation is reciprocal to the small-signal amplitude compensation implied by the paper's own Fourier response, and the same response yields an exact frequency-matched normalization and exact autonomous GZT Hopf anchors that quantify the mismatch.

## Limitations

The exact gain/phase statements apply to the linear response of the convolution operator, and the Hopf formulas apply to the linearization of the unforced \(c=0\) equilibrium. They do not assert that the full nonlinear, seasonally forced bifurcation diagram is obtained from a constant-delay diagram by any scalar rescaling. Indeed, the \(\tanh\) nonlinearity generates harmonics, so no one-frequency normalization can make the two nonlinear systems globally equivalent.

This record does not claim that the numerical continuation curves in the source were computed incorrectly. It shows that the printed normalization does not perform the amplitude compensation its Fourier-filter rationale suggests, and that matching the mean delay is not the same as matching the phase at the forcing frequency.

## Reproducibility

`artifacts/verify_frequency_match.py` evaluates the source parameters using only the Python standard library and checks the characteristic-equation residuals for the quoted Hopf points.

## References

1. J. Steele, A. Keane, B. Krauskopf, *A distributed-delay model for the El Niño Southern Oscillation with a minimum delay: a case study of the shifted linear chain trick*, arXiv:2609.08127v1 (2026). https://arxiv.org/abs/2609.08127
2. C.-I. Morărescu, S.-I. Niculescu, K. Gu, *Stability Crossing Curves of Shifted Gamma-Distributed Delay Systems*, SIAM Journal on Applied Dynamical Systems 6 (2007). https://doi.org/10.1137/060670766
3. M. Ghil, I. Zaliapin, S. Thompson, *A delay differential model of ENSO variability: parametric instability and the distribution of extremes*, Nonlinear Processes in Geophysics 15 (2008), 417–433. https://doi.org/10.5194/npg-15-417-2008
