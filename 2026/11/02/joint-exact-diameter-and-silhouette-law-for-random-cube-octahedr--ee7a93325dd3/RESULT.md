# Joint exact diameter and silhouette law for random cube–octahedron shadows

## Finding
Let \(Q=[-1/2,1/2]^3\) be the unit-edge cube and let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\) be its regular cross-polytope counterpart. Choose an unoriented plane \(E\) uniformly with respect to Haar measure on \(\operatorname{Gr}(2,3)\). Denote by \(D\) the Euclidean diameter of the orthogonal projection \(P_EQ\), and by \(N\) the number of vertices of the orthogonal projection \(P_EO\).

Define the signed random variable \(L\) by sorting the absolute components of a unit normal \(u\) as \(a\ge b\ge c\ge0\) and setting \(L=a-b-c\). Put \(t_*=1/\sqrt3\). Then, outside measure-zero degeneracies,
\[
\boxed{D=\sqrt{3-L^2},\qquad N=4\ \text{if }L>0,\quad N=6\ \text{if }L<0.}
\]
The signed slack \(L\) has **the following exact elementary probability density** on \([-t_*,1]\):
\[
\boxed{f_L(\ell)=\frac{12}{\pi\sqrt3}
\begin{cases}
\displaystyle\arccos\!\left(\frac{3\sqrt{1-\ell^2}-\sqrt2\ell}{2\sqrt{3-\ell^2}}\right),&-t_*\le\ell<0,\\[6pt]
\displaystyle\arccos\!\left(\frac{3\sqrt{2-\ell^2}+\ell}{2\sqrt{2(3-\ell^2)}}\right),&0\le\ell\le1,\\
0,&\text{otherwise}.
\end{cases}}
\]
At \(\ell=0\) both branches equal \(2/\sqrt3\). Define \(t(d)=\sqrt{3-d^2}\). The **complete joint law** for \(\sqrt2<d<\sqrt3\) is
\[
\boxed{\frac{\Pr\{D\in\mathrm{d}d,N=4\}}{\mathrm{d}d}
=\frac{d}{t(d)}f_L(t(d)),}
\]
whereas
\[
\boxed{\frac{\Pr\{D\in\mathrm{d}d,N=6\}}{\mathrm{d}d}
=\begin{cases}
0,&\sqrt2<d<\sqrt{8/3},\\
\displaystyle\frac{d}{t(d)}f_L(-t(d)),&\sqrt{8/3}<d<\sqrt3.
\end{cases}}
\]
These two densities, integrated over an interval, determine every joint and conditional probability. No atoms occur. In particular \(D\in[\sqrt2,\sqrt3]\) and a six-vertex octahedral shadow forces \(D\ge\sqrt{8/3}\), with both support boundaries sharp. The known hexagonal-shadow probability is recovered as
\[
\Pr(N=6)=\frac6\pi\arccos(1/3)-2=\frac4\pi\arctan(\sqrt2/5).
\]
The exact new joint distribution also gives three sharp endpoint laws, as \(\varepsilon\downarrow0\):
\[
\boxed{\begin{aligned}
\Pr(D\le\sqrt2+\varepsilon)&\sim\frac6\pi\varepsilon^2,\\
\Pr(N=6,\ D\le\sqrt{8/3}+\varepsilon)&\sim\frac{18\sqrt3}{\pi}\varepsilon^2,\\
\Pr(D\ge\sqrt3-\varepsilon)&\sim4\sqrt{\frac2{\sqrt3}}\,\sqrt\varepsilon.
\end{aligned}}
\]
More precisely, \(f_L(-t)\sim\frac{9\sqrt3}{2\pi}(t_*-t)\) as \(t\uparrow t_*\). Thus the density of \(|L|\) is continuous but has a first-derivative jump of \(9\sqrt3/(2\pi)\) at \(t_*\); the transition is the appearance of the six-vertex component, not a probability atom.

## Assumptions and scope
All distances use the ambient Euclidean metric. The cube's edge length is one; its centered position is immaterial for diameter. The octahedron has vertices \(\pm e_i\), so its vertex count refers to the *same* randomly chosen plane as the cube shadow. Haar-random means the plane normal can be represented by a uniformly random point of \(S^2\), with opposite normals identified. Endpoints and ties have spherical measure zero. The asserted law is joint, not a product of independent marginals. The density is with respect to ordinary one-dimensional Lebesgue measure.

## Proof
**1. Deterministic diameter reduction.** Distances between projected cube vertices attain the shadow's diameter. Differences of unit-cube vertices belong to \(\{-1,0,1\}^3\). For a difference vector \(v\), the projected squared distance is \(\|v\|_2^2-(v\cdot u)^2\). If \(v_j=0\), changing this coordinate to \(\sigma\in\{-1,1\}\) with \(\sigma n_j(v\cdot u)\le0\) changes the squared distance by
\[
1-u_j^2+2|u_j(v\cdot u)|\ge0.
\]
One can therefore extend every candidate to a signed body diagonal without decreasing its projected length. Thus
\[
D^2=3-\min_{\sigma_i\in\{-1,1\}}(\sigma_1u_1+\sigma_2u_2+\sigma_3u_3)^2.
\]
After taking absolute values and ordering \(a\ge b\ge c\), the least absolute signed sum is \(|a-b-c|\). Indeed the other essentially different sums are \(a-b+c\), \(a+b-c\), and \(a+b+c\); all have absolute values at least \(|a-b-c|\), using \(a\ge b\ge c\). This proves \(D^2=3-L^2\).

