# Exact VC dimension of inclusion-minimal edge covers of complete bipartite graphs

## Finding
For all integers \(a,b\ge 1\), let \(K_{a,b}\) have labeled bipartition \(A=\{0,\ldots,a-1\}\), \(B=\{0,\ldots,b-1\}\). A **minimal edge cover** is a subset of edges meeting every vertex, none of whose proper subsets meets every vertex. Let \(\mathcal C_{a,b}\) be the family of these covers, regarded as Boolean concepts on the \(ab\) edges. Then
\[
\operatorname{VCdim}(\mathcal C_{a,b})=
\begin{cases}
0,&\min\{a,b\}=1,\\
a+b-3,&a,b\ge2.
\end{cases}
\]
In particular, for both parts of size at least two, the largest shattered query support has **one fewer edge than the maximum size of a minimal edge cover**. An explicit three-star support realizes every Boolean labeling when both parts have size at least three.

## Assumptions and scope
The graph is the complete simple bipartite graph. The concept domain consists of **edges** (not vertices), and concepts are inclusion-minimal edge covers rather than minimum-cardinality edge covers or arbitrary edge covers. A support \(S\subseteq E(K_{a,b})\) is shattered when, for every \(T\subseteq S\), some \(M\in\mathcal C_{a,b}\) satisfies \(M\cap S=T\). All integers \(a,b\ge1\) are covered; there is no asymptotic or generic-position hypothesis.

## Proof
**Lemma 1 (structure and size).** An edge cover \(M\) is inclusion-minimal if and only if every edge \(xy\in M\) has an endpoint of degree one in the spanning subgraph \((V,M)\). Indeed, removing \(xy\) fails to cover a vertex exactly when one endpoint has degree one. Therefore every component of \((V,M)\) is a nontrivial star: if a vertex has degree at least two, all its neighbors must have degree one. If \(c\) is the number of components, then \(|M|=a+b-c\). When \(a,b\ge2\), there cannot be just one star because both bipartition classes have at least two vertices. Hence \(|M|\le a+b-2\). These structural facts are also established in the literature cited below.

**Lemma 2 (upper bound).** Suppose \(a,b\ge2\). No support of size \(a+b-2\) is shattered. Otherwise its all-one trace forces a minimal cover \(M\) with \(|M|=a+b-2\), so the support is precisely \(M\). Lemma 1 forces exactly two star components.

If \(a,b\ge3\), the two star centers lie in opposite bipartition classes (otherwise every vertex of the class of centers must itself be a center, forcing that class to have size two). Each star then has at least two leaves. Select an edge \(xy\) from the star centered at \(x\), with leaf \(y\). To realize the trace \(M\setminus\{xy\}\) on the support \(M\), any replacement cover must retain every other edge of \(M\), omit \(xy\), and cover \(y\) by connecting it to a vertex \(z\) in the opposite star. Such a \(z\) is a leaf in that opposite star, so its degree becomes at least two; the opposite star's center already has degree at least two. The retained edge from \(z\) to that center is therefore redundant, contradicting minimality. (Here the two center degrees are respectively \(b-1\) and \(a-1\).)

If \(a=2\), a two-component minimal cover assigns each right-side vertex to exactly one of the two left-side vertices, and each left-side vertex receives at least one. Write the right-side partition as nonempty \(P\sqcup Q\), with original edges \(\{(0,j):j\in P\}\) and \(\{(1,j):j\in Q\}\). The trace retaining all the first group and omitting all the second group cannot occur: every \(j\in Q\) must then be covered through \((0,j)\), making vertex \(0\) have degree \(b\ge2\). Yet vertex \(1\) must still be covered, and every permitted edge incident with it ends at some \(j\in P\), making \(j\) have degree at least two and rendering the retained edge \((0,j)\) redundant. The case \(b=2\) is symmetric. Thus the dimension is at most \(a+b-3\).

**Lemma 3 (lower bound when \(a=2\) or \(b=2\)).** Suppose \(a=2\), \(b\ge2\). Choose the support \(H=\{(0,j):1\le j<b\}\), which has size \(b-1=a+b-3\). For an arbitrary \(T\subseteq H\), assign each \(j\ge1\) to vertex \(0\) when \((0,j)\in T\), otherwise to vertex \(1\). Assign the remaining right-side vertex \(j=0\) to left-side vertex \(1\) if \(T\ne\varnothing\), and to vertex \(0\) if \(T=\varnothing\). Both left vertices are incident to at least one assigned edge, all right vertices have degree one, so the resulting edge set is a minimal cover with trace \(T\). The case \(b=2\) is symmetric.

**Lemma 4 (lower bound when \(a,b\ge3\)).** Define the following three-component star forest as the support:
\[
H=\{(0,j):2\le j<b\}\ \cup\
  \{(i,0):2\le i<a\}\ \cup\ \{(1,1)\}.
\]
It has cardinality \(a+b-3\). We construct a minimal edge cover with intersection \(T\) with \(H\) for an arbitrary \(T\subseteq H\).

