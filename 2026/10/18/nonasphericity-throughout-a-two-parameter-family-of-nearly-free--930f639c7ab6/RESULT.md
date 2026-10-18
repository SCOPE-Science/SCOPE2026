# Nonasphericity throughout a two-parameter family of nearly free line arrangements

## Finding
For all integers \(2\le p\le q\), consider the projective line arrangement in \(\mathbb P^2_{\mathbb C}\) with equation
\[
F_{p,q}(x,y,z)=x(y-z)\prod_{i=1}^{p-1}(x-iy)\prod_{j=2}^{q}(x-jz)=0.
\]
Its complement is **not** an Eilenberg–Mac Lane space \(K(\pi,1)\). The family is nearly free by the construction of Dimca–Sticlaru [1]. The assertion settles the asphericity status of every member of that family, not merely the previously known subfamilies.

## Assumptions and scope
All arrangements and complements are over \(\mathbb C\). The integers satisfy \(2\le p\le q\); empty index ranges mean empty products. Nonasphericity means that at least one higher homotopy group of the complement is nonzero, without determining which group. We use two established arrangement-topology theorems: the simple-triangle obstruction to asphericity [2], and invariance of the complement under a lattice isotopy [3].

## Proof
Remove the distinguished line \(x=0\) and set \(x=1\). The affine complement is the complement in \(\mathbb C^2\) of three kinds of lines:
\[
V_i:\ y=1/i\quad(1\le i\le p-1),\qquad
H_j:\ z=1/j\quad(2\le j\le q),\qquad D:\ z=y.
\]
The only finite triple points are \(V_i\cap H_i\cap D\) for \(2\le i\le p-1\); all other finite intersection points have multiplicity two. At infinity, the vertical and horizontal parallel classes form their own distinct multiple points, and the diagonal meets the line at infinity at a third point. For the minimal values of \(p,q\), multiplicity-two classes are interpreted in the usual way.

To deform the arrangement, keep the vertical lines fixed. Introduce a diagonal \(D_{s,c}: z=c+sy\), shared horizontal lines \(H_j:z=c+s/j\) for \(2\le j\le p-1\), and additional horizontal lines \(H_j:z=c+s u_j\) for \(p\le j\le q\). Require \(s\in\mathbb C^*\), \(c\in\mathbb C\), and mutually distinct \(u_p,\ldots,u_q\) outside the fixed finite set \(\{1,1/2,\ldots,1/(p-1)\}\). Thus every deformation has precisely the same labelled intersection lattice: a triple point on the diagonal occurs exactly at the shared index, and no additional horizontal passes through a diagonal–vertical intersection. The three points at infinity remain distinguished. The parameter space
\[
\mathbb C^*\times\mathbb C\times\operatorname{Conf}_{q-p+1}\!\bigl(\mathbb C\setminus\{1/i:1\le i<p\}\bigr)
\]
is path-connected. A piecewise smooth path in it is a lattice isotopy; by Randell's theorem [3], the complex arrangement complements at any two parameters are diffeomorphic.

The original arrangement corresponds to \(s=1\), \(c=0\), and \(u_j=1/j\) for \(p\le j\le q\). Choose instead \(s=-1\), \(c=1\), and
\[
u_j=1-b_j,\qquad b_j=\frac{1}{4(j-p+2)}\quad(p\le j\le q).
\]
The new diagonal is \(z=1-y\); the shared horizontals have heights \(1-1/j\ge1/2\), and the extra horizontals have pairwise distinct heights \(b_j\in(0,1/2)\). Put \(b=b_q\), the smallest horizontal height. The lines \(V_1:y=1\), \(H_q:z=b\), and \(D:z=1-y\) enclose an open bounded triangular chamber in the real affine plane, with vertices
\[
(1,0),\qquad(1,b),\qquad(1-b,b).
\]
Inside this triangle, \(y>1-b>1/2\) and \(0<z<b\). No other vertical meets it, since the remaining verticals have \(y\le1/2\). No other horizontal meets it, since \(b\) was chosen smallest. Its three vertices are each on exactly the two displayed incident lines: at \((1,0)\) all horizontal heights are positive, at \((1,b)\) the diagonal has height zero, and at \((1-b,b)\) every vertical has abscissa either \(1\) or at most \(1/2\). Thus the real arrangement has a **simple triangular chamber**.

The simple-triangle criterion of Falk–Randell [2] implies that the complement of the complexification of this arrangement is not \(K(\pi,1)\). By lattice-isotopy invariance [3], the original affine complement, hence the stated projective complement, is likewise not \(K(\pi,1)\) for every allowed \(p,q\).

## Verification
The supplied standalone script `verify_incidence.py` performs exact rational-arithmetic checks for \(2\le p\le13\) and \(p\le q\le16\), including every labelled finite intersection incidence and the three simple-triangle vertex conditions: 114 parameter pairs pass. Its finite enumeration is only an independent sanity check. The infinite result follows from the connected parameter space, explicit incidence classification, and the two cited arrangement-topology theorems. The source formula, deconing convention, and boundary values \(p=q=2\) are covered by the proof.

## Relationship to prior work
Dimca and Sticlaru [1, Proposition 4.3] proved nonasphericity for the subfamily \(p=2\) and the additional case \(p=q=3\) and constructed the larger nearly free family [1, Theorem 3.4]. The statement here contains those cases and establishes the remaining parameter region by a lattice isotopy that exposes a simple real triangular chamber. The obstruction theorem [2] and invariance theorem [3] are established ingredients; the contribution is the uniform deformation and its application to the previously untreated family. Later work on nearly supersolvable arrangements [4] concerns algebraic structure and does not, from its inspected abstract, establish this all-parameter topological statement.

## Limitations
This result determines failure of asphericity, not the first nonzero higher homotopy group or its module structure. It applies only to the explicitly defined Dimca–Sticlaru family over \(\mathbb C\), not to all nearly free arrangements. The literature comparison includes primary text for [1], theorem-level sourcing for [2] and [3], and abstract-level inspection for [4]; a comprehensive survey of all subsequent publications was not possible. The accompanying finite script is not a proof of the infinite statement.

## References
[1] A. Dimca and G. Sticlaru, *On the exponents of free and nearly free projective plane curves*, arXiv:1511.08938, first posted 2015-11-28, Theorem 3.4 and Proposition 4.3.

[2] M. Falk and R. Randell, simple-triangle obstruction to the \(K(\pi,1)\) property (1987), Corollary 3.3, as cited in [1] and in *On connected subgraph arrangements* (2026), Lemma 7.4.

[3] R. Randell, *Lattice-isotopic arrangements are topologically isomorphic*, Proceedings of the American Mathematical Society **107** (1989), 555–559, DOI: 10.2307/2047847.

[4] A. Dimca and G. Sticlaru, *On supersolvable and nearly supersolvable line arrangements*, arXiv:1712.03885, first posted 2017-12-11.
