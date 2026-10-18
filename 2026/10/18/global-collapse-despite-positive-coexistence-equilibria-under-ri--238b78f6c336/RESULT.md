# Global collapse despite positive coexistence equilibria under risk–cost feedback

## Finding
In the three-variable collective-risk cooperation dynamics of Wang et al. (2026), an exact, parameter-only feedback inequality makes the maximal cooperation cost globally and exponentially selected for **every strictly interior trajectory**. When the maximal possible pivotal benefit is below that maximal cost, every interior trajectory converges exponentially to complete defection and maximal risk. This can happen even while **two positive cooperation equilibria exist on a cost-boundary face**, so stationary coexistence alone does not imply accessibility from fully mixed initial conditions. A second exact example shows that the strict benefit condition cannot be discarded uniformly across feedback parameters.

## Assumptions and scope
Fix integers \(N\ge3\) and \(2\le M\le N-1\), rates \(b,\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4>0\), and \(0<\beta<\alpha\). Put
\[
K(x)=\binom{N-1}{M-1}x^{M-1}(1-x)^{N-M},\quad
K_{\max}=K\bigl((M-1)/(N-1)\bigr).
\]
Study the autonomous flow
\[
\begin{aligned}
\dot x&=x(1-x)[bK(x)r-c],\\
\dot r&=r(1-r)[\mu_1-(\mu_1+\mu_2)x],\\
\dot c&=(\alpha-c)(c-\beta)[\theta_1-\theta_4-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r].
\end{aligned}
\]
For every initial condition \(0<x(0),r(0)<1\) and \(\beta<c(0)<\alpha\), the solution exists globally in the open box; closure of the box is invariant. Define
\[
\Delta=\theta_1\mu_2-\theta_2\mu_1-\theta_4(\mu_1+\mu_2),\qquad
\gamma=\frac{(\alpha-\beta)\Delta}{\mu_1+\mu_2}.
\]
**Theorem.** If \(\Delta>0\), then \(\alpha-c(t)=O(e^{-\gamma t})\) for every strictly interior solution, without a constraint on \(b\). If also \(bK_{\max}<\alpha\), the full trajectory converges exponentially to \((0,1,\alpha)\). In particular, the conclusion holds in the nonempty range \(\beta<bK_{\max}<\alpha\), in which positive boundary coexistence equilibria may still exist.

## Proof
**1. Uniform upper barrier for cooperation.** Let \(u=\log(x/(1-x))\). Since \(M<N\), \(K(1)=0\). Choose \(\xi\in(\mu_1/(\mu_1+\mu_2),1)\) so that \(bK(x)\le\beta/2\) for every \(x\ge\xi\). Whenever \(x\ge\xi\), \(\dot u=bK(x)r-c\le-\beta/2\). Consequently \(u(t)\le U:=\max\{u(0),\log(\xi/(1-\xi))\}<\infty\) for all \(t\ge0\). This bounded-logit property is crucial and is the reason for the hypothesis \(M<N\).

**2. Risk never approaches zero.** Put \(x_*=\mu_1/(\mu_1+\mu_2)\) and take \(r_0\in(0,1)\) with \(bK_{\max}r_0\le\beta/2\). While \(r\le r_0\), \(\dot u\le-\beta/2\). Hence the time spent in this region with \(x>x_*\) during any excursion below \(r_0\) is at most \(T=2\max(0,U-\log(x_*/(1-x_*)))/\beta\). In that portion, \(\frac d{dt}\log[r/(1-r)]=\mu_1-(\mu_1+\mu_2)x\ge-\mu_2\). Once \(x\le x_*\) while \(r\le r_0\), cooperation continues to decrease and risk cannot decrease further. Each excursion therefore has a risk minimum at least
\[
\rho=\operatorname{logistic}\!\left(\operatorname{logit}(\min\{r(0),r_0\})-\mu_2T\right)>0,
\]
where \(\operatorname{logistic}(z)=1/(1+e^{-z})\) and \(\operatorname{logit}(p)=\log(p/(1-p))\). Thus \(r(t)\ge\rho\) for all \(t\ge0\), with \(\rho\) allowed to depend on the initial state.

**3. An exact forced cost–risk identity.** Define
\[
 v=\log\frac r{1-r},\quad w=\log\frac{c-\beta}{\alpha-c},\quad
 k=\frac{(\alpha-\beta)(\theta_1+\theta_2)}{\mu_1+\mu_2}>0.
\]
Differentiating the exact equations gives
\[
\begin{aligned}
\dot v&=\mu_1-(\mu_1+\mu_2)x,\\
\dot w&=(\alpha-\beta)[\theta_1-\theta_4-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r],\\
\frac d{dt}(w-kv)&=(\alpha-\beta)(\theta_3+\theta_4)r+\gamma\ge\gamma>0.
\end{aligned}
\]
Therefore \(e^{-(w-kv)}\le e^{-(w(0)-kv(0))}e^{-\gamma t}\). Since \(r\ge\rho\),
\[
\alpha-c(t)
= (c(t)-\beta)\left(\frac{1-r(t)}{r(t)}\right)^k e^{-(w(t)-kv(t))}
\le(\alpha-\beta)\left(\frac{1-\rho}{\rho}\right)^k
 e^{-(w(0)-kv(0))}e^{-\gamma t}.
\]
This proves global exponential selection of the upper cost boundary, regardless of \(b\).