Write \(I=\{i\in\{2,\ldots,a-1\}:(i,0)\in T\}\), \(J=\{j\in\{2,\ldots,b-1\}:(0,j)\in T\}\); let \(I^c\) and \(J^c\) denote complements in the respective displayed index sets. Begin with all edges of \(T\).

*Case \((1,1)\notin T\).* Add every \((i,1)\) for \(i\in I^c\) and every \((1,j)\) for \(j\in J^c\). Add \((0,1)\) if and only if \(J=\varnothing\) or \(I^c=\varnothing\); add \((1,0)\) if and only if \(I=\varnothing\) or \(J^c=\varnothing\). These additions cover vertices \(0,1\) on both sides, as needed. Every selected edge has a degree-one endpoint. To see this explicitly, if \((0,1)\) is added while \(J\ne\varnothing\), then \(I^c=\varnothing\), so right vertex \(1\) has degree one; otherwise left vertex \(0\) has degree one. The symmetric check works for \((1,0)\); the remaining edges meet degree-one outer vertices. Consequently the constructed edge set is minimal and its trace on \(H\) is exactly \(T\).

*Case \((1,1)\in T\).* If \(J^c\ne\varnothing\) and \(I^c\ne\varnothing\), choose \(j_*\in J^c\), add every \((i,j_*)\) for \(i\in I^c\), and add every \((1,j)\) for \(j\in J^c\setminus\{j_*\}\). If \(J^c\ne\varnothing\) but \(I^c=\varnothing\), add \((1,j)\) for all \(j\in J^c\). If \(J^c=\varnothing\), add \((i,1)\) for all \(i\in I^c\). Finally add \((0,0)\) if and only if \(I=\varnothing\) or \(J=\varnothing\). All vertices are covered. Every selected edge again has a degree-one endpoint: when \((0,0)\) is added, at least one endpoint is otherwise unused; if \(I^c,J^c\) are both nonempty, vertex \(j_*\) is the center of a star with leaves \(i\in I^c\), while vertex \(1\) is a leaf of the edge \((1,1)\) unless it also connects to one or more degree-one right-side vertices. All other edges meet an outer degree-one vertex. No added edge belongs to \(H\). Thus the cover is minimal with trace \(T\).

The construction realizes every one of the \(2^{a+b-3}\) traces, proving the lower bound.

**Conclusion.** Lemmas 2–4 establish the stated equality for \(a,b\ge2\). If one part has size one, the unique possible edge cover is the entire star, so the concept class is a singleton and its VC dimension is zero.

## Verification
`verify_minimal_edge_covers.py` independently enumerates the minimal covers for ten small parameter pairs and computes their entire edge-support VC dimension; it also computes their exact Littlestone dimensions for comparison without claiming an infinite-family Littlestone formula. In a separate test, it constructs witnesses for all \(7{,}688\) traces across \(3\le a,b\le7\), checking full vertex coverage, edge essentiality, and exact support traces. Execute `python3 verify_minimal_edge_covers.py` with Python 3.9 or later. Expected terminal line: `ALL_MINIMAL_EDGE_COVER_SHATTERING_CHECKS_PASS`. Finite computation supplements but does not establish the universal quantifiers in the proof.

## Relationship to prior work
Kunjwal (2018 preprint; 2020 journal) establishes the characterization of minimal edge covers of complete bipartite graphs as star forests and the extremal edge count (Theorem 7), including explicit small-graph counts. Khoshkhah, Khosravian Ghadikolaei, Monnot and Sikora (2018 preprint) use the same star-forest characterization for upper-edge-cover optimization and study complexity and approximation, including bipartite graphs. Neither inspected source states a VC-dimension formula for the **edge-incidence concept class** of all minimal covers. The contribution here is the sharp shattering upper obstruction and the explicit all-traces lower construction; the star-forest equivalence and count bound themselves are previously known.

## Limitations
The theorem is specific to complete bipartite graphs and to inclusion-minimal, not minimum-cardinality, edge covers. It gives no general exact Littlestone dimension, a classification of all shattered supports, or VC dimension for arbitrary bipartite graphs. The literature comparison was bounded and does not certify global historical priority; further sources using alternate terminology such as “spanning star forest” or “nonblocker” could overlap. No independent scientific audit was conducted.

## References
1. R. Kunjwal, *Hypergraph framework for irreducible noncontextuality inequalities from logical proofs of the Kochen-Specker theorem*, arXiv:1805.02083, originally posted 2018-05-05, Theorem 7. https://arxiv.org/abs/1805.02083
2. K. Khoshkhah, M. Khosravian Ghadikolaei, J. Monnot and F. Sikora, *Weighted Upper Edge Cover: Complexity and Approximability*, arXiv:1811.02599, originally posted 2018-11-06, Sections 1–3. https://arxiv.org/abs/1811.02599
