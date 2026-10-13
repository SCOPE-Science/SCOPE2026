# The affine two-dimensional Lie universal algebra needs a missing diagonal factor

## Finding

Let
\[
\mathfrak a=\operatorname{aff}(2,k)
\]
have basis \(\{e_1,e_2\}\) and bracket
\[
[e_1,e_2]=e_1.
\]

Example 2.9 of Agore--Militaru prints
\[
X_{11}-X_{12}X_{22}+X_{12}X_{21}
\]
as the first nonzero universal polynomial. The correct specialization of the paper's own general formula is
\[
\boxed{X_{11}-X_{11}X_{22}+X_{12}X_{21}.}
\]

Together with
\[
X_{21}=0,
\]
this gives
\[
\boxed{
\mathcal A(\mathfrak a)
\cong
k[X_{11},X_{12},X_{21},X_{22}]
/
(X_{21},X_{11}-X_{11}X_{22}+X_{12}X_{21})
\cong
k[a,b,d]/(a(1-d)).
}
\]

The printed algebra
\[
k[X,Y,Z]/(X-YZ)\cong k[Y,Z]
\]
is therefore not the universal algebra: it is an integral domain, while the corrected algebra is the reducible union of the two planes
\[
a=0
\quad\text{and}\quad
d=1.
\]

Over
\[
k=\mathbf F_q,
\]
the complete Lie endomorphism monoid is
\[
\boxed{
\operatorname{End}_{\mathrm{Lie}}(\mathfrak a)
=
\left\{
\begin{pmatrix}a&b\\0&d\end{pmatrix}:a(1-d)=0
\right\}.
}
\]
It has
\[
\boxed{2q^2-q}
\]
elements, with rank multiplicities
\[
\boxed{1,\quad q^2-1,\quad q(q-1)}
\]
in ranks \(0,1,2\), respectively.

It has exactly
\[
\boxed{q+2}
\]
idempotents and exactly
\[
\boxed{q}
\]
nilpotent endomorphisms, all square-zero. Its center is
\[
\boxed{\{0,I\}}.
\]

The centralizer-size distribution is
\[
\boxed{
\begin{array}{c|c}
\text{centralizer size}&\text{number of elements}\\
\hline
2q^2-q&2\\
2q&2(q-1)\\
2q-1&q(2q-3)
\end{array}}
\]
and the commuting probability of two uniformly chosen endomorphisms is
\[
\boxed{\frac{4q^2-3}{q(2q-1)^2}}.
\]

Finally, the point count itself detects the error: the corrected universal algebra has
\[
2q^2-q
\]
\(\mathbf F_q\)-valued characters, exactly matching the Lie endomorphisms, whereas the printed polynomial ring has only
\[
q^2
\]
such characters.

## Assumptions and scope

The correction is local to Example 2.9. It does not challenge the paper's general universal-algebra construction or its universal-property theorems.

The algebraic correction holds over an arbitrary field \(k\). The counting statements require \(k=\mathbf F_q\).

Matrices are written so that
\[
f(e_1)=a e_1,\qquad f(e_2)=b e_1+d e_2.
\]

The nilpotent count includes the zero endomorphism.

## Proof

The source defines
\[
P_{(a,i,j)}
=
\sum_u\tau^u_{i,j}X_{au}
-
\sum_{s,t}\tau^a_{s,t}X_{si}X_{tj},
\]
where
\[
[e_i,e_j]=\sum_u\tau^u_{i,j}e_u.
\]
For the affine algebra,
\[
\tau^1_{1,2}=1,\qquad \tau^1_{2,1}=-1.
\]
Hence
\[
P_{(1,1,2)}
=
X_{11}-X_{11}X_{22}+X_{21}X_{12},
\]
and
\[
P_{(2,1,2)}=X_{21}.
\]
This proves the corrected coordinate algebra.

There is an independent direct check. Write
\[
f(e_1)=a e_1+c e_2,\qquad
f(e_2)=b e_1+d e_2.
\]
Bracket preservation gives
\[
a e_1+c e_2
=
f([e_1,e_2])
=
[f(e_1),f(e_2)]
=
(ad-cb)e_1.
\]
Thus
\[
c=0,\qquad a=ad,
\]
equivalently
\[
a(1-d)=0.
\]

