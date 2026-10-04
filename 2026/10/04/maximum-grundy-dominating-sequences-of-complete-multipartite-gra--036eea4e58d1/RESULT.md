# Maximum Grundy dominating sequences of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\). Put \(N=\sum_i n_i\), \(m=\max_i n_i\), and let \(t\) be the number of parts of size \(m\). Then \(\gamma_{\mathrm{gr}}(G)=m\). More strongly, every Grundy dominating sequence of length \(m\) has exactly one of the following forms:

1. an arbitrary ordering of all vertices of a part of size \(m\); or
2. when \(m\ge 2\), an arbitrary ordering of \(m-1\) vertices of a part of size \(m\), followed by one vertex outside that part.

Hence the number \(A(G)\) of maximum Grundy dominating sequences is
\[
A(G)=
\begin{cases}
N, & m=1,\\
t\,m!\,(N-m+1), & m\ge 2.
\end{cases}
\]
If \(B(G)\) denotes the number of distinct underlying Grundy dominating sets, then
\[
B(G)=
\begin{cases}
N, & m=1,\\
\binom{N}{2}-\binom{s}{2}, & m=2,\\
t\bigl(1+m(N-m)\bigr), & m\ge 3,
\end{cases}
\]
where \(s\) is the number of singleton parts when \(m=2\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A legal closed-neighborhood sequence \((v_1,\ldots,v_k)\) requires
\[
N[v_i]\setminus \bigcup_{j<i}N[v_j]\ne\varnothing
\]
for every \(i\). A Grundy dominating sequence is a legal dominating sequence of maximum length. The result concerns connected complete multipartite graphs, including complete graphs as the case \(m=1\).

## Proof
Let \(S=(v_1,\ldots,v_k)\) be any legal sequence in \(G\), and let \(P\) be the multipartite part containing \(v_1\). The first vertex \(v_1\) dominates every vertex outside \(P\) and also itself. As long as later selected vertices remain in \(P\), each such vertex can newly dominate only itself, so vertices of \(P\) may be appended one at a time.

Suppose a first vertex \(w\notin P\) is selected after exactly \(q\ge 1\) vertices from \(P\). Every vertex outside \(P\) was already dominated by \(v_1\). The closed neighborhood of \(w\) contains all of \(P\), so \(w\) is legal exactly when some vertex of \(P\) is still undominated; when it is legal, it dominates all remaining vertices of \(P\) at once. At that point every vertex of \(G\) is dominated, so no further legal choice is possible. Consequently every legal sequence either stays entirely inside its first part or consists of \(q<|P|\) vertices of its first part followed by one vertex outside it. In particular its length is at most \(|P|\le m\).

Conversely, listing all vertices of a part of size \(m\) is legal: the first vertex dominates all other parts, and each subsequent vertex footprints itself. Therefore \(\gamma_{\mathrm{gr}}(G)=m\). Equality in the preceding upper-bound argument forces either all \(m\) vertices of a largest part, or \(m-1\) vertices of a largest part followed by one outside vertex, proving the structural classification.

For the sequence count, each largest part contributes \(m!\) orderings of type 1. For \(m\ge2\), type 2 contributes \(m\) choices for the omitted vertex, \((m-1)!\) orders of the retained vertices, and \(N-m\) choices for the final outside vertex, namely \(m!(N-m)\) sequences per largest part. This gives the formula for \(A(G)\).

For underlying sets, when \(m\ge3\) a mixed maximum set contains \(m-1\ge2\) vertices from a unique largest part, so no double counting occurs; this gives \(t\bigl(1+m(N-m)\bigr)\). When \(m=2\), a maximum two-set is either an entire 2-vertex part or a cross-part pair with at least one endpoint in a 2-vertex part. Equivalently it is any unordered vertex pair except a pair of singleton-part vertices, giving \(\binom N2-\binom s2\). The case \(m=1\) is immediate.

## Verification
A standalone exact checker exhaustively generated every complete multipartite graph with two to four parts, each part of size one to three, and total order at most eight. For all 85 parameter tuples it independently computed the longest legal sequences by dynamic programming and checked the structural classification and both counting formulas. The replay prints `VERIFY_OK cases=85`.

## Relationship to prior work
Brešar et al. introduced the Grundy domination framework and studied exact values and graph products; their 2016 preprint gives the closed-neighborhood definition used here and records earlier exact algorithms for several graph classes. The present statement is not a product formula: it classifies every maximum sequence and counts both ordered maximum sequences and their underlying extremal sets for the complete multipartite class.

A 2026 paper by Brešar and Dravec studies uniqueness of Grundy dominating sets. It proves that no nontrivial connected graph has a unique Grundy dominating set and that complete graphs are the only connected iso-unique Grundy domination graphs. The formulas above refine that qualitative viewpoint on one canonical graph class by giving the full maximum-set and maximum-sequence counts.

## Limitations
The proof is specific to ordinary closed-neighborhood Grundy domination on complete multipartite graphs. It does not claim analogous formulas for Grundy total, Z-, L-, hop, or locating variants. Literature searches did not locate a prior statement of these exact enumeration formulas, but negative search evidence is not a proof of novelty; an unindexed or differently phrased source could still exist.

## References
1. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, B. Patkós, Z. Tuza, and M. Vizer, “Dominating sequences in grid-like and toroidal graphs,” arXiv:1607.00248, first posted 2016-07-01; later Electronic Journal of Combinatorics 23(4), P4.34 (2016).
2. B. Brešar and T. Dravec, “Graphs with unique Grundy dominating sets,” Computational and Applied Mathematics 45, 444 (2026), DOI: 10.1007/s40314-026-03835-w.
3. B. Brešar, T. Gologranc, M. Milanič, D. F. Rall, and R. Rizzi, “Dominating sequences in graphs,” Discrete Mathematics 336 (2014), 22–36, DOI: 10.1016/j.disc.2014.07.016.
