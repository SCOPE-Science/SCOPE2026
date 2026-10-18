# Sharp algebraic consensus and a dwell-time reversal at the hybrid opinion pitchfork

## Finding
At the opinion-forming pitchfork of a hybrid continuous--discrete tanh dyad, the nonovershooting discrete update yields global attraction to the neutral consensus. For all componentwise nonnegative, nonzero initial opinions, both opinions have the same sharp inverse-square-root asymptotic, with an explicit coefficient that distinguishes iteration time from physical time. The sign-reversed assertion holds for nonpositive initial opinions.

Define \(L=\alpha+\gamma_r\), \(a=d\gamma_r/L\), \(q=e^{-ah}\), and
\[
C=\frac{L^3}{3\gamma_r}\,\frac{\gamma_h(1-q)}{1-(1-\gamma_h)q}>0.
\]
For the post-jump iterates \(z_n=z(nh)\), \(v_n=v(nh)\),
\[
\lim_{n\to\infty}\sqrt n\,z_n
=\lim_{n\to\infty}\sqrt n\,v_n=\frac{1}{\sqrt{2C}}.
\]
In real time, with \(v(t)\) piecewise constant between jumps,
\[
\lim_{t\to\infty}\sqrt t\,z(t)
=\lim_{t\to\infty}\sqrt t\,v(t)=\sqrt{\frac{h}{2C}}.
\]
Increasing the update gain \(\gamma_h\) or the dwell interval \(h\) strictly increases \(C\), improving the cubic relaxation per jump. However, increasing \(h\) strictly decreases \(C/h\) and therefore worsens the sharp relaxation per unit physical time. These are quantitative, model-specific conclusions at the exact pitchfork, not claims about the separate flip bifurcation of opinionated states.

## Assumptions and scope
Fix \(d>0\), \(\alpha\ge0\), \(\gamma_r>0\), \(h>0\), \(0<\gamma_h\le1\). Set the social-attention parameter exactly at the pitchfork,
\[
u=\frac d{\alpha+\gamma_r}.
\]
For each integer \(n\ge0\), hold the discrete opinion constant as \(v(t)=v_n\) on \([nh,(n+1)h)\), and solve
\[
\dot z(t)=-dz(t)+u\tanh(\alpha z(t)+\gamma_r v_n),
\quad z(nh)=z_n.
\]
At \((n+1)h\) set \(z_{n+1}=z((n+1)h^-)\) and
\[
v_{n+1}=(1-\gamma_h)v_n+\gamma_hz_{n+1}.
\]
Global existence and uniqueness of the flow hold because the right-hand side is globally Lipschitz. The gain restriction is mathematically substantive: it makes the jump a convex average and is not a claim for overshooting gains \(\gamma_h>1\). The universal positive amplitude is asserted for \(z_0,v_0\ge0\), not both zero. For \(z_0,v_0\le0\), not both zero, both limits have a negative sign. For arbitrary real initial opinions global convergence holds, but a nonzero universal amplitude is not asserted.

## Proof
**1. Uniform global attraction.** For a state at a jump, put \(M=\max(|z_n|,|v_n|)\). When \(M>0\), the vector field at the upper boundary \(z=M\) obeys
\[
-dM+\frac dL\tanh(\alpha M+\gamma_rv_n)
\le-dM+\frac dL\tanh(LM)<0.
\]
At \(z=-M\) the corresponding derivative is strictly positive, by oddness and strict monotonicity of tanh. Therefore every forward flow of positive duration enters \((-M,M)\), uniformly over its interval. Since \(0<\gamma_h\le1\), the jump takes \(v_n\) to a convex combination of \(v_n\) and \(z_{n+1}\), and \(\max(|z_{n+1}|,|v_{n+1}|)<M\). The stroboscopic map is continuous, and on any compact annulus separated from zero its strict maximum-norm decrement has a positive minimum. Thus the decreasing maximum norms must tend to zero. The positive and negative quadrants are forward invariant; if the nonnegative initial pair is nonzero, both sampled coordinates become strictly positive after one step. This establishes global critical consensus without linearized-stability inference.

**2. Exact cubic perturbation of a stochastic matrix.** Put \(K=dL^2/3\), \(q=e^{-ah}\), \(D=1-q+\gamma_hq\) and \(\psi(x)=x-\tanh x\). The exact flow is
\[
\dot z=-a(z-v_n)-u\psi(\alpha z+\gamma_r v_n),
\]
so variation of constants gives
\[
\begin{aligned}
z_{n+1}&=qz_n+(1-q)v_n-\delta_n,\\
\delta_n&=u\int_0^h e^{-a(h-r)}
\psi(\alpha z(nh+r)+\gamma_r v_n)\,dr.
\end{aligned}
\]
For positive opinions \(\delta_n>0\). The linearization of the stroboscopic map at zero is the row-stochastic matrix
\[
J=\begin{pmatrix}q&1-q\\\gamma_hq&1-\gamma_hq\end{pmatrix}.
\]
Its normalized positive stationary left vector is
\[
\ell=\left(\frac{\gamma_hq}{D},\frac{1-q}{D}\right).
\]
Define \(s_n=\ell_1z_n+\ell_2v_n>0\) and \(y_n=z_n-v_n\). The exact nonlinear recurrences become
\[
s_{n+1}=s_n-\frac{\gamma_h}{D}\delta_n,\qquad
 y_{n+1}=(1-\gamma_h)(qy_n-\delta_n).
\]
Because \(\ell_1,\ell_2>0\), both sampled coordinates are \(O(s_n)\); variation of constants implies the entire flow within a fixed dwell interval is \(O(s_n)\). Since \(\psi(x)=x^3/3+O(x^5)\), uniformly on that interval \(\delta_n=O(s_n^3)\). Hence \(s_{n+1}/s_n=1+O(s_n^2)\to1\).

