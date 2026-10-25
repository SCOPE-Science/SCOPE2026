# A sharp facet-to-vertex Hausdorff crossover in three-periodic Minkowski polygons

## Finding
Let \(N=3m\) with integer \(m\ge3\), put \(\delta=2\pi/N\), and let \(0\le t\le1\). There is a uniquely Steiner-centered convex polygon \(K_{N,t}\) whose outward normals are \(u_j=(\cos(j\delta),\sin(j\delta))\), with (possibly zero) facet lengths \(\ell_j=\delta(1-t)\) for \(j\equiv0\pmod3\), and \(\ell_j=\delta(1+t/2)\) otherwise. Its perimeter is \(2\pi\). Write
\[
A=\frac\delta2\cot\frac\delta2,\qquad L=\frac{\delta\sin\delta}{1+2\cos\delta},\qquad c=\cos\delta,\qquad a=A+Lt,\qquad b=A-\frac{Lt}{2}.
\]
Then the centered inradius and circumradius are **exactly**
\[
r(K_{N,t})=b,\qquad R(K_{N,t})=\frac{\sqrt{a^2+b^2-2cab}}{\sin\delta}.
\]
In particular, for the Euclidean unit disk \(B\),
\[
\boxed{d_H(K_{N,t},B)=\max\{1-b,\;R(K_{N,t})-1\}.}\tag{1}
\]
There exists a **unique** \(t_N\in(0,1)\) such that \(1-b\) is the larger term in (1) for \(0\le t<t_N\), the two terms agree for \(t=t_N\), and \(R-1\) is larger for \(t_N<t\le1\). It is an explicit algebraic-trigonometric root: set
\[
\begin{split}
C_0&=A^2\sec^2(\delta/2)-(2-A)^2,\\
C_1&=L\bigl(A/(1+c)-(2-A)\bigr),\\
C_2&=L^2(2+c)^2/[4(1-c^2)].
\end{split}
\]
Then \(C_0<0<C_2\) and
\[
\boxed{t_N=\frac{-C_1+\sqrt{C_1^2-4C_2C_0}}{2C_2}\in(0,1),\qquad
1-t_N=\frac{3\pi^2}{5N^2}+O(N^{-4}).}\tag{2}
\]
Let \(\rho_{N,t}\) be the normalized outward-facet surface-area measure and \(\nu_N\) the equal-weight measure on these \(N\) normal directions. For geodesic transportation on \(S^1\),
\[
\boxed{W_1(\rho_{N,t},\nu_N)=\frac{2\pi t}{3N}.}\tag{3}
\]
Nonetheless, **uniformly** for \(0\le t\le1\),
\[
\boxed{d_H(K_{N,t},B)=\frac{\pi^2(1+2t)}{3N^2}+O(N^{-4}).}\tag{4}
\]
Thus order-\(N^{-1}\) normal-measure transport can coexist with order-\(N^{-2}\) Hausdorff reconstruction; at the extreme zero-facet endpoint, the farthest vertices, rather than the nearest facets, dictate the exact Hausdorff error. Equation (2) quantifies the thin order-\(N^{-2}\) transition layer in the parameter.

## Assumptions and scope
Only Euclidean planar convex bodies and geodesic distance on the unit circle are considered. At \(t=1\), every third indicated facet has zero length and is omitted from the actual polygon; the remaining facet normals retain the cyclic ordering. All polygons are centered at their Steiner point, which coincides with the center of the nontrivial \(m\)-fold rotational symmetry. Inradius and circumradius here are those of concentric disks with center at the origin. Because of the symmetry, these are also the unconstrained extremal Euclidean radii. The expressions are valid for each integer \(N\ge9\) divisible by three and every real \(t\in[0,1]\). No perturbations outside this period-three family are included.

