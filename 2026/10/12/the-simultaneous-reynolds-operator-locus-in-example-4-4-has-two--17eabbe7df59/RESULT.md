# The simultaneous Reynolds-operator locus in Example 4.4 has two completed components

## Finding

Let \(\mathfrak g\) be the complex Lie algebra with basis
\[
\{e_1,e_2,e_3\}
\]
and sole nonzero basic bracket
\[
[e_1,e_2]=e_2.
\]
Let \(f(e_1)=f(e_3)=1\) and \(f(e_2)=0\). The induced \(3\)-Lie algebra \(\mathfrak g_f\) has
\[
\{e_1,e_2,e_3\}=e_2.
\]

Write a linear map \(R:\mathfrak g\to\mathfrak g\) as
\[
R=
\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{pmatrix},
\]
with columns equal to the coordinates of \(R(e_1),R(e_2),R(e_3)\).

Then \(R\) is a Reynolds operator for both the Lie bracket and the induced \(3\)-Lie bracket if and only if
\[
\boxed{R\in X_1\cup X_2,}
\]
where
\[
X_1=
\left\{
a_{12}=a_{22}=a_{32}=0,\quad
a_{11}a_{23}-a_{21}a_{13}=0
\right\}
\]
and
\[
X_2=
\left\{
a_{11}+a_{22}=0,\quad
a_{13}=a_{23}=0,\quad
a_{12}a_{21}+a_{22}^{2}=0
\right\}.
\]

Both \(X_1\) and \(X_2\) are irreducible affine varieties of dimension \(5\). Their intersection is
\[
X_1\cap X_2
=
\left\{
a_{11}=a_{12}=a_{13}=a_{22}=a_{23}=a_{32}=0
\right\}
\cong\mathbb A^3,
\]
with free coordinates \(a_{21},a_{31},a_{33}\).

Example 4.4 of Hou--Sheng ends with two rational matrix families. The first is the chart of \(X_1\) obtained by solving
\[
a_{11}a_{23}-a_{21}a_{13}=0
\]
for \(a_{13}\), which requires \(a_{21}\ne0\). The second is the chart of \(X_2\) obtained by solving
\[
a_{12}a_{21}+a_{22}^{2}=0
\]
for \(a_{21}\), which requires \(a_{12}\ne0\).

Consequently those two displayed families omit nonempty boundary loci. Two particularly simple omitted operators are
\[
R_1=E_{13}
=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix}
\in X_1
\]
and
\[
R_2=E_{21}+E_{32}
=
\begin{pmatrix}
0&0&0\\
1&0&0\\
0&1&0
\end{pmatrix}
\in X_2.
\]

## Assumptions and scope

The ground field is \(\mathbb C\). This matches the standard characteristic-zero setting and avoids any characteristic-dependent interpretation of the displayed signs.

The claim concerns exactly the Lie algebra and trace-induced \(3\)-Lie algebra in Example 4.4. It does not classify Reynolds operators on arbitrary \(3\)-dimensional Lie or \(3\)-Lie algebras.

A simultaneous Reynolds operator means that the same linear map \(R\) satisfies the Reynolds identity for both operations.

The conclusion corrects the set-theoretic completion of the example's final parameterization. It does not challenge the general construction theorem preceding the example.

## Proof

For the Lie algebra, the Reynolds identity is
\[
[R x,R y]
=
R\bigl([R x,y]+[x,R y]-[R x,R y]\bigr).
\]
For the \(3\)-Lie algebra it is
\[
\{R x,R y,R z\}
=
R\bigl(
\{R x,R y,z\}
+\{R x,y,R z\}
+\{x,R y,R z\}
-\{R x,R y,R z\}
\bigr).
\]

Substituting the nine matrix entries into these identities on basis elements gives a polynomial ideal. Exact elimination reduces that ideal to the following Gröbner basis:
\[
a_{12}(a_{11}+a_{22}),
\]
\[
a_{22}^{2}(a_{11}+a_{22}),
\]
\[
a_{11}a_{23}-a_{13}a_{21}-a_{22}a_{23},
\]
\[
a_{32}(a_{11}+a_{22}),
\]
\[
a_{12}a_{13},
\qquad
a_{12}a_{21}+a_{22}^{2},
\qquad
a_{12}a_{23},
\]
\[
a_{13}a_{22}^{2},
\qquad
a_{13}a_{32},
\qquad
a_{22}^{2}a_{23},
\qquad
a_{23}a_{32}.
\]

We now solve this system set-theoretically.

First suppose
\[
a_{12}=a_{22}=a_{32}=0.
\]
Every displayed equation vanishes except
\[
a_{11}a_{23}-a_{21}a_{13}=0.
\]
This is exactly \(X_1\).

Now suppose the second column is nonzero. If
\[
a_{12}\ne0,
\]
then the Gröbner equations give
\[
a_{11}=-a_{22},
\qquad
a_{13}=a_{23}=0,
\qquad
a_{12}a_{21}+a_{22}^{2}=0.
\]
Thus \(R\in X_2\).

