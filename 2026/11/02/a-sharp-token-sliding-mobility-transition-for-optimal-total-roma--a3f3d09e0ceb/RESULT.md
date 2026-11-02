# A sharp token-sliding mobility transition for optimal total Roman functions on Kneser graphs

## Finding

Let \(k\ge 2\), \(n\ge k(k+1)\), and let \(K(n,k)\) be the Kneser graph whose vertices are the \(k\)-subsets of \([n]\), adjacent exactly when disjoint. A total Roman dominating function is a labeling \(f:V(K(n,k))\to\{0,1,2\}\) such that (i) each \(0\)-labeled vertex has a \(2\)-labeled neighbor, and (ii) every positive-labeled vertex has a positive-labeled neighbor. Its weight is the sum of labels. Only **minimum-weight** functions are considered below.

Write \(s=n-k(k+1)\), and let \(\mathscr R_{n,k}\) be the graph whose vertices are minimum-weight total Roman functions, with an edge whenever one \(2\)-label is moved to a previously \(0\)-labeled adjacent Kneser vertex, leaving every other label unchanged, and the intermediate state is not used. This is the token-sliding rule restricted to minimum total Roman functions.

**Theorem.** Every minimum function assigns label \(2\) to exactly \(k+1\) pairwise disjoint \(k\)-subsets and assigns \(0\) elsewhere. Its weight is \(2(k+1)\); this weight and the disjoint-block construction were established previously [1], and are not claimed as new. The reconfiguration graph has
\[
N_{n,k}=\frac{n!}{s!(k!)^{k+1}(k+1)!}
\]
vertices and is regular of degree
\[
d_{n,k}=(k+1)\binom{s}{k},
\]
where \(\binom{s}{k}=0\) if \(s<k\). Its complete component structure is:

* If \(0\le s<k\), it has \(N_{n,k}\) isolated vertices.
* If \(s=k\), it is the disjoint union of
\[
\frac{n!}{(k!)^{k+2}(k+2)!}
\]
cliques of order \(k+2\).
* If \(s\ge k+1\), it is connected.

In particular, the exact connectivity threshold is \(n=k(k+2)+1\). When connected, it has exactly \(N_{n,k}d_{n,k}/2\) edges.

## Assumptions and scope

The graph is simple and undirected. Here \(k,n\) are integers; vertices of \(K(n,k)\) are **unordered** subsets, and a minimum labeling is not equipped with distinguishable tokens. Ground-set labels distinguish configurations: all counts are labeled counts. The 2018–2025 literature on clique and matching reconfiguration uses several different sliding conventions; the one here requires the **removed and inserted Kneser vertices to be adjacent**, i.e., their representing \(k\)-subsets to be disjoint. It is not the operation that moves an endpoint of a matching edge.

## Proof

**1. Characterization of minimum labelings.** Write \(F\) for the family of vertices labeled \(2\), and let \(t=|F|\), \(u\) be the number of vertices labeled \(1\). Every \(k\)-set meeting every member of \(F\), unless it belongs to \(F\), must be labeled \(1\). A family of \(k+1\) disjoint \(k\)-sets yields a valid total Roman labeling by giving its members label \(2\): every \(k\)-set meets at most \(k\) of these disjoint blocks and is therefore disjoint from some block; every positive vertex also sees another positive vertex. Its weight is \(2(k+1)\).

For completeness, we verify that no other labeling attains this weight. If \(t=0\), no zeros are allowed and the weight is \(\binom nk>2(k+1)\). If \(t\ge k+2\), the weight is at least \(2(k+2)\). Suppose \(1\le t\le k-1\). By Hall's theorem, choose distinct representatives, one from each of the \(t\) size-\(k\) sets in \(F\), forming a set \(H\) of size \(t\). The complement \(R=[n]\setminus\bigcup F\) has size at least \(k(k+1-t)\). For \(r=k-t\), every set \(H\cup X\) with \(X\subseteq R\), \(|X|=r\), meets every element of \(F\) and differs from all of them. Therefore
\[
u\ge \binom{k(r+1)}r>2(r+1)=2(k+1-t)
\]
whenever \(k\ge3\) or \(r\ge2\). In the sole exceptional pair \((k,t)=(2,1)\), the number of \(2\)-sets meeting the unique \(2\)-labeled pair but differing from it is \(2(n-2)\ge8>4\); again \(2t+u>2(k+1)\).