**2. Octahedral silhouette.** Put \(q_i=P_Ee_i\). These three planar vectors span \(E\) outside null degeneracies and satisfy \(u_1q_1+u_2q_2+u_3q_3=0\). The pair \(\pm q_i\) is redundant precisely when it lies in \(\operatorname{conv}\{\pm q_j,\pm q_k\}\). Expressing \(q_i\) in the basis \((q_j,q_k)\) shows redundancy exactly when \(|u_i|\ge|u_j|+|u_k|\). Since at most one of these inequalities can hold strictly, \(P_EO\) is a quadrilateral if \(a>b+c\) and a hexagon if \(a<b+c\). This is the asserted sign classification.

**3. Spherical fundamental chamber and coarea.** Except on great circles, \(S^2\) is partitioned into 48 sign-and-coordinate-order chambers of equal area. Consider
\[
T=\{(a,b,c)\in S^2:a\ge b\ge c\ge0\}.
\]
Its vertices are \(A=(1,0,0)\), \(B=(1,1,0)/\sqrt2\), and \(C=(1,1,1)/\sqrt3\). The linear functional \(L(a,b,c)=a-b-c\) has values \(1,0,-t_*\) at these vertices and has no stationary point in the relative interior. Along the three edges the values vary monotonically. Each intermediate level therefore cuts \(T\) in exactly one circular arc: between \(AB\) and \(AC\) for \(\ell>0\), or between \(BC\) and \(AC\) for \(\ell<0\).

Write \(w=(1,-1,-1)\) so \(L=w\cdot u\), with \(\|w\|=\sqrt3\). Around the polar axis \(w/\sqrt3\), the spherical area element is \(\mathrm{d}\phi\,\mathrm{d}(\ell/\sqrt3)\). If \(\alpha(\ell)\) denotes the angular span of the level arc, the 48 chambers yield the density \(f_L(\ell)=12\alpha(\ell)/(\pi\sqrt3)\).

**4. Computing the arc endpoints.** On edge \(AC\), put \(s=\sqrt{(3-\ell^2)/2}\). Its level endpoint is
\[
P(\ell)=\left(\frac{\ell+2s}{3},\frac{s-\ell}{3},\frac{s-\ell}{3}\right).
\]
For \(0\le\ell\le1\), the second endpoint is on \(AB\):
\[
Q_+(\ell)=\left(\frac{\sqrt{2-\ell^2}+\ell}{2},\frac{\sqrt{2-\ell^2}-\ell}{2},0\right).
\]
For \(-t_*\le\ell\le0\), it is on \(BC\):
\[
Q_-(\ell)=\left(\sqrt{\frac{1-\ell^2}{2}},\sqrt{\frac{1-\ell^2}{2}},-\ell\right).
\]
All these endpoints are unit vectors satisfying \(w\cdot P=w\cdot Q=\ell\). Their azimuthal angle around \(w\) is therefore
\[
\alpha(\ell)=\arccos\!\left(\frac{P(\ell)\cdot Q_{\pm}(\ell)-\ell^2/3}{1-\ell^2/3}\right).
\]
The arc is the short azimuthal arc inside the convex spherical chamber; its span is below \(\pi\). Direct substitution simplifies the cosine to the two algebraic functions in the displayed density. Integrating the resulting density over \([-t_*,1]\) gives one because the 48 chambers partition the unit sphere. The map \(\ell\mapsto\sqrt{3-\ell^2}\) has two smooth inverse branches away from \(\ell=0\). Their Jacobian is \(d/\sqrt{3-d^2}\), proving both joint density formulas.

**5. Sharp supports, transition, and endpoint orders.** The signed slack ranges from \(-t_*\) at \(C\) to \(1\) at \(A\). Its zero is achieved on a smooth internal level curve, so \(D\) has the claimed support. The six-vertex regime \(L<0\) has \(|L|<t_*\), giving its sharp lower diameter \(\sqrt{3-t_*^2}=\sqrt{8/3}\).

