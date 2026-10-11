# Critical \(t^{-1}\) predator extinction with an exact gestation-delay factor

## Finding

For the positive-parameter three-species food-chain delay equations (1) below, **every solution with nonnegative continuous histories and strictly positive population values at time zero** satisfies
\[
\lim_{t\to\infty}x_2(t)=\lim_{t\to\infty}x_3(t)=0
\qquad\text{whenever }\beta\le d,
\]
for **all finite nonnegative gestation delays** \(\tau_1,\tau_2\). When \(\beta<d\), the two predator populations decay exponentially (with rates possibly depending on the delays). At the nonhyperbolic boundary \(\beta=d\), assume additionally
\[
r>b+\frac{\alpha}{m}.
\]
Then the prey converges to \(X=(r-b)/a>0\), the top predator still decays exponentially, and the intermediate predator has the **exact positive asymptotic constant**
\[
\boxed{\lim_{t\to\infty}t\,x_2(t)
=\frac{X(1+d\tau_1)}{d m}
=\frac{(r-b)(1+d\tau_1)}{a d m}.}
\tag{A}
\]
In particular, this critical decay is algebraic, not exponential; its leading constant depends linearly on the intermediate predator's gestation delay \(\tau_1\) but not on the fear coefficient \(k\), predation coefficient \(\alpha\), or top-predator delay \(\tau_2\). The threshold \(\beta=d\) cannot be enlarged as a parameter-uniform predator-extinction condition: a strictly positive intermediate-predator equilibrium is locally attracting for an explicit admissible parameter choice with \(\beta>d\).

## Assumptions and scope

Write \(x=x_1\) for prey, \(y=x_2\) for intermediate predator, and \(z=x_3\) for top predator. The complete model is
\[
\begin{aligned}
\dot x(t)&=\frac{r x(t)}{1+k y(t)}-b x(t)-a x(t)^2-\frac{\alpha x(t)y(t)}{x(t)+m y(t)},\\
\dot y(t)&=\frac{\beta x(t-\tau_1)y(t-\tau_1)}{x(t-\tau_1)+m y(t-\tau_1)}-d y(t)-\frac{\theta y(t)z(t)}{v+p y(t)+q z(t)},\\
\dot z(t)&=\frac{\eta y(t-\tau_2)z(t-\tau_2)}{v+p y(t-\tau_2)+q z(t-\tau_2)}-e z(t).
\end{aligned}\tag{1}
\]
All fourteen parameters \(r,k,b,a,\alpha,m,\beta,d,\theta,v,p,q,\eta,e\) in (1) are strictly positive, and \(\tau_1,\tau_2\in[0,\infty)\) are fixed and finite. Let \(\tau=\max\{\tau_1,\tau_2\}\). Initial data are continuous and nonnegative on \([-\tau,0]\), with \(x(0),y(0),z(0)>0\); fractions are interpreted in their continuous extension along positive solutions. The exact limit (A) requires \(\beta=d\) and \(r>b+\alpha/m\), whereas extinction of \(y,z\) for \(\beta\le d\) requires no extra inequality involving \(r\) or the fear parameters. No assertion is made about prey convergence when the extra inequality fails, or about global survival when \(\beta>d\).

## Proof

**1. Positivity, boundedness, and global existence.** The prey equation is proportional to \(x\), with locally bounded per-capita rate along positive trajectories. Nonnegative delayed recruitment and the variation-of-constants formula give \(y,z>0\) for forward time when their values at zero are positive. The first equation implies
\[
\dot x\le (r-b)x-a x^2.
\]
Consequently the prey and its entire prescribed history are bounded by a finite constant \(M_x\). For any positive \(u,w\), \(uw/(u+mw)\le u/m\); hence
\[
\dot y\le (\beta/m)M_x-dy.
\]
Thus the intermediate predator and its prescribed history are bounded by \(M_y\). Similarly \(uw/(v+pu+qw)\le u/q\), so
\[
\dot z\le (\eta/q)M_y-ez.
\]
All three variables are bounded, with no finite-time singularity, establishing forward global existence. The bounds are independent of the size of either delay except for the finite initial-history suprema.

**2. Strict subcritical extinction.** For \(\beta<d\), the intermediate equation satisfies \(\dot y(t)\le\beta y(t-\tau_1)-d y(t)\). Choose \(\lambda>0\) small enough that
\[
d-\lambda>\beta e^{\lambda\tau_1}.
\]
An exponential positive supersolution of this scalar delay inequality bounds \(y(t)\) by \(C e^{-\lambda t}\). Eventually \((\eta/v)y(t-\tau_2)<e/2\), and the top-predator equation satisfies \(\dot z\le(e/2)z(t-\tau_2)-e z\). A second exponential supersolution gives \(z(t)=O(e^{-\lambda_3t})\) for some \(\lambda_3>0\).

