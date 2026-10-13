# Exact component phase diagram for dominating-set reconfiguration of crown graphs

## Finding
Let \(G=\operatorname{Cr}_n=K_{n,n}-M_n\), for each integer \(n\ge3\), with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and missing edges \(a_i b_i\). For integer \(k\ge2\), define the *add–delete reconfiguration graph* \(D_k(G)\) to have one vertex for each dominating set of \(G\) with at most \(k\) vertices; two such vertices are adjacent when their sets differ by exactly one graph vertex. Let \(c_{n,k}\) be its number of connected components.

**Theorem.** For all integers \(n\ge3\) and \(k\ge2\),
\[
c_{n,k}=\begin{cases}
n,& k=2,\\
n+2\mathbf1_{\{n=3\}},&k=3,\\
1+\binom{n}{2}\binom{n-2}{2}+2\mathbf1_{\{n=4\}},&k=4,\ n\ge4,\\
1,&5\le k<n,\\
3,&k=n\ge5,\\
1,&k\ge n+1.
\end{cases}
\]
These six alternatives are disjoint and exhaust the indicated domain. At budget \(4\), the binomial term counts isolated mixed minimal dominating sets supported on two vertices of each side with disjoint deleted-matching indices; the extra term for \(n=4\) counts the two isolated entire sides. At budget \(n\ge5\), the two entire sides are isolated and the remaining vertices form one connected component. For every \(n\ge6\), connectivity holds at budget \(5\), fails at budget \(n\), and returns at budget \(n+1\); hence budget-monotone connectivity is false even within this explicit bipartite family.

## Assumptions and scope
All graphs are finite, undirected, simple and labeled as above. A dominating set \(S\subseteq V(G)\) is one such that every vertex outside \(S\) has a neighbor in \(S\). The reconfiguration operation is *token addition/removal* (TAR), not token jumping, swapping, or sliding; the bound \(k\) applies to every intermediate dominating set. Denote the selected index sets by \(I=\{i:a_i\in S\}\) and \(J=\{j:b_j\in S\}\). A *matched pair* means \(\{a_i,b_i\}\), which is a nonedge of \(G\) but dominates \(G\). The indicator \(\mathbf1_{\{P\}}\) equals \(1\) when \(P\) holds and \(0\) otherwise.

## Proof
**Step 1 (classification of inclusion-minimal dominating sets).** Such a set is exactly one of the following three types:

(i) a pair \(P_i=\{a_i,b_i\}\), for any \(1\le i\le n\);

(ii) a set \(Q_{I,J}=\{a_i:i\in I\}\cup\{b_j:j\in J\}\) with \(\lvert I\rvert=\lvert J\rvert=2\) and \(I\cap J=\varnothing\);

(iii) either entire bipartition class \(A\) or \(B\).

Indeed, the pair \(P_i\) dominates because \(a_i\) is adjacent to all \(b_j\) with \(j\ne i\) and \(b_i\) to all \(a_j\) with \(j\ne i\). Thus any dominating set containing a pair has a minimal dominating subset of type (i). A set contained in one bipartition class dominates only if it equals the entire class: no unselected vertex in that same class could otherwise be dominated. Consider instead a dominating set meeting both classes and containing no pair. Its index sets \(I,J\) are disjoint. Necessarily \(\lvert I\rvert,\lvert J\rvert\ge2\): if, say, \(I=\{i\}\), then the unselected vertex \(b_i\) has no selected neighbor, while \(J=\varnothing\) is ruled out by the one-class case. Conversely, if both sizes are at least two, every unselected vertex has a selected neighbor on the opposite side, since at most one opposite vertex is its nonneighbor. One can therefore trim to two selected indices per side. Each resulting \(Q_{I,J}\) is minimal, as deleting a member of either side leaves a one-element side disjoint from the other, thereby failing domination; and \(A,B\) are minimal by the one-class observation. This proves the classification. The type-(ii) count is \(\binom n2\binom{n-2}2\).

**Step 2 (the pair core).** Let \(\mathcal C_k\) consist of feasible dominating sets containing some \(P_i\). Each such set is joined by successive vertex deletions to that pair. If \(k\ge4\), any two pairs \(P_i,P_j\) can be connected: starting with \(P_i\), add \(a_j\) and \(b_j\) (reaching size four), then remove \(a_i\) and \(b_i\). Every intermediate set contains at least one complete pair. Hence \(\mathcal C_k\) is connected for \(k\ge4\). For \(k=2\) precisely the \(n\) pairs occur, and all are isolated. For \(k=3\), any feasible set other than an entire part is a pair or a three-element superset of exactly one pair; hence the pair-centered components are disjoint stars, one for each index, with \(2n-2\) leaves each. When \(n=3\), there are also the two entire-side sets of size three, each isolated because it is minimal and no addition fits the budget. This establishes the first two lines.

