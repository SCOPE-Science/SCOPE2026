# Global mixed-endemic convergence with finite-rate evolutionary protection

## Finding

In a homogeneous deterministic SIS population in which susceptible and infected individuals independently revise protection choices by replicator dynamics, a mixed-protection endemic equilibrium attracts **every** solution with initially positive infection, both susceptible strategies represented, and fewer than all infected individuals unprotected. This holds for **every positive finite** ratio of the epidemic, susceptible-learning, and infected-learning timescales; no singular fast-behavior limit is required.

More strongly, a joint infection–behavior entropy controls the total squared deviation of infection prevalence from its eventual equilibrium, despite the transient contribution of initially unprotected infected individuals.

## Assumptions and scope

Let \(y\) be the infected fraction; \(z\) the fraction of susceptibles who do not adopt protection; and \(w\) the fraction of infected individuals who do not adopt protection. Introduce susceptible-protection efficacy \(0<\alpha<1\), transmission coefficients \(0<\beta_p<\beta_u<1\), recovery rate \(\gamma>0\), infection-loss parameter \(L>0\), susceptible protection cost \(c>0\), learning speeds \(\rho_S,\rho_I>0\), and positive infected payoff advantage of protection \(\kappa>0\). Write \(u=1-\alpha\), \(\Delta=\beta_u-\beta_p\), \(A(z)=\alpha+uz\), and \(B(w)=\beta_p+\Delta w\). Consider the exactly specified autonomous system

\[
\begin{aligned}
\dot y&=y\big((1-y)A(z)B(w)-\gamma\big),\\
\dot z&=\rho_S z(1-z)\big(c-LuB(w)y\big),\\
\dot w&=-\rho_I\kappa w(1-w).
\end{aligned}
\]

Define

\[
q=\frac{c}{Lu\beta_p},\qquad p=\frac{\gamma/(\beta_p(1-q))-\alpha}{u}.
\]

Assume \(0<q<1\) and \(\alpha\beta_p(1-q)<\gamma<\beta_p(1-q)\); these conditions give \(0<p<1\). The initial condition lies in \(0<y(0)\le1\), \(0<z(0)<1\), \(0\le w(0)<1\). There is no hypothesis that \(\rho_S\) or \(\rho_I\) is large or small.

**Theorem.** All such solutions converge to the unique equilibrium in the specified interior/boundary class:

\[\lim_{t\to\infty}(y(t),z(t),w(t))=(q,p,0).\]

Set

\[
V(y,z)=y-q-q\log(y/q)+\frac{1-q}{\rho_S L}\left[p\log(p/z)+(1-p)\log\left(\frac{1-p}{1-z}\right)\right].
\]

Then the following explicit, initial-state-dependent dissipation budget holds:

\[
\boxed{\beta_p\alpha\int_0^\infty (y(t)-q)^2\,dt\ \le\ V(y(0),z(0)) +\frac{2\Delta}{\rho_I\kappa}\log\frac{1}{1-w(0)}.}
\]

In particular, a nonconstant periodic or recurrent endemic orbit cannot lie in the specified attracting domain.

## Proof

**1. Forward invariance and infected protection.** The vector field is polynomial and leaves the cube \([0,1]^3\) forward invariant: at \(y=0\), its derivative is zero, and at \(y=1\) it is \(-\gamma\); each strategy boundary is invariant. The factors \(y\) and \(z(1-z)\) preserve strict positivity of \(y,z,1-z\) over finite intervals. The last equation is a scalar logistic decay and gives, with \(k=\rho_I\kappa>0\),

\[
w(t)=\frac{w(0)}{w(0)+(1-w(0))e^{kt}},\qquad
\int_0^\infty w(t)\,dt=\frac{1}{k}\log\frac1{1-w(0)}.
\]

These identities include \(w(0)=0\) by continuity.

**2. Exact entropy cancellation.** Both terms defining \(V\) are nonnegative: the first is the usual one-dimensional relative-entropy function and the second is a Bernoulli relative entropy. Differentiation along the specified vector field gives

\[
\begin{aligned}
\dot V&=(y-q)\big((1-y)A(z)B(w)-\gamma\big)\\
&\qquad+\frac{1-q}{L}(z-p)\big(c-LuB(w)y\big).
\end{aligned}
\]

Use \(c=Lu\beta_p q\) and \(\gamma=\beta_p(1-q)A(p)\), and write \(B(w)=\beta_p+\Delta w\). After collecting terms,

\[
\boxed{\dot V=-\beta_p A(z)(y-q)^2 +\Delta w\left[(y-q)(1-y)A(z)-(1-q)u y(z-p)\right].}
\]

On the invariant probability cube, \(\alpha\le A(z)\le1\), and the absolute value of the expression in square brackets is at most \(2\). Therefore

\[\dot V\le-\beta_p\alpha(y-q)^2+2\Delta w.\]

