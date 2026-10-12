# Heisenberg noncommuting graphs have exact spread colorings

## Finding

Let
\[
H_n(q)
\]
be the \((2n+1)\)-dimensional Heisenberg Lie algebra over the finite field
\[
\mathbf F_q,
\qquad n\ge1.
\]
Write
\[
Z=Z(H_n(q)).
\]
The quotient
\[
V=H_n(q)/Z
\]
is a \(2n\)-dimensional symplectic vector space over \(\mathbf F_q\): there is a nondegenerate alternating form
\[
B:V\times V\to\mathbf F_q
\]
such that
\[
[x,y]=B(\bar x,\bar y)z
\]
for a fixed nonzero \(z\in Z\).

Let
\[
\mathcal N(H_n(q))
\]
be the noncommuting graph whose vertex set is
\[
H_n(q)\setminus Z
\]
and in which
\[
x\sim y
\quad\Longleftrightarrow\quad
[x,y]\ne0.
\]

Then
\[
\boxed{
\alpha(\mathcal N(H_n(q)))
=
q(q^n-1)
}
\]
and
\[
\boxed{
\chi(\mathcal N(H_n(q)))
=
q^n+1.
}
\]

The maximum independent sets are exactly
\[
\boxed{
A\setminus Z
}
\]
where \(A\) is a maximal abelian subalgebra containing \(Z\). Equivalently,
\[
A/Z
\]
is a maximal totally isotropic \(n\)-dimensional subspace of \(V\).

Optimal colorings also admit an exact geometric classification. The \((q^n+1)\)-colorings of \(\mathcal N(H_n(q))\) are precisely the colorings arising from symplectic spreads of \(V\): if
\[
V\setminus\{0\}
=
\bigsqcup_{i=1}^{q^n+1}
(U_i\setminus\{0\}),
\]
where every \(U_i\) is a maximal totally isotropic \(n\)-subspace, then the color classes are
\[
(U_i\oplus Z)\setminus Z.
\]
Conversely, every optimal coloring yields such a spread.

Thus the exact chromatic number is not merely a covering count: every optimal coloring is a partition of the Heisenberg algebra by maximal abelian subalgebras meeting exactly in the center.

## Assumptions and scope

The graph convention is the element-level noncommuting graph introduced for finite-dimensional Lie algebras: central elements are omitted, and two noncentral elements are adjacent when their bracket is nonzero.

The result holds for every prime power \(q\), including even characteristic, and for every Heisenberg rank \(n\ge1\).

The theorem concerns the ordinary independence and chromatic numbers. It does not determine the clique number.

A later projective version of the noncommuting graph identifies its chromatic number with the minimum size of an abelian-subalgebra cover in general. The theorem here determines that minimum exactly for the Heisenberg family and classifies all extremal colorings.

## Proof

Write
\[
H_n(q)=V\oplus Z
\]
as a vector space, with
\[
\dim_{\mathbf F_q}V=2n,
\qquad
\dim_{\mathbf F_q}Z=1,
\]
and
\[
[(v,a),(w,b)]=B(v,w)z
\]
for a nondegenerate alternating form \(B\).

The graph has
\[
|V(\mathcal N(H_n(q)))|
=
q^{2n+1}-q
=
q(q^{2n}-1)
\]
vertices.

Let \(S\) be an independent set. For any two elements
\[
(v,a),(w,b)\in S,
\]
independence gives
\[
B(v,w)=0.
\]
Therefore the linear span
\[
U=\operatorname{span}_{\mathbf F_q}\{v:(v,a)\in S\}
\]
is totally isotropic.

A totally isotropic subspace of a nondegenerate symplectic \(2n\)-space has dimension at most \(n\). Hence
\[
|U\setminus\{0\}|
\le
q^n-1.
\]
For each nonzero \(v\in U\), there are exactly \(q\) possible central lifts
\[
(v,a),
\qquad a\in\mathbf F_q.
\]
Thus
\[
|S|
\le
q(q^n-1).
\]

Equality is attained by any maximal totally isotropic subspace \(U\) of dimension \(n\): all vertices
\[
(U\oplus Z)\setminus Z
\]
commute pairwise. Hence
\[
\alpha(\mathcal N(H_n(q)))=q(q^n-1).
\]

The equality case also proves the classification of maximum independent sets. If
\[
|S|=q(q^n-1),
\]
then its projection span \(U\) must have dimension \(n\), every nonzero vector of \(U\) must occur as a projection of a vertex in \(S\), and all \(q\) central lifts of every such vector must occur. Therefore
\[
S=(U\oplus Z)\setminus Z.
\]
The subalgebra
\[
A=U\oplus Z
\]
is maximal abelian.

For the chromatic number,
\[
\chi(\mathcal N(H_n(q)))
\ge
\frac{|V(\mathcal N(H_n(q)))|}{\alpha(\mathcal N(H_n(q)))}
=
\frac{q(q^{2n}-1)}{q(q^n-1)}
=
q^n+1.
\]

It remains to construct a coloring with exactly \(q^n+1\) colors.

