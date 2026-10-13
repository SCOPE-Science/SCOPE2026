# Rank-one Rota–Baxter geometry of a four-dimensional Lie–Yamaguti example

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2,
\]
and let \(L_K\) be the four-dimensional Lie–Yamaguti algebra with basis
\[
\{e_1,e_2,e_3,e_4\},
\]
whose sole independent nonzero products are
\[
[e_1,e_2]=2e_4,
\qquad
\llbracket e_1,e_2,e_1\rrbracket=e_4.
\]

The rank-at-most-one weight-zero Rota–Baxter locus is exactly
\[
\boxed{
\mathcal R_{\le1}=\mathcal A\cup\mathcal B,
}
\]
where
\[
\mathcal A=
\{R:\operatorname{rank}R\le1,\ R(e_4)=0\}
\]
and
\[
\mathcal B=
\{R:\operatorname{rank}R\le1,\ \operatorname{im}R\subseteq\langle e_3,e_4\rangle\}.
\]

Equivalently, if \(R\ne0\) has rank one and
\[
R(x)=\ell(x)u
\]
with \(u\ne0\) and \(\ell\ne0\), then
\[
\boxed{
R\text{ is Rota–Baxter}
\iff
\ell(e_4)=0
\text{ or }
u\in\langle e_3,e_4\rangle.
}
\]

This gives a simple operator omitted by the displayed family in the source example:
\[
\boxed{E_{21}.}
\]
Indeed, \(E_{21}(e_1)=e_2\) and \(E_{21}(e_j)=0\) for \(j\ne1\), so \(E_{21}(e_4)=0\). The source's displayed matrix family has zero second row, hence does not contain \(E_{21}\).

Geometrically, \(\mathcal A\) is the rank-at-most-one determinantal variety of \(4\times3\) matrices, so
\[
\dim \mathcal A=6.
\]
The component \(\mathcal B\) is the rank-at-most-one determinantal variety of \(2\times4\) matrices, so
\[
\dim \mathcal B=5.
\]
Their intersection is the rank-at-most-one determinantal variety of \(2\times3\) matrices,
\[
\mathcal A\cap\mathcal B
=
\{R:\operatorname{rank}R\le1,\ R(e_4)=0,\ \operatorname{im}R\subseteq\langle e_3,e_4\rangle\},
\]
with
\[
\dim(\mathcal A\cap\mathcal B)=4.
\]

Over every odd finite field \(\mathbf F_q\),
\[
\boxed{
|\mathcal R_{\le1}(\mathbf F_q)|
=q^6+2q^5+q^4-q^3-q^2-q.
}
\]

Over every extension field \(\mathbf F_{q^m}\),
\[
|\mathcal R_{\le1}(\mathbf F_{q^m})|
=q^{6m}+2q^{5m}+q^{4m}-q^{3m}-q^{2m}-q^m.
\]
Thus the reduced Hasse–Weil zeta function of this rank-at-most-one Rota–Baxter locus is
\[
\boxed{
Z(T)=
\frac{(1-qT)(1-q^2T)(1-q^3T)}{(1-q^4T)(1-q^5T)^2(1-q^6T)}.
}
\]

## Assumptions and scope

Sheng and Zhao introduced relative Rota–Baxter operators on Lie–Yamaguti algebras and, in their four-dimensional Example 3.5, used the algebra above. Their preprint was first public on 8 August 2021. Zhao and Qiao later reused the same algebra and displayed Rota–Baxter family in their deformation paper; that paper lists \(17B38\) as its primary Mathematics Subject Classification code and states the Rota–Baxter identities explicitly.

The source papers work in characteristic zero. The proof below extends the rank-at-most-one statement to every field of characteristic different from \(2\). Characteristic \(2\) is excluded because the binary product \([e_1,e_2]=2e_4\) degenerates there.

This is not a classification of all Rota–Baxter operators on \(L_K\). It is an exact classification of the natural minimal nonzero rank stratum together with its closure, arithmetic, and component geometry.

## Proof

For vectors \(x,y,z\in L_K\), put
\[
\omega(x,y)=x_1y_2-x_2y_1.
\]
Then
\[
[x,y]=2\omega(x,y)e_4,
\qquad
\llbracket x,y,z\rrbracket=\omega(x,y)z_1e_4.
\]

A weight-zero Rota–Baxter operator satisfies
\[
[Rx,Ry]
=
R\bigl([Rx,y]-[Ry,x]\bigr)
\]
and
\[
\llbracket Rx,Ry,Rz\rrbracket
=
R\bigl(
\llbracket Rx,Ry,z\rrbracket
+
\llbracket x,Ry,Rz\rrbracket
+
\llbracket Rx,y,Rz\rrbracket
\bigr).
\]

