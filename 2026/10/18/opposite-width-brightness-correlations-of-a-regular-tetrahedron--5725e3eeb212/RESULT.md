# Opposite width–brightness correlations of a regular tetrahedron and octahedron

## Finding

Let \(U\) be uniformly distributed on the Euclidean unit sphere \(S^2\). For any convex polytope \(K\subset\mathbb R^3\), put \(W_K(U)=h_K(U)+h_K(-U)\) (directional width) and \(B_K(U)=\operatorname{area}(\operatorname{proj}_{U^\perp}K)\) (orthogonal-projection brightness). Consider the regular octahedron and tetrahedron in the *same* Cartesian frame,
\[
O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\},\quad
T=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}.
\]
Let \(\theta=\arctan(1/\sqrt2)\) and
\[
\omega=2\arctan\!\left(\frac1{3+2\sqrt2+2\sqrt3+\sqrt6}\right).
\]
Then the two brightness functions are pointwise proportional, \(B_T(u)=2B_O(u)\) for **every** \(u\in S^2\); in particular their brightness divided by its own mean is the identical random variable for the same view. Nevertheless their *same-view* width–brightness covariances have **opposite signs**:
\[
\boxed{\begin{aligned}
\operatorname{Cov}(W_O,B_O)&=\frac23+\frac{4\sqrt2+8\omega-6\sqrt6\,\theta}{\pi}
=0.0206677304112\ldots>0,\\
\operatorname{Cov}(W_T,B_T)&=\frac83+\frac{8\sqrt6}{\pi}-\frac{12\sqrt6}{\pi}\left(\frac\pi2-\theta\right)
=-0.0340466592685\ldots<0.
\end{aligned}}
\]
This is an exact joint-statistic counterexample: proportional brightness profiles do not determine even the sign of a same-direction width–brightness correlation.

## Assumptions and scope

Both bodies are nondegenerate Euclidean convex polytopes with the coordinates given above; their edge lengths differ, so the numerical covariances use those specified unscaled representatives. The view \(U\) is Haar-uniform on \(S^2\); *the same* \(U\) defines width and brightness. Translations change neither variable. Uniform positive spatial rescaling of either body multiplies its covariance by the cube of the scale and therefore preserves its sign. The equality \(B_T=2B_O\) is pointwise under the displayed common orientation, not merely an equality in distribution.

## Proof

**Directional normal forms.** On a direction \(u\), let \(x\ge y\ge z\ge0\) be the ordered absolute Cartesian coordinates. The octahedron's support function is \(\max_i|u_i|=x\), whence \(W_O=2x\). The difference-body vertices of \(T\) are the coordinate permutations of \((0,\pm2,\pm2)\); hence \(W_T=2(x+y)\).

Every octahedral facet has area \(\sqrt3/2\) and its outward unit normal is one of the eight signed triples divided by \(\sqrt3\). Every tetrahedral facet has area \(2\sqrt3\) and its normal is one of four such sign triples, one from each antipodal pair. Cauchy's projection formula gives
\[
B_O(u)=\frac14\sum_{s\in\{-1,1\}^3}|s\cdot u|
=\max\{2x,x+y+z\},\qquad B_T(u)=2B_O(u).
\]
The last equality holds because the sum of absolute scalar products over four antipodal representatives is half the sum over all eight sign triples. Cauchy's mean projection formula, equivalently \(\mathbb E|\langle U,n\rangle|=1/2\), now yields \(\mathbb E B_O=\sqrt3\) and \(\mathbb E B_T=2\sqrt3\).

**Spherical-chamber integration.** The 48 signed order sectors are congruent. Let \(S=\{x\ge y\ge z\ge0:x^2+y^2+z^2=1\}\), of spherical area \(\pi/12\). Put
\[
a=(1,0,0),\quad b=(1,1,0)/\sqrt2,\quad
c=(2,1,1)/\sqrt6,\quad d=(1,1,1)/\sqrt3.
\]
The two subtriangles \(A=(a,b,c)\) and \(C=(b,d,c)\) triangulate \(S\), with \(x\ge y+z\) on \(A\) and \(x\le y+z\) on \(C\). The spherical area of \(A\) is exactly \(\omega\) by the determinant/solid-angle identity
\[
\operatorname{area}(p,q,r)=2\arctan\frac{|\det(p,q,r)|}{1+p\cdot q+q\cdot r+r\cdot p}
\]
for a positively oriented geodesic triangle of unit vertices.