If \(t=k\) and the members of \(F\) are disjoint, independently choose one point from each: these give \(k^k\ge4\) distinct \(k\)-sets meeting all members of \(F\) and differing from them, so \(u>2\). If two members intersect, choose a common element of those two, and one element from each of the remaining \(k-2\) members, making a hitting set \(H\) of at most \(k-1\) elements. The set \(R\) outside all members of \(F\) has at least \(k\) elements; enlarging \(H\) by subsets of \(R\) to size \(k\) gives at least \(k\) distinct members outside \(F\) that hit every member. For \(k\ge3\), this exceeds \(2\); if \(k=2\), two intersecting pairs have union of size \(3\), hence \(|R|=n-3\ge3\), again exceeding \(2\). Thus \(2t+u>2(k+1)\) throughout \(t\le k\).

Consequently, minimum weight forces \(t=k+1\) and \(u=0\). If two members of \(F\) intersect, their common element together with one element from each of the other \(k-1\) members can be completed to a \(k\)-set meeting *every* member of \(F\). If this \(k\)-set belongs to \(F\), it violates positive-neighbor totality; if not, it is a zero with no label-\(2\) neighbor. Hence all \(k+1\) members of \(F\) must be pairwise disjoint. Conversely, their disjointness was already shown sufficient. (The existing literature [1] implies the optimum value and exhibits the matching construction; the new claim of this paper is the component theorem.)

**2. Vertex count and degree.** A configuration is an unordered family of \(k+1\) disjoint \(k\)-blocks, with \(s\) unused ground elements. Counting ordered partitions and removing the block ordering gives \(N_{n,k}\). Each move chooses one of \(k+1\) occupied blocks to remove and one new \(k\)-subset of the \(s\) previously unused elements to insert; the new block must be disjoint from the removed block and from the retained blocks. These choices give distinct edges and exactly \(d_{n,k}\) neighbors.

**3. No free block and exactly one free block.** For \(s<k\), there is no unused \(k\)-subset, so every state is isolated. For \(s=k\), adjoining the single unused \(k\)-set to the occupied blocks creates a partition of all \([n]\) into \(k+2\) unordered \(k\)-blocks. A move interchanges which one of these \(k+2\) blocks is unused, leaving the underlying partition invariant. Conversely any two choices of the unused block are related by one move. Thus each partition contributes exactly \(K_{k+2}\), and the number of such partitions is the stated factorial quotient.

**4. Connectivity after one additional free element.** Assume \(s\ge k+1\). Temporarily allow an **exchange**, in which one occupied \(k\)-block is replaced by any other \(k\)-block disjoint from the remaining occupied blocks; adjacency between the removed and inserted blocks is not required. We first show all configurations are connected under exchanges.

Label the \(k+1\) blocks temporarily. Let \(U\) be the unused-element set and choose a block \(B\), an element \(x\in B\), and \(y\in U\). Because \(|U|\ge k+1\), choose \(C\subseteq U\setminus\{y\}\) with \(|C|=k\). The two exchanges
\[
B\longrightarrow C\longrightarrow(B\setminus\{x\})\cup\{y\}
\]
preserve disjointness from all other blocks and swap the occupied element \(x\) with the unused element \(y\). Such occupied–unused transpositions generate every permutation of the ground elements across the occupied blocks and the unused pool: to swap elements of two occupied blocks, use one unused element as a three-transposition buffer. Hence the graph of labeled-block configurations is exchange-connected, and so is the unlabeled graph.

