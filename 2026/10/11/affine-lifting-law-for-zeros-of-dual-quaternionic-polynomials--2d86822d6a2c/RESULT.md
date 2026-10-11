# Affine lifting law for zeros of dual quaternionic polynomials

## Finding

Let
\[
P(x)=\sum_{\ell=0}^{d}x^\ell(q_\ell+\epsilon r_\ell)
\]
be a one-sided dual quaternionic polynomial. Write
\[
g(x)=\sum_{\ell=0}^{d}x^\ell q_\ell,
\qquad
h(x)=\sum_{\ell=0}^{d}x^\ell r_\ell
\]
for its quaternionic primal and dual coefficient polynomials.

For every fixed
\[
x_1\in\mathbb H,
\]
the zeros of \(P\) over the full dual fiber
\[
x_1+\epsilon\mathbb H
\]
are completely controlled by the real differential of \(g\):
\[
P(x_1+\epsilon x_2)
=
g(x_1)
+
\epsilon\left(h(x_1)+dg_{x_1}(x_2)\right).
\]
Hence a zero can lie over \(x_1\) only if
\[
g(x_1)=0.
\]
If \(x_1\) is a primal zero, then it lifts precisely when
\[
-h(x_1)\in\operatorname{im}dg_{x_1},
\]
and in that case the whole lift fiber is
\[
x_2^{(0)}+\ker dg_{x_1}
\]
for any one solution \(x_2^{(0)}\).

For a quaternionic slice regular polynomial, the differential rank is
\[
0,\ 2,\ \text{or }4
\]
at a nonreal point and
\[
0\ \text{or }4
\]
at a real point. Thus every nonempty dual lift fiber has real dimension
\[
4,\ 2,\ \text{or }0.
\]
In particular, if
\[
dg_{x_1}
\]
is invertible, the primal zero has the unique lift
\[
x_1-\epsilon(dg_{x_1})^{-1}h(x_1).
\]

The full-space statement produces zeros that the older quadratic-cone theory cannot see. For
\[
P_*(x)=x^2+1+\epsilon i,
\]
the complete zero set is
\[
\begin{aligned}
V(P_*)
={}&
\left\{
i+\epsilon\left(-\frac12+cj+dk\right):
c,d\in\mathbb R
\right\}\\
&\cup
\left\{
-i+\epsilon\left(\frac12+cj+dk\right):
c,d\in\mathbb R
\right\}.
\end{aligned}
\]
These are two affine real \(2\)-planes, and both are disjoint from the quadratic cone
\[
Q_{\mathbb{DH}}.
\]

## Assumptions and scope

The polynomial convention is the one used in arXiv:2609.35518v1:
\[
\mathbb{DH}[x]
=
\left\{
\sum_{\ell=0}^{d}x^\ell a_\ell
\right\},
\]
with coefficients on the right.

The recent paper embeds these polynomials into the newly defined dual slice regular functions on all of
\[
\mathbb{DH}.
\]
Its Theorem 7.2 supplies the differential extension formula used here, while Lemma 2.17 supplies the possible real ranks of differentials of quaternionic slice regular functions.

The finding classifies zeros fiber-by-fiber over the primal projection
\[
\pi_{\mathbb H}:\mathbb{DH}\to\mathbb H.
\]
It does not classify the set of primal zeros of \(g\); that is the usual quaternionic slice-regular zero problem.

## Proof

By Remark 8.2 of the source,
\[
P=g+\epsilon h
\]
with
\[
g,h\in\mathbb H[x].
\]
Since every polynomial in
\[
\mathbb{DH}[x]
\]
is dual slice regular on the full algebra, Theorem 7.2 applies without a nonreal restriction. It gives
\[
P(x_1+\epsilon x_2)
=
g(x_1)
+
\epsilon\left(
h(x_1)+dg_{x_1}(x_2)
\right).
\]

A dual quaternion vanishes exactly when its primal and dual parts both vanish. Therefore
\[
P(x_1+\epsilon x_2)=0
\]
is equivalent to the simultaneous conditions
\[
g(x_1)=0
\]
and
\[
dg_{x_1}(x_2)=-h(x_1).
\]
This immediately proves the lifting criterion.

If one solution \(x_2^{(0)}\) exists, all solutions are
\[
x_2^{(0)}+\ker dg_{x_1},
\]
so the fiber is an affine real subspace of dimension
\[
4-\operatorname{rank}_{\mathbb R}dg_{x_1}.
\]
Lemma 2.17 of the source gives the rank alternatives
\[
\{0,2,4\}
\]
at nonreal points and
\[
\{0,4\}
\]
at real points.

When
\[
dg_{x_1}
\]
is invertible, the affine equation has exactly one solution,
\[
x_2=-(dg_{x_1})^{-1}h(x_1),
\]
which proves the unique-lift formula.

