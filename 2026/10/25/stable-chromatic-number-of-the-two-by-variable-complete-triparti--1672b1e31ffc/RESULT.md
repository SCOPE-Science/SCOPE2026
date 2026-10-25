# Stable chromatic number of the two-by-variable complete tripartite family

## Finding

For all integers \(2\le m\le n\), the preference-stable chromatic number of the complete tripartite graph \(K_{2,m,n}\) is
\[
\boxed{\chi_{\mathrm{stable}}(K_{2,m,n})=m+3.}
\]
In particular, the exact value for every \(m\ge4\) is not determined by the previously recorded individual examples \(K_{2,2,2}\) and \(K_{2,3,3}\). The principal mechanism is a two-part amplification of an obstruction to stable coloring: augmenting two different parts of a complete tripartite graph by the same number of vertices increases the stable chromatic number by at least that number.

## Assumptions and scope

All graphs are finite, simple, and undirected. The graph \(K_{a,b,c}\) has three nonempty independent vertex parts of respective sizes \(a,b,c\), with every edge between distinct parts. A profile assigns each vertex a strict total preference ranking of the positive integers, interpreted as named colors. A proper coloring assigns different colors to adjacent vertices. For a proper coloring \(\varphi\), its envy digraph has an arc \(u\to v\) when \(u\) and \(v\) are adjacent and \(u\) strictly prefers \(\varphi(v)\) to \(\varphi(u)\). A coloring is **stable** when this digraph is acyclic. The invariant \(\chi_{\mathrm{stable}}(G)\) is the smallest \(k\) such that every preference profile on \(G\) admits a stable proper coloring from the named palette \(\{1,\ldots,k\}\).

The theorem concerns exactly the family \(2\le m\le n\). The lower-bound obstruction is for the named palette of \(m+2\) colors; it is sufficient to disprove the existence of a stable coloring under that profile, not to analyze every possible palette. The theorem does not assert the same formula for arbitrary complete multipartite graphs or that all optimal colorings have a specified form.

## Proof

**Upper bound.** Write the graph's parts as \(C,A,B\), where \(|C|=2\), \(|A|=m\), and \(|B|=n\). Orient every edge from \(B\) towards \(A\cup C\), and every edge between \(C\) and \(A\) from \(C\) to \(A\). The orientation is acyclic. A vertex of \(B\) can reach at most itself plus the \(m+2\) vertices in \(A\cup C\); a vertex in \(C\) reaches at most itself and the \(m\) vertices of \(A\); vertices of \(A\) are sinks. Thus the maximum reachable-set size, counting its starting vertex, is \(m+3\). The preference-stable coloring reachability theorem [1, Theorem 3.1] supplies a stable proper coloring with at most \(m+3\) colors under every profile. Hence \(\chi_{\mathrm{stable}}(K_{2,m,n})\le m+3\).

**Two-part obstruction amplification.** We establish the following supporting lemma. For all positive integers \(a,b,c\) and all nonnegative integers \(q\),
\[
\chi_{\mathrm{stable}}(K_{a+q,b+q,c})\ge
\chi_{\mathrm{stable}}(K_{a,b,c})+q.
\]
Let \(s=\chi_{\mathrm{stable}}(K_{a,b,c})\). There is a preference profile on the core \(H=K_{a,b,c}\) for which no stable coloring from \(\{1,\ldots,s-1\}\) exists. (The integer-valued invariant is the maximum, over preference profiles, of the least palette size.) Put \(k=q+s-1\). Build \(K_{a+q,b+q,c}\) from \(H\) by adding vertices \(x_i\) to the first part and \(y_i\) to the second part for each \(1\le i\le q\). Call \(\{x_i,y_i\}\) level \(i\). Every vertex in a later level, and every core vertex, has a neighbor in each earlier level.

For each level-\(i\) vertex, rank the named palette in this exact order:
\[
i\succ i+1\succ\cdots\succ k\succ i-1\succ i-2\succ\cdots\succ1.
\]
For each core vertex, place all high colors \(q+1,\ldots,k\) above all low colors \(1,\ldots,q\), retaining on the high colors the selected obstructing core profile, and place the low colors in descending order. Extend these finite rankings arbitrarily to the remaining positive integers.

Suppose there were a stable proper \(k\)-coloring \(\varphi\). Induction on \(i\) shows that each vertex of level \(i\) has \(\varphi(v)\ge i\). Indeed, if \(\varphi(v)=j<i\), take a neighbor \(u\) in level \(j\). By induction \(\varphi(u)\ge j\), and properness forces \(\varphi(u)>j\). The level-\(j\) preference ranking makes \(u\) prefer color \(j\) over \(\varphi(u)\), whereas the level-\(i\) ranking makes \(v\) prefer \(\varphi(u)\) over \(j\). This creates a directed envy two-cycle. Likewise, no core vertex can receive a color \(j\le q\): it has a neighbor in level \(j\), which by the same argument creates a directed envy two-cycle. The core therefore receives only colors \(q+1,\ldots,q+s-1\). Its restricted preference profile is the shifted obstructing profile for \(H\), so its envy digraph contains a directed cycle, contradicting stability. Consequently no stable \(k\)-coloring exists, and the lemma follows. The case \(q=0\) is immediate.

