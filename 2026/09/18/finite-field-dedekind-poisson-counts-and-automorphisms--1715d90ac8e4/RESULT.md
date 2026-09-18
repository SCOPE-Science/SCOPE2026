# Finite-field enumeration and automorphism orders for Dedekind Poisson algebras

## Statement

Let \(\mathbb F_q\) be a finite field and let \(N_q(n)\) denote the number of \(\mathbb F_q\)-isomorphism classes of \(n\)-dimensional Dedekind Poisson algebras, where a Dedekind Poisson algebra means that every Poisson subalgebra is a Poisson ideal.

Then

\[
N_q(n)=
\begin{cases}
2,&n=1,\\
3,&n=2,\\
4,&n\ge 3,
\end{cases}
\qquad (q\text{ even}),
\]

and

\[
N_q(n)=
\begin{cases}
2,&n=1,\\
3,&n=2,\\
(q+9)/2,&n=3,\\
q+5,&n\ge4,
\end{cases}
\qquad (q\text{ odd}).
\]

For odd \(q\), the mixed classes (both associative and Lie products nonzero) are parametrized by the nonsquares \(\kappa\in\mathbb F_q^\times\). Hence the number of mixed classes is

\[
0\quad(n<3),\qquad \frac{q-1}{2}\quad(n=3),\qquad q-1\quad(n\ge4).
\]

The same classification gives the automorphism-group order of every finite-dimensional class explicitly.

## Input from the arbitrary-field classification

Plakosh and Pypka classify Dedekind Poisson algebras over arbitrary fields. In their Type II case one has

\[
P=E\oplus Z\oplus V\oplus Fc,
\]

where \(E=0\) or \(Fe\) with \(e^2=e\), \(Z\) is a zero Poisson algebra, \(V\ne0\), and the only further nonzero operations are

\[
uv=\beta(u,v)c,\qquad [u,v]=\omega(u,v)c\qquad(u,v\in V).
\]

Here \(\beta\) is symmetric and anisotropic in the sense that \(\beta(v,v)\ne0\) for every \(v\ne0\), and \(\omega\) is alternating. Their isomorphism criterion identifies two such algebras exactly when the presence of \(E\), the dimension of \(Z\), and the simultaneous-similarity class of \((\beta,\omega)\) agree. Type I consists of a zero algebra, optionally with one idempotent summand \(Fe\).

The finite-field problem is therefore the explicit orbit problem for the active pair \((\beta,\omega)\).

## Finite-field collapse of the active dimension

Write \(d=\dim V\).

If \(q\) is even, \(\mathbb F_q\) is perfect. In characteristic two,

\[
\beta(v,v)=\sum_i b_{ii}v_i^2
\]

is the square of a linear form. If \(d\ge2\), that linear form has a nonzero kernel vector, contradicting anisotropy. Thus

\[
d=1\qquad(q\text{ even}).
\]

In particular \(\omega=0\).

If \(q\) is odd and \(d\ge3\), the homogeneous quadratic polynomial \(v\mapsto\beta(v,v)\) has a nonzero zero by Chevalley--Warning, since its degree is two and the number of variables exceeds two. Hence

\[
d\le2\qquad(q\text{ odd}).
\]

Thus only one- and two-dimensional active pairs occur over finite fields.

## Normal forms

Let \(\epsilon\in\{0,1\}\) record whether the idempotent summand \(E\) is present, and let \(z=\dim Z\). All products and brackets not displayed below are zero; when \(\epsilon=1\), \(e^2=e\) and \(e\) annihilates the remaining summands.

### Active dimension one

There is exactly one active-pair class over every finite field:

\[
P^{(1)}_{\epsilon,z}=E_\epsilon\oplus Z\oplus Fx\oplus Fc,
\qquad x^2=c.
\]

Indeed, a nonzero one-dimensional symmetric form is unique up to the common scalar allowed by simultaneous similarity.

### Active dimension two, zero bracket

