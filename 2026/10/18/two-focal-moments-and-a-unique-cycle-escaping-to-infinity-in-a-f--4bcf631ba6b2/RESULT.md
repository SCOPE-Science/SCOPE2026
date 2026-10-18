# Two focal moments and a unique cycle escaping to infinity in a four-jump Liénard oscillator

## Finding
For a real, compactly supported piecewise-affine function \(F\) with finitely many jump points, consider the planar Liénard field
\[
\dot x=F(x)-y,\qquad \dot y=x.
\]
Write \(R\) for Euclidean radius on a fixed upper half-plane Poincaré section located to the right of the support, and \(P_F(R)\) for its next-return radius. Define the first two nontrivial exterior focal moments by
\[
M_1(F)=\int_{\mathbb R}xF(x)\,dx,\qquad
M_3(F)=\int_{\mathbb R}xF(x)\left(F(x)^2+\frac{x^2}{2}\right)\,dx.
\]
Then every sufficiently large orbit makes one transversal rotation and
\[
P_F(R)-R=\frac{2M_1(F)}{R^2}+\frac{2M_3(F)}{R^4}+O(R^{-5}).
\]
The expansion is smooth in the reciprocal radius and uniform on a sufficiently small compact parameter family with fixed switch locations and bounded affine coefficients.

This expansion gives a complete local bifurcation in a concrete **four-jump, no-fold family**:
\[
F_\lambda(x)=
\begin{cases}
1,&-2<x<-1,\\
\frac35+\lambda,&2<x<3,\\
0,&\text{otherwise}.
\end{cases}
\]
There exist \(R_0>4\) and \(\lambda_0>0\) such that, for \(0<|\lambda|<\lambda_0\), the region intersecting the section at \(R>R_0\) contains exactly one periodic orbit for negative \(\lambda\), and none for positive \(\lambda\). The negative-parameter orbit is transversal, hyperbolic and attracting, with section radius
\[
R_\lambda\sim\sqrt{\frac{102}{125(-\lambda)}}\quad(\lambda\uparrow0),
\]
and multiplier
\[
\mu_\lambda=1-\frac{204}{25R_\lambda^5}+o(R_\lambda^{-5})\in(0,1).
\]
At \(\lambda=0\), there is no periodic orbit in the same exterior region; the outward radial displacement is
\[
P_{F_0}(R)-R=\frac{102}{25R^4}+O(R^{-5})>0.
\]
The quantifier “exactly one” refers only to the fixed exterior section \(R>R_0\), not to all possible finite-radius crossing, grazing, or sliding cycles.

## Assumptions and scope
For the moment expansion, assume \(F\) is real bounded and compactly supported, is \(C^1\) on finitely many closed subintervals, and has finitely many one-sided finite limits. Its values at the jump points do not affect transversal crossing solutions. Fix \(L>0\) with \(\operatorname{supp}F\subseteq[-L,L]\); take the transversal section
\[
\Sigma=\{(L+1,y): y>0\}.
\]
The section radius \(R=\sqrt{(L+1)^2+y^2}\) is used only for \(R\) large enough that \(y\) does not change sign on \(|x|\le L\). At discontinuities, solutions are interpreted via standard crossing continuation; there is no grazing or sliding along these switching lines at such radii. The two moments have the units fixed by the displayed oscillator normalization.

For the explicit family, \(L=3\) and all four jump points \(-2,-1,2,3\) are genuine when \(|\lambda|\) is sufficiently small. In particular there are no fold points, no switching point at the origin, and the vector field is a harmonic oscillator outside \(|x|\le3\).

## Proof
**1. Exact energy equation on each crossing segment.** Let \(H=(x^2+y^2)/2\). In any smooth sector,
\[
\dot H=xF(x).
\]
For a large-radius orbit, the upper half-turn crosses the support from right to left, and the lower half-turn crosses it from left to right. On a branch with \(y=\sigma\sqrt{2H-x^2}\), \(\sigma\in\{+1,-1\}\), monotonicity of \(x\) gives
\[
\frac{dH}{dx}=\frac{xF(x)}{F(x)-\sigma\sqrt{2H-x^2}}.
\]
Since \(F\) and its support are bounded and each denominator has magnitude bounded below by a fixed positive multiple of \(R\), the total variation of \(H\) on every support crossing is \(O(R^{-1})\). The dynamics outside the support preserves \(H\). Differentiating the right-hand side with respect to \(H\) shows a bound \(O(R^{-3})\), so replacing the evolving \(H\) in each crossing integral by the incoming value \(R^2/2\) contributes \(O(R^{-4})\) to the total energy change. All bounds are uniform in small parameter families of \(F\).

