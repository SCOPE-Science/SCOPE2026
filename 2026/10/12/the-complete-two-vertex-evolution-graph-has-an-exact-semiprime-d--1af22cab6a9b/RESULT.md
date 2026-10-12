# The complete two-vertex evolution graph has an exact semiprime defect locus

## Finding

Let \(K\) be a field and let \(A=A(a,b,c,d)\) be the two-dimensional evolution algebra with natural basis
\[
\{e_1,e_2\},
\]
multiplication
\[
e_1e_2=0,
\]
and
\[
e_1^2=a e_1+c e_2,\qquad
e_2^2=b e_1+d e_2.
\]
Assume
\[
abcd\ne0.
\]
Thus every possible arrow, including both loops, occurs in the associated two-vertex directed graph.

Then
\[
\boxed{
A\text{ is semiprime}
\iff
A\text{ is prime}.
}
\]
More precisely,
\[
\boxed{
A\text{ is semiprime}
\iff
\det
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}\ne0
\quad\text{or}\quad
a^3+b c^2\ne0.
}
\]
In the second condition the determinant is understood to vanish. Equivalently, the complete-graph fiber has exact nonsemiprime locus
\[
\boxed{
ad-bc=0,\qquad
a^3+b c^2=0.
}
\]

Thus the graph-theoretic failure exhibited in the motivating literature is not sporadic: inside the smallest full-support graph fiber, semiprimeness and primeness fail on an explicit codimension-two algebraic locus.

If
\[
K=\mathbf F_q,
\]
then among the
\[
(q-1)^4
\]
full-support structure matrices:
\[
\boxed{(q-1)^2}
\]
are nonsemiprime;
\[
\boxed{(q-1)^3(q-2)}
\]
are perfect;
\[
\boxed{(q-1)^2(q-2)}
\]
are semiprime but nonperfect; and
\[
\boxed{q(q-2)(q-1)^2}
\]
are semiprime, equivalently prime, in total.

Among the nonperfect matrices in this graph fiber, the proportion that remain semiprime is
\[
\frac{q-2}{q-1}.
\]

## Assumptions and scope

The theorem concerns structure matrices with all four entries nonzero relative to a fixed natural basis. This is exactly the fiber of the complete two-vertex associated graph with both loops.

The finite-field formulas count structure matrices, not isomorphism classes.

No assumption on the characteristic is required. The case \(q=2\) is included: the unique full-support structure matrix is nonsemiprime.

## Proof

Write
\[
M=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]

If
\[
\det M\ne0,
\]
then \(A^2=A\), so \(A\) is perfect. The standard implication
\[
\text{perfect}\Longrightarrow\text{semiprime}
\]
therefore gives semiprimeness.

Now suppose
\[
\det M=0.
\]
Since every entry is nonzero, \(M\) has rank one and
\[
e_2^2=\lambda e_1^2
\]
for the nonzero scalar
\[
\lambda=\frac ba=\frac dc.
\]
Hence
\[
A^2=K v,\qquad
v=e_1^2=a e_1+c e_2.
\]

Every nonzero ideal \(I\) contains \(A^2\). Indeed, choose
\[
0\ne x=u e_1+w e_2\in I.
\]
If \(u\ne0\), then
\[
xe_1=u e_1^2\in I,
\]
so \(e_1^2\in I\). If \(u=0\), then \(w\ne0\) and
\[
xe_2=w e_2^2
\]
is a nonzero scalar multiple of \(e_1^2\), again giving
\[
A^2\subseteq I.
\]

Therefore \(A\) is semiprime exactly when
\[
(A^2)^2\ne0.
\]
Now
\[
v^2
=
a^2 e_1^2+c^2 e_2^2
=
(a^2+\lambda c^2)v.
\]
Using
\[
\lambda=\frac ba,
\]
we obtain
\[
v^2=0
\iff
a^2+\frac{bc^2}{a}=0
\iff
a^3+b c^2=0.
\]
This proves the semiprime criterion.