## Proof
**1. Construct and center the polygon.** The probability weights \(w_j=\ell_j/(2\pi)\) are nonnegative and sum to one. They obey \(\sum_j w_j u_j=0\), because each residue class modulo three consists of a regular \(m\)-point rotation orbit and \(m\ge3\). Minkowski's planar existence and uniqueness theorem gives the polygon, up to translation. Rotational symmetry by angle \(2\pi/m\) forces its Steiner point to be the origin. This also proves existence at \(t=1\) after deleting zero-length facets.

**2. Exact support distances.** For a convex polygon with consecutive outward normals separated by \(\delta\), the facet support distances \(r_j\) and lengths satisfy
\[
\ell_j=\frac{r_{j-1}+r_{j+1}-2\cos\delta\,r_j}{\sin\delta}.
\tag{5}
\]
To check (5), intersect the supporting lines adjacent to the line \(u_j\cdot x=r_j\) and subtract their tangential coordinates. Put \(\tau_j=-t\) for \(j\equiv0\pmod3\), and \(\tau_j=t/2\) for the other indices. Then \(\tau_{j-1}+\tau_{j+1}=-\tau_j\). Inserting \(r_j=A-L\tau_j\) into (5), using \(2(1-c)A/\sin\delta=\delta\) and \(L(1+2c)/\sin\delta=\delta\), recovers exactly \(\ell_j=\delta(1+\tau_j)\). Minkowski uniqueness and the common rotational center identify these distances with the actual polygon. The three support values are \(a,b,b\) in cyclic order. Consequently the smallest support value is \(b\).

**3. Exact vertex norm and Hausdorff error.** If adjacent support lines have normals at angular separation \(\delta\) and distances \(x,y\), their intersection has squared distance from the origin
\[
\frac{x^2+y^2-2cxy}{\sin^2\delta}.
\tag{6}
\]
The vertices are of cyclic types \((a,b)\), \((b,b)\), and \((b,a)\). For \(t>0\) the first and third have strictly larger radius than the second, since the difference of their squared radii equals \((a-b)(a+b-2cb)/\sin^2\delta>0\); equality holds at \(t=0\). This gives the stated \(R\). For a polygon containing the origin, the maximum of its support function is its greatest vertex radius, while its minimum is its smallest facet support. Since \(h_B\equiv1\) and Hausdorff distance equals the sup-norm of the difference of support functions, (1) follows.

**4. Unique sharp phase threshold.** Because \(b>0\) and \(2-b>0\), the signs of \(R+b-2\) and \(R^2-(2-b)^2\) agree. Direct substitution of \(a=A+Lt\) and \(b=A-Lt/2\) yields the exact quadratic identity
\[
R^2-(2-b)^2=C_0+C_1t+C_2t^2,\tag{7}
\]
with coefficients in (2). At \(t=0\), \(R+b=(\delta/2)\cot(\delta/4)<2\), using \(x\cot x<1\) for \(0<x<\pi/2\). Hence \(C_0<0\), and \(C_2>0\) directly.

At \(t=1\), all actual facets are tangent to the circle of radius \(b\), and their outward-normal gaps alternate between \(\delta\) and \(2\delta\). Their vertices have maximal radius \(R=b\sec\delta\). Summing tangent lengths along the \(2m\) actual facets gives
\[
b=\frac{3\delta}{2(\tan(\delta/2)+\tan\delta)}.
\]
Set \(z=\tan(\delta/2)\in(0,1)\). Elementary half-angle identities simplify
\[
b(1+\sec\delta)=\frac{3\delta}{z(3-z^2)}.
\]
This exceeds two precisely because \(\arctan z>z-z^3/3\). The difference vanishes at zero and has strictly positive derivative \(z^4/(1+z^2)\) for \(z>0\). Thus (7) is strictly positive at \(t=1\). A quadratic with negative constant coefficient and positive leading coefficient has exactly one positive real root; because the endpoint signs differ, that root lies in \((0,1)\). This proves (2) and the strict phase inequalities.

