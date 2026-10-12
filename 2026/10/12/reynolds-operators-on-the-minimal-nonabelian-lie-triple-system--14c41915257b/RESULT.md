# Reynolds operators on the minimal nonabelian Lie triple system

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
Let \(L_K\) have basis
\[
\{e_1,e_2\}
\]
and ternary product determined by
\[
[e_1,e_2,e_2]=e_1,
\qquad
[e_2,e_1,e_2]=-e_1.
\]

This is a Lie triple system; for example it is induced by the two-dimensional affine Lie algebra
\[
[e_1,e_2]=e_1
\]
through
\[
[x,y,z]=[[x,y],z].
\]

A Reynolds operator is a linear map \(R:L_K\to L_K\) satisfying
\[
[Rx,Ry,Rz]
=
R\!\left(
[Rx,Ry,z]
+[x,Ry,Rz]
+[Rx,y,Rz]
-[Rx,Ry,Rz]
\right)
\]
for all \(x,y,z\in L_K\).

Write
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]
Then the complete Reynolds locus is
\[
\boxed{
\operatorname{Rey}(L_K)
=
\mathcal A\cup\mathcal B\cup\mathcal C\cup\mathcal N,
}
\]
where
\[
\mathcal A
=
\left\{
\begin{pmatrix}
0&b\\
0&d
\end{pmatrix}
:b,d\in K
\right\},
\]
\[
\mathcal B
=
\left\{
\begin{pmatrix}
a&b\\
0&0
\end{pmatrix}
:a,b\in K
\right\},
\]
\[
\mathcal C
=
\left\{
\begin{pmatrix}
a&b\\
0&2
\end{pmatrix}
:a,b\in K
\right\},
\]
and
\[
\mathcal N
=
\{R\in M_2(K):R^2=0\}.
\]

Equivalently, when
\[
c=0,
\]
the Reynolds identity reduces to
\[
\boxed{
a^2d(d-2)=0.
}
\]
When
\[
c\ne0,
\]
it is equivalent to
\[
\boxed{
\operatorname{tr}R=0,
\qquad
\det R=0,
}
\]
and hence to
\[
R^2=0.
\]

Over every odd finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{Rey}(L_{\mathbf F_q})|
=
4q^2-3q.
}
\]
The exact rank distribution in ranks \(0,1,2\) is
\[
\boxed{
\left(
1,\,
(q-1)(3q+1),\,
q(q-1)
\right).
}
\]

The invertible Reynolds operators are exactly
\[
\begin{pmatrix}
a&b\\
0&2
\end{pmatrix},
\qquad
a\ne0,
\]
so there are
\[
q(q-1)
\]
of them.

Over every extension field,
\[
|\operatorname{Rey}(L_{\mathbf F_q})(\mathbf F_{q^m})|
=
4q^{2m}-3q^m.
\]
Therefore the Hasse--Weil zeta function of the reduced solution set is
\[
\boxed{
Z(T)
=
\frac{(1-qT)^3}{(1-q^2T)^4}.
}
\]

## Assumptions and scope

Teng, Jin, and Long introduce Reynolds operators on Lie--Yamaguti algebras. When the binary product vanishes, their Reynolds identity specializes to the ternary identity used here. Their preprint first appeared on 10 February 2023.

A later paper of Mu and Guo develops Reynolds Lie triple systems directly. In its weight convention, the present Reynolds identity is weight
\[
-1.
\]
Their Example 4 uses exactly the two-dimensional Lie triple system above and records the affine plane
\[
\mathcal A
\]
as a family of Reynolds operators for arbitrary weight. The theorem here completes the weight-\(-1\) classification.

The 2023 source assumes an algebraically closed field with characteristic different from \(2\) and \(3\), while the later Reynolds Lie triple paper works in characteristic \(0\). The direct calculation here is valid over every field of characteristic different from \(2\).

No assertion is made here about characteristic \(2\), where the branch labeled by \(d=2\) merges with the branch \(d=0\).

## Proof

For
\[
x=x_1e_1+x_2e_2,\qquad
y=y_1e_1+y_2e_2,\qquad
z=z_1e_1+z_2e_2,
\]
the ternary bracket is
\[
[x,y,z]
=
(x_1y_2-x_2y_1)z_2e_1.
\]

Substituting
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\]
into the Reynolds identity and evaluating on all ordered basis triples gives four independent polynomial equations:
\[
c(a^2d-a^2-abc-bc)=0,
\]
\[
c^2(ad-a-bc-d)=0,
\]
\[
a^2d^2-2a^2d-abcd+abc-bcd=0,
\]
and
\[
c(ad^2-2ad-bcd+bc-d^2)=0.
\]

First suppose
\[
c=0.
\]
The system collapses to
\[
a^2d(d-2)=0.
\]
Since \(K\) is a field, this is equivalent to
\[
a=0,
\qquad
d=0,
\qquad\text{or}\qquad
d=2.
\]
These are exactly the three affine planes
\[
\mathcal A,\quad
\mathcal B,\quad
\mathcal C.
\]

