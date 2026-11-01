# A fourth-iterate projection law and a physical-measure bifurcation in a border-collision map

## Finding
For every real \(\mu\), define the continuous piecewise-affine map \(F_\mu:\mathbb R^2\to\mathbb R^2\) by
\[
F_\mu(x,y)=\begin{cases}(y+\mu,0),&x\le0,\\(y+\mu,-x),&x\ge0.\end{cases}
\]
Define the closed convex set
\[
K_\mu=\begin{cases}\{(\mu,0)\},&\mu\le0,\\[0,\mu]\times[-\mu,0],&\mu>0.\end{cases}
\]
The fourth iterate is *exactly the Euclidean nearest-point projection*, on the **entire plane**:
\[
\boxed{F_\mu^4=\Pi_{K_\mu}.}
\]
The bound four is sharp as a uniform entry time for every value of \(\mu\). Every forward orbit enters \(K_\mu\) by its fourth step, and all of its subsequent iterates are periodic with period dividing four.

For \(\mu\le0\), the only periodic point and invariant Borel probability are respectively \((\mu,0)\) and its Dirac measure; all points reach the fixed point in at most four steps. For \(\mu>0\), the restriction \(F_\mu|_{K_\mu}\) is a clockwise quarter-turn about \((\mu/2,-\mu/2)\). Thus the center is the sole fixed point, and every other point of the square has **least period four**. Every invariant Borel probability is supported on the square; its ergodic components are uniform measures on these finite orbits.

Let \(\lambda_2\) be planar Lebesgue measure, and call an invariant probability *physical* when its empirical-measure basin has positive \(\lambda_2\)-measure in \(\mathbb R^2\). For \(\mu>0\), the unique physical probability is the uniform measure \(\eta_\mu\) on the four corners of \(K_\mu\). Its basin is exactly
\[
\boxed{B(\eta_\mu)=\bigl(( -\infty,0]\cup[\mu,\infty)\bigr)\times\bigl(( -\infty,-\mu]\cup[0,\infty)\bigr).}
\]
No other invariant probability has a positive planar-Lebesgue basin. In particular the normalized area probability on the square is invariant, but is **not** physical. For \(\mu\le0\), the unique physical measure is \(\delta_{(\mu,0)}\) with whole-plane basin. The family therefore undergoes an exact stationary-measure and basin-structure transition at \(\mu=0\).

## Assumptions and scope
The map acts on all real pairs \((x,y)\) and permits any real forcing \(\mu\). The two branch formulas agree on the switching line \(x=0\), so its assignment there is unambiguous. The coefficient choice is the zero-determinant planar border-collision normal form with a nilpotent left Jacobian (zero trace) and right Jacobian having eigenvalues \(\pm i\), i.e. the quarter-turn unit-determinant resonance. No attractivity or continuity conclusion is asserted for nearby choices of the branch Jacobians. Invariant measures are Borel probabilities on \(\mathbb R^2\), not assumed absolutely continuous. Empirical measures are \(N^{-1}\sum_{n=0}^{N-1}\delta_{F_\mu^n(z)}\), with weak convergence tested against bounded continuous functions.

## Proof
**Exact scalar reduction.** Put \(t_+=\max(t,0)\) and \(q_\mu(t)=\mu-t_+\). The map can be written \(F_\mu(x,y)=(y+\mu,-x_+)\). For its iterates \((x_n,y_n)\),
\[
x_{n+1}=\mu+y_n,\qquad x_{n+2}=q_\mu(x_n).
\]
Consequently,
\[
F_\mu^4(x,y)=\bigl(q_\mu^2(x),q_\mu^2(\mu+y)-\mu\bigr).
\]
If \(\mu\le0\), then \(q_\mu(t)\le\mu\le0\) for all real \(t\), hence \(q_\mu^2(t)=\mu\). If \(\mu>0\), the exhaustive cases \(t\le0\), \(0\le t\le\mu\), and \(t\ge\mu\) give
\[
q_\mu^2(t)=\begin{cases}0,&t\le0,\\t,&0\le t\le\mu,\\\mu,&t\ge\mu.\end{cases}
\]
Thus \(q_\mu^2\) is clipping to \([0,\mu]\); the displayed formula for \(F_\mu^4\) is coordinatewise orthogonal projection onto \(K_\mu\). This establishes the formula for all parameters, all initial conditions, and all branch-boundary points.

