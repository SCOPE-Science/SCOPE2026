# Well-edge-dominated complete bipartite graphs with a matching deleted
## Finding
Let \(1\le a\le b\) and \(0\le t\le a\), and let
\[
G_{a,b,t}=K_{a,b}-M_t,
\]
where \(M_t\) is a matching of size \(t\). Then \(G_{a,b,t}\) is well-edge-dominated if and only if at least one of the following holds:

1. \(a=1\);
2. \(t=0\) and \(a=b\);
3. \(a=2\) and \(t=2\);
4. \((a,b,t)=(2,3,1)\);
5. \((a,b,t)=(3,4,3)\).

Thus, after excluding stars and the previously understood undeleted balanced bicliques, the unbalanced matching-deletion members that are well-edge-dominated are exactly
\[
K_{2,b}-M_2\quad (b\ge3),\qquad K_{2,3}-M_1,\qquad K_{3,4}-M_3.
\]

## Assumptions and scope
All graphs are finite and simple. An edge dominating set is a set of edges that dominates every edge by equality or incidence. It is minimal when no proper subset remains edge dominating. A graph is well-edge-dominated when all minimal edge dominating sets have the same cardinality.

Label the bipartition classes by \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), and take the deleted matching to be \(\{a_i b_i:1\le i\le t\}\). Identify each surviving edge \(a_i b_j\) with cell \((i,j)\) in an \(a\)-by-\(b\) board whose only holes are the \(t\) diagonal cells \((i,i)\) with \(i\le t\).

## Proof
Let \(F\) be an edge set, let \(R\) and \(C\) be the rows and columns met by \(F\), and put \(I=[a]\setminus R\) and \(J=[b]\setminus C\). A surviving cell is undominated exactly when its row and its column are both missed. Therefore \(F\) is edge dominating exactly when
\[
I\times J\subseteq \{(h,h):1\le h\le t\}.
\]
Because the holes form a matching, this happens precisely in one of four support patterns: \(I=\varnothing\); \(J=\varnothing\); \(I=J=\varnothing\); or \(I=J=\{h\}\) for some \(h\le t\).

Minimality sharpens these patterns. If \(I=\varnothing\) and \(J\ne\varnothing\), every selected cell must be the only selected cell in its row, so every such minimal set has size \(a\). The only exceptional local check occurs when \(J=\{h\}\) is exactly the missing diagonal hole; then the selected cell in row \(h\) must also be the only selected cell in its column, but the size is still \(a\). Symmetrically, if \(J=\varnothing\) and \(I\ne\varnothing\), every minimal set has size \(b\). If \(I=J=\varnothing\), every selected cell must be unique in both its row and column, so this pattern exists only when \(a=b\) and then it is a perfect matching of size \(a\).

Finally suppose \(I=J=\{h\}\) with \(h\le t\). After deleting row \(h\) and column \(h\), the set \(F\) is an edge cover of
\[
K_{a-1,b-1}-M_{t-1}.
\]
It is minimal as an edge dominating set exactly when each selected edge is private at at least one endpoint, which is exactly inclusion-minimality as an edge cover. Thus the cardinalities in this fourth pattern are precisely the cardinalities of inclusion-minimal edge covers of the reduced punctured board.

The classification now follows by cases.

If \(a=1\), the nontrivial component is a star, so every minimal edge dominating set has one edge; when the graph is edgeless the unique minimal edge dominating set is empty.

Assume \(a\ge2\) and \(t=0\). If \(a=b\), the support analysis above forces every minimal edge dominating set to have size \(a\). If \(a<b\), one may take one edge in each row, giving a minimal set of size \(a\), or all \(b\) edges incident with one row, giving a minimal set of size \(b\). Hence exactly the balanced undeleted case is well-edge-dominated.

Assume next \(a=b\ge2\) and \(t\ge1\). A cyclic-shift perfect matching is a minimal edge dominating set of size \(a\). For any deleted index \(h\), the reduced graph \(K_{a-1,a-1}-M_{t-1}\) has a perfect matching and hence an inclusion-minimal edge cover of size \(a-1\), except when \((a,t)=(2,2)\), where the reduced graph has no edges. Thus the only balanced matching-deletion exception is \(K_{2,2}-M_2\cong2K_2\), which is well-edge-dominated.

It remains to take \(2\le a<b\) and \(t\ge1\). There is always a minimal edge dominating set of size \(a\): choose the edge from every row to the unmatched column \(a+1\). If \(a\ge4\), the set
\[
\{(2,1),(1,2)\}\cup\{(1,j):3\le j\le b\}
\]
meets every column, misses at least two rows, is minimal, and has size \(b\); hence these graphs are not well-edge-dominated.