Let
\[
E=\mathbf F_{q^n}.
\]
Identify the symplectic space \(V\) with \(E^2\), viewed as a \(2n\)-dimensional vector space over \(\mathbf F_q\), equipped with
\[
B((x,y),(x',y'))
=
\operatorname{Tr}_{E/\mathbf F_q}(xy'-x'y).
\]
This is a nondegenerate alternating form.

For every
\[
a\in E,
\]
put
\[
U_a=\{(x,ax):x\in E\},
\]
and put
\[
U_\infty=\{(0,y):y\in E\}.
\]
Every \(U_a\) and \(U_\infty\) has \(\mathbf F_q\)-dimension \(n\). Any two vectors in one \(U_a\) have determinant zero over \(E\), hence are orthogonal under \(B\), so every \(U_a\) is totally isotropic. The same is true of \(U_\infty\).

Distinct members intersect only in \(0\), and every nonzero vector of \(E^2\) lies in exactly one of them. Hence
\[
\{U_a:a\in E\}\cup\{U_\infty\}
\]
is a symplectic spread with
\[
q^n+1
\]
members.

Color every vertex whose nonzero quotient vector lies in \(U_a\) by the color \(a\), and use one additional color for \(U_\infty\). Each color class is independent. Therefore
\[
\chi(\mathcal N(H_n(q)))\le q^n+1,
\]
and so
\[
\chi(\mathcal N(H_n(q)))=q^n+1.
\]

Finally consider any optimal coloring with \(q^n+1\) colors. Since the number of vertices equals
\[
(q^n+1)\alpha(\mathcal N(H_n(q))),
\]
every color class must be a maximum independent set. Hence every color class is
\[
(U_i\oplus Z)\setminus Z
\]
for a maximal totally isotropic \(U_i\). Distinct classes are disjoint, so
\[
U_i\cap U_j=0
\]
for \(i\ne j\), and the classes cover all vertices, so the nonzero vectors of \(V\) are partitioned by the \(U_i\). Thus the \(U_i\) form a symplectic spread.

This proves the optimal-coloring classification.

## Verification

The included checker works with the projective quotient because the element graph is obtained from it by replacing every projective point by an independent fiber of size
\[
q(q-1).
\]

For the \(5\)-dimensional Heisenberg algebra over
\[
\mathbf F_2,
\]
the projective symplectic graph has \(15\) vertices. The checker exhaustively verifies that its independence number is \(3\), so the full Lie-algebra graph has
\[
\alpha=2\cdot3=6.
\]
It constructs a symplectic spread of five isotropic planes, giving
\[
\chi=5.
\]

For the \(5\)-dimensional Heisenberg algebra over
\[
\mathbf F_3,
\]
the checker constructs the \(40\)-vertex projective graph, exhaustively rules out independent sets of size \(5\), and verifies a partition into ten maximal isotropic projective lines. Thus
\[
\alpha_{\mathrm{proj}}=4,
\qquad
\chi_{\mathrm{proj}}=10,
\]
and therefore
\[
\alpha(\mathcal N(H_2(3)))=24,
\qquad
\chi(\mathcal N(H_2(3)))=10.
\]

The checker also verifies that every maximum independent set found in the \(\mathbf F_2\) test case spans a maximal totally isotropic subspace.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Chareh Khah Moghaddam, Erfanian, and Shamsaki introduced the element-level noncommuting graph of a finite-dimensional Lie algebra and proved general results on degree, connectivity, diameter, girth, Hamiltonicity, planarity, and related properties. Their full public preprint contains no Heisenberg specialization and no exact chromatic or independence formula.

Sriwongsa later introduced a projective quotient version of the graph. Theorem 2.18 of that paper proves that, over a finite field, the chromatic number equals the minimum number of abelian subalgebras needed to cover the Lie algebra. The inspected full text contains no Heisenberg or symplectic-spread specialization. The theorem here computes that minimum exactly for every finite Heisenberg algebra and strengthens it by classifying all maximum independent sets and every optimal coloring.

Related literature on finite Heisenberg Lie algebras studies subalgebra commutativity probabilities rather than element-level noncommuting graph colorings.

Targeted semantic searches under Heisenberg, noncommuting graph, chromatic number, independence number, symplectic spread, and abelian-cover formulations did not locate the displayed formulas or extremal classification.

## Limitations

The result uses the fact that the Heisenberg commutator is controlled by one nondegenerate alternating form. Class-two Lie algebras with a higher-dimensional derived algebra need not reduce to a single symplectic space.

The theorem does not determine the clique number of the noncommuting graph.

The projective chromatic-cover theorem is prior work; the new content is the exact Heisenberg value, the exact independence number, the extremal independent-set classification, and the bijection between optimal colorings and symplectic spreads.

Failed searches do not prove novelty.

## References

1. A. Chareh Khah Moghaddam, A. Erfanian, and A. Shamsaki, “On the non-commuting graph associated to a finite-dimensional Lie algebra,” arXiv:2406.15902v1, first public version 22 June 2024; later published in *Journal of the Indonesian Mathematical Society* 32 (2026), DOI 10.22342/jims.v32i1.1643. Primary MSC in the preprint: 17B60.
2. S. Sriwongsa, “Non-commuting graphs of projective spaces over central quotients of Lie algebras,” arXiv:2505.00726v1, 27 April 2025.
