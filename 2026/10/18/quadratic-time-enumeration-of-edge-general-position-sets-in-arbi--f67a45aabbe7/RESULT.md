# Quadratic-time enumeration of edge general-position sets in arbitrary trees

## Finding
Let \(T\) be an arbitrary finite simple tree with \(n\geq1\) vertices. An edge set \(S\subseteq E(T)\) is **edge general position** if no simple path contains three distinct edges of \(S\). Define its full cardinality enumerator by
\[
\mathcal E_T(z)=\sum_{\substack{S\subseteq E(T)\\ S\text{ edge general position}}}z^{|S|}.
\]
**Theorem.** All coefficients of \(\mathcal E_T(z)\), including the counts of small and maximum edge general-position sets, are computed exactly by the three-state rooted-tree recursion given below in \(O(n^2)\) integer-arithmetic operations, independently of the number or placement of branching vertices. The recurrence is valid for the single-vertex tree, where \(\mathcal E_T(z)=1\).

This is a counting statement rather than merely an extremal formula. A rooted subtree contributes three polynomials, distinguished by maximum number \(0,1,2\) of selected edges on a root-to-vertex path.

## Assumptions and scope
All graphs here are finite, simple and undirected. The input is a connected acyclic graph \(T\), whose vertex and edge labels, if supplied, are retained. Paths include their endpoints. In a tree, every simple path is the unique geodesic between its endpoints; therefore the displayed definition agrees with ordinary edge general position. Empty edge sets are counted once, and all set counts concern distinct subsets of the actual edge set, not graph-isomorphism types.

For an edge subset \(S\), assign each edge \(e\) its indicator weight \(w_S(e)=1\) if \(e\in S\), and \(0\) otherwise. For vertices \(a,b\) set
\[
 d_S(a,b)=\sum_{e\in E(P_{ab})}w_S(e),\qquad
 \Delta(S)=\max_{a,b\in V(T)}d_S(a,b).
\]
The crucial equivalence is
\[
 S\text{ is edge general position}\quad\Longleftrightarrow\quad\Delta(S)\leq2.
\]
No restriction on the ordinary diameter or maximum degree of \(T\) is needed.

## Proof
**Step 1: weighted-path equivalence.** In a tree, a path contains at least three edges of \(S\) precisely when the sum of the indicator weights along that path is at least three. Every simple path joins some pair of tree vertices. Maximizing this sum over all vertex pairs gives \(\Delta(S)\). Hence exactly those subsets with \(\Delta(S)\leq2\) are admissible.

**Step 2: rooted states.** Root the tree at an arbitrary vertex \(r\). For a vertex \(v\), write \(T_v\) for the subtree rooted at \(v\). For \(a\in\{0,1,2\}\), define
\[
 F_v^{(a)}(z)=\sum_{\substack{S\subseteq E(T_v)\\ \Delta_{T_v}(S)\leq2\\ H_v(S)=a}} z^{|S|},\qquad
 H_v(S)=\max_{x\in V(T_v)}d_S(v,x).
\]
For a leaf, \(F_v^{(0)}=1\) and \(F_v^{(1)}=F_v^{(2)}=0\). All polynomials with an out-of-range superscript are zero.

Suppose \(w\) is a child of \(v\). After adding the edge \(vw\), its selected-edge indicator \(b\in\{0,1\}\) increases every \(v\)-to-branch path weight by \(b\); paths entirely inside \(T_w\) are unchanged. Consequently the branch polynomials, indexed by maximum distance from \(v\), are exactly
\[
 B_{vw}^{(h)}(z)=F_w^{(h)}(z)+zF_w^{(h-1)}(z),\qquad h=0,1,2.
\]
Terms with \(h=3\), and hence with a root-to-vertex path of selected weight three, are discarded. Notice that the unselected choice contributes no factor of \(z\), whereas the selected edge contributes one.

**Step 3: merge rule.** Merge the child branches of \(v\) in any fixed order. Start with \(A^{(0)}=1\) and \(A^{(1)}=A^{(2)}=0\), representing the singleton vertex \(v\). When merging a new branch with polynomials \(B^{(h)}\), replace the three accumulated polynomials by
\[
 A_{\mathrm{new}}^{(c)}(z)=
 \sum_{\substack{0\leq a,h\leq2\\a+h\leq2\\ \max\{a,h\}=c}}
 A^{(a)}(z)B^{(h)}(z),\qquad c=0,1,2.
\]
Indeed, paths with both endpoints in the old union, or both in the new branch, were certified at previous steps. Any remaining path has endpoints in different pieces and passes through \(v\). Its maximum selected weight is **exactly** \(a+h\), because the maximum path weights \(a\) and \(h\) are each attained in their respective finite pieces. It is admissible precisely when \(a+h\leq2\). The maximum distance from \(v\) in the merged piece is exactly \(\max\{a,h\}\). Thus the recurrence neither rejects a valid subset nor double-counts one; selected-edge assignments of different branches are disjoint and independently specified.

