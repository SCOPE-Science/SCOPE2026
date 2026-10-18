# Universal critical inverse-time and logarithmic relaxation at adaptive-reward saturation

## Finding
Consider the adaptive institutional-reward public-goods evolutionary system of Hua and Liu [1], with the parameters and variables specified below. There are two natural critical equality surfaces: the reward balance required to sustain the feedback-selected cooperation fraction exactly equals the institution's minimum reward or exactly equals its maximum reward. At **either** equality, every strictly interior trajectory reaches the critical equilibrium with an explicit inverse-time rate, and the inverse reward deviation has an exact logarithmic correction.

For integer \(N\ge2\), \(1<r<N\), and \(c,\delta,u,\varepsilon>0\), set
\[
g(x)=\sum_{j=0}^{N-1}(1-x)^j,\quad d=c(1-r/N),\quad q(x)=\frac{d}{\delta g(x)},\quad F(x)=\frac{\delta x(1-x)g(x)}{\varepsilon}.
\]
Let \(0<\alpha<\beta\), \(x_*=u/(u+1)\), and assume that \(a_*=q(x_*)\) equals **either** \(\alpha\) or \(\beta\). Define \(\sigma=1\) in the first case and \(\sigma=-1\) in the second case, as well as
\[
L=\beta-\alpha,\qquad D=(u+1)L,\qquad q_1=q'(x_*)>0,\qquad q_2=q''(x_*),\qquad F_*=F(x_*)>0.
\]
For **every** initial condition \(0<x(0)<1\), \(\alpha<a(0)<\beta\),
\[
\boxed{\lim_{t\to\infty}t\,\sigma(x(t)-x_*)=\frac1D,\qquad
\lim_{t\to\infty}t\,\sigma(a(t)-a_*)=\frac{q_1}{D}.}
\]
More precisely, an initial-condition-dependent finite real number \(C\) exists such that
\[
\boxed{\frac{1}{\sigma(a(t)-a_*)}=\frac{D}{q_1}t+
\left(\frac{D}{F_*q_1^2}-\frac{\sigma q_2}{2q_1^2}-\frac1L\right)\log t+C+o(1).}
\]
The cooperation-fraction inverse-time amplitude is independent of the group size, payoff parameters, incentive amount, and relative feedback speed except through \(u\) and the available reward interval \(L\). The relative speed \(\varepsilon\), absent from both leading limits, enters the explicit logarithmic coefficient through \(F_*\).

## Assumptions and scope
The dynamics are exactly
\[
\varepsilon\dot x=x(1-x)\big[-d+a\delta g(x)\big],\qquad
\dot a=(a-\alpha)(\beta-a)\big[u(1-x)-x\big].
\]
Here \(x\) is the cooperator proportion, \(a\) is reward intensity, and time is the original continuous physical time of the equations. Parameters are constant; no stochastic population interpretation or environmental time dependence is assumed. The equality \(q(x_*)\in\{\alpha,\beta\}\) and strict interior initial conditions are essential. The critical point lies at \((x_*,a_*)\), with \(x_*\in(0,1)\). The conclusions hold for **every** \(\varepsilon>0\), not only the fast-strategy regime.