Suppose first that \(R\ne0\) has rank one. Write
\[
R(x)=\ell(x)u,
\qquad
u=(u_1,u_2,u_3,u_4)^T,
\]
with nonzero linear functional \(\ell\). Define
\[
h(x)=u_1x_2-u_2x_1.
\]
Since \(Rx\) and \(Ry\) are collinear,
\[
[Rx,Ry]=0,
\qquad
\llbracket Rx,Ry,Rz\rrbracket=0.
\]
A direct substitution gives the binary defect
\[
-2\ell(e_4)
\bigl(\ell(x)h(y)-\ell(y)h(x)\bigr)u.
\]
The ternary defect is
\[
-\ell(e_4)u_1\ell(z)
\bigl(\ell(x)h(y)-\ell(y)h(x)\bigr)u.
\]
Thus, because \(2\ne0\), the binary identity is decisive and the two identities hold exactly when
\[
\ell(e_4)\,\ell\wedge h=0.
\]

If \(\ell(e_4)=0\), then \(R(e_4)=0\), giving \(\mathcal A\).

Now assume \(\ell(e_4)\ne0\). Then \(\ell\wedge h=0\). If \(h\ne0\), the two nonzero linear functionals \(\ell\) and \(h\) are proportional. But
\[
h(e_4)=0
\]
while
\[
\ell(e_4)\ne0,
\]
a contradiction. Hence \(h=0\), so
\[
u_1=u_2=0,
\]
which is exactly
\[
\operatorname{im}R\subseteq\langle e_3,e_4\rangle.
\]
This gives \(\mathcal B\). The converse is immediate from the defect formulas. Adding the zero map yields the asserted rank-at-most-one union.

For finite-field counting, the number of rank-at-most-one \(m\times n\) matrices is
\[
1+\frac{(q^m-1)(q^n-1)}{q-1}.
\]
Therefore
\[
|\mathcal A|
=1+\frac{(q^4-1)(q^3-1)}{q-1},
\]
\[
|\mathcal B|
=1+\frac{(q^2-1)(q^4-1)}{q-1},
\]
and
\[
|\mathcal A\cap\mathcal B|
=1+\frac{(q^2-1)(q^3-1)}{q-1}.
\]
Inclusion–exclusion simplifies to
\[
q^6+2q^5+q^4-q^3-q^2-q.
\]
Replacing \(q\) by \(q^m\) gives the extension-field count and hence the stated zeta function.

## Verification

The included program `artifacts/verify.py` reconstructs the two Lie–Yamaguti products and the two Rota–Baxter identities from the source definitions.

For a symbolic rank-one operator \(R=u\otimes\ell\), it verifies the two universal defect formulas above exactly.

It then enumerates every rank-at-most-one \(4\times4\) matrix over \(\mathbf F_3\), tests both Rota–Baxter identities directly on all basis pairs and triples, and confirms that the direct solution set equals \(\mathcal A\cup\mathcal B\). There are
\[
3201
\]
rank-at-most-one matrices in total and exactly
\[
1257
\]
Rota–Baxter matrices. The checker also verifies \(E_{21}\) directly.

The component-count formulas are replayed over \(\mathbf F_5\), \(\mathbf F_7\), and \(\mathbf F_{11}\), giving respectively
\[
22345,
\qquad
153265,
\qquad
2106841
\]
points in the rank-at-most-one Rota–Baxter locus.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is the symbolic rank-one proof above.

## Relationship to prior work

The 2021 Sheng–Zhao paper introduces relative Rota–Baxter operators on Lie–Yamaguti algebras and contains this four-dimensional algebra as an explicit example. The openly indexed source text shows a substantial matrix family of Rota–Baxter operators, but the present theorem does not rely on that paper for an exhaustiveness claim.

The 2022 Zhao–Qiao preprint, later published in 2024, gives the Rota–Baxter equations explicitly and repeats the four-dimensional example. Its displayed family is
\[
\begin{pmatrix}
0&a_{12}&0&0\\
0&0&0&0\\
a_{31}&a_{32}&a_{33}&a_{34}\\
a_{41}&a_{42}&a_{43}&a_{44}
\end{pmatrix}.
\]
The paper states that this matrix is a Rota–Baxter operator; it does not assert that this is the complete operator locus. A full-text search of that paper found no rank-one classification.

The new statement is therefore not a correction of the displayed family. It classifies the entire rank-at-most-one stratum. The operator \(E_{21}\) proves that this stratum is not exhausted by the displayed family, because its second row is nonzero.

Targeted literature searches using the exact multiplication, rank-one terminology, the explicit operator \(E_{21}\), and finite-field formulations did not locate a covering classification.

## Limitations

The theorem does not classify Rota–Baxter operators of rank at least \(2\).

Characteristic \(2\) is excluded because the source binary bracket degenerates.

The arXiv HTML endpoint for the 2021 paper timed out during direct full-text access; its earliest public date and indexed example text were available, while the later same-object paper was inspected in full. No noncoverage conclusion depends solely on the inaccessible 2021 full text.

Failed searches do not prove absolute novelty.

## References

1. Y. Sheng and J. Zhao, “Relative Rota-Baxter operators and symplectic structures on Lie-Yamaguti algebras,” arXiv:2108.03556v1, first public 8 August 2021; *Communications in Algebra* 50 (2022), 4056–4073, DOI `10.1080/00927872.2022.2057517`.
2. J. Zhao and Y. Qiao, “Cohomology and deformations of relative Rota-Baxter operators on Lie-Yamaguti algebras,” arXiv:2204.04872v1, first public 11 April 2022; *Mathematics* 12 (2024), 166, DOI `10.3390/math12010166`.
