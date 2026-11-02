# Exact cooperation balance and fluctuation penalty under periodic environmental forcing

## Finding

In the eco-evolutionary public-goods equations (9) of Jiang et al. [1, 2], with any integer group size \(N\geq2\), every strictly interior time-periodic solution satisfies an **exact payoff-weighted cooperation calibration**: the time average of cooperation weighted by defector payoff is \(\theta/(1+\theta)\), regardless of the waveform, period, or amplitude of the prescribed positive global environment \(w(t)\).

For the natural pairwise case \(N=2\), this becomes the unweighted, finite-amplitude mean–variance law
\[
\operatorname{Var}_T(x)=\bar x\left(\frac{\theta}{1+\theta}-\bar x\right).
\]
Every nonconstant interior periodic response consequently has \(\bar x<\theta/(1+\theta)\), although the corresponding static-environment interior equilibrium has cooperator fraction \(\theta/(1+\theta)\).

The conclusion is nonvacuous within the parameter constraints of [1, 2]. For the admissible values \(N=2\), \(\theta=r_d=1\), \(\alpha=3/2\), \(\beta=9/5\), and \(\varepsilon=12\), the forcing \(w(t)=1+\eta\cos t\) has, for every sufficiently small nonzero real \(\eta\), a unique locally exponentially attracting \(2\pi\)-periodic interior orbit near \((x,r)=(1/2,5/3)\). Its temporal mean satisfies
\[
\bar x(\eta)=\frac12-\frac{625}{54772}\eta^2+O(\eta^4).
\]
These are statements about periodic orbits and local periodic response, not about global attraction for arbitrary forcing amplitudes.

## Assumptions and scope

Fix an integer \(N\geq2\) and constants \(\varepsilon>0\), \(\theta>0\), \(0<r_d\leq\alpha<\beta<N\), with \(1<\alpha\) as in [1, 2]. Let the externally prescribed function \(w:\mathbb R\to(0,\infty)\) be continuous and \(T\)-periodic for some \(T>0\). Define
\[
S(t,x)=1+(w(t)-1)x,\qquad
P_N(t,x)=\frac{w(t)S(t,x)^{N-1}-1}{N(w(t)-1)},\qquad
Q_N(t,x)=\frac{S(t,x)^{N-1}-1}{N(w(t)-1)}.
\]
At times where \(w(t)=1\), use the continuous extensions \(P_N=[1+(N-1)x]/N\) and \(Q_N=(N-1)x/N\). Let \(A=rP_N-1\), \(B=r_dQ_N\), and study the exact published system
\[
\dot x=x(1-x)(A-B),\qquad
\dot r=\varepsilon(r-\alpha)(\beta-r)[-xA+\theta(1-x)B].
\tag{1}
\]
A strictly interior \(T\)-periodic solution means a classical solution with \(0<x(t)<1\), \(\alpha<r(t)<\beta\), and \((x(t+T),r(t+T))=(x(t),r(t))\) for all real \(t\). The average of a \(T\)-periodic observable \(h\) is \(\bar h=T^{-1}\int_0^T h(t)\,dt\). The temporal variance is \(\operatorname{Var}_T(x)=\overline{x^2}-\bar x^2\). Since \(x>0\), \(r_d>0\), and \(w>0\), one has \(B>0\) along such a solution.

## Proof

**Exact cancellation.** On the interior define
\[
H(x,r)=-\log(1-x)+\frac{1}{\varepsilon(\beta-\alpha)}\log\frac{r-\alpha}{\beta-r}.
\]
By differentiating and substituting (1), without approximating \(w\),
\[
\begin{aligned}
\frac{dH}{dt}
&=x(A-B)+[-xA+\theta(1-x)B]\\
&=B[\theta-(1+\theta)x].
\end{aligned}
\tag{2}
\]
Integration over the common period makes the left side vanish. As \(B>0\),
\[
\frac{\overline{xB}}{\overline B}=\frac{\theta}{1+\theta}.
\tag{3}
\]
This is the announced all-group-size, all-amplitude calibration. It is stronger than the condition for a static equilibrium because it applies to arbitrary nonconstant periodic trajectories of the nonautonomous system.

**Pairwise fluctuation law.** If \(N=2\), the factors simplify exactly to \(P_2=(1+w x)/2\) and \(Q_2=x/2\), including at \(w=1\). Hence \(B=r_d x/2\), so (3) is \(\overline{x^2}=[\theta/(1+\theta)]\bar x\). Subtracting \(\bar x^2\) gives the displayed variance law. The variance is strictly positive for nonconstant continuous \(x\), proving \(0<\bar x<\theta/(1+\theta)\). If \(x\) is constant, (3) instead forces \(x=\theta/(1+\theta)\).

**Existence of genuine periodically forced responses.** In the stated rational example, when \(\eta=0\), \(w=1\) and \((x_*,r_*)=(1/2,5/3)\) is an interior equilibrium. Direct exact differentiation gives the Jacobian
\[
J=\begin{pmatrix}1/12&3/16\\-8/45&-1/10\end{pmatrix},\qquad
\operatorname{tr}J=-1/60<0,\qquad \det J=1/40>0.
\]
Both eigenvalues have strictly negative real parts. At \(\eta=0\), the derivative of the time-\(2\pi\) Poincaré map is \(e^{2\pi J}\), so the derivative of the fixed-point equation with respect to the initial state, \(e^{2\pi J}-I\), is invertible. Analytic dependence of the time map and the implicit-function theorem yield a unique analytic branch of \(2\pi\)-periodic solutions in a neighborhood for sufficiently small \(\eta\); continuity preserves strict interiority and exponential attraction.

