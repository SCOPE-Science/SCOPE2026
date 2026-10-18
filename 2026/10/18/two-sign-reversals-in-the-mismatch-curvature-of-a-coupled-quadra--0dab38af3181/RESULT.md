# Two sign reversals in the mismatch curvature of a coupled quadratic-map unit-circle boundary

## Finding
Fix a real coupling parameter \(b\in(-1,0)\) and consider the nonidentically driven, linearly coupled quadratic map
\[
F_{a,b,\delta}(x,y)=\bigl(a+\delta-x^2+b(x-y),\ a-\delta-y^2+b(y-x)\bigr).
\]
Set
\[
a_0(b)=b^2+\frac52 b+\frac54,\qquad m_0=b+\frac12,\qquad r_0=\sqrt{\frac{b+1}{2}}.
\]
At \(\delta=0\) and \(a=a_0(b)\), the points \((m_0+r_0,m_0-r_0)\) and \((m_0-r_0,m_0+r_0)\) form a genuine period-two orbit. For each fixed \(b\in(-1,0)\) there are neighborhoods of these points and a unique real-analytic continuation of this orbit together with a real-analytic parameter threshold \(a_{\mathrm{uc}}(b,\delta)\), for \(|\delta|\) sufficiently small, satisfying
\[
\det D(F_{a,b,\delta}^{2})\big|_{\mathrm{orbit}}=1,
\qquad -2<\operatorname{tr}D(F_{a,b,\delta}^{2})\big|_{\mathrm{orbit}}<2.
\]
Thus the two Floquet multipliers are complex conjugates on the unit circle. On the same local complex-multiplier branch, the continued two-cycle is spectrally attracting for \(a<a_{\mathrm{uc}}(b,\delta)\) and spectrally repelling for \(a>a_{\mathrm{uc}}(b,\delta)\), when \(a\) is sufficiently close to the threshold. The boundary is crossed transversely as \(a\) varies. Its **exact leading mismatch response** is
\[
\boxed{a_{\mathrm{uc}}(b,\delta)=b^2+\frac52 b+\frac54+
\frac{(b+1)(3b+1)(3b+2)}{(b-1)^2}\,\delta^2+O_b(\delta^4).}
\]
The quadratic coefficient is positive on \((-1,-2/3)\cup(-1/3,0)\), negative on \((-2/3,-1/3)\), and vanishes exactly at \(b=-2/3\) and \(b=-1/3\). Hence infinitesimal drive heterogeneity changes the spectral threshold in opposite directions across **two exact sign reversals**. The zero coefficients at those two couplings do not assert equality of the full thresholds for nonzero mismatch.

## Assumptions and scope
The statement is local in mismatch for each **fixed** \(b\in(-1,0)\), and the neighborhood size may depend on \(b\). The map is defined on the full real plane; no positivity restriction on state coordinates is imposed. The condition \(\det D(F^2)=1\) is evaluated at the continued prime period-two orbit, not at a fixed point. The orbit is labeled only up to cyclic interchange. The trace inequality is strict locally because at zero mismatch it equals \(4b^2-2\in(-2,2)\). At the strong resonances \(b=-1/2\) and \(b=-1/\sqrt2\), the result concerns the unit-circle **spectral** boundary and does not assert an ordinary nonresonant Neimark–Sacker normal form. No assertion is made about a globally unique periodic orbit, stable invariant circle, or global attractor.

## Proof
Use center-difference coordinates \(u=(x+y)/2\), \(v=(x-y)/2\). The map is
\[
(u,v)\mapsto\bigl(a-u^2-v^2,\ \delta+2(b-u)v\bigr).
\]
For its nearby two-cycle write \((u_0,v_0)=(m+p,q+r)\) and \((u_1,v_1)=(m-p,q-r)\), with \((m,p,q,r)=(m_0,0,0,r_0)\) at the reference orbit. Adding and subtracting the four orbit equations gives the exact identities
\[
\begin{aligned}
a&=m+m^2+p^2+q^2+r^2,\\
(1-2m)p&=2qr,\\
(1+2(b-m))r&=2pq,\\
\delta&=(1-2(b-m))q+2pr.
\end{aligned}
\]
The one-step Jacobian in these coordinates is
\[
J(u,v)=\begin{pmatrix}-2u&-2v\\-2v&2(b-u)\end{pmatrix},
\qquad \det J(u,v)=4(u^2-bu-v^2).
\]
At the zero-mismatch orbit, direct multiplication yields
\[
\operatorname{tr}(J_1J_0)=4b^2-2,\qquad \det(J_1J_0)=1.
\]
Therefore \(1\) is not a multiplier of the second iterate for \(-1<b<0\). The analytic implicit-function theorem gives a unique continued two-cycle for \((a,\delta)\) near \((a_0,0)\). Along that continuation at \(\delta=0\), the explicit interchange orbit satisfies \(m=m_0\), \(p=q=0\), and \(r^2=a-m_0-m_0^2\). Hence
\[
\det(J_1J_0)=16\bigl(m_0^2-bm_0-r^2\bigr)^2,
\qquad \left.\frac{\partial}{\partial a}\det(J_1J_0)\right|_{a=a_0,\delta=0}=8.
\]
A second application of the implicit-function theorem constructs the unique analytic unit-circle parameter \(a_{\mathrm{uc}}(b,\delta)\), preserves the strict trace inequality and negative discriminant, and proves transverse crossing. Because the determinant increases strictly through one on this branch, the modulus of each complex multiplier crosses one from below to above. Exchange of the two coordinates conjugates mismatch \(\delta\) to \(-\delta\), while merely exchanging the two orbit points, so this threshold is even in \(\delta\).

