# Rooted cup stacking of matching-deleted complete bipartite graphs

## Finding
Let \(m,n\ge3\) and \(0\le t\le\min\{m,n\}\) be integers. Let \(G_{m,n,t}\) be obtained from \(K_{m,n}\), with bipartition \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), by removing precisely \(a_jb_j\) for \(1\le j\le t\). Begin with one cup at each vertex. A legal move transfers an entire stack of \(k\ge1\) cups from \(x\) to an **occupied** vertex \(y\) at graph distance exactly \(k\). A target \(r\) is **stackable** when all cups can be brought to \(r\) by legal moves.

**Theorem (complete target profile).** For \(1\le i\le m\) and \(1\le j\le n\),
\[
\begin{aligned}
 a_i\text{ is stackable}&\iff m\le n+1+\mathbf1_{\{i\le t\}},\\
 b_j\text{ is stackable}&\iff n\le m+1+\mathbf1_{\{j\le t\}}.
\end{aligned}
\]
Consequently, the number of stackable targets is
\[
\begin{aligned}
 \mathcal S(m,n,t)={}&t\mathbf1_{\{m\le n+2\}}+(m-t)\mathbf1_{\{m\le n+1\}}\\
 &+t\mathbf1_{\{n\le m+2\}}+(n-t)\mathbf1_{\{n\le m+1\}}.
\end{aligned}
\]
In particular, \(G_{m,n,t}\) is stackable at **every** target if and only if \(|m-n|\le1\). The target-specific threshold is sharper: on \(G_{n+2,n,t}\), for every \(n\ge3\) and \(1\le t\le n\), exactly the \(t\) deleted-edge endpoints in the larger part become stackable in addition to all \(n\) vertices of the smaller part. Thus deleting one edge from \(K_{n+2,n}\) makes its larger-part endpoint stackable, even though the graph remains non-stackable as a whole.

## Assumptions and scope
All graphs are finite, undirected, simple and connected. The restrictions \(m,n\ge3\) guarantee that every pair of vertices in the same bipartition class is at distance two despite the deleted matching. More precisely, a vertex of \(A\) has distance two from all other \(A\)-vertices; its distance from every \(B\)-vertex is one except that the endpoint \(b_i\) of its deleted edge, when present, has distance three. The symmetric statement holds for vertices of \(B\). These distance claims follow because at most two opposite-side vertices are excluded as common neighbors, and each side has size at least three.

The graph \(G_{m,n,0}\) is the complete bipartite graph. Deleting a matching means the omitted edges have pairwise distinct endpoints; arbitrary nonmatching edge deletions are not covered.

## Proof
First consider a fixed target \(r=a_i\); the other case follows by interchanging the parts. In any successful sequence, the original cup at \(r\) never leaves: if the stack at \(r\) moved away, \(r\) would become empty, and no legal move could ever refill it. Group the other original cups according to their **last** move into \(r\). Each group is a disjoint *packet*; its size is the number of cups at the source of that last move and hence equals its distance from \(r\).

There are only three possible terminal sources. A neighboring vertex of \(B\) sends a packet of size one. Such a packet contains only that vertex's original cup, since the formation of any nontrivial stack requires a merger. A vertex of \(A\setminus\{r\}\) sends a packet of size two. A packet of size two contains at most one original cup from \(A\): its two original cups must initially occupy adjacent vertices (the unique first merger combines two singleton stacks), and there are no edges within \(A\). If \(i\le t\), the only other possible source is \(b_i\), at distance three, sending a packet of size three. There can be at most one such packet. It contains the original cup at \(b_i\), because an emptied vertex cannot subsequently receive a cup; thus this packet contains at most two original cups from \(A\). Every packet containing a cup from \(A\setminus\{r\}\) consequently also contains at least one original cup from \(B\). Since the packets are disjoint and there are exactly \(n\) original cups on \(B\), we obtain
\[
 m-1\le n+\mathbf1_{\{i\le t\}}.
\]
This proves the necessary inequality; it includes the undisturbed case, where no size-three packet exists.

