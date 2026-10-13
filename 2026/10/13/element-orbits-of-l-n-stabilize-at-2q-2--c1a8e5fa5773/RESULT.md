# Element orbits of \(L_n\) stabilize at \(2q+2\)

## Finding

Let \(K\) be any field. For \(n\ge2\), let \(L_n(K)\) be the left Leibniz algebra with basis
\[
\{e_1,e_2,f_3,\ldots,f_n\}
\]
and sole nonzero bracket
\[
[e_2,e_1]=e_1.
\]

Put
\[
D=[L_n,L_n]=K e_1.
\]
For \(n\ge3\), the center is
\[
Z=Z(L_n)=\operatorname{span}\{f_3,\ldots,f_n\}.
\]

Every automorphism has the form
\[
\boxed{
\phi(e_1)=\beta e_1,\qquad
\phi(e_2)=e_2+b,\qquad
\phi|_Z=B,
}
\]
where
\[
\beta\in K^\times,\qquad
b\in Z,\qquad
B\in\operatorname{GL}(Z).
\]

Define the intrinsic scalar
\[
\chi(x)\in K
\]
by the condition
\[
[x,d]=\chi(x)d
\qquad
(d\in D).
\]
Since \(D\) is one-dimensional and characteristic, \(\chi\) is invariant under every automorphism.

For \(n\ge3\), the automorphism orbits on \(L_n\) are exactly
\[
\boxed{\{0\},}
\]
\[
\boxed{D\setminus\{0\},}
\]
\[
\boxed{Z\setminus\{0\},}
\]
\[
\boxed{(D\setminus\{0\})+(Z\setminus\{0\}),}
\]
and, for each \(c\in K^\times\), the two sets
\[
\boxed{
\{x:\chi(x)=c,\ [x,x]=0\}
}
\]
and
\[
\boxed{
\{x:\chi(x)=c,\ [x,x]\ne0\}.
}
\]

Thus every nonzero value of the adjoint scalar \(\chi\) contributes exactly two orbits, while the zero fiber contributes exactly four orbits once \(n\ge3\).

For \(n=2\), the center is zero, so the zero fiber has only
\[
\{0\}
\quad\text{and}\quad
D\setminus\{0\}.
\]
Hence over a finite field
\[
\boxed{
|L_2(\mathbf F_q)/\operatorname{Aut}(L_2)|=2q,
}
\]
whereas for every \(n\ge3\),
\[
\boxed{
|L_n(\mathbf F_q)/\operatorname{Aut}(L_n)|=2q+2.
}
\]

The striking point is that after dimension \(3\), the number of element orbits is completely independent of the dimension.

If
\[
m=n-2\ge1,
\]
the six orbit types over \(\mathbf F_q\) have sizes
\[
\boxed{
1,\quad
q-1,\quad
q^m-1,\quad
(q-1)(q^m-1),
}
\]
and, for each \(c\in\mathbf F_q^\times\),
\[
\boxed{
q^m,\qquad
(q-1)q^m.
}
\]

## Assumptions and scope

The theorem concerns the canonical algebra \(L_n(K)\) itself and is valid over every field, including characteristic \(2\).

The classification result used as the literature anchor proves that, over fields of characteristic different from \(2\), every non-nilpotent non-Lie finite-dimensional Leibniz algebra with one-dimensional derived subalgebra is isomorphic to this \(L_n\). Thus, in that characteristic range, the orbit theorem applies to the entire class classified there.

The finite-field statements count automorphism orbits of elements, not isomorphism classes of algebras.

## Proof

Write
\[
V=\operatorname{span}\{f_3,\ldots,f_n\},
\]
with \(V=0\) when \(n=2\).

First derive the automorphism group directly.

The derived algebra
\[
D=K e_1
\]
is characteristic, so every automorphism satisfies
\[
\phi(e_1)=\beta e_1
\]
for some
\[
\beta\in K^\times.
\]

Write
\[
\phi(e_2)=a e_1+c e_2+b,
\qquad
b\in V.
\]
Preservation of
\[
[e_2,e_1]=e_1
\]
gives
\[
[\phi(e_2),\phi(e_1)]
=
c\beta e_1
=
\beta e_1,
\]
hence
\[
c=1.
\]
Preservation of
\[
[e_2,e_2]=0
\]
then gives
\[
[\phi(e_2),\phi(e_2)]
=
a e_1
=
0,
\]
so
\[
a=0.
\]

The center is \(V\), hence characteristic, so
\[
\phi|_V=B
\]
for some
\[
B\in\operatorname{GL}(V).
\]
Conversely every such triple \((\beta,b,B)\) preserves the sole nonzero bracket.

Now write
\[
x=u e_1+c e_2+v,
\qquad
v\in V.
\]
Then
\[
\phi(x)
=
\beta u\,e_1+c e_2+(cv+Bv).
\]

The coefficient \(c\) is exactly the intrinsic scalar \(\chi(x)\), because
\[
[x,e_1]=c e_1.
\]
Thus \(c\) is constant on automorphism orbits.

