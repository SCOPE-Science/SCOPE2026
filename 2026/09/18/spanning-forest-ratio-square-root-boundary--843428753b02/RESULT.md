# A square-root boundary layer for the consecutive spanning-forest ratio conjecture

Let \(F_s(G)\) denote the number of spanning forests of a connected \(n\)-vertex simple graph \(G\) with exactly \(s\) connected components. Equivalently, put
\[
f_k(G):=F_{n-k}(G),
\]
so \(f_k(G)\) is the number of \(k\)-edge spanning forests.

Bencs and Csikvári conjectured that for every connected simple \(n\)-vertex graph and every \(2\le s\le n\),
\[
\frac{F_s(G)}{F_{s-1}(G)}\ge
\frac{F_s(K_n)}{F_{s-1}(K_n)},
\]
with equality only for \(G=K_n\).

## Main theorem

**Theorem 1 (square-root boundary layer).**
Let \(k\ge2\), let \(G\) be a connected simple graph on \(n\) vertices, and suppose
\[
n\ge 3k^2.
\]
Then
\[
\boxed{\frac{f_k(G)}{f_{k+1}(G)}\ge
\frac{f_k(K_n)}{f_{k+1}(K_n)}}
\]
and equality holds if and only if \(G=K_n\).

Thus the conjecture holds throughout the growing range
\[
0\le n-s\le \sqrt{n/3}
\]
(up to the trivial top ranks \(n-s=0,1\), which also satisfy the conjecture).

The constant \(3\) is not optimized.

## A first nontrivial fixed boundary rank

**Theorem 2.**
For every admissible \(n\), the conjecture holds for
\[
n-s\le3.
\]
In particular, for every connected simple graph on \(n\ge5\) vertices,
\[
\boxed{\frac{F_{n-3}(G)}{F_{n-4}(G)}\ge
\frac{F_{n-3}(K_n)}{F_{n-4}(K_n)}},
\]
with equality if and only if \(G=K_n\).

The cases \(n-s=0,1\) are immediate, while \(n-s=2\) follows from the same extension argument below. The case \(n-s=3\) is the first one in which four-edge forests, triangles and 4-cycles can affect the denominator.

## Extension deficit in the complete graph

Write
\[
M=\binom n2,\qquad A_k=f_k(K_n).
\]
For a \(k\)-edge forest \(H\subseteq K_n\), let its nontrivial tree components contain
\(e_1,e_2,\ldots\) edges and define
\[
q(H):=\sum_i\binom{e_i}2.
\]
An unchosen edge of \(K_n\) can be added to \(H\) unless its endpoints already lie in the same component. A tree component with \(e_i\) edges has \(e_i+1\) vertices, so the number of unchosen internal edges in that component is
\[
\binom{e_i+1}2-e_i=\binom{e_i}2.
\]
Hence \(H\) has exactly
\[
M-k-q(H)
\]
one-edge extensions that remain forests.

Let
\[
\bar q_k=\frac1{A_k}\sum_{H\in\mathcal F_k(K_n)}q(H),
\]
where \(\mathcal F_k(K_n)\) is the set of \(k\)-edge forests of \(K_n\). Double-counting inclusions between \(k\)- and \((k+1)\)-edge forests gives
\[
(k+1)A_{k+1}=A_k\bigl(M-k-\bar q_k\bigr),
\]
and therefore
\[
\frac{A_k}{A_{k+1}}
=\frac{k+1}{M-k-\bar q_k}. \tag{1}
\]

For an arbitrary connected \(G\) with \(m\) edges, every \(k\)-edge forest has at most \(m-k\) valid one-edge extensions. Thus
\[
(k+1)f_{k+1}(G)\le (m-k)f_k(G),
\]
so
\[
\frac{f_k(G)}{f_{k+1}(G)}\ge\frac{k+1}{m-k}. \tag{2}
\]
If \(G\ne K_n\), then \(m\le M-1\). Consequently, (1) and (2) show that it is enough to prove
\[
\bar q_k<1. \tag{3}
\]

## Bounding the complete-graph extension deficit

Consider the line graph \(L(K_n)\). It has
\[
N=M=\binom n2
\]
vertices and maximum degree
\[
D=2(n-2).
\]
For any \(k\)-edge subset \(S\subseteq E(K_n)\), let \(Q(S)\) be the number of unordered pairs of edges of \(S\) lying in the same connected component. For forests, \(Q(H)=q(H)\).

If two selected edges lie in the same component, their corresponding vertices in \(L(K_n)[S]\) are joined by a simple path. The number of undirected simple paths of length \(\ell\) in \(L(K_n)\) is at most \(ND^\ell/2\). Therefore, averaging over all \(k\)-subsets of \(E(K_n)\),
\[
\mathbb E_S Q(S)
\le
\sum_{\ell\ge1}
\frac{ND^\ell}2
\frac{\binom{N-\ell-1}{k-\ell-1}}{\binom Nk}.
\]
Put
\[
x=\frac{D(k-1)}{N-1}.
\]
Since
\[
\frac{\binom{N-\ell-1}{k-\ell-1}}{\binom Nk}
=\frac{(k)_{\ell+1}}{(N)_{\ell+1}},
\]
the preceding display yields, whenever \(x<1\),
\[
\mathbb E_S Q(S)
\le \frac{k}{2}\sum_{\ell\ge1}x^\ell
=\frac{k}{2}\frac{x}{1-x}. \tag{4}
\]

