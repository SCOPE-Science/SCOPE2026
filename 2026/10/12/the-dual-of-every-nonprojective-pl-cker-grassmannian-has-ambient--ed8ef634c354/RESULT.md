# The dual of every nonprojective Plücker Grassmannian has ambient Euler characteristic
## Finding
Let
\[
2\le k\le n-2,
\]
and let
\[
X=\operatorname{Gr}(k,n)
\subset
\mathbb P\!\left(\bigwedge^k\mathbb C^n\right)
\]
be the Plücker Grassmannian. Let
\[
X^\vee
\subset
\mathbb P\!\left(\left(\bigwedge^k\mathbb C^n\right)^*\right)
\]
be its projective dual.

Then
\[
\boxed{
\chi_{\mathrm{top}}(X^\vee)=\binom nk.
}
\]

Consequently
\[
\boxed{
\chi_{\mathrm{top}}(X^\vee)
=
\chi_{\mathrm{top}}(X)
=
\chi_{\mathrm{top}}\!\left(\mathbb P^{\binom nk-1}\right).
}
\]

Equivalently,
\[
\boxed{
\chi_c\!\left(
\mathbb P^{\binom nk-1}\setminus X^\vee
\right)=0.
}
\]

Thus the projective dual can have complicated Pfaffian or higher Grassmannian-dual singularities while remaining indistinguishable from its ambient projective space by ordinary Euler characteristic.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

The projective dual is the Zariski closure of the hyperplanes tangent to the smooth Grassmannian:
\[
X^\vee
=
\overline{
\left\{
[H]:
T_xX\subset H
\text{ for some }x\in X
\right\}
}.
\]

The range
\[
2\le k\le n-2
\]
is essential for the statement. If
\[
k=1
\quad\text{or}\quad
k=n-1,
\]
then the Plücker Grassmannian is the whole projective space and its projective dual is empty.

No smoothness or normality assumption is imposed on
\[
X^\vee.
\]

## Proof
Fix the standard basis
\[
e_1,\ldots,e_n
\]
of
\[
\mathbb C^n.
\]
For a \(k\)-subset
\[
I=\{i_1<\cdots<i_k\},
\]
write
\[
e_I=e_{i_1}\wedge\cdots\wedge e_{i_k}
\]
and let
\[
p_I
\]
be the dual Plücker coordinate.

Choose the diagonal one-parameter subgroup
\[
\lambda(z)e_i=z^{2^i}e_i.
\]
On
\[
\bigwedge^k\mathbb C^n
\]
the weight of
\[
e_I
\]
is
\[
\sum_{i\in I}2^i.
\]
Distinct subsets have distinct binary sums. Hence the induced action on the dual projective space has exactly the coordinate hyperplanes
\[
[p_I]
\]
as fixed points, one for each \(k\)-subset \(I\).

The dual variety
\[
X^\vee
\]
is invariant under this action because the Grassmannian is invariant.

We now show that every coordinate fixed point lies in
\[
X^\vee.
\]
Fix a \(k\)-subset \(I\). Since
\[
k\ge2
\quad\text{and}\quad
n-k\ge2,
\]
choose distinct
\[
a,b\in I
\]
and distinct
\[
c,d\notin I.
\]
Put
\[
J=(I\setminus\{a,b\})\cup\{c,d\}.
\]
Then
\[
|I\cap J|=k-2.
\]

At the coordinate point
\[
[e_J]\in X,
\]
the affine tangent cone to the Grassmannian is
\[
\bigwedge^{k-1}\langle e_j:j\in J\rangle
\wedge
\mathbb C^n.
\]
Equivalently, it is spanned by the basis vectors
\[
e_K
\]
for which
\[
|K\cap J|\ge k-1.
\]

Because
\[
|I\cap J|=k-2,
\]
the basis vector
\[
e_I
\]
does not occur in this tangent space. Therefore the coordinate hyperplane
\[
H_I=\{p_I=0\}
\]
contains the embedded projective tangent space
\[
T_{[e_J]}X.
\]
Thus
\[
[H_I]\in X^\vee.
\]

Since \(I\) was arbitrary, every ambient fixed point belongs to the dual:
\[
(X^\vee)^{\mathbb C^*}
=
\{[H_I]:|I|=k\}.
\]
This is a finite set of cardinality
\[
\binom nk.
\]

For every complex algebraic variety \(Y\) with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof stratifies the nonfixed locus into locally trivial pieces whose fibers are finite quotients of
\[
\mathbb C^*,
\]
each of compactly supported Euler characteristic zero.

Because
\[
X^\vee
\]
is projective,
\[
\chi_{\mathrm{top}}(X^\vee)
=
\chi_c(X^\vee)
=
\binom nk.
\]

The Grassmannian itself has
\[
\binom nk
\]
Schubert cells, so
\[
\chi_{\mathrm{top}}(X)=\binom nk.
\]
The ambient dual projective space has the same Euler characteristic:
\[
\chi_{\mathrm{top}}
\!\left(
\mathbb P^{\binom nk-1}
\right)
=
\binom nk.
\]
Constructible additivity gives the vanishing Euler characteristic of the complement.

## Verification
The bundled checker enumerates all pairs
\[
(n,k)
\]
with
\[
4\le n\le14,
\qquad
2\le k\le n-2.
\]

For every \(k\)-subset \(I\), it explicitly constructs a \(k\)-subset \(J\) with
\[
|I\cap J|=k-2
\]
and verifies that \(I\) does not occur among the coordinate basis vectors spanning the tangent space at
\[
[e_J].
\]

It independently checks that binary one-parameter-subgroup weights separate every Plücker coordinate and that the number of fixed coordinate hyperplanes is
\[
\binom nk.
\]

These finite computations are regression evidence only. The all-parameter theorem follows from the symbolic tangent-space construction and Euler localization.

## Relationship to prior work
Shimada studies complements of Grassmannian dual varieties and proves Lefschetz--Zariski--van Kampen type results for their fundamental groups.

Holweck studies the singularities and normality of projective duals of Plücker Grassmannians. In particular, the dual of
\[
\operatorname{Gr}(2,n)
\]
is identified with the projectivized variety of degenerate skew-symmetric matrices, while higher Grassmannian duals are studied through their singular loci and secant geometry.

The inspected full texts do not state the ordinary Euler characteristic formula above. Targeted searches for Euler-characteristic, Poincaré-polynomial, Pfaffian, and torus-fixed formulations did not locate an equivalent or stronger result implying it.

The formula is not a consequence of the known degree or normality statements: degree, singularity codimension, and ordinary Euler characteristic are independent global invariants.

## Limitations
Ordinary Euler characteristic is coarse. The formula does not determine the degree, singular strata, intersection cohomology, mixed Hodge structure, or individual Betti numbers of
\[
X^\vee.
\]

The argument is specific to the nonprojective Plücker Grassmannians, where every coordinate hyperplane can be made tangent by changing two indices. The boundary projective-space cases have empty dual.

Because the torus-localization proof is short, an older unindexed or folklore observation remains a residual originality risk.

## References
Ichiro Shimada, *Generalized Zariski--van Kampen theorem and its application to Grassmannian dual varieties*, arXiv:0906.1074, first submitted 5 June 2009.

Frédéric Holweck, *Singularities of duals of Grassmannians*, arXiv:1206.1038, first submitted 5 June 2012.
