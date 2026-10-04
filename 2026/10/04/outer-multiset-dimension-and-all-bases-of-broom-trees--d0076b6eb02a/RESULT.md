# Outer multiset dimension and all bases of broom trees
## Finding
For integers \(\ell\ge2\) and \(q\ge3\), let \(B_{\ell,q}\) be the tree formed from a path \(p_0p_1\cdots p_\ell\) by adjoining \(q\) new leaves \(w_1,\ldots,w_q\) to \(p_0\). Then the outer multiset dimension is \(\operatorname{dim}_{\mathrm{ms}}(B_{\ell,q})=q\). Moreover, every outer multiset basis is exactly one of the following: the full brush \(\{w_1,\ldots,w_q\}\), or a set obtained by omitting exactly one brush leaf and adding exactly one non-root handle vertex \(p_j\) with \(1\le j\le\ell\). Consequently the number of outer multiset bases is \(1+q\ell\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. For integers \(\ell\ge2\) and \(q\ge3\), define the broom tree \(B_{\ell,q}\) by starting from the path
\[
p_0p_1\cdots p_\ell
\]
and adjoining \(q\) additional leaves
\[
W=\{w_1,\ldots,w_q\}
\]
to \(p_0\).

For a set \(S\subseteq V(G)\), the multiset representation of a vertex \(v\notin S\) is the multiset of distances from \(v\) to the vertices of \(S\). The set \(S\) is outer multiset resolving when distinct vertices outside \(S\) have distinct multiset representations.

## Proof
The brush vertices \(w_1,\ldots,w_q\) are false twins. Hence every outer multiset resolving set contains at least \(q-1\) of them.

Suppose first that \(|S|=q-1\). Then the twin lower bound forces
\[
S=W\setminus\{w\}
\]
for one brush leaf \(w\). The omitted brush leaf \(w\) is at distance \(2\) from every vertex of \(S\). The handle vertex \(p_1\) is also at distance \(2\) from every vertex of \(S\). Therefore they have the same multiset representation, so no set of size \(q-1\) resolves. Thus
\[
\operatorname{dim}_{\mathrm{ms}}(B_{\ell,q})\ge q.
\]

On the other hand, the full brush \(W\) resolves every handle vertex: for \(0\le i\le\ell\),
\[
m(p_i\mid W)=\{(i+1)^q\},
\]
meaning that the value \(i+1\) occurs with multiplicity \(q\). These multisets are pairwise distinct. Hence
\[
\operatorname{dim}_{\mathrm{ms}}(B_{\ell,q})=q.
\]

It remains to classify the bases. Let \(S\) be an outer multiset basis, so \(|S|=q\). The twin condition implies that \(S\) contains either all \(q\) brush leaves, or exactly \(q-1\) brush leaves.

If all \(q\) brush leaves are in \(S\), then \(S=W\), which is a basis as shown above.

Now suppose that exactly one brush leaf \(w\) is omitted. Then
\[
S=(W\setminus\{w\})\cup\{x\}
\]
for one non-brush vertex \(x\). If \(x=p_0\), then both \(w\) and \(p_1\) have the same multiset
\[
\{1,2^{q-1}\},
\]
so this choice fails.

Take instead \(x=p_j\) with \(1\le j\le\ell\). For every unselected handle vertex \(p_i\), its representation is
\[
m(p_i\mid S)=\{(i+1)^{q-1},|i-j|\},
\]
while the omitted brush leaf has
\[
m(w\mid S)=\{2^{q-1},j+1\}.
\]
Because \(q-1\ge2\), equality of two multisets of the form \(\{a^{q-1},b\}\) forces equality of the repeated value \(a\). Therefore two distinct handle vertices cannot collide.

If the omitted brush leaf collided with a handle vertex, the repeated value would force that handle vertex to be \(p_1\). But then equality would require
\[
j+1=|j-1|,
\]
which is impossible for \(j\ge1\). Thus every choice \(p_j\), \(1\le j\le\ell\), gives a basis.

There is one basis using all brush leaves. Otherwise, choose the omitted brush leaf in \(q\) ways and the added handle vertex in \(\ell\) ways. Hence the number of bases is
\[
1+q\ell.
\]

## Verification
The included checker constructs every \(B_{\ell,q}\) for \(3\le q\le7\) and \(2\le\ell\le8\), computes all-pairs distances, enumerates every vertex subset, and tests the outer multiset resolving condition directly from sorted distance multisets.

For each parameter pair it independently checks that the minimum size is \(q\), that every minimum basis belongs to the two structural types proved above, and that the total number of bases is \(1+q\ell\).

## Relationship to prior work
The 2019 paper introducing outer multiset dimension proves the basic twin lower bound and develops exact and algorithmic results for selected graph families. Its tree section is devoted to full regular rooted trees and explicitly presents those results as a step toward understanding general trees. Targeted full-text searches of that source found no broom, caterpillar, or spider treatment.

A 2022 follow-up gives the extremal characterization \(\operatorname{dim}_{\mathrm{ms}}(G)=|V(G)|-1\), characterizes graphs of outer multiset dimension two, studies lexicographic products, and determines rectangular grids. Its full text and conclusion do not contain a broom-tree formula.

The present theorem concerns a non-regular, unbounded-diameter tree family and additionally classifies every minimum basis, not only the minimum cardinality.

## Limitations
The theorem assumes \(q\ge3\) and \(\ell\ge2\). The case \(q=2\) has extra multiset symmetries and a different basis classification, so it is intentionally excluded. No claim is made for arbitrary caterpillars or general trees. The finite verification is corroborative only; the all-parameter result follows from the proof.

## References
1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, I. G. Yero, “Distance-based vertex identification in graphs: the outer multiset dimension,” arXiv:1902.03017v1, 8 February 2019; Applied Mathematics and Computation 363 (2019), 124612.
2. S. Klavžar, D. Kuziak, I. G. Yero, “Further contributions on the outer multiset dimension of graphs,” arXiv:2207.06834v1, 14 July 2022; Results in Mathematics 78 (2023), Article 50.