Assume \(q\) is odd and fix one nonsquare \(\nu\in\mathbb F_q^\times\). There is exactly one class with \(d=2\) and \(\omega=0\):

\[
P^{(2,0)}_{\epsilon,z}:
\qquad x^2=c,\quad y^2=-\nu c,\quad xy=0.
\]

All anisotropic binary symmetric forms over \(\mathbb F_q\) have the same similarity class.

### Active dimension two, nonzero bracket

Assume \(q\) is odd. For every nonsquare \(\kappa\in\mathbb F_q^\times\), put

\[
P^{(2,\kappa)}_{\epsilon,z}:
\qquad
x^2=c,\quad xy=0,\quad y^2=-\kappa^{-1}c,\quad [x,y]=c.
\]

These are pairwise non-isomorphic, and every mixed active pair is isomorphic to exactly one of them.

To see this invariant intrinsically, let \(T\in\operatorname{End}(V)\) be defined by

\[
\omega(u,v)=\beta(u,Tv).
\]

When \(\omega\ne0\), \(T\) is invertible and \(\beta\)-skew-adjoint. In dimension two it has trace zero, hence

\[
T^2=\kappa I,
\qquad
\kappa=-\det T=-\frac{\det\omega}{\det\beta}.
\]

Since \(\det\omega\) is a square and anisotropy of the binary form is equivalent to \(-\det\beta\) being a nonsquare, \(\kappa\) is a nonsquare. Simultaneous similarity conjugates \(T\), so \(\kappa\) is unchanged. Conversely, for every nonsquare \(\kappa\), the displayed normal form has \(T^2=\kappa I\), and the skew-adjoint relation determines the binary symmetric form up to the common scalar. Hence \(\kappa\) is a complete invariant for the mixed active pair.

There are therefore \((q-1)/2\) mixed active-pair classes.

## Enumeration

Type I contributes two classes in every positive dimension: the zero algebra and the algebra \(Fe\oplus Z\) with \(e^2=e\).

A Type II class with active dimension \(d\) has dimension

\[
n=\epsilon+z+d+1.
\]

For even \(q\), only \(d=1\) occurs. This gives one additional class in dimension two and two additional classes in every dimension at least three, proving

\[
N_q(1)=2,\quad N_q(2)=3,\quad N_q(n)=4\ (n\ge3).
\]

For odd \(q\), \(d=1\) again contributes one class in dimension two and two in each dimension at least three. The \(d=2\) sector has

\[
1+\frac{q-1}{2}=\frac{q+1}{2}
\]

active-pair classes: one with zero bracket and \((q-1)/2\) mixed classes. It occurs once when \(n=3\) and twice when \(n\ge4\), according to \(\epsilon=0\) or \(1\). This yields

\[
N_q(3)=2+2+\frac{q+1}{2}=\frac{q+9}{2}
\]

and, for every \(n\ge4\),

\[
N_q(n)=2+2+2\frac{q+1}{2}=q+5.
\]

Equivalently, the ordinary generating functions are

\[
\sum_{n\ge1}N_q(n)t^n
=2t+3t^2+\frac{4t^3}{1-t}
\qquad(q\text{ even}),
\]

and

\[
\sum_{n\ge1}N_q(n)t^n
=2t+3t^2+\frac{q+9}{2}t^3+\frac{(q+5)t^4}{1-t}
\qquad(q\text{ odd}).
\]

## Automorphism-group orders

Put

\[
G_z(q)=|\operatorname{GL}_z(q)|=\prod_{i=0}^{z-1}(q^z-q^i),
\qquad G_0(q)=1.
\]

For Type I, the zero algebra of dimension \(n\) has automorphism group of order \(G_n(q)\), while \(Fe\oplus Z\) has order \(G_{n-1}(q)\), because the unique nonzero idempotent is fixed.

For Type II, \(Fc=P^2\) is characteristic and \(Z\oplus Fc=\operatorname{Ann}(P(+ ,\cdot))\) is characteristic. Every automorphism is uniquely of triangular form