**Sharpness, periodic points, and measures.** For \(\mu>0\), on \(K_\mu\), set \(u=x-\mu/2\) and \(v=y+\mu/2\). One iteration acts as \((u,v)\mapsto(v,-u)\), a rotation of order four with only the origin fixed. Since the fourth iterate maps the whole plane into \(K_\mu\), all later trajectories rotate there. If a point outside \(K_\mu\) were periodic, one of its sufficiently large periodic iterates would lie inside \(K_\mu\), a contradiction. For \(\mu\le0\) the fourth iterate is constant at the fixed point. The universal entry time cannot be three: for \(\mu>0\), the state \((\mu/2,\mu)\) has third iterate \((-\mu,-\mu/2)\), outside \(K_\mu\); for \(\mu\le0\), the state \((0,1-2\mu)\) has third-iterate first coordinate \(2\mu-1\ne\mu\). The fourth-iterate map has image exactly \(K_\mu\) because it fixes every point there. For any invariant probability \(\rho\), invariance under the fourth iterate and its image imply \(\rho(K_\mu)=1\). On the finite-order rotation, averaging an arbitrary probability \(\nu\) over its four rotations produces precisely the invariant probabilities; the ergodic ones are orbit-uniform measures. For \(\mu\le0\) only the single Dirac measure remains.

**Physical-measure classification.** For every initial state \(z\), the empirical measures converge to the orbit-uniform probability of \(\Pi_{K_\mu}(z)\) (the first four transient terms do not affect the limit). If \(\mu>0\), the four corners form a primitive orbit, and a point projects to a corner exactly when each coordinate lies beyond an endpoint of its corresponding projection interval. This proves the stated basin equality. It contains open quadrants and hence has positive Lebesgue measure. For any other orbit in \(K_\mu\), every point of that orbit has at least one coordinate strictly inside its corresponding clipping interval; the inverse image of that single point under \(\Pi_{K_\mu}\) is a singleton or one straight ray, both planar null sets. A finite union remains null. No non-ergodic invariant measure is an empirical limit at any point, because every limit is supported on a single finite orbit. Therefore the corner measure is the unique physical measure. The square's normalized area measure is invariant under its rotation but its basin is empty. For \(\mu\le0\), every point lands at the fixed point within four steps, proving the remaining assertions.

## Verification
The proof uses only explicit scalar identities, three exhaustive intervals for \(q_\mu^2\), and elementary properties of finite rotations and coordinatewise projection. A standalone standard-library Python program, `verify.py`, exercises the exact fourth-, eighth-, and twelfth-iterate identities on a rational grid for negative, zero and positive forcing, including switching-line and interval-boundary points. It additionally checks the four-corner cycle, fixed center, and sharpness witnesses. Its executed output is recorded in `VERIFICATION.md`. Finite checks are supplementary and are not the proof of the universal quantifiers.

## Relationship to prior work
Simpson's 2024 preprint (later published in 2025) supplies the two-dimensional zero-determinant border-collision normal form and studies its principal bifurcation regimes; that construction is prior work. The present result is an exact global fourth-iterate projection, complete invariant-probability classification and physical-basin theorem at the simultaneous nilpotent-left/quarter-turn-right resonance, not a new normal-form construction. Simpson's 2026 first-return analysis treats repelling right focus parameters with right determinant **strictly greater than one**, whereas the present right determinant is exactly one. The 2007/2008 Szalai–Osinga work examines invariant polygons for unstable complex multipliers and is relevant background but its complete preprint was not obtainable in this investigation. Generic existence results for absolutely continuous stationary measures in border-collision maps do not imply the claimed physical-basin classification here. None of these literature comparisons is a proof of absolute novelty; see `REVIEW.md` for residual risk.

## Limitations
The projection identity relies on the exact branch coefficients: it does not imply persistence under generic perturbation, and the physical measure is defined relative to ambient planar Lebesgue measure, not normalized Lebesgue restricted to the invariant square. At \(\mu>0\), the corner-cycle basin has positive ambient area but is not full measure; indeed a positive-area set of other initial conditions has distinct orbit averages. Unindexed equivalent results and an inaccessible older polygon-preprint remain publication-priority risks. No independent validation has been performed.

## References
1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1 (first public posting 2024-08-08); SIAM J. Appl. Dyn. Syst. 24 (2025), 2205–2245, DOI:10.1137/24M1683548. https://arxiv.org/abs/2408.04790
2. D. J. W. Simpson, *One-Dimensional First Return Maps for the Two-Dimensional Border-Collision Normal Form with a Zero Determinant*, arXiv:2606.08901 (2026), Qual. Theory Dyn. Syst. 25 (2026), article 160. https://doi.org/10.1007/s12346-026-01576-z
3. R. Szalai and H. M. Osinga, *Invariant polygons in systems with grazing-sliding*, Chaos 18 (2008), 023121; 2007 preprint. DOI:10.1063/1.2904774.
4. P. Glendinning, *Invariant measures for the n-dimensional border collision normal form*, Int. J. Bifurcation Chaos (2014), preprint in MIMS EPrints. https://eprints.maths.manchester.ac.uk/2252/
