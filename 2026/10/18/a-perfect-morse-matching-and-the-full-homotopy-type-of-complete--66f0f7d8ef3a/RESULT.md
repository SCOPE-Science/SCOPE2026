# A perfect Morse matching and the full homotopy type of complete-multipartite dominance complexes

## Finding
For any \(k\ge2\), and any integers \(m_1,\ldots,m_k\ge2\), let \(N=\sum_{i=1}^{k}m_i\) and \(G=K_{m_1,\ldots,m_k}\). Its dominance complex satisfies the **homotopy equivalence**
\[
\mathcal D(G)\simeq\left(\bigvee^{k-1}S^{N-3}\right)\vee\left(\bigvee_{i=1}^{k}S^{N-m_i-1}\right).
\]
Dimensions and summands are counted with multiplicity, even when the dimensions coincide. Furthermore the augmented face poset of \(\mathcal D(G)\) admits an explicit acyclic matching with exactly \(k-1\) critical \((N-3)\)-simplices and one critical \((N-m_i-1)\)-simplex for each \(i\). Thus it is perfect for integral free homology as well as every field. For example \(\mathcal D(K_{2,2})\simeq\bigvee^3S^1\), whereas \(\mathcal D(K_{2,3,4})\simeq S^4\vee S^5\vee\bigvee^3S^6\).

## Assumptions and scope
A *dominating set* \(R\subseteq V(G)\) contains or neighbors every vertex. We use the standard dominance complex \(\mathcal D(G)=\{\sigma\subseteq V(G):V(G)\setminus\sigma\text{ dominates }G\}\). In \(K_{m_1,\ldots,m_k}\), the vertex set is partitioned into nonempty pairwise disjoint independent parts \(A_1,\ldots,A_k\), with all edges between different parts and none within a part. Every part has at least two vertices. A finite join and the ordinary topological wedge of geometric realizations are understood throughout. A face has dimension one less than its cardinality; the empty face has formal dimension \(-1\). All displayed spheres have dimension at least one.

## Proof
**Step 1: characterize domination.** A subset \(R\) dominates \(G\) if and only if it meets at least two parts, or equals an entire part \(A_i\). Indeed, meeting two parts gives an external neighbor to each vertex outside \(R\). A subset contained in one part has no external neighbors for the remaining vertices of that part, and thus dominates exactly when it contains that whole part. The empty set never dominates.

**Step 2: a vertex-deletion cofiber and all relative cells.** Choose \(v\in A_1\) and put \(X=\mathcal D(G)\), \(X_0=\operatorname{del}_X(v)\), and \(L=\operatorname{lk}_X(v)\). Since \(X=X_0\cup(v*L)\) with intersection \(L\), the simplicial cofibration yields \(X\simeq X_0/L\). A face \(\sigma\) of \(X_0\) lies outside \(L\) precisely when its dominating complement \(R=V\setminus\sigma\) ceases to dominate after deleting \(v\). By Step 1 this happens exactly in the following mutually exclusive situations:

(1) \(R=A_1\), producing the exceptional relative face \(\sigma_0=V\setminus A_1\);

(2) \(R=\{v\}\cup Q\), with \(\varnothing\ne Q\subsetneq A_j\) for a unique \(j\ge2\). Writing \(B_j=V\setminus(A_j\cup\{v\})\), its relative face is \(\sigma=B_j\cup T\), where \(T=A_j\setminus Q\) runs over all nonempty proper subsets of \(A_j\). Importantly, because \(m_j\ge2\), each \(B_j\) is nonempty. No relative face of one branch is comparable with a relative face of another, or with \(\sigma_0\).

**Step 3: each branch quotient.** Let \(\Delta(S)\) be the full simplex on a nonempty set \(S\), and \(\partial\Delta(S)\) its boundary (allowing the conventional \((-1)\)-sphere when \(|S|=1\)). The downward closure of branch \(j\) is
\[
Y_j=\Delta(B_j)*\partial\Delta(A_j).
\]
The part already in \(L\) is exactly
\[
Z_j=Y_j\cap L=(\partial\Delta(B_j)*\partial\Delta(A_j))\cup\Delta(B_j).
\]
The simplex \(\Delta(B_j)\) attaches along \(\partial\Delta(B_j)\) to the boundary sphere \(\partial\Delta(B_j)*\partial\Delta(A_j)\), which has dimension \(N-4\). Put \(b_j=|B_j|=N-m_j-1\ge1\). The attaching map \(S^{b_j-2}\to S^{N-4}\) is null-homotopic when \(b_j\ge2\) because \(b_j-2<N-4\) (as \(m_j\ge2\)). Consequently \(Z_j\simeq S^{N-4}\vee S^{b_j-1}\). When \(b_j=1\), the simplex is a separate point and the same assertion holds with \(S^0\): \(Z_j\simeq S^{N-4}\sqcup\{\mathrm{pt}\}\simeq S^{N-4}\vee S^0\). Here no assertion of equality as simplicial complexes is intended.