**4. Collapse once pivotal benefit is below upper cost.** Suppose \(bK_{\max}<\alpha\), and let \(d=(\alpha-bK_{\max})/2>0\). After a finite time the preceding estimate gives \(c\ge\alpha-d\); then \(\dot u=bK(x)r-c\le-d\). Consequently \(x(t)\le C_x e^{-dt}\). Eventually \(x\le x_*/2\), so \(\dot v\ge\mu_1/2\), giving \(1-r(t)\le C_r e^{-\mu_1t/2}\). Together with the cost estimate, the full state approaches \((0,1,\alpha)\) exponentially.

**5. Equilibrium coexistence and the sharpness witness.** Take \(N=3,M=2\), so \(K(x)=2x(1-x)\) and \(K_{\max}=1/2\). For \(b=3/5,\beta=1/5,\alpha=2/5,\mu_1=1,\mu_2=2\) and \((\theta_1,\theta_2,\theta_3,\theta_4)=(4,1,1,1)\), one has \(\Delta=4>0\) and \(\beta=1/5<3/10=bK_{\max}<2/5=\alpha\). Direct substitution verifies the two distinct equilibria \(((1\pm1/\sqrt3)/2,1,\beta)\). Nevertheless, all strictly interior initial conditions collapse by the theorem.

The strict benefit condition is meaningful. Keep \(N=3,M=2,\beta=1/5,\alpha=2/5\), but take \(b=1,\mu_1=4,\mu_2=1\), and \((\theta_1,\theta_2,\theta_3,\theta_4)=(12,1,1,1)\). Then \(\Delta=3>0\) and \(bK_{\max}=1/2>\alpha\). The positive-cooperation equilibrium \((x_+,1,\alpha)\), where \(x_+=(1+1/\sqrt5)/2\), has Jacobian eigenvalues
\[
-\frac{2\sqrt5}{25},\qquad \frac{\sqrt5-3}{2},\qquad \frac{13(\sqrt5-5)}{50},
\]
all strictly negative. Therefore a nonempty open subset of strictly interior initial conditions tends to that cooperative equilibrium, excluding any parameter-uniform global-defection theorem without an additional benefit restriction.

## Verification
The accompanying `verification/check.py` uses exact SymPy arithmetic to reconstruct the log-odds cancellation, both equilibrium witnesses, the pivotal peak calculation, and all three eigenvalue signs of the stable cooperative witness. Run `python verification/check.py` after installing `sympy>=1.12`. These finite symbolic checks support—but do not replace—the all-parameter analytical comparison and barrier proof above.

## Relationship to prior work
Wang et al. (2026), in their three-variable risk–cost–cooperation model, classified equilibrium branches and their local stability and observed multistability. The theorem here addresses a different question: a sufficient **global** convergence condition for every strictly interior initial state, plus a positive-equilibrium example where the global outcome nonetheless is defection. The two-variable adaptive risk–cooperation model of Liu, Chen and Szolnoki (2023) omits the dynamically evolving cost coordinate, so its phase diagram does not imply cost-boundary selection. Log-odds differentiation and scalar comparison are standard techniques; novelty is claimed only for the resulting global selection and coexistence-versus-accessibility boundary in this three-variable system.

## Limitations
The theorem is deterministic and well-mixed. It assumes strictly interior initial data and \(2\le M\le N-1\); exact boundary initial data can be stationary at positive cooperation. It gives sufficient parameter conditions and not an exhaustive global phase diagram. It does not address equality \(bK_{\max}=\alpha\), the \(\Delta\le0\) parameter region, finite populations, stochastic outcomes, or the separate extended feedback model with cost entering the risk equation. The supplementary PDF of the 2026 primary paper was not available for full independent comparison; an unnoticed stronger supplementary theorem remains an originality risk.

## References
1. L. Wang, S. Hua, Y. Liu, L. Zhang, L. Liu and A. Szolnoki, “Coevolutionary dynamics of cooperation, risk, and cost in collective risk games,” *PLOS Computational Biology* **22**, e1013512 (2026), published February 20, 2026. DOI: 10.1371/journal.pcbi.1013512.
2. L. Liu, X. Chen and A. Szolnoki, “Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game,” *eLife* **12**, e82954 (2023). DOI: 10.7554/eLife.82954.