Now suppose
\[
c\ne0.
\]
Put
\[
\Delta=ad-bc.
\]
The second displayed equation gives
\[
\Delta=a+d.
\]
Using this relation, the first equation becomes
\[
c\Delta=0.
\]
Hence
\[
\Delta=0
\]
and therefore
\[
a+d=0.
\]
Thus
\[
\det R=0,
\qquad
\operatorname{tr}R=0.
\]
By Cayley--Hamilton,
\[
R^2=0.
\]

Conversely, every square-zero matrix has trace and determinant zero and satisfies the four displayed equations, so the square-zero cone is exactly the \(c\ne0\) branch together with its boundary inside \(c=0\). This proves the classification.

For finite-field counting, each of
\[
\mathcal A,\quad\mathcal B,\quad\mathcal C
\]
has \(q^2\) points. The square-zero cone in \(M_2(\mathbf F_q)\) also has \(q^2\) points: zero plus the \(q^2-1\) nonzero rank-one nilpotents.

Let
\[
\mathcal L
=
\left\{
\begin{pmatrix}
0&b\\
0&0
\end{pmatrix}
:b\in\mathbf F_q
\right\}.
\]
Then
\[
\mathcal A\cap\mathcal B
=
\mathcal A\cap\mathcal N
=
\mathcal B\cap\mathcal N
=
\mathcal A\cap\mathcal B\cap\mathcal N
=
\mathcal L,
\]
while
\[
|\mathcal A\cap\mathcal C|=q,
\]
and, because the characteristic is odd,
\[
\mathcal B\cap\mathcal C
=
\mathcal C\cap\mathcal N
=
\varnothing.
\]
Inclusion--exclusion therefore yields
\[
4q^2-3q.
\]

Only the branch
\[
\mathcal C
\]
contains invertible matrices, and
\[
\det
\begin{pmatrix}
a&b\\
0&2
\end{pmatrix}
=
2a.
\]
Thus the rank-two count is
\[
q(q-1).
\]
Subtracting zero and the invertible stratum from the total gives
\[
4q^2-3q-1-q(q-1)
=
(q-1)(3q+1)
\]
rank-one operators.

Finally, replacing \(q\) by \(q^m\) gives the extension-field count and the displayed zeta function.

## Verification

The included `artifacts/verify.py` reconstructs the Lie triple product and the Reynolds identity.

It symbolically evaluates every ordered basis triple and verifies that the defect ideal is generated by the four equations used in the proof.

It then exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,\quad
\mathbf F_{11}.
\]

The resulting totals are
\[
27,\quad
85,\quad
175,\quad
451,
\]
matching
\[
4q^2-3q.
\]

The corresponding rank profiles are
\[
(1,20,6),
\quad
(1,64,20),
\quad
(1,132,42),
\quad
(1,340,110).
\]

For every tested matrix, the direct Reynolds identity agrees exactly with membership in
\[
\mathcal A\cup\mathcal B\cup\mathcal C\cup\mathcal N.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field theorem follows from the polynomial case split above.

## Relationship to prior work

Teng, Jin, and Long establish the Reynolds-operator framework on Lie--Yamaguti algebras and explain its reduction to ternary settings. Their inspected full text does not give a complete two-dimensional Reynolds classification.

Mu and Guo later formulate Reynolds Lie triple systems directly. Their Example 4 is especially close: for the same two-dimensional Lie triple system it records
\[
\begin{pmatrix}
0&a\\
0&b
\end{pmatrix}
\]
as a Reynolds family for arbitrary weight. At weight \(-1\), this is exactly the plane
\[
\mathcal A
\]
above. Their inspected article develops representations, cohomology, deformations, extensions, and higher structures; it does not state that this plane is exhaustive, nor does it give the additional planes
\[
\mathcal B,\quad\mathcal C,
\]
the square-zero cone
\[
\mathcal N,
\]
or the finite-field rank distribution.

A weight-zero Rota--Baxter classification for the same two-dimensional Lie triple is a different operator problem. Weight zero and weight \(-1\) have different defining equations and different solution varieties; in particular, the present Reynolds locus has an invertible branch.

Targeted searches using the exact ternary product, Reynolds terminology, the four-component decomposition, and the point-count polynomial
\[
4q^2-3q
\]
did not locate a covering Reynolds-Lie-triple result.

## Limitations

The theorem treats one two-dimensional nonabelian Lie triple system and the Reynolds identity corresponding to weight \(-1\).

Characteristic \(2\) is excluded.

The result does not classify Reynolds operators for every weight parameter simultaneously.

A differently indexed low-dimensional calculation may exist. Failed searches do not prove absolute novelty.

## References

1. W. Teng, J. Jin, and F. Long, “Generalized Reynolds Operators on Lie-Yamaguti Algebras,” preprint DOI `10.13140/RG.2.2.20194.81605`, first public 10 February 2023; *Axioms* 12 (2023), 934, DOI `10.3390/axioms12100934`.
2. Y. Mu and S. Guo, “Cohomology of Reynolds Lie Triple Systems and Applications,” *Axioms* 15 (2026), 616, DOI `10.3390/axioms15080616`.
