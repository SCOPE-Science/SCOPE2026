# Exact short-geodesic-distance law on convex polyhedral surfaces

## Finding
Let \(S\) be the boundary of any nondegenerate convex polyhedron in \(\mathbb R^3\), with intrinsic shortest-path distance \(d_S\) and surface area \(A\). At each vertex \(v\), let \(\alpha_v\in(0,2\pi)\) be the sum of its incident planar face angles. For independent surface-area-uniform points \(X,Y\), there exists \(r_0(S)>0\) such that for **every** \(0<r<r_0(S)\),
\[
\Pr(d_S(X,Y)\le r)=\frac{\pi r^2}{A}-\frac{r^4}{8A^2}\sum_v\alpha_v\left[\cot\frac{\alpha_v}{2}+\frac{\pi-\alpha_v/2}{\sin^2(\alpha_v/2)}\right].
\]
The formula is exactly quartic on a nonempty interval, rather than an asymptotic expansion. Its coefficient detects nonlinear concentration of vertex curvature, not merely the total angular deficit. In particular, the unit-edge regular tetrahedron (surface area \(\sqrt3\), four cone angles \(\pi\)) obeys
\[
\Pr(d_S(X,Y)\le r)=\frac{\pi r^2}{\sqrt3}-\frac{\pi^2r^4}{12}
\]
for all sufficiently small positive \(r\).

## Assumptions and scope
The polyhedron is fixed, compact, convex, three-dimensional and nondegenerate; intrinsic surface distance is the infimum of lengths of paths **on its surface**. The law is for two independent points sampled by normalized two-dimensional surface-area measure, not for Euclidean chords or Euclidean distances between the sampled points. Adjacent planar faces unfold isometrically across their shared edges: only vertices are intrinsic metric singularities. Each vertex has positive cone angle strictly below \(2\pi\).

## Proof
Define the cone correction
\[
F(\alpha)=-\frac{\alpha}{8}\left[\cot\frac\alpha2+\frac{\pi-\alpha/2}{\sin^2(\alpha/2)}\right],\qquad 0<\alpha<2\pi.
\]
Fix a vertex and unfold its incident faces to a Euclidean cone of angle \(\alpha\). Write two points in polar cone coordinates as \((t,\theta)\) and \((s,\eta)\). Their minimal circular angular separation is \(\delta\in[0,\alpha/2]\subset[0,\pi)\); within a sufficiently small cone neighborhood their intrinsic distance satisfies
\[
d^2=t^2+s^2-2ts\cos\delta.
\]
For \(t,s>0\), put
\[
\beta(t,s;r)=\arccos\left(\operatorname{clip}_{[-1,1]}\frac{t^2+s^2-r^2}{2ts}\right).
\]
The accessible angular measure at radius \(s\) for a center at radius \(t\) is \(2\min\{\beta,\alpha/2\}\) on the cone, versus \(2\beta\) in a Euclidean plane. When integrating the area of radius-\(r\) balls over centers, the **difference** from the flat baseline is therefore
\[
\Delta_\alpha(r)=-2\alpha\int_0^\infty\!\int_0^\infty ts\,[\beta(t,s;r)-\alpha/2]_+\,ds\,dt.
\]
Only radii \(t,s=O_\alpha(r)\) contribute, so this expression is valid inside a sufficiently small finite cone neighborhood. Since
\([\beta-\alpha/2]_+=\int_{\alpha/2}^{\pi}\mathbf1_{\{\beta>\phi\}}\,d\phi\),
rescaling both radii gives
\[
\Delta_\alpha(r)=-2\alpha r^4\int_{\alpha/2}^{\pi}J(\phi)\,d\phi,
\quad
J(\phi)=\int_{\substack{t,s\ge0\\t^2+s^2-2ts\cos\phi\le1}}ts\,dt\,ds.
\]
Putting \(t=R\cos\psi\) and \(s=R\sin\psi\) and integrating in \(R\), followed by \(u=\pi/2-2\psi\) on the two symmetric halves, yields
\[
J(\phi)=\frac18\int_0^{\pi/2}\frac{\cos u}{(1-\cos\phi\cos u)^2}\,du.
\]
For \(0<\phi<\pi\), the elementary integral
\(\int_0^{\pi/2}(1-\cos\phi\cos u)^{-1}du=(\pi-\phi)/\sin\phi\)
may be differentiated with respect to \(\cos\phi\), giving
\[
J(\phi)=\frac18\left[\frac1{\sin^2\phi}+\frac{(\pi-\phi)\cos\phi}{\sin^3\phi}\right].
\]
Consequently, using the continuous limit at \(\phi=\pi\),
\[
\int_{\alpha/2}^{\pi}J(\phi)d\phi
=\frac1{16}\left[\cot\frac\alpha2+\frac{\pi-\alpha/2}{\sin^2(\alpha/2)}\right],
\]
and therefore \(\Delta_\alpha(r)=F(\alpha)r^4\).

