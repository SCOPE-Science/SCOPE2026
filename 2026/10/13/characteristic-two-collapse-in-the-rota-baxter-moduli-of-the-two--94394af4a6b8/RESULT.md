# Characteristic-two collapse in the Rota–Baxter moduli of the two-dimensional cyclic Leibniz algebra

## Finding

Let \(K\) be any field. Let \(L_K\) be the two-dimensional left Leibniz algebra with basis
\[
\{e_1,e_2\}
\]
and sole nonzero bracket
\[
[e_1,e_1]=e_2.
\]

A linear map \(R:L_K\to L_K\) is a weight-zero Rota–Baxter operator when
\[
[R(x),R(y)]
=
R\bigl([R(x),y]+[x,R(y)]\bigr)
\]
for all \(x,y\in L_K\).

Write
\[
R(e_1)=a e_1+c e_2,
\qquad
R(e_2)=b e_1+d e_2.
\]
Then
\[
\boxed{
R\text{ is Rota--Baxter}
\iff
b=0,\qquad a(a-2d)=0.
}
\]

Thus, if
\[
\operatorname{char}K\ne2,
\]
the operator variety is the union of two affine planes,
\[
\boxed{
\{a=b=0\}
\ \cup\
\{b=0,\ a=2d\},
}
\]
meeting in the affine line
\[
\{a=b=d=0\}.
\]

In characteristic \(2\), the two set-theoretic components collapse:
\[
\boxed{
\operatorname{RB}_0(L_K)=\{a=b=0\}\cong\mathbb A^2_K.
}
\]

The algebra automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)
=
\left\{
\phi_{u,v}
=
\begin{pmatrix}
u&0\\
v&u^2
\end{pmatrix}
:
u\in K^\times,\ v\in K
\right\}.
}
\]
Conjugation acts by
\[
\boxed{
(a,c,d)
\longmapsto
\left(
a,\,
uc+\frac{v(a-d)}u,\,
d
\right).
}
\]

When
\[
\operatorname{char}K\ne2,
\]
every automorphism orbit contains exactly one of
\[
\boxed{0,}
\qquad
\boxed{E_{21},}
\]
\[
\boxed{
D_d=
\begin{pmatrix}
0&0\\
0&d
\end{pmatrix},
\quad d\in K^\times,
}
\]
or
\[
\boxed{
H_d=
\begin{pmatrix}
2d&0\\
0&d
\end{pmatrix},
\quad d\in K^\times.
}
\]

In characteristic \(2\), the \(H_d\) family coincides with \(D_d\), so the representatives are exactly
\[
\boxed{
0,\quad E_{21},\quad D_d\ (d\in K^\times).
}
\]

Consequently, over every finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{RB}_0(L_{\mathbf F_q})|
=
\begin{cases}
2q^2-q,&q\text{ odd},\\
q^2,&q\text{ even},
\end{cases}
}
\]
and the number of automorphism-conjugacy classes is
\[
\boxed{
|\operatorname{RB}_0(L_{\mathbf F_q})/\operatorname{Aut}(L_{\mathbf F_q})|
=
\begin{cases}
2q,&q\text{ odd},\\
q+1,&q\text{ even}.
\end{cases}
}
\]

For odd \(q\), the orbit sizes are one singleton orbit, one orbit of size \(q-1\), and \(2(q-1)\) orbits of size \(q\). For even \(q\), they are one singleton orbit, one orbit of size \(q-1\), and \(q-1\) orbits of size \(q\).

## Assumptions and scope

The algebra is the nilpotent two-dimensional cyclic non-Lie Leibniz algebra. It is the first case in the two-dimensional classification used by Zhang--Li--Zheng.

The Rota--Baxter weight is zero.

The source literature works over \(\mathbb C\) or in characteristic zero. The equations above are rederived directly and then interpreted over arbitrary fields; this is necessary because the characteristic-\(2\) component collapse is invisible over \(\mathbb C\).

The equivalence relation is conjugacy by automorphisms of the fixed Leibniz algebra. It is not simultaneous isomorphism of arbitrary Leibniz multiplications and operators.

## Proof

Let
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\]
in the column convention.

Because the only nonzero basis bracket is
\[
[e_1,e_1]=e_2,
\]
for vectors
\[
x=x_1e_1+x_2e_2,\qquad
y=y_1e_1+y_2e_2
\]
we have
\[
[x,y]=x_1y_1e_2.
\]

Apply the Rota--Baxter equation to the four ordered basis pairs.

For \((e_2,e_2)\), its \(e_2\)-coordinate gives
\[
b^2=0.
\]
Since \(K\) is a field,
\[
b=0.
\]

With \(b=0\), the only remaining nontrivial equation comes from the \(e_2\)-coordinate at \((e_1,e_1)\):
\[
a^2-2ad=0.
\]
Thus
\[
a(a-2d)=0.
\]

Conversely, direct substitution shows that \(b=0\) and \(a(a-2d)=0\) make every Rota--Baxter defect vanish.

If the characteristic is not \(2\), the scalar equation factors into the two distinct hyperplanes
\[
a=0
\quad\text{or}\quad
a=2d.
\]
Together with \(b=0\), these are two affine planes. Their intersection has
\[
a=b=d=0
\]
and free \(c\).

