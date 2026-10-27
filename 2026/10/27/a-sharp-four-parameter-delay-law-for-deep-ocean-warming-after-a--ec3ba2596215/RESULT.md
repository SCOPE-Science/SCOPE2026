# A sharp four-parameter delay law for deep-ocean warming after a finite forcing pulse

## Finding
For a positive, finite-duration direct radiative forcing in the classical two-layer linear energy-balance model, the surface temperature peaks exactly at forcing shutdown, whereas the deep-layer temperature peaks strictly later, at the unique explicit time
\[
t_* = \frac{1}{b-a}\log\!\left(\frac{e^{b\tau}-1}{e^{a\tau}-1}\right)>\tau.
\]
The post-shutdown delay \(\Delta=t_*-\tau\) **strictly increases** when either heat capacity increases, and **strictly decreases** when either the radiative feedback or interlayer exchange increases. It also strictly decreases with forcing duration, with \(0<\partial t_*/\partial\tau<1\). These conclusions hold throughout the positive-parameter domain, independently of forcing amplitude.

## Assumptions and scope
The surface and deep temperatures \(T_s,T_d\), initially zero, satisfy
\[
C_s\dot T_s=F(t)-\lambda T_s-\gamma(T_s-T_d),\qquad
C_d\dot T_d=\gamma(T_s-T_d),
\]
where \(C_s,C_d,\lambda,\gamma,F_0,\tau\) are **all strictly positive** and \(F(t)=F_0\) for \(0\le t<\tau\), \(F(t)=0\) for \(t\ge\tau\). The function \(F\) is prescribed direct radiative forcing; it is not an emissions or carbon-cycle experiment. Define
\[
C=\begin{pmatrix}C_s&0\\0&C_d\end{pmatrix},\quad
K=\begin{pmatrix}\lambda+\gamma&-\gamma\\-\gamma&\gamma\end{pmatrix},
\quad \text{with eigenvalues }0<a<b\text{ of }C^{-1/2}KC^{-1/2}.
\]
The pair \(a,b\) is the ordered pair of eigenvalues; explicitly
\[
a+b=\frac{\lambda+\gamma}{C_s}+\frac\gamma{C_d},
\qquad ab=\frac{\lambda\gamma}{C_s C_d}.
\]
The positive-definite matrix \(K\) gives \(0<a<b\) (strictly distinct because the off-diagonal coupling is nonzero). All peak claims are global over \(t\ge0\).

## Proof
Let \(k_s,k_d\) be the temperature impulse responses to unit surface forcing. Solving the linear system, or inverting its Laplace resolvent, gives for \(t\ge0\)
\[
k_s(t)=\frac{(\gamma/C_d-a)e^{-at}+(b-\gamma/C_d)e^{-bt}}{C_s(b-a)},
\qquad
k_d(t)=\frac{\gamma}{C_sC_d(b-a)}(e^{-at}-e^{-bt}).
\]
The characteristic polynomial evaluated at \(\gamma/C_d\) is negative: \(p(\gamma/C_d)=-\gamma^2/(C_sC_d)<0\), hence \(a<\gamma/C_d<b\). Thus \(k_s\) is positive and strictly decreasing; \(k_d(t)>0\) for all \(t>0\).

For either output, linear superposition gives \(T_j(t)=F_0\int_{\max(0,t-\tau)}^t k_j(u)\,du\). Before shutdown, \(T_j'(t)=F_0k_j(t)>0\) for \(0<t<\tau\). After shutdown, \(T_j'(t)=F_0[k_j(t)-k_j(t-\tau)]\). Since \(k_s\) is strictly decreasing, \(T_s\) decreases strictly after shutdown, making \(\tau\) its unique global peak.

For the deep layer, set \(A=e^{a\tau}-1>0\), \(B=e^{b\tau}-1>0\). For \(t>\tau\),
\[
T_d'(t)=\frac{F_0\gamma}{C_sC_d(b-a)}\bigl(-A e^{-at}+B e^{-bt}\bigr).
\]
Its sign is the sign of \(B/A-e^{(b-a)t}\), which crosses zero **exactly once**, at the claimed \(t_*\). Rewriting
\[
\Delta:=t_*-\tau
=\frac{1}{b-a}\log\left(\frac{1-e^{-b\tau}}{1-e^{-a\tau}}\right)
=\frac{1}{b-a}\int_a^b\frac{\tau}{e^{r\tau}-1}\,dr>0
\]
proves the strictly positive delay and gives a useful integral mean.