The complete two-vertex graph is downward directed. The known primeness theorem for semiprime evolution algebras therefore gives
\[
\text{semiprime}\Longrightarrow\text{prime}.
\]
Conversely, every prime algebra is semiprime. Hence prime and semiprime coincide throughout this graph fiber.

For the finite-field counts, there are
\[
(q-1)^4
\]
full-support matrices.

The determinant-zero matrices are counted by choosing arbitrary nonzero
\[
a,b,c
\]
and then forcing
\[
d=\frac{bc}{a}.
\]
Thus there are
\[
(q-1)^3
\]
nonperfect matrices and
\[
(q-1)^4-(q-1)^3=(q-1)^3(q-2)
\]
perfect ones.

On the determinant-zero locus, nonsemiprimeness is
\[
a^3+b c^2=0.
\]
For every nonzero pair \(a,c\), this determines uniquely
\[
b=-\frac{a^3}{c^2},
\qquad
d=-\frac{a^2}{c},
\]
both nonzero. Hence the defect locus has exactly
\[
(q-1)^2
\]
points.

Subtracting gives
\[
(q-1)^3-(q-1)^2=(q-1)^2(q-2)
\]
semiprime but nonperfect matrices, and therefore
\[
(q-1)^4-(q-1)^2
=
q(q-2)(q-1)^2
\]
semiprime matrices in total.

## Verification

The included checker exhaustively treats
\[
q\in\{2,3,5,7\}.
\]

For every full-support structure matrix it explicitly enumerates every one-dimensional subspace of \(\mathbf F_q^2\), determines which are ideals, and checks semiprimeness directly from the definition.

It also checks primeness directly by testing all pairs of nonzero ideals.

The resulting classifications agree exactly with
\[
ad-bc=0,\qquad a^3+b c^2=0
\]
for the nonsemiprime locus, and with the four closed counting formulas above.

For
\[
q=5,
\]
there are
\[
256
\]
full-support matrices:
\[
192
\]
are perfect,
\[
48
\]
are semiprime but nonperfect, and
\[
16
\]
are nonsemiprime.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.

## Relationship to prior work

Cabrera Casado, Cardoso Gonçalves, Gonçalves, Martín Barquero, Martín González, and Ruiz Campos prove that semiprimeness and perfection cannot be characterized by the associated graph. Their Proposition 3.4 uses two explicit two-dimensional algebras with the same complete graph, one semiprime and one nonsemiprime.

The same source proves that perfect evolution algebras are semiprime and that, for a semiprime evolution algebra, downward directedness of the associated graph is equivalent to primeness. Those results supply the perfect and prime implications used above.

The present result resolves the entire full-support two-vertex graph fiber: it identifies the exact rank-one defect equation, shows that primeness and semiprimeness coincide there, and gives the complete finite-field stratification.

A separate classification paper treats two-dimensional perfect evolution algebras over domains; its searchable text does not address semiprimeness or primeness, and by construction it excludes the rank-one locus where the new defect equation occurs.

Targeted semantic and literature searches for two-dimensional complete-graph evolution algebras, semiprime criteria, rank-one structure matrices, and the polynomial \(a^3+b c^2\) did not locate the displayed criterion or finite-field counts.

## Limitations

The theorem classifies a fixed graph fiber relative to a chosen natural basis; it does not quotient the finite-field counts by algebra isomorphism.

The assumption that all four structure constants are nonzero is essential to the short ideal argument. Other two-vertex graph supports have different ideal structures.

An equivalent rank-one criterion may occur in broader low-dimensional classification literature under different coordinates.

Failed searches do not prove novelty.

## References

1. Y. Cabrera Casado, M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González, and I. Ruiz Campos, “Centroid and algebraic properties of evolution algebras through graphs,” arXiv:2404.08752v1, first public version 12 April 2024. MSC 2020: 17A60, 17D92, 05C25.
2. Y. Cabrera Casado, D. Martín Barquero, and C. Martín González, “Two-dimensional perfect evolution algebras over domains,” arXiv:2204.08410v1, first public version 18 April 2022; *Journal of Algebraic Combinatorics* 58 (2023), 569–587.