Induction on the rooted tree now proves that the final accumulated polynomials are \(F_v^{(0)},F_v^{(1)},F_v^{(2)}\) at every vertex. At the root,
\[
 \boxed{\mathcal E_T(z)=F_r^{(0)}(z)+F_r^{(1)}(z)+F_r^{(2)}(z).}
\]
This proves the claimed exact enumerator for every finite tree, without any restriction on shape or branching complexity.

**Step 4: arithmetic bound.** Represent each polynomial as its dense array of integer coefficients. For a merge whose processed piece has \(s\) edges and incoming child subtree has \(t\) edges, at most nine ordinary polynomial convolutions are required, each in \(O((s+1)(t+1))\) arithmetic operations. Across all merges, the \(st\) terms charge each unordered pair of edges in *different* child pieces at their unique first meeting vertex, at most once. The linear terms \(s+t+1\) sum to \(O(n^2)\), because every edge can belong to at most \(n\) rooted subtree/processed-prefix descriptions. Thus the total operation count is \(O(n^2)\), including coefficient-array updates. Coefficients can have exponentially many configurations, so this is an arithmetic-operation bound and not a claim of constant-bit integer operations.

**A non-spider specialization.** Let \(D_{a,b}\) be the double-star consisting of a central edge with \(a\) pendant edges incident to one endpoint and \(b\) incident to the other, with \(a,b\geq1\). If the central edge is unselected, any collection of pendant edges is valid. If it is selected, selected pendant edges must lie entirely on one side. Therefore
\[
 \mathcal E_{D_{a,b}}(z)=(1+z)^{a+b}
 +z\big((1+z)^a+(1+z)^b-1\big).
\]
This exact formula is an independent check on the merge rule when there are two distinct branching vertices. More generally, stars and paths yield \((1+z)^{n-1}\) and \(1+(n-1)z+\binom{n-1}{2}z^2\), respectively, with the evident omission of impossible terms for short paths.

## Verification
The accompanying `verify.py` independently constructs the unique graph paths and checks every edge-subset mask directly against the condition that no path carries three selected edges. This exhaustive checker does not use the rooted-state criterion to decide validity. It compares resulting coefficient arrays against the recursion on **18,744** labeled-tree instances and checks **1,390,623** edge-subset masks. The instances include all Prüfer-encoded labeled trees through seven vertices and further fixed-seed sampled trees through thirteen vertices. Separate exact identities are checked for stars and paths through sixty vertices and for 100 double-star profiles.

Run `python3 verify.py` with standard Python 3; the recorded expected result is in `verification_output.txt`. Successful finite tests support implementation correctness, but the general theorem is proved by the preceding induction, not by extrapolation from finite cases.

## Relationship to prior work
Manuel, Prabha and Klavžar introduced edge general position and determined its **maximum cardinality** for every tree as the number of leaves; their paper does not give a coefficient-by-coefficient enumeration of all edge general-position subsets of arbitrary trees. Klavžar and Tan subsequently studied extremal edge general-position sets in Fibonacci and Lucas cubes. Tian, Klavžar and Tan studied extremal edge general-position numbers and block-graph bounds. An earlier published combinatorial record explicitly counts edge general-position sets for **spider trees** (one possible branching vertex); its closed expression is a proper special case and does not establish the above recursion for trees with unrestricted numbers of branching vertices. The double-star identity shows the first genuinely multi-branching setting, while the recursion handles all such settings.

The new claim is restricted to the quadratic-arithmetic full-tree enumeration theorem, not the known leaf extremal number or already-available special-family polynomial identities.

## Limitations
This result concerns trees and ordinary edge general position only; the recurrence need not remain correct for graphs with cycles, because arbitrary simple paths are then not necessarily geodesics. The stated running time counts integer arithmetic operations rather than bit operations, and constructing the full degree-\(n-1\) coefficient array necessarily requires output space. Similar algorithms might exist under different names or in unindexed literature; exhaustive bibliographic priority and independent validation have not been established. The computation does not enumerate or list individual qualifying subsets efficiently; it counts them by cardinality.

## References
1. P. Manuel, R. Prabha and S. Klavžar, *The edge general position problem*, Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 2997–3009; publicly available preprint arXiv:2105.04292, initially posted 2021-05-10. DOI: 10.1007/s40840-022-01319-8.
2. S. Klavžar and E. Tan, *Edge general position sets in Fibonacci and Lucas cubes*, Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 120; preprint arXiv:2304.10114, initially posted 2023-04-20. DOI: 10.1007/s40840-023-01517-y.
3. J. Tian, S. Klavžar and E. Tan, *Extremal edge general position sets in some graphs*, Graphs and Combinatorics 40 (2024), article 40; preprint arXiv:2302.01587, initially posted 2023-02-03. DOI: 10.1007/s00373-024-02770-z.
4. *All edge general-position sets of spider trees*, public mathematical research record, identifier `96369ffaa123` (spider-only structural formula).