For completeness, differentiation of the endpoint expressions at \(\ell=1\) gives \(P'(1)=(0,-1/2,-1/2)\) and \(Q_+'(1)=(0,-1,0)\). Their derivative separation has norm \(1/\sqrt2\), while the level-circle radius is \(\sqrt{2/3}\). At \(\ell=-t_*\), the derivatives are \(P'(-t_*)=(1/2,-1/4,-1/4)\) and \(Q_-'(-t_*)=(1/2,1/2,-1)\), with separation norm \(3\sqrt2/4\) and level-circle radius \(2\sqrt2/3\). Hence the angular spans grow linearly with respective coefficients \(\sqrt3/2\) and \(9/8\). Consequently \(f_L(1-\delta)\sim(6/\pi)\delta\) and \(f_L(-t_*+\delta)\sim(9\sqrt3/(2\pi))\delta\). At zero, the two branches agree with \(f_L(0)=2/\sqrt3\). Integrating at each endpoint gives the first and third displayed probability asymptotics. For the six-vertex onset, \(\sqrt{3-(\sqrt{8/3}+\varepsilon)^2}=t_*-2\sqrt2\varepsilon+O(\varepsilon^2)\); integration of the negative-end linear density gives \((18\sqrt3/\pi)\varepsilon^2\). All constants are strictly positive. The negative branch contributes \((9\sqrt3/(2\pi))(t_*-t)+o(t_*-t)\) as \(t\uparrow t_*\), proving the stated derivative jump.

**6. Known hexagonal probability as a check.** In a fixed positive coordinate octant, \(N=6\) is the spherical triangle generated by \((1,1,0)\), \((1,0,1)\), and \((0,1,1)\). Its side lengths are \(\pi/3\); each spherical interior angle is \(\arccos(1/3)\). Girard's theorem gives area \(3\arccos(1/3)-\pi\). Divide by the octant area \(\pi/2\) to obtain \(\Pr(N=6)=6\arccos(1/3)/\pi-2\). The equivalent arctangent expression follows from the spherical-triangle half-angle identity. This probability is previously known; only its embedding in the complete joint law is used here.

Finally, polarity within \(E\) gives \((P_EQ)^\circ=2(O\cap E)\). Because \(P_EQ\) is centrally symmetric, its circumradius is \(D/2\), and the centered inradius of \(O\cap E\) equals \(1/D\). Hence the new diameter law is equivalently an exact random **inradius-of-section** law, not an inradius-of-projection or diameter-of-section law. \(\square\)

## Verification
Run `python3 verify.py` with standard Python 3 from the directory containing this file and the accompanying checker. The checker independently enumerates all projected cube-vertex pair distances and constructs each planar octahedron convex hull for 1600 seeded Haar-random normals; verifies the two density integrals and the classical hexagonal probability; compares seven CDF thresholds with 160000 independently sampled Gaussian normals; and checks sharp endpoint constants by numerical integration. A successful run prints `ALL_CHECKS_PASSED`. Finite sampling does not prove the density or endpoint asymptotics: the analytic chamber/coarea calculation above does.

## Relationship to prior work
Kabluchko, Prochno, and Thäle [1] investigate Haar random projections of cubes in high-dimensional limits and their projected mass/vertices; their 2019 full text treats \(n\to\infty\), not the fixed three-dimensional joint diameter–silhouette law. Lonke [2] studies whether cube vertices project into a central section; the full note gives a criterion involving the product of the \(\ell_1\)- and \(\ell_\infty\)-norms, not a diameter distribution. Black and Criado [3] bound the expected number of shadow vertices for fixed polytopes; the inspected main theorems concern estimates in terms of geometric diameter, edge lengths, and normal-cone parameters, not the distribution of the *shadow diameter*.

For exact close comparisons, a published 2026 result [4] determines the **diameter of random central sections of the octahedron**, equivalent by polarity to the inradius of random *cube projections*. Another [5] determines the inradius of random *octahedron projections*, equivalent to circumradii of cube sections. Neither is the **inradius of octahedron sections**, equivalently the diameter of cube projections, derived here. A further result [6] proves the exact *marginal* probability that an octahedral shadow is hexagonal and its sharp triaxial shape optimization; that probability is credited and recovered above, but it does not give the continuous diameter law conditional on vertex type. These geometric distinctions are essential: exchanging section with projection or diameter with inradius does not preserve these laws. No claim of exhaustive historical priority is made.

## Limitations
The formulas are for the regular three-dimensional cube–octahedron pair, the same uniform random plane, and Euclidean orthogonal projections. They do not assert an analogous density for unequal orthotopes, higher dimensions, random affine sections, or a joint law involving shadow area. The inverse-cosine expressions rely on the small 48-chamber spherical arrangement. An equivalent formula may exist in unindexed spherical-order-statistic or stereological literature; independent mathematical audit has not been performed.

## References
1. Z. Kabluchko, J. Prochno, C. Thäle, *A new look at random projections of the cube and general product measures*, arXiv:1910.02676, first posted 2019-10-07, https://arxiv.org/abs/1910.02676.
2. Y. Lonke, *Shadows of cube vertices*, arXiv:2010.05758, first posted 2020-10-08, full text https://arxiv.org/html/2010.05758v1.
3. A. E. Black, F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first posted 2024-06-11, full text https://arxiv.org/html/2406.06936v1.
4. *Exact Haar diameter law for central sections of the regular octahedron*, published published-finding corpus record 2026/10/11, identifier 4948185eba2f.
5. *Exact inradius law for random planar projections of the regular octahedron*, published published-finding corpus record 2026/10/11, identifier 5fbcddcea5e5.
6. *Sharp triaxial octahedron shadow bound and quadratic shape stability*, published published-finding corpus record 2026/10/11, identifier c544249c351b.