**3. The critical Lyapunov–Krasovskii mass.** Suppose \(\beta=d\). Introduce
\[
P(t)=y(t)+d\int_{t-\tau_1}^{t}y(s)\,ds.
\tag{2}
\]
Direct differentiation, using the entire nonlinear recruitment term, gives the exact identity
\[
\boxed{
P'(t)=-\frac{d m\,y(t-\tau_1)^2}{x(t-\tau_1)+m y(t-\tau_1)}
-\frac{\theta y(t)z(t)}{v+p y(t)+qz(t)}\le0.}
\tag{3}
\]
Thus \(0<P(t)\le P(0)\) and \(y(t)\le P(0)\). Since the first denominator is bounded above by \(M_x+mM_y\), integrating (3) gives
\[
\int_0^\infty y(t-\tau_1)^2\,dt<\infty.
\]
Every \(\dot y(t)\) is bounded by Step 1, so \(y\) is uniformly continuous. Uniform continuity together with square-integrability implies \(y(t)\to0\), including when \(\tau_1=0\). The bounded \(z\)-equation then has, for sufficiently large \(t\),
\[
\dot z(t)\le c\,z(t-\tau_2)-e z(t),\qquad 0<c<e,
\]
because \(\eta y(t-\tau_2)/(v+p y(t-\tau_2)+q z(t-\tau_2))\le(\eta/v)y(t-\tau_2)\to0\). Comparison with an exponential supersolution again proves \(z(t)=O(e^{-\lambda_3t})\). This proves extinction at equality with no assumed convergence of the prey.

**4. Prey convergence in the rate regime.** Now impose \(r>b+\alpha/m\). The inequality
\[
\dot x\ge x\left(\frac r{1+k y}-b-\frac{\alpha}{m}-a x\right)
\]
and \(y(t)\to0\) imply, by scalar logistic comparison, that \(\liminf x(t)\ge(r-b-\alpha/m)/a>0\). Therefore \(y(t)/(x(t)+m y(t))\to0\), and the exact prey equation is
\[
\dot x=x\bigl((r-b)-a x+o(1)\bigr).
\]
Upper and lower asymptotic logistic comparisons give \(x(t)\to X=(r-b)/a\).