Now \(Y_j\) is contractible, being the join with the simplex \(\Delta(B_j)\), and \(Z_j\subset Y_j\) is a cofibration. Therefore
\[
Y_j/Z_j\simeq\Sigma Z_j\simeq S^{N-3}\vee S^{b_j}.
\]

**Step 4: assemble the wedge.** The downward closure of \(\sigma_0\) is \(\Delta(\sigma_0)\); all its proper faces lie in \(L\), and it contributes \(\Delta(\sigma_0)/\partial\Delta(\sigma_0)\cong S^{N-m_1-1}\). Distinct branch closures and this exceptional simplex intersect only in \(L\), since a face outside \(L\) belongs to exactly one of the disjoint families of Step 2. Hence the quotient is the based wedge of the indicated quotients:
\[
X_0/L\cong S^{N-m_1-1}\vee\bigvee_{j=2}^k\bigl(S^{N-3}\vee S^{N-m_j-1}\bigr).
\]
This proves the asserted homotopy type for **all** part sizes in the specified range, not just the enumerated examples.

**Step 5: explicit acyclic perfect matching.** In the augmented face poset, first pair each face \(\tau\in L\) with \(\tau\cup\{v\}\). These are exactly the faces containing \(v\) and their vertex-deleted partners. In each relative branch \(j\ge2\), fix \(w_j\in A_j\); pair \(B_j\cup T\) with \(B_j\cup T\cup\{w_j\}\) whenever \(\varnothing\ne T\subsetneq A_j\), \(w_j\notin T\), and \(T\cup\{w_j\}\subsetneq A_j\). Exactly two branch faces are unpaired: \(B_j\cup\{w_j\}\), of dimension \(b_j\), and \(B_j\cup(A_j\setminus\{w_j\})\), of dimension \(N-3\). The exceptional \(\sigma_0\) is also unpaired and has dimension \(N-m_1-1\).

Orient matched cover edges upward and every other cover edge downward. There is no directed edge deleting \(v\): all such edges are matched and hence directed upward. Thus a directed cycle cannot pass from the \(v\)-containing layer to the \(v\)-free layer. Within the containing layer every edge is downward. Within the free layer, \(L\) is a down-set with no remaining matched edges, so any path entering \(L\) cannot return to the relative faces. Different relative branches are incomparable, and the exceptional face has no relative neighbors. In a fixed branch every upward edge inserts \(w_j\), while a downward edge cannot remove \(w_j\), because every allowed such cover edge is matched. Thus no directed cycle exists in any branch. This is a genuine global acyclic matching, with precisely the stated critical dimensions.

## Verification
The included standalone `verify_dominance_multipartite.py` independently enumerates all dominating complements, reconstructs the two-stage face matching, checks every matched cover, topologically sorts **every** directed Hasse edge to certify acyclicity, and computes reduced simplicial Betti numbers over \(\mathbb F_2\) from full boundary matrices. The nine tested tuples are \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((3,3,3)\), \((2,3,4)\), \((2,2,2,2)\), \((2,2,3,3)\), and \((4,4)\). All tests passed. The infinite-family conclusion relies on Steps 1–5, not on this finite test set. Run `python verify_dominance_multipartite.py` with a standard Python 3 installation.

## Relationship to prior work
Ehrenborg and Hetyei introduced the dominance complex and established a sphere result for forests. Taylan developed matching-tree methods and proved a sphere result for chordal graphs. In contrast, every graph in the present family has an induced four-cycle, so those graph-family classifications do not cover these examples (including the ordinary four-cycle as the smallest case). Matsushita and Wakatsuki identified the Alexander dual of the dominance complex with the neighborhood complex of the graph complement, yielding powerful *homological* information; their general identity does not specify the attaching maps or provide the explicit perfect matching and homotopy splitting above. Their work also records the known three-circle calculation for the four-cycle, recovered here rather than claimed as new. The new content is the **general** nonchordal multipartite homotopy formula with a uniform, directly checkable discrete-Morse construction.

## Limitations
The formula assumes at least two parts, each of size at least two. Singleton parts or one-part graphs are not included. The chosen vertices in the proof and matching are noncanonical; no action of the automorphism group on homology or equivariant splitting is asserted. The exact proof is abstract simplicial topology, not a machine-assisted formal proof. The finite verifier confirms sample cases only; it is not the basis for extrapolating to all sizes. Existing general-purpose homotopy reductions may produce alternate proofs of particular subfamilies.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923. First publicly online 28 November 2005, as stated in the paper. DOI: `10.1016/j.ejc.2005.04.010`.
2. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:`1501.06754`, first posted 27 January 2015; Order 33 (2016), 459–476.
3. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:`2312.02639`, first posted 5 December 2023; Journal of Combinatorial Theory, Series A 211 (2025), article 105978.