For each \(\tau>0\), the function \(g(r,\tau)=\tau/(e^{r\tau}-1)\) is strictly decreasing in \(r>0\); for each \(r>0\), it is strictly decreasing in \(\tau>0\), because \(e^x(1-x)-1<0\) for \(x>0\). An interval mean of a strictly decreasing continuous function strictly decreases whenever either endpoint increases. Therefore \(\Delta\) strictly decreases with \(a\), with \(b\), and with \(\tau\).

To translate this into physical parameter signs, regard \(K v=r C v\) as a symmetric generalized eigenproblem and choose \(v^TCv=1\). The simple eigenvalue perturbation formula is \(\partial r=v^T(\partial K-r\partial C)v\). For \(\lambda\), it is \(v_s^2>0\); for \(\gamma\), it is \((v_s-v_d)^2>0\). The equality \(v_s=v_d\ne0\) would contradict the generalized eigenproblem for \(\lambda>0\). For \(C_s\) and \(C_d\), the derivatives are \(-r v_s^2<0\) and \(-r v_d^2<0\), respectively. Both eigenvector entries are nonzero because \(\gamma>0\). Thus **both** \(a,b\) strictly increase under increasing \(\lambda\) or \(\gamma\), and strictly decrease under increasing either capacity. Combining this with the interval-mean monotonicity proves all four global comparative statics.

Finally, from \(t_*=\frac{1}{b-a}\int_a^b \tau/(1-e^{-r\tau})\,dr\), direct differentiation yields for \(x=r\tau>0\)
\[
\frac{\partial}{\partial\tau}\left(\frac{\tau}{1-e^{-r\tau}}\right)
=\frac{1-(1+x)e^{-x}}{(1-e^{-x})^2}\in(0,1).
\]
Positivity follows from \(e^x>1+x\); the strict upper bound follows from \(e^{-x}>1-x\). Taking the interval mean proves \(0<\partial t_*/\partial\tau<1\). All outputs scale linearly with \(F_0\), so their maximizing times do not depend on it.

## Verification
The accompanying standalone Python 3 program `check_two_box.py` rederives the characteristic-polynomial identities in exact rational arithmetic and tests representative eigenvalues, stationary points, signs, and finite-difference parameter comparisons. Run with `python3 check_two_box.py`; the observed output was `CHECK_OK representative_peak=22.2543875592 delay=12.2543875592`. For \(C_s=8\), \(C_d=100\), \(\lambda=1.3\), \(\gamma=0.7\), and \(\tau=10\), the peak occurs at \(t_*=22.2543875592\ldots\), delayed \(12.2543875592\ldots\) after shutdown. This numerical example corroborates, but does not prove, the global analytic statements above.

## Relationship to prior work
Geoffroy et al. (2013) introduced the linear two-layer analytical solution and analyzed step and linear forcing (with a separate abrupt return from ramped forcing). Hence the exact transfer function and ability to superpose a finite pulse are **covered by the general prior model**. The contribution here is the **global strict shape theorem**, including the unique deep peak and simultaneous four-parameter, all-positive-domain monotonicity. Held et al. (2010) discussed an abrupt return to preindustrial forcing, fast/slow climate timescales, and continued adjustment. Lutsko and Popp (2019) studied parameter sensitivities of the linear two-layer model in a frequency-space and ramp-forcing setting. These works supply motivation and closely related context; no priority is claimed for the linear system, its eigenvalues, superposition, or climate adjustment itself.

## Limitations
The theorem assumes positive constant linear coefficients, an exact rectangular *radiative forcing* pulse, zero initial anomaly, and two thermal layers. It does not incorporate carbon-cycle dynamics, feedback efficacy, spatial heterogeneity, ocean stratification or circulation, stochastic forcing, or nonlinear warming/cooling asymmetry. The full publisher rendering of Geoffroy et al.'s formulas and appendices could not be exhaustively inspected, and an equivalent specialized corollary may exist in broader two-box or linear-systems literature. Numerical spot checks are not a proof, and the relative merits of an actual climate calibration are outside this theorem.

## References
- O. Geoffroy et al., “Transient Climate Response in a Two-Layer Energy-Balance Model. Part I: Analytical Solution and Parameter Calibration Using CMIP5 AOGCM Experiments,” *Journal of Climate* 26 (2013), 1841–1857, DOI: 10.1175/JCLI-D-12-00195.1. Public date: 2013-03-15.
- I. M. Held et al., “Probing the Fast and Slow Components of Global Warming by Returning Abruptly to Preindustrial Forcing,” *Journal of Climate* (2010), DOI: 10.1175/2009JCLI3466.1.
- N. J. Lutsko and M. Popp, “Probing the Sources of Uncertainty in Transient Warming on Different Timescales,” *Geophysical Research Letters* (2019), DOI: 10.1029/2019GL084018.
