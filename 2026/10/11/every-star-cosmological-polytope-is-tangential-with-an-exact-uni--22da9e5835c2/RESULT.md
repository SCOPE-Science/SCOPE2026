# Every star cosmological polytope is tangential with an exact unique inball
## Finding
Let
\[
m\ge1
\]
and let
\[
G=K_{1,m}
\]
be the star with center \(0\), leaves \(1,\ldots,m\), and edges
\[
e_i=\{0,i\}.
\]
Use the standard cosmological-polytope realization in the orthonormal coordinates
\[
x_0,x_1,\ldots,x_m,y_1,\ldots,y_m.
\]
Put
\[
D=2m+1,
\]
\[
\alpha_m
=
\sqrt{\frac{m(m+1)}{2m+1}},
\qquad
\beta_m
=
\sqrt{\frac{2(2m-1)}{2m+1}}.
\tag{1}
\]

Then the star cosmological polytope \(P_G\) is tangential. All of its
\[
2^m+m
\]
facets touch one Euclidean insphere.

Its inradius is
\[
\boxed{
r_m
=
\frac{2}{2\alpha_m+m\beta_m}
=
\frac{2\sqrt{2m+1}}
{2\sqrt{m(m+1)}+m\sqrt{2(2m-1)}}.
}
\tag{2}
\]

The incenter is unique. Define
\[
t_m=\frac{r_m\beta_m}{2}
\tag{3}
\]
and
\[
a_m=1-2mt_m.
\tag{4}
\]
Then the unique incenter is
\[
\boxed{
c_m
=
a_m e_{x_0}
+
t_m
\sum_{i=1}^m
\left(e_{x_i}+e_{y_i}\right).
}
\tag{5}
\]

Thus an exponentially growing facet family is exactly circumscribed about one sphere: every leaf facet and every facet corresponding to a connected subgraph containing the star center is tangent.

For \(m=1\), the polytope is the source triangle and
\[
r_1=\sqrt{\frac23}.
\]
For \(m=2\),
\[
r_2=\frac1{\sqrt{24/5}}=\sqrt{\frac5{24}},
\]
and the central coordinate of the incenter is \(0\).

## Assumptions and scope
The metric is the Euclidean metric inherited from the standard source coordinates.

For an edge \(e_i=\{0,i\}\), the three cosmological-polytope vertices are
\[
p_i=-y_i+x_0+x_i,
\]
\[
p_{i,0}=y_i+x_0-x_i,
\qquad
p_{i,i}=y_i-x_0+x_i.
\tag{6}
\]
Every vertex has total coordinate sum \(1\). The \(2m\) differences
\[
p_{i,0}-p_i=2(y_i-x_i),
\qquad
p_{i,i}-p_i=2(y_i-x_0)
\]
are linearly independent. Hence the affine hull is exactly
\[
H=
\left\{
z:
x_0+\sum_{i=1}^m x_i+\sum_{i=1}^m y_i=1
\right\}.
\tag{7}
\]

All distances below are intrinsic to \(H\).