Integrating from zero to time \(T\), dropping nonnegative \(V(T)\), and then taking \(T\to\infty\), proves the boxed dissipation bound.

**3. Uniform interiority.** The same inequality without its negative term gives a finite uniform upper bound for \(V(t)\). Because \(y-q-q\log(y/q)\to\infty\) as \(y\downarrow0\), and the Bernoulli entropy diverges as \(z\downarrow0\) or \(z\uparrow1\), the trajectory remains in a compact subset with \(y>0\) and \(0<z<1\) for all time. All derivatives of the state and of the vector field are bounded there.

**4. Convergence.** The dissipation bound shows \(\int_0^\infty(y-q)^2dt<\infty\). Since \(\dot y\) is bounded, \(y-q\) is uniformly continuous; the elementary finite-energy/uniform-continuity argument gives \(y(t)\to q\). Because \(\ddot y\) is bounded, \(\dot y\) is uniformly continuous. Together with convergence of \(y\), this forces \(\dot y(t)\to0\). The logistic formula gives \(w(t)\to0\). Divide the first differential equation by \(y(t)\), which stays bounded away from zero, and pass to the limit:

\[
(1-q)\beta_p A(z(t))\longrightarrow\gamma=\beta_p(1-q)A(p).
\]

As \(A\) is strictly increasing (\(u>0\)), \(z(t)\to p\). This proves convergence of all three coordinates. Any equilibrium in the stated initial-state domain must have \(w=0\), \(y=q\), and \(z=p\), giving uniqueness there.

## Verification

The included `verify.py` uses exact symbolic differentiation and factorization to check the entropy identity without relying on a trajectory simulation. It also checks the rational parameter instance

\[
(\alpha,\beta_p,\beta_u,\gamma,L,c,\rho_S,\rho_I,\kappa)
=\left(\tfrac12,\tfrac34,\tfrac78,\tfrac{27}{64},4,\tfrac38,\tfrac23,4,\tfrac15\right),
\]

for which \(q=1/4\) and \(p=1/2\). Independently, deterministic numerical integrations from three widely separated initial states converge to the displayed equilibrium within the numerical tolerances documented in `VERIFICATION.md`. Such experiments are finite-time consistency checks only; they are not used in the all-time theorem.

Run `python verify.py` with Python 3 and SymPy as specified in `requirements.txt`.

## Relationship to prior work

The model equations are a homogeneous, arbitrary-positive-learning-speed specialization of the SIS-replicator protection framework in Satapathi, Dhar, Hota and Srivastava (arXiv:2203.10276; arXiv:2209.07348). Those studies classify equilibria and their local stability and examine fast-behavior reductions; their presented results do not yield global attraction of the full finite-speed mixed-endemic equilibrium from the entire specified initial domain, nor this dissipation budget. The related networked protection-adoption study (arXiv:2407.03126) analyzes a reduced epidemic system using timescale separation, rather than the stated global full-system claim.

The distinct model of Frieswijk, Zino, Ye, Rizzo and Cao (arXiv:2203.04016) includes a social-imitation feedback term, complete protection, and a different evolutionary state equation; it admits an attracting cycle in some regimes. That does not contradict a theorem for the different partial-protection payoff structure and positive \(\alpha\) stipulated above.

## Limitations

The theorem excludes disease-free initial states, pure susceptible-strategy boundaries, and the invariant all-unprotected-infected face \(w=1\). It assumes \(\alpha>0\), positive protected transmission \(\beta_p\), strictly better infected payoff for adopting protection, and the explicit interior-equilibrium inequalities. It establishes deterministic asymptotic convergence, not stochastic extinction probabilities, quantitative pointwise convergence rates, global behavior outside the given regime, or convergence in heterogeneous networks. The coefficient in the displayed integral bound is conservative; no claim of optimality is made. Bibliographic priority against all possible unindexed equivalent Lyapunov arguments has not been independently established.

## References

1. A. Satapathi, N. K. Dhar, A. R. Hota and V. Srivastava, *Epidemic Propagation under Evolutionary Behavioral Dynamics: Stability and Bifurcation Analysis*, arXiv:2203.10276v1 (19 March 2022), https://arxiv.org/abs/2203.10276.
2. A. Satapathi, N. K. Dhar, A. R. Hota and V. Srivastava, *Coupled Evolutionary Behavioral and Disease Dynamics under Reinfection Risk*, arXiv:2209.07348v1 (15 September 2022), https://arxiv.org/abs/2209.07348.
3. A. Satapathi and A. R. Hota, *Game-Theoretic Protection Adoption Against Networked SIS Epidemics*, arXiv:2407.03126v1 (3 July 2024), https://arxiv.org/abs/2407.03126.
4. K. Frieswijk, L. Zino, M. Ye, A. Rizzo and M. Cao, *A mean-field analysis of a network behavioural-epidemic model*, arXiv:2203.04016v1 (8 March 2022), https://arxiv.org/abs/2203.04016.
