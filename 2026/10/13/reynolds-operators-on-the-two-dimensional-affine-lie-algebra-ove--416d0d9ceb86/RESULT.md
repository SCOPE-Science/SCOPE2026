# Reynolds operators on the two-dimensional affine Lie algebra over finite fields

## Finding

Let
\[
L_q=\mathbf F_q e\oplus\mathbf F_q f
\]
be the unique nonabelian two-dimensional Lie algebra, with bracket
\[
[e,f]=f.
\]

A linear map
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
where the columns are \(R(e)\) and \(R(f)\), is a Reynolds operator when
\[
[Rx,Ry]
=
R\!\left([Rx,y]+[x,Ry]-[Rx,Ry]\right)
\]
for all \(x,y\in L_q\).

The complete defining system is
\[
\boxed{
b(ad-a-bc-d)=0,
}
\]
\[
\boxed{
d^2(a-1)-bc(d+1)=0.
}
\]

Equivalently, the set of Reynolds operators is the following disjoint union:
\[
\boxed{
b=d=0,
}
\]
\[
\boxed{
b=0,\qquad d\ne0,\qquad a=1,
}
\]
and
\[
\boxed{
b\ne0,\qquad d=-a,\qquad bc=-a^2.
}
\]

Therefore, for every prime power \(q\),
\[
\boxed{
|\operatorname{Reyn}(L_q)|=3q^2-2q.
}
\]

The exact rank distribution is
\[
\boxed{
\#\{R:\operatorname{rank}R=0\}=1,
}
\]
\[
\boxed{
\#\{R:\operatorname{rank}R=1\}=2q^2-q-1,
}
\]
and
\[
\boxed{
\#\{R:\operatorname{rank}R=2\}=q(q-1).
}
\]

In particular, the invertible Reynolds operators are exactly
\[
\boxed{
R=
\begin{pmatrix}
1&0\\
c&d
\end{pmatrix},
\qquad d\in\mathbf F_q^\times,\quad c\in\mathbf F_q,
}
\]
so there are precisely
\[
q(q-1)
\]
of them.

The same equations over every extension field give
\[
|\operatorname{Reyn}(L_q)(\mathbf F_{q^m})|
=
3q^{2m}-2q^m.
\]
Consequently the Hasse–Weil zeta function of the reduced Reynolds-operator solution set is
\[
\boxed{
Z(T)=\frac{(1-qT)^2}{(1-q^2T)^3}.
}
\]

## Assumptions and scope

The algebra is the smallest nonabelian Lie algebra. Over any field it is the affine Lie algebra of the line, characterized by
\[
[e,f]=f.
\]

The Reynolds identity is the Lie-algebra identity introduced by Das as a special case of a twisted Rota–Baxter operator:
\[
[Rx,Ry]
=
R\!\left([Rx,y]+[x,Ry]-[Rx,Ry]\right).
\]

Das works over characteristic zero. The calculation here uses the identity itself and is valid over every finite field, including characteristic \(2\).

No quotient by \(\operatorname{Aut}(L_q)\) is taken.

## Proof

Write
\[
R(e)=ae+cf,
\qquad
R(f)=be+df.
\]

Since
\[
[x_1e+x_2f,\ y_1e+y_2f]
=
(x_1y_2-x_2y_1)f,
\]
the Reynolds identity is automatic on the ordered pairs
\[
(e,e)
\qquad\text{and}\qquad
(f,f).
\]

For the pair
\[
(e,f),
\]
direct substitution gives the two scalar equations
\[
b(ad-a-bc-d)=0
\]
and
\[
ad^2-bcd-bc-d^2=0.
\]
The second equation is
\[
d^2(a-1)-bc(d+1)=0.
\]
The pair
\[
(f,e)
\]
gives the negatives of the same equations, so there are no further conditions.

Now split according to \(b\).

If
\[
b=0,
\]
the second equation becomes
\[
d^2(a-1)=0.
\]
Thus either
\[
d=0,
\]
with \(a,c\) arbitrary, or
\[
d\ne0,\qquad a=1,
\]
with \(c\) arbitrary. These branches contain
\[
q^2
\]
and
\[
q(q-1)
\]
operators, respectively.

Suppose now that
\[
b\ne0.
\]
The first equation forces
\[
bc=ad-a-d.
\]
Substituting this into the second equation gives
\[
a+d=0.
\]
Hence
\[
d=-a
\]
and then
\[
bc=-a^2.
\]
For each
\[
a\in\mathbf F_q
\]
and each
\[
b\in\mathbf F_q^\times,
\]
there is a unique
\[
c=-a^2/b.
\]
This branch therefore has
\[
q(q-1)
\]
operators.