Suppose
\[
c\ne0.
\]
Since \(b\) is arbitrary, choose it to kill the \(V\)-component. The scalar \(\beta\) independently rescales every nonzero \(u\). Therefore the fiber
\[
\chi^{-1}(c)
\]
has exactly two orbits:
\[
u=0
\quad\text{and}\quad
u\ne0.
\]
These are intrinsically distinguished because
\[
[x,x]=cu\,e_1.
\]
Thus they are exactly the square-zero and non-square-zero parts of the fiber.

Now suppose
\[
c=0.
\]
Then
\[
\phi(x)=\beta u\,e_1+Bv.
\]
The two factors act independently. If \(V\ne0\), the group \(\operatorname{GL}(V)\) is transitive on \(V\setminus\{0\}\), so there are four possibilities according to whether \(u\) and \(v\) vanish:
\[
0,\qquad
D\setminus\{0\},\qquad
V\setminus\{0\},\qquad
(D\setminus\{0\})+(V\setminus\{0\}).
\]
When \(V=0\), only the first two remain.

For finite fields, let
\[
|K|=q
\]
and
\[
m=\dim V=n-2.
\]
The first four orbit sizes for \(m\ge1\) are respectively
\[
1,\qquad
q-1,\qquad
q^m-1,\qquad
(q-1)(q^m-1).
\]

For each
\[
c\ne0,
\]
the square-zero orbit has arbitrary \(V\)-component and fixed \(u=0\), hence size
\[
q^m.
\]
The non-square-zero orbit has arbitrary \(V\)-component and arbitrary nonzero \(u\), hence size
\[
(q-1)q^m.
\]

There are
\[
4+2(q-1)=2q+2
\]
orbits for \(n\ge3\), and
\[
2+2(q-1)=2q
\]
for \(n=2\).

As a consistency check, the orbit sizes sum to
\[
q^n.
\]

## Verification

The included checker verifies the orbit theorem directly for
\[
q\in\{2,3,5\}
\]
and
\[
n\in\{2,3,4\}.
\]

For each pair \((q,n)\), it constructs the full automorphism group from the defining bracket, checks every listed transformation, computes all element orbits, and compares the resulting representatives and sizes with the closed formulas.

In particular:
\[
L_3(\mathbf F_2)
\]
has \(6\) element orbits,
\[
L_3(\mathbf F_3)
\]
has \(8\), and
\[
L_4(\mathbf F_5)
\]
has \(12\), exactly as the dimension-stable formula predicts.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.

## Relationship to prior work

Di Bartolo, La Rosa, and Mancini classify the non-nilpotent non-Lie Leibniz algebras with one-dimensional derived subalgebra over fields of characteristic different from \(2\). Their theorem shows that every such algebra is
\[
L_n=S_2\oplus K^{n-2},
\]
with sole nonzero bracket
\[
[e_2,e_1]=e_1.
\]

The same paper computes the complete automorphism group as the block matrices corresponding precisely to
\[
\phi(e_1)=\beta e_1,\qquad
\phi(e_2)=e_2+b,\qquad
\phi|_Z=B.
\]

The present result uses that symmetry description as the starting point and determines the complete orbit geometry of the underlying element set. The orbit classification is intrinsic through the adjoint scalar \(\chi\), the derived line \(D\), the center \(Z\), and the square map.

Nearby work on automorphism groups of low-dimensional and non-nilpotent Leibniz algebras focuses on describing the groups themselves. The inspected abstracts and searchable pages do not state element-orbit classifications or the dimension-stable finite-field count \(2q+2\).

Targeted semantic-database and literature searches for \(L_n\), \(S_2\), one-dimensional derived subalgebras, element automorphism orbits, and finite-field orbit counts did not locate the theorem above.

## Limitations

The class-wide conclusion from the 2023 classification source is restricted to characteristic different from \(2\). The orbit theorem for the fixed canonical algebra \(L_n(K)\) itself is characteristic-free.

The result classifies single elements only; it does not classify tuples, subalgebras, ideals, or endomorphisms under automorphisms.

A specialized or unindexed source may contain the same element-orbit stratification.

Failed searches do not prove novelty.

## References

1. A. Di Bartolo, G. La Rosa, and M. Mancini, “Non-nilpotent Leibniz algebras with one-dimensional derived subalgebra,” arXiv:2307.09102v1, first public version 18 July 2023; *Mediterranean Journal of Mathematics* 21 (2024), 138, DOI 10.1007/s00009-024-02679-0. MSC 2020: 16W25, 17A32, 17B30, 17B40, 20M99, 22A30.
2. L. A. Kurdachenko, P. Ye. Minaiev, and O. O. Pypka, “Automorphism groups of some non-nilpotent Leibniz algebras,” *Researches in Mathematics* 32 (2024), DOI 10.15421/242409.
3. L. Kurdachenko, O. Pypka, and M. Semko, “On the Structure of Automorphism Groups of Some Low-Dimensional Leibniz Algebras,” *Ukrainian Mathematical Journal* 76 (2024), 973–987, DOI 10.1007/s11253-024-02367-y.
