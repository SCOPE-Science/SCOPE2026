# Resonant extinction slip at a double cancellation in a strong-Allee Holling–Tanner flow

## Finding

Fix real parameters \(A>0\) and \(0<M<1\) with \(A\ne 1+M\), and set
\[
 S=M,\qquad Q=\frac{A(1+M)}2,\qquad \delta=\frac{1+M-A}{A}\ne0.
\]
Consider the dimensionless **physical-time** Holling–Tanner equations on \(u,v>0\):
\[
 \frac{du}{d\theta}=u\left[(1-u)(u-M)-\frac{Qv}{u+A}\right],
 \qquad
 \frac{dv}{d\theta}=M v\left(1-\frac vu\right). \tag{1}
\]
For every strictly positive solution of (1) satisfying \((u(\theta),v(\theta))\to(0,0)\), there exist trajectory-dependent constants \(L>0\) and \(H\in\mathbb R\) such that
\[
 u(\theta)=L e^{-M\theta}-\frac{\delta L^3}{2M}e^{-3M\theta}
                  +o(e^{-3M\theta}), \tag{2}
\]
\[
 \frac{v(\theta)}{u(\theta)}
 =2+e^{-2M\theta}\left(-2\delta L^2\theta+H+o(1)\right). \tag{3}
\]
In particular, **the first nonzero predator/prey ratio defect is resonantly logarithmic in the vanishing prey density**:
\[
 \boxed{\displaystyle\lim_{\theta\to\infty}
 \frac{v(\theta)/u(\theta)-2}{\theta\,u(\theta)^2}=-2\delta\ne0.} \tag{4}
\]
Equivalently the predator has the sharper physical-time expansion
\[
 v(\theta)=2L e^{-M\theta}-2\delta L^3\theta e^{-3M\theta}
 +\left(LH-\frac{\delta L^3}{M}\right)e^{-3M\theta}
 +o(e^{-3M\theta}). \tag{5}
\]
The extinction-basin condition is nonvacuous: every initial condition \(0<u(0)<M\), \(v(0)>0\) satisfies it. The coefficient in (4) changes sign exactly when \(A\) crosses \(1+M\); equality is excluded because the displayed nonzero resonance then cancels.

## Assumptions and scope

The original model of Liu–Li–He (2023), also studied by Arancibia-Ibarra–Flores–Pettet–van Heijster (2019), has prey density \(x\), predator density \(y\), positive scaling constants \(K,n,r\), and positive Allee threshold \(m<K\). Its dimensionless populations are \(u=x/K\), \(v=y/(nK)\); the nondimensional *original* physical time is \(\theta=rKt\), where \(t\) denotes biological time. The parameters \(A=e/K\), \(S=s/(rK)\), \(Q=nq/(rK)\), and \(M=m/K\) match the source's scaled parameters. Equation (1) is the resulting physical-time system on the positive quadrant. In contrast, the source's polynomial system (1.5) uses the singularly accelerated clock \(d\tau/d\theta=[u(u+A)]^{-1}\). Equations (2)–(5) are **not** statements about that accelerated clock.

All quantifiers in this theorem refer to \(A>0\), \(0<M<1\), \(A\ne1+M\), \(S=M\), \(Q=A(1+M)/2\), and any strictly positive trajectory converging to the origin. There is no claim that trajectories outside the extinction basin converge to the origin or that other equilibria and cycles cannot coexist.

## Proof

