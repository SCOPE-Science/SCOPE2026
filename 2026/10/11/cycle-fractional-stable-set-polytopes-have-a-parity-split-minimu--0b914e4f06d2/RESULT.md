# Cycle fractional stable-set polytopes have a parity-split minimum sphere
## Finding
For \(n\ge3\), let
\[
P_n=\operatorname{FRAC}(C_n)
=
\left\{
x\in\mathbb R^n:
x_i\ge0,\quad x_i+x_{i+1}\le1
\text{ for all }i\in\mathbb Z/n\mathbb Z
\right\}.
\tag{1}
\]
Equip \(P_n\) with the standard Euclidean metric of \(\mathbb R^n\).

If \(n\) is even, then the unique minimum enclosing Euclidean ball has
\[
\boxed{c_n=\frac12\mathbf1}
\tag{2}
\]
and
\[
\boxed{R_n^2=\frac n4}.
\tag{3}
\]
Every vertex of \(P_n\) is a contact point.

If \(n\) is odd, put
\[
\alpha=\frac{n-1}{2}.
\tag{4}
\]
Then the unique minimum enclosing ball has
\[
\boxed{
c_n=\frac{\alpha}{n}\mathbf1
=\frac{n-1}{2n}\mathbf1
}
\tag{5}
\]
and
\[
\boxed{
R_n^2
=\frac{\alpha(n-\alpha)}{n}
=\frac{n^2-1}{4n}.
}
\tag{6}
\]
The contact set consists exactly of the \(n\) incidence vectors of maximum stable sets of \(C_n\).

The odd cycle has one additional vertex,
\[
h=\frac12\mathbf1,
\tag{7}
\]
which is the unique fractional vertex. It is strictly interior to the minimum sphere, with
\[
\boxed{
\|h-c_n\|^2=\frac1{4n}.
}
\tag{8}
\]
Moreover, if \(S\) is any stable set with \(|S|=k\), then
\[
\boxed{
\|\chi_S-c_n\|^2
=\frac{\alpha^2+k}{n},
\qquad 0\le k\le\alpha.
}
\tag{9}
\]
Thus the stable-set vertices form \(\alpha+1\) exact radial shells in the odd case, indexed only by stable-set cardinality.

## Assumptions and scope
The fractional stable-set polytope is the standard linear-programming relaxation of the stable-set polytope. The primary source studies its circuit geometry and records the general half-integrality and graph interpretation of its vertices. An earlier same-object source studies its Ehrhart theory and gives the vertex criterion used below.

The metric is the ordinary Euclidean metric in the coordinate realization (1). The theorem concerns the minimum enclosing ball of the whole polytope, equivalently of its vertex set.

## Proof
We first determine the vertices for a cycle.

Every vertex of a fractional stable-set polytope is half-integral. More specifically, if \(x\in\{0,1/2,1\}^n\) is feasible, then it is a vertex exactly when every connected component induced by the coordinates equal to \(1/2\) contains an odd cycle, unless there are no half coordinates.

For a cycle this immediately gives the complete list. If \(n\) is even, the cycle is bipartite, so there are no fractional vertices and the vertices are exactly
\[
\chi_S
\qquad(S\subseteq V(C_n)\text{ stable}).
\tag{10}
\]
If \(n\) is odd, any nonempty proper induced subgraph of the cycle is a union of paths and therefore contains no odd cycle. Consequently the only vertex containing a half coordinate is
\[
h=\frac12\mathbf1,
\]
and all remaining vertices are the stable-set incidence vectors.

This cycle-specific vertex statement can also be proved directly from (1): if a vertex has a zero coordinate, deleting that coordinate cuts the cycle constraints into path systems and forces an integral path vertex; if every coordinate is positive, vertexhood requires all \(n\) edge inequalities to be tight. The equations \(x_i+x_{i+1}=1\) have the unique solution \(h\) when \(n\) is odd and have a one-dimensional solution family when \(n\) is even.

Now consider a block-symmetric point
\[
c=s\mathbf1.
\tag{11}
\]
For a stable set \(S\) of size \(k\),
\[
\begin{aligned}
\|\chi_S-c\|^2
&=k(1-s)^2+(n-k)s^2\\
&=ns^2+k(1-2s).
\end{aligned}
\tag{12}
\]
The dihedral symmetry of \(C_n\) preserves \(P_n\). Since a finite Euclidean point set has a unique minimum-enclosing center, that center is fixed by the full dihedral action and hence has the form (11). We will also give contact-barycenter certificates, so the optimality does not rely only on symmetry.

Suppose first that \(n\) is even. The stability number is
\[
\alpha=\frac n2.
\]
For \(s\le1/2\), equation (12) is maximized by \(k=\alpha\), giving
\[
ns^2+\frac n2(1-2s)
=n\left(s-\frac12\right)^2+\frac n4.
\tag{13}
\]
For \(s\ge1/2\), the empty stable set gives squared distance \(ns^2\), which is at least \(n/4\). Hence the unique optimum is \(s=1/2\), with squared radius \(n/4\).