**2. Evaluation of the first two moments.** Put \(Y_R(x)=\sqrt{R^2-x^2}\). Integrating the upper leg with reversed orientation and the lower leg with forward orientation yields
\[
\begin{aligned}
\Delta H&=\int_{-L}^{L}xF(x)
\left(\frac1{Y_R(x)-F(x)}+\frac1{Y_R(x)+F(x)}\right)dx+O(R^{-4})\\
&=2\int_{-L}^{L}\frac{xF(x)Y_R(x)}{Y_R(x)^2-F(x)^2}\,dx+O(R^{-4})\\
&=\frac{2M_1(F)}R+\frac{2M_3(F)}{R^3}+O(R^{-4}).
\end{aligned}
\]
The last equality follows by uniform geometric and binomial expansion, using
\[
\frac{Y_R}{Y_R^2-F^2}=\frac1R\left[1+\frac{x^2/2+F^2}{R^2}+O(R^{-4})\right].
\]
Since \(\Delta H=((P_F(R))^2-R^2)/2\) and \(\Delta H=O(R^{-1})\), solving for \(P_F(R)-R\) gives the claimed two-term expansion. For piecewise affine coefficients depending analytically on parameters, each transversal sector flow and finite composition extends analytically after setting \(u=R^{-1}\): the normalized energy differs from its initial value by \(O(u^3)\), and the denominators become analytic, uniformly nonvanishing functions of \(u\). Consequently the remainder may be differentiated with respect to \(u\), so
\[
G(u,\lambda):=u^{-2}\big(P_{F_\lambda}(1/u)-1/u\big)
=2M_1(F_\lambda)+2M_3(F_\lambda)u^2+O(u^3),
\]
and \(\partial_uG=4M_3(F_\lambda)u+O(u^2)\), uniformly for \(u\ge0\) small.

**3. Exact four-jump moments.** On the negative pulse \([-2,-1]\), the moment contributions are \(-3/2\) and \(-27/8\). On the positive pulse \([2,3]\), writing \(c=3/5+\lambda\), they are \(5c/2\) and \(5c^3/2+65c/8\), respectively. Thus
\[
M_1(F_\lambda)=\frac52\lambda,\qquad
M_3(F_\lambda)=-\frac{27}{8}+\frac52c^3+\frac{65}{8}c,
\]
and in particular \(M_3(F_0)=51/25>0\). These equalities use exact rational arithmetic.

**4. Exterior orbit census and scale.** Choose \(u_0>0\) and \(\lambda_0>0\) small enough that \(\partial_uG(u,\lambda)>0\) throughout \(0<u\le u_0\), \(|\lambda|\le\lambda_0\), and \(G(u_0,\lambda)>0\). For negative \(\lambda\), \(G(0,\lambda)=5\lambda<0\), so strict monotonicity produces precisely one root \(u_\lambda\in(0,u_0)\). For \(\lambda\ge0\), \(G(u,\lambda)>0\) for every \(u\in(0,u_0]\), hence no such root. Every root determines one prime periodic crossing orbit since it is the first-return section of one rotation.

At the unique negative-parameter root,
\[
u_\lambda^2\sim-\frac{M_1(F_\lambda)}{M_3(F_0)}=-\frac{125}{102}\lambda,
\]
which gives the stated radius law. Differentiating the return expansion in \(R\), substituting \(M_1(F_\lambda)=-M_3(F_\lambda)/R_\lambda^2+O(R_\lambda^{-3})\), yields
\[
P'_{F_\lambda}(R_\lambda)
=1-\frac{4M_3(F_0)}{R_\lambda^5}+o(R_\lambda^{-5})
=1-\frac{204}{25R_\lambda^5}+o(R_\lambda^{-5}).
\]
This is strictly between zero and one for sufficiently small negative \(\lambda\), completing hyperbolicity and attraction. At \(\lambda=0\), the positive fourth-order displacement excludes exterior cycles. All claims concern the crossing field itself, not an averaging approximation.