Over \(\mathbf F_q\), the endomorphism set is the union of the plane \(a=0\) and the plane \(d=1\), intersecting in a line. Inclusion--exclusion yields
\[
q^2+q^2-q=2q^2-q.
\]

Rank two occurs exactly when \(a\ne0\), which forces \(d=1\). This gives \(q(q-1)\) rank-two maps. The zero map is the sole rank-zero map, leaving \(q^2-1\) maps of rank one.

For idempotence,
\[
\begin{pmatrix}a&b\\0&d\end{pmatrix}^2
=
\begin{pmatrix}a^2&b(a+d)\\0&d^2\end{pmatrix}.
\]
Together with \(a(1-d)=0\), the solutions are the zero map, the \(q\) maps with \((a,d)=(0,1)\), and the identity. Hence there are \(q+2\) idempotents.

A triangular map is nilpotent exactly when \(a=d=0\), so \(b\) is arbitrary and there are \(q\) nilpotents.

For
\[
x=(a,b,d),\qquad y=(a',b',d'),
\]
commutation is equivalent to
\[
b'(a-d)+b(d'-a')=0.
\tag{1}
\]
The only elements satisfying equation (1) for every \(y\) are \(0\) and \(I\).

The monoid is the union of
\[
A=\{a'=0\}
\quad\text{and}\quad
B=\{d'=1\},
\]
with \(A\cap B=\{a'=0,d'=1\}\). Counting solutions of equation (1) on these two planes and their intersection gives:
- centralizer size \(2q^2-q\) for the two central elements;
- centralizer size \(2q\) for the \(2(q-1)\) elements with \(a=d\) and \(b\ne0\);
- centralizer size \(2q-1\) for the remaining \(q(2q-3)\) elements.

Thus the number of commuting ordered pairs is
\[
2(2q^2-q)+2(q-1)(2q)+q(2q-3)(2q-1)
=
4q^3-3q,
\]
which gives the displayed commuting probability.

## Verification

The included checker enumerates the endomorphism monoid directly over
\[
\mathbf F_q,\qquad q\in\{2,3,5,7,11\}.
\]
It verifies the defining relation, total count, rank distribution, idempotent and nilpotent counts, center, centralizer strata, and commuting-pair formula.

It also verifies that the printed polynomial algebra would have only \(q^2\) field-valued characters, whereas the true endomorphism monoid has \(2q^2-q\).

The checker returns `VERIFY_OK`.

## Relationship to prior work

Agore and Militaru introduce the universal algebra \(\mathcal A(\mathfrak h)\), prove that its characters parameterize Leibniz/Lie endomorphisms, and give a structure-constant formula for its defining polynomials.

Their Example 2.9 specializes the construction to \(\operatorname{aff}(2,k)\). The example prints
\[
X_{11}-X_{12}X_{22}+X_{12}X_{21}
\]
and concludes
\[
\mathcal A(\operatorname{aff}(2,k))
\cong
k[X,Y,Z]/(X-YZ).
\]

The source's own general formula instead gives
\[
X_{11}-X_{11}X_{22}+X_{12}X_{21}.
\]
Direct bracket preservation gives the same corrected relation independently.

Focused searches for the exact example, the printed polynomial, the corrected relation, affine-Lie endomorphism monoids, and errata did not locate a published correction. The closest database results concern other invariants of the two-dimensional affine Lie algebra or corrections in unrelated algebra families.

## Limitations

The correction is local to Example 2.9. No broader theorem of the source is claimed false.

The finite-field monoid census is an additional consequence of the corrected coordinate algebra and is not needed to establish the typographical error.

An unindexed erratum or author correction may exist.

Failed searches do not prove novelty.

## References

1. A. L. Agore and G. Militaru, “A new invariant for finite dimensional Leibniz/Lie algebras,” arXiv:2006.00711v1, first public version 1 June 2020; *Journal of Algebra* 562 (2020), 390–409, DOI 10.1016/j.jalgebra.2020.07.005. The preprint lists MSC 2010: 17A32, 17A36, 17A60, 17B05, 17B40, 17B70.
