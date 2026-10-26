# Midpoint rigidity for universal weak entropy stability of compact Runge–Kutta DG

## Finding

Consider the **uncorrected** degree-one compact Runge–Kutta discontinuous Galerkin (cRKDG) method for constant-speed scalar advection with the upwind physical and entropy fluxes. Among every two-stage second-order explicit Runge–Kutta tableau with **nonnegative output weights**, the discrete weak cell-entropy inequality for **every finite convex entropy and every piecewise-affine input** holds at a positive Courant number **if and only if the tableau is explicit midpoint**. For explicit midpoint the exact universal Courant interval is \(0<r\leq1\); outside it the inequality fails already for the quadratic entropy. All other tableaus fail at *every* positive Courant number, even for a suitably chosen \(C^2\), globally strongly convex entropy.

The distinction is in the entropy-flux quadrature, not the solution update: **every tableau in this family has exactly the same linear cRKDG solution map**, while only explicit midpoint admits the stated universal entropy certificate. Moreover, on even periodic meshes, for \(1/3<r\leq1\) the explicit-midpoint map satisfies the weak inequality for every convex entropy in every cell, but its full polynomial-state update has an amplifying alternating Fourier mode. Thus this entropy inequality cannot be mistaken for full-state stability.

## Assumptions and scope

On a uniform periodic mesh of \(N\geq2\) cells of width \(h>0\), consider \(u_t+v u_x=0\) with \(v>0\). Each input cell polynomial has the form \(u_j(\xi)=a_j+b_j\xi\), \(-1\leq\xi\leq1\). Define the Courant number \(r=v\tau/h\), where \(\tau\geq0\) is one time step. We use exact spatial integration, the cell-local operator \(\mathcal G=-v\partial_x\) for inner stages, and the upwind DG operator \(\mathcal F\) in the final update. There is no stage or end-of-step limiter.

Every two-stage second-order explicit RK tableau with nonnegative output weights is parametrized by \(\gamma\geq1/2\): \(a_{21}=\gamma\), \(w_1=1-1/(2\gamma)\), and \(w_2=1/(2\gamma)\). The internal state is \(u^{(2)}=u+\gamma\tau\mathcal G(u)\), and the final update is \(u^+=u+\tau[w_1\mathcal F(u)+w_2\mathcal F(u^{(2)})]\). Explicit midpoint corresponds to \(\gamma=1/2\).

For any finite convex \(\eta:\mathbb R\to\mathbb R\), the compatible physical entropy flux is \(q(u)=v\eta(u)\), and the proper upwind numerical entropy flux is \(v\eta(u_{\mathrm{left}})\). The RK-averaged outgoing stage entropy flux, after division by \(v\), is
\[
Q_j^\eta=w_1\eta(a_j+b_j)+w_2\eta\bigl(a_j+(1-2\gamma r)b_j\bigr).
\]
The weak cell-entropy inequality in question is
\[
\eta(a_j^+)\leq\frac12\int_{-1}^{1}\eta(a_j+b_j\xi)\,d\xi-r(Q_j^\eta-Q_{j-1}^\eta),\qquad j=0,\ldots,N-1.
\]
All indices are periodic. The quantifier “universal” means this inequality for every admissible periodic input and every finite convex entropy; the same tableau and Courant number must work for all of them.

## Proof

**1. Identical physical updates.** The local operator sends the affine polynomial \(a_j+b_j\xi\) to the constant \(-2vb_j/h\). Consequently its stage-face values are \(p_j^{(1)}=a_j+b_j\) and \(p_j^{(2)}=a_j+(1-2\gamma r)b_j\). Their RK average equals
\[
\overline p_j=w_1p_j^{(1)}+w_2p_j^{(2)}=a_j+(1-r)b_j.
\]
Testing the final DG equation by the cell constant gives
\[
a_j^+=a_j-r(\overline p_j-\overline p_{j-1}).
\]
Because the physical DG operator is linear, the entire (mean and slope) update is \(u^+=u+\tau\mathcal F(u)+\tau^2\mathcal F\mathcal G(u)/2\), independent of \(\gamma\). This does **not** make the nonlinear entropy-flux averages \(Q_j^\eta\) independent of \(\gamma\).