## Proof
**1. Positive dynamics and a critical Lyapunov function.** Because \(g'(x)=-\sum_{j=1}^{N-1}j(1-x)^{j-1}<0\) on \((0,1)\), the function \(q\) is strictly increasing. The equations can be written
\[
\dot x=F(x)(a-q(x)),\qquad \dot a=(u+1)(a-\alpha)(\beta-a)(x_*-x).
\]
Every strictly interior solution remains interior at each finite time and exists for all positive time, because the closed rectangle is invariant and the vector field is smooth. Define
\[
V(x,a)=\int_{x_*}^{x}\frac{s-x_*}{F(s)}\,ds+
\begin{cases}
\displaystyle\frac{1}{u+1}\log\frac{\beta-\alpha}{\beta-a},&a_*=\alpha,\\[4pt]
\displaystyle\frac{1}{u+1}\log\frac{\beta-\alpha}{a-\alpha},&a_*=\beta.
\end{cases}
\]
Both terms are nonnegative and vanish together only at the critical equilibrium. Direct differentiation gives the exact identity
\[
\dot V=-(x-x_*)\big(q(x)-q(x_*)\big)\le0.
\]
The first integral diverges as \(x\downarrow0\) or \(x\uparrow1\). The second term diverges at the reward boundary opposite to \(a_*\). Consequently a sublevel of \(V\), closed by adjoining just the critical reward face, is compact and positively invariant. Equality \(\dot V=0\) requires \(x=x_*\), where \(\dot x=F_*(a-a_*)\) is nonzero unless \(a=a_*\). LaSalle's invariance argument therefore proves \((x(t),a(t))\to(x_*,a_*)\) for all the stated initial conditions. This convergence is used only as a verified premise for the **new quantitative rates**; global boundary selection itself is established in earlier related analysis.

**2. One-sided passage and leading coefficients.** Set
\[
y=\sigma(a-a_*)>0,\qquad z=\sigma(x-x_*),\qquad C(y)=(u+1)(L-y).
\]
For both choices of \(\sigma\), the exact equations become
\[
\dot z=F(x_*+\sigma z)\,[y-G(z)],\qquad
\dot y=-C(y)zy,\qquad
G(z)=\sigma[q(x_*+\sigma z)-q(x_*)].
\]
On \(z=0\), the vector field has \(\dot z=F_*y>0\). If a trajectory remained on \(z<0\) forever, then \(\dot y>0\), contradicting \(y(t)\to0\). Hence \(z>0\) from some finite time onward, and thereafter \(y\) decreases. Let \(h=z/y\). Since \(G(z)/z\to q_1\), its exact equation
\[
\dot h=F(x_*+\sigma z)\left[1-\frac{G(z)}z h\right]+C(y)zh
\]
is an asymptotically stable scalar linear equation, with limiting forcing \(F_*\) and damping \(F_*q_1\). It follows by variation of constants that \(h\to1/q_1\). Now
\[
\frac{d}{dt}\frac1y=C(y)h\longrightarrow\frac D{q_1}.
\]
Therefore \(ty\to q_1/D\) and \(tz\to1/D\), proving the leading laws.

**3. Logarithmic correction with a controlled remainder.** Taylor's theorem yields
\[
G(z)=q_1z+\frac{\sigma q_2}{2}z^2+O(z^3),\qquad
F(x_*+\sigma z)=F_*+O(z).
\]
Put \(k=1/q_1\) and \(\ell=D/(F_*q_1^3)-\sigma q_2/(2q_1^3)\). Substitution in the exact equation for \(h\) shows that \(e=h-k-\ell y\) satisfies
\[
\dot e=-\big(F_*q_1+O(y)\big)e+O(y^2).
\]
Indeed the constant and first-order forcing terms cancel by the definitions of \(k\) and \(\ell\); the derivative \(\ell\dot y\) is itself \(O(y^2)\). The already proved \(y\sim q_1/(Dt)\), the positivity of \(F_*q_1\), and variation of constants imply \(e=O(y^2)\): split the exponentially weighted convolution at half the observation time to bound its recent forcing by \(O(t^{-2})\). Thus
\[
\frac{d}{dt}\frac1y=Dk+\big(D\ell-(u+1)k\big)y+O(y^2).
\]
The leading law first gives \(1/y=(D/q_1)t+O(\log t)\), and hence \(y=q_1/(Dt)+O(\log t/t^2)\). Inserting this into the last differential identity produces an integrable error after subtracting both the linear and logarithmic derivatives. Integration proves existence of \(C\) and the asserted expansion, since
\[
\frac{D\ell-(u+1)k}{D/q_1}=\frac{D}{F_*q_1^2}-\frac{\sigma q_2}{2q_1^2}-\frac1L.
\]
No numerical or finite-time assumption enters this infinite-time argument.

## Verification
An exact-parameter check takes \(N=3\), \(r=2\), \(c=1\), \(u=1\), \(\varepsilon=1\), \(\alpha=1/2\), \(\beta=2\), giving \(x_*=1/2\), \(g(x_*)=7/4\). For the lower critical boundary choose \(\delta=8/21\). Then \(a_*=\alpha\), \(q_1=4/7\), and
\[
\lim_{t\to\infty}t(a(t)-1/2)=\frac4{21},\quad
\lim_{t\to\infty}t(x(t)-1/2)=\frac13,\quad
\frac1{a(t)-1/2}=\frac{21}4t+\frac{160}3\log t+C+o(1).
\]
For the upper critical boundary choose instead \(\delta=2/21\). Then \(a_*=\beta\), \(q_1=16/7\), and
\[
\lim_{t\to\infty}t(2-a(t))=\frac{16}{21},\quad
\lim_{t\to\infty}t(1/2-x(t))=\frac13,\quad
\frac1{2-a(t)}=\frac{21}{16}t+\frac{643}{48}\log t+C+o(1).
\]
Every limit in these displays is as \(t\to\infty\). The standalone script `verify_reward_edge.py` performs exact rational identity checks and independently integrates both cases to verify approach toward the leading constants and logarithmic coefficients. The code uses Python and SciPy. These numerical checks are supplemental; the preceding argument proves all infinite-time statements.

## Relationship to prior work
Hua and Liu [1] define the coupled public-goods/reward system and identify interior and boundary equilibria with local stability conditions. Their full arXiv manuscript, including the appendix, treats several strict-parameter scenarios but does not state inverse-time asymptotics or their logarithmic corrections at either reward saturation equality. Related previous analysis already establishes global equilibrium selection, including equality cases; that qualitative convergence is not claimed as new. The new mathematical content is the joint, all-initial-data, exact leading amplitudes at **both** reward boundaries and the next logarithmic term that separates the influence of relative adjustment speed. Weitz and collaborators [2] develop broader feedback-evolving replicator models with different payoff and environment mechanisms, including oscillatory behavior; their statements do not yield these model-specific coefficients. General nonlinear-stability and center-manifold techniques motivate the method but do not by themselves supply the displayed formulas for this constrained reward mechanism.

## Limitations
The law concerns an autonomous deterministic, infinitely large, well-mixed public-goods population and the particular polynomial incentive feedback. It does not assert the same amplitudes in finite stochastic games, nonlinear feedback laws, time-dependent incentives, or networked populations. Initial conditions on an invariant edge are excluded: a trajectory initialized on the critical reward edge may converge exponentially rather than algebraically. The logarithmic coefficient is an exact statement for fixed parameters and fixed positive \(\varepsilon\), not a uniform joint limit as the speed tends to zero. Independent scientific validation and exhaustive global publication-priority verification have not been performed.

## References
[1] Shijia Hua and Linjie Liu, *Coevolutionary dynamics of population and institutional rewards in public goods games*, arXiv:2308.09530v1, first posted 2023-08-18; journal DOI: 10.1016/j.eswa.2023.121579. https://arxiv.org/html/2308.09530v1

[2] Joshua S. Weitz, Ceyhun Eksin, Keith Paarporn, Sam P. Brown, and William C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113 (2016), E7518–E7525, DOI: 10.1073/pnas.1604096113. https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/