\[
\begin{aligned}
c&\mapsto \lambda c,\\
z_0&\mapsto A z_0+\mu(z_0)c,\\
v&\mapsto \phi(v)+L(v)+r(v)c,
\end{aligned}
\]

where \(A\in\operatorname{GL}(Z)\), \(\mu\in Z^*\), \(L\in\operatorname{Hom}(V,Z)\), \(r\in V^*\), and

\[
\beta(\phi u,\phi v)=\lambda\beta(u,v),\qquad
\omega(\phi u,\phi v)=\lambda\omega(u,v).
\]

Thus

\[
|\operatorname{Aut}P|
=q^{dz+d+z}G_z(q)\,|\operatorname{Sim}(\beta,\omega)|.
\]

The active simultaneous-similitude groups are elementary:

\[
|\operatorname{Sim}(\beta,0)|=q-1\qquad(d=1),
\]

\[
|\operatorname{Sim}(\beta,0)|=2(q^2-1)
\qquad(d=2,\ q\text{ odd}),
\]

and

\[
|\operatorname{Sim}(\beta,\omega)|=q^2-1
\qquad(d=2,\ \omega\ne0).
\]

Consequently

\[
\boxed{|\operatorname{Aut}P^{(1)}_{\epsilon,z}|
=q^{2z+1}G_z(q)(q-1)},
\]

\[
\boxed{|\operatorname{Aut}P^{(2,0)}_{\epsilon,z}|
=2q^{3z+2}G_z(q)(q^2-1)},
\]

and

\[
\boxed{|\operatorname{Aut}P^{(2,\kappa)}_{\epsilon,z}|
=q^{3z+2}G_z(q)(q^2-1)}.
\]

For the pure two-dimensional active form, the similitude group is \(GO^-(2,q)\), of order \(2(q^2-1)\). For a mixed pair, the two simultaneous similitude conditions force \(\phi\) to commute with \(T\). Since \(T^2=\kappa I\) with \(\kappa\) nonsquare,

\[
\mathbb F_q[T]\cong\mathbb F_{q^2},
\]

and every nonzero element \(aI+bT\) is automatically a simultaneous similitude; hence the active group is \(\mathbb F_{q^2}^{\times}\), of order \(q^2-1\). Thus turning on the bracket cuts the active similitude group by a factor of two.

## Relation to prior work and novelty boundary

The arbitrary-field structural classification, the decomposition into \(E\oplus Z\oplus V\oplus Fc\), and the simultaneous-similarity criterion are due to Plakosh--Pypka. General classification problems for pairs of bilinear forms are classical and can be wild in larger dimensions; no novelty is claimed for that general theory. Petrov--Pypka also give a contemporaneous classification of Poisson algebras in dimensions at most three, so low-dimensional normal-form phenomena are likewise not claimed as new.

The contribution here is the finite-field specialization of the Dedekind classification: the collapse to \(d\le1\) in even characteristic and \(d\le2\) in odd characteristic, the exact nonsquare parameter for the mixed Dedekind sector, the all-dimension isomorphism counts (including stabilization at \(q+5\) for odd \(q\)), and the automorphism-order formulas above. Targeted searches did not locate these finite-field enumeration or automorphism formulas in the existing Dedekind Poisson literature.

Originality is therefore asserted only to the best of our knowledge. Both 2026 source papers are recent preprints, so later revisions or concurrent independent derivations remain a material risk.

## References

- A. I. Plakosh and O. O. Pypka, *Dedekind Poisson Algebras over Arbitrary Fields*, arXiv:2609.13767v1 (2026), https://arxiv.org/abs/2609.13767.
- A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784v1 (2026), https://arxiv.org/abs/2609.13784.
- G. Belitskii, V. M. Bondarenko, R. Lipyanski, V. V. Plachotnik and V. V. Sergeichuk, *The problems of classifying pairs of forms and local algebras with zero cube radical are wild*, Linear Algebra Appl. 402 (2005), 135--142, https://doi.org/10.1016/j.laa.2004.12.016.