For \(\eta\ne0\), its \(x\) component cannot be constant. Indeed, if \(x\equiv c\) on such a periodic solution, (3) gives \(c=1/2\). Then \(\dot x=0\) forces \(A=B\) at all times, and the second equation of (1) forces \(\dot r=0\). But with fixed positive \(r\) and \(c=1/2\), \(A=r(1+w(t)c)/2-1\) cannot equal the constant \(B=c/2\) for nonconstant \(w\). Thus the strict mean gap occurs on an actual attracting periodic response.

**Sharp small-forcing coefficient.** At the unforced equilibrium, the vector derivative of the right side with respect to \(\eta\), divided by \(\cos t\), equals \(f=(5/48,-1/18)^\mathsf T\). For the first harmonic of the orbit write \(u(t)=\operatorname{Re}(z e^{it})\), where \((iI-J)z=f\). Exact inversion gives
\[
z_x=\frac{25}{13693}-\frac{2925}{27386}i,\qquad |z_x|^2=\frac{625}{54772}.
\]
The analytic periodic orbit has \(x(t;\eta)=1/2+\eta\operatorname{Re}(z_xe^{it})+O(\eta^2)\) uniformly in time, so its variance is \(\eta^2|z_x|^2/2+O(\eta^3)\). The exact variance identity at \(\theta=1\) gives \(1/2-\bar x=\operatorname{Var}_T(x)/\bar x\), implying the coefficient \(|z_x|^2\). The unique periodic orbit at parameter \(-\eta\) is the orbit at \(+\eta\) shifted by \(\pi\) in time; therefore its average is an even analytic function of \(\eta\). All odd coefficients vanish, upgrading the remainder to \(O(\eta^4)\).

## Verification

The standalone program `verify.py` checks the algebraic cancellation, exact rational Jacobian, forcing derivative, and complex first-harmonic coefficient using SymPy. It checks the original quotient expressions against their \(N=2\) reductions and continuous extensions, and independently solves a high-accuracy time-\(2\pi\) shooting problem for three nonzero amplitudes using SciPy. It tests the exact temporal mean–variance identity and the quadratic asymptotic, with positive interior margins. Run `python verify.py` after installing the libraries recorded in `requirements.txt`.

For example, for \(\eta=0.08\) it obtains \(\bar x\approx0.499926994862\), \(\operatorname{Var}_{2\pi}(x)\approx3.649723914\cdot10^{-5}\), and the exact identity residual is below numerical integration error. Numerical evidence corroborates but does not replace the all-parameter integration proof or the implicit-function theorem.

## Relationship to prior work

Jiang et al. [1, 2] introduce (1), prove the static-environment interior equilibrium fraction \(x_*=\theta/(1+\theta)\), and study periodic environments through phase-plane trajectories. Their equilibrium formula does not determine the **time average** of a nonstationary orbit; it does not by itself imply (3), the pairwise finite-amplitude variance penalty, or the explicit locally attracting forced example. The cancellation in (2) is specific to their payoff-dependent feedback, not a generic conclusion from autonomous equilibrium equations.

Weitz et al. [3], Tilman et al. [4], and Wang and Fu [5] develop or survey eco-evolutionary feedback and oscillatory behavior, with different feedback laws or general frameworks. Those broader results motivate but do not supply the stated formula for the Jiang et al. system. An exact equivalent in unindexed or inaccessible supplementary literature remains a bibliographic risk.

## Limitations

The weighted calibration applies only to strictly interior periodic solutions with bounded periodic environmental forcing; it asserts neither existence nor global attraction in arbitrary parameter regions. Strict unweighted mean suppression is proved for \(N=2\), not automatically for larger \(N\), where the defector-payoff weight depends on both \(w\) and \(x\). Local periodic existence and attraction are proved only for the explicit rational example and sufficiently small nonzero sinusoidal forcing. The numerical tests do not certify all amplitudes or infer infinite-dimensional behavior from finite runs. No claim is made about stochastic population sizes, other environmental feedback mechanisms, or independent validation.

## References

[1] Y. Jiang, X. Wang, L. Liu, M. Wei, J. Zhao, Z. Zheng, S. Tang, *Nonlinear eco-evolutionary games with global environmental fluctuations and local environmental feedbacks*, arXiv:2212.06497v1, first public version 2022-12-13, https://arxiv.org/abs/2212.06497 .

[2] The same authors, *PLoS Computational Biology* **19** (2023), e1011269, https://doi.org/10.1371/journal.pcbi.1011269 , especially Eq. (9) and the static/periodic environment sections.

[3] J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, *PNAS* **113** (2016), E7518–E7525, https://doi.org/10.1073/pnas.1604096113 .

[4] A. R. Tilman, J. B. Plotkin, E. Akçay, *Evolutionary games with environmental feedbacks*, *Nature Communications* **11** (2020), 915, https://doi.org/10.1038/s41467-020-14531-6 .

[5] X. Wang and F. Fu, *Eco-evolutionary dynamics with environmental feedback: cooperation in a changing world*, arXiv:2008.07671 (2020), https://arxiv.org/abs/2008.07671 .
