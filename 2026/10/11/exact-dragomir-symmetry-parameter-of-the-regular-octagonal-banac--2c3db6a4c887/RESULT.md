# Exact Dragomir symmetry parameter of the regular octagonal Banach plane
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,t)
=
\max\left\{
|s|,
|t|,
\frac{|s|+|t|}{\sqrt2}
\right\}.
\]
For vectors \(u,v\), write
\[
u\perp_D^\varepsilon v
\]
when
\[
N_8(u+\lambda v)
\ge
\sqrt{1-\varepsilon^2}\,N_8(u)
\qquad
\text{for every }\lambda\in\mathbb R.
\]
Define the optimal global Dragomir symmetry parameter by
\[
\sigma_D(X_8)
=
\inf\left\{
\varepsilon\in[0,1):
x\perp_B y
\Longrightarrow
y\perp_D^\varepsilon x
\text{ for all }x,y\in X_8
\right\}.
\]

Then
\[
\boxed{
\sigma_D(X_8)
=
\sqrt{\frac{5-2\sqrt2}{8}}
}.
\tag{1}
\]

Equivalently, every unit Birkhoff--James pair \(x\perp_B y\) satisfies the sharp reverse-line separation
\[
\boxed{
\inf_{\lambda\in\mathbb R}N_8(y+\lambda x)
\ge
\frac{2+\sqrt2}{4}
}.
\tag{2}
\]
Equality in (2) is attained, for example, by
\[
x=(1,\sqrt2-1),
\qquad
y=(0,-1).
\tag{3}
\]

## Assumptions and scope
All scalars are real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N_8(x+\lambda y)\ge N_8(x)
\text{ for every }\lambda\in\mathbb R.
\]

The modified Dragomir approximate orthogonality used here is the normalization from the motivating paper:
\[
u\perp_D^\varepsilon v
\quad\Longleftrightarrow\quad
N_8(u+\lambda v)
\ge
\sqrt{1-\varepsilon^2}\,N_8(u)
\text{ for every }\lambda\in\mathbb R.
\]
Thus, for \(u\ne0\),
\[
u\perp_D^\varepsilon v
\quad\Longleftrightarrow\quad
\operatorname{dist}(u,\mathbb Rv)
\ge
\sqrt{1-\varepsilon^2}\,N_8(u).
\tag{4}
\]

Put
\[
r=\sqrt2-1.
\]
The unit ball has vertices
\[
(1,r),\ (r,1),\ (-r,1),\ (-1,r)
\]
and their negatives.

## Proof
By homogeneity, it is enough to consider
\[
x,y\in S_{X_8},
\qquad
x\perp_B y.
\tag{5}
\]
By a dihedral isometry of the regular octagon, move \(x\) to the vertical edge
\[
x=(1,t),
\qquad
-r\le t\le r.
\tag{6}
\]

For any linearly independent unit vectors \(x,y\), define
\[
d(x,y)
=
\operatorname{dist}(y,\mathbb Rx)
=
\inf_{\lambda\in\mathbb R}N_8(y+\lambda x).
\]
Let
\[
h_x(z)=\det(x,z).
\]
The annihilator of \(\mathbb Rx\) is one-dimensional, so quotient duality gives
\[
d(x,y)
=
\frac{|\det(x,y)|}
{\sup_{z\in B_{X_8}}|\det(x,z)|}.
\tag{7}
\]
For \(x=(1,t)\), a direct check on the eight vertices gives
\[
\sup_{z\in B_{X_8}}|\det(x,z)|
=
1+r|t|.
\tag{8}
\]

First suppose
\[
-r<t<r.
\]
The point \(x\) lies in the relative interior of the facet \(s=1\), whose unique supporting functional is
\[
f(s,t)=s.
\]
Since \(x\perp_B y\), James's supporting-functional criterion forces
\[
f(y)=0.
\]
Therefore
\[
y=(0,\pm1).
\]
Equations (7) and (8) give
\[
d(x,y)
=
\frac{1}{1+r|t|}
\ge
\frac{1}{1+r^2}.
\tag{9}
\]