**2. All convex entropies for midpoint.** Suppose \(\gamma=1/2\), hence \(w_1=0\), \(w_2=1\), and \(Q_j^\eta=\eta(\overline p_j)\). For \(0\leq r\leq1\), partition the reference interval into \([-1,1-2r]\) and \([1-2r,1]\). Their fractional lengths are \(1-r\) and \(r\), with respective means under \(u_j\)
\[
\ell_j=a_j-rb_j,\qquad \overline p_j=a_j+(1-r)b_j.
\]
Thus \(a_j=(1-r)\ell_j+r\overline p_j\) and the updated mean is \(a_j^+=(1-r)\ell_j+r\overline p_{j-1}\). Jensen's inequality on each subinterval and then on this final convex combination gives
\[
\frac12\int_{-1}^1\eta(u_j(\xi))\,d\xi
\geq(1-r)\eta(\ell_j)+r\eta(\overline p_j)
\geq\eta(a_j^+)+r\bigl[\eta(\overline p_j)-\eta(\overline p_{j-1})\bigr].
\]
This proves the requested inequality simultaneously for all convex entropies, including nonsmooth ones, without curvature bounds or stage limiting.

For \(\eta\in C^2\) with \(\eta''\geq\mu\geq0\), the same decomposition yields the quantitative bound
\[
\begin{split}
&\frac12\int_{-1}^1\eta(u_j(\xi))\,d\xi-r(Q_j^\eta-Q_{j-1}^\eta)-\eta(a_j^+)\\
&\qquad\geq\frac{\mu b_j^2}{6}\bigl[(1-r)^3+r^3\bigr]
+\frac{\mu r(1-r)}2\bigl(\ell_j-\overline p_{j-1}\bigr)^2.
\end{split}
\]
It is an **identity** for a quadratic entropy of curvature \(\mu\), up to an arbitrary affine term.

**3. Necessity of the Courant bound at midpoint.** For any \(r>1\), take the current cell constant \(0\), the preceding cell constant \(1\), and \(\eta(z)=z^2/2\). Then \(a_j^+=r\), while the entropy budget is \(r/2\). Since \(r^2/2>r/2\), the inequality fails. This construction is available on any periodic mesh with at least two cells.

**4. Every other nonnegative-weight tableau fails at every positive Courant number.** Fix \(\gamma>1/2\) and \(r>0\). Set the current cell polynomial to \(u_j(\xi)=\xi\) and the upstream cell to the constant \(-r\), so that \(a_j^+=-r\). Put \(w_1=1-1/(2\gamma)>0\). Choose \(0<\delta<\min\{2,1+r,2\gamma r,10rw_1\}\), set \(t=1-\delta\), and first consider \(\eta_0(z)=(z-t)_+^4\). Both the new mean and all incoming stage values lie below \(t\); so does the outgoing second-stage value \(1-2\gamma r\). Only the outgoing first-stage value \(1\) contributes. Direct integration gives the exact weak-entropy defect (budget minus entropy of the new mean):
\[
\frac12\int_{-1}^1\eta_0(\xi)\,d\xi-rw_1\eta_0(1)
=\delta^4\left(\frac{\delta}{10}-rw_1\right)<0.
\]
Now let \(\eta_\mu(z)=\eta_0(z)+\mu z^2/2\). For sufficiently small \(\mu>0\), the strict negative defect persists. This entropy is \(C^2\), globally \(\mu\)-strongly convex, and has bounded curvature on every compact state range. Hence **no positive Courant threshold**, however small, works uniformly over convex entropies for any \(\gamma>1/2\).

For an exact concrete instance, choose \(\gamma=1\), \(r=1/4\), \(\delta=1/4\), and \(\mu=1/1000\). Then the entropy \(\eta(z)=(z-3/4)_+^4+z^2/2000\) has exact defect
\[
-\frac1{2560}+\frac1{1000}\cdot\frac{25}{384}=-\frac1{3072}<0.
\]
Together with Steps 2–3 this completes the “if and only if” classification for positive Courant numbers.