Let \(a=3\). If \(t\le2\), row \(3\) has no hole, so all \(b\) edges in that row form a second minimal edge dominating set, of size \(b\). If \(t=3\), a column-covering minimal set cannot exist: omitting two rows leaves one row unable to meet its diagonal column, while omitting one row forces the edge in that row's diagonal column to be row-private, leaving the other used row to cover its own missing diagonal column, which is impossible. The remaining fourth-pattern sets are minimal edge covers of \(K_{2,b-1}-M_2\). Every such cover has exactly \(b-1\) edges: every remaining column must be covered, and no column can contain two selected edges because then both selected edges would need to be row-private, leaving no edge for the other columns. Therefore all minimal edge dominating sets have size \(3\) exactly when \(b-1=3\), giving \(K_{3,4}-M_3\); for \(b\ge5\) the sizes \(3\) and \(b-1\) differ.

Let \(a=2\). If \(t=1\), no minimal set can cover every column while omitting a row, and the fourth pattern reduces to the unique edge cover of \(K_{1,b-1}\), of size \(b-1\). Hence equality with the baseline size \(2\) occurs exactly at \(b=3\). If \(t=2\), a column-covering minimal set is impossible because either remaining row misses its diagonal column, while the reduced graph \(K_{1,b-1}-M_1\) has an isolated column and hence no edge cover. Thus only size-\(2\) minimal edge dominating sets occur for every \(b\ge2\).

These cases exhaust all parameters and prove the claim.

## Verification
The standalone checker `verify_wed_matching_deleted.py` reconstructs the graphs from the definition, exhaustively enumerates every edge subset for all \(1\le a\le b\le4\), computes all minimal edge dominating set sizes directly, and compares the observed well-edge-dominated status with the theorem. It also constructs and independently checks two different-cardinality minimal edge dominating sets for every negative case in the range \(2\le a\le12\), \(a\le b\le15\).

The replayed output is:

`ALL CHECKS PASSED; exhaustive_cases=30; subset_candidates=136249; negative_witness_cases=655; negative_witness_sets=1310; exhaustive_range=1<=a<=b<=4; witness_range=2<=a<=12,a<=b<=15`

The finite computation is a stress test only. The theorem for arbitrary parameters is proved analytically above.

## Relationship to prior work
Anderson and Kuenzel define well-edge-domination and, in their 2026 classification of the nonbipartite case, explicitly state that they had made no progress on a structural description of bipartite well-edge-dominated graphs and pose that description as Problem 1. Their paper was first public on 2026-05-30 and lists primary MSC 05C69.

The 2022 paper of Anderson, Kuenzel, and Rall already proves that stars and balanced complete bipartite graphs are well-edge-dominated, that unbalanced complete bipartite graphs with both sides of size at least two are not, and that a connected graph containing a perfect matching is well-edge-dominated only in the complete-bipartite or \(K_4\) cases. Consequently, the undeleted portion of the present classification and most balanced negative cases are prior-implied. The new content is the exact matching-deletion classification, especially the infinite unbalanced family \(K_{2,b}-M_2\) and the two isolated unbalanced exceptions, together with the punctured-board description of all minimal edge dominating sets needed to prove the iff statement.

The 2023 structural work on equimatchable bipartite graphs concerns the weaker requirement that all maximal matchings have the same size. Since every well-edge-dominated graph is equimatchable but not conversely, that classification does not imply equality of all minimal edge dominating set sizes for the matching-deletion family.

## Limitations
The result classifies only the one-matching-deletion family and does not solve the general structural problem for bipartite well-edge-dominated graphs. Literature searches found no statement equivalent to this exact family classification, but absence from the searched sources is not a proof of global novelty. In particular, older matching and edge-domination literature could contain the same family under a different rook-board or line-graph formulation. The computation checks bounded parameters and explicit obstruction witnesses; it is not used as proof for the infinite theorem.

## References
1. S. E. Anderson and K. Kuenzel, *Characterizing all nonbipartite well-edge-dominated graphs*, arXiv:2606.00802, 2026.
2. S. E. Anderson, K. Kuenzel, and D. F. Rall, *On well-edge-dominated graphs*, Graphs and Combinatorics 38 (2022), arXiv:2110.07133.
3. Y. Büyükçolak, D. Gözüpek, and S. Özkan, *Equimatchable bipartite graphs*, Discussiones Mathematicae Graph Theory 43 (2023), 77–94, doi:10.7151/dmgt.2356.
