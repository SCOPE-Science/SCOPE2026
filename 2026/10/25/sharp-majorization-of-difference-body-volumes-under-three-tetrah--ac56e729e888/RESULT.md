# Sharp majorization of difference-body volumes under three tetrahedral vertex cuts

## Finding
Consider the nondegenerate tetrahedron \(\Delta=\{x\in\mathbb R^3:x_i\ge0,\ x_1+x_2+x_3\le1\}\). For \(a,b,c\ge0\) with \(s=a+b+c<1\), form
\[
K_{a,b,c}=\Delta\cap\{x_1\le1-a,\ x_2\le1-b,\ x_3\le1-c\}.
\]
Define \(Q_2=a^2+b^2+c^2\), \(Q_3=a^3+b^3+c^3\), and the affine-invariant Rogers--Shephard ratio \(R(a,b,c)=\operatorname{vol}_3(K_{a,b,c}-K_{a,b,c})/\operatorname{vol}_3(K_{a,b,c})\). Then
\[
\boxed{R(a,b,c)=20-6\left[s+(2-s)\frac{Q_2-Q_3}{1-Q_3}\right].}
\]
For each fixed \(0<s<1\), \(R\) is **strictly Schur-concave** on the depth simplex: any nontrivial averaging of two unequal depths strictly raises \(R\). In particular, the following complete sharp interval holds:
\[
\boxed{20-6\frac{s(1+3s)}{1+s+s^2}\ \le R(a,b,c)\ \le20-6\frac{s(9+6s-5s^2)}{9-s^3}.}
\]
The lower bound is attained **only** at permutations of \((s,0,0)\); the upper bound is attained **only** when \(a=b=c=s/3\). For \(s=0\), the body is the original tetrahedron and \(R=20\). The result is valid under all invertible affine coordinate changes of the tetrahedron and gives the exact response to distributing a fixed total barycentric truncation depth across three vertices.

## Assumptions and scope
The three cut planes parallel to the facets opposite \(e_1,e_2,e_3\) truncate the corresponding original simplex vertices by barycentric fractions \(a,b,c\). Since \(s<1\), their removed corner tetrahedra have pairwise disjoint interiors. Zero depths are permitted, allowing exact boundary equality cases. Here \(K-K=K+(-K)\) and all volumes are three-dimensional ordinary Lebesgue volumes. For two depth vectors with the same sum, \((a,b,c)\) majorizes \((a',b',c')\) when the partial sums of their decreasing rearrangements satisfy the standard majorization inequalities; strict Schur concavity means \(R(a,b,c)<R(a',b',c')\) whenever they differ by more than a permutation. No claim is made for total depth \(s\ge1\), arbitrary cut-plane orientations, or arbitrary convex bodies.

## Proof
**1. Exact volume.** The original tetrahedron has volume \(1/6\). At vertex \(e_i\), the removed corner is a homothetic tetrahedron of scale \(a_i\), hence volume \(a_i^3/6\). As these three regions are interior-disjoint for \(s<1\),
\[
\operatorname{vol}_3(K_{a,b,c})=\frac{1-Q_3}{6}.
\]
**2. The relevant mixed volume.** For a three-dimensional polytope \(K\) and any convex body \(L\), the standard surface-area formula is \(3V(K,K,L)=\sum_F A_Fh_L(u_F)\), with facets \(F\), unit outer normals \(u_F\), Euclidean facet areas \(A_F\), and support function \(h_L\). Apply it with \(L=-K\). The facet lying in \(x_i=0\) has area \((1-Q_2+a_i^2)/2\), outer normal \(-e_i\), and support \(h_{-K}(-e_i)=1-a_i\). Every other facet lies in a plane \(\sum_i x_i=1\) or \(x_i=1-a_i\), with outward normal having nonnegative coordinates, and has \(h_{-K}(u)=0\) because \(0\in K\) and \(\inf_{x\in K}\langle u,x\rangle=0\) for those normals (a point of the original origin-facing coordinate facets achieves it). Thus
\[
3V(K,K,-K)=\frac12\sum_{i=1}^3(1-a_i)(1-Q_2+a_i^2)
=\frac{3-s-(2-s)Q_2-Q_3}{2},
\]
so
\[
V(K,K,-K)=\frac{3-s-(2-s)Q_2-Q_3}{6}.
\]
Reflection invariance of mixed volume yields \(V(K,-K,-K)=V(K,K,-K)\). Expanding \(\operatorname{vol}_3(K-K)\) therefore gives \(2\operatorname{vol}_3(K)+6V(K,K,-K)\). Dividing by volume and simplifying proves the displayed exact formula for \(R\).