If the characteristic is \(2\), the equation becomes
\[
a^2=0,
\]
hence
\[
a=0.
\]
Therefore the set of field-valued solutions is the single affine plane
\[
a=b=0.
\]

Now determine automorphisms. Write
\[
\phi(e_1)=u e_1+v e_2.
\]
Multiplicativity forces
\[
\phi(e_2)=\phi([e_1,e_1])
=
[\phi(e_1),\phi(e_1)]
=
u^2e_2.
\]
Thus
\[
\phi=
\begin{pmatrix}
u&0\\
v&u^2
\end{pmatrix},
\]
and invertibility is equivalent to \(u\ne0\).

For an operator with \(b=0\), direct matrix multiplication gives
\[
\phi R\phi^{-1}
=
\begin{pmatrix}
a&0\\
uc+\dfrac{v(a-d)}u&d
\end{pmatrix}.
\]
Hence \(a\) and \(d\) are invariants.

If
\[
a=d=0,
\]
then
\[
c\longmapsto uc.
\]
There are exactly two orbits: \(c=0\), represented by \(0\), and \(c\ne0\), represented by \(E_{21}\).

If
\[
a=0,\qquad d\ne0,
\]
then
\[
a-d=-d\ne0,
\]
so \(v\) can be chosen uniquely after \(u\) to kill \(c\). This gives \(D_d\), and different \(d\) are inequivalent because \(d\) is invariant.

When the characteristic is not \(2\), the second component has
\[
a=2d.
\]
For \(d\ne0\),
\[
a-d=d\ne0,
\]
so again \(c\) can be removed, giving \(H_d\). The case \(d=0\) is already the intersection orbit.

When the characteristic is \(2\), \(a=2d\) reduces to \(a=0\), so this second family contributes no new points or orbits.

For the finite-field counts, in odd characteristic each affine plane has \(q^2\) points and their intersection has \(q\) points, giving
\[
2q^2-q.
\]
The normal forms give
\[
2+2(q-1)=2q
\]
orbits.

In even characteristic the solution set is one affine plane, giving \(q^2\) points, and the normal forms give
\[
2+(q-1)=q+1
\]
orbits.

The orbit-size statements follow directly from the conjugation formula. On the nonzero intersection line, \(K^\times\) acts transitively, giving size \(q-1\). For every \(D_d\), and for every \(H_d\) when present, the free shear parameter produces an orbit of size \(q\).

## Verification

The included checker `artifacts/verify.py` reconstructs every weight-zero Rota--Baxter defect symbolically from the multiplication table.

It obtains a polynomial ideal generated by
\[
a^2-2ad,\qquad ab,\qquad b^2,\qquad bd.
\]
Over a field this is equivalent to
\[
b=0,\qquad a(a-2d)=0.
\]

The checker independently derives and verifies the automorphism matrix and its conjugation formula.

It then exhaustively enumerates all linear maps and all algebra automorphisms over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]
The observed operator and orbit counts are
\[
(4,3),\quad
(15,6),\quad
(45,10),\quad
(91,14),
\]
respectively, exactly matching the theorem.

The checker returns `VERIFY_OK`.

Finite enumeration is not used as a proof of the arbitrary-field classification.

## Relationship to prior work

Das and Guo develop relative Rota--Baxter systems on Leibniz algebras and situate the ordinary Rota--Baxter identity inside that framework. Their work supplies a contemporary structural motivation for studying operator moduli on fixed Leibniz algebras but does not give the orbit classification above.

Zhang, Li, and Zheng give all weight-zero and weight-\(-1\) Rota--Baxter operators on solvable and nilpotent non-Lie Leibniz algebras of dimension at most three over \(\mathbb C\). Their Lemma 16 identifies the present nilpotent two-dimensional cyclic algebra, and Theorem 17 lists its raw Rota--Baxter operators. That result does not quotient by the automorphism group, does not give finite-field orbit counts, and does not expose the characteristic-\(2\) collapse because the ground field is complex.

Focused searches for automorphism normal forms, conjugacy classes, finite-field counts, and characteristic-\(2\) behavior for this cyclic Leibniz Rota--Baxter family did not locate a covering result.

## Limitations

The theorem treats only the nilpotent two-dimensional cyclic Leibniz algebra and weight zero.

It does not classify weight-\(-1\) operators or the second two-dimensional non-Lie Leibniz algebra.

The characteristic-\(2\) statement is set-theoretic on field-valued operators. No claim about the scheme structure of the polynomial solution space is made.

A specialized or unindexed source may contain an equivalent automorphism quotient. Failed searches do not prove novelty.

## References

1. A. Das and S. Guo, “Relative Rota-Baxter systems on Leibniz algebras,” arXiv:2101.04831v1, first public 13 January 2021. MSC 2020: 17A32, 17B38, 17B62.
2. L. Zhang, L. Li, and H. Zheng, “Rota-Baxter Leibniz Algebras and Their Constructions,” *Advances in Mathematical Physics* 2018, Article ID 8540674, DOI `10.1155/2018/8540674`.
