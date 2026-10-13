# Operator rigidity and parity splitting in a two-dimensional Hom-associative color algebra

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2.
\]
Consider the \(G=\{-1,+1\}\)-graded Hom-associative color algebra from Bakayoko–Attan Example 1.12:
\[
A_{-1}=Ke_2,\qquad A_1=Ke_1,
\]
with multiplication
\[
e_1e_1=-e_1,\qquad
e_1e_2=e_2e_1=e_2,\qquad
e_2e_2=e_1,
\]
and twisting map
\[
\alpha(e_1)=e_1,\qquad \alpha(e_2)=-e_2.
\]

Every even endomorphism is diagonal in the ordered basis \((e_1,e_2)\). The complete operator profile is:

1. For every \(\lambda\in K\), the weight-\(\lambda\) Rota–Baxter operators are
\[
\boxed{\{0\}}
\]
when \(\lambda=0\), and
\[
\boxed{\{0,-\lambda I\}}
\]
when \(\lambda\ne0\). In particular, the source's displayed operator \(R=-\lambda I\) is the unique nonzero even Rota–Baxter operator at nonzero weight.

2. The Nijenhuis operators are exactly
\[
\boxed{\{aI:a\in K\}}.
\]

3. For every integer \(k\), the \(\alpha^k\)-centroid is exactly
\[
\boxed{K\alpha^k}.
\]

4. The \(\alpha^k\)-averaging operators exhibit a parity jump. If \(k\) is odd, they are exactly
\[
\boxed{\{\operatorname{diag}(a,0):a\in K\}}.
\]
If \(k\) is even, they are exactly
\[
\boxed{
\{\operatorname{diag}(a,0):a\in K\}
\cup
\{aI:a\in K\}.
}
\]

Thus the Rota–Baxter, Nijenhuis, and centroid loci are rigid in the indicated senses, while the averaging locus changes from one affine line to two affine lines meeting at the origin when the parity of \(k\) changes. Over every odd finite field \(\mathbf F_q\), the averaging locus therefore has
\[
\boxed{q}
\]
points for odd \(k\) and
\[
\boxed{2q-1}
\]
points for even \(k\).

## Assumptions and scope

The primary source first appeared publicly as arXiv:1912.01358v1 on 3 December 2019 and lists \(17A30\) first among its Mathematics Subject Classification codes.

The source works over a field of characteristic different from \(2\). Its Example 1.12 gives the algebra, grading, bicharacter, twist, and the particular weight-\(\lambda\) Rota–Baxter operator
\[
R(e_1)=-\lambda e_1,\qquad R(e_2)=-\lambda e_2.
\]
The definitions immediately following the example introduce \(\alpha^k\)-averaging operators and the \(\alpha^k\)-centroid, and the next definition introduces Nijenhuis operators.

The classification here is restricted to even operators, which is the operator class used in those color-algebra definitions. Since both homogeneous components are one-dimensional, every even operator is automatically diagonal.

A later paper by Bakayoko and Silvestrov reuses the same algebra and the same Rota–Baxter operator as an example in a Hom-tridendriform color construction. That reuse motivates determining whether the displayed operator is representative of a larger family.

## Proof

Write an arbitrary even endomorphism as
\[
T=\operatorname{diag}(a,b).
\]

For a weight-\(\lambda\) Rota–Baxter operator \(R=\operatorname{diag}(a,b)\), the defining identity
\[
R(x)R(y)
=
R\bigl(R(x)y+xR(y)+\lambda xy\bigr)
\]
on the four basis pairs reduces exactly to
\[
a(a+\lambda)=0,
\qquad
b(b+\lambda)=0,
\qquad
b^2=a(2b+\lambda).
\]
If \(\lambda=0\), the first two equations force \(a=b=0\). If \(\lambda\ne0\), then
\[
a,b\in\{0,-\lambda\},
\]
and the third equation removes the two mixed choices. Hence only
\[
R=0
\qquad\text{and}\qquad
R=-\lambda I
\]
remain.

For a Nijenhuis operator \(N=\operatorname{diag}(a,b)\), use
\[
N(x)N(y)
=
N\bigl(N(x)y+xN(y)-N(xy)\bigr).
\]
The basis pairs containing \(e_1\) satisfy the identity identically. The pair \((e_2,e_2)\) gives
\[
b^2=a(2b-a),
\]
equivalently
\[
(a-b)^2=0.
\]
Because \(K\) is a field,
\[
a=b.
\]
Thus the Nijenhuis locus is precisely the scalar line.