## Verification
A standalone executable `check.py` evaluates both moments with exact fractions and integrates the four energy branches independently by fourth-order Runge–Kutta. It passed 13 diagnostic assertions, including scaling of the unperturbed energy defect and the opposite signed returns on either side of the predicted large orbit for two negative parameters. The analytic proof establishes the universal expansion, exterior root uniqueness and multiplier; these finite tests merely corroborate constants and signs. The package contains the complete source of `check.py` for reproduction with a standard Python 3 interpreter.

## Relationship to prior work
Chen, Li, Zhang and Zhang's 2026 investigation develops phase-portrait classifications and cycle lower bounds for piecewise-linear Liénard fields. The full author-uploaded manuscript's Remark 2 explicitly leaves the exceptional **symmetric exterior but asymmetric interior** center–focus distinction for further analysis. Our compactly supported \(F\) is identically zero on the two outer tails and asymmetric inside, precisely meeting the stated exceptional geometry. Their results do not supply the displayed moment sequence, the exact four-jump tuning, or the unique cycle escaping at the inverse square-root rate. General higher-cycle existence bounds cannot imply this localized bifurcation theorem.

Jia and Meng's September 2026 work concerns a broader family with independently piecewise-linear restoring force and supplies sufficient conditions for focus direction and a necessary condition for a center. Its public abstract was examined, but its full primary text was not accessible, so potential implicit overlap with moment criteria remains unresolved. Bastos, Buzzi and Torregrosa examine nonregular angular switching rather than four fixed vertical jump lines. More recent bounds for discontinuous piecewise-linear Liénard systems concern global counts; the available abstract alone does not settle whether they contain a similar exterior reduction. These are acknowledged priority limitations, not claims that their unavailable text was exhaustively checked.

## Limitations
The exterior moment expansion does not classify the simultaneous-vanishing case \(M_1(F)=M_3(F)=0\). The four-jump example proves uniqueness only sufficiently near infinity, not globally. The result is limited to bounded compact-support forcing for the moment formulas and to sufficiently small parameter magnitude for the cycle bifurcation. No robustness under shifted jump locations, higher-dimensional perturbations, or noncrossing Filippov cycles is claimed. The cited September 2026 primary article and the October 2026 discontinuous-case preprint could not both be compared in full text; bibliographic priority remains subject to independent confirmation.

## References
1. H. Chen, Z. Li, R. Zhang and X. Zhang, *The number of limit cycles of piecewise linear Liénard systems*, author full text uploaded 2026-08-06, arXiv:2608.19542 (arXiv version first posted 2026-08-20). https://www.researchgate.net/publication/411756691_The_number_of_limit_cycles_of_piecewise_linear_Lienard_systems
2. M. Jia and Y. Meng, *Dynamics of piecewise linear Lienard systems near infinity*, Electronic Journal of Differential Equations 2026, no. 74, pp. 1–19, published 2026-09-28. https://doi.org/10.58997/ejde.2026.74
3. C. A. B. Bastos, C. A. Buzzi and J. Torregrosa, *Cyclicity Near Infinity in Piecewise Linear Vector Fields Having a Nonregular Switching Line*, Qualitative Theory of Dynamical Systems (2023). https://doi.org/10.1007/s12346-023-00817-9
4. H. Chen, J. Jin, Z. Li and Y. Lu, *Bounds on the maximum number of limit cycles of piecewise linear Lienard systems II. The discontinuous case*, arXiv:2610.11916, first posted 2026-10-08. https://arxiv.org/abs/2610.11916
5. S. Cai, H. Chen, J. Jin and Y. Lu, *Bounds on the maximum number of limit cycles of piecewise linear Lienard systems I. The continuous case*, arXiv:2610.10050, first posted 2026-10-07. https://arxiv.org/abs/2610.10050
