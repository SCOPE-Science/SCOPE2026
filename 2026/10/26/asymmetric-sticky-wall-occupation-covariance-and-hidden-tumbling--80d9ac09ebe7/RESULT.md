# Asymmetric sticky-wall occupation covariance and hidden-tumbling identification

## Finding
For the stationary, nonabsorbing, one-dimensional run-and-tumble particle specified below, the two cumulative wall-occupation times have an exact long-time covariance matrix. Its off-diagonal coefficient is **strictly negative** and **strictly decreasing** in the bulk tumbling rate, even though both stationary wall-occupation means are independent of that rate. Consequently, for a known interval length and speed, the two mean wall occupations and their long-time cross-covariance uniquely determine the two possibly unequal wall-detachment rates and the bulk tumbling rate.

Write the flight time \(\tau=L/v\), wall waiting-time halves \(u=1/(2\gamma_0)\), \(w=1/(2\gamma_L)\), and \(H=\tau+u+w\). The stationary wall masses are \(p_0=u/H\) and \(p_L=w/H\). Define \(A_i(T)=\int_0^T\mathbf1_{\{Y_t=B_i\}}\,dt\). For indices \(i,j\in\{0,L\}\), the limits
\[
\Sigma_{ij}=\lim_{T\to\infty}T\operatorname{Cov}\left(\frac{A_i(T)}T,\frac{A_j(T)}T\right)
\]
exist and have entries
\[
\begin{aligned}
\Sigma_{00}&=\frac{2u^2}{3H^3}\left(2\alpha\tau^3+6\alpha\tau^2w+6\alpha\tau w^2+3\tau^2+6\tau w+6w^2\right),\\
\Sigma_{LL}&=\frac{2w^2}{3H^3}\left(2\alpha\tau^3+6\alpha\tau^2u+6\alpha\tau u^2+3\tau^2+6\tau u+6u^2\right),\\
\Sigma_{0L}&=\Sigma_{L0}=-\frac{2uw}{3H^3}\left[\alpha\bigl(\tau^3+3\tau^2(u+w)+6\tau uw\bigr)+3\tau(u+w)+6uw\right].
\end{aligned}
\]
Every parameter is positive, hence \(\Sigma_{0L}<0\) and \(\partial_\alpha\Sigma_{0L}<0\), with
\[
\partial_\alpha\Sigma_{0L}=-\frac{2uw\tau}{3H^3}\left(\tau^2+3\tau(u+w)+6uw\right).
\]

The inverse map is explicit: from measured \(p_0,p_L\) (both positive, with \(p_0+p_L<1\)), obtain
\[
H=\frac{\tau}{1-p_0-p_L},\qquad u=Hp_0,\qquad w=Hp_L,\qquad \gamma_0=\frac1{2u},\quad\gamma_L=\frac1{2w},
\]
and then recover
\[
\alpha=\frac{-3H^3\Sigma_{0L}/(2uw)-3\tau(u+w)-6uw}{\tau^3+3\tau^2(u+w)+6\tau uw}.
\]
For observations arising from the stated model with \(\alpha>0\), this reconstructed value is positive. These equalities are population identities, not finite-sample estimation-error bounds.

## Assumptions and scope
Fix \(L,v,\alpha,\gamma_0,\gamma_L>0\). In the interior \((0,L)\) the particle travels at velocity \(+v\) or \(-v\), reversing direction at independent exponential rate \(\alpha\). When a left-moving particle reaches zero it enters the bound state \(B_0\), stays an independent exponential time of rate \(\gamma_0\), then departs rightward. When a right-moving particle reaches \(L\) it enters \(B_L\), stays at exponential rate \(\gamma_L\), then departs leftward. There is no killing or absorption. The particle is initialized in the invariant distribution, and wall occupations include only time in their respective bound states. Distinct wall waiting times are independent of all interior reversals. The bulk generator, acting on differentiable test functions \(f_\pm\), is
\[
(\mathcal L f)_\pm(x)=\pm v\,\partial_x f_\pm(x)+\alpha(f_\mp(x)-f_\pm(x)),
\]
with wall generators \((\mathcal L f)(B_0)=\gamma_0[f_+(0)-f(B_0)]\) and \((\mathcal L f)(B_L)=\gamma_L[f_-(L)-f(B_L)]\). Functions in its natural piecewise-smooth domain satisfy \(f_-(0)=f(B_0)\) and \(f_+(L)=f(B_L)\). This convention is essential to the normalizations above; some literature calls twice the reversal rate the tumbling rate.

## Proof
**Invariant law.** Zero stationary current makes the two interior velocity densities constant and equal. Normalize each to \(1/(2vH)\) with respect to physical position \(x\). The inflow/outflow balances at the walls then give masses \(p_0=u/H\) and \(p_L=w/H\), while the interior mass is \(\tau/H\). The positive rates, finite interval, and regeneration at the walls give an irreducible positive-recurrent process and a unique invariant law.