**1. Positive solutions and an open extinction basin.** The positive quadrant is forward invariant for (1) as long as the solution is defined. For \(u>1\), its derivative is negative; hence \(u\) is bounded above on every forward solution. The inequality \(v'\le Mv\) ensures there is no finite-time positive-quadrant blow-up, and local smoothness for \(u>0\) precludes a finite-time loss of positivity. Suppose \(0<u(0)<M\). Then \(u\) decreases, and throughout \(0<u\le u(0)\) one has
\[
 \frac{u'}u\le(1-u)(u-M)
 \le-(1-u(0))(M-u(0))<0.
\]
Thus \(u\to0\) exponentially. For every \(\varepsilon>0\), eventually \(u<\varepsilon\); from \(v'\le Mv(1-v/\varepsilon)\), logistic comparison yields \(\limsup v\le\varepsilon\). Consequently \(v\to0\). The same subsequent analysis applies to any other strictly positive trajectory that is known to converge to the origin.

**2. Ratio and the exact cancellation.** Define \(R=v/u\) and \(\eta=R-2\), and write \(F\) and \(h\) for the analytic functions
\[
 F(u)=\frac{u^2(1+M-A-u)}{u+A},\qquad
 h(u)=\frac{Q u}{u+A}.
\]
Direct substitution of \(S=M\) and \(Q=A(1+M)/2\) into (1) gives the **exact** differential equations
\[
 \boxed{\begin{aligned}
 u'&=u[-M+F(u)-h(u)\eta],\
 \eta'&=(2+\eta)[-M\eta-F(u)+h(u)\eta].
 \end{aligned}} \tag{6}
\]
Before using (6), ratio convergence must be justified without presupposing any trajectory rate. For an arbitrary positive extinction trajectory, \(R'/R=M(1-R)-u'/u\) and \(u'/u\to-M\), since \(u,v\to0\). Hence
\[
 \frac{R'}R=M(2-R)+o(1).
\]
Comparison against the autonomous logistic equations with constant perturbations \(\pm\varepsilon\) proves \(R\to2\), so \(\eta\to0\). Equation (6) extends smoothly near \((u,\eta)=(0,0)\). Its Jacobian is \(\operatorname{diag}(-M,-2M)\), the natural \(1{:}2\) stable-node resonance. Expanding its nonlinear terms yields
\[
 F(u)=\delta u^2+O(u^3),\quad h(u)=O(u),\quad
 \eta'+2M\eta=-2\delta u^2+O(u^3+u|\eta|+\eta^2). \tag{7}
\]
The quadratic prey drift vanishes exactly because of the chosen predation parameter; the nonzero quadratic *forcing* in (7) is the resonant obstruction.

**3. Positive exponential prey amplitude.** Since \(u'/u\to-M\), for every sufficiently small \(\varepsilon>0\) one has \(u=O(e^{-(M-\varepsilon)\theta})\). From (6),
\[
 \frac{d}{d\theta}\log(u e^{M\theta})=F(u)-h(u)\eta.
\]
Its right-hand side is absolutely integrable, because \(u\) decays exponentially and \(\eta\to0\) is bounded. Thus the logarithm converges to a finite real number and
\[
 L:=\lim_{\theta\to\infty}e^{M\theta}u(\theta)\in(0,\infty). \tag{8}
\]
This also gives \(u=L e^{-M\theta}(1+o(1))\).

**4. Resonant ratio asymptotics and finite phase.** Use (7) and (8). Since \(\eta\to0\), variation of constants, absorbing the \(O(u|\eta|+\eta^2)\) terms into a coefficient of arbitrarily small size, gives
\[
 \eta=O(e^{-(2M-\varepsilon)\theta})
 \quad\text{for any fixed }0<\varepsilon<M/2. \tag{9}
\]
Indeed its inhomogeneity is \(O(e^{-2M\theta})\) and the perturbed linear contraction is at least \(2M-\varepsilon\). Now write (7) more precisely as
\[
 (e^{2M\theta}\eta)'=-2\delta e^{2M\theta}u^2+\mathcal E(\theta),
 \quad \mathcal E\in L^1([\theta_0,\infty)), \tag{10}
\]
because (8), (9) make \(e^{2M\theta}(u^3+u|\eta|+\eta^2)\) integrable. In particular, dividing the integral of (10) by \(\theta\) shows
\[
 \lim_{\theta\to\infty}\frac{e^{2M\theta}\eta}{\theta}=-2\delta L^2. \tag{11}
\]
To strengthen the remainder to a finite constant, integrate the logarithmic derivative from step 3 backwards from infinity. The estimates \(F(u)=O(e^{-2M\theta})\) and \(h(u)\eta=O(e^{-(3M-\varepsilon)\theta})\) imply
\[
 u=L e^{-M\theta}(1+O(e^{-2M\theta})),
 \qquad e^{2M\theta}u^2-L^2=O(e^{-2M\theta}). \tag{12}
\]
Subtracting the constant \(-2\delta L^2\) from (10) therefore leaves an absolutely integrable derivative. Hence
\[
 H:=\lim_{\theta\to\infty}
 \big[e^{2M\theta}\eta+2\delta L^2\theta\big]
 \quad\text{exists in }\mathbb R.
\]
This proves (3). Combining (3) with (8) gives the nonzero, initial-condition-independent normalized limit (4).

**5. Sharp prey and predator coefficients.** The exact first equation in (6) and (3) give
\[
 \frac{d}{d\theta}\log(u e^{M\theta})
 =\delta L^2e^{-2M\theta}+o(e^{-2M\theta}).
\]
Integrating from \(\theta\) to infinity and using the definition of \(L\) gives
\[
 \log\frac{u e^{M\theta}}L
 =-\frac{\delta L^2}{2M}e^{-2M\theta}+o(e^{-2M\theta}).
\]
Exponentiating establishes (2). Finally multiply (2) by (3) to obtain (5). No finite-time computation was substituted for an infinite-time argument.

**6. Sharp sign realizations.** Taking \(M=S=1/4\), \(A=1/2\) requires \(Q=5/16\) and yields \(\delta=3/2\); the limit in (4) is \(-3\). Taking the same \(M=S=1/4\), \(A=2\) requires \(Q=5/4\) and yields \(\delta=-3/8\), so the limit is \(3/4\). In both cases every initial datum \(0<u(0)<1/4\), \(v(0)>0\) lies in the open extinction basin from step 1. The exact symbolic checker corroborates these identities but is not the asymptotic proof.

## Verification

Run `python verify_resonance.py` with Python 3 and SymPy. Its successful output is `CHECK_OK: exact vector field, Jacobian, resonant forcing, and asymptotic coefficient balances`. It verifies the exact transformations in (6), the \(-2\delta\) resonant forcing coefficient, the \(1{:}2\) eigenvalues, and coefficient balances in (2)–(5). The comparison estimates, the existence of the limits \(L,H\), and convergence for positive extinction trajectories are established in the proof above, not by finite numerical integration.

## Relationship to prior work

Liu–Li–He (2023) analyze bifurcations of the same Holling–Tanner system in the singularly desingularized time variable; their equation (1.5) is the polynomial reparametrization of (1). Arancibia-Ibarra–Flores–Pettet–van Heijster (2019), especially their blow-up analysis of the nonhyperbolic origin, already establish that the origin attracts and give the first-order eigendirections. Their printed eigenvector implies the first-order ratio-curvature cancellation at \(Q=A(1+M)/(1+M/S)\); this **is not claimed as new**. Their eigenvalues also expose the possibility of \(1{:}2\) resonance when \(S=M\). The present theorem instead establishes the ensuing nonzero quadratic resonant forcing and the exact physical-time \(\theta e^{-3M\theta}\) predator correction, including a finite renormalized ratio phase. A third 2023 paper by Huang–Jia–Li treats a modified Holling–Tanner model whose predator carrying capacity has an added positive constant; it therefore does not have the same extinction ratio equation.

Generic resonant-node normal-form theory predicts that resonant powers can carry time-polynomial factors. The scientific contribution asserted here is the **exact parameter location, model-specific coefficient, physical-time expansion and extinction-basin quantifier**, not a new generic theory of resonances. These literature comparisons do not prove exhaustive priority.

## Limitations

The result is for the specified codimension-two cancellation/resonance surface, not arbitrary predation rates or growth ratios. The nondegenerate assumption \(A\ne1+M\) is necessary for a nonzero leading logarithmic defect; at equality further-order analysis would be required. Coefficients \(L\) and \(H\) depend on the initial condition, and no closed expressions for their values are asserted. The theorem gives no statement about coexistence attractors, other possible limit cycles, basins outside the stated open subset, noise, discrete populations, or spatial effects. The physical-time normalization \(\theta=rKt\) is essential. 

## References

1. Y. Liu, Z. Li, M. He, *Bifurcation analysis in a Holling-Tanner predator-prey model with strong Allee effect*, Mathematical Biosciences and Engineering **20** (2023), 8632–8665, DOI: `10.3934/mbe.2023379`, first public online 2023-03-06; lawful open full text: https://www.aimspress.com/aimspress-data/mbe/2023/5/PDF/mbe-20-05-379.pdf.
2. C. Arancibia-Ibarra, J. D. Flores, G. Pettet, P. van Heijster, *A Holling–Tanner predator-prey model with strong Allee effect*, International Journal of Bifurcation and Chaos **29** (2019), 1930032, DOI: `10.1142/S0218127419300325`; open preprint `arXiv:1809.05854`, https://arxiv.org/pdf/1809.05854.
3. K. Huang, X. Jia, C. Li, *Analysis of modified Holling-Tanner model with strong Allee effect*, Mathematical Biosciences and Engineering **20** (2023), 15524–15543, DOI: `10.3934/mbe.2023693`, https://www.aimspress.com/aimspress-data/mbe/2023/8/PDF/mbe-20-08-693.pdf.
