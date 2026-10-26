# An interior peak-optimal SIR budget split spends strictly more on prevention than an infectious-person-time optimum

## Finding
For the closed homogeneous SIR model with a fixed split between transmission prevention and improved recovery, let \(u\in[0,1]\) be the prevention fraction and let \(Q(u)=\int_0^\infty I_u(t)\,dt\) be cumulative infectious person-time per population member. If \(u_R\in(0,1)\) minimizes the controlled reproduction ratio, **every** global minimizer of \(Q\) lies strictly to the treatment-heavy side: \(u_Q<u_R\). If every allocation initially grows an epidemic, \(u_R\) is also the unique prevalence-peak minimizer. For fixed positive initial infection and response coefficients, sufficiently large baseline transmission makes \(Q\) strictly increasing, so its unique minimizer is \(u_Q=0\) although the peak minimizer can remain interior. A concrete exact example has \(u_Q=0\) and \(u_R=1/2\).

More precisely, for any \(\beta_0,\gamma_0,b,g>0\), define
\[
\beta(u)=\frac{\beta_0}{1+bu},\quad \gamma(u)=\gamma_0[1+g(1-u)],\quad
\mathcal R(u)=\frac{\beta(u)}{\gamma(u)},\quad
u_R=\operatorname{proj}_{[0,1]}\left[\frac12\left(1-\frac1b+\frac1g\right)\right].
\]
Then \(Q\) is strictly increasing on \([u_R,1]\) whenever \(u_R<1\), and its minimizing set is contained in \([0,u_R)\) when \(0<u_R<1\). If \(u_R=0\), the unique minimizer is \(0\). The strict high-transmission all-treatment limit holds for arbitrary fixed \(b,g,\gamma_0,S_0,I_0>0\), not only for the example.

## Assumptions and scope
Time is continuous and the population is normalized. For each *constant* choice \(u\in[0,1]\), the trajectory solves
\[
\dot S=-\beta(u)SI,\qquad \dot I=\beta(u)SI-\gamma(u)I,\qquad \dot R=\gamma(u)I.
\]
Initial values satisfy \(S(0)=S_0>0\), \(I(0)=I_0>0\), \(R(0)=1-S_0-I_0\ge0\). Parameters \(\beta_0,\gamma_0,b,g\) are strictly positive. The same constant allocation applies throughout the outbreak. Total infectious person-time \(Q\) is **not** the number of distinct people ever infected. Let \(P(u)=\sup_{t\ge0}I_u(t)\) be the prevalence peak. No demographic turnover, immunity loss, delayed switching, heterogeneous contacts, or time-varying intervention is assumed.

## Proof
**1. Final-size identity and smooth dependence.** Put \(M=S_0+I_0\), \(s=s(\mathcal R)=\lim_{t\to\infty}S(t)\), and \(A=M-s\). The closed SIR conservation law implies \(I(t)\to0\), \(A=\gamma(u)Q\), and
\[
s=S_0\exp(-\mathcal R A),\qquad I_0<A<M.
\]
The function \(f(A)=M-S_0e^{-\mathcal R A}-A\) is strictly concave, is positive at \(I_0\), and negative at \(M\); it has exactly one root in \((I_0,M)\), with negative derivative there. Thus \(y=\mathcal R s\in(0,1)\). Implicit differentiation yields
\[
\frac{dA}{d\mathcal R}=\frac{A s}{1-\mathcal R s}>0.
\]
Every derivative here is valid also when \(S_0\mathcal R\le1\), because \(I_0>0\).