It remains to treat the vertices. Reflection reduces them to
\[
x=(1,r).
\]
The norm-one supporting functionals at \(x\) form the segment joining
\[
(1,0)
\qquad\text{and}\qquad
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right).
\]
Hence every direction \(y\) for which \(x\perp_B y\) can be written, up to sign, as
\[
y
=
\frac{(q,-1)}{N_8(q,-1)},
\qquad
0\le q\le1.
\tag{10}
\]
Moreover,
\[
N_8(q,-1)
=
\begin{cases}
1,&0\le q\le r,\\[4pt]
\dfrac{1+q}{\sqrt2},&r\le q\le1.
\end{cases}
\tag{11}
\]
For this vertex, (8) becomes
\[
\sup_{z\in B_{X_8}}|\det(x,z)|
=
1+r^2.
\tag{12}
\]
Using (7), (10), and (12),
\[
d(x,y)
=
\frac{1+rq}
{(1+r^2)N_8(q,-1)}.
\tag{13}
\]

If
\[
0\le q\le r,
\]
then (11) and (13) give
\[
d(x,y)
\ge
\frac1{1+r^2}.
\tag{14}
\]
If
\[
r\le q\le1,
\]
then
\[
\frac{1+rq}{N_8(q,-1)}
=
\frac{\sqrt2(1+rq)}{1+q}.
\]
The exact identity
\[
\sqrt2(1+rq)-(1+q)
=
r(1-q)
\ge0
\]
again yields
\[
d(x,y)
\ge
\frac1{1+r^2}.
\tag{15}
\]

Therefore every pair in (5) satisfies
\[
d(x,y)
\ge
\frac1{1+r^2}
=
\frac{2+\sqrt2}{4}.
\tag{16}
\]

For the pair in (3), the supporting functional \(f(s,t)=s\) shows
\[
x\perp_B y.
\]
Equation (7) gives equality in (16). Thus the reverse-line separation constant is exactly
\[
d_0=\frac{2+\sqrt2}{4}.
\]

Finally, by (4), the least admissible global \(\varepsilon\) is determined by
\[
\sqrt{1-\varepsilon^2}=d_0.
\]
Hence
\[
\varepsilon^2
=
1-\left(\frac{2+\sqrt2}{4}\right)^2
=
\frac{5-2\sqrt2}{8},
\]
which proves (1).

## Verification
The proof is exact and finite after the dihedral reduction. The only boundary cases are the interior of one edge and one representative vertex.

The bundled `verify.py` checks symbolically that
\[
\frac1{1+(\sqrt2-1)^2}
=
\frac{2+\sqrt2}{4},
\]
that the stated \(\sigma_D\) is exactly
\[
\sqrt{1-d_0^2},
\]
and that the two vertex branches in (11)--(15) never fall below \(d_0\). It also samples every edge and every normal-cone direction to stress-test the classification.

The numerical sampling is not used as an infinite proof. The continuum result follows from (8)--(15).

## Relationship to prior work
Chmieliński, Khurana and Sain introduced the global \(D\)-approximate symmetry question in the form used here and proved that every finite-dimensional Banach space has some global parameter strictly below \(1\). Their proof is compactness-based and does not compute the optimal parameter. In the same paper they prove qualitative \(C\)-approximate symmetry for every regular polygonal Banach plane with at least six vertices, including the octagon; that is a different approximate-orthogonality relation and gives no numerical value for \(\sigma_D(X_8)\).

A later published exact result computes the optimal \(D\)-symmetry parameter for the Hölder-dual planes \(\ell_3^2\) and \(\ell_{3/2}^2\). It confirms that the optimal parameter is a natural quantitative invariant, but it concerns smooth nonpolyhedral norms and does not imply the octagonal value.

Targeted searches used the exact \(D\)-approximate-symmetry terminology, the regular-octagon aliases, the candidate radical, and the equivalent reverse-line-distance formulation. No covering regular-octagonal formula was located.

## Limitations
The calculation is specific to the regular octagonal norm.

No formula is claimed here for all regular \(2n\)-gonal Banach planes. The argument does suggest that such a family problem reduces to finitely many facet and vertex-normal configurations, but that extension is not proved.

The result concerns Dragomir's modified \(D\)-approximate orthogonality. It does not compute the optimal parameter for the distinct \(C\)-approximate symmetry relation.

Bibliographic and semantic searches cannot prove absolute novelty; an equivalent formula could have appeared under a different normalization of approximate orthogonality.

## References
1. J. Chmieliński, D. Khurana and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162v1, 15 December 2020; later published in *Results in Mathematics* 76 (2021), article 136, doi:10.1007/s00025-021-01437-y.