## Proof
The source facet theorem says that facets of a cosmological polytope are indexed by connected subgraphs \(H'\) of the defining graph, and gives their supporting hyperplanes explicitly.

For the star, connected subgraphs have only two forms.

First, for each leaf \(i\), the one-vertex subgraph \(\{i\}\) gives the facet
\[
L_i(z)=x_i+y_i=0.
\tag{8}
\]
The polytope lies in
\[
L_i(z)\ge0.
\]

Second, every connected subgraph containing the center is uniquely determined by a subset
\[
S\subseteq[m]
\]
of leaves. It contains the center, the leaves in \(S\), and exactly the edges \(e_i\) with \(i\in S\). Its facet is
\[
F_S(z)
=
x_0
+
\sum_{i\in S}x_i
+
\sum_{j\notin S}y_j
=
0,
\tag{9}
\]
with
\[
F_S(z)\ge0
\]
on \(P_G\).

These are all facets, so there are
\[
m+2^m
\]
of them.

We now normalize their intrinsic Euclidean normals.

The ambient normal of \(L_i\) has two unit entries. Projecting it orthogonally to the translation space of \(H\) gives squared norm
\[
2-\frac4D
=
\frac{2(2m-1)}{2m+1}
=
\beta_m^2.
\tag{10}
\]

Every normal of \(F_S\) has exactly \(m+1\) unit entries, independently of \(S\). Its projected squared norm is
\[
(m+1)-\frac{(m+1)^2}{D}
=
\frac{m(m+1)}{2m+1}
=
\alpha_m^2.
\tag{11}
\]

Consequently, if a radius-\(\rho\) Euclidean ball centered at \(z\in H\) lies in \(P_G\), then
\[
L_i(z)\ge\rho\beta_m
\qquad
(1\le i\le m)
\tag{12}
\]
and
\[
F_S(z)\ge\rho\alpha_m
\qquad
(S\subseteq[m]).
\tag{13}
\]

Let \(x_0(z)\) denote the central coordinate. Summing (12) gives
\[
1-x_0(z)
=
\sum_{i=1}^m(x_i+y_i)
\ge
m\rho\beta_m,
\]
hence
\[
x_0(z)
\le
1-m\rho\beta_m.
\tag{14}
\]

Now average (13) over all \(2^m\) subsets \(S\). Each \(x_i\) and each \(y_i\) occurs in exactly half of the forms, so
\[
\frac1{2^m}\sum_{S\subseteq[m]}F_S(z)
=
x_0(z)
+\frac12\sum_{i=1}^m(x_i+y_i)
=
\frac{1+x_0(z)}2.
\]
Thus
\[
x_0(z)\ge2\rho\alpha_m-1.
\tag{15}
\]

Combining (14) and (15) yields
\[
2\rho\alpha_m-1
\le
1-m\rho\beta_m,
\]
so every inscribed ball satisfies
\[
\rho
\le
\frac{2}{2\alpha_m+m\beta_m}
=
r_m.
\tag{16}
\]

We now construct a center attaining equality. Put
\[
t_m=\frac{r_m\beta_m}{2}
\]
and
\[
a_m=1-2mt_m.
\]
The point \(c_m\) in (5) belongs to \(H\). For every leaf,
\[
L_i(c_m)=2t_m=r_m\beta_m.
\tag{17}
\]
For every subset \(S\),
\[
F_S(c_m)
=
a_m+mt_m
=
1-mt_m.
\]
Equation (2) is equivalent to
\[
1-mt_m=r_m\alpha_m,
\]
so
\[
F_S(c_m)=r_m\alpha_m.
\tag{18}
\]
Equations (17)--(18) show that the radius-\(r_m\) ball centered at \(c_m\) is contained in \(P_G\) and tangent to every facet. Together with (16), this proves the inradius formula and tangentiality.

It remains to prove uniqueness. Suppose \(z\) is any incenter of radius \(r_m\). Equality must hold in the combined bound (14)--(15). Since every summand in (12) is at least \(r_m\beta_m\) and their sum is exactly \(mr_m\beta_m\),
\[
L_i(z)=r_m\beta_m
\]
for every \(i\). Likewise, every \(F_S(z)\) is at least \(r_m\alpha_m\) and their average is exactly \(r_m\alpha_m\), so
\[
F_S(z)=r_m\alpha_m
\]
for every \(S\).

Comparing \(F_S\) with \(F_{S\cup\{i\}}\) for \(i\notin S\) gives
\[
x_i=y_i.
\]
Together with the leaf equalities this yields
\[
x_i=y_i=t_m
\]
for all \(i\). The affine equation (7) then forces
\[
x_0=a_m.
\]
Hence \(z=c_m\), proving uniqueness.

## Verification
The proof is symbolic for every \(m\ge1\).

The source-dependent ingredients were checked in the open-access primary full text: the standard vertex realization, the complete connected-subgraph facet theorem, and the explicit facet hyperplanes. The publication record verifies primary classification \(52B05\).

The accompanying `verify.py` independently builds all \(m+2^m\) star facets for
\[
1\le m\le7,
\]
computes their intrinsic projected-normal lengths, and solves the full Chebyshev linear program numerically using all facet inequalities. The resulting optimal radius and center agree with (2)--(5), and every facet is at the predicted tangent distance.

The finite computation is corroborative only.

## Relationship to prior work
Kühne and Monin initiate the systematic mathematical study of cosmological-polytope faces. Their full facet theorem identifies facets with connected subgraphs and supplies the supporting hyperplanes used here. For trees they also describe a recursive pyramid-over-bipyramid construction and compute face enumerators and normalized volumes.

Later work on cosmological polytopes studies regular unimodular triangulations, toric ideals, normalized volumes, and Ehrhart theory. Targeted searches under “cosmological polytope”, “star”, “inradius”, “insphere”, “Chebyshev center”, and “largest inscribed ball” did not locate an exact Euclidean inball theorem.

A previously established minimum-enclosing-sphere result for general connected cosmological polytopes is complementary rather than covering: it is controlled by the vertex shell, while the present theorem is controlled by supporting hyperplanes. The star inball additionally has the stronger tangential property that all exponentially many facets are contacts.

## Limitations
The theorem concerns star graphs and the standard Euclidean realization.

It does not give the inradius of a general cosmological polytope. For a general graph, connected-subgraph facet normals have several coefficient patterns and do not collapse to the two normal lengths in (10)--(11).

The result does not determine John or Löwner ellipsoids or Euclidean radii after non-orthogonal coordinate transformations.

A broader theorem for graph families with similarly uniform connected-subgraph facet norms could subsume the star calculation. No such covering statement was located in the targeted comparisons.

## References
1. Lukas Kühne and Leonid Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first public version 2022-09-16; *Annales de l'Institut Henri Poincaré D, Combinatorics, Physics and their Interactions* 12 (2025), 445--461, DOI 10.4171/AIHPD/192.
2. Martina Juhnke-Kubitzke, Liam Solus, and Lorenzo Venturello, *Triangulations of cosmological polytopes*, arXiv:2303.05876, first public version 2023-03-10.
