# A mixed token-slide phase and a connected jump metric for minimum decycling sets of \(GP(7,2)\)

## Finding
For the generalized Petersen graph \(G=GP(7,2)\), the decycling number is \(4\), and exactly \(70\) minimum decycling sets exist. Every one is independent and its complement is an induced spanning tree on ten vertices. The token-slide reconfiguration graph on those minimum sets is exactly
\[
14K_1\;\sqcup\;14K_2\;\sqcup\;7P_4,
\]
where \(P_4\) is a path on four vertices. In contrast, the token-jump reconfiguration graph is a connected four-regular graph on \(70\) vertices with \(140\) edges, radius \(6\), diameter \(7\), and eccentricity counts \(56\) at six and \(14\) at seven. This is the first coexistence of frozen and movable minimum decycling sets under token sliding within the initial \(GP(n,2)\) sequence \(n\geq5\): at \(n=5\) every optimal state is frozen, while at \(n=6\) the slide graph is connected.

## Assumptions and scope
All graphs are finite, simple and undirected. For each integer \(n\geq5\), set \(V(GP(n,2))=\{u_i,v_i:i\in\mathbb Z/n\mathbb Z\}\) with edges \(u_i u_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with indices modulo \(n\). A decycling (feedback vertex) set \(S\) is a vertex set such that the induced subgraph on \(V\setminus S\) is a forest. A minimum set has minimum cardinality. A token jump from \(S\) to \(S'\) requires \(|S\setminus S'|=|S'\setminus S|=1\); a token slide additionally requires that the removed and inserted vertices be adjacent in the original graph. Both endpoints must be minimum decycling sets. All exact graph metrics in the claim concern only \(GP(7,2)\), with auxiliary classifications of the smaller \(n=5,6\) cases. No assertion is made for all \(n\geq8\).

## Proof
**Lower bound and induced trees.** The cubic graph \(GP(7,2)\) has \(14\) vertices and \(21\) edges. If \(S\) has \(k\) vertices and \(e(S)\) internal edges, the complement has exactly \(21-3k+e(S)\) edges. A forest on \(14-k\) vertices has at most \(13-k\) edges. Thus \(21-3k+e(S)\leq13-k\), or \(2k\geq8+e(S)\). Therefore \(k\geq4\). When \(k=4\), it follows that \(e(S)=0\), and the complement has nine edges on ten vertices and is a tree.

**Exhaustive state-space determination.** Use the canonical labeling \(u_i=i\) and \(v_i=7+i\) for \(0\leq i<7\). The first embedded verifier enumerates every one of the \(\binom{14}{4}=1001\) four-vertex subsets and applies a disjoint-set union cycle test to the nine-or-more retained edges. Exactly \(70\) subsets yield forests. An independent verifier generates all \(185\) distinct simple-cycle vertex masks and accepts a candidate if and only if it meets every such mask. It obtains the same \(70\) states. Five orbit representatives under the graph's dihedral rotations and reflections are, in the above numeric labeling,
\[
\{1,3,5,7\},\quad \{2,4,7,8\},\quad \{2,5,7,8\},\quad \{1,4,7,10\},\quad \{3,7,8,11\}.
\]
Their orbits are disjoint and each has size \(14\); together they exhaust the accepted subsets. In particular the lower bound is attained, and the preceding counting argument proves all accepted complements are induced trees.

**Exact move graphs.** For each ordered pair of distinct accepted sets, the verifiers compute the two one-element set differences. Their sizes are both one exactly when the pair is a legal token jump; checking adjacency between the exchanged vertices decides token sliding. The first verifier builds both undirected graphs by all unordered pairs, and the second independently builds them by generating all possible exchanges from each state. Breadth-first component enumeration gives the token-slide component sizes: fourteen of size one, fourteen of size two, and seven of size four. Degree checks show the four-vertex components have degree sequence \((1,1,2,2)\), so they are all \(P_4\). The token-slide graph has \(35\) edges. Every token-jump vertex has degree four, and its graph has \(140\) edges and one component; breadth-first search from all \(70\) vertices gives eccentricity distribution \(56\) at six and \(14\) at seven, proving its radius and diameter.

**First coexistence in the initial sequence.** Identical exhaustive definitions and the same two independently implemented methods applied to \(GP(5,2)\) and \(GP(6,2)\) give respectively \(20\) optimal triples with token-slide graph \(20K_1\), and \(120\) optimal quadruples with a connected token-slide graph on \(120\) vertices. Hence seven is the first parameter \(n\geq5\) where frozen and movable optimal states coexist. This is a finite initial-sequence assertion, not a monotonicity statement for larger parameters.

## Verification
The package includes `direct_check.js` and `cycle_check.js` and their exact recorded outputs. From a directory containing these artifacts, run `node direct_check.js` and `node cycle_check.js` (Node.js with ordinary standard-library APIs). Each verifies its own expected counts and terminates in `DIRECT_CHECK_PASS` or `CYCLE_CHECK_PASS` only if every relevant assertion succeeds. The first algorithm screens complement acyclicity with a disjoint-set union; the second independently enumerates simple cycles and checks hitting sets. Both reconstruct all token moves and execute exact breadth-first searches. The complete domains are enumerated, rather than inferred from a sample; graph radius and diameter follow from exhaustive distances within the finite jump graph. The programs and outputs are the computational certificates of the exact finite classification, not evidence of any infinite-family result.

## Relationship to prior work
Bau and Beineke studied the decycling number, gave degree-based lower bounds and discussed the Petersen graph; the public arXiv version is dated 19 March 2007. Wei and Li (2013) and Gao et al. (2015) studied decycling numbers of generalized Petersen graphs. These establish or approach scalar cardinality questions, not the specific optimal-set move graphs classified here. A 2019 compilation of reconfiguration questions explicitly discusses feedback-vertex-set token jumping, stable-tree decomposition exchanges and maximal induced-tree movement; these are prior formulations of the mobility problem, not new move notions. In particular, the known median-based stable-tree operation is **not** claimed as original. The numerical reconfiguration classifications above are a separate, narrower graph-specific claim.

## Limitations
This is an exact finite classification for one natural fourteen-vertex graph with a checked two-case minimality comparison, not a theorem about all generalized Petersen graphs. It does not establish historical priority over unpublished tables or inaccessible complete texts. The 2013 and 2015 generalized-Petersen papers were compared using publicly accessible bibliographic records and abstracts, but their complete texts were not accessible here. Two independently implemented exhaustive verifiers support the finite result, while independent mathematical peer review has not been performed.

## References
- S. Bau and L. W. Beineke, *The Decycling Number of Graphs*, arXiv:math/0703544, publicly submitted 19 March 2007, https://arxiv.org/abs/math/0703544 .
- E. L. Wei and Y. F. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, Acta Mathematica Sinica, Chinese Series 56 (2013), 211–216, DOI:10.12386/A2013sxxb0022, https://actamath.cjoe.ac.cn/Jwk_sxxb_cn/EN/10.12386/A2013sxxb0022 .
- L. Gao, X. Xu, J. Wang, D. Zhu and Y. Yang, *The decycling number of generalized Petersen graphs*, Discrete Applied Mathematics 181 (2015), 297–300, DOI:10.1016/j.dam.2014.09.005 .
- *CoRe 2019: Open Problems*, sections by Akira Suzuki, František Kardoš and Kunihiro Wasa, https://hoanganhduc.github.io/events/CoRe2019/CoRe_2019_Open_Problems.pdf .
