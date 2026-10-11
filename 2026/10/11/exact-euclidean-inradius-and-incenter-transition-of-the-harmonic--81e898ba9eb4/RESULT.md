# Exact Euclidean inradius and incenter transition of the harmonic polytope
## Finding
Let
\[
H_{n,n}\subset\mathbb R^n\times\mathbb R^n
\]
be the harmonic polytope introduced by Ardila and Escobar, in its standard coordinate realization. Its affine hull is
\[
\sum_{i=1}^n x_i
=
\sum_{i=1}^n y_i
=
C_n,
\qquad
C_n=\frac{n(n+1)}2+1.
\tag{1}
\]
Equip this affine space with the Euclidean metric inherited from
\[
\mathbb R^n\times\mathbb R^n.
\]

For every
\[
n\ge3,
\]
define
\[
\mu_n
=
\frac{C_n}{n}
=
\frac{n+1}{2}+\frac1n.
\tag{2}
\]
Then the harmonic polytope has the unique incenter
\[
\boxed{
c_n=(\mu_n\mathbf1,\mu_n\mathbf1)
}
\tag{3}
\]
and exact Euclidean inradius
\[
\boxed{
r_{\mathrm{in}}(H_{n,n})
=
\frac{n^2-n+2}{2\sqrt{n(n-1)}}.
}
\tag{4}
\]

Although
\[
H_{n,n}
\]
has
\[
3^n-3
\]
facets, the maximal ball for
\[
n\ge3
\]
is tangent exactly to the
\[
2n
\]
coordinate facets
\[
x_i=1,
\qquad
y_i=1
\qquad
(1\le i\le n).
\tag{5}
\]

The rank-two case is exceptional. One has
\[
\boxed{
r_{\mathrm{in}}(H_{2,2})=1,
}
\tag{6}
\]
and the complete incenter set is the segment
\[
\boxed{
\left\{
\bigl((2+t,2-t),(2+t,2-t)\bigr):
|t|
\le
1-\frac1{\sqrt2}
\right\}.
}
\tag{7}
\]

Thus the harmonic family has a sharp Chebyshev-center transition: rank two has a one-dimensional family of optimal centers, while every rank
\[
n\ge3
\]
has a unique incenter. In higher rank the metric bottleneck collapses from exponentially many facets to the two coordinate-facet orbits.

## Assumptions and scope
The harmonic polytope is the standard realization
\[
H_{n,n}
=
(\Pi_n\times\Pi_n)+D_n
\]
used in the cited source, where
\[
D_n=\operatorname{conv}\{e_i+f_i:1\le i\le n\}.
\]

The theorem concerns the inherited Euclidean metric on the affine hull in (1). It is realization-specific and is not invariant under arbitrary affine transformations.

Only the inradius, all incenters, and inball-contact facets are determined here. No formula is claimed for the circumradius, John ellipsoid, or other norms.

## Proof
The cited source proves the following minimal inequality description. A **bisubset**
\[
S\mid T
\]
consists of nonempty subsets
\[
S,T\subseteq[n]
\]
with
\[
S\cup T=[n]
\]
and not both equal to
\[
[n].
\]
Writing
\[
s=|S|,
\qquad
t=|T|,
\]
the corresponding facet inequality is
\[
x(S)+y(T)
\ge
\frac{s(s+1)+t(t+1)}2+1,
\tag{8}
\]
together with the two affine equations (1).

Assume first that
\[
n\ge3.
\]

Take
\[
S=\{i\},
\qquad
T=[n].
\]
Since
\[
y([n])=C_n,
\]
equation (8) becomes
\[
x_i\ge1.
\tag{9}
\]
Similarly,
\[
S=[n],
\qquad
T=\{i\}
\]
gives
\[
y_i\ge1.
\tag{10}
\]