For the explicit example, put
\[
P_*(x)=x^2+1+\epsilon i.
\]
Its primal polynomial is
\[
g(x)=x^2+1,
\]
whose zeros are exactly the imaginary units
\[
J\in\mathbb S_{\mathbb H}.
\]
Its dual coefficient polynomial is constant:
\[
h(x)=i.
\]

At such a primal zero,
\[
dg_J(v)=Jv+vJ.
\]
Writing
\[
v=a+bJ+w,
\qquad
a,b\in\mathbb R,
\quad
w\in\mathbb C_J^\perp,
\]
gives
\[
Jv+vJ=2aJ-2b.
\]
Thus
\[
\operatorname{im}dg_J=\mathbb C_J,
\qquad
\ker dg_J=\mathbb C_J^\perp.
\]

The lift equation is
\[
Jv+vJ=-i.
\]
Because the right side is purely imaginary, it belongs to
\[
\mathbb C_J
\]
only when
\[
J=\pm i.
\]
For
\[
J=i,
\]
the equation gives
\[
a=-\frac12,\qquad b=0,
\]
with the two perpendicular coordinates free. Hence
\[
v=-\frac12+cj+dk.
\]
For
\[
J=-i,
\]
the solutions are
\[
v=\frac12+cj+dk.
\]
This proves the displayed zero set.

Finally, the source describes the quadratic cone over a nonreal primal point \(J\) by requiring its dual part to be purely imaginary and perpendicular to \(J\). Every zero above has dual part with real component
\[
\pm\frac12,
\]
so none belongs to
\[
Q_{\mathbb{DH}}.
\]

## Verification

The fresh primary paper was inspected at its construction of the full dual-slice domain, Lemma 2.17 on differential ranks, Theorem 7.2 on the extension formula, Theorem 8.1 on inclusion of dual quaternionic polynomials, Remark 8.2 on quaternionic components, Example 8.3, and the concluding discussion of future zero-set work.

The proof of the general lifting law is a direct logical consequence of the exact Theorem 7.2 formula and uses no numerical approximation.

The explicit example was checked independently by expanding
\[
(J+\epsilon v)^2+1+\epsilon i
=
\epsilon(Jv+vJ+i)
\]
for
\[
J^2=-1.
\]
The real-linear map
\[
v\mapsto Jv+vJ
\]
has rank \(2\), image \(\mathbb C_J\), and kernel \(\mathbb C_J^\perp\). For \(J=i\) and \(J=-i\), solving the resulting \(4\)-real-variable linear equations gives exactly the two stated affine planes.

The 2021 factorization paper was inspected at its right-zero/factor relation and its generic root-extraction lemma. Those results organize roots through polynomial factors and norm-polynomial factors; they do not give the full differential fiber classification above.

## Relationship to prior work

Gentili, Stoppato, and Trinci developed a detailed zero theory for dual quaternionic slice functions on the quadratic cone. The new 2026 paper explicitly distinguishes that older setting from its newly constructed dual slice functions on open subsets of the whole algebra
\[
\mathbb{DH}.
\]
It also states that systematic study of zeros in this new full-space setting is deferred to future work.

Siegele, Pfurner, and Schröcker study right zeros of dual quaternion polynomials through factorization. Their generic extraction theorem assumes an appropriate quadratic norm factor whose primal part does not divide the primal polynomial, and their methods are designed around factorization rather than the differential geometry of all lifts over a fixed primal zero.

The present result uses the new full-space extension formula to obtain a fiberwise classification valid without those generic factorization assumptions. The example
\[
x^2+1+\epsilon i
\]
is deliberately nongeneric from the factorization perspective because its primal part is real. Its two zero planes lie completely outside the quadratic cone, making the distinction from the older slice-zero theory explicit.

Targeted searches for derivative lifting, affine zero fibers, the normalized example, and a dual-quaternionic Hensel-type statement did not locate an implication-equivalent result.

## Limitations

The theorem reduces the full dual zero problem to the primal zero set and a real-linear solvability condition. It does not by itself classify all zeros of the quaternionic polynomial \(g\).

The phrase “lifting” refers only to the square-zero dual extension
\[
\epsilon^2=0.
\]
No higher-order nilpotent or non-Archimedean Hensel theorem is claimed.

The complete 2021 zero-set article could not be retrieved in full through the available lawful full-text routes. Its role is therefore treated conservatively: the accessible material and the 2026 paper identify its domain as the quadratic cone, but no whole-document negative claim is made beyond that domain distinction.

## References

1. G. Binosi and C. Stoppato, *Dual slice functions and dual quaternionic polynomials*, arXiv:2609.35518v1, 2026.
2. G. Gentili, C. Stoppato, and T. Trinci, *Zeros of slice functions and polynomials over dual quaternions*, Transactions of the American Mathematical Society 374 (2021), 5509--5544, DOI: 10.1090/tran/8346.
3. J. Siegele, M. Pfurner, and H.-P. Schröcker, *Factorization of Dual Quaternion Polynomials Without Study’s Condition*, Advances in Applied Clifford Algebras 31 (2021), Article 22, DOI: 10.1007/s00006-021-01123-w.
