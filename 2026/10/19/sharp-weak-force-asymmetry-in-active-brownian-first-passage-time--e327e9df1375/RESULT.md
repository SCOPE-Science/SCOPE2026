# Sharp weak-force asymmetry in active Brownian first-passage times

## Finding

For a planar active Brownian particle projected onto a symmetric, finite first-passage interval, the leading weak-propulsion response of the difference between uphill and downhill *conditional* mean exit times has an exact finite-diffusivity formula. In the fast-angular-relaxation regime, it is one order smaller than the previously established bound allows, with an explicit coefficient and an exponentially accurate two-term asymptotic.

Let \(\varepsilon>0\). For \(U,F\in\mathbb R\), consider
\[
 dX_t=(U\cos\Phi_t+\varepsilon F)\,dt+\sqrt{2\varepsilon}\,dW_t,
 \qquad d\Phi_t=\sqrt{2}\,dB_t,
\]
with independent standard Brownian motions, initial position \(X_0=0\), and initial angle uniform on \([0,2\pi)\). Stop at \(\tau=\inf\{t\ge0:|X_t|=1/2\}\), and let \(T_+(F,U,\varepsilon)=\mathbb E[\tau\mid X_\tau=1/2]\), with \(T_-\) defined analogously for the left exit. These conditional expectations are finite.

Define the *linear-force, quadratic-activity directional susceptibility*
\[
 \mathcal C(\varepsilon)=\lim_{U\to0}\frac1{U^2}
 \left.\frac{\partial}{\partial F}
 \big(T_-(F,U,\varepsilon)-T_+(F,U,\varepsilon)\big)\right|_{F=0}.
\]
Both the derivative and the limit exist. Set \(t=1/\sqrt{\varepsilon}\), \(y=e^{-t/2}\),
\[
 A(y)=y^4+2y^3+6y^2+2y+1,
 \qquad B(y)=y^4-8y^2+1.
\]
Then, for every \(\varepsilon>0\),
\[
 \boxed{\displaystyle
 \mathcal C(\varepsilon)=
 \frac{t(1-y)A(y)}{4(1+y)(1+y^2)^2}
 +\frac{t^2 B(y)}{12(1+y)^2(1+y^2)}
 -\frac{t^3y}{8(1-y)(1+y)}.}
\]
In particular, as \(\varepsilon\downarrow0\),
\[
 \boxed{\displaystyle
 \mathcal C(\varepsilon)
 =\frac{1}{12\varepsilon}+\frac{1}{4\sqrt{\varepsilon}}
 +O\!\left(\varepsilon^{-3/2}e^{-1/(2\sqrt{\varepsilon})}\right).}
\]
Hence the infinitesimal-force uphill-minus-downhill time response has positive leading coefficient and diverges as \(1/(12\varepsilon)\) in the specified sequential limit. For each fixed \(\varepsilon>0\), analyticity implies
\[
 T_-(F,U,\varepsilon)-T_+(F,U,\varepsilon)
 =F U^2\mathcal C(\varepsilon)+O_\varepsilon(FU^4+F^3U^2)
\]
as \((F,U)\to(0,0)\). This is a *small-force, small-activity* statement; it does not assert the same sharp coefficient at fixed nonzero force.

## Assumptions and scope

The spatial boundaries are perfectly absorbing and exactly \(\pm1/2\). The angle performs free rotational Brownian motion with generator \(\partial_\phi^2\), and its initial law is uniform. Positive translational diffusivity makes the backward problem uniformly elliptic for each fixed \(\varepsilon\). The dimensionless force is \(F\), so its physical drift in this normalization is \(\varepsilon F\). The order of limits is: first the force derivative at zero, next the coefficient of quadratic propulsion as \(U\to0\), and only afterward \(\varepsilon\downarrow0\). No uniform assertion in jointly growing \(F\) or \(U/\varepsilon\) is made.

## Proof

