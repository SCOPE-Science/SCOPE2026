# A two-dimensional Hom-Leibniz algebra is misclassified as characteristically nilpotent

## Finding

Consider the two-dimensional Hom-Leibniz algebra \(L_2^1\) over \(\mathbb C\) with basis \(\{e_1,e_2\}\), twisting map
\[
\alpha=\operatorname{id},
\]
and only nonzero bracket
\[
[e_2,e_2]=e_1.
\]

The published derivation table gives
\[
\operatorname{Der}_{\alpha^r}(L_2^1)
=
\left\{
\begin{pmatrix}
d_1&d_2\\
0&d_1/2
\end{pmatrix}
:d_1,d_2\in\mathbb C
\right\},
\]
but labels the algebra
\[
\mathrm{CN}=\mathrm{Yes}.
\]
The derivation formula is correct, while the characteristically-nilpotent label is not.

Equivalently, writing \(d_1=2d\) and \(d_2=b\),
\[
\boxed{
\operatorname{Der}(L_2^1)
=
\left\{
\begin{pmatrix}
2d&b\\
0&d
\end{pmatrix}
:b,d\in\mathbb C
\right\}.
}
\]
Let
\[
H=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Then
\[
\operatorname{Der}(L_2^1)=\mathbb C H\oplus\mathbb C E
\]
and
\[
\boxed{[H,E]=E.}
\]
Therefore
\[
\gamma_2=[\operatorname{Der},\operatorname{Der}]=\mathbb C E
\]
and
\[
\gamma_n=\mathbb C E
\qquad(n\ge2).
\]
The derivation Lie algebra is the two-dimensional affine Lie algebra, which is solvable but not nilpotent. Hence, under the source's own definition,
\[
\boxed{L_2^1\text{ is not characteristically nilpotent}.}
\]

## Assumptions and scope

The correction is restricted to the source's row for \(L_2^1\) over \(\mathbb C\) with \(\alpha=\operatorname{id}\). No claim is made about any other row of the classification table.

The source defines a Hom-Leibniz algebra to be characteristically nilpotent when its Lie algebra \(\operatorname{Der}_{\alpha^0}(L)\) is nilpotent. Because \(\alpha=\operatorname{id}\), this is the ordinary derivation Lie algebra used below.

The correction does not challenge the printed derivation space itself. It corrects the logical classification of that space as nilpotent.

## Proof

Write a general linear map as
\[
D(e_1)=a e_1+c e_2,
\qquad
D(e_2)=b e_1+d e_2.
\]
Since \(\alpha=\operatorname{id}\), the relevant derivation identity is
\[
D([x,y])=[D(x),y]+[x,D(y)].
\]
Apply it to \(x=y=e_2\). Since \([e_2,e_2]=e_1\),
\[
D(e_1)
=[D(e_2),e_2]+[e_2,D(e_2)].
\]
Only the \(e_2\)-component of \(D(e_2)\) contributes to either bracket, so
\[
a e_1+c e_2=2d e_1.
\]
Thus
\[
c=0,
\qquad
a=2d.
\]
The remaining ordered basis pairs give no additional constraint. Consequently
\[
D=
\begin{pmatrix}
2d&b\\
0&d
\end{pmatrix},
\]
which agrees with the source's printed derivation formula after setting \(d_1=2d\) and \(d_2=b\).

Now take
\[
H=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Their commutator is
\[
[H,E]=HE-EH=E.
\]
Hence
\[
[\mathbb C H\oplus\mathbb C E,\mathbb C H\oplus\mathbb C E]=\mathbb C E,
\]
and because \([H,E]=E\),
\[
[\mathbb C H\oplus\mathbb C E,\mathbb C E]=\mathbb C E.
\]
The lower central series never reaches zero. Therefore the derivation Lie algebra is not nilpotent.

The source's definition of characteristically nilpotent therefore forces the corrected table entry
\[
\mathrm{CN}=\mathrm{No}.
\]

## Verification

The included checker `artifacts/verify.py` uses exact integer arithmetic. It verifies that \(H\) and \(E\) satisfy the derivation identity on all ordered basis pairs, checks
\[
[H,E]=E,
\]
and iterates the lower-central commutator with \(H\), confirming that the generator \(E\) persists rather than vanishing.

It also checks representative matrices of the form
\[
\begin{pmatrix}2d&b\\0&d\end{pmatrix}
\]
for several exact integer values of \(b,d\), and rejects maps violating the necessary relation \(a=2d\) or \(c=0\).

The checker returns `VERIFY_OK`.

The finite sample of parameter values is not used to prove the classification; the symbolic derivation calculation above is the proof.

## Relationship to prior work

Arfa, Saadaoui, and Silvestrov classify two-dimensional multiplicative Hom-Leibniz algebras and compute their centroids and derivations. Their paper explicitly introduces the characteristically-nilpotent condition through nilpotence of \(\operatorname{Der}_{\alpha^0}(L)\), then tabulates a CN status alongside each derivation algebra.

For \(L_2^1\), the displayed derivation space itself contains the decisive obstruction: after rescaling its diagonal parameter it has basis \(H,E\) with \([H,E]=E\). Thus the table's derivation formula and its CN label are mutually inconsistent.

A later Springer chapter carrying the same work still states the same characteristically-nilpotent definition and records the derivation algebra of \(L_2^1\) with basis proportional to \(H\) and \(E\). Focused searches for the exact algebra label, the derivation basis, “characteristically nilpotent,” and corrections or errata did not locate a published correction of the CN entry.

## Limitations

Only the CN status of \(L_2^1\) is assessed. Other rows of the source's classification and derivation tables are outside the claim.

The correction is stated over \(\mathbb C\), matching the derivation table being corrected. No positive-characteristic generalization is claimed.

An unindexed erratum or author correction may exist. Failed searches do not prove novelty.

## References

1. A. Arfa, N. Saadaoui, and S. Silvestrov, “Classification, centroids and derivations of two-dimensional Hom-Leibniz algebras,” arXiv:2110.13364v1, first public version 26 October 2021; later published as a Springer chapter, DOI 10.1007/978-3-031-32009-5_3. MSC 2020 includes 17B61 and 17D30.
