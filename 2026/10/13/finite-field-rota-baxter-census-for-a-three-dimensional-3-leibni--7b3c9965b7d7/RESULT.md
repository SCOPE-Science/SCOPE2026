# Finite-field Rota–Baxter census for a three-dimensional \(3\)-Leibniz algebra

## Finding

Let \(K\) be a field, and let \(L_K\) be the \(3\)-dimensional \(3\)-Leibniz algebra with basis
\[
\{e_1,e_2,e_3\}
\]
and nonzero brackets
\[
[e_3,e_2,e_3]=-e_2,
\qquad
[e_3,e_3,e_2]=e_2.
\]

A weight-zero Rota–Baxter operator is a linear map
\[
B:L_K\to L_K
\]
satisfying
\[
[Bx,By,Bz]
=
B\!\left(
[Bx,By,z]+[Bx,y,Bz]+[x,By,Bz]
\right)
\]
for all \(x,y,z\in L_K\).

Write
\[
B=
\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}
\end{pmatrix},
\]
where the \(j\)-th column is the coordinate vector of \(B(e_j)\).

For every finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{RB}(L_{\mathbf F_q})|
=
\begin{cases}
q^6+2q^5-q^4-q^3,
&
\operatorname{char}\mathbf F_q\ne2,\\[2mm]
q^6+3q^5-3q^4,
&
\operatorname{char}\mathbf F_q=2.
\end{cases}}
\]

The characteristic-\(2\) excess over the odd-characteristic polynomial is
\[
\boxed{
q^3(q-1)^2.
}
\]

It is concentrated in one geometric stratum:
\[
a_{31}=a_{32}=0,
\qquad
a_{33}\ne0.
\]
When the characteristic is not \(2\), this stratum forces
\[
a_{12}=a_{21}=a_{22}=0.
\]
In characteristic \(2\), only
\[
a_{12}=a_{21}=0
\]
remain forced, so \(a_{22}\) becomes a new free parameter.

The remaining nonzero-bottom-row strata are characteristic-independent.

## Assumptions and scope

The bracket is exactly the three-dimensional example used in Hu–Hou–Song–Zhou, Example 2.11.

The source works over an algebraically closed field of characteristic \(0\). The present theorem base-changes the defining polynomial identity to arbitrary finite fields and solves it directly; it does not assume that the source's characteristic-zero case split remains valid after reduction.

The operator convention is the same column convention as in the source:
\[
B(e_j)=\sum_i a_{ij}e_i.
\]

No automorphism quotient is taken. The invariant counted here is the full set of linear Rota–Baxter operators on the fixed \(3\)-Leibniz multiplication.

## Proof

For vectors
\[
x=x_1e_1+x_2e_2+x_3e_3,
\qquad
y=y_1e_1+y_2e_2+y_3e_3,
\qquad
z=z_1e_1+z_2e_2+z_3e_3,
\]
the bracket is
\[
[x,y,z]
=
x_3(y_3z_2-y_2z_3)e_2.
\]

It is enough to impose the Rota–Baxter identity on the \(27\) ordered triples of basis vectors. The resulting polynomial system contains the decisive relations
\[
a_{12}a_{31}^2=0,
\qquad
a_{31}^2a_{32}=0,
\qquad
a_{31}(a_{22}^2+a_{23}a_{32})=0,
\]
\[
a_{21}a_{32}^2=0,
\qquad
a_{32}^2(a_{22}+a_{33})=0,
\qquad
a_{32}(a_{22}^2+a_{23}a_{32})=0.
\]

These relations split the solution set according to the bottom row
\[
(a_{31},a_{32},a_{33}).
\]

If
\[
a_{31}=a_{32}=a_{33}=0,
\]
all six entries in the first two rows are free. This contributes
\[
q^6
\]
operators.

Suppose
\[
a_{31}\ne0.
\]
Then
\[
a_{12}=0,
\qquad
a_{32}=0,
\qquad
a_{22}=0.
\]
The remaining nontrivial equation is
\[
a_{21}a_{33}=a_{23}a_{31}.
\]

If
\[
a_{33}=0,
\]
then
\[
a_{23}=0,
\]
and \(a_{11},a_{13},a_{21}\) are free. This contributes
\[
(q-1)q^3.
\]

If
\[
a_{33}\ne0,
\]
then \(a_{21}\) is uniquely determined by
\[
a_{21}=\frac{a_{23}a_{31}}{a_{33}},
\]
while \(a_{11},a_{13},a_{23}\) are free. This contributes
\[
(q-1)^2q^3.
\]

Now suppose
\[
a_{31}=0,
\qquad
a_{32}\ne0.
\]
The equations force
\[
a_{21}=0,
\qquad
a_{22}=-a_{33},
\qquad
a_{23}a_{32}=-a_{33}^2.
\]

If
\[
a_{33}=0,
\]
then
\[
a_{22}=a_{23}=0,
\]
and \(a_{11},a_{12},a_{13}\) are free. This contributes
\[
(q-1)q^3.
\]