**Poisson equations.** Set \(b_j=\mathbf1_{\{B_j\}}\), \(g_j=b_j-p_j\), and \(s=x/v\), so \(0\le s\le\tau\). For \(j\in\{0,L\}\), put \(c_j=u(p_j-\mathbf1_{\{j=0\}})\),
\[
J_j(s)=p_js+c_j,\qquad K_j(s)=\alpha p_js^2+2\alpha c_js,
\]
and construct the bounded functions
\[
h_{j,+}(x)=K_j(x/v)+J_j(x/v),\quad h_{j,-}(x)=K_j(x/v)-J_j(x/v),
\]
\[
h_j(B_0)=-c_j,\qquad h_j(B_L)=K_j(\tau)+J_j(\tau).
\]
Direct differentiation gives \((\mathcal Lh_j)_\pm=p_j=-g_j\) in the interior. At the left wall, \(\gamma_0(h_{j,+}(0)-h_j(B_0))=2\gamma_0c_j=p_j-\mathbf1_{\{j=0\}}=-g_j(B_0)\). At the right wall, the identity \(J_j(\tau)=-w(p_j-\mathbf1_{\{j=L\}})\) gives \(\gamma_L(h_{j,-}(L)-h_j(B_L))=p_j-\mathbf1_{\{j=L\}}=-g_j(B_L)\). The boundary continuity conditions also hold. Thus \(-\mathcal Lh_j=g_j\) at all states.

**Integrated covariance.** By Dynkin's formula, \(M_j(T)=h_j(Y_T)-h_j(Y_0)+\int_0^Tg_j(Y_t)dt\) is a square-integrable martingale. Both correctors are bounded; their bounded endpoint terms contribute \(o(T)\) to variances and covariances, by Cauchy--Schwarz and the martingale \(O(T)\) second-moment bound. Invariance applied to the product of the correctors yields the limiting cross-quadratic-variation rate
\[
\Sigma_{ij}=\pi(g_i h_j)+\pi(g_j h_i).
\]
The invariant expectation is an elementary integral with density \(1/(2vH)\) for each interior velocity and masses \(p_0,p_L\) at the two walls. Substituting the explicit quadratic polynomials gives the three displayed entries. All finite integrals and generator identities are exact; the standalone symbolic checker independently verifies their algebra. Since every term inside the displayed bracket for \(\Sigma_{0L}\) is positive, the strict sign and strict slope follow; rearranging its affine dependence on \(\alpha\) gives the inverse formula.

## Verification
Run `python checker.py` with Python, SymPy, NumPy, and SciPy. It checks all generator equations, both boundary conditions, invariant integrations, the complete covariance matrix, and strict-slope identity symbolically. As an independent diagnostic, it forms finite-state upwind transport chains for three unequal-wall parameter choices, computes their invariant Green--Kubo matrices by solving Poisson systems, and checks monotone convergence of the finite-mesh errors as the mesh is refined through 40, 80, 160, and 320 cells. The exact symbolic calculation, not finite-mesh agreement, supplies the general proof. The actual stdout is in `checker_output.txt`.

## Relationship to prior work
Bressloff's 2023 encounter-based sticky-boundary model introduces the same confined active particle, its bound-state probabilities, and occupation-time propagators. Its explicit two-wall occupation-time transform uses a common release rate \(\gamma_0=\gamma_L\), and focuses on absorption and first-passage observables. Thus it covers key model foundations and, in its equal-release subfamily, broad generating-function information; no priority is claimed for that subfamily or for the generator itself. The theorem above instead evaluates the stationary **long-time covariance matrix at arbitrary unequal positive release rates**, proves global cross-anticorrelation, and gives exact parameter identifiability. Angelani's 2023 generic-boundary work allows unequal wall parameters but derives mean exit times, not the stationary residence-time covariance matrix. The new result is a direct analysis of the asymmetric no-absorption model rather than a new boundary dynamics model.

## Limitations
The result requires independent memoryless wall release, two symmetric bulk velocities with a constant speed, homogeneous Poisson reversals, no absorption, and stationary initialization. It does not establish finite-time covariance functions, finite-sample uncertainty for the inverse reconstruction, analogous formulas with orientation-dependent reversals, or interacting-particle extensions. Priority remains subject to wider literature and independent review; an unpublished or differently formulated additive-functional calculation could overlap the evaluated result. The equal-wall case is particularly close to existing joint occupation-time transform methods and is not the novelty basis.

## References
1. Paul C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1, first public February 2, 2023. https://arxiv.org/html/2302.01158v1 . See Sections 2 and 5.
2. Luca Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, Journal of Physics A: Mathematical and Theoretical 56 (2023) 455003, doi:10.1088/1751-8121/ad009e. https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf . See Sections 2, 4--6 and Appendix.
3. Luca Angelani, *Confined run-and-tumble swimmers in one dimension*, arXiv:2206.03123, first public June 7, 2022. https://arxiv.org/abs/2206.03123 .