If
\[
a_{12}=0,\qquad a_{32}\ne0,
\]
then
\[
a_{11}=-a_{22},
\qquad
a_{13}=a_{23}=0.
\]
The equation
\[
a_{12}a_{21}+a_{22}^{2}=0
\]
forces \(a_{22}=0\), hence also \(a_{11}=0\). Again \(R\in X_2\).

The only remaining possibility would be
\[
a_{12}=a_{32}=0,\qquad a_{22}\ne0.
\]
But then
\[
a_{12}a_{21}+a_{22}^{2}=0
\]
would force \(a_{22}=0\), a contradiction. Therefore no other solutions occur.

Conversely, direct substitution shows that every point of \(X_1\) and every point of \(X_2\) satisfies both Reynolds identities.

The defining quadratic of \(X_1\),
\[
a_{11}a_{23}-a_{21}a_{13},
\]
is the irreducible \(2\times2\) determinant polynomial, while the defining quadratic of \(X_2\),
\[
a_{12}a_{21}+a_{22}^{2},
\]
is an irreducible rank-\(3\) quadratic over \(\mathbb C\). Each component has three independent linear equations plus one irreducible quadratic in \(\mathbb A^9\), so both have dimension \(5\).

Adding the two component ideals gives
\[
a_{11}=a_{12}=a_{13}=a_{22}=a_{23}=a_{32}=0,
\]
so the intersection is \(\mathbb A^3\).

## Verification

The included program `artifacts/verify.py` reconstructs both Reynolds identities directly from
\[
[e_1,e_2]=e_2
\]
and
\[
\{e_1,e_2,e_3\}=e_2.
\]

It computes the exact polynomial defects over \(\mathbb Q\), forms their Gröbner basis, and checks that the basis is exactly the eleven-polynomial system used in the proof.

It independently forms the ideals of \(X_1\) and \(X_2\) and verifies that every direct Reynolds defect reduces to zero on both components.

It also computes the ideal-theoretic intersection of the two reduced component ideals by elimination and verifies the stated component intersection.

Finally it substitutes the two boundary witnesses \(E_{13}\) and \(E_{21}+E_{32}\) into every direct defect and checks that every defect vanishes.

Running the script prints `VERIFY_OK`.

## Relationship to prior work

Hou and Sheng introduce Reynolds operators on \(n\)-Lie algebras and prove a construction that transfers a Reynolds operator on an \(n\)-Lie algebra to a trace-induced \((n+1)\)-Lie algebra under an additional condition. Their Example 4.4 specializes that construction to the Lie algebra
\[
[e_1,e_2]=e_2
\]
and the induced \(3\)-Lie algebra
\[
\{e_1,e_2,e_3\}=e_2.
\]

The example first gives polynomial conditions and then splits them into two cases. In the first case it solves a determinantal equation by dividing by \(a_{21}\); in the second it solves a quadratic equation by dividing by \(a_{12}\). No nonzero assumptions on those denominators are stated before the final matrices are displayed.

The exact completion above shows that the printed families are principal charts of two irreducible components rather than the complete simultaneous-operator locus. The omitted sets are not isolated accidents: each is a positive-dimensional boundary of its component.

The later journal publication has the same article and subject classification. Targeted searches for the source identifier, Example 4.4, the exact multiplication tables, the two determinant equations, correction or erratum terminology, and simultaneous Reynolds-operator classifications did not locate a published completion of these boundary strata.

Broader work on generalized Reynolds operators and later unified deformation-map approaches treats structural operator theory on \(3\)-Lie algebras, but the inspected statements do not give this exact completed variety for Example 4.4.

## Limitations

The result is set-theoretic over \(\mathbb C\). The polynomial scheme defined by the raw Reynolds equations can retain nonreduced structure along the components; no scheme-theoretic primary decomposition is claimed here.

No claim is made about the full moduli quotient by automorphisms of the Lie or \(3\)-Lie algebra.

The result concerns one explicit example, not a classification of all Reynolds operators in dimension three.

A correction in unindexed literature or private author notes may exist. Failed searches do not prove bibliographic uniqueness.

## References

1. S. Hou and Y. Sheng, “Reynolds \(n\)-Lie algebras and NS-\(n\)-Lie algebras,” arXiv:2108.04407v1, first public 10 August 2021; later published as “Cohomologies of Reynolds operators on \(n\)-Lie algebras,” *Communications in Algebra* 51 (2023), 779–798, DOI:10.1080/00927872.2022.2113403. First listed MSC: 17B56.
2. S. Hou and Y. Sheng, “Generalized Reynolds operators on \(3\)-Lie algebras and NS-\(3\)-Lie algebras,” *International Journal of Geometric Methods in Modern Physics* 19 (2022), 2150223, DOI:10.1142/S0219887821502236.
