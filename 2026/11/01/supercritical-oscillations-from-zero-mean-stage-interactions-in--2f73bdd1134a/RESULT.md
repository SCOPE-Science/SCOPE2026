# Supercritical oscillations from zero-mean stage interactions in a two-species community

## Finding
Consider two exchange-symmetric species, each with two life stages, governed by the quadratic demographic–interaction equations defined below. Although the four interspecies stage-interaction coefficients add to zero, a positive coexistence equilibrium loses stability through a **supercritical Hopf bifurcation** at the exact threshold \(w=2d+2\). For every \(u>2\) and \(d>u+2\), that equilibrium is locally exponentially attracting for \(0<w<2d+2\) and unstable for \(w>2d+2\). At the threshold the critical frequency is \(\Omega=\sqrt{u^2-4}\); with the explicitly specified canonical normalization, the first Lyapunov coefficient is
\[
\boxed{\ell_1=-\frac{du}{4(u+2)}<0.}
\]
Consequently, for all \(w>2d+2\) sufficiently close to the threshold, the **full four-dimensional system** has a locally unique (up to phase), strictly positive, exponentially orbitally attracting periodic orbit. It lies in the species-exchange fixed plane, has equal stage abundances across the two species, and persists under small symmetry-breaking perturbations. The result supplies an exact finite-demography oscillatory boundary which a zero-average, infinitely fast stage-aggregation limit cannot resolve.

## Assumptions and scope
Fix real constants \(u>2\), \(d>u+2\), and \(w>0\). For \(i\in\{1,2\}\), write \(j=3-i\) and let \(x_i(t)\), \(y_i(t)\) be the densities in stages one and two. Set
\[
R=\begin{pmatrix}2+u-d&d\\ d&2-u-d\end{pmatrix},\quad
H=\begin{pmatrix}-1&-1\\-1&-1\end{pmatrix},\quad
M=\begin{pmatrix}w/2&-u-w/2\\u-w/2&w/2\end{pmatrix}.
\]
With \(v_i=(x_i,y_i)^\mathsf T\), the autonomous ordinary differential equation is
\[
\dot v_i=Rv_i+\operatorname{diag}(v_i)(Hv_i+Mv_j),\qquad i=1,2.
\]
Equivalently,
\[
\begin{aligned}
\dot x_i&=(2+u-d)x_i+d y_i+x_i[-x_i-y_i+(w/2)x_j-(u+w/2)y_j],\\
\dot y_i&=d x_i+(2-u-d)y_i+y_i[-x_i-y_i+(u-w/2)x_j+(w/2)y_j].
\end{aligned}
\]
All intra-species same-stage and cross-stage competition coefficients are \(-1\), both linear stage-transfer rates are \(d>0\), and both direct stage-specific mortality coefficients are strictly negative, since \(d>u+2\). Each positive-coordinate face is inward pointing under stage transfer, so positivity is preserved as long as a solution exists. The interspecies stage matrix has zero aggregate interaction, \(\sum_{\alpha,\beta}M_{\alpha\beta}=0\), but its individual rows need not sum to zero. No stochastic covariance or Gaussian ensemble assumption is made.

## Proof
**1. Equilibrium and exchange reduction.** Let \(\mathbf1=(1,1)^\mathsf T\). Direct substitution gives \(R\mathbf1+H\mathbf1+M\mathbf1=0\). Hence \(E=(1,1,1,1)\) is a strictly positive equilibrium for every admissible \(w\). The exchange of the two species commutes with the vector field. Linearization at \(E\) therefore decomposes into its species-symmetric and species-antisymmetric two-dimensional blocks. Define \(\tau=w-2d-2\). In the stage coordinates, these blocks are
\[
J_+=\begin{pmatrix}\tau/2&-u-2-\tau/2\\u-2-\tau/2&\tau/2\end{pmatrix},\qquad
J_-=\begin{pmatrix}-2d-2-\tau/2&2d+u+\tau/2\\2d-u+\tau/2&-2d-2-\tau/2\end{pmatrix}.
\]
Their characteristic polynomials, with spectral parameter \(z\), are exactly
\[
\begin{aligned}
p_+(z)&=z^2-\tau z+u^2-4-2\tau,\\
p_-(z)&=z^2+(2d+2+w)z+(4d+2w+u^2).
\end{aligned}
\]
Because \(d,w,u>0\), the quadratic \(p_-\) is Hurwitz for all admissible parameters. For \(\tau<0\), the two coefficients following the leading coefficient of \(p_+\) are strictly positive, so \(E\) is hyperbolically attracting. For \(\tau>0\), \(\operatorname{tr}J_+=\tau>0\), so at least one eigenvalue has positive real part and \(E\) is unstable. This proves the **global-in-parameter local stability classification** (not a global-attraction claim).

**2. The nondegenerate Hopf point.** At \(\tau=0\), the symmetric block has simple eigenvalues \(\pm i\Omega\) with \(\Omega=\sqrt{u^2-4}>0\). Its eigenvalue real parts cross zero with derivative \(1/2\) as \(w\) increases through \(2d+2\). The other two eigenvalues are
\[
-2(d+1)\pm\sqrt{4d^2-u^2},
\]
strictly negative since \(d>u+2\). Thus the full system has exactly one simple critical conjugate pair and no other center directions.

