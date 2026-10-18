# Asymmetric sharp endpoint tails of random regular-simplex brightness

## Finding
Let \(m\ge 3\) be an integer, \(\Delta_m=\operatorname{conv}\{e_1,\ldots,e_m\}\subset\mathbb R^m\), and let \(U\) be uniform on the unit sphere of \(H_0=\{u:\sum_i u_i=0\}\). The orthogonal projection of \(\Delta_m\) along \(U\) has \((m-2)\)-volume \(B(U)\). Put
\[
 k=m-2,\quad c_m=\frac{\sqrt m}{2(m-2)!},\quad Z=\frac{B(U)}{c_m}=\sum_{i=1}^m|U_i|,
 \quad p=\lfloor m/2\rfloor,\quad q=m-p,\quad L_m=2\sqrt{pq/m}.
\]
Thus \(\sqrt2\le Z\le L_m\). Write \(\sigma_k=2\pi^{(k+1)/2}/\Gamma((k+1)/2)\) for the area of the unit \(k\)-sphere and \(\kappa_k=\pi^{k/2}/\Gamma(1+k/2)\) for the volume of the unit \(k\)-ball. Then, as \(t\downarrow0\),
\[
 \Pr\{Z\le\sqrt2+t\}=\frac{m(m-1)2^k\sqrt{m/2}}{k!\,\sigma_k}t^k+O_m(t^{k+1}). \tag{1}
\]
Set \(N_m=\binom{m}{m/2}\) if \(m\) is even, and \(N_m=2\binom{m}{(m-1)/2}\) if \(m\) is odd. Then
\[
 \Pr\{Z\ge L_m-t\}=\frac{N_m\kappa_k}{\sigma_k}\left(\frac2{L_m}\right)^{k/2}t^{k/2}+O_m(t^{k/2+1}). \tag{2}
\]
Indeed the entire near-maximum law is an *exact* disjoint spherical-cap formula. Put
\[
 D_m=2\sqrt{\frac{\lfloor(m-1)/2\rfloor\lceil(m-1)/2\rceil}{m-1}},\qquad
 E_m=2\sqrt{\frac{(p-1)(q+1)}m},\qquad \delta_m=L_m-\max(D_m,E_m)>0.
\]
For every real \(0<t<\delta_m\),
\[
 \boxed{\displaystyle\Pr\{Z\ge L_m-t\}=\frac{N_m\int_0^{\arccos(1-t/L_m)}\sin^{k-1}s\,ds}{\int_0^\pi\sin^{k-1}s\,ds}.} \tag{3}
\]
For \(m=3\), (3) extends through the whole support and reads \(\Pr\{Z\ge z\}=(6/\pi)\arccos(z/\sqrt{8/3})\) for \(\sqrt2\le z\le\sqrt{8/3}\).

## Assumptions and scope
The simplex has edge length \(\sqrt2\); directions are uniformly sampled from the sphere in the simplex's \((m-1)\)-dimensional affine span, not from the ambient \(m\)-sphere. All bounds and constants are for this normalization. The endpoint asymptotics concern fixed integer \(m\), with the indicated remainder depending on \(m\). The direction \(U\) and \(-U\) induce the same projection, but we normalize probability on the full unit sphere; this does not double-count events.

## Proof
**Projection normalization and extrema.** The regular simplex has \(m\) congruent facets of \((m-2)\)-volume \(\sqrt{m-1}/(m-2)!\). Its unit facet normals in \(H_0\) are \((e_i-m^{-1}\boldsymbol 1)/\sqrt{(m-1)/m}\), up to sign. Cauchy's hyperplane projection formula therefore gives \(B(u)=c_m\sum_i|u_i|\). If positive coordinates sum to \(s\), then the negative coordinates sum to \(-s\), and \(\lVert u\rVert_2^2\le 2s^2\); hence \(Z=2s\ge\sqrt2\), with equality precisely at the \(m(m-1)\) ordered directions \((e_i-e_j)/\sqrt2\). On an orthant with \(r\) positive coordinates, \(1\le r\le m-1\), the linear functional \(Z\) is represented in \(H_0\) by the orthogonal projection of its sign vector and has norm \(2\sqrt{r(m-r)/m}\). Its unique maximizer in that orthant has constant positive coordinates and constant negative coordinates, and lies in the orthant's interior. Maximizing over \(r\) gives \(L_m\) and exactly \(N_m\) distinct maximizing directions (all balanced signs).

