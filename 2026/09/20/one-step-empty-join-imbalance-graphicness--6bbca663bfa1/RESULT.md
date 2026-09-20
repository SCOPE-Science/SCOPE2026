# A one-step improvement for empty joins in imbalance graphicness

## Statement

For a finite simple graph \(X\), define the imbalance of an edge \(uv\in E(X)\) by
\[
\operatorname{imb}_X(uv)=|d_X(u)-d_X(v)|.
\]
The imbalance multiset \(M_X\) consists of these values over all edges, with multiplicity. A graph is **imbalance graphic** if \(M_X\) is the degree multiset of a finite simple graph.

### Theorem
Let \(G\) be an \(n\)-vertex graph with \(n\ge 5\), and put
\[
r=\max\{1,\delta(G)\},\qquad m=n-r-1.
\]
Then
\[
G+\overline{K_m}
\]
is imbalance graphic.

Thus the sufficient bound in Kozerenko--Serdiuk (2023, Theorem 3.7)
\[
m\ge n-\max\{1,\delta(G)\}
\]
can always be lowered by one when \(n\ge5\). In particular, their question asking whether the failure at the one-step-lower value can be reproduced for arbitrary order has a negative answer: the exhibited four-vertex example \(G=K_3\cup K_1\) is an order-four phenomenon at this boundary.

The theorem does not claim that the new bound is the smallest possible for each individual graph.

## A graphicality lemma

We use a simple consequence of the Erdős--Gallai criterion.

**Lemma.** Let
\[
D=d_1\ge d_2\ge\cdots\ge d_N\ge1
\]
be positive integers with even sum \(S\). If
\[
S\ge D(D+1),
\]
then \((d_1,\ldots,d_N)\) is graphic.

**Proof.**
For \(k>D\),
\[
\sum_{i=1}^k d_i\le kD\le k(k-1),
\]
so the \(k\)-th Erdős--Gallai inequality is immediate.

Now let \(1\le k\le D\), and write \(T=\sum_{i=1}^k d_i\). Since \(d_i\le D\),
\[
\min\{k,d_i\}\ge \frac{k}{D}d_i
\]
for every \(i>k\). Therefore
\[
k(k-1)+\sum_{i=k+1}^N\min\{k,d_i\}-T
\ge
k(k-1)+\frac{k}{D}(S-T)-T.
\]
The right-hand side is decreasing in \(T\), while \(T\le kD\). Hence it is at least
\[
k(k-1)+\frac{k}{D}(S-kD)-kD
=
k\left(\frac{S}{D}-D-1\right)\ge0.
\]
All Erdős--Gallai inequalities hold, and the parity hypothesis completes the proof. \(\square\)

## Proof of the theorem

If \(m=0\), then \(r=n-1\), so \(G=K_n\) and the conclusion is immediate. Assume \(m\ge1\), and put
\[
H=G+\overline{K_m},\qquad c=r+1=n-m.
\]
For \(v\in V(G)\) and \(a\in V(\overline{K_m})\),
\[
d_H(v)=d_G(v)+m,\qquad d_H(a)=n.
\]
Consequently,
\[
\operatorname{imb}_H(va)=|d_G(v)-c|,
\]
whereas the imbalance of an edge internal to \(G\) is unchanged.

Define
\[
A=\sum_{v\in V(G)}|d_G(v)-c|,
\qquad
J=\sum_{uv\in E(G)}|d_G(u)-d_G(v)|.
\]
The sum \(S\) of all entries of \(M_H\) is therefore
\[
S=J+mA. \tag{1}
\]

Let \(D\) be the largest positive imbalance in \(H\); if no positive imbalance exists, the result is trivial. Every cross-edge imbalance is one summand of \(A\), and for an edge \(uv\in E(G)\),
\[
|d_G(u)-d_G(v)|
\le |d_G(u)-c|+|d_G(v)-c|
\le A.
\]
Thus
\[
A\ge D. \tag{2}
\]

We next show \(D\le m\).

If \(\delta(G)\ge1\), then \(r=\delta(G)\). For an edge internal to \(G\),
\[
|d_G(u)-d_G(v)|
\le \Delta(G)-\delta(G)
\le n-1-\delta(G)=m.
\]
For a cross edge,
\[
|d_G(v)-(\delta(G)+1)|
\le \max\{1,m-1\}\le m.
\]

If \(\delta(G)=0\), then \(r=1\) and \(m=n-2\). Endpoints of an internal edge both have positive degree, so
\[
|d_G(u)-d_G(v)|\le \Delta(G)-1\le n-2=m.
\]
For a cross edge,
\[
|d_G(v)-2|\le\max\{2,n-3\}\le n-2=m,
\]
where \(n\ge5\) is used.

Combining (1) and (2),
\[
S\ge mD.
\]
If \(D\le m-1\), then
\[
S\ge mD\ge D(D+1),
\]
and the graphicality lemma applies once parity is noted.