For the remaining two operator classes, put
\[
s=(-1)^k,
\qquad
\alpha^k=\operatorname{diag}(1,s).
\]

An \(\alpha^k\)-centroid element \(\beta=\operatorname{diag}(a,b)\) satisfies
\[
\beta(xy)=\beta(x)\alpha^k(y)=\alpha^k(x)\beta(y).
\]
The basis equations reduce to
\[
b=sa,\qquad a=sb.
\]
Since \(s^2=1\), these are equivalent and give
\[
\beta=a\alpha^k.
\]

Finally, an \(\alpha^k\)-averaging operator satisfies
\[
\beta(x)\beta(y)
=
\beta\bigl(\beta(x)\alpha^k(y)\bigr)
=
\beta\bigl(\alpha^k(x)\beta(y)\bigr).
\]
For \(\beta=\operatorname{diag}(a,b)\), the complete basis reduction is
\[
b(a-b)=0,
\qquad
b(as-b)=0,
\qquad
ab(s-1)=0.
\]
If \(k\) is even, then \(s=1\), so the system is simply
\[
b(a-b)=0,
\]
which gives the union of the two lines
\[
b=0
\qquad\text{or}\qquad
b=a.
\]
If \(k\) is odd, then \(s=-1\). If \(b\ne0\), the first two equations imply simultaneously
\[
a=b
\qquad\text{and}\qquad
a=-b,
\]
hence \(2b=0\), contradicting the characteristic assumption. Therefore \(b=0\), giving only the first line.

## Verification

The bundled program `artifacts/verify.py` independently reconstructs the multiplication and the four operator identities.

It first verifies Hom-associativity on all homogeneous basis triples. It then exhaustively checks every even operator over
\[
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7,\qquad
\mathbf F_{11}.
\]
For each field it checks every weight \(\lambda\), both parities of \(k\), and every diagonal map.

The output confirms:
\[
|\operatorname{RB}_0|=1,
\qquad
|\operatorname{RB}_\lambda|=2\quad(\lambda\ne0),
\]
\[
|\operatorname{Nij}|=q,
\qquad
|\operatorname{Cent}_{k}|=q,
\]
and
\[
|\operatorname{Avg}_{k}|=
\begin{cases}
q,&k\text{ odd},\\
2q-1,&k\text{ even}.
\end{cases}
\]

The checker returns `VERIFY_OK`.

These finite-field checks are replay evidence, not the proof of the arbitrary-field statement. The arbitrary-field classification follows from the displayed polynomial reductions.

## Relationship to prior work

Bakayoko and Attan introduce the exact Hom-associative color algebra in Example 1.12 and exhibit
\[
R=-\lambda I
\]
as a weight-\(\lambda\) Rota–Baxter operator. They do not classify all even Rota–Baxter operators on the example, nor do they compute its Nijenhuis, centroid, or averaging loci.

Bakayoko and Silvestrov later reuse the same algebra and the same displayed Rota–Baxter operator in a Hom-tridendriform color construction. Their paper gives general Nijenhuis, averaging, and centroid constructions but does not state the complete operator profile above.

Searches were made for the example by arXiv identifier, authors, exact multiplication table, exact twist, Rota–Baxter terminology, Nijenhuis terminology, centroid terminology, averaging terminology, two-dimensional classification, and parity-dependent \(\alpha^k\)-operator formulations. No located source states the complete four-class classification or the averaging parity split.

## Limitations

The result concerns even operators on this specific two-dimensional Hom-associative color algebra.

Characteristic \(2\) is excluded, as in the primary source, and the odd-\(k\) averaging argument uses \(2\ne0\).

The published journal record of the primary paper was identified, but its journal-hosted full text was not retrievable during the literature check; the arXiv v1 full text was inspected instead.

An equivalent classification may exist under different Hom-color terminology or notation. Failed searches do not prove absolute historical novelty.

## References

1. I. Bakayoko and S. Attan, “Some structures of Hom-Poisson color algebras,” arXiv:1912.01358v1, 2019; later published in *Quasigroups and Related Systems* 29 (2021), 1–16.
2. I. Bakayoko and S. Silvestrov, “Hom-left-symmetric color dialgebras, Hom-tridendriform color algebras and Yau’s twisting generalizations,” *Afrika Matematika* 32 (2021), DOI `10.1007/s13370-021-00871-z`.
