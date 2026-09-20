# Sharp maximum semitotal-domination gap at fixed order

Let \(G\) be a finite simple connected graph of order \(n\ge 2\). Write
\(\gamma(G)\) for its domination number and \(\gamma_{t2}(G)\) for its
semitotal domination number: a dominating set \(S\) is semitotal when every
vertex of \(S\) is at distance at most two from another vertex of \(S\).

## Theorem

For every \(n\ge 2\),
\[
\max_{\substack{G\ \mathrm{connected}\\ |V(G)|=n}}
\bigl(\gamma_{t2}(G)-\gamma(G)\bigr)
=
\max\left\{1,\left\lfloor\frac{n-2}{4}\right\rfloor\right\}.
\]
The same maximum is obtained if the maximization is restricted to trees.

Equivalently, for every connected graph with \(\gamma(G)\ge 2\),
\[
\gamma_{t2}(G)-\gamma(G)
\le
\min\left\{\gamma(G)-1,\,
\left\lfloor\frac n2\right\rfloor-\gamma(G)\right\}.
\]

For every \(n\ge 6\), an explicit extremal tree is obtained as follows. Put
\[
d=\left\lfloor\frac{n-2}{4}\right\rfloor,\qquad
s=n-(4d+2)\in\{0,1,2,3\}.
\]
Start with a vertex \(x\). Attach \(d\) internally disjoint length-four
pendant paths
\[
x-a_i-b_i-c_i-d_i\qquad (1\le i\le d)
\]
and attach \(s+1\) further leaves directly to \(x\). Denote the resulting
tree by \(B_{d,s}\). Then
\[
\gamma(B_{d,s})=d+1,\qquad
\gamma_{t2}(B_{d,s})=2d+1.
\]

**Same-model review: passed. Independent audit: not yet performed.**

## Proof

We first record two upper bounds.

If \(\gamma(G)=1\), then \(G\) has a universal vertex. A semitotal
dominating set cannot have one vertex, while a universal vertex together
with any neighbor is semitotal dominating. Hence
\[
\gamma_{t2}(G)=2,\qquad
\gamma_{t2}(G)-\gamma(G)=1.
\]

Now suppose \(\gamma(G)\ge2\). We give a short proof of
\[
\gamma_{t2}(G)\le 2\gamma(G)-1.
\]
Let \(D\) be a minimum dominating set. Form an auxiliary graph \(A\) on
vertex set \(D\), joining two members of \(D\) whenever their distance in
\(G\) is at most three. The graph \(A\) is connected: along any path in
\(G\), assign each path vertex to a member of \(D\) that dominates it;
dominators assigned to consecutive path vertices are at distance at most
three, giving a walk in \(A\).

Take a spanning tree \(F\) of \(A\). For every edge \(uv\in E(F)\) with
\(d_G(u,v)=3\), choose one internal vertex of a shortest \(u\)-\(v\) path
and add it to \(D\). Call the resulting set \(S\). It remains dominating.
Every vertex of \(D\) has an incident edge in \(F\): if that edge joins two
dominators at distance at most two, they witness each other; if its
endpoints have distance three, the added internal vertex is within distance
two of both. Every added vertex is itself within distance at most two of an
endpoint in \(D\). Thus \(S\) is semitotal dominating, and at most one
vertex was added for each of the \(\gamma(G)-1\) edges of \(F\). Therefore
\[
\gamma_{t2}(G)\le2\gamma(G)-1.
\]

Goddard, Henning and McPillan proved that every connected graph of order
\(n\ge4\) satisfies
\[
\gamma_{t2}(G)\le \frac n2.
\]
Consequently, writing
\(q=\gamma_{t2}(G)-\gamma(G)\), when \(\gamma(G)\ge2\) we have
\[
q\le\gamma(G)-1,\qquad
q\le\frac n2-\gamma(G).
\]
Adding these inequalities gives
\[
2q\le\frac n2-1,
\]
and hence
\[
q\le\left\lfloor\frac{n-2}{4}\right\rfloor.
\]
The displayed parameter-sensitive bound follows as well, using the
integrality of \(\gamma_{t2}(G)\).

For \(n=4,5\), the preceding argument shows that graphs with
\(\gamma(G)\ge2\) have gap zero, while a star has gap one. The connected
graphs of orders two and three are checked directly, and a star again has
gap one. This proves the required upper bound for every \(n\ge2\).

It remains to prove sharpness. For \(2\le n\le5\), the star \(K_{1,n-1}\)
has domination number one and semitotal domination number two.

