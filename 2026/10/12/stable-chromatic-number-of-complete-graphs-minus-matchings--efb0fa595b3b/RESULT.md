# Stable chromatic number of complete graphs minus matchings

## Finding

For every integer \(n\ge 1\) and \(0\le r\le\lfloor n/2\rfloor\), let \(M_r\) be any matching of \(r\) edges in the complete graph \(K_n\). The stable chromatic number, in the sense of Koana–Oh–Yoneda, satisfies

\[
\chi_{\mathrm{stable}}(K_n-M_r)=
\begin{cases}
n,&r=0,\\
n-1,&r\ge1.
\end{cases}
\]

The ordinary chromatic number of \(K_n-M_r\) is \(n-r\). Thus whenever \(r\ge1\), its stable-to-ordinary chromatic gap is exactly \(r-1\). For the cocktail-party graph \(K_{2r}-M_r\), this gap is unbounded as \(r\) grows, although only a matching of edges is missing from a complete graph.

## Assumptions and scope

Graphs are finite, simple, undirected and have labeled vertices. A matching is a set of pairwise vertex-disjoint edges. A proper \(q\)-coloring is a map \(c:V(G)\to[q]\) taking distinct values on adjacent vertices. Each vertex \(v\) strictly ranks the \(q\) colors; we write \(a\succ_v b\) when it prefers \(a\) to \(b\). The envy digraph has an arc \(v\to w\) precisely when \(vw\in E(G)\) and \(c(w)\succ_v c(v)\). A coloring is stable if the envy digraph has no directed cycle, including a directed two-cycle. The stable chromatic number is the smallest \(q\) for which every strict preference profile has some stable proper \(q\)-coloring. As in the source definition, preference profiles can be extended to rankings of all positive integers; only their restriction to the chosen finite palette matters.

When \(r=0\), the graph is complete. When \(r\ge1\), its only nonadjacent distinct vertex pairs are the edges of \(M_r\). No regularity of the matching or parity of \(n\) is assumed.

## Proof

**Upper bound.** Fix \(r\ge1\), and write one deleted pair as \(\{u,v\}\). Put \(u,v\) first in a linear ordering of the vertices, followed by all remaining vertices in any order. Orient every present edge from its earlier endpoint to its later endpoint. This orientation is acyclic. The only vertex preceding \(v\) is \(u\), and \(uv\) is absent, so no directed path starting at another vertex can reach \(v\); similarly no vertex except \(u\) reaches \(u\). Every vertex consequently reaches at most \(n-1\) vertices including itself.

For completeness, the following preferred-available-color algorithm proves the needed reachability bound for stable coloring. In reverse order, assign to each vertex its most preferred color in \([n-1]\) that is not used by any other vertex reachable from it in the orientation. There are at most \(n-2\) such other vertices, so a color always remains. Since every out-neighbor is reachable, the coloring is proper. For an oriented edge \(x\to y\), suppose that \(y\) preferred \(c(x)\) to \(c(y)\). When \(y\) chose its color, the more preferred color \(c(x)\) would have been unavailable; hence some vertex \(z\) reachable from \(y\) already carried \(c(z)=c(x)\). Then \(z\) is reachable from \(x\), contrary to the selection of \(c(x)\). Thus no envy arc runs opposite the acyclic orientation, and the coloring is stable. This gives \(\chi_{\mathrm{stable}}(K_n-M_r)\le n-1\).

**Lower bound.** For \(r=1\), \(K_n-M_1\) has a clique of order \(n-1\), so properness alone proves the lower bound. Assume \(r\ge2\); in particular \(n\ge4\). Set \(q=n-2\). For each deleted edge \(u_iv_i\in M_r\), make the first endpoint rank \(1\succ2\succ\cdots\succ q\) and the second rank \(q\succ(q-1)\succ\cdots\succ1\). Give the remaining vertices arbitrary strict preferences. Extend every ranking beyond \([q]\) in any way.