Adding the three disjoint branches gives
\[
q^2+q(q-1)+q(q-1)
=
3q^2-2q.
\]

For ranks, the first branch consists of matrices
\[
\begin{pmatrix}
a&0\\
c&0
\end{pmatrix}.
\]
Exactly one is zero, and the remaining
\[
q^2-1
\]
have rank \(1\).

Every matrix in the second branch is
\[
\begin{pmatrix}
1&0\\
c&d
\end{pmatrix},
\qquad d\ne0,
\]
and therefore has rank \(2\). This gives
\[
q(q-1)
\]
rank-two operators.

In the third branch,
\[
\det R
=
ad-bc
=
-a^2-(-a^2)=0,
\]
while
\[
b\ne0.
\]
Hence every operator in that branch has rank \(1\). It contributes
\[
q(q-1)
\]
additional rank-one operators.

Thus
\[
1+(q^2-1)+q(q-1)+q(q-1)=3q^2-2q
\]
with the asserted rank distribution.

Finally, replacing \(q\) by \(q^m\) gives
\[
N_m=3q^{2m}-2q^m.
\]
Therefore
\[
\begin{aligned}
Z(T)
&=
\exp\!\left(
\sum_{m\ge1}\frac{N_mT^m}{m}
\right)\\
&=
\exp\!\left(
3\sum_{m\ge1}\frac{q^{2m}T^m}{m}
-
2\sum_{m\ge1}\frac{q^mT^m}{m}
\right)\\
&=
\frac{(1-qT)^2}{(1-q^2T)^3}.
\end{aligned}
\]

## Verification

The included program `artifacts/verify.py` reconstructs the Reynolds defect from the bracket
\[
[e,f]=f.
\]

Symbolically it obtains exactly the two polynomial equations
\[
b(ad-a-bc-d)=0,
\]
\[
d^2(a-1)-bc(d+1)=0.
\]

It then exhaustively tests every \(2\times2\) matrix over
\[
\mathbf F_2,\qquad
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7
\]
against the defining identity.

The resulting totals are
\[
8,\qquad21,\qquad65,\qquad133,
\]
equal to
\[
3q^2-2q.
\]

The corresponding rank distributions are
\[
(1,5,2),
\]
\[
(1,14,6),
\]
\[
(1,44,20),
\]
and
\[
(1,90,42).
\]

The script returns `VERIFY_OK`.

The finite checks replay the proof; the arbitrary-prime-power formula is established by the exact branch decomposition above.

## Relationship to prior work

Das introduced twisted Rota–Baxter operators on Lie algebras and identified Reynolds operators as a special class. The paper develops their graph description, cohomology, deformation theory, relation with derivations, and the associated NS-Lie structures. It does not give a classification or finite-field census for the two-dimensional affine Lie algebra.

Xu, Wang, and Zhao later extended the framework to Hom-Lie algebras and again treated Reynolds operators as a distinguished special case. Their work is structural and cohomological rather than an exact low-dimensional finite-field enumeration.

The two-dimensional affine Lie algebra is the unique nonabelian Lie algebra of dimension \(2\), so it is the canonical first finite test object for the Reynolds identity.

Targeted searches for Reynolds operators on the two-dimensional nonabelian or affine Lie algebra, finite-field counts, rank distributions, and the exact polynomial
\[
3q^2-2q
\]
did not locate a covering result.

## Limitations

The exact count and rank distribution concern only the two-dimensional affine Lie algebra.

No classification modulo algebra automorphisms is claimed.

The zeta statement refers to the reduced solution set determined by the field-valued Reynolds equations. It does not assert that the scheme defined by the two displayed equations is reduced in every characteristic.

A specialized or differently indexed classification may exist. Failed searches do not prove novelty.

## References

1. A. Das, “Twisted Rota–Baxter operators and Reynolds operators on Lie algebras and NS-Lie algebras,” arXiv:2009.09368v1, first public 20 September 2020; *Journal of Mathematical Physics* 62 (2021), 091701, DOI `10.1063/5.0051142`.
2. S. Xu, W. Wang, and J. Zhao, “Twisted Rota-Baxter operators on Hom-Lie algebras,” *AIMS Mathematics* 9 (2024), 2619–2640, DOI `10.3934/math.2024129`.