Inside the affine tangent space
\[
\left\{
(u,v):
\sum_i u_i=\sum_i v_i=0
\right\},
\]
the projected normal of the facet
\[
x_i=1
\]
is
\[
e_i-\frac1n\mathbf1,
\]
whose squared norm is
\[
\frac{n-1}{n}.
\tag{11}
\]
The same holds for
\[
y_i=1.
\]

Suppose a radius-\(r\) Euclidean ball centered at
\[
c=(c^x,c^y)
\]
lies in
\[
H_{n,n}.
\]
The
\[
n
\]
facets (9) imply
\[
c^x_i-1
\ge
r\sqrt{\frac{n-1}{n}}
\qquad
(1\le i\le n).
\]
Summing and using
\[
\sum_i c^x_i=C_n
\]
gives
\[
r
\le
\frac{\mu_n-1}{\sqrt{(n-1)/n}}
=
\frac{n^2-n+2}{2\sqrt{n(n-1)}}.
\tag{12}
\]
Moreover, equality in (12) forces every
\[
c^x_i=\mu_n.
\]
The
\[
y_i=1
\]
facets similarly force every
\[
c^y_i=\mu_n.
\]
Thus if the bound in (12) is attainable, its center is necessarily the point (3).

It remains to verify every facet at that center and identify equality.

For a bisubset
\[
S\mid T,
\]
put
\[
u=|S\setminus T|,
\qquad
v=|T\setminus S|,
\qquad
w=|S\cap T|.
\]
Then
\[
u+v+w=n,
\qquad
u+v>0.
\tag{13}
\]
Let
\[
d=u-v
\]
and define
\[
Q=n^2-w^2-d^2.
\tag{14}
\]

The facet normal from (8), projected to the affine tangent space, is
\[
\nu_{S,T}
=
\left(
\mathbf1_S-\frac{s}{n}\mathbf1,\,
\mathbf1_T-\frac{t}{n}\mathbf1
\right).
\]
A direct calculation gives
\[
\|\nu_{S,T}\|^2
=
\frac{s(n-s)+t(n-t)}n
=
\frac{Q}{2n}.
\tag{15}
\]

At the point (3), the slack in (8) is
\[
\ell_{S,T}
=
\mu_n(s+t)
-
\frac{s(s+1)+t(t+1)}2
-1
=
\frac Q4+\frac wn.
\tag{16}
\]
Hence the Euclidean distance from (3) to this facet is
\[
\delta_{S,T}
=
\frac{\ell_{S,T}}{\|\nu_{S,T}\|}
=
\sqrt{\frac{nQ}{8}}
+
w\sqrt{\frac{2}{nQ}}.
\tag{17}
\]

First suppose
\[
w\ge1.
\]
Since
\[
|d|\le n-w,
\]
equation (14) gives
\[
Q
\ge
n^2-w^2-(n-w)^2
=
2w(n-w)
\ge
2(n-1).
\tag{18}
\]
For fixed
\[
w,
\]
the right-hand side of (17) is strictly increasing as a function of
\[
Q
\]
throughout this range, because
\[
Q>\frac{4w}{n}.
\]
It is also increasing in
\[
w.
\]
Therefore
\[
\delta_{S,T}
\ge
\sqrt{\frac{n(n-1)}4}
+
\frac1{\sqrt{n(n-1)}}
=
\frac{n^2-n+2}{2\sqrt{n(n-1)}}.
\tag{19}
\]
Equality requires
\[
w=1,
\qquad
Q=2(n-1),
\]
and consequently
\[
|d|=n-1.
\]
This is exactly the case
\[
(S,T)=(\{i\},[n])
\]
or
\[
(S,T)=([n],\{i\}),
\]
namely the coordinate facets (5).