**5. The crossover boundary layer.** Expanding the analytic quantities for \(\delta\to0\) gives
\[
R^2-(2-b)^2\big|_{t=1}=\delta^4/20+O(\delta^6),\qquad
\partial_t\bigl(R^2-(2-b)^2\bigr)\big|_{t=1}=\delta^2/3+O(\delta^4).
\]
The second derivative of (7) is \(O(\delta^4)\). Taylor's formula at the root shows
\[
1-t_N=3\delta^2/20+O(\delta^4)=3\pi^2/(5N^2)+O(N^{-4}).
\]
The same Taylor expansions of \(A\), \(L\), and the vertex formula give, uniformly for \(0\le t\le1\),
\[
1-b=\delta^2(1/12+t/6)+O(\delta^4),\qquad
R-1\le\delta^2(1/12+t/6)+O(\delta^4).
\]
Combining with (1) and \(\delta=2\pi/N\) gives (4), including the endpoint.

**6. Exact transportation distance.** Relative to \(\nu_N\), at each index divisible by three the measure \(\rho_{N,t}\) has deficit \(t/N\); its two neighboring residue classes each have surplus \(t/(2N)\). Move each surplus mass one mesh step of length \(\delta\) to a nearest deficit node: this costs \(t\delta/3\). For the reverse inequality use the geodesic-distance-to-the-deficit-node-set function, which is \(1\)-Lipschitz, vanishes on all deficit nodes, and equals \(\delta\) at every surplus node. Kantorovich duality yields exactly \(t\delta/3\), proving (3).

## Verification
The accompanying dependency-free `verify.py` reconstructs every facet line and vertex independently from the support data for multiples of three up to \(120\), tests several values of \(t\), checks all facet lengths, the perimeter, the radii, and the zero of the exact quadratic. Its command is `python3 verify.py`, returning `VERIFY_OK 3105`. These are finite diagnostics, not substitutes for steps 1–6. The asymptotic coefficients follow from the displayed analytic identities, not from numerical fitting.

## Relationship to prior work
An's 2026 planar inverse-Minkowski work gives the exact regular-grid Hausdorff error and a general \(d_H\le\pi W_1\) estimate. Its regular-grid case is exactly \(t=0\) here; its general inequality only gives order \(N^{-1}\) for the present fixed-positive-\(t\) family and does not identify which geometric feature controls the error. The theorem here gives an exact signed-defect competition and a unique vertex-versus-facet crossover, including its order-\(N^{-2}\) boundary layer. An's earlier spherical-design work motivates the geometric focus on shape reconstruction and supplies the applicable primary MSC2020 field.

Published work on equiangular equal-area polygons identifies the *period-two* alternating-length edge class and its Euclidean area deficit. The present polygon has *period-three* lengths, with different endpoint normal gaps, and studies a distinct Hausdorff-to-disk extremum; that equal-area result does not imply the crossing coefficients in (2). The sharp Cauchy-quadrature result concerns optimal positive brightness samplers and centrally symmetric zonogons, not this three-periodic Minkowski support reconstruction. Comparisons are of the actual claims; they do not establish universal novelty.

## Limitations
The weights are constrained to one specific three-periodic family; arbitrary weighted grids may have different error rates. The leading quadratic approximation does not by itself reveal the narrow fourth-order transition. The result does not optimize over all perturbations with fixed transportation discrepancy. Independent expert validation has not been performed. There remains a possibility that an unindexed detailed calculation of periodically weighted Minkowski polygons gives the same crossover.

## References
1. C. An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1 (first public 12 August 2026), https://arxiv.org/abs/2608.11570.
2. C. An, *Gauss--Chebyshev Quadrature, Spherical Designs, and the Planar Minkowski Inverse Problem*, arXiv:2610.11814v1 (first public 8 October 2026), https://arxiv.org/html/2610.11814v1.
3. *Euclidean rigidity and exact area stability of equal-area equiangular polygons*, published mathematical record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-rigidity-and-exact-area-stability-of-equal-area-equian--311ac224be8e.
4. *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity*, published mathematical record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-n-direction-cauchy-quadrature-and-angular-rigidit--33b1062b46ae.
