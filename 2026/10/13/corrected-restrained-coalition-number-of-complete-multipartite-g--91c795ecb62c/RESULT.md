# Corrected restrained coalition number of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), \(n_i\ge1\), and \(N=\sum_i n_i\). Put
\[
p=\lvert\{i:n_i\ge2\}\rvert,\qquad u=\lvert\{i:n_i=1\}\rvert.
\]
Under the standard convention that singleton partite classes are allowed,
\[
\operatorname{RDc}(G)=
\begin{cases}
N,&p\ne1,\\
2,&p=1\text{ and }u=1,\\
u+2,&p=1\text{ and }u\ge2.
\end{cases}
\]
Here \(\operatorname{RDc}(G)\) is the maximum order of a restrained domination coalition partition. In particular,
\[
\operatorname{RDc}(K_{3,1,1})=4<5,
\]
so the unrestricted complete-multipartite statement in Proposition 2.17 of Nesam--Amutha--Anbazhagan (2025) needs a boundary correction when singleton partite classes occur.

## Assumptions and scope
Graphs are finite, simple, and connected. A restrained dominating set \(D\) is a dominating set such that every vertex in \(V(G)\setminus D\) has a neighbor in \(V(G)\setminus D\). Two disjoint non-restrained-dominating sets form a restrained domination coalition when their union is restrained dominating. A restrained domination coalition partition is a vertex partition in which every non-restrained-dominating block has such a partner and every block that is itself restrained dominating is a singleton.

For a complete multipartite graph, a nonempty set \(D\) is dominating exactly when either it meets at least two partite classes or it equals one whole partite class. If \(O=V(G)\setminus D\), then \(G[O]\) has no isolated vertex exactly when \(O=\varnothing\) or \(O\) meets at least two partite classes. These two elementary conditions give the complete restrained-domination test used below.

## Proof
First suppose \(p=0\). Then every part is a singleton and \(G\) is complete. For \(N\ge3\), every singleton is restrained dominating because its complement induces a complete graph of order at least two; for \(N=2\), the two singleton blocks are both non-restrained-dominating but their union is \(V(G)\). Hence the singleton partition is valid and \(\operatorname{RDc}(G)=N\).

Now suppose \(p\ge2\). Consider the singleton partition. A vertex lying in a singleton part is itself a restrained dominating singleton: its complement contains the two non-singleton parts and therefore meets at least two parts. A vertex \(v\) lying in a non-singleton part is not dominating by itself. Choose \(w\) in a different non-singleton part. Then \(\{v,w\}\) meets two parts and dominates, while its complement still meets both of those parts because each has size at least two. Thus \(\{v,w\}\) is restrained dominating, and the two singleton blocks \(\{v\}\) and \(\{w\}\) form a coalition. Every non-restrained-dominating singleton therefore has a partner. The singleton partition has \(N\) blocks, so \(\operatorname{RDc}(G)=N\).

It remains to suppose \(p=1\). Let \(P\) be the unique non-singleton part, of size \(m\ge2\), and let the other \(u\) parts be singletons.

If \(u=1\), the graph is the star \(K_{1,m}\). The only restrained dominating set is \(V(G)\): any proper set containing the center leaves a nonempty subset of the leaf part as an independent complement; the whole leaf part leaves the center isolated in the complement; and a proper subset of the leaf part does not dominate omitted leaves. Thus the union of coalition partners must be all of \(V(G)\), which is impossible in a partition with three or more nonempty blocks. Any bipartition of \(V(G)\) into two proper nonempty sets is a valid coalition partition. Hence \(\operatorname{RDc}(G)=2\).

Finally let \(u\ge2\). Split \(P=A\mathbin{\dot\cup}B\) into two nonempty sets. Each singleton-part vertex is a restrained dominating singleton, while neither \(A\) nor \(B\) dominates and \(A\cup B=P\) is restrained dominating because its complement is the complete graph on the \(u\) singleton-part vertices. Thus there is a restrained coalition partition with \(u+2\) blocks.

For the matching upper bound, use the general inequality \(\operatorname{RDc}(G)\le C(G)\), where \(C(G)\) is the ordinary coalition number. We compute \(C(G)\) directly. In an ordinary coalition partition, every singleton-part vertex must appear as its own singleton block: any larger block containing it meets at least two parts and is dominating, while dominating blocks are required to be singletons. The remaining blocks partition \(P\). A proper nonempty subset of \(P\) is non-dominating, and two such blocks have a dominating union exactly when together they cover all of \(P\). Therefore \(P\) can contribute at most two blocks, and it must contribute exactly two in a maximum partition. Consequently \(C(G)=u+2\), so \(\operatorname{RDc}(G)\le u+2\). The construction above proves equality.

## Verification
The proof is symbolic and covers all positive part sizes. The accompanying `verify.py` independently enumerates every integer part-size profile of total order from \(2\) through \(8\) having at least two parts, generates every set partition of the labeled vertex set, tests the restrained-dominating definition directly, and maximizes valid coalition partitions. It checks all \(58\) complete-multipartite profiles and \(101632\) candidate vertex partitions. It also explicitly checks \(K_{3,1,1}\), where the computed value is \(4\).

The finite enumeration is corroborative only; the infinite theorem follows from the proof above.

## Relationship to prior work
Nesam, Amutha, and Anbazhagan introduced the restrained domination coalition parameter and, in Proposition 2.17, stated that a complete multipartite graph of order \(m\) has restrained domination coalition number \(m\). The same paper immediately precedes this with the distinct star formula \(\operatorname{RDc}(K_{1,n})=2\). Under the standard complete-multipartite convention allowing singleton parts, Proposition 2.17 is therefore overbroad. The present classification identifies the exact missing boundary and supplies the non-star counterexample \(K_{3,1,1}\).

Dobrynin, Glebov, and Golmohammadi subsequently proved the general inequality \(\operatorname{RDc}(G)\le C(G)\) and corrected the cycle values. Their paper does not state a complete-multipartite correction; its full text contains no occurrence of “multipartite.” The inequality is used only for the upper bound in the unique-nonsingleton-part case above.

## Limitations
The result concerns complete multipartite graphs in the standard notation \(K_{n_1,\ldots,n_r}\) with every \(n_i\ge1\). If a source adopts a nonstandard convention that excludes singleton partite classes from the phrase “complete multipartite,” then the disagreement with its wording must be interpreted relative to that convention. No claim is made here for other graph classes or for total restrained coalitions, which use a different domination condition.

## References
1. A. H. Shola Nesam, S. Amutha, N. Anbazhagan, “Restrained Domination Coalition Number of Paths and Cycles,” Statistics, Optimization & Information Computing 14 (2025), 3409–3417, DOI 10.19139/soic-2310-5070-2962. Publisher page records publication on 2025-09-26; the paper lists AMS 2010 subject classification 05C69. Proposition 2.16 gives the star value and Proposition 2.17 states the unrestricted complete-multipartite value.
2. A. A. Dobrynin, A. N. Glebov, H. Golmohammadi, “On Restrained Coalitions in Graphs: Bounds and Exact Values,” Discrete Mathematics Letters 17 (2026), 57–63, DOI 10.47443/dml.2025.223. Theorem 2.1 proves \(\operatorname{RDc}(G)\le C(G)\).