To pass from local cones to the compact surface, choose pairwise disjoint intrinsic cone neighborhoods around the finitely many vertices. For all sufficiently small \(r\), a shortest path of length at most \(r\) intersecting a vertex neighborhood cannot encounter any other vertex neighborhood or leave the local cone chart. Outside fixed smaller cone neighborhoods, geodesic disks of sufficiently small radius are isometric to flat Euclidean disks, including when they cross edges. By shrinking \(r_0\) further, every nonflat contribution to the double area integral is supported in the corresponding isolated \(O(r)\) vertex neighborhood, where the preceding scale-invariant cone calculation applies without truncation. Hence
\[
\int_S \operatorname{area}\big(B_S(x,r)\big)\,dA(x)
=A\pi r^2+r^4\sum_vF(\alpha_v)
\]
for \(0<r<r_0\). Division by \(A^2\) proves the probability formula.

For comparison, a cube has eight cone angles \(3\pi/2\) and correction sum \(3\pi/2-3\pi^2/4\), whereas a tetrahedron has four cone angles \(\pi\) and correction sum \(-\pi^2/4\). These differ despite the common total angular defect \(4\pi\), demonstrating that the coefficient is not determined by Gauss--Bonnet alone.

## Verification
The included `check_cone_distance.py` computes the coefficient in two mathematically different forms: the exact cotangent expression and nested numerical integration of the radial-angular cone integral. It checks a range of cone angles as well as the independent half-turn quotient construction at cone angle \(\pi\). The exact tetrahedral specialization follows by direct substitution. The analytic calculation above, not numerical quadrature, establishes the continuum statement.

## Relationship to prior work
Wenk and Cook's 2009 treatment of shortest paths on polyhedral surfaces supplies background on the intrinsic metric and its algorithms, but its inspected introductory results, shortest-path section and document-wide searches do not supply a law for the distribution of surface-point geodesic distances. Mathai, Moschopoulos and Pederzoli's 1999 article treats distances between sampled points on or inside a cube in the Euclidean setting; its accessible abstract does not establish this *intrinsic cone-angle* formula. A related published finding on planar polygons concerns Euclidean distances of points in a flat two-dimensional interior, rather than intrinsic distances between points on closed polyhedral surfaces. None of those distinctions alone certifies comprehensive historical priority.

## Limitations
The radius threshold \(r_0\) depends on the polyhedron; the formula does not determine the distribution at arbitrary distances. The proof requires finitely many convex cone singularities with angles below \(2\pi\). It does not directly treat smooth curved surfaces, nonconvex vertex cones, or nonsurface sampling. The 1999 cube article was examined at abstract level only, so prior literature may contain related special cases. Independent mathematical validation has not been performed.

## References
- C. Wenk and A. Cook, *Shortest Path Problems on a Polyhedral Surface*, Dagstuhl Seminar Proceedings 09111 (2009), DOI: 10.4230/DagSemProc.09111.5. First public date verified 2009-06-23.
- A. M. Mathai, P. G. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, *Statistica* 59(1) (1999), 61–81, DOI: 10.6092/issn.1973-2201/1104. Only abstract and bibliographic material checked.