For the exact curvature, the third orbit identity and the second identity imply
\[
z=1-2m,\qquad z^2+2bz-4q^2=0.
\]
Since \(b<0\) and \(z=-2b\) at \(q=0\), the relevant root and associated difference are
\[
z=-b+\sqrt{b^2+4q^2},\quad
m=b+\frac12+\frac{q^2}{b}+O_b(q^4),\quad
p=-\frac{qr_0}{b}+O_b(q^3).
\]
Write \(r^2=r_0^2+r_2q^2+O_b(q^4)\), where \(r_2\) is determined by the spectral condition. Define \(K_j=u_j^2-bu_j-v_j^2\) and \(\overline K=(K_0+K_1)/2\), \(\Delta K=(K_0-K_1)/2\). The exact determinant equation is \(16(\overline K^2-\Delta K^2)=1\). The preceding expansions give
\[
\begin{aligned}
\overline K&=-\frac14+\left(\frac1b+\frac{r_0^2}{b^2}-r_2\right)q^2+O_b(q^4),\\
\Delta K&=-\frac{r_0(3b+1)}b\,q+O_b(q^3).
\end{aligned}
\]
Consequently
\[
r_2=\frac1b+\frac{r_0^2}{b^2}+\frac{2r_0^2(3b+1)^2}{b^2}.
\]
Substitute into the exact formula for \(a\) to obtain
\[
a=a_0+\frac{(b+1)(3b+1)(3b+2)}{b^2}\,q^2+O_b(q^4).
\]
Finally the fourth orbit equation yields \(\delta=(b-1)q/b+O_b(q^3)\). Inverting gives \(q^2=b^2\delta^2/(b-1)^2+O_b(\delta^4)\), proving the boxed formula and its sharp sign partition.

## Verification
A standalone checker in `verify_curvature.py` tests all orbit/determinant identities symbolically and independently solves the five nonlinear orbit-plus-unit-determinant equations at high precision for three rational values of \(b\), including one from each curvature-sign phase. It compares measured quotients with the derived rational coefficient for two decreasing mismatch magnitudes. The actual script was executed successfully; these finite tests check algebra and numerics only, not the analytic implicit-function theorem or a global bifurcation classification.

## Relationship to prior work
Rech, Beims and Gallas (2004) found the exact equal-drive non-diagonal two-cycle and the unit-circle boundary \(a=a_0(b)\); their conclusion specifically identifies parameter mismatch as a further question. Rech, Beims and Gallas (2007), Section 4 and Appendix A, determine normal-form data and mode locking for the same **equal-drive** symmetric linear coupling; their distinct 'asymmetric coupling' model is not unequal quadratic drive in the present equations. Lloyd (1995) studies a different, post-map diffusive coupling of logistic maps. The present result gives a previously unreported perturbative coefficient and two coupling-dependent reversals for unequal drive, rather than rederiving the zero-mismatch formula.

## Limitations
This is a local spectral threshold result, not a proof of attracting invariant circles or any global phase diagram. The \(O_b\)-remainder is not uniform as \(b\) approaches \(-1\) or \(0\). Strong resonances require separate normal-form analysis. The quadratic correction vanishes at two exact couplings, where the fourth-order correction is not evaluated here. Although the inspected sources and research-record queries disclosed no implication covering this specific mismatch coefficient, unindexed historical treatments may exist and independent priority review is outstanding.

## References
1. P. C. Rech, M. W. Beims, J. A. C. Gallas, *Naimark–Sacker bifurcations in linearly coupled quadratic maps*, Physica A 342 (2004), 351–355; first available online 25 May 2004. DOI: 10.1016/j.physa.2004.04.105; preprint arXiv:nlin/0408010; author's authorized full text: https://inaesp.org/PublicJG/physicaA_neimark_rbg2004.pdf.
2. P. C. Rech, M. W. Beims, J. A. C. Gallas, *Generation of quasiperiodic oscillations in pairs of coupled maps*, Chaos, Solitons & Fractals 33 (2007), 1394–1410. DOI: 10.1016/j.chaos.2006.01.091; author's authorized full text: https://inaesp.org/PublicJG/rech_beims_gallas_SCF2007.pdf.
3. A. L. Lloyd, *The coupled logistic map: a simple model for the effects of spatial heterogeneity on population dynamics*, Journal of Theoretical Biology 173 (1995), 217–230. DOI: 10.1006/jtbi.1995.0058.