Now suppose
\[
w=0.
\]
Then
\[
u,v\ge1,
\]
so
\[
|d|\le n-2
\]
and
\[
Q\ge4(n-1).
\]
Equation (17) reduces to
\[
\delta_{S,T}
=
\sqrt{\frac{nQ}{8}}
\ge
\sqrt{\frac{n(n-1)}2}.
\]
For
\[
n\ge3,
\]
this is strictly larger than the value in (19), since
\[
(\sqrt2-1)n(n-1)>2.
\]
Thus no disjoint bisubset facet is tangent.

Equations (12) and (19) prove (3)--(5).

It remains to analyze
\[
n=2.
\]
Here
\[
C_2=4.
\]
Write an arbitrary point in the affine hull as
\[
x=(2+p,2-p),
\qquad
y=(2+q,2-q).
\tag{20}
\]
The four coordinate facets have distances
\[
\sqrt2(1+p),\quad
\sqrt2(1-p),\quad
\sqrt2(1+q),\quad
\sqrt2(1-q).
\tag{21}
\]
The two remaining facets come from the complementary singleton bisubsets and have distances
\[
1+p-q,
\qquad
1-p+q.
\tag{22}
\]
The two quantities in (22) sum to
\[
2,
\]
so every inscribed ball has radius at most
\[
1.
\]
At radius
\[
1,
\]
both inequalities in (22) force
\[
p=q.
\]
The coordinate-facet conditions (21) then become
\[
|p|
\le
1-\frac1{\sqrt2}.
\]
This is exactly the segment in (7), completing the proof.

## Verification
The proof is symbolic and covers every
\[
n\ge2.
\]

The critical source premise was checked directly in the full text and page image: Proposition 3.8 gives exactly the affine equations (1) and the bisubset facet inequalities (8), and states that the description is minimal.

The accompanying `verify.py` checks every cardinality pair
\[
(s,t)
\]
allowed by the bisubset conditions for
\[
3\le n\le200.
\]
It computes the exact rational slack and projected-normal norm squared, verifies that the smallest centered facet distance occurs only at
\[
(s,t)=(1,n)
\]
and
\[
(s,t)=(n,1),
\]
and verifies the closed formula (4). It separately checks the complete rank-two incenter segment from the six explicit facet distances. These finite checks are corroborative only.

## Relationship to prior work
Ardila and Escobar introduce the harmonic polytope as the Minkowski sum of a product of permutohedra and a diagonal simplex. They determine its face structure, vertices, all
\[
3^n-3
\]
facets, and its volume. Proposition 3.8 is the exact structural input used here.

The same object has subsequently been studied combinatorially through its vertex degrees and simple vertices. Those local one-skeleton statements do not determine the distance from an interior point to the facet hyperplanes and therefore do not imply the present inradius theorem.

The related bipermutahedron contains the harmonic polytope as a Minkowski summand and has a different, finer normal fan. A metric result about the bipermutahedron's vertex radii does not determine the harmonic polytope's largest inscribed ball.

The inspected harmonic-polytope full text contains no occurrence of “inradius”, “Chebyshev”, or “inscribed”. Its use of Euclidean geometry is for volume normalization and an auxiliary edge-polytope sphere, not for the metric invariant computed here. Targeted literature and published-result searches under “harmonic polytope”, “inradius”, “Chebyshev center”, “largest inscribed ball”, and facet-distance formulations did not locate a theorem implying (3)--(7).

## Limitations
The metric formula is specific to the standard realization
\[
H_{n,n}=(\Pi_n\times\Pi_n)+D_n.
\]
It is not affine invariant.

The theorem does not determine the circumradius, John ellipsoid, or complete Euclidean distance spectrum.

The facet-distance optimization is short once the source's minimal
\[
H
\]
-description is available. An equivalent observation could therefore exist under general Chebyshev-center terminology without naming the harmonic polytope; this remains the principal originality risk.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, first public version 2020-06-04; Selecta Mathematica 27 (2021), DOI 10.1007/s00029-021-00687-6.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, first public version 2020-08-05; Combinatorial Theory 2 (2022), no. 3.
