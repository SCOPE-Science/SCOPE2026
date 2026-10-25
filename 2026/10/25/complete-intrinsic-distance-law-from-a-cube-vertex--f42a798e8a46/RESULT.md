# Complete intrinsic-distance law from a cube vertex

## Finding

Let \(S=\partial[0,1]^3\) carry its intrinsic Euclidean path metric \(d_S\), let \(o=(0,0,0)\), and choose \(X\) uniformly with respect to surface area on \(S\). Put \(R=d_S(o,X)\). The complete cumulative distribution function \(F(r)=\Pr(R\le r)\) is given for \(r\ge0\) by
\[
F(r)=\frac{A(r)+B(r)}2,
\]
where
\[
A(r)=\begin{cases}
\pi r^2/4,&0\le r\le1,\\
\sqrt{r^2-1}+r^2\bigl(\arcsin(1/r)-\pi/4\bigr),&1<r<\sqrt2,\\
1,&r\ge\sqrt2,
\end{cases}
\]
and \(B(r)=0\) for \(r\le1\), \(B(r)=1\) for \(r\ge\sqrt5\), while for \(1<r<\sqrt5\),
\[
\begin{aligned}
a(r)&=\max\{0,\sqrt{r^2-1}-1\},\\
b(r)&=\frac{\sqrt{2r^2-1}-1}{2},\\
J_r(t)&=\frac{(1+t)\sqrt{r^2-(1+t)^2}+r^2\arcsin((1+t)/r)}2,\\
B(r)&=2\left[J_r(b(r))-J_r(a(r))+a(r)-\frac{b(r)^2}2\right].
\end{aligned}
\]
For \(r<0\), \(F(r)=0\). In particular, \(F(r)=\pi r^2/8\) for \(0\le r\le1\), the interior transition radii are \(r=1\) and \(r=\sqrt2\), with support endpoint \(\sqrt5\), and \(F(r)=1\) for \(r\ge\sqrt5\). The farthest surface point is the opposite cube vertex, uniquely, at distance \(\sqrt5\). The even moments and upper endpoint obey
\[
\mathbb E[R^2]=\frac32,\qquad
\mathbb E[R^4]=\frac{61}{18},\qquad
1-F(r)\sim\frac{(5-r^2)^2}{48}\sim\frac5{12}(\sqrt5-r)^2\quad(r\uparrow\sqrt5).
\]

## Assumptions and scope

The cube has unit side length. Distances are *intrinsic shortest-surface-path lengths*, not three-dimensional chords or graph distances. Uniformity refers to total surface area, so each of the six faces has probability \(1/6\). Paths may cross edges but an interior point of a shortest path cannot cross a convex cube vertex. The distribution is invariant under choice of the marked vertex and scales linearly with cube side length.

## Proof

**1. Pointwise intrinsic distances.** On each of the three faces containing \(o\), planar straight segments give \(d_S(o,(u,v,0))^2=u^2+v^2\), and similarly under coordinate permutation. On a face opposite one of these, say \(x=1\), write the target as \((1,y,z)\) with \(0\le y,z\le1\). Two genuine paths are obtained by unfolding across \(y=0\) or across \(z=0\), and have lengths \(\sqrt{(1+y)^2+z^2}\) and \(\sqrt{(1+z)^2+y^2}\). The straight segments cross the designated common edge within its unit interval, so they are feasible. We prove that no other surface path is shorter:
\[
d_S(o,(1,y,z))^2=1+y^2+z^2+2\min\{y,z\}.\tag{1}
\]

A minimizing surface path can be selected so that it visits no face twice. Indeed, if it visited the same closed square face twice with an intervening excursion, the intervening segment could be replaced by its Euclidean chord lying in that square, without increasing length; repeated replacements eliminate revisits. If there are vertex/edge degeneracies, use limiting interior crossings, or make the chord replacement before taking a minimizing limit. Its face sequence consequently begins on one of the three faces incident to \(o\), ends on \(x=1\), and is a simple walk in the cube face-adjacency graph (the graph on the six faces in which distinct-coordinate faces are adjacent).

Develop each possible face walk into the plane across its successive common edges, always attaching the next square on the outward side. The first face is placed with \(o\) at the planar origin. The unfolded target is an affine isometric image \(p+y e_y+z e_z\), so its squared planar distance to the origin is
\[
y^2+z^2+c_0+c_y y+c_z z,\tag{2}
\]
where \(c_0,c_y,c_z\) are integers. The 80 possible simple face walks yield just 24 distinct triples. Exhaustive construction of these walks and their coefficients is performed with exact integer coordinates in `verify_cube_vertex_law.py`. All 24 triples satisfy
\[
c_0-1\ge0,\quad c_0+c_y-1\ge0,\quad c_0+c_z-1\ge0,\quad
c_0+c_y+c_z-3\ge0.\tag{3}
\]
To verify the implication from (3), subtract \(1+2\min\{y,z\}\) from the affine part of (2): it is affine separately on the triangles \(0\le y\le z\le1\) and \(0\le z\le y\le1\). The vertices of those triangles are exactly \((0,0),(0,1),(1,0),(1,1)\), where the four differences are those in (3). Thus every developed route has length at least the smaller of the two feasible two-face paths, proving (1). The certificate is exhaustive rather than a sample of trajectories.

