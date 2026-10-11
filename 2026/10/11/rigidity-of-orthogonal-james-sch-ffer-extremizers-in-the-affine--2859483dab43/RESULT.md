# Rigidity of orthogonal James--Schäffer extremizers in the affine-regular hexagon
## Finding
Let \(X=(\mathbb R^2,N)\) with
\[
N(u,v)=\max\{|u|,|v|,|u-v|\},
\]
the affine-regular hexagonal norm. For Birkhoff--James orthogonality \(x\perp_B y\), set
\[
J_\perp(X)=\sup_{\substack{x,y\in S_X\\x\perp_B y}}
\min\{N(x-y),N(x+y)\},
\qquad
g_\perp(X)=\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\max\{N(x-y),N(x+y)\}.
\]
Then
\[
J_\perp(X)=g_\perp(X)=\frac32.
\]
More strongly, for every unit Birkhoff pair \(x\perp_B y\), the following are equivalent:
\[
\min\{N(x-y),N(x+y)\}=\frac32,
\]
\[
\max\{N(x-y),N(x+y)\}=\frac32,
\]
and, up to a linear isometry of \(X\), replacing \(y\) by \(-y\), and reversing the ordered pair,
\[
(x,y)=\left((1,0),\left(\frac12,1\right)\right).
\]
Hence every extremizer of either orthogonal constant is automatically isosceles,
\[
N(x-y)=N(x+y)=\frac32,
\]
and all extremizers form one symmetry orbit.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N(x+\lambda y)\ge N(x)
\qquad(\lambda\in\mathbb R).
\]
The unit ball is the affine-regular hexagon with vertices
\[
(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1).
\]
The claim concerns complete equality cases for the orthogonal James and Schäffer constants on this single plane.

## Proof
Two linear isometries are
\[
R(u,v)=(u-v,u),
\qquad
S(u,v)=(v,u),
\]
because each merely permutes the three quantities
\[
|u|,\quad |v|,\quad |u-v|.
\]
They generate symmetries transitive on the six vertices and on the six open edges. It therefore suffices to treat one open edge and one vertex.

First let
\[
x=(1,t),\qquad 0<t<1.
\]
The unique norming functional of \(x\) is
\[
f(u,v)=u.
\]
Thus \(x\perp_B y\) for a unit vector \(y\) if and only if \(f(y)=0\), hence
\[
y=(0,1)\quad\text{or}\quad y=(0,-1).
\]
Changing the sign of \(y\) only interchanges \(x+y\) and \(x-y\), so take \(y=(0,1)\). Directly,
\[
N(x+y)=1+t,
\qquad
N(x-y)=2-t.
\]
Consequently
\[
\min\{N(x-y),N(x+y)\}
=
1+\min\{t,1-t\}
\le\frac32
\]
and
\[
\max\{N(x-y),N(x+y)\}
=
2-\min\{t,1-t\}
\ge\frac32.
\]
Equality in either inequality holds exactly when
\[
t=\frac12,
\]
and then both chord lengths equal \(3/2\).

Now let
\[
x=(1,0).
\]
The norming functionals of this vertex are exactly
\[
f_a(u,v)=u-av,
\qquad
0\le a\le1.
\]
Thus a unit vector \(y\) satisfies \(x\perp_B y\) precisely when, after possibly replacing \(y\) by \(-y\),
\[
y=(a,1)
\qquad\text{for some }0\le a\le1.
\]
For these pairs,
\[
N(x+y)=1+a,
\qquad
N(x-y)=2-a.
\]
Hence
\[
\min\{N(x-y),N(x+y)\}
=
1+\min\{a,1-a\}
\le\frac32
\]
and
\[
\max\{N(x-y),N(x+y)\}
=
2-\min\{a,1-a\}
\ge\frac32,
\]
with equality in either case exactly at
\[
a=\frac12.
\]

Every unit vector lies either in an open edge or at a vertex, so these two cases are exhaustive. The pair
\[
\left((1,0),\left(\frac12,1\right)\right)
\]
has
\[
N(x-y)=N(x+y)=\frac32.
\]
This proves the two constants and their equality cases.

It remains only to identify the orbit. The open-edge equality pair
\[
\left(\left(1,\frac12\right),(0,1)\right)
\]
is obtained from the vertex equality pair by applying the reflection \(S\) and reversing the ordered pair. Since \(R\) and \(S\) are transitive on the corresponding boundary strata, every equality pair belongs to the stated single orbit.

## Verification
The proof is an exhaustive support-functional calculation. On an open edge the norming functional is unique. At a vertex the entire norming-functional segment
\[
\{f_a:0\le a\le1\}
\]
is used, so no nonsmooth Birkhoff directions are omitted.

Both strata reduce to the same exact pair of chord lengths,
\[
1+s,\qquad 2-s,
\qquad 0\le s\le1.
\]
Their minimum is at most \(3/2\), their maximum is at least \(3/2\), and equality in either statement occurs only at \(s=1/2\). No finite sampling or numerical optimization is used.

## Relationship to prior work
Baronti and Papini introduced \(J_\perp\) and \(g_\perp\) and, in their Example 5.1, computed the values
\[
J_\perp(X)=g_\perp(X)=\frac32
\]
for exactly this affine-regular hexagonal plane. Their example gives individual attaining pairs but does not classify all equality cases.

Arambašić, Guterman, Kuzma, Rajić, and Zhilina study symmetrized Birkhoff--James orthogonality and use the regular hexagonal norm as a canonical nonsmooth example with abundant mutual orthogonality. This supports the geometric relevance of the hexagon but does not determine the equality set for the two orthogonal constants.

A later preprint on Birkhoff-orthogonal Takahashi--von Neumann--Jordan type constants again singles out affine-regular hexagons as extremal Radon planes. Its public abstract and detailed public summary concern global constants and the affine-hexagon equality geometry, not the complete pair-level classification proved here; the full text was not available through the checked access route and remains a residual comparison risk.

## Limitations
The theorem is only an equality-case classification for one real two-dimensional norm. It does not provide a family-wide classification for arbitrary polygonal or Radon planes.

The originality conclusion rests on the inspected primary literature and targeted semantic searches. A differently phrased pair-level classification outside the checked sources remains possible.

## References
1. M. Baronti and C. Franchetti, “The isosceles orthogonality and a new 2-dimensional parameter in real normed spaces,” *Aequationes Mathematicae* 89 (2015), 673--683, DOI 10.1007/s00010-014-0255-9; first published online 2014-03-14.
2. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” *Constructive Mathematical Analysis* 5 (2022), 37--45, DOI 10.33205/cma.1067323.
3. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, and S. Zhilina, “Symmetrized Birkhoff--James orthogonality in arbitrary normed spaces,” *Journal of Mathematical Analysis and Applications* 502 (2021), 125203, DOI 10.1016/j.jmaa.2021.125203.
4. J. Qi, Z. Yin, and Q. Liu, “Birkhoff-Orthogonal Takahashi-von Neumann-Jordan Type Constants in Banach Spaces,” arXiv:2608.07146, submitted 2026-08-07.
