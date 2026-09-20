# Sharp lower bound for the average size of maximal matchings in cyclic graphs

## Statement

Let \(G\) be a finite simple connected graph of order \(n\), and let
\[
r=|E(G)|-|V(G)|+1
\]
be its cyclomatic number. Write \(\operatorname{avm}(G)\) for the arithmetic mean of the sizes of all maximal matchings of \(G\).

**Theorem.** If \(r\ge 2\), then
\[
\boxed{\operatorname{avm}(G)\ge 2-\frac{1}{r(n-3)+1}.}
\]
Equality holds if and only if \(n\ge r+2\) and \(G\) is obtained from the \(r\)-page book graph (\(r\) triangles sharing a common edge \(uv\)) by attaching all remaining \(n-r-2\) leaves to one endpoint of the common edge.

Consequently, for every \(r\ge2\) and every \(n\ge r+2\),
\[
\boxed{\min\{\operatorname{avm}(G): |V(G)|=n,\ |E(G)|=n-1+r,\ G\text{ connected}\}
=2-\frac{1}{r(n-3)+1},}
\]
and the extremal graph is unique up to isomorphism.

For \(r=2\), this becomes
\[
2-\frac1{2n-5}=\frac{4n-11}{2n-5},
\]
recovering the bicyclic minimum of Zhang (2026), while also including the order-4 boundary case. For \(r=3\), for example, the tricyclic minimum for every \(n\ge5\) is
\[
2-\frac1{3n-8}=\frac{6n-17}{3n-8}.
\]

## Proof

If every maximal matching of \(G\) has size at least \(2\), then
\(\operatorname{avm}(G)\ge2\), which is strictly stronger than the stated bound. Hence suppose that \(G\) has a maximal matching of size \(1\), say \(\{uv\}\).

A one-edge matching is maximal exactly when its edge dominates every edge of the graph. Thus every edge of \(G\) is incident with \(u\) or \(v\). Because \(G\) is connected, every vertex outside \(\{u,v\}\) belongs to exactly one of
\[
A=N(u)\setminus(N(v)\cup\{v\}),\qquad
B=N(v)\setminus(N(u)\cup\{u\}),\qquad
C=N(u)\cap N(v).
\]
Put \(a=|A|\), \(b=|B|\), and \(q=|C|\). Then
\[
n=2+a+b+q,
\qquad
|E(G)|=1+a+b+2q,
\]
so
\[
r=|E(G)|-|V(G)|+1=q.
\]
In particular \(|C|=r\ge2\).

The edge \(uv\) is the unique one-edge maximal matching. Indeed, for any other edge, say \(ux\), choose a common neighbor \(y\in C\) different from \(x\) if \(x\in C\) (and arbitrary if \(x\in A\)); then \(vy\) is disjoint from \(ux\). The case of an edge incident with \(v\) is symmetric.

Every matching has size at most \(2\), since every edge is incident with \(u\) or \(v\). Conversely every two-edge matching is maximal, because it covers both \(u\) and \(v\), hence dominates every edge. Such a matching is a pair \(\{ux,vy\}\) with distinct outside endpoints. Therefore the number \(t\) of two-edge maximal matchings is
\[
t=(a+r)(b+r)-r.
\]
Using \(a+b=n-r-2\), this simplifies to
\[
t=ab+r(n-3).
\]
There is exactly one one-edge maximal matching and all remaining maximal matchings have size \(2\). Hence
\[
\operatorname{avm}(G)
=\frac{1+2t}{1+t}
=2-\frac{1}{ab+r(n-3)+1}
\ge 2-\frac{1}{r(n-3)+1},
\]
since \(ab\ge0\).

Equality holds exactly when \(ab=0\). Since
\(a+b=n-r-2\), this is possible precisely in the stated equality family: after interchanging \(u\) and \(v\) if necessary, all \(n-r-2\) private neighbors are leaves at \(u\), while the \(r\) common neighbors form the \(r\) triangles sharing \(uv\). This also proves uniqueness up to isomorphism. If \(n<r+2\), no graph with a one-edge maximal matching can have cyclomatic number \(r\), so the inequality is strict. ∎

## Context and originality

Engbers and Erey introduced the fixed-family extremal study of the average size of maximal matchings and asked for extensions from trees and unicyclic graphs to \(k\)-cyclic graphs. Zhang (2026) treated the first non-unicyclic case, proving the exact bicyclic minimum
\((4n-11)/(2n-5)\) and uniquely identifying two triangles sharing an edge with all extra leaves concentrated at one endpoint. Zhang's proof explicitly uses the observation that a maximal matching of size one is a single edge dominating all edges, but the paper then analyzes the three bicyclic core types separately.

The theorem above turns that observation into a cyclomatic identity: whenever \(\operatorname{avm}(G)<2\), a dominating edge forces the cyclomatic number to equal the number of its common neighbors. This collapses the minimum problem in the full range \(n\ge r+2\) to an exact two-parameter count and extends the bicyclic extremal graph to an arbitrary book size.

Searches for the exact formula and synonymous formulations involving average maximal matching size, tricyclic/\(k\)-cyclic graphs, book graphs, dominating edges, and the line-graph independent-domination translation did not locate this all-\(r\) result. Originality is therefore claimed only to the best of our knowledge.

## Verification

A standalone finite check in `artifacts/verify.py` enumerates every connected graph in the NetworkX Graph Atlas for orders at most \(7\), computes all maximal matchings exactly, and checks every parameter pair \((n,r)\) with \(r\ge2\) and \(n\ge r+2\). In all ten parameter pairs present in the atlas, the minimum equals the theorem's formula and there is exactly one extremal isomorphism class. This computation is supporting evidence; the proof above is the general certificate.

## Limitations

The universal inequality applies to every connected graph with cyclomatic number \(r\ge2\), but the displayed fixed-\((n,r)\) minimum is asserted only for \(n\ge r+2\), where equality is attainable. The denser finite regime \(n<r+2\) generally has minimum strictly above the bound and is not classified here. The maximum side of the \(k\)-cyclic extremal problem is also not addressed.

The full text of Engbers and Erey (2023) was not inspected in this review; its bibliographic scope and the relevant extension question were checked through Zhang's 2026 paper, which quotes and attributes that question. This leaves residual originality uncertainty from that source and from differently indexed or very recent work.

## References

1. J. Engbers and A. Erey, *Extremal graphs for average sizes of maximal matchings*, Discrete Applied Mathematics 341 (2023), 308-321. DOI: https://doi.org/10.1016/j.dam.2023.08.022
2. K. Zhang, *Extremal graphs for average size of maximal matchings in bicyclic graphs*, arXiv:2604.28033 (2026). https://arxiv.org/abs/2604.28033
3. K. Zhang, *Upper bounds for the average size of maximal matchings in bicyclic graphs*, arXiv:2608.06818 (2026). https://arxiv.org/abs/2608.06818
4. A. Hertz, S. Bonte, G. Devillez, and H. Mélot, *The average size of maximal matchings in graphs*, Journal of Combinatorial Optimization 47 (2024), Article 46. DOI: https://doi.org/10.1007/s10878-024-01144-8
