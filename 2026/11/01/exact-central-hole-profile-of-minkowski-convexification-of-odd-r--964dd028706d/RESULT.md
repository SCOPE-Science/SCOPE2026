# Exact central-hole profile of Minkowski convexification of odd regular polygon vertex sets

## Finding
Let \(m\ge5\) be odd, let \(P_m\) be the regular Euclidean \(m\)-gon of circumradius one centered at the origin, and let \(V_m\) be its vertex set. Set \(\theta=\pi/m\) and \(c=\cos\theta\). The union of its vertex translates by a dilated copy,
\[
U_t=V_m+tP_m=\bigcup_{v\in V_m}(v+tP_m),
\]
has an exact one-hole description for every \(1\le t<\sec\theta\):
\[
U_t=(1+t)P_m\setminus\operatorname{int}Q_t,\qquad
Q_t=\bigcap_{v\in V_m}\{x:\langle x,v\rangle\le1-tc\}.
\]
Here \(Q_t\) is the concentric regular \(m\)-gon whose facet normals are the vertex directions of \(P_m\), with inradius \(1-tc\). Its boundary belongs to \(U_t\). At \(t=\sec\theta\), the hole collapses to the origin and \(U_t=(1+t)P_m\); this equality persists for larger \(t\). For \(0\le t<1\), the union is not convex. Consequently, the exact Schneider convexification index of the discrete vertex set is
\[
c(V_m)=\sec(\pi/m),\qquad \lambda(P_m)=\frac{1}{1+\sec(\pi/m)}.
\]
The missing area, for all \(1\le t\le\sec\theta\), is
\[
\Delta_m(t)=\operatorname{area}((1+t)P_m)-\operatorname{area}(U_t)
=m(1-tc)^2\tan\theta.
\]
Its fractional form is the exact quadratic law
\[
\frac{\Delta_m(t)}{\operatorname{area}((1+t)P_m)}
=\left(\frac{\sec\theta-t}{1+t}\right)^2.
\]
In particular, for \(t=1\), the fractional uncovered area is asymptotic to \(\pi^4/(16m^4)\), while the absolute uncovered area is asymptotic to \(\pi^5/(4m^4)\) as odd \(m\) tends to infinity.

## Assumptions and scope
The vertices are \(v_j=(\cos(2\pi j/m),\sin(2\pi j/m))\) for \(0\le j<m\). Minkowski addition is set-theoretic: \(A+B=\{a+b:a\in A,b\in B\}\). The polygon \(P_m=\operatorname{conv}V_m\) is closed. The set \(U_t\) is a finite union of closed polygons. Its missing-area function is taken relative to \((1+t)P_m\), not to a fixed unscaled polygon. The theorem concerns odd orders at least five, and its one-hole statement concerns \(1\le t<\sec\theta\); it does not assert a one-hole description for smaller dilation.

## Proof
**1. An unavoidable central exclusion.** Every odd regular polygon has support \(h_{P_m}(-v_j)=c\): the direction opposite a vertex faces the middle of an edge. Thus, if \(x=v_j+tz\), \(z\in P_m\), then \(\langle x,v_j\rangle\ge1-tc\). Write \(h=1-tc\). For \(1\le t\le1/c\), we have \(h\ge0\), and the interior of \(Q_t=\bigcap_j\{x:\langle x,v_j\rangle\le h\}\) is excluded from each vertex translate. Also every translate lies in \((1+t)P_m\). Therefore \(U_t\subseteq (1+t)P_m\setminus\operatorname{int}Q_t\).

**2. Coverage outside the hole.** Take \(x\in(1+t)P_m\setminus\operatorname{int}Q_t\) and choose an index \(j\) maximizing \(\langle x,v_j\rangle\). At least one such scalar is at least \(h\), and the chosen vertex is angularly nearest to \(x\). By rotation let \(v_j=(1,0)\) and write \(x=(X,Y)\). The angular sector of this vertex is \(S=\{X\ge0,\ |Y|\le X\tan\theta\}\), and the exclusion condition gives \(X\ge h\). We claim
\[
(1+t)P_m\cap S\cap\{X\ge h\}\subseteq (1,0)+tP_m.
\]
The left-hand polygon is the convex hull of the five points
\[
A=(1+t,0),\quad E_\pm=((1+t)c^2,\ \pm(1+t)c\sin\theta),\quad
H_\pm=(h,\ \pm h\tan\theta).
\]
Indeed, \(A,E_\pm\) are the vertices of the radial sector cut from \((1+t)P_m\), and the line \(X=h\) intersects its two radial sides between the origin and \(E_\pm\), because \(h\le(1+t)c^2\) for \(t\ge1\) and \(c\ge1/2\).