**1. An exact zero-force response identity.** Define \(I=\int_0^\tau\cos\Phi_s\,ds\) and denote by \(\mathbb P_{F,U}\) the stopped-path law. Conditional on a path ending at \(X_\tau=\sigma/2\), \(\sigma\in\{-1,+1\}\), Girsanov's formula, first at bounded stopping times and then by exponential exit-time integrability for sufficiently small \(|F|\), gives
\[
 \frac{d\mathbb P_{F,U}}{d\mathbb P_{0,U}}
 =\exp\!\left[\frac F2\left(\frac\sigma2-U I\right)
 -\frac{\varepsilon F^2}{4}\tau\right].
\]
The exit-position term is fixed after conditioning. Differentiating the quotient defining the conditional mean yields the exact identity
\[
 \left.\partial_F T_\sigma(F,U,\varepsilon)\right|_{F=0}
 =-\frac U2\operatorname{Cov}_{0,U}
 \!\left(\tau,I\mid X_\tau=\sigma/2\right).
\]
At zero force, the transformation \((X,\Phi,W)\mapsto(-X,\Phi+\pi,-W)\) interchanges the two exit events, preserves \(\tau\), and negates \(I\). Therefore
\[
 \left.\partial_F(T_--T_+)\right|_{F=0}
 =U\operatorname{Cov}_{0,U}\!\left(\tau,I\mid X_\tau=1/2\right).
\]
All conditional exit probabilities are strictly positive. Elliptic perturbation theory on a bounded spatial interval supplies analyticity in \((F,U)\) near the origin; the angle-shift symmetry makes the time difference even in \(U\), while reflection makes it odd in \(F\).

**2. A closed resolvent hierarchy.** Write \(D=\partial_x\) on the Dirichlet interval \((-1/2,1/2)\), and introduce the positive Dirichlet inverses
\[
 K=(-D^2)^{-1},\qquad H=(1-\varepsilon D^2)^{-1}.
\]
Let \(p,m,b,c\) be the initial-state expectations of, respectively, \(\mathbf1_{\{X_\tau=1/2\}}\), \(\tau\mathbf1_{\{X_\tau=1/2\}}\), \(I\mathbf1_{\{X_\tau=1/2\}}\), and \(\tau I\mathbf1_{\{X_\tau=1/2\}}\), all initially defined for fixed \((x,\phi)\). At \(F=0\), their backward equations are
\[
 \mathscr L_U p=0,\quad \mathscr L_U m=-p,\quad
 \mathscr L_U b=-\cos\phi\,p,\quad
 \mathscr L_U c=-b-\cos\phi\,m,
\]
where \(\mathscr L_U=\varepsilon D^2+\partial_\phi^2+U\cos\phi D\). The boundary values are \(p(-1/2,\phi)=0\), \(p(1/2,\phi)=1\), and zero for the other three functions.