It remains to consider \(D=m\). If some edge internal to \(G\) has imbalance \(m\), then \(J\ge m\), so
\[
S=J+mA\ge m+m^2=D(D+1).
\]
Suppose instead that no internal edge has imbalance \(m\). Then an imbalance \(m\) must occur on a cross edge.

When \(\delta(G)\ge1\), every cross imbalance is at most \(\max\{1,m-1\}\). Hence equality with \(m\) can occur only when \(m=1\). In that case \(D=1\), and \(S\) is a positive even integer, so \(S\ge2=D(D+1)\).

When \(\delta(G)=0\), we have \(m=n-2\ge3\), while every cross imbalance is at most
\[
\max\{2,n-3\}=m-1.
\]
So this final subcase cannot occur.

It remains only to justify parity. For every graph \(X\),
\[
\sum_{uv\in E(X)}|d_X(u)-d_X(v)|
\equiv
\sum_{uv\in E(X)}(d_X(u)+d_X(v))
=
\sum_{v\in V(X)}d_X(v)^2
\equiv
\sum_{v\in V(X)}d_X(v)
\equiv0\pmod 2.
\]
Thus \(S\) is even. After discarding zero entries of \(M_H\), the graphicality lemma proves that the positive part is graphic; reattaching the zero entries as isolated vertices proves that \(M_H\) itself is graphic. \(\square\)

## Relation to the 2023 question

Kozerenko and Serdiuk proved that if \(G\) has \(n\) vertices and
\[
m\ge n-\max\{1,\delta(G)\},
\]
then \(G+\overline{K_m}\) is imbalance graphic. Immediately afterward they observed that the bound fails one step lower for
\[
G=K_3\cup K_1,\qquad n=4,\qquad m=2,
\]
whose positive imbalance multiset after the join is \(\{2,2\}\), and asked whether analogous examples exist for arbitrary \(n\).

The theorem above shows that they do not: at precisely that one-step-lower value, every graph of order at least five is imbalance graphic.

## Verification

The symbolic proof is independent of computation. As a finite sanity check, `artifacts/verify.py` exhaustively scans all unlabeled graphs in the NetworkX graph atlas through seven vertices. It verifies the theorem for all 34 graphs on five vertices, 156 graphs on six vertices, and 1044 graphs on seven vertices. It also confirms that among the eleven four-vertex graphs, the known \(K_3\cup K_1\) example is the unique failure at this boundary.

For the nonzero cases, the script additionally checks the proof's sufficient inequality
\[
S\ge D(D+1).
\]
The minimum observed slack \(S-D(D+1)\) is \(0\), \(2\), and \(4\) for orders five, six, and seven respectively.

## Originality and limitations

To the best of our knowledge, the one-step improvement and the resulting negative answer to the arbitrary-order question are new. The 2023 source states the question explicitly after Theorem 3.7. Searches through current literature under the exact threshold, join-with-empty-graph terminology, imbalance graphicness, and equivalent degree-sequence language did not locate a later theorem resolving this boundary.

Two 2026 preprints prove the broader Imbalance Conjecture for graphs in which every edge has positive imbalance. That hypothesis does not cover the present join theorem in general, because \(G+\overline{K_m}\) may contain zero-imbalance edges. A separate 2026 preprint on regular blocks settles several other conjectures from the 2023 paper but does not, in the accessible statement and searchable text, address this join threshold.

Residual originality risk remains from unindexed or inaccessible work. No specific inaccessible paper was identified whose title, abstract, or visible theorem statement suggests coverage of the one-step boundary.

The finite verification is supporting evidence only. The result rests on the general Erdős--Gallai argument above.

## References

1. S. Kozerenko and A. Serdiuk, *New results on imbalance graphic graphs*, Opuscula Mathematica 43 (2023), 81--100. https://doi.org/10.7494/OpMath.2023.43.1.81
2. P. Erdős and T. Gallai, *Gráfok előírt fokszámú pontokkal*, Matematikai Lapok 11 (1960), 264--274.
3. S. Kozerenko and V. Skochko, *On graphs with graphic imbalance sequences*, Algebra and Discrete Mathematics 18 (2014), 97--108.
4. S. Kozerenko, *Edge imbalance sequences and their graphicness*, Journal of Advanced Mathematical Studies 12 (2019), 50--62.
5. J. A. Schreib and Y. Yavari, *A Proof of the Imbalance Conjecture*, arXiv:2608.09191v2 (2026). https://arxiv.org/abs/2608.09191
6. A. A. Raoui, *The Imbalance Conjecture* (2026), Zenodo DOI 10.5281/zenodo.20589431.
7. A. A. Raoui, *Regular Blocks and Imbalance Graphicness* (2026), Zenodo DOI 10.5281/zenodo.21286238.