If
\[
a_{33}\ne0,
\]
then \(a_{22}\) and \(a_{23}\) are uniquely determined by \(a_{32},a_{33}\), while
\[
a_{11},a_{12},a_{13}
\]
are free. This contributes
\[
(q-1)^2q^3.
\]

It remains to consider
\[
a_{31}=a_{32}=0,
\qquad
a_{33}\ne0.
\]

The basis-triple equations reduce to
\[
a_{12}a_{33}(2a_{22}+a_{33})=0,
\]
\[
a_{21}a_{33}(2a_{22}-a_{33})=0,
\]
and
\[
2a_{22}^2a_{33}=0,
\]
together with consequences of these equations.

If
\[
\operatorname{char}K\ne2,
\]
then \(a_{22}=0\), and hence
\[
a_{12}=a_{21}=0.
\]
The free variables are
\[
a_{11},a_{13},a_{23},
\]
so this contributes
\[
(q-1)q^3.
\]

If
\[
\operatorname{char}K=2,
\]
the square term vanishes identically. The other equations force
\[
a_{12}=a_{21}=0
\]
but impose no condition on \(a_{22}\). Thus
\[
a_{11},a_{13},a_{22},a_{23}
\]
are free, giving
\[
(q-1)q^4.
\]

For odd characteristic the total is therefore
\[
q^6
+
3(q-1)q^3
+
2(q-1)^2q^3
=
q^6+2q^5-q^4-q^3.
\]

For characteristic \(2\), the total is
\[
q^6
+
(q-1)q^4
+
2(q-1)q^3
+
2(q-1)^2q^3
=
q^6+3q^5-3q^4.
\]

Subtracting the two polynomials gives
\[
q^3(q-1)^2.
\]

## Verification

The included program `artifacts/verify.py` implements the ternary bracket directly and tests the Rota–Baxter identity on all \(27\) ordered basis triples.

It exhaustively enumerates every \(3\times3\) matrix over
\[
\mathbf F_2
\]
and
\[
\mathbf F_3.
\]
The exact counts are
\[
112
\]
and
\[
1107,
\]
which agree with the two formulas:
\[
2^6+3\cdot2^5-3\cdot2^4=112,
\]
and
\[
3^6+2\cdot3^5-3^4-3^3=1107.
\]

The checker independently generates the disjoint strata and confirms their counts for
\[
q=2,3,5,7,11.
\]

It also exhibits the characteristic-\(2\) boundary witness
\[
B=
\begin{pmatrix}
0&0&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\]
which satisfies the Rota–Baxter identity over \(\mathbf F_2\) but is excluded by the characteristic-zero stratum condition \(a_{22}=0\).

The program returns `VERIFY_OK`.

The arbitrary-\(q\) formulas are proved by the field-level case split above; finite enumeration is only a replay check.

## Relationship to prior work

Hu, Hou, Song, and Zhou develop relative Rota–Baxter operators on \(3\)-Leibniz algebras, their deformation theory, and associated cohomology. Their Example 2.11 uses exactly the algebra studied here and records the characteristic-zero polynomial equations together with six families of Rota–Baxter operators.

Their paper explicitly works over an algebraically closed field of characteristic \(0\). Its first-listed Mathematics Subject Classification is \(17A42\).

The earlier paper of Li, Li, and Zhang studies constructions of \(3\)-Leibniz algebras and their Rota–Baxter operators in general, but the accessible metadata and abstract do not give this finite-field census.

Targeted searches for this specific \(3\)-Leibniz multiplication, finite-field Rota–Baxter counts, characteristic-\(2\) behavior, and the resulting counting polynomials did not locate the formulas above.

The new point is not merely substituting a finite field into the characteristic-zero list: the characteristic-\(2\) stratum is strictly larger, so a direct polynomial re-analysis is necessary.

## Limitations

The theorem counts all Rota–Baxter operators on one fixed \(3\)-dimensional \(3\)-Leibniz algebra. It does not classify them up to automorphism.

No claim is made for arbitrary \(3\)-Leibniz algebras.

The source's characteristic-zero classification is used only as literature context; the finite-field proof independently reconstructs the defining equations.

A specialized or unindexed finite-field calculation may exist. Failed searches do not prove novelty.

## References

1. M. Hu, S. Hou, L. Song, and Y. Zhou, “3-pre-Leibniz Algebras, Deformations and Cohomologies of Relative Rota-Baxter Operators on 3-Leibniz Algebras,” *Journal of Nonlinear Mathematical Physics* 31 (2024), article 37, DOI `10.1007/s44198-024-00198-w`.
2. F.-S. Li, L.-H. Li, and L.-Y. Zhang, “Construction of 3-Leibniz algebras and their Rota-Baxter operators,” *Journal of Shandong University (Natural Science)* 55 (2020), 48–53, DOI `10.6040/j.issn.1671-9352.0.2019.560`.