Let \(n\ge6\), and consider \(B_{d,s}\) above. Its order is
\[
1+4d+(s+1)=4d+s+2=n.
\]
The set
\[
\{x,c_1,\ldots,c_d\}
\]
dominates the tree, so \(\gamma(B_{d,s})\le d+1\). Conversely, the terminal
leaf \(d_i\) on each long arm forces every dominating set to contain at
least one of \(c_i,d_i\), and any leaf adjacent directly to \(x\) forces at
least one selected vertex from the disjoint set consisting of \(x\) and
those direct leaves. Thus \(\gamma(B_{d,s})\ge d+1\), proving equality.

Next,
\[
S=\{x\}\cup\{b_i,c_i:1\le i\le d\}
\]
is semitotal dominating. The pair \(b_i,c_i\) witnesses itself on each
arm, and \(x\) is at distance two from every \(b_i\), so
\(\gamma_{t2}(B_{d,s})\le2d+1\).

For the reverse inequality, fix any semitotal dominating set \(R\). On
each long arm, domination of the terminal leaf \(d_i\) forces
\(c_i\in R\) or \(d_i\in R\). If \(c_i\in R\), then its semitotal witness
must lie among \(a_i,b_i,d_i\), all within that arm. If
\(d_i\in R\) while \(c_i\notin R\), its witness must be \(b_i\).
Hence every long arm contributes at least two vertices of \(R\). In
addition, a direct leaf at \(x\) can be dominated only by itself or by
\(x\), so \(R\) contains at least one vertex from the set consisting of
\(x\) and its direct leaves. These sets are disjoint from the long-arm
interiors, and therefore
\[
|R|\ge2d+1.
\]
Thus \(\gamma_{t2}(B_{d,s})=2d+1\), and
\[
\gamma_{t2}(B_{d,s})-\gamma(B_{d,s})=d
=\left\lfloor\frac{n-2}{4}\right\rfloor.
\]
Since every \(B_{d,s}\) is a tree, sharpness holds simultaneously for
trees and for all connected graphs.

## Context and originality

Goddard, Henning and McPillan introduced semitotal domination and proved
the order bound \(\gamma_{t2}(G)\le n/2\) for connected graphs of order at
least four. Their paper also records a comparison with ordinary domination.
Zhuang later proved and characterized the tree equality case
\(\gamma_{t2}(T)=2\gamma(T)-1\) for non-star trees. Chen and Xu subsequently
characterized all graphs with \(\gamma_{t2}(G)=n/2\).

The checked sources and exact/synonymous searches did not locate the
fixed-order extremal difference
\(\max(\gamma_{t2}-\gamma)\), the formula above, or the all-order extremal
tree family \(B_{d,s}\). The upper bound is a short optimization of known
order/ratio bounds; the substantive addition is the exact fixed-order
extremum together with sharp constructions for every order. Originality is
therefore claimed only to the best of our knowledge.

## Verification

`artifacts/verify_semitotal_gap.py` independently computes domination and
semitotal domination numbers by exhaustive subset search. With NetworkX
3.6.1 it checks all connected Graph Atlas graphs of orders \(2\) through
\(7\), all nonisomorphic trees through order \(10\), and the explicit
extremal family for orders \(6\) through \(20\). The recorded output is in
`artifacts/expected_output.txt`.

## Limitations

- No classification of all extremal graphs is claimed.
- The exact fixed-order upper bound is obtained by combining established
  inequalities; an equivalent corollary may exist in literature using
  different terminology even though none was located in the checked search.
- The result concerns finite simple connected graphs. Disconnected graphs
  and variants of semitotal domination are not treated.

## References

1. W. Goddard, M. A. Henning, C. A. McPillan, *Semitotal Domination in
   Graphs*, Utilitas Mathematica 94 (2014), 67--81.
   https://people.computing.clemson.edu/~goddard/papers/SemiTDomUtilitas.pdf
2. W. Zhuang, *Semitotal domination versus domination and total domination
   in trees*, RAIRO Operations Research 58 (2024), 1249--1256.
   https://doi.org/10.1051/ro/2024037
3. Q. Chen, Y. Xu, *Graphs with semitotal domination number half their
   order*, Bulletin of the Australian Mathematical Society 111 (2025),
   197--204. https://doi.org/10.1017/S0004972724000509
4. Z. Wei, G. Hao, *Semitotal domination in trees*, Discrete Mathematics
   & Theoretical Computer Science 20(2) (2018).
   https://doi.org/10.23638/DMTCS-20-2-5