Consider any proper \(q\)-coloring. Every color class has size one or two, since the only possible same-color pairs are missing edges, and no three vertices are pairwise nonadjacent. If \(t\le q=n-2\) colors are used, the number of two-vertex classes is \(n-t\ge2\). Choose two of these doubled classes: the vertices of missing pair \(u_iv_i\) both carry color \(a\), and those of another missing pair \(u_jv_j\) both carry distinct color \(b\). Within the first pair, one endpoint prefers \(b\) to \(a\); within the second, one endpoint prefers \(a\) to \(b\), by the reverse rankings. These two selected endpoints are adjacent because they belong to different missing pairs. They mutually envy each other, producing a directed two-cycle. Hence no proper \(q\)-coloring is stable for this preference profile. This proves \(\chi_{\mathrm{stable}}(K_n-M_r)\ge n-1\).

Finally, \(K_n\) requires \(n\) distinct colors. Applying the same reverse-orientation preferred-available-color construction to a total ordering of \(K_n\), now with \(n\) available colors, provides a stable coloring for every profile. Therefore \(\chi_{\mathrm{stable}}(K_n)=n\).

For ordinary coloring, at most one color may be saved for each of the \(r\) missing pairs, and assigning a common color to each pair realizes all \(r\) savings. Thus \(\chi(K_n-M_r)=n-r\), as claimed.

## Verification

The complete argument above applies to every admissible integer \(n,r\) and every preference profile; the finite checks are not used to extrapolate an infinite assertion. The standalone `verify.py` script enumerates every proper \((n-2)\)-coloring for nine nontrivial graph profiles with \(4\le n\le8\) and \(2\le r\le\lfloor n/2\rfloor\): all 11,888 colorings have a directed blocking two-cycle under the stated reverse-pair preferences. The same script independently constructs a stable \((n-1)\)-coloring for 3,000 reproducible pseudorandom preference profiles covering \(2\le n\le11\) and \(1\le r\le\lfloor n/2\rfloor\). It checks properness and absence of envy arcs against the chosen acyclic orientation. Run `python3 verify.py` with Python 3 standard library. The file `verification_output.txt` contains the actual result of the included program.

## Relationship to prior work

Koana, Oh and Yoneda introduced the stable chromatic number for graph coloring with preference-driven envy cycles and proved a general reachability upper bound. Their exact-family results include paths, cycles, and complete bipartite graphs. In particular, their complete-bipartite theorem already determines the four-vertex case \(K_4-M_2\cong K_{2,2}\); that instance is not asserted to be new here. The current result determines every matching-deletion graph, including all larger cocktail-party graphs and graphs with unmatched vertices, by combining a sharp near-complete orientation with an explicit adversarial ranking profile.

The known reachability theorem supplies the upper-bound principle, while the published exact complete-bipartite formula does not supply the lower-bound obstruction for arbitrary disjoint deleted edges. Results about different coloring notions or acyclic-signature invariants of the same graphs are not equivalent to the stable chromatic number. The exact family classification has not been identified in the inspected principal source and targeted literature searches; this does not rule out unindexed equivalent work.

## Limitations

The result is restricted to deleting a matching from a complete graph. It does not classify arbitrary complete multipartite graphs with parts of size at least three, arbitrary near-complete graphs, or individual preference profiles. The verification program covers finitely many parameters and preference profiles only; the unrestricted statement is proved by the explicit combinatorial argument. Literature searches are not a proof of global novelty, and independent audit has not been performed.

## References

1. Tomohiro Koana, Yeeseok Oh, Hirotaka Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1, first posted 2026-09-01, especially Sections 2, 3.1, 3.3 and 3.4. https://arxiv.org/abs/2609.00569
2. The complete-graph-minus-matching family is also known, in the perfect-matching case, as the cocktail-party graph or cross-polytope graph. This is terminology, not a separate claim of novelty.