**Small-projection tail.** Fix a minimum \(v=(e_i-e_j)/\sqrt2\). For sufficiently small \(y\in\mathbb R^k\), use the orthogonal tangent vector \(w\in H_0\cap v^\perp\) with \(w_i=w_j=-\frac12\sum_{\ell\ne i,j}y_\ell\), \(w_\ell=y_\ell\) for other coordinates. Its Gram matrix in these \(y\)-coordinates is \(I_k+\frac12\boldsymbol1\boldsymbol1^{\mathsf T}\), of determinant \(m/2\). Parametrize the sphere near \(v\) by \(u=\sqrt{1-\lVert w\rVert^2}\,v+w\). As long as the original nonzero coordinate signs are unchanged,
\[
 Z(u)=\sqrt2\sqrt{1-\lVert w\rVert^2}+\sum_{\ell\ne i,j}|y_\ell|
 =\sqrt2+\lVert y\rVert_1+O_m(\lVert y\rVert_1^2).
\]
The induced sphere-area form is \(\sqrt{m/2}(1+O_m(\lVert y\rVert_1^2))\,dy\). For small \(t>0\), the sublevel \(Z\le\sqrt2+t\) about \(v\) is sandwiched between \(\ell_1\)-balls of radii \(t-O_m(t^2)\) and \(t+O_m(t^2)\). Each has leading area \(\sqrt{m/2}\,(2^k/k!)t^k+O_m(t^{k+1})\). Distinct minima have disjoint neighborhoods; compactness excludes other contributions for small \(t\). Divide by \(\sigma_k\) and multiply by \(m(m-1)\) to prove (1).

**Exact top cap and sharp top tail.** Within any orthant of balanced signs, let \(a\) be its unique unit maximizing direction. The orthant's sign functional is \(u\mapsto L_m\langle a,u\rangle\); hence inside it \(Z(u)=L_m\cos\angle(a,u)\). On a coordinate hyperplane \(u_j=0\), the remaining coordinates are zero-sum, unit length, and their absolute sum is at most \(D_m\): this is the balanced sign maximum in \(m-1\) coordinates. Moreover every unbalanced orthant has maximum at most \(E_m\); if \(m=3\) the right side is \(0\), representing the absence of other sign splits. Hence \(Z>L_m-t>\max(D_m,E_m)\) forces one of the balanced orthants, and the entire radius-\(\arccos(1-t/L_m)\) spherical cap about its maximizer remains inside that orthant. To see the latter, a geodesic from the maximizer leaving its orthant would cross its boundary at a smaller geodesic distance, where the sign functional (and thus \(Z\)) exceeds \(L_m-t\), contradicting the boundary bound \(D_m\). These \(N_m\) caps are disjoint. A single cap on \(S^k\) occupies proportion \(\int_0^\theta\sin^{k-1}s\,ds /\int_0^\pi\sin^{k-1}s\,ds\), proving (3). The local expansion \(\int_0^\theta\sin^{k-1}s\,ds=\theta^k/k+O_k(\theta^{k+2})\), with \(\theta=\sqrt{2t/L_m}+O_m(t^{3/2})\), gives (2). For \(m=3\), \(D_3=\sqrt2\), the entire support is covered by the six equal caps without overlap, giving the stated closed distribution.

## Verification
The self-contained `check_brightness.py` checks the exact cap formula against seeded spherical sampling in several dimensions and tests the endpoint coefficient asymptotics. The proof of all-dimensional assertions is analytical; simulations verify only finite instances and are not used to infer infinitary claims. To run: `python check_brightness.py` (requires NumPy and SciPy).

## Relationship to prior work
The Cauchy projection formula and the extremal values/directions of the regular simplex are **prior results**, not contributions claimed here. Filliman (1990) studied extreme projections; Pandis (2026, arXiv:2601.18436) provides the precise simplex hyperplane-projection formula and extremizers. Kabluchko, Litvak and Zaporozhets (2015, arXiv:1511.08479) establish stochastic results for *one-dimensional* widths of regular polytopes, whereas the present statistic is the volume of a *codimension-one* projection. The assessed addition is the all-dimensional probability behavior at both endpoints: an exact upper cap-law window and two different sharp power-law exponents and constants. The fact that the base formula enables further analysis does not itself establish the endpoint laws in these sources.

## Limitations
The result is restricted to regular simplices, Haar viewing directions, and fixed-dimensional endpoint asymptotics. It does not provide the complete brightness law in dimension \(m\ge4\), an approximation uniform as \(m\to\infty\), or error guarantees under observational noise. Similar results may exist in older literature under spherical \(\ell_1\)-section or projection-body terminology; an inaccessible plausible historical source remains a priority risk.

## References
- D. Filliman, *The extreme projections of the regular simplex*, Transactions of the American Mathematical Society (1990), DOI 10.1090/S0002-9947-1990-0989573-6 (abstract examined, complete article unavailable).
- Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, originally public 2015-11-26 (full text examined).
- C. Pandis, *On Extremal Volume Projections of the Simplex and the Cube*, arXiv:2601.18436, originally public 2026-01-26 (full text examined).