We also need a lower bound on the proportion of \(k\)-subsets that are forests. A cyclic \(k\)-subset contains a simple cycle of some length \(\ell\ge3\). Since \(K_n\) has \((n)_\ell/(2\ell)\) cycles of length \(\ell\), a union bound gives
\[
\Pr(S\text{ is cyclic})
\le
\sum_{\ell\ge3}
\frac{(n)_\ell}{2\ell}
\frac{(k)_\ell}{(N)_\ell}
\le
\sum_{\ell\ge3}\frac{y^\ell}{2\ell},
\qquad
y:=\frac{nk}N=\frac{2k}{n-1}. \tag{5}
\]

Assume now \(n\ge3k^2\) and \(k\ge2\). Since
\[
N-1>\frac{n(n-2)}2,
\]
we have
\[
x<\frac{4(k-1)}n\le\frac{4(k-1)}{3k^2}.
\]
Substituting this into (4),
\[
\mathbb E_S Q(S)
<
\frac{2k(k-1)}{3k^2-4k+4}
<\frac34, \tag{6}
\]
because
\[
9k^2-12k+12-8k(k-1)=(k-2)^2+8>0.
\]

Moreover,
\[
y\le\frac{2k}{3k^2-1}<\frac25,
\]
so (5) gives
\[
\Pr(S\text{ is cyclic})
<
\frac{(2/5)^3}{6(1-2/5)}
=\frac4{225}<\frac1{10}.
\]
Thus more than \(9/10\) of all \(k\)-edge subsets are forests. Since the sum of \(q(H)\) over forests is at most the sum of \(Q(S)\) over all \(k\)-subsets, (6) implies
\[
\bar q_k
<
\frac{3/4}{9/10}
=\frac56<1.
\]
This proves (3), and hence Theorem 1. The inequalities are strict for every noncomplete \(G\), while equality is immediate for \(G=K_n\).

## The rank \(n-s=2\)

For \(k=2\), every two-edge subset of \(K_n\) is a forest. Here \(q(H)=1\) exactly when the two edges are adjacent, so
\[
\bar q_2=
\frac{n\binom{n-1}2}{\binom M2}
=\frac{4(n-2)}{n(n-1)-2}<1
\qquad(n\ge4).
\]
The same comparison (1)--(2) proves the conjecture for \(k=2\) for every admissible \(n\).

## The rank \(n-s=3\)

For \(k=3\),
\[
A_3=\binom M3-\binom n3.
\]
To sum \(q(H)\), fix a pair of selected edges. If they are adjacent, there are \(M-3\) choices for the third edge that keep a forest. If they are disjoint, exactly four choices for the third edge connect them into one component. There are
\[
n\binom{n-1}2
\]
adjacent edge pairs and \(3\binom n4\) disjoint edge pairs. Hence
\[
\bar q_3
=
\frac{
n\binom{n-1}2(M-3)+12\binom n4
}{
\binom M3-\binom n3
}
=
\frac{12(n+4)}{n^2+3n+4}. \tag{7}
\]
Therefore
\[
\bar q_3<2\quad(n\ge7),
\qquad
\bar q_3<1\quad(n\ge13). \tag{8}
\]

Let \(d=M-m\) be the number of missing edges of \(G\). From (1)--(2), \(d\ge\bar q_3\) is sufficient for the desired inequality, and strict inequality follows whenever \(d>\bar q_3\). Thus (8) handles all \(d\ge2\) for \(7\le n\le12\), all \(d\ge1\) for \(n\ge13\), and all \(d\ge3\) for \(n=5,6\).

If \(d=1\), write \(G=K_n-e\). Edge-transitivity of \(K_n\) gives
\[
f_j(K_n-e)=A_j\left(1-\frac jM\right),
\]
so
\[
\frac{f_3(K_n-e)}{f_4(K_n-e)}
=
\frac{A_3}{A_4}
\frac{1-3/M}{1-4/M}
>
\frac{A_3}{A_4}.
\]

It remains only to check \(n\in\{5,6\}\) with exactly two missing edges. Up to isomorphism, those two missing edges are adjacent or disjoint. Direct inclusion-exclusion gives:

| \(n\) | graph type | \(f_3\) | \(f_4\) | \(f_3/f_4\) |
|---:|---|---:|---:|---:|
| 5 | \(K_5\) | 110 | 125 | \(22/25\) |
| 5 | two adjacent edges deleted | 51 | 40 | \(51/40\) |
| 5 | two disjoint edges deleted | 52 | 45 | \(52/45\) |
| 6 | \(K_6\) | 435 | 1080 | \(29/72\) |
| 6 | two adjacent edges deleted | 273 | 561 | \(91/187\) |
| 6 | two disjoint edges deleted | 274 | 572 | \(137/286\) |

Both noncomplete types are strict in both orders. This completes the proof of Theorem 2.

## Context and limitations

Bencs and Csikvári proved the total forest/tree ratio inequality
\[
\frac{F(G)}{T(G)}\ge\frac{F(K_n)}{T(K_n)}
\]
and then proposed the stronger consecutive-component ratio inequality above as Conjecture 5.8. They further related it to a normalized-matching/LYM conjecture for the forest poset of \(K_n\).

The present result establishes a growing square-root-width boundary layer of Conjecture 5.8 and completely settles its first four top ranks \(n-s\le3\). It does not prove the conjecture for component counts deeper than this range. The constant \(3\) in \(n\ge3k^2\) is only a convenient sufficient constant and is not claimed optimal.

The source conjecture is very recent. Exact-formula and synonymous searches found no prior result establishing this square-root boundary layer or the all-\(n\) \(n-s=3\) case. Unindexed parallel work remains a residual originality risk.

## Reference

Ferenc Bencs and Péter Csikvári, *An inequality for the number of independent sets of matroids with an application to the forest-tree ratio of graphs*, arXiv:2609.18611 (2026), especially Conjectures 5.7--5.10.
