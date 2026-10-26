# Exact seven-point partition-EKR bound and extremal rigidity

## Finding
Let \(\Pi_{7,4}\) be the set of partitions of \([7]=\{1,\ldots,7\}\) into exactly four nonempty, *unlabelled* blocks. Two partitions \(P,Q\in\Pi_{7,4}\) **pair-intersect** when there exist distinct elements \(a,b\in[7]\) that belong to a common block of \(P\) and also to a common block of \(Q\). If \(\mathcal F\subseteq\Pi_{7,4}\) is pairwise pair-intersecting, then
\[
|\mathcal F|\le S(6,4)=65.
\]
Equality holds if and only if there is an unordered pair \(\{a,b\}\subset[7]\) such that
\[
\mathcal F=\{P\in\Pi_{7,4}:a,b\text{ lie in one block of }P\}.
\]
There are precisely \(\binom 72=21\) distinct labelled extremal families, forming one isomorphism type under permutations of \([7]\).

## Assumptions and scope
Partitions have exactly four nonempty blocks, with no designated block order. “Intersection” means sharing a *two-element subset of a block*, not sharing an entire block and not sharing an element (every pair of partitions shares ground elements). \(S(n,k)\) denotes the Stirling number of the second kind. The assertion is limited to seven ground elements and four blocks, equivalently to rank-three flats of the graphic matroid of \(K_7\).

## Proof
A fixed-pair family is pair-intersecting. Identifying its prescribed pair reduces a partition of seven points into four blocks to a partition of six points into four blocks, so each such family has exactly \(S(6,4)=65\) members. Distinct prescribed pairs yield distinct families.

For the upper bound and equality classification, the following finite exhaustive certificate is a complete search, not a random experiment. Encode each unlabelled partition by its unique *restricted-growth word* \((w_1,\ldots,w_7)\): \(w_1=0\), and for each subsequent position \(w_j\) ranges from \(0\) through \(1+\max_{i<j}w_i\), with exactly four symbols in total. Exhaustive recursion yields \(S(7,4)=350\) distinct words. Their block-size profiles occur in counts \(35,210,105\), respectively for \((4,1,1,1)\), \((3,2,1,1)\), and \((2,2,2,1)\); these independently sum to \(350\).

Index the \(\binom72=21\) unordered ground-point pairs and associate to a partition \(P\) the 21-bit integer \(m(P)\), whose bit for \(\{a,b\}\) is set precisely when \(a,b\) share a block of \(P\). Construct the graph \(G\) on all 350 partitions, adjoining distinct \(P,Q\) precisely when \(m(P)\mathbin{\&}m(Q)\ne0\). Every pair-intersecting family is exactly a clique of \(G\), so the task is to bound its clique number and classify all maximum cliques.

The accompanying self-contained file `verify.py` performs a branch-and-bound search *without using an external solver*. At every search node it greedily partitions the surviving candidate vertices into independent colour classes. Within each class, a clique can use at most one vertex; consequently, if a branch currently has \(d\) chosen vertices, and the remaining vertex prefix has been assigned at most \(c\) colours, that branch cannot reach a target \(t\) when \(d+c<t\). For each candidate vertex chosen, recursion restricts the candidate set to its neighbours; already handled vertices are removed, so every potential clique is represented by a branch and target-sized cliques are counted only once. A recursive call ending at \(d=t\) records a target clique; a branch failing the colour bound is discarded by this proved upper bound rather than by an empirical heuristic.

With target \(t=66\), the complete search visits \(396\) recursion nodes and finds no clique. Thus all pair-intersecting families have size at most 65. With target \(t=65\), the complete enumeration visits \(1827\) nodes and returns precisely 21 cliques. A separately generated set of the 21 fixed-pair families is verified to have 65 vertices apiece and to coincide exactly, as a set of vertex subsets, with the enumerated cliques. This proves the bound and the asserted complete equality classification.

## Verification
Run `python3 verify.py` using Python's standard library, with the script in the same directory as this document. Its exact output is in `verification_output.txt`: `partitions=350`, `star_size=65 labelled_stars=21`, `clique_ge_66=False search_nodes=396`, `cliques_size_65=21 search_nodes=1827`, `all_maximum_families_are_stars=True`, and `VERIFY_OK`. The verifier explicitly generates every partition and every pair-intersection adjacency. A separately implemented C++ maximum-clique branch-and-bound (`maxclique.cpp`) also yields maximum size 65 on 350 vertices; run `g++ -O2 -std=c++17 maxclique.cpp -o maxclique && ./maxclique 7 3` to replay its calculation, with an exact sample in `cpp_verify_output.txt` and diagnostic text in `cpp_progress.txt`. The branch-and-bound completeness argument above explains why no unvisited clique of target size can exist. The finite enumeration is exhaustive for exactly this finite ground set; it gives no claim for larger ground sets.

## Relationship to prior work
Erdős and Székely formulate a conjecture attributed to Czabarka: if partitions of \(n\) elements into \(k\) blocks are pairwise pair-intersecting, then the fixed-pair family of size \(S(n-1,k)\) should be largest for \(n\le2k-1\). This finding verifies and classifies equality at \((n,k)=(7,4)\), precisely the endpoint \(n=2k-1\) for four-block partitions. Cao, Liao and Zhang (2026) prove a higher-rank general theorem in a substantially larger ground-set range and explicitly retain the near-boundary conjectural regime; their rank-three theorem with at least 24 ground elements does not cover the present seven-element case. Meagher and Moura (2005) treat intersecting *whole blocks* in structured partition systems, which is a different relation. No stronger published statement covering the exact bound together with seven-point equality classification was identified in the inspected materials; a search is not a proof of historical priority.

## Limitations
This is a fully finite, code-assisted mathematical proof for exactly seven ground elements and four blocks. Its completeness relies on the correctness of the enumerator, compatibility test and colour-bounded exhaustive search, whose logic is shown above and whose implementation is provided. It does not prove the general conjecture, extend to larger ranks, or establish historical priority independently of a comprehensive review of every prior publication. Independent external audit has not been performed.

## References
1. P. L. Erdős and L. A. Székely, *Erdős-Ko-Rado Theorems of Higher Order* (2000), Section 3, Conjecture 1. Author-hosted full text: https://www.renyi.hu/~elp/Other/higher.pdf.
2. M. Cao, J. Liao and H. Zhang, *Erdős--Ko--Rado and Hilton--Milner Theorems in the Partition Lattice* (first publicly available 2026-08-06), arXiv:2608.05951, Theorems 1.1--1.2 and closing discussion. https://arxiv.org/abs/2608.05951.
3. K. Meagher and L. Moura, *Erdős–Ko–Rado theorems for uniform set-partition systems*, Electron. J. Combin. 12 (2005), R40; Section 5.2. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1r40.