For explicit and reproducible integration, let \(J_i(D)=\int_D u_i\,d\sigma\), \(J_{ij}(D)=\int_D u_iu_j\,d\sigma\) over such a spherical triangle \(D\). On its directed sides \(v\to w\), let \(\phi=\arccos(v\cdot w)\) and let \(n=-(v\times w)/\|v\times w\|\) be the outward tangent conormal. The side identities are
\[
\int_{v\to w}1\,ds=\phi,\qquad
\int_{v\to w}u\,ds=\tan(\phi/2)(v+w).
\]
Integrating \(\Delta_{S^2}u_i=-2u_i\) and \(\Delta_{S^2}(u_iu_j)=2\delta_{ij}-6u_iu_j\) by parts therefore gives the **exact finite boundary formulas**
\[
J_i(D)=-\frac12\sum_{v\to w}n_i\phi,\quad
J_{ij}(D)=\frac{\delta_{ij}}3\operatorname{area}(D)
-\frac16\sum_{v\to w}\left[n_i\tan(\phi/2)(v_j+w_j)+n_j\tan(\phi/2)(v_i+w_i)\right].
\]
Applying them to \(A,C,S\) and simplifying the square roots yields the four identities
\[
\begin{aligned}
\int_S x\,d\sigma&=\frac{\sqrt2}{4}\theta,&
\int_S(x+y)\,d\sigma&=\frac{\sqrt2}{4}\left(\frac\pi2-\theta\right),\\
4\int_A x^2\,d\sigma+2\int_C x(x+y+z)\,d\sigma
 &=\frac\pi{18}+\frac{\sqrt2}3+\frac{2\omega}3,&
8\int_A x(x+y)\,d\sigma+4\int_C (x+y)(x+y+z)\,d\sigma
 &=\frac{2\pi}9+\frac{2\sqrt6}3.
\end{aligned}
\]
These are purely elementary integrals: the accompanying `spherical_integrals_check.py` substitutes the displayed geodesic vertices into the boundary formulas and checks the algebraic reductions. In particular, \(\operatorname{area}(C)=\pi/12-\omega\) is used, as required by the exact triangulation.

A full-sphere average of an order-invariant integrand is \(12/\pi\) times its integral over \(S\). Combining the two piecewise brightness branches with the four identities gives
\[
\begin{aligned}
\mathbb E W_O&=\frac{6\sqrt2\,\theta}{\pi},&
\mathbb E(W_OB_O)&=\frac23+\frac{4\sqrt2+8\omega}{\pi},\\
\mathbb E W_T&=\frac{6\sqrt2}{\pi}\left(\frac\pi2-\theta\right),&
\mathbb E(W_TB_T)&=\frac83+\frac{8\sqrt6}{\pi}.
\end{aligned}
\]
Subtracting products of the means and using the previously computed mean brightness yields exactly the displayed covariance formulas.

**Strict signs.** The standalone standard-library checker `covariance_certificate.py` uses only rational arithmetic, exact integer-square-root brackets, and alternating power-series brackets for \(\arctan\). It derives \(\pi\) through the Machin identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\). With terminating rational bounds, it verifies the stronger strict rational inequalities
\[
\frac1{50}<\operatorname{Cov}(W_O,B_O)<\frac3{100},\qquad
-\frac4{100}<\operatorname{Cov}(W_T,B_T)<-\frac3{100}.
\]
Thus numerical rounding is not used to infer either sign.

## Verification

Execute `python covariance_certificate.py` (Python standard library) and `python spherical_integrals_check.py` (SymPy). Both scripts were run successfully. The first constructs certified intervals of widths less than \(5\times10^{-15}\) around both exact covariances and proves the strict rational sign bounds. The second recomputes all exact spherical triangle surface integrals from the boundary formulas. As an independent finite sanity check, sampling two million Gaussian-normalized uniform directions yielded approximately \(0.02068\) and \(-0.03408\) for the two covariances. Finite sampling is not a proof; the exact geodesic integrations and rational inequalities are.

## Relationship to prior work

Abas (2026, arXiv:2609.26202) studies the regular tetrahedron's **width law**, its **brightness law**, and polarized moments for zonoidal transforms; relevant mathematical sections of the complete manuscript were inspected. These univariate results and general moment mechanisms do not themselves give the claimed same-view tetrahedron–octahedron covariance sign contrast. Finch (2011, arXiv:1110.0671) concerns moments of *width alone*. Published geometric comparisons for orthotopes give width–brightness covariance formulas but do not apply to triangular-faced tetrahedra or octahedra. Another published calculation of the tetrahedron's area–perimeter shadow covariance studies two **planar projection** observables, whereas our first observable is the body's **line-projection width**. Published brightness-variance comparisons show the tetrahedron and octahedron have equal normalized brightness variance; that does not determine their distinct mixed covariances.

## Limitations

The sign reversal is established for this aligned regular tetrahedron–octahedron pair, not for arbitrary polyhedra or arbitrary rotations of one body relative to another. No full joint probability-density formula, universal covariance extremum, or reconstruction theorem is claimed. Accessible indexed and primary works did not reveal this exact sign comparison, but unindexed historical calculations remain a possible priority risk. The present verification is mathematical checking, not independent scientific audit or formal certification.

## References

1. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first public 2026-08-10, https://arxiv.org/abs/2609.26202 , especially §§4–6 and the full manuscript's searchable mathematical text.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public 2011-10-04, https://arxiv.org/abs/1110.0671 .
3. *Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes*, published record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-aspect-ratio-phase-diagram-for-width-brightness-covariance--ef50d44d3e36 .
4. *Exact orientation-variance spectrum of Platonic shadow areas*, published record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859 .
5. *Exact elliptic mixed shadow moment and negative covariance of a regular tetrahedron*, published record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-elliptic-mixed-shadow-moment-and-negative-covariance-of-a--6552ca8e2b99 .