Finally consider **any** permitted exchange, keeping the other \(k\) occupied blocks fixed. The available ground set for the moving block contains \(n-k^2\ge2k+1\) elements. On that set, all \(k\)-subsets form a connected Kneser graph under disjoint-set adjacencies: the Johnson graph of one-element replacements is connected, and two Johnson-adjacent \(k\)-sets have a union of size \(k+1\), so a disjoint auxiliary \(k\)-set exists when the ambient set has at least \(2k+1\) points. Hence each one-element replacement can be implemented by two Kneser slides. Every exchange can therefore be replaced by a finite path of legal token slides while the other \(k\) blocks are fixed. Because exchanges connect all configurations, slides do too.

The three cases are exhaustive. \(\square\)

## Verification

Run `python3 verify.py` from a directory containing the standalone script. It independently constructs three-matchings of complete graphs, builds all legal token-sliding transitions for \(k=2\), and checks components, degrees, and state counts for \(6\le n\le10\). It independently evaluates the original total Roman condition on every three-defender labeling for \(6\le n\le9\). It verifies connectivity of the auxiliary Kneser graphs \(K(5,2)\), \(K(7,3)\), and \(K(9,4)\), and checks factorial component identities for \(2\le k\le14\). The script terminates with `VERIFY_OK` if every assertion holds. These are finite diagnostics; the proof above supplies the all-integer result.

Representative exact results: \(k=2,n=6\) has \(15\) isolates; \(n=7\) has \(105\) isolates; \(n=8\) has \(105\) copies of \(K_4\); and \(n=9\) has one connected, degree-\(9\) graph on \(1260\) vertices.

## Relationship to prior work

Zec and Grbić [1] proved \(\gamma_{tR}(K(n,k))=2(k+1)\) for \(n\ge k(k+1)\) and constructed labelings using pairwise disjoint \(k\)-sets. Brešar, Cornet, Dravec, and Henning [2] proved clique structure for several minimum multiple-domination variants of Kneser graphs. These are **existing optimization results**, not novelty claimed here.

Bousquet, Hatanaka, Ito, and Mühlenthaler [3] studied reconfiguration of matchings primarily under unrestricted token jumping; their problem is closely related to the exchange graph used as an auxiliary device here. Lam, Phan, and Hoang [4] developed the general framework of clique token-sliding and token-jumping reconfiguration; they do not provide this Kneser-family component classification. The new claim concerns the exact sharp component transition under Kneser-adjacent slides on optimal total Roman labelings, including its critical clique decomposition.

## Limitations

This result concerns only the specified minimum-weight total Roman functions, only the Kneser graph \(K(n,k)\) for \(k\ge2\), \(n\ge k(k+1)\), and only the specified one-token sliding rule. It does not determine graph diameter or mixing time in the connected range, nor does it address Roman functions above minimum weight. Computations do not establish the infinite theorem; that depends on the written argument. Although targeted record and primary-literature comparisons did not identify a prior identical statement, unpublished or unindexed equivalent results remain possible, especially via graph-clique reconfiguration or set-partition state graphs. Independent validation has not been performed.

## References

[1] T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, Discrete Mathematics & Theoretical Computer Science 25:1 (2023), article 14; arXiv:2204.05664 (first public version April 12, 2022), DOI 10.46298/dmtcs.10506.

[2] B. Brešar, M. G. Cornet, T. Dravec, and M. A. Henning, *\(k\)-Domination invariants on Kneser graphs*, arXiv:2312.15464 (December 24, 2023).

[3] N. Bousquet, T. Hatanaka, T. Ito, and M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419 (December 13, 2018).

[4] Q. N. Lam, H.-A. Phan, and D. A. Hoang, *A Note on Reconfiguration Graphs of Cliques*, arXiv:2506.07821 (June 9, 2025).

[5] L. Eroh and M. Schultz, *Matching graphs*, Journal of Graph Theory 29 (1998), 73–86, DOI 10.1002/(SICI)1097-0118(199810)29:2<73::AID-JGT3>3.0.CO;2-9 (abstract inspected; full text not available in this inspection).
