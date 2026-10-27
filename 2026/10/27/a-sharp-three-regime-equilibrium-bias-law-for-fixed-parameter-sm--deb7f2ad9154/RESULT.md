# A sharp three-regime equilibrium bias law for fixed-parameter smoothed clipping with error feedback

## Finding

For deterministic three-client smooth-clipping error feedback (SClip-EF), a fixed clipping amplitude can produce an attracting stationary point different from the true minimizer, even when all local objectives are equally curved, smooth and strongly convex. On the natural family with centers \((-a,-a,2a)\), the unique equilibrium has a sharp phase boundary at \(\varphi=2a\). Its displacement has a nonzero limiting value below the boundary, a cube-root transition at the boundary, and a square-root decay above it. In contrast, no deterministic two-client equal-curvature quadratic instance has biased equilibria.

**Exact theorem.** Fix \(a,\varphi,\epsilon,\eta>0\) and \(0<\beta<1\). Set \(c_1=c_2=-a\), \(c_3=2a\), and \(f_i(x)=\frac12(x-c_i)^2\); their average has unique minimizer \(x^*=0\). Define \(\Psi(y)=\varphi y/\sqrt{y^2+\epsilon}\) and the constant-parameter recurrence
\[
 m_i^{k+1}=\beta m_i^k+(1-\beta)\Psi(x^k-c_i-m_i^k),\qquad
 x^{k+1}=x^k-\frac{\eta}{3}\sum_{i=1}^3m_i^{k+1}.
\]
For every admissible parameter choice there is exactly one joint equilibrium. It has \((m_1,m_2,m_3)=(p,p,-2p)\) with \(0<p<\min\{a,\varphi/2\}\), where \(p\) is the unique solution of
\[
 3a=3p+\sqrt{\epsilon}\,p\left(\frac1{\sqrt{\varphi^2-p^2}}+\frac2{\sqrt{\varphi^2-4p^2}}\right),\qquad
 x_\epsilon=p-a+\frac{\sqrt{\epsilon}\,p}{\sqrt{\varphi^2-p^2}}.
\]
In particular \(-a<x_\epsilon<0\), independently of \(\beta\) and \(\eta\). For fixed \(a,\varphi\), as \(\epsilon\downarrow0\), the following exhaustive asymptotic regimes hold:
\[
 x_\epsilon=\begin{cases}
 \varphi/2-a+\sqrt{\epsilon/3}+O(\epsilon),&0<\varphi<2a,\\
 -(\varphi\epsilon/36)^{1/3}+o(\epsilon^{1/3}),&\varphi=2a,\\
 -\dfrac{2a\sqrt\epsilon}{3}\left(\dfrac1{\sqrt{\varphi^2-4a^2}}-\dfrac1{\sqrt{\varphi^2-a^2}}\right)+O(\epsilon),&\varphi>2a.
\end{cases}
\]
In the first case, moreover,
\[
 p=\frac{\varphi}{2}-\frac{\varphi\epsilon}{36(a-\varphi/2)^2}+o(\epsilon).
\]
If, additionally, \((1-\beta)\varphi/\sqrt\epsilon<\beta\), then the equilibrium is locally asymptotically stable for every sufficiently small \(\eta>0\). Thus stable biased equilibria exist for each positive \(\epsilon\), with a suitable fixed \(\beta\) and step size.

## Assumptions and scope

All controls here are deterministic and scalar; the three local objectives are strictly convex quadratics with unit Hessian. The clipping parameters \(\varphi\) and \(\epsilon\), feedback weight \(\beta\), and step size \(\eta\) are constant in iteration time. Local stability means asymptotic attraction for sufficiently close starting values of the full state \((x,m_1,m_2,m_3)\), not global convergence from arbitrary initialization. The asymptotic statements concern the location of equilibria as \(\epsilon\downarrow0\); they do not assume a common value of \(\beta\) stable at every \(\epsilon\).

## Proof