**3. Collapse onto the slow direction.** Divide the exact recurrence for \(y_n\) by \(s_{n+1}\):
\[
\frac{y_{n+1}}{s_{n+1}}
=(1-\gamma_h)q\frac{s_n}{s_{n+1}}\frac{y_n}{s_n}
-(1-\gamma_h)\frac{\delta_n}{s_{n+1}}.
\]
The multiplier converges to \((1-\gamma_h)q<1\), while the forcing tends to zero. The normalized differences \(y_n/s_n\) are bounded, so the standard stable-affine-recursion estimate yields \(y_n/s_n\to0\). As \(\ell_1+\ell_2=1\), this proves \(z_n/s_n,v_n/s_n\to1\). The flow formula gives uniformly for \(r\in[0,h]\):
\[
z(nh+r)=s_n+o(s_n).
\]

**4. Exact asymptotic constant.** Uniform convergence in the previous step gives \(\alpha z(nh+r)+\gamma_rv_n=Ls_n+o(s_n)\), so
\[
\delta_n
=\frac{uL^3}{3}\frac{1-e^{-ah}}a\,s_n^3+o(s_n^3)
=\frac Ka(1-q)s_n^3+o(s_n^3).
\]
Therefore
\[
s_{n+1}=s_n-Cs_n^3+o(s_n^3),\qquad
C=\frac Ka\frac{\gamma_h(1-q)}{D}.
\]
Taking inverse squares shows \(s_{n+1}^{-2}-s_n^{-2}\to2C\); summation and division by \(n\) yield \(ns_n^2\to(2C)^{-1}\). The limits for both sampled coordinates follow. Uniform within-interval convergence and \(t/(nh)\to1\) establish the physical-time limits. Sign symmetry gives the negative-quadrant assertion.

**5. Update-frequency reversal.** Differentiating the explicit coefficient, holding the other parameters fixed, yields
\[
\frac{\partial C}{\partial\gamma_h}
=\frac Ka\frac{(1-q)^2}{D^2}>0,
\qquad
\frac{\partial C}{\partial h}
=K\frac{\gamma_h^2q}{D^2}>0.
\]
For \(x=ah>0\), the sign of \(\partial_h(C/h)\) is the sign of
\[
\gamma_hxe^{-x}-(1-e^{-x})[1-(1-\gamma_h)e^{-x}].
\]
This is negative: \(xe^{-x}<1-e^{-x}\), and \(1-(1-\gamma_h)e^{-x}\ge\gamma_h\). The small-dwell limit is \(C/h\to K=dL^2/3\). Thus a longer dwell helps by update count but slows convergence on the original physical clock. \(\square\)

## Verification
The standalone `verification/check.py` evaluates the exact stationary left eigenvector and stochastic Jacobian for five parameter configurations, integrates the continuous flow by fourth-order Runge--Kutta over 60,000 jumps per configuration, checks positivity, maximum-norm contraction, asymptotic scaled coordinates and the opposite monotonicities of \(C\) and \(C/h\). The maximum displayed relative asymptotic discrepancy is approximately \(2.1\times10^{-4}\). The symbolic identities and analytic arguments above, rather than finite numerical runs, prove all infinite-time statements. Run with `python3 verification/check.py` (Python standard library only).

## Relationship to prior work
Kumar and Yao (2026, doi:10.1109/lcsys.2026.3708586) introduce this hybrid continuous--discrete tanh--Rescorla--Wagner dyad, derive its stroboscopic Jacobian, and identify the pitchfork value \(u=d/(\alpha+\gamma_r)\). Their main focus is the higher-attention flip bifurcation, indecisive oscillations and feedback intervention. The accessible full article and the supplementary material's flip-normal-form sections do not establish a global attraction theorem at the pitchfork with a sharp, gain- and dwell-dependent algebraic amplitude. Bizyaeva, Franci and Leonard (2023) develop nonlinear opinion sensitivity and pitchfork principles in a different continuous network model. General cubic normal-form theory anticipates an inverse-square-root exponent, so that exponent alone is not presented as novel. The specifically proved quantitative contribution is global critical attraction for the nonovershooting hybrid map, its original-clock coefficient, and opposite frequency orderings.

## Limitations
The result is deterministic and dyadic with fixed parameters and synchronous regular jump intervals. It does not cover \(\gamma_h>1\), noise, varying attention, arbitrary network sizes, or a universal nonzero asymptotic amplitude for mixed-sign initial opinions. Historical novelty cannot be certified by finite bibliographic searches.

## References
1. R. Kumar and N. Yao, *Analysis of Bifurcation-Induced Indecisive Limit Cycles in Hybrid Opinion Dynamics with Social Attention-Controlled Consensus*, IEEE Control Systems Letters 10 (2026), 1789--1794, doi:10.1109/lcsys.2026.3708586, https://pmc.ncbi.nlm.nih.gov/articles/PMC13441232/ (published June 30, 2026).
2. R. Kumar and N. Yao, *Supplementary Material*, https://ciaolab.org/wp-content/uploads/2026/06/LCSS.pdf (sections A1.1--A1.2 inspected).
3. A. Bizyaeva, A. Franci and N. E. Leonard, *Nonlinear Opinion Dynamics With Tunable Sensitivity*, IEEE Transactions on Automatic Control (2023), https://naomi.princeton.edu/wp-content/uploads/sites/744/2023/03/Nonlinear_Opinion_Dynamics_With_Tunable_Sensitivity.pdf.