**Step 3 (the budget-four isolates).** For \(n\ge4\), every type-(ii) set has size four, is minimal, and therefore has no permitted deletion or addition when \(k=4\). Such sets supply exactly \(\binom n2\binom{n-2}2\) isolated components. When \(n=4\), the entire classes also have size four and are isolated. Every remaining feasible dominating set contains a pair and hence lies in the connected core \(\mathcal C_4\). This proves the third line. If \(n=3\), the budget \(4\) case belongs instead to the final line below.

**Step 4 (bridging the four-sets).** For any \(k\ge5\), from a type-(ii) set \(Q_{I,J}\) one may add \(a_j\) for any \(j\in J\), obtaining a size-five dominating set containing the pair \(P_j\). Thus every type-(ii) set, and every dominating superset of one, lies in the pair core whenever feasible; to see this for any superset, delete its excess vertices to a type-(ii) minimal set and reverse that deletion path. A dominating set whose minimal subset is a pair is already in the core.

**Step 5 (the entire sides and all remaining budgets).** Both classes \(A,B\) are inclusion-minimal of size \(n\). They are absent for \(k<n\) and are isolated for \(k=n\), because no deletion preserves domination and no addition satisfies the budget. When \(k\ge n+1\), adding an arbitrary opposite-class vertex to \(A\) or \(B\) forms a set containing a complete pair, so each class joins \(\mathcal C_k\). Every other dominating set has a minimal subset of type (i) or (ii), and by Steps 2–4 belongs to the same component whenever \(k\ge5\). For \(n=3\) and \(k\ge4\), note that type (ii) is impossible and the two side-sets connect to the pair core at \(k=4\); this covers the only budget-four boundary omitted in Step 3. The stated cases now follow. \(\square\)

## Verification
The independent-of-proof brute-force script `verify.py` enumerates all \(2^{2n}\) vertex subsets for each \(3\le n\le8\), tests domination using the actual adjacency of the deleted-matching biclique, builds TAR adjacency by every single-bit flip, computes connected components, and compares their number with the six-case formula for each \(2\le k\le n+1\). It additionally checks star sizes, isolated four-set counts, and the entire-side isolates. Run `python3 verify.py` from the directory containing this document and the script. Observed output starts with `VERIFY_OK` and reports `orders=3..8 cases=33`, `set_visits=165129`, `edge_visits=954140`. This exhaustive finite check is corroborative, not an infinite-order proof; the proof above establishes the unrestricted integer quantifiers.

## Relationship to prior work
Haas and Seyffarth introduced the TAR \(k\)-dominating graph and proved broad connectivity criteria for bipartite graphs. Their criterion at budget \(\Gamma(G)+1\) already covers the return to connectivity at \(k=n+1\), once the familiar equality \(\Gamma(\operatorname{Cr}_n)=n\) is supplied; that endpoint is not claimed as a new general result. Suzuki, Mouawad and Nishimura studied boundary cases and counterexamples for other graph families, including the failure of general budget-monotone connectivity. Alikhani, Fatehi and Klavžar studied structural realizability and related aspects of dominating graphs. Exact enumeration of crown-graph inclusion-minimal dominating sets is also prior information; the present claim concerns the *entire component structure under a variable budget*, in particular the exact \(\binom n2\binom{n-2}2\) isolated-vertex obstruction at \(k=4\), its disappearance at \(k=5\), and the later reappearance of exactly two isolates at \(k=n\). None of the cited general connectivity statements or minimal-set counts by themselves asserts this six-regime component formula.

## Limitations
The formula concerns the TAR convention, not alternative reconfiguration moves. It gives component numbers and indicated component shapes but does not determine diameters or the full adjacency spectrum of the reconfiguration graphs. Exhaustive computations cover only \(3\le n\le8\). General-literature overlap beyond the inspected full-text sources and indexed searches remains a possible residual risk; uniqueness is not independently certified.

## References
1. R. Haas and K. Seyffarth, *The k-Dominating Graph*, arXiv:1209.5138v1 (first public 2012-09-24), https://arxiv.org/abs/1209.5138 .
2. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714v1 (2014-01-22), https://arxiv.org/abs/1401.5714 .
3. S. Alikhani, D. Fatehi and S. Klavžar, *On the Structure of Dominating Graphs*, arXiv:1512.07514 (first public 2015-12-23), https://arxiv.org/abs/1512.07514 .
4. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956 (2020), https://arxiv.org/abs/2003.05956 .
