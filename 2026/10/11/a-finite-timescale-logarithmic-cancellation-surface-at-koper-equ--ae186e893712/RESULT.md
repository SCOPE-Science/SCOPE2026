# A finite-timescale logarithmic-cancellation surface at Koper equilibrium folds

## Finding
Consider the three-dimensional Koper flow
\[
\varepsilon\dot x=ky+3x-x^3-\lambda,\qquad
\dot y=x-2y+z,\qquad
\dot z=\delta(y-z).
\]
For arbitrary fixed real parameters \(k>0\), \(\varepsilon>0\), and \(\delta>0\), define
\[
r\in\left\{\sqrt{\frac{k+3}{3}},-\sqrt{\frac{k+3}{3}}\right\},
\qquad \lambda=\frac23(k+3)r,\qquad E_r=(r,r,r),
\]
and set
\[
H=\varepsilon+k\left(1+\frac1\delta\right),\quad
S=1+\frac2\delta+\frac2{\delta^2},\quad
L=\frac1{3r}-\frac{6krS}{H^2}.
\]
**Theorem.** At this parameter value, \(E_r\) is an ordinary nondegenerate saddle-node with a one-dimensional center direction and a two-dimensional exponentially stable direction. Every nonstationary trajectory that eventually remains sufficiently close, converges to \(E_r\), and does *not* lie in its local strong-stable manifold has the asymptotic law
\[
\frac1{x(t)-r}=\frac{3r}{H}t+L\log t+C+o(1)\qquad(t\to\infty)
\]
for a finite trajectory-dependent constant \(C\). Such trajectories exist on the attracting side \(r(x-r)>0\); strong-stable trajectories instead converge exponentially. The logarithmic coefficient has a single positive-parameter cancellation threshold:
\[
L=0\ \Longleftrightarrow\
\varepsilon=\varepsilon_*(k,\delta)
:=\sqrt{6k(k+3)\left(1+\frac2\delta+\frac2{\delta^2}\right)}
-k\left(1+\frac1\delta\right)>0.
\]
Thus, for \(r>0\), \(L<0\) below this threshold and \(L>0\) above it; for \(r<0\) the signs reverse. Exactly on the surface the reciprocal relaxation has no logarithmic term: \(1/(x(t)-r)=(3r/H)t+C+o(1)\).

## Assumptions and scope
All statements are for the finite-dimensional smooth ODE at fixed strictly positive \(k,\varepsilon,\delta\); no singular-limit scaling, global-attractor assertion, or nonstationary periodic-orbit exclusion is asserted. The fold is a collision of full-system equilibria, **not** a fold of the singular critical manifold or a folded saddle-node of type II. The time \(t\) is the ODE time appearing above. A local strong-stable manifold of \(E_r\) is the invariant two-dimensional manifold tangent at \(E_r\) to the eigenspaces with negative-real-part eigenvalues. The attracting side exists in a one-dimensional center manifold; for converging nearby orbits off the strong-stable manifold, stable-fiber tracking yields the same algebraic asymptotics. The reciprocal quantity is evaluated only for sufficiently large \(t\), where \(x(t)-r\ne0\).

## Proof
First, equilibria have \(x=y=z=q\) and satisfy \((k+3)q-q^3-\lambda=0\). A multiple root has \(3q^2=k+3\), hence \(q=r\) and \(\lambda=2(k+3)r/3\). At \(E_r\) the Jacobian equals
\[
J=\begin{pmatrix}-k/\varepsilon&k/\varepsilon&0\\1&-2&1\\0&\delta&-\delta\end{pmatrix},
\quad
\det(sI-J)=s\left[s^2+\left(2+\delta+\frac{k}{\varepsilon}\right)s
+\delta+\frac{k(1+\delta)}{\varepsilon}\right].
\]
Both coefficients of the quadratic are positive, so its two roots have strictly negative real parts. Since \(r\ne0\), the fold is nondegenerate once the quadratic center coefficient below is shown nonzero.

Write \(u=x-r\), \(v=y-r\), and \(w=z-r\). Then
\[
\varepsilon\dot u=k(v-u)-3ru^2-u^3,\qquad
\dot v=u-2v+w,\qquad \dot w=\delta(v-w).
\]
The smooth center-manifold theorem gives a local invariant graph
\[
v=u+a u^2+b u^3+O(u^4),\qquad
w=u+c u^2+d_3u^3+O(u^4),
\]
and reduced flow \(\dot u=A u^2+B u^3+O(u^4)\). Matching the coefficients of \(\dot v=(dv/du)\dot u\), \(\dot w=(dw/du)\dot u\) with their original right sides yields
\[
a=-\left(1+\frac1\delta\right)A,\qquad
c=-\left(1+\frac2\delta\right)A,
\]
\[
A=-\frac{3r}{H}\ne0,\qquad
B=\frac{-1+2kA^2S}{H}.
\]
At cubic order a useful explicit consistency representation is \(b=(\varepsilon B+1)/k\) and \(d_3=b-(B+2cA)/\delta\). Substitution into all three graph-invariance equations gives zero residual through cubic order (the accompanying checker reproduces all coefficients).