**Six-vertex seed.** We show \(\chi_{\mathrm{stable}}(K_{2,2,2})\ge5\). Label its three independent pairs \(A=(a_1,a_2)\), \(B=(b_1,b_2)\), \(C=(c_1,c_2)\). The following four-color preference profile gives the six rows in that vertex order, from best to worst:

| Vertex | Preference order |
| --- | --- |
| \(a_1\) | \(1\succ2\succ3\succ4\) |
| \(a_2\) | \(2\succ3\succ4\succ1\) |
| \(b_1\) | \(2\succ3\succ4\succ1\) |
| \(b_2\) | \(4\succ1\succ2\succ3\) |
| \(c_1\) | \(2\succ3\succ4\succ1\) |
| \(c_2\) | \(4\succ1\succ2\succ3\) |

There are precisely \(96\) proper colorings with the four named colors: \(24\) use three colors (the three parts monochromatic, with different colors), and \(72\) use all four colors (exactly one part uses two distinct colors). The complete finite verification `verify.py` evaluates every such assignment. All \(24\) three-color assignments and \(68\) of the four-color assignments have an envy two-cycle. The remaining four assignments, in the displayed vertex order, are
\[
(2,2,3,1,4,4),\quad(2,2,4,4,3,1),\quad
(3,3,2,1,4,4),\quad(3,3,4,4,2,1).
\]
The first and third have the directed triangle \(a_1\to b_2\to c_1\to a_1\); the second and fourth have \(a_1\to c_2\to b_1\to a_1\). Thus there is no stable four-coloring. This is a complete finite certificate rather than inference from random testing. Independently, the triangular-prism obstruction in [1, Appendix A] gives another route to the seed: the prism is a spanning subgraph of \(K_{2,2,2}\), and the invariant is subgraph-monotone [1, Proposition 3.4]. The seed itself is therefore not claimed as new.

**Lower bound and conclusion.** Apply the amplification lemma to \(K_{2,2,2}\), increasing the two parts of size \(2\) by \(q=m-2\). Then
\[
\chi_{\mathrm{stable}}(K_{2,m,m})\ge5+(m-2)=m+3.
\]
The graph \(K_{2,m,m}\) is an induced subgraph of \(K_{2,m,n}\) whenever \(n\ge m\), and the stable chromatic number is subgraph-monotone [1, Proposition 3.4]. Hence \(\chi_{\mathrm{stable}}(K_{2,m,n})\ge m+3\). Combined with the upper bound, this proves the theorem for every \(2\le m\le n\).

## Verification

The standalone standard-library checker `verify.py` explicitly constructs the seed profile, enumerates **all** \(96\) proper four-colorings, and verifies a blocking directed two- or three-cycle for each. It independently constructs the amplified rankings, then enumerates **all** proper colorings for the balanced cases \(m=2,3,4\) with respective palettes of \(4,5,6\) colors, confirming \(96,2940,165360\) complete assignments and no stable coloring. Its output is saved in `verify_output.txt` and can be regenerated by running `python3 verify.py` with the two files in the same directory. The enumeration proves the finite seed; the inductive amplification and upper-bound orientation prove the unbounded family. Tests through \(m=4\) alone would not prove the general theorem.

## Relationship to prior work

Koana, Oh, and Yoneda [1] introduced this precise preference-stable chromatic number, proved the general reachability upper bound and subgraph monotonicity, and determined complete bipartite graphs. Their Appendix A establishes a four-color obstruction for the triangular prism; as explained above, it already implies the \(K_{2,2,2}\) seed. The same paper does not state the two-part amplification lemma or the parameter-wide exact values here (the paper's graph-family table concerns paths, cycles, and complete bipartite graphs). The published record [2] establishes \(\chi_{\mathrm{stable}}(K_{2,3,3})=6\) through a five-color obstruction. That case and its extensions to \(K_{2,3,n}\) by subgraph monotonicity and the upper bound are already covered. The present new scope is the infinite regime \(m\ge4\), including the balanced cases \(K_{2,m,m}\). The extension is not a consequence of the isolated recorded \(K_{2,3,3}\) statement; it requires the explicit obstruction-amplification argument above.

## Limitations

The proof does not classify individual stable colorings, all complete tripartite graphs, or arbitrary part-size vectors with no part of size \(2\). An equivalent amplification lemma or more general classification may exist under alternative terminology or in unindexed literature. The full content of published record [2] was not accessible in this check, although its indexed title and exact summary were available; it is not claimed that unseen portions contain no related argument. Independent mathematical audit has not been performed. The finite certificate is exhaustive for the explicitly stated seed and tested finite cases only.

## References

[1] T. Koana, Y. Oh, and H. Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1, first publicly posted September 1, 2026, §§2–3, Proposition 3.4, Theorem 3.1, Appendix A. https://arxiv.org/pdf/2609.00569v1

[2] *Stable chromatic number of the complete tripartite graph* \(K_{2,3,3}\), published research record, October 4, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-stable-chromatic-number-of-the-complete-tripartite-graph-k-2-3-3--b34a81e3d305