**3. Strict balancing.** Fix two depths \(x,y\) with sum \(v=x+y>0\) and keep the third depth \(z\) fixed, so \(v+z=s<1\). Put \(p=xy\). Then \(Q_2-Q_3\) and \(1-Q_3\) reduce to linear functions in \(p\):
\[
H(p):=\frac{Q_2-Q_3}{1-Q_3}
=\frac{v^2-v^3+z^2-z^3+(3v-2)p}{1-v^3-z^3+3vp}.
\]
Direct differentiation gives
\[
H'(p)=-\frac{B(v,z)}{(1-v^3-z^3+3vp)^2},
\qquad B(v,z)=2-3v+v^3+3vz^2-2z^3.
\]
For fixed \(0<v<1\), the derivative of \(B\) with respect to \(z\) is \(6z(v-z)\), making the minimum on \([0,1-v]\) occur at an endpoint. The endpoint values are
\[
B(v,0)=(1-v)^2(v+2)>0,\qquad
B(v,1-v)=6v(1-v)^2>0.
\]
Thus \(H'(p)<0\) throughout the parameter domain. Averaging unequal \(x,y\) with fixed sum strictly increases \(p=xy\), strictly decreases \(H\), and strictly increases \(R=20-6[s+(2-s)H]\). Successive pairwise averaging is the elementary characterization of majorization, establishing the strict Schur-concavity assertion and its equality rigidity.

**4. Sharp endpoints.** With fixed \(s\), \((s,0,0)\) majorizes every other depth triple and every triple majorizes \((s/3,s/3,s/3)\). Substitution in the formula gives
\[
R(s,0,0)=20-6\frac{s(1+3s)}{1+s+s^2},\quad
R(s/3,s/3,s/3)=20-6\frac{s(9+6s-5s^2)}{9-s^3}.
\]
Strictness of balancing supplies precisely the announced equality cases.

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy. An exact-rational checker constructs all vertices of the three-cut tetrahedra, uses numerical convex hulls **only to propose triangulations**, then checks every proposed triangle's supporting-plane condition with exact `fractions.Fraction` arithmetic and accumulates all pyramid determinants exactly. In 112 admissible rational depth configurations it independently verifies the original volume, difference-body volume, both mixed-volume identities, and sharp endpoints; it certifies all 6,060 proposed facet triangles, together with 75 exact pair-mixing derivative identities. Its expected output is `VERIFY_OK exact_hulls= 112 rational_triangles= 6060 mixing_derivative_checks= 75`. These finite checks corroborate, but do not replace, the continuous proof above.

## Relationship to prior work
Rogers and Shephard established the universal difference-body bound \(R\le20\) in dimension three. Artstein-Avidan, Sadovsky and Sanyal proved the anti-blocking-body case of Godbersen's inequality and a general decomposition of differences; Manui, Ndiaye and Zvavitch further developed projection-volume decompositions for anti-blocking bodies. These results include the general technique of reconstructing a difference-body volume from coordinate projections, and are acknowledged as stronger **general formulas/inequalities** of which the expression for \(R\) is a computable specialization. Kotrbatý and Mouamine's July 2026 theorem proves the full Godbersen conjecture, including the global sharp bound but not a fixed-depth ordering for multivertex truncations. A published calculation of every mixed volume for a simplex truncated at **one vertex** determines the \((s,0,0)\) endpoint; it does not compare the different triple-cut distributions at fixed sum. The present contribution is the strict all-triple majorization theorem, sharp two-sided interval, and rigid extremizers, not the universal inequality, the anti-blocking decomposition, or the already-known single-vertex endpoint.

## Limitations
Only three separate facet-parallel cuts at three selected vertices, with total barycentric depth strictly less than one, are treated. Fixed total cut depth is not the same as fixed removed volume. No global sharp stability exponent for all convex bodies is claimed. Equivalent formulas or majorization observations in unindexed historical sources cannot be excluded; the recent higher-order Godbersen full text was not fully inspectable, although its available abstract addresses a different global inequality.

## References
1. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220--233.
2. S. Artstein-Avidan, S. Sadovsky and R. Sanyal, *Geometric Inequalities for Anti-Blocking Bodies*, arXiv:2008.10394; Communications in Contemporary Mathematics 25 (2023), article 2150113.
3. A. Manui, C. S. Ndiaye and A. Zvavitch, *On the volume of sums of anti-blocking bodies*, arXiv:2409.14214 (first submitted 21 September 2024), especially the orthant decomposition of \(K-K\).
4. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387 (first submitted 22 July 2026), Theorem 1.1.
5. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, public research record, 11 October 2026, identifier `2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949`.
6. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806 (first submitted 5 October 2026).