On the attracting center half-curve \(ru>0\), \(Au<0\), so \(u(t)\to0\) and \(u(t)\sim-1/(At)\). Set \(W(t)=1/u(t)\). The scalar equation gives
\[
\dot W=-A-\frac{B}{W}+O(W^{-2}),
\qquad W(t)\sim -At.
\]
Initially this implies \(W=-At+O(\log t)\); inserting that approximation into the right side sharpens it to
\[
\dot W=-A+\frac{B}{A}\frac1t+O\!\left(\frac{\log t}{t^2}\right).
\]
The remainder is integrable, proving \(W=-At+(B/A)\log t+C+o(1)\). Local exponential tracking along the stable foliation transfers this expansion from center-manifold trajectories to all local convergent trajectories off the strong-stable manifold: the difference between the corresponding reciprocal coordinates is \(O(t^2e^{-\eta t})\) for some \(\eta>0\). Since \(-A=3r/H\) and
\[
\frac BA=\frac1{3r}-\frac{6krS}{H^2}
=\frac{H^2-6k(k+3)S}{3rH^2},
\]
the claimed law follows.

Finally \(H\) is strictly increasing in \(\varepsilon\). The equation \(L=0\) has the sole candidate stated above. It is positive because \(S>(1+1/\delta)^2\) and \(6(k+3)>k\) for all \(k,\delta>0\). The sign assertions follow from the sign of \((H^2-6k(k+3)S)/r\).

## Verification
The standalone `check_koper.py` symbolically expands and checks all cubic-order center-manifold identities, including the coefficient \(B/A\). Running it with Python and SymPy returns seven zero residuals. The independent finite-time numerical *sanity test* `numerical_koper.py` integrates representative trajectories for \(k=\delta=1\), \(r=\sqrt{4/3}\), and \(\varepsilon=2,\varepsilon_*,18\), showing the predicted change of sign and near stabilization of the compensated reciprocal. This integration does not establish the theorem or an infinite-time limit: those follow from the analytic argument above. Both scripts are included as complete runnable text with their library requirements.

## Relationship to prior work
Koper (1995) introduced the full three-variable model, gave its equilibrium saddle-node loci, and focused on bifurcation diagrams and mixed-mode dynamics, with a Hopf normal-form Appendix. Guckenheimer and Lizarraga (2015) studied Shilnikov homoclinic behavior in the same family, principally its singularly perturbed oscillatory regime. Kaklamanos, Popović, and Kristiansen (2022) analyzed singular-limit folded geometries and mixed-mode bifurcations. Here the object is instead the *finite* \(\varepsilon,\delta\) ordinary equilibrium saddle-node on the \(k>0\) side: the explicit reciprocal-rate logarithm and its unique cancellation surface are not asserted in those primary works. Standard center-manifold theory explains the form of the asymptotic expansion, but not the parameter-dependent cancellation expression, which requires the full model's cubic reduction. This relationship is a literature comparison, not a declaration of exhaustive novelty.

## Limitations
There is no claim about basins outside a neighborhood of \(E_r\), periods, mixed-mode oscillations, global heteroclinic connections, dynamics at \(k\le0\), or singular limits \(\varepsilon=0\) or \(\delta=0\). Strong-stable trajectories are explicitly excluded from the reciprocal law. The scalar center manifold need not be unique as a global object, but its displayed Taylor jet and asymptotic coefficients are determined. The earliest precise source date recorded below is the original 1995 issue date, not a later revision date. The broader literature may contain implicit derivations of this model-specific coefficient; the inspected texts and targeted searches did not establish stronger covering statements.

## References
1. M. T. M. Koper, “Bifurcations of mixed-mode oscillations in a three-variable autonomous Van der Pol–Duffing model with a cross-shaped phase diagram,” *Physica D* 80 (1995), 72–94. DOI: 10.1016/0167-2789(95)90061-6. Full work reviewed, particularly Eq. (1), §3.1, and Appendix.
2. J. Guckenheimer and I. Lizarraga, “Shilnikov Homoclinic Bifurcation of Mixed-Mode Oscillations,” *SIAM J. Appl. Dyn. Syst.* 14 (2015), 764–786; arXiv:1406.1813. DOI: 10.1137/140972007.
3. P. Kaklamanos, N. Popović, and K. U. Kristiansen, “Bifurcations of mixed-mode oscillations in three-timescale systems: An extended prototypical example,” *Chaos* 32 (2022), 013108. DOI: 10.1063/5.0073353.
