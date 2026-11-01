# Two-tap synaptic memory forces a universal restabilization window

## Finding

Fix real parameters \(0<b<a\), and consider the linear retarded differential equation
\[
 u''(t)+a u(t)-\frac b2\bigl(u(t-\tau)+u(t-2\tau)\bigr)=0,\qquad \tau>0.
\]
Its equilibrium \(u=0\) is exponentially asymptotically stable for **exactly** the following two initial delay intervals, through its first three changes of stability:
\[
\begin{aligned}
&0<\tau<\frac{2\pi}{3\sqrt{a+b/2}} &&\text{stable},\\
&\frac{2\pi}{3\sqrt{a+b/2}}<\tau<\frac{\pi}{\sqrt a} &&\text{unstable},\\
&\frac{\pi}{\sqrt a}<\tau<\frac{4\pi}{3\sqrt{a+b/2}} &&\text{stable}.
\end{aligned}
\]
The **first three** purely imaginary spectral crossings occur at precisely the three displayed positive endpoints, in that order. All three are simple transverse conjugate-pair crossings: destabilizing, stabilizing, and destabilizing. Immediately after the third endpoint the zero solution is unstable. The assertions do not classify all larger delays.

For comparison, the **single-delay** equation
\[
 u''(t)+a u(t)-b u(t-h)=0
\]
never recovers exponential stability after its first destabilization when \(5a/13<b<a\). Thus replacing a single delay by two equally weighted delays in the ratio \(1:2\) forces reentrant stability even in a parameter regime where a single delay cannot restabilize. Comparison at the same mean delay uses \(h=3\tau/2\).

The conclusion applies to a concrete stationary state in the delayed theta-neuron macroscopic equation of Bîrdac–Fikl–Kaslik–Mureşan (2026): with synaptic coupling \(\kappa=1\), input \(\eta=-1/2\), and real equilibrium \(z^*=0\), its characteristic equation is the one above with \(a=4\), \(b=2\) for the two-tap probability kernel \((\delta_\tau+\delta_{2\tau})/2\). Hence this **macroscopic equilibrium**, on the specified reduced invariant family, has two separate local exponential-stability windows in the first three crossing intervals. This is a local statement, not a claim of global stabilization or of a nonlinear periodic orbit at the crossings.

## Assumptions and scope