Retain their first angular harmonics and the angle-independent terms through first order in \(U\). Writing \(p_0(x)=x+1/2\), the required quantities are characterized *uniquely* by
\[
 \begin{aligned}
 m_0&=\varepsilon^{-1}Kp_0,&p_1&=Hp_0',\\
 b_1&=Hp_0,&m_1&=H(m_0'+p_1),\\
 c_1&=H(b_1+m_0),&
 b_{20}&=(2\varepsilon)^{-1}K(p_1+b_1'),\\
 &&c_{20}&=\varepsilon^{-1}K\!\left(b_{20}+\tfrac12m_1+\tfrac12c_1'\right).
 \end{aligned}
\]
Indeed \(b=b_1\cos\phi+U(b_{20}+b_{22}\cos2\phi)+O(U^2)\) and \(c=c_1\cos\phi+U(c_{20}+c_{22}\cos2\phi)+O(U^2)\), while \(p=p_0+Up_1\cos\phi+O(U^2)\) and \(m=m_0+Um_1\cos\phi+O(U^2)\). Uniform angle averaging at \(x=0\), using \(p_0(0)=1/2\) and \(m_0(0)=1/(16\varepsilon)\), gives
\[
 \operatorname{Cov}_{0,U}(\tau,I\mid X_\tau=1/2)
 =U\left[2c_{20}(0)-4m_0(0)b_{20}(0)\right]+O(U^3).
\]
Consequently \(\mathcal C(\varepsilon)=2c_{20}(0)-4m_0(0)b_{20}(0)\). This derivation requires only the zero-force resolvents, not a formal path-integral argument.

**3. Exact resolvent evaluation.** Put \(a=1/2\), \(h=\sqrt\varepsilon\), \(z=a/h\). With zero boundary data,
\[
 H1=1-\frac{\cosh(x/h)}{\cosh z},\qquad
 Hx=x-a\frac{\sinh(x/h)}{\sinh z}.
\]
For an even function \(f\), the centered Dirichlet Green formula is
\[
 (Kf)(0)=\int_0^a(a-x)f(x)\,dx.
\]
Applying these identities to the displayed hierarchy, and reducing the resulting elementary polynomial–hyperbolic integrals (including the odd Dirichlet part of \(c_1\)), gives, with \(t=1/h\), \(y=e^{-t/2}\),
\[
 2c_{20}(0)-4m_0(0)b_{20}(0)
 =\frac{t(1-y)A(y)}{4(1+y)(1+y^2)^2}
 +\frac{t^2B(y)}{12(1+y)^2(1+y^2)}
 -\frac{t^3y}{8(1-y)(1+y)}.
\]
The complete quadrature expressions and an independent finite-difference solution of the backward equations are reproduced in `verify.py`. There are no unevaluated infinite series or numerical extrapolations in the identity.

**4. Sharp small-diffusivity asymptotic.** As \(t\to\infty\), \(y=e^{-t/2}\to0\), and both \(A(y)\) and \(B(y)\) equal \(1+O(y)\) while every displayed denominator has a nonzero limit. Directly,
\[
 \mathcal C(\varepsilon)=\frac{t^2}{12}+\frac t4+O(t^3e^{-t/2}).
\]
Replacing \(t\) with \(1/\sqrt\varepsilon\) proves the stated expansion. In particular, the putative \(\varepsilon^{-3/2}\) term cancels in this linear-force susceptibility, and the first nonzero algebraic term is \(\varepsilon^{-1}/12\). This completes the proof.

## Verification

Running `python verify.py` reproduces the closed formula from independent one-dimensional Green-function quadratures at six positive diffusivities. It separately solves the coupled angular-harmonic finite-difference boundary problems (with three angular modes, sufficient at quadratic order in propulsion) at four parameter choices and compares the observed force-odd conditional mean difference with its small-parameter prediction. The script also compares the exact susceptibility with its two-term asymptotic at \(\varepsilon=10^{-6}\). The numerical tests pass; the analytic derivation above, not those tests, is the proof.

## Relationship to prior work

Tasinkevych, Le and Ryabov (2026, arXiv:2609.27425v1) introduce the projected active-Brownian directional first-passage problem and establish reflection reweighting and the common \(O(U^2\varepsilon^{-2})\) correction to the two conditional means. Their Section IV.1 and Appendix C bound the difference of the order-\(U^2\) coefficients by \(O(\varepsilon^{-3/2})\) but explicitly leave its leading directional term undetermined. The present result resolves the *zero-force derivative* of that difference: its scale is \(\varepsilon^{-1}\), its leading constant is \(1/12\), and its next algebraic correction is \(1/(4\sqrt\varepsilon)\).

Caraglio's active-particle parabolic-barrier work (arXiv:2410.07226) gives propagator and transition-path methods in a different force field. Baouche, Le Goff, Kurzthaler and Franosch (arXiv:2503.05401) analyze small-activity first passage to a single absorbing wall. Iyaniwura and Peng (New Journal of Physics 28, 054401, 2026) analyze splitting probabilities for chiral active particles, not the present two-exit conditional mean susceptibility. Standard elliptic perturbation and Girsanov tools are used without claiming those methods as novel.

## Limitations

The theorem does not establish the directional difference at fixed nonzero \(F\) as \(\varepsilon\downarrow0\), the global sign of the exact coefficient for every \(\varepsilon\), or a uniform joint \((F,U,\varepsilon)\) limit. The result is limited to a centered interval, isotropic initial orientation, free rotational diffusion, constant force, and two perfectly absorbing boundaries. Numerical finite differences are corroboration, not infinite-dimensional certificates. A broader general perturbative first-passage theory could also imply this specialization, although no explicit statement covering its sharp coefficient was identified in the inspected sources.

## References

1. M. Tasinkevych, X. M. Le, A. Ryabov, *Uphill and downhill first passage of an active Brownian particle: Asymmetry and exact path reweighting*, arXiv:2609.27425v1 (first posted 2026-09-23), https://arxiv.org/abs/2609.27425.
2. M. Caraglio, *Two-Dimensional Active Brownian Particles Crossing a Parabolic Barrier: Transition-Path Times, Survival Probability, and First-Passage Time*, arXiv:2410.07226, https://arxiv.org/abs/2410.07226.
3. Y. Baouche, M. Le Goff, C. Kurzthaler, T. Franosch, *First-passage-time statistics of active Brownian particles: A perturbative approach*, Phys. Rev. E 111, 054113 (2025), arXiv:2503.05401, https://arxiv.org/abs/2503.05401.
4. S. A. Iyaniwura, Z. Peng, *Splitting probabilities of confined chiral active Brownian particles*, New Journal of Physics 28, 054401 (2026), DOI:10.1088/1367-2630/ae635d.