At \(s=1/2\), equation (12) is exactly \(n/4\) for every \(k\), so every vertex is a contact. There is also a sharp two-point certificate: the two alternating maximum stable sets have complementary incidence vectors, their midpoint is \(\mathbf1/2\), and their mutual distance is \(\sqrt n\). Any ball containing both must have radius at least \(\sqrt n/2\), with equality only at their midpoint.

Now let \(n\) be odd and \(\alpha=(n-1)/2\). Restrict first to the integral stable-set vertices. For \(s\le1/2\), (12) is maximized at \(k=\alpha\), and the resulting quadratic
\[
ns^2+\alpha(1-2s)
\tag{14}
\]
has its unique minimum at
\[
s=\frac\alpha n.
\tag{15}
\]
The minimum value is
\[
\alpha-\frac{\alpha^2}{n}
=\frac{\alpha(n-\alpha)}n
=\frac{n^2-1}{4n}.
\tag{16}
\]
At (15), equation (12) simplifies to
\[
\|\chi_S-c_n\|^2
=\frac{\alpha^2+k}{n},
\tag{17}
\]
which is strictly increasing with \(k\). Thus the integral contacts are exactly the maximum stable sets.

There are exactly \(n\) maximum stable sets in an odd cycle: each has one unique pair of consecutive omitted vertices, and the location of that double gap determines the set. By cyclic symmetry, each cycle vertex belongs to exactly \(\alpha\) of these \(n\) maximum stable sets. Their barycenter is therefore
\[
\frac\alpha n\mathbf1=c_n.
\tag{18}
\]
Since all these contact points have the common squared distance (16), for any competing center \(y\), averaging squared distances over the \(n\) contacts gives
\[
R_n^2+\|y-c_n\|^2.
\tag{19}
\]
At least one contact is therefore at distance at least the square root of (19). This proves global minimality and uniqueness.

Finally,
\[
\left\|\frac12\mathbf1-c_n\right\|^2
=n\left(\frac12-\frac{n-1}{2n}\right)^2
=\frac1{4n},
\tag{20}
\]
which is strictly smaller than (16) for every odd \(n\ge3\). Thus the unique fractional vertex lies strictly inside the minimum sphere.

## Verification
The proof is symbolic for every \(n\ge3\).

The same-object literature was checked directly. The circuit-diameter source identifies the fractional stable-set polytope as the standard LP relaxation, records half-integrality, and studies its vertex/circuit graph interpretation. The earlier Ehrhart paper defines \(\operatorname{FRAC}(G)\), states that \(\operatorname{FRAC}(G)=\operatorname{STAB}(G)\) exactly for bipartite graphs, and gives the precise half-integral vertex criterion from which the cycle vertex list follows.

The accompanying `verify.py` independently constructs the halfspace system for \(3\le n\le12\), enumerates its vertices with a halfspace-intersection routine, compares them with the claimed stable-set-plus-half-vector list, checks every closed radius and contact formula, and numerically solves the full ambient minimum-enclosing-ball epigraph problem for \(3\le n\le9\). The finite replay is corroborative only.

## Relationship to prior work
Kafer, Pashkovich, and Sanità study circuit diameter for several classical optimization polytopes, including the fractional stable-set polytope. Their results concern circuit directions and path length, not Euclidean enclosing spheres.

Hamano, Hibi, and Ohsugi study the same fractional stable-set polytope for arbitrary graphs through Ehrhart series, Gorenstein properties, and half-integral vertices. Their full text contains no circumradius, Euclidean-radius, Chebyshev-center, or minimum-enclosing-ball result.

For even cycles, \(\operatorname{FRAC}(C_n)=\operatorname{STAB}(C_n)\), but existing Euclidean inradius results for perfect stable-set polytopes concern facet clearance rather than the minimum enclosing ball. The odd-cycle statement is genuinely about the fractional relaxation: its unique half-integral vertex is present but does not support the minimum sphere.

The parity transition is therefore tied to the integrality obstruction of the cycle relaxation itself. In the bipartite case every vertex lies on one sphere; in the odd case the unique fractional vertex moves close to the center while only maximum stable sets remain on the outer shell.

## Limitations
The theorem is specific to cycles. General fractional stable-set polytopes can have many half-integral vertices whose half-coordinate supports contain several odd-cycle components, so one should not expect a two-orbit reduction.

The result concerns the standard coordinate realization. It does not determine the inradius, John ellipsoid, or minimum sphere after arbitrary affine changes of coordinates.

The cycle calculation is concise once the half-integral vertex criterion is combined with dihedral symmetry, so independent rediscovery under optimization terminology remains a residual originality risk.

## References
1. Sean Kafer, Kanstantsin Pashkovich, and Laura Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642, first public version 2017-09-27; *SIAM Journal on Discrete Mathematics* 33 (2019), 1--25, DOI 10.1137/17M1152115.
2. Ginji Hamano, Takayuki Hibi, and Hidefumi Ohsugi, *Ehrhart Series of Fractional Stable Set Polytopes of Finite Graphs*, arXiv:1603.09613; *Annals of Combinatorics* 22 (2018), 563--573, DOI 10.1007/s00026-018-0392-2.
3. Carlo Michini and Antonio Sassano, *The Hirsch Conjecture for the Fractional Stable Set Polytope*, *Mathematical Programming* 147 (2014), 309--330, DOI 10.1007/s10107-013-0723-3.