Now \(A=(1,0)+t(1,0)\) belongs to the claimed translate. Also \(E_\pm=(1+t)(v_0+v_{\pm1})/2\), so
\[
E_\pm-v_0=\frac{t-1}{2}v_0+\frac{t+1}{2}v_{\pm1}\in tP_m
\]
when \(t\ge1\). Finally the edge of \(v_0+tP_m\) opposite \(v_0\) is the vertical segment \(\{(h,Y):|Y|\le t\sin\theta\}\). The points \(H_\pm\) lie on this segment because
\[
h\tan\theta\le t\sin\theta\quad\Longleftrightarrow\quad1\le2tc,
\]
and \(2tc\ge1\) throughout the stated range. By convexity, the entire five-vertex polygon belongs to \(v_0+tP_m\), proving coverage and the asserted set equality. The same argument applies at \(h=0\), covering the origin as well, and gives \(U_{1/c}=(1+1/c)P_m\).

**3. Stabilization and sharpness.** For \(t\ge1/c\), put \(r=t-1/c\). Associativity of Minkowski addition gives
\[
U_t=U_{1/c}+rP_m=(1+1/c)P_m+rP_m=(1+t)P_m.
\]
For \(1\le t<1/c\) the open polygon \(\operatorname{int}Q_t\) is nonempty, so \(U_t\) is not convex. For \(0\le t<1\), restrict the union to the supporting edge of \((1+t)P_m\) parallel to an edge \([v_j,v_{j+1}]\) of \(P_m\). Only the two translates based at its endpoints meet this face. They occupy the respective initial and terminal proportions \(t/(1+t)\) of the edge, leaving an open middle interval because \(t<1\). Thus the union is again nonconvex. Therefore \(1/c\) is the exact threshold.

**4. Area law.** A regular \(m\)-gon of inradius \(h\) has area \(m h^2\tan\theta\), including the limiting case \(h=0\). Hence the area deficit is \(m(1-tc)^2\tan\theta\). Since \(\operatorname{area}(P_m)=mc\sin\theta\), normalization gives \(((1/c-t)/(1+t))^2\). Finally \(1-\cos\theta=\theta^2/2+O(\theta^4)\) and \(\tan\theta=\theta+O(\theta^3)\) give the two large-order asymptotics.

## Verification
An accompanying standalone program independently constructs the vertex translates using polygon union geometry for several odd orders and dilation values, then compares the uncovered area with the exact expression; it also checks the strict exterior-edge gap below unit dilation and the normalized identity. The script runs its geometry comparisons when the documented open-source polygon package is installed. These finite checks are **not** used to prove the universal statement; the convex-sector argument above supplies the proof for all odd orders and all real parameters in scope.

## Relationship to prior work
Meyer's *Finite convexification by Minkowski summation* (first public version, 19 October 2026) characterizes **whether** a compact pair admits eventual convexification, particularly through exposed-face covering, rather than this exact one-hole area profile for odd regular vertex sets. Artstein-Avidan, Falah and Slomka's *Vertex generated polytopes* (first public version, 30 July 2024) defines the same Schneider index and normalized vertex-generation parameter, establishes the general planar bounds, the simplex extremum and the zonotope/even-symmetric case. Those definitions and results are not novel here. The specific odd regular polygon index and, more substantially, the exact changing missing-area region and fractional quadratic closure are the present statements. Searches for equivalent formulations, broader coverage and exact tables did not identify an earlier statement encompassing the full profile; this negative search is not a priority guarantee.

## Limitations
The formula is proved only for odd regular polygons of order at least five and the full geometric profile for \(t\ge1\); no shape classification is asserted for \(0<t<1\). The result does not address arbitrary planar polytopes, nonregular polygons, or finite Minkowski averages. It has not undergone independent mathematical review. Earlier literature may contain an equivalent formula under a different terminology.

## References
- Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (19 October 2026), https://arxiv.org/html/2610.26744v1.
- Shiri Artstein-Avidan, Tomer Falah and Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1 (30 July 2024), https://arxiv.org/html/2407.20604v1.
- Rolf Schneider, *A measure of convexity for compact sets* (1975), as cited in the preceding two papers; primary original text not independently examined here.