**5. Weak entropy versus full-state stability.** On an even periodic mesh, the alternating Fourier mode in the two coefficients \((a_j,b_j)\) has full-step matrix
\[
M_\pi(r)=\begin{pmatrix}1-2r&-2r(1-r)\\6r&1-6r^2\end{pmatrix},
\qquad\det M_\pi(r)=1-2r+6r^2.
\]
For every \(r>1/3\), its determinant is greater than one, so at least one eigenvalue has modulus exceeding one. In particular, the range \(1/3<r\leq1\) has an amplifying full-polynomial Fourier mode **despite** the per-cell weak inequality for every convex entropy. No full-state stability or nonlinear-conservation-law conclusion is claimed.

## Verification

The accompanying `checker.py` uses exact rational arithmetic. It compares the DG coefficient update and the quadratic Jensen identity on 320 rational configurations; confirms the \(-1/3072\) smooth strongly convex witness; checks a further 16 non-midpoint tableau/Courant combinations against the constructive quartic-hinge argument; and checks the alternating-mode determinant identity. These finite calculations confirm formulas and examples; universality follows from the preceding proofs.

## Relationship to prior work

Sun (2026), arXiv:2610.18837, develops cRKDG weak cell entropy inequalities for strongly convex entropies under sufficient dissipation and CFL restrictions, then imposes a common end-of-step entropy limiter. Its flux and RK-stage definitions are those used here. The present result is a sharp uncorrected **linear-advection, degree-one, upwind** classification that includes all convex entropies, and distinguishes the nonlinear entropy-flux averages of physically identical RK2 updates. It does not imply the source's nonlinear results.

Liu, Sun, and Zhang (2024), arXiv:2412.16002, derive invariant-domain and bound-preserving cRKDG decompositions, including the explicit midpoint tableau. Those conclusions are about bounds of stage solutions and do not give the present necessary-and-sufficient classification of the RK-averaged numerical entropy flux across every convex entropy. Chen, Sun, and Xing (2023), arXiv:2307.06471, develop the cRKDG construction and relate its linear physical update to Lax–Wendroff DG; the equivalence of physical updates is prior context, not claimed new here. Earlier Lax–Wendroff DG stability theory addresses spectral or error bounds rather than this entropy-flux tableau rigidity. Literature comparisons remain subject to possible unindexed antecedents.

## Limitations

The theorem assumes constant positive advection speed, degree-one polynomials, a uniform periodic mesh, exact spatial integration, no limiters, and the specific proper upwind entropy flux with RK stage averaging. The full state can be unstable when the weak inequality holds. The negative result concerns universal quantification over all convex entropies; an individual fixed well-conditioned entropy may satisfy an inequality for a positive timestep with a non-midpoint tableau. The proof does not classify higher-order RK methods, higher-degree DG, nonlinear fluxes, or other numerical entropy-flux definitions.

## References

1. Zheng Sun, *Fully discrete multi-entropy-stable compact Runge–Kutta discontinuous Galerkin methods for hyperbolic conservation laws*, arXiv:2610.18837, first public version 2026-10-13, https://arxiv.org/abs/2610.18837.
2. Chen Liu, Zheng Sun, Xiangxiong Zhang, *A bound-preserving Runge–Kutta discontinuous Galerkin method with compact stencils for hyperbolic conservation laws*, arXiv:2412.16002, first public version 2024-12-20, https://arxiv.org/abs/2412.16002.
3. Qifan Chen, Zheng Sun, Yulong Xing, *The Runge–Kutta discontinuous Galerkin method with compact stencils for hyperbolic conservation laws*, arXiv:2307.06471, first public version 2023-07-12, https://arxiv.org/abs/2307.06471.
4. Zheng Sun, Chi-Wang Shu, *Stability analysis and error estimates of Lax–Wendroff discontinuous Galerkin methods for linear conservation laws*, ESAIM: M2AN 51 (2017), 1063–1087, DOI:10.1051/m2an/2016049.