**3. The cubic Hopf coefficient.** The invariant species-symmetric plane \(x_1=x_2=x\), \(y_1=y_2=y\) contains the critical eigenspace, and hence supplies a local center manifold at the threshold. With \(X=x-1\), \(Y=y-1\), the exact restricted equations at \(\tau=0\) are
\[
\begin{aligned}
\dot X&=-(u+2)Y+dX^2-(d+u+2)XY,\\
\dot Y&=(u-2)X+(u-d-2)XY+dY^2.
\end{aligned}
\]
Let \(A=u+2\), \(B=u-2\), \(\Omega=\sqrt{AB}\), and \(s=\Omega/A\). Using canonical coordinates \(h=X\), \(k=Y/s\), the linear part is \(\dot h=-\Omega k\), \(\dot k=\Omega h\). The quadratic terms are
\[
f(h,k)=d h^2-(d+A)s hk,\qquad
g(h,k)=(B-d)hk+d s k^2.
\]
For a quadratic planar field with this canonical linearization, its first Lyapunov coefficient in this normalization is
\[
\ell_1=\frac{f_{hk}(f_{hh}+f_{kk})-g_{hk}(g_{hh}+g_{kk})-f_{hh}g_{hh}+f_{kk}g_{kk}}{16\Omega},
\]
with derivatives evaluated at the origin (the usual cubic-derivative terms vanish). Substitution yields
\[
\ell_1=-\frac{2ds(A+B)}{16\Omega}=-\frac{du}{4(u+2)}<0.
\]
Since the crossing is transversal and the coefficient is negative, the Hopf theorem gives a supercritical family of attracting periodic solutions on the \(\tau>0\) side. At \(\tau=0\), the equilibrium is locally asymptotically stable but not exponentially stable. In the indicated canonical coordinates, the periodic solution's first-harmonic radius satisfies
\[
r(\tau)=\sqrt{\frac{2(u+2)\tau}{du}}+O(\tau),\qquad \tau\downarrow0,
\]
and its frequency is \(\Omega+O(\tau)\). The orbit is strictly positive for sufficiently small \(\tau>0\), since it approaches \(E\). The antisymmetric eigenvalues are strictly stable at the bifurcation and remain transverse stable along the small orbit; hence orbital attraction holds in all four variables, not merely in the invariant plane. A small perturbation breaking species-exchange symmetry preserves each nondegenerate attracting periodic orbit by hyperbolic periodic-orbit persistence (though it need not retain exact stage equality across species).

**4. Exact witness.** The admissible choice \(u=3\), \(d=6\), \(w=14\) has
\[
R=\begin{pmatrix}-1&6\\6&-7\end{pmatrix},\quad
M=\begin{pmatrix}7&-10\\-4&7\end{pmatrix},
\]
critical characteristic polynomial \((z^2+5)(z^2+28z+61)\) and \(\ell_1=-9/10\). The resulting attracting periodic branch occurs for \(w>14\) sufficiently near \(14\).

## Verification
The included standalone `verify_stage_hopf.py` checks symbolically the zero-mean identity, positivity-compatible demographic equilibrium, exact exchange-block Jacobians, both characteristic polynomials, nonlinear center-plane equations, the normalized Hopf coefficient, and the full four-dimensional characteristic factorization. It additionally checks the rational witness and twenty rational parameter cases. Run it with `python verify_stage_hopf.py` in an environment with Python 3 and SymPy. The checker verifies algebra but is not, by itself, a proof of the Hopf existence or infinite-range statements; those follow from the explicit sign inequalities and standard local Hopf and hyperbolic-persistence theorems above.

## Relationship to prior work
Garmire and O'Dwyer (2026, arXiv:2610.23557v1) derive a stage-structured generalized Lotka–Volterra framework, analyze random community stability, and emphasize the infinitely fast demographic limit. They discuss finite demographic speeds numerically. The present result uses their deterministic model class but replaces random interactions by a specifically constructed zero-aggregate matrix and obtains an exact finite-rate nonlinear stability boundary and an attracting-cycle branch. It does **not** change or contradict their random-ensemble threshold.

Giménez-Romero, Hernández, Genovart, and Salguero Gómez (2025) study community-matrix effects of stage-dependent interaction types. Their broad matrix framework does not, by itself, state the exact exchange-symmetric four-dimensional Hopf threshold or the nonlinear coefficient above. Ke and Nakazawa (2018) analyze a different one-consumer/two-resource ontogenetic antagonism–mutualism model; its accessible abstract does not imply this particular two-species, two-stage result. The general Hopf theorem and planar coefficient formula are standard tools, not claimed as new.

## Limitations
The theorem is local near a positive equilibrium, not a classification of all equilibria, all attractors, or global basins. The source-inspired stage matrix is a deterministic mixed-sign, zero-aggregate construction, **not** a typical member of the random equicorrelated ensemble. The periodic-orbit conclusion applies for sufficiently small positive distance from the Hopf threshold, not arbitrary larger forcing. The result gives no quantitative size for that neighborhood, nor ecological calibration. Existing literature could contain an equivalent parameterized example not located by the described comparisons; independent scientific review has not been performed.

## References
1. Grace Garmire and James P. O'Dwyer, *Heterogeneity among and competition between life stages together extend the stability boundary of complex ecological communities*, arXiv:2610.23557v1, first posted 2026-10-16. https://arxiv.org/abs/2610.23557
2. Àlex Giménez-Romero, Christina Hernández, Meritxell Genovart, and Roberto Salguero Gómez, *Population Structure Plays a Key Role in Community Stability*, Ecology Letters 28 (2025), e70272. https://doi.org/10.1111/ele.70272
3. Po-Ju Ke and Takefumi Nakazawa, *Ontogenetic antagonism–mutualism coupling: perspectives on resilience of stage-structured communities*, Oikos 127 (2018), 353–363. https://doi.org/10.1111/oik.04702
4. Yuri A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer, standard Hopf and first-Lyapunov-coefficient reference.
