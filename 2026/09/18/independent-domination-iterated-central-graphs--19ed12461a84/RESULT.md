# Independent domination stabilizes on iterated central graphs

**Same-model review: passed. Independent audit: not yet performed.**

Let \(G\) be a finite connected simple graph of order \(n\ge 3\) and size \(m\). Write
\[
C^0(G)=G,\qquad C^{j+1}(G)=C(C^j(G)),
\]
where \(C\) is the central-graph operator, and put
\[
n_j=|V(C^j(G))|,\qquad m_j=|E(C^j(G))|.
\]

## Main result

For every integer \(k\ge 3\),
\[
\boxed{\,i(C^k(G))=2m_{k-2}\,}.
\]

The numbers \(n_j,m_j\) obey
\[
n_{j+1}=n_j+m_j,\qquad
m_{j+1}=\binom{n_j}{2}+m_j,
\]
with \(n_0=n\) and \(m_0=m\). Consequently, every value \(i(C^k(G))\) for
\(k\ge3\) is determined by the two numbers \(n,m\) alone. In particular,
\[
\boxed{\,i(C^3(G))=n(n-1)+2m\,}
\]
and
\[
\boxed{\,i(C^4(G))
=m^2+2mn+m+2n^2-2n\,}.
\]

Thus any two connected graphs having the same order and size have identical
independent domination numbers after at least three central iterations.

## Lemma: independence number of a central graph

For every connected graph \(G\) of order at least \(3\) and size \(m\),
\[
\boxed{\alpha(C(G))=m.}
\]

### Proof

The \(m\) subdivision vertices introduced by the central construction are
pairwise nonadjacent, so \(\alpha(C(G))\ge m\).

Let \(S\) be any independent set of \(C(G)\), and let
\(Q=S\cap V(G)\). Two original vertices are adjacent in \(C(G)\) exactly when
they are nonadjacent in \(G\); hence \(Q\) is a clique of \(G\). A subdivision
vertex corresponding to an edge of \(G\) can belong to \(S\) only when neither
endpoint of that edge lies in \(Q\). Therefore
\[
|S|\le |Q|+|E(G-Q)|.
\]
If \(Q=\varnothing\), the right-hand side is \(m\). If \(q=|Q|\ge1\), let
\(r(Q)\) be the number of edges of \(G\) incident with at least one vertex of
\(Q\). Then
\[
|Q|+|E(G-Q)|=m-r(Q)+q.
\]
We have \(r(Q)\ge q\): for \(q=1\), connectedness gives positive degree; for
\(q=2\), the clique edge together with an edge leaving \(Q\) gives at least two
incident edges because \(n\ge3\) and \(G\) is connected; and for \(q\ge3\),
the \(\binom q2\) internal clique edges already satisfy
\(\binom q2\ge q\). Thus \(|S|\le m\), proving the lemma. \(\square\)

## Proof of the main result

Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz proved that
for every connected graph \(H\) of order \(N\ge3\), size \(M\), and
independence number \(a\),
\[
i(C^2(H))
=
M+\binom N2+\frac{a^2-a(2N-3)}2.
\tag{1}
\]
This is Theorem 2.12 of arXiv:2609.16357v1.

Fix \(k\ge3\) and set
\[
Y=C^{k-3}(G),\qquad H=C(Y).
\]
Write \(r=|V(Y)|\) and \(s=|E(Y)|\). The central-graph construction gives
\[
|V(H)|=r+s,\qquad |E(H)|=\binom r2+s.
\]
By the lemma,
\[
\alpha(H)=s.
\]
Applying (1) to \(H\) gives
\[
\begin{aligned}
i(C^k(G))
&=i(C^2(H))\\
&=|E(H)|+\binom{r+s}{2}
 +\frac{s^2-s(2(r+s)-3)}2.
\end{aligned}
\]
The last two terms simplify to
\[
\binom{r+s}{2}
+\frac{s^2-s(2(r+s)-3)}2
=\binom r2+s
=|E(H)|.
\]
Hence
\[
i(C^k(G))=2|E(H)|=2m_{k-2},
\]
as claimed. \(\square\)

## Relation to prior literature

The immediate source is:

- A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar,
  A. Serrano-Díaz, *Independent domination in central graphs*,
  arXiv:2609.16357v1 (2026),
  https://arxiv.org/abs/2609.16357

That paper develops independent domination for \(C(G)\), explicitly introduces
the notation \(C^2(G)\), and ends its results section with the closed formula
(1) for \(i(C^2(G))\). The result above starts at the next iterate:
the new ingredient is the exact identity \(\alpha(C(G))=|E(G)|\), which makes
the published \(C^2\)-formula collapse under further iteration.

Related work on ordinary domination of central graphs includes:

- R. D. Barish, S. Fujita, F. Kazemnejad, B. Pahlousay,
  *Classification of Graphs Via Vertex Cover and Domination Numbers*,
  Graphs and Combinatorics 42 (2026), article 33,
  https://doi.org/10.1007/s00373-026-03028-6

It concerns the ordinary domination number rather than independent domination
and does not imply the iteration law above.

## Verification

A standalone verification script in `artifacts/verify.py` checks the structural
identities on the NetworkX graph atlas. For all connected atlas graphs of orders
\(3\) through \(7\), it verifies \(\alpha(C(G))=|E(G)|\) and the algebraic
collapse of the published \(C^2\)-formula after substituting \(C(G)\). For all
connected atlas graphs of orders \(3\) through \(5\), it also computes minimum
maximal independent sets directly in \(C^2(G)\) and \(C^3(G)\) and confirms the
stated formulas.

The computation is supporting evidence only; the general result is proved above.

## Limitations

The theorem assumes finite connected simple graphs of order at least \(3\), in
the same setting as the source theorem used in the proof. No claim is made here
for disconnected graphs or for order \(1\) or \(2\).

Originality is asserted only to the best of our knowledge. Exact and synonymous
searches for independent domination of iterated central graphs, \(C^3(G)\), and
higher central iterates did not locate an equivalent result. The primary 2026
source was inspected through its complete HTML version, including its final
Theorem 2.12. Very recent or unindexed parallel work remains a residual risk.
No independent validation or independent audit is asserted.