**2. Surface-area integration.** Let \(A(r)\) denote the fraction of the unit area on one incident face within distance \(r\), and \(B(r)\) the corresponding fraction on one nonincident face. There are three of each, hence \(F=(A+B)/2\). The first is the area of a disk of radius \(r\), centered at a corner, intersected with a unit square; elementary circular-segment integration gives \(A\) above.

For \(B\), split the opposite square into the two triangles \(0\le y\le z\le1\) and \(0\le z\le y\le1\). By (1), on the first triangle the circle condition is \((1+y)^2+z^2\le r^2\). Its upper boundary is \(z=\sqrt{r^2-(1+y)^2}\), and it intersects \(z=y\) at \(y=b(r)\). When \(r>\sqrt2\), it first reaches the top of the square at \(y=a(r)\); otherwise \(a(r)=0\). Therefore
\[
B(r)=2\left[\int_0^{a(r)}(1-y)\,dy+
\int_{a(r)}^{b(r)}\bigl(\sqrt{r^2-(1+y)^2}-y\bigr)\,dy\right].\tag{4}
\]
An antiderivative of the square-root term is \(J_r(y)\), giving the displayed formula. All the limits hold by continuity. The full support ends at \(\sqrt5\), uniquely at \((1,1,1)\), by (1).

**3. Moments and endpoint.** On an incident face the random squared distance is \(U^2+V^2\); on an opposite face it is \(1+U^2+V^2+2\min(U,V)\), with \(U,V\) independent uniform on \([0,1]\). Direct polynomial integration on the square split by \(U=V\) gives, respectively, first moments \(2/3,7/3\) and second moments \(28/45,277/45\). Averaging the two face types proves the stated moments.

For the upper tail, put \(s=5-r^2\) and write \(y=1-u,z=1-v\). On \(u\ge v\ge0\), (1) is \(5-4u-2v+u^2+v^2\). Hence the part of this triangle with distance exceeding \(r\) has area \(s^2/48+o(s^2)\): after rescaling by \(s\), it tends to the triangle \(4u+2v<1,\ u\ge v\ge0\). Doubling for \(v\ge u\) gives opposite-face tail \(s^2/24+o(s^2)\). Half of the total surface area lies on opposite faces, giving \(1-F(r)=s^2/48+o(s^2)\). Since \(s\sim2\sqrt5(\sqrt5-r)\), the other form follows.

## Verification

Run `python3 verify_cube_vertex_law.py` with Python 3 and no third-party dependencies. It constructs all 80 simple face walks and all 24 integer coefficient classes and checks the four exact inequalities (3) for every class. Separately it integrates the even moments using rational polynomial arithmetic, and it compares the CDF with direct area midpoint quadrature at seven radii. The quadrature is a numerical sanity check only; the proof is the exhaustive face-walk argument and analytic integration (4).

## Relationship to prior work

Fuchs (2016) develops the regular cube by a square lattice to study geodesic segments with **vertex endpoints** and their asymptotic endpoint frequencies, not the area law of distance to an arbitrary uniformly selected surface point. Goldstone–Roca–Suzzi Valli (2020) study shortest routes between arbitrary points in **opposite face interiors**, and Davis (2023) studies the topological/geodesic complexity and cut-locus types on the cube. These methods motivate the present vertex-source development but do not supply formula (4) or the complete vertex-centered distance CDF. Mathai–Moschopoulos–Pederzoli (1999) treat Euclidean distances between points in or on cubes, not intrinsic surface paths. The general shortest-surface-path algorithm of Mitchell–Mount–Papadimitriou (1987) computes pointwise paths, but does not state the distribution integral or its special transitions and moments. No claim of exhaustive literature uniqueness is made.

## Limitations

Only a unit-edge regular cube and a fixed **vertex** source are covered. This does not give the law for two independent random points on a cube surface or a source in a face interior. Bibliographic completeness cannot be guaranteed for unindexed or inaccessible literature. The numerical quadrature is not an infinite proof; the all-walk inequality certificate, together with its combinatorial completeness argument, is the finite exact part of the proof. Independent audit has not been performed.

## References

1. D. Fuchs, *Geodesics on Regular Polyhedra with Endpoints at the Vertices*, Arnold Mathematical Journal 2 (2016), 201–211. First published online 2016-03-23. https://doi.org/10.1007/s40598-016-0040-z . Open full text: https://armj.math.stonybrook.edu/pdf-Springer-final/016-0040.pdf .
2. R. Goldstone, R. Roca, R. Suzzi Valli, *Shortest Paths on Cubes*, 2020, https://arxiv.org/abs/2003.06096 .
3. D. M. Davis, *Geodesic complexity of a cube*, 2023, https://arxiv.org/abs/2308.04316 .
4. J. S. B. Mitchell, D. M. Mount, C. H. Papadimitriou, *The Discrete Geodesic Problem*, SIAM Journal on Computing 16 (1987), 647–668, https://doi.org/10.1137/0216045 .
5. A. M. Mathai, P. Moschopoulos, G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81, https://doi.org/10.6092/issn.1973-2201/1104 .