**2. Exact slope law.** Define positive fractions
\[
h(u)=\frac{b}{1+bu},\quad g_*(u)=\frac{g}{1+g(1-u)},\quad y(u)=\mathcal R(u)s(\mathcal R(u)).
\]
As \(\mathcal R'/\mathcal R=g_*-h\) and \(\gamma'/\gamma=-g_*\), step 1 gives the exact identity
\[
\boxed{\quad\frac{Q'(u)}{Q(u)}=\frac{g_*(u)-y(u)h(u)}{1-y(u)}.\quad}
\]
The denominator is strictly positive. The product \((1+bu)[1+g(1-u)]\) is a strictly concave quadratic, so \(\mathcal R\) decreases before its unique clipped minimizer \(u_R\) and increases afterward. For \(u\ge u_R\) when \(u_R<1\), \(g_*\ge h\), so \(g_*-yh\ge g_*(1-y)>0\). At any interior minimizer \(u_R\) of \(\mathcal R\), \(Q'(u_R)>0\). Continuity, compactness, and strict increase on its right force **every** minimum of \(Q\) to lie strictly below \(u_R\). When \(u_R=0\), \(Q\) is strictly increasing everywhere.

**3. Peak comparison.** If \(S_0\mathcal R(u)>1\) for all \(u\in[0,1]\), the standard SIR first integral yields
\[
P(u)=M-\frac{1+\log(S_0\mathcal R(u))}{\mathcal R(u)},\qquad
\frac{dP}{d\mathcal R}=\frac{\log(S_0\mathcal R)}{\mathcal R^2}>0.
\]
Thus the peak's unique optimal allocation is \(u_R\). If some allocations are initially non-growing, the peak objective can have a flat minimum; the strict comparison is asserted specifically under the stated all-growing condition.

**4. Universal high-transmission regime.** Keep \(S_0,I_0,b,g,\gamma_0\) fixed and increase \(\beta_0\). Uniformly in \(u\in[0,1]\),
\[
\frac{\beta_0}{\gamma_0(1+b)(1+g)}\le\mathcal R(u)\le\frac{\beta_0}{\gamma_0},\quad
s(u)\le S_0e^{-\mathcal R(u)I_0}.
\]
Consequently \(0<y(u)\le (\beta_0S_0/\gamma_0)\exp[-\beta_0I_0/(\gamma_0(1+b)(1+g))]\to0\) uniformly. Since \(g_*(u)\ge g/(1+g)>0\) and \(h(u)\le b\), the slope law is strictly positive everywhere for sufficiently large \(\beta_0\). Hence \(Q\) has unique minimizer \(u_Q=0\), while \(u_R\) is independent of \(\beta_0\).

**5. A fully bounded example.** Take \(S_0=9/10\), \(I_0=1/10\), \(\beta_0=30\), \(\gamma_0=b=g=1\). Then
\[
\mathcal R(u)=\frac{30}{(1+u)(2-u)},\quad \frac{40}{3}\le\mathcal R(u)\le15,\quad u_R=\tfrac12.
\]
All allocations have \(S_0\mathcal R(u)\ge12>1\), so the peak is uniquely minimized at \(u_R=1/2\). From the final-size fixed point, \(A\ge I_0+S_0(1-e^{-\mathcal R I_0})\); since \(e^{4/3}>1+4/3>2\), it follows that \(A>11/20\). Hence
\[
y=\mathcal R s<\frac{27}{2}e^{-22/3}<\frac13.
\]
The last inequality follows rigorously from \(e^{22/3}>\sum_{j=0}^{3}(22/3)^j/j!>81/2\). With \(g_*(u)\ge1/2\) and \(h(u)\le1\), the slope numerator satisfies \(g_*-yh>1/6\). Thus the person-time optimum is uniquely \(u_Q=0\), not merely a numerical local minimum. Numerically \(Q(0)\approx0.499999862343\), whereas \(Q(1/2)\approx0.666665694890\); these decimals only illustrate the exact proof.

## Verification
Execute `python3 check.py` using Python 3, SciPy, and mpmath. The checker independently tests exact rational inequalities, the final-size relation by both root-finding and Lambert \(W\), finite-difference derivatives at interior allocations, and independent numerical ODE integration. It reports `CERTIFICATE_OK` with 522 checks. The infinite-domain strict optimization follows from the analytic slope and exponential inequalities, not sampled grid points. The code is ancillary to the proof.

## Relationship to prior work
Maity, Banerjee, Senapati and Chattopadhyay (2023) introduce the exact two-intervention production functions and derive the allocation minimizing **peak prevalence** as \(\frac12(1-1/b+1/g)\), including the initially non-growing flat-peak case. The controlled SIR model, peak formula, and peak optimum are not new. Their appendix analyzes peak allocation, not the objective \(\int_0^\infty I\,dt\) when the same budget also changes the recovery rate. Sereno and collaborators (2021) relate the integrated infectious profile to final epidemic size in an SIR control problem with a single recovery-time normalization, while Bolzoni and collaborators (2017) investigate epidemic eradication time under individually varied control types. Those known ingredients do not state the universal strict resource-ordering, high-transmission all-treatment optimum, or exact budget-split counterexample here. General optimization and final-size literature could contain more encompassing results; publication priority remains provisional.

## Limitations
The result covers deterministic well-mixed closed SIR and time-constant allocation only. It concerns infectious person-time, not infection incidence, deaths, monetary expenses, and epidemiologically realistic hospital occupancy without additional assumptions. The theorem orders optimizers but does not assert uniqueness of the person-time optimum for *all* parameter values, nor a uniform amount by which the two optimal allocations differ. The high-transmission conclusion is mathematical, not a clinical recommendation to neglect prevention. No finite simulation certifies an infinite-domain statement.

## References
1. B. Maity, S. Banerjee, A. Senapati, J. Chattopadhyay, *Quantifying optimal resource allocation strategies for controlling epidemics*, arXiv:2302.00960v1 (first public version 2023-02-02), https://arxiv.org/abs/2302.00960; *J. R. Soc. Interface* 20, 20230036 (2023), doi:10.1098/rsif.2023.0036.
2. J. Sereno et al., *Minimizing the Epidemic Final Size while Containing the Infected Peak Prevalence in SIR Systems*, arXiv:2111.05652 (2021), https://arxiv.org/abs/2111.05652.
3. L. Bolzoni et al., *Time-optimal control strategies in SIR epidemic models*, arXiv:1706.04447 (2017), https://arxiv.org/abs/1706.04447.