For sufficiency, use the following elementary matching fact. Let \(X\) and \(Y\) be subsets of the two parts of a complete bipartite graph with a matching removed, and assume \(|X|\le|Y|\) and \(|Y|\ge2\). Then there is a matching saturating \(X\), provided each missing edge is part of that deleted matching. Indeed, a singleton \(x\in X\) has at least \(|Y|-1\ge1\) neighbors in \(Y\), while any subset \(X'\subseteq X\) of size at least two has the entire \(Y\) as its neighborhood: the at-most-one forbidden partner of different vertices is distinct. Hall's theorem gives the asserted matching.

If \(i>t\), the target \(a_i\) is adjacent to every \(B\)-vertex. The hypothesis \(m\le n+1\) allows a matching of \(A\setminus\{a_i\}\) into \(B\). For each matched edge \(a_jb_k\), first move the singleton at \(b_k\) onto \(a_j\), forming two cups, then move this two-cup stack to \(a_i\), at distance two. Finally, send each unmatched \(B\)-singleton directly to the adjacent target. Every move is legal and all cups arrive.

If \(i\le t\), the hypothesis \(m\le n+2\) holds. Choose two distinct vertices \(a_p,a_q\in A\setminus\{a_i\}\), possible since \(m\ge3\). Each is adjacent to \(b_i\), so move the two singleton cups successively to \(b_i\), building a three-cup stack; send this stack to \(a_i\), at distance three. There remain \(m-3\) unprocessed vertices of \(A\) and \(n-1\) unprocessed vertices of \(B\). Their sizes satisfy \(m-3\le n-1\), and \(n-1\ge2\), so the matching fact supplies a matching saturating the remaining \(A\)-vertices. Process each matched pair as a two-cup packet, and send every remaining \(B\)-singleton directly to \(a_i\). None of those remaining \(B\)-vertices equals \(b_i\), so these last moves are legal. This completes the equivalence for \(a_i\), and swapping the two bipartition classes proves it for \(b_j\).

Summing the indicator conditions yields \(\mathcal S(m,n,t)\). If \(|m-n|\le1\), every target satisfies its inequality. If, say, \(m\ge n+2\), then \(m-t\ge m-n\ge2\) vertices in the larger part are not incident to a removed edge, and each fails the necessary inequality. Thus not all targets are stackable. Finally, if \(m=n+2\), precisely the \(t\) matched endpoints on the larger side satisfy \(m\le n+2\), while every vertex on the smaller side satisfies its own inequality. All claims follow.

## Verification
The standalone Python 3 program `verify_cup.py` constructs graph distances independently, explores **every legal cup-stacking continuation** with memoization on all graphs with \(m,n\ge3\) and \(m+n\le9\), and compares each result against the theorem. It also directly executes the constructive proof, verifying every move and the final state for every predicted successful target for \(3\le m,n\le12\) and all matching sizes. The captured run `verify_output.txt` reports 346 exhaustive target cases, 666,192 examined memoized states across those cases, and 6,984 constructive witnesses. These finite calculations are checks, not the proof for unrestricted parameters.

## Relationship to prior work
Fay, Hurlbert and Tennant introduced the geodesic cup-stacking game and characterized target stackability for complete multipartite graphs; their Corollary 12 gives the \(t=0\) endpoint here, and their Lemma 10 gives a matching criterion for targets of eccentricity two. In the present family, vertices incident to deleted edges have eccentricity three, which lies outside that lemma. Gregor, Merino, Mütze and Verciani proved that graphs with Hamilton paths are stackable and recalled the complete-bipartite target dichotomy. Those theorems cover some positive global cases but not the sharp additional stackable targets on the non-Hamiltonian graph \(G_{n+2,n,t}\), whose bipartition sizes differ by two. The contribution here is the complete rooted-target classification for **all** matching deletions, including the one-edge endpoint transition.

## Limitations
The theorem applies only to deleting a matching from a complete bipartite graph and to \(m,n\ge3\). No general criterion is asserted for arbitrary bipartite graphs or for arbitrary initial cup configurations. The construction proves existence of a successful sequence but does not enumerate all successful sequences. Literature equivalence under the alternative name *frog jumping* has not been excluded exhaustively; the nongeodesic frog-jumping version is a distinct rule and cannot automatically imply the claimed exact geodesic characterization.

## References
- P. Fay, G. Hurlbert, M. Tennant, *Cup Stacking in Graphs*, arXiv:2310.06192 (first publicly posted 9 October 2023); see the definitions, Lemma 10, and Corollary 12. https://arxiv.org/abs/2310.06192
- P. Gregor, A. Merino, T. Mütze, F. Verciani, *Graphs that admit a Hamilton path are cup-stackable*, arXiv:2401.06189 (first publicly posted 11 January 2024); see Theorems 1, 6, and 19. https://arxiv.org/abs/2401.06189