**5. Exact coefficient at the zero spectral root.** Write \(h(t)=-P'(t)\ge0\), so that, by (3),
\[
\dot y(t)=d\,[y(t-\tau_1)-y(t)]-h(t).
\tag{4}
\]
Boundedness of \(z\) gives \(\dot y(t)\ge-Dy(t)\) for some fixed \(D>0\). Hence \(y(t-\tau_1)\le e^{D\tau_1}y(t)\le e^{D\tau_1}P(t)\) for all sufficiently large \(t\). Since \(x(t)\to X>0\), (3) supplies constants \(C,T>0\) such that
\[
0\le h(t)\le C\bigl(P(t)^2+z(t)P(t)\bigr),\qquad t\ge T.
\tag{5}
\]
In particular, \(P(t)\to0\) and \(|(\log P)'|=h/P\to0\). As \(z\) is integrable, (5) also yields \((1/P)'\le C+Cz/P\). Gronwall's inequality applied to \(1/P\) implies \(1/P(t)=O(1+t)\), so
\[
P(t)\ge\frac{c_0}{1+t},\qquad \frac{z(t)}{P(t)}\to0.
\tag{6}
\]
For each fixed real \(s\), it follows from \((\log P)'\to0\) that \(P(t+s)/P(t)\to1\), locally uniformly in \(s\).

To identify the size of \(y\) relative to the critical mass, fix any sequence \(t_n\to\infty\) and set \(Y_n(s)=y(t_n+s)/P(t_n)\). The inequality \(y\le P\) and the local slow variation of \(P\) bound \(Y_n\) on every compact real interval. Equation (4) and (5) make these normalized functions equicontinuous. Arzelà–Ascoli yields a subsequence converging locally uniformly to a bounded entire solution \(Y\) of
\[
Y'(s)=d\,[Y(s-\tau_1)-Y(s)],\qquad
Y(s)+d\int_{s-\tau_1}^{s}Y(u)\,du=1.
\tag{7}
\]
Every bounded entire solution of the homogeneous equation in (7) is constant. One direct justification regards \(Y\) as a tempered distribution and Fourier-transforms the equation: its Fourier transform is annihilated by \(i\xi+d(1-e^{-i\xi\tau_1})\), which has no real zero except \(\xi=0\) (its real part vanishes only at integer phase multiples, when its imaginary part is \(\xi\)). Thus the Fourier transform is supported at zero; \(Y\) is a polynomial, and boundedness forces it to be constant. The second equation in (7) fixes this constant to \((1+d\tau_1)^{-1}\). Since every subsequential limit has this value,
\[
\frac{y(t)}{P(t)}\longrightarrow\frac1{1+d\tau_1},\qquad
\frac{y(t-\tau_1)}{P(t)}\longrightarrow\frac1{1+d\tau_1}.
\tag{8}
\]
Substitute (8), \(x(t-\tau_1)\to X\), and (6) in the exact identity (3):
\[
\lim_{t\to\infty}\frac{P'(t)}{P(t)^2}
=-\frac{d m}{X(1+d\tau_1)^2}.
\]
Integration of \((1/P)'=-P'/P^2\) now gives \(P(t)\sim X(1+d\tau_1)^2/(d m t)\); combining with (8) proves (A) for every allowed strictly positive history. No finite simulation has been used to infer this infinite-time limit.

**6. Sharpness of the universal threshold.** Take zero delays and the positive constants
\[
(r,k,b,a,\alpha,m,\beta,d,\theta,v,p,q,\eta,e)
=\left(\frac92,1,1,1,\frac12,1,2,1,1,1,1,1,1,1\right).
\]
Here \(\beta>d\), and \((x,y,z)=(1,1,0)\) is an equilibrium. Its Jacobian is
\[
J=\begin{pmatrix}-7/8&-5/4&0\\1/2&-1/2&-1/2\\0&0&-1/2\end{pmatrix}.
\]
The upper-left block has trace \(-11/8\) and determinant \(17/16\); the final eigenvalue is \(-1/2\). Hence this equilibrium is locally asymptotically stable, including for sufficiently small strictly positive top-predator initial density. Its intermediate predator remains positive in the limit. Therefore the inequality \(\beta\le d\) is a sharp *parameter-uniform sufficient boundary* for predator extinction, though the theorem does not classify every choice with \(\beta>d\).

## Verification

The accompanying `CHECK.py` recomputes (3), the quadratic delay-normal-form coefficient, and the rational equilibrium/Jacobian in Step 6 with exact SymPy arithmetic. Its expected result is `CHECK_OK`. As a supplementary numerical sanity check (not a proof), forward Euler at step \(0.02\) with \(r=4,b=1,a=1,\alpha=0.5,k=0.3,m=1,d=\beta=2,\theta=0.5,v=p=q=\eta=e=1,\tau_1=1.3,\tau_2=0.7\) yielded \(t y(t)\approx5.33747\) at \(t=2000\), approaching the analytically predicted limit \(5.4\). The prescribed histories for that check were constant \(x=3,y=0.5,z=0.2\) on the full delay interval. The limit proof is Steps 1–5, not this finite experiment.

## Relationship to prior work

Wang–Shao–Chai [1] introduce precisely (1), prove positivity/boundedness, characterize equilibria, and analyze local stability and delay-induced Hopf bifurcations. Their Theorem 5.2 supplies the strict inequality \(\beta<d\) for local stability of the predator-free axial equilibrium, while its Appendix (A.1) implies a zero characteristic root at \(\beta=d\); that source does not establish global critical extinction or the exact tail (A). The elementary equilibrium existence conditions for \(\beta>d\) are already in [1]; our sharpness example uses them without asserting their novelty.

Tian–Xu [2] prove predator-extinction stability in a distinct, nondelayed Holling-II *stage-structured* system; their theorem neither covers the gestation-delay recruitment in (1) nor determines the critical \(t^{-1}\) constant. Shao–Kong [3] examine a two-species Beddington–DeAngelis model with delayed fear and gestation and global coexistence stability, but not this three-level ratio-dependent chain or its nonhyperbolic predator-free rate. Shao [4] studies global *coexistence* stability in a different two-species delayed Holling-II fear model. Generic scalar delay comparison and center-manifold theory motivate the method but do not by themselves provide the model-specific global extinction proof and exact delayed constant.

## Limitations

The claimed limit is for a deterministic autonomous delay system with constant finite delays and strictly positive initial values at time zero. The stronger prey-growth inequality is needed for the **exact coefficient** but not for predator extinction. The result does not establish global stability of positive equilibria when \(\beta>d\), higher-order corrections to the critical asymptotic, or behavior under stochastic forcing, spatial dispersal, time-varying delay, or variable coefficients. It does not say the prey survives for every parameter choice when \(\beta=d\). The top predator's exponential rate and transient dynamics can depend on both delays.

## References

[1] Y. Wang, Y. Shao, C. Chai, “Dynamics of a predator-prey model with fear effects and gestation delays,” *AIMS Mathematics* **8** (2023), 7535–7559, first published 2023-01-17, DOI: 10.3934/math.2023378. https://www.aimspress.com/aimspress-data/math/2023/3/PDF/math-08-03-378.pdf

[2] X. Tian, R. Xu, “Global dynamics of a predator-prey system with Holling type II functional response,” *Nonlinear Analysis: Modelling and Control* **16** (2011), 242–253, DOI: 10.15388/NA.16.2.14109. https://www.journals.vu.lt/nonlinear-analysis/article/download/14109/13018/20895

[3] Y. Shao, W. Kong, “A Predator–Prey Model with Beddington–DeAngelis Functional Response and Multiple Delays in Deterministic and Stochastic Environments,” *Mathematics* **10** (2022), 3378, DOI: 10.3390/math10183378. https://www.mdpi.com/2227-7390/10/18/3378

[4] Y. Shao, “Global stability of a delayed predator–prey system with fear and Holling-type II functional response in deterministic and stochastic environments,” *Mathematics and Computers in Simulation* **200** (2022), 65–77, DOI: 10.1016/j.matcom.2022.04.013.