The equation is interpreted on continuous initial histories \((u,u')\) over \([-2\tau,0]\) in the standard retarded functional-differential sense. Its characteristic function is
\[
 \Delta(s,\tau)=s^2+a-\frac b2(e^{-s\tau}+e^{-2s\tau}).
\]
Exponential stability means that all characteristic roots have strictly negative real parts; instability means that at least one characteristic root has positive real part. No assertion is made at the three critical endpoints, where characteristic roots lie on the imaginary axis. The two-tap kernel has mean \(3\tau/2\), so the parameter \(\tau\) here denotes the shorter tap delay, not the mean. Equivalently, with mean delay \(m\), the two taps occur at \(2m/3\) and \(4m/3\).

The normalized Fourier transform of the reference two-tap delay distribution vanishes at an infinite set of real frequencies. Consequently this law is admissible as a positive finite-support delay kernel but **not phase-regular** in the sense of Definition 2.4 of the 2026 motivating paper. Its existing phase-regular Hopf reduction cannot simply be substituted at the transform zeros.

## Proof

**1. Initial stability.** At \(\tau=0\), the characteristic roots are \(s_\pm(0)=\pm i\sqrt{a-b}\), both simple. The implicit-function derivative of a root at zero delay is
\[
 s'_\pm(0)=-\frac{3b}{4}<0.
\]
For any root with \(\Re s\ge0\), the characteristic equation and \(|e^{-s\tau}|\le1\) imply \(|s|^2\le a+b\), uniformly in \(\tau\ge0\). Thus no additional right-half-plane roots can enter from infinity as \(\tau\downarrow0\). Compactness and the two simple perturbed roots show that every characteristic root has negative real part for all sufficiently small positive delays.

**2. Exhaustive imaginary-axis spectrum.** Substitute \(s=i\omega\), \(\omega>0\), and write \(\vartheta=\omega\tau\). Separating the imaginary part gives
\[
 \sin\vartheta+\sin(2\vartheta)
 =\sin\vartheta(1+2\cos\vartheta)=0.
\]
There are exactly three frequency classes, all positive because \(a>b>0\):
\[
 \begin{array}{c|c|c}
\text{phase angles }\vartheta & \text{frequency }\omega & \text{critical delays }\tau=\vartheta/\omega\\ \hline
2k\pi,\;k\ge1 & \alpha=\sqrt{a-b} & 2k\pi/\alpha\\
(2k+1)\pi,\;k\ge0 & \beta=\sqrt a & (2k+1)\pi/\beta\\
2k\pi+2\pi/3\ \text{or}\ 2k\pi+4\pi/3,\;k\ge0 & \gamma=\sqrt{a+b/2} & \vartheta/\gamma
\end{array}
\]
Here the table follows from the respective real transform values \(1\), \(0\), and \(-1/2\). There are no positive imaginary roots outside these families. A zero characteristic root is impossible since \(\Delta(0,\tau)=a-b>0\).

**3. Simplicity and crossing direction.** Put \(S(\vartheta)=e^{-i\vartheta}+2e^{-2i\vartheta}\). Implicit differentiation at a crossing gives
\[
 \bigl(s'(\tau)\bigr)^{-1}
 =-\frac4{bS(\vartheta)}-\frac\tau{s}.
\]
The real part of the second summand vanishes at \(s=i\omega\), and the sign of the real part of a complex number equals the sign of the real part of its reciprocal. Thus
\[
 \operatorname{sgn}\Re s'(\tau)
 =-\operatorname{sgn}\bigl(\cos\vartheta+2\cos2\vartheta\bigr).
\]
At integer multiples of \(\pi\), the parenthesis is \(1\) or \(3\), so crossings are stabilizing; at the remaining angles it is \(-3/2\), so crossings are destabilizing. In each case \(\Re\Delta_s=(b\tau/2)\Re S\ne0\), proving simplicity and transversality.

**4. Ordering and stability.** Define
\[
 T_1=\frac{2\pi}{3\gamma},\qquad
 T_2=\frac\pi\beta,\qquad
 T_3=\frac{4\pi}{3\gamma}.
\]
Since \(\beta<\gamma<\sqrt{3/2}\,\beta\) and \(\alpha<\beta\), one has \(T_1<T_2<T_3\), while
\[
 T_3<\min\left\{\frac{2\pi}{\alpha},\frac{3\pi}{\beta},\frac{8\pi}{3\gamma}\right\}.
\]
The exhaustive crossing list therefore proves these are the first three positive critical delays. The number of right-half-plane roots stays constant between such delays, because its possible roots in that half-plane are uniformly bounded and the roots depend continuously on the parameters. Starting with no unstable roots, the three crossings contribute \(+2,-2,+2\) to that number, respectively. This proves the stated two stable intervals, the intervening unstable interval, and instability immediately beyond the third crossing.

**5. Single-delay contrast.** For a single atom at delay \(h\), the imaginary-axis critical times are the odd multiples \((2k+1)\pi/\sqrt{a+b}\), which destabilize, and the positive even multiples \(2k\pi/\sqrt{a-b}\), which stabilize. The zero-delay root moves left at small positive \(h\). If \(b>5a/13\), then
\[
 \frac{\sqrt{a+b}}{\sqrt{a-b}}>\frac32.
\]
For every \(k\ge1\), the \((k+1)\)-st destabilizing time occurs before the \(k\)-th stabilizing time; consequently no later delay can reduce the unstable-pair count back to zero after the first destabilization. Rescaling \(h=3\tau/2\) makes the one-atom and two-atom delay distributions have equal mean.

**6. Realization as a theta-neuron macroscopic equilibrium.** The 2026 motivating paper gives the real-axis equilibrium equation \(((1-z)/(1+z))^2-\kappa I(z)=\eta\), with \(I(0)=3/2\). At \((\kappa,\eta,z^*)=(1,-1/2,0)\) the equation holds. Its characteristic coefficients at a real equilibrium are \(a_2=4((1-z^*)/(1+z^*))^2\), \(b_2=\kappa(1-z^{*2})(2-z^*)\), hence \(a_2=4\) and \(b_2=2\). The admissible two-atom kernel has transform \((e^{-s\tau}+e^{-2s\tau})/2\), giving exactly \(\Delta(s,\tau)\). For this example the first three critical shorter-tap delays are
\[
 0.9366419641387634\ldots,\quad1.5707963267948966\ldots,\quad1.8732839282775269\ldots.
\]
Standard retarded-equation linearization theory transfers strict characteristic-root stability or instability to the local macroscopic equilibrium on its stated reduced state space.

## Verification

The standalone file `check_stability.py` uses only the Python standard library. It evaluates characteristic residuals and implicit root-crossing derivatives at the analytically listed crossings for five parameter pairs, checks the strict ordering against all competing next candidate types, verifies 80 additional imaginary-root candidates, and tests the theta-neuron parameter example. Run `python check_stability.py` beside this file. The finite checks are corroborative; none replaces the exhaustive trigonometric factorization, root-count argument, or proof of the analytic inequalities above.

## Relationship to prior work

Bîrdac, Fikl, Kaslik and Mureşan (2026), Sections 2–5 and Appendix A, derive the real-axis characteristic equation and discuss phase-regular kernels and the single-Dirac case. In particular their Remark 5.13 contains the \(13b=5a\) single-delay restabilization boundary. Their phase-regular hypothesis requires a nonvanishing frequency transform, whereas the equal two-tap kernel has zeros; the two-tap, three-crossing theorem and universal reentrance are not established in the inspected source. The single-Dirac result is used only for the comparison, not claimed as new.

Cahlon and Schmidt (2024) study the broader class of second-order equations with two commensurate delays and may contain closely relevant specialized criteria. Only the accessible abstract and first page could be inspected, not its full article, so overlap within that paper remains a genuine priority risk. General two-delay stability-region frameworks, including Gu–Niculescu–Chen (2005), cover broad methodology; the narrow claim here is the explicit universal two-window interval and its theta-neuron interpretation, not a new general DDE root-location method.

## Limitations

The conclusion gives local linear and nonlinear hyperbolic stability statements for a specified equilibrium, not global attraction, nonlinear Hopf criticality, periodic-orbit existence, or robustness to unequal delay weights. It does not classify all subsequent stability intervals at large delay. The two-atom kernel is not phase-regular as defined in the motivating paper. A plausible 2024 same-class paper could not be reviewed in full; independent mathematical priority review remains necessary.

## References

1. L. Bîrdac, A. Fikl, E. Kaslik and R. Mureşan, *Macroscopic Multistability and Bifurcations in Theta-Neuron Networks with Distributed Delays*, arXiv:2607.17645v1 (first public July 20, 2026), https://arxiv.org/abs/2607.17645 . Sections 2–5, 8 and Appendix A.
2. B. Cahlon and D. Schmidt, *On Asymptotic Stability of Second Order Differential Equations with Two Commensurate Delays*, Dynamics of Continuous, Discrete and Impulsive Systems A 31 (2024), 213–239; accessible abstract and first page: https://online.watsci.org/abstract_pdf/2024v31/v31n4a-pdf/1.pdf . Complete text not inspected.
3. K. Gu, S.-I. Niculescu and J. Chen, *On stability crossing curves for general systems with two delays*, J. Math. Anal. Appl. 311 (2005), 231–253, https://doi.org/10.1016/j.jmaa.2005.02.034 .
4. Y. Hata and H. Matsunaga, *Stability switches in a linear differential equation with two delays*, Opuscula Math. 42 (2022), 673–690, https://doi.org/10.7494/OpMath.2022.42.5.673 . Its equation is first-order in time.