**1. Inverting the fixed-point feedback.** Since \(0<\beta<1\), stationarity of the memories gives \(m_i=\Psi(g_i-m_i)\) with \(g_i=x-c_i\). The range of \(\Psi\) is exactly \((-\varphi,\varphi)\). Solving for its argument yields the strictly increasing odd bijection
\[
 g=H(m):=m+\frac{\sqrt\epsilon\,m}{\sqrt{\varphi^2-m^2}},\quad |m|<\varphi.
\]
Its derivative is \(H'(m)=1+\sqrt\epsilon\,\varphi^2/(\varphi^2-m^2)^{3/2}>0\), and its second derivative is \(H''(m)=3\sqrt\epsilon\,\varphi^2m/(\varphi^2-m^2)^{5/2}\). Hence its inverse \(h=H^{-1}\) is strictly increasing and odd, and strictly concave on positive inputs. The primal stationarity condition is \(\sum_i h(x-c_i)=0\). This sum is strictly increasing from \(-3\varphi\) to \(3\varphi\), so it has exactly one zero and thus one joint equilibrium.

**2. Sign, reduction and two-client minimum.** For the three centers, \(F(x)=2h(x+a)+h(x-2a)\). At \(x=-a\), \(F(-a)=h(-3a)<0\); at \(x=0\), strict concavity and \(h(0)=0\) give \(F(0)=2h(a)-h(2a)>0\). Thus \(-a<x_\epsilon<0\). The first two memories coincide, and zero sum forces the third to be \(-2p\). Inverting the feedback twice and subtracting \(x+a=H(p)\) from \(x-2a=H(-2p)\) gives the stated scalar equation and reconstruction. Its right side is strictly increasing on \((0,\min(a,\varphi/2))\), starts at zero and exceeds \(3a\) at the right boundary (diverging when \(\varphi\le2a\)), proving existence and uniqueness of \(p\). For any one or two equal-curvature scalar quadratic clients, oddness of \(h\) makes the arithmetic mean of the centers solve the stationary sum, and strict monotonicity makes it unique. Therefore three is the minimal client count for this kind of deterministic bias.

**3. Three singular limits.** For \(0<\varphi<2a\), the scalar equation forces \(p\to\varphi/2\). Put \(d=a-\varphi/2>0\) and \(p=\varphi/2-\delta\). The second square-root term gives \(3d\sim\sqrt\epsilon\sqrt\varphi/(2\sqrt\delta)\), and hence \(\delta=\varphi\epsilon/(36d^2)+o(\epsilon)\). Smooth expansion of the first square-root term then yields \(x_\epsilon=\varphi/2-a+\sqrt{\epsilon/3}+O(\epsilon)\). At \(\varphi=2a\), writing \(p=a-\delta\) gives \(3\delta\sim\sqrt{a\epsilon/(2\delta)}\) and \(\delta^3\sim a\epsilon/18=\varphi\epsilon/36\). The first square-root contribution to \(x_\epsilon\) is only \(O(\sqrt\epsilon)\), proving the cube-root law. For \(\varphi>2a\), the scalar equation is smooth near \((p,\sqrt\epsilon)=(a,0)\); implicit expansion gives
\[
 p=a-\frac{a\sqrt\epsilon}{3}\left(\frac1{\sqrt{\varphi^2-a^2}}+\frac2{\sqrt{\varphi^2-4a^2}}\right)+O(\epsilon).
\]
Substitution in \(x_\epsilon=H(p)-a\) gives the final formula.

**4. Local attraction.** At the equilibrium put \(d_i=\Psi'(x-c_i-m_i)=\varphi\epsilon/((x-c_i-m_i)^2+\epsilon)^{3/2}\), \(q_i=(1-\beta)d_i\), and \(\alpha_i=\beta-q_i\). The linearized state map has memory rows \(\delta m_i^+=q_i\delta x+\alpha_i\delta m_i\) and top row \(\delta x^+=\delta x-(\eta/3)\sum_i\delta m_i^+\). The stated condition implies \(0<\alpha_i<\beta<1\), because \(d_i\le\varphi/\sqrt\epsilon\). At \(\eta=0\) the four eigenvalues are the simple eigenvalue \(1\) and the three \(\alpha_i\). The eigenvalue issuing from \(1\) has derivative at zero
\[
 \left.\frac{d\lambda}{d\eta}\right|_{\eta=0}=-\frac13\sum_{i=1}^3\frac{q_i}{1-\alpha_i}<0.
\]
Therefore for all sufficiently small positive \(\eta\) every eigenvalue is strictly inside the unit disk. The discrete linearization theorem gives local asymptotic attraction of the nonlinear equilibrium.

## Verification

Execute `python3 verify.py` using only the Python standard library. It solves the monotone scalar equation by bisection, tests joint update residuals over a grid of positive parameters and several feedback/step values, checks asymptotic coefficients in all three regimes, tests the two-client symmetry, and checks positive-memory eigenvalue separation at examples satisfying the stability hypothesis. Its successful output is `VERIFY_OK 1011`. The infinitely many parameter cases and the local stability conclusion follow from the analytical proof, not from finite tests.

## Relationship to prior work

Yu, Jakovetić, and Kar introduced the smoothed clipping operator and SClip-EF feedback equations; their 2023 preprint supplies the algorithm, while the accessible later version gives explicit formulas (5)–(7) and a convergence theorem using **time-dependent** parameter sequences (Theorem 1, Corollary 1). Those rate guarantees neither assert nor preclude the distinct fixed-parameter equilibrium and its three-regime singular behavior. Khirirat and collaborators introduced Clip21 with hard clipping and *additive* residual memories; its stationary memory satisfies an unmodified gradient equation, rather than the fixed smooth feedback equation studied here. Koloskova, Hendrikx, and Stich analyze clipped SGD without this distributed feedback memory. The phenomenon of gradient-clipping bias is previously known and is not claimed as new; the present contribution is the exact bias and transition law for this particular smooth residual-feedback dynamics.

## Limitations

This is not a stochastic-noise theorem and does not contradict decaying-parameter convergence results. The local stability proof applies under a sufficient parameter condition and small step size, not to arbitrary feedback gains. The zero-smoothing limit describes the location of equilibria; no common stability guarantee is asserted along that limit for fixed \(\beta\). The result does not extend automatically to general client curvatures, higher-dimensional objectives, arbitrary topologies or hard-clipping error feedback. Originality is assessed against identified sources and is not an independent priority determination.

## References

1. S. Yu, D. Jakovetić, S. Kar, *Smoothed Gradient Clipping and Error Feedback for Distributed Optimization under Heavy-Tailed Noise*, arXiv:2310.16920v1 (first publicly submitted 2023-10-25); revised as *Smoothed Gradient Clipping and Error Feedback for Decentralized Optimization under Symmetric Heavy-Tailed Noise*, arXiv:2310.16920v3, 2024. https://arxiv.org/abs/2310.16920
2. S. Khirirat, E. Gorbunov, S. Horváth, R. Islamov, F. Karray, P. Richtárik, *Clip21: Error Feedback for Gradient Clipping*, arXiv:2305.18929, 2023. https://arxiv.org/abs/2305.18929
3. A. Koloskova, H. Hendrikx, S. U. Stich, *Revisiting Gradient Clipping: Stochastic Bias and Tight Convergence Guarantees*, arXiv:2305.01588, 2023. https://arxiv.org/abs/2305.01588
