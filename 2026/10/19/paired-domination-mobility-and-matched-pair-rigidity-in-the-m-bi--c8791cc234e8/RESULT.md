# Paired-domination mobility and matched-pair rigidity in the Möbius–Kantor graph

## Finding

Let \(G=\operatorname{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph, and let \(\mathcal P\) be the family of its minimum paired-dominating vertex sets. Then
\[
\gamma_{\mathrm{pr}}(G)=8,\qquad |\mathcal P|=684.
\]
Every \(S\in\mathcal P\) contains four vertices from each of the two bipartition classes. Four natural reconfiguration relations on \(\mathcal P\) have sharply different structures:

1. **Token jumping:** Replace one chosen vertex by any unchosen vertex. The graph \(J\) has \(3504\) edges, is connected, and has radius \(6\) and diameter \(8\). The numbers of states with eccentricities \(6,7,8\) are respectively \(216,432,36\).
2. **Token sliding:** Replace one chosen vertex by an adjacent unchosen vertex. The graph consists of \(684\) isolated states.
3. **Adjacent-pair substitution:** Remove two adjacent chosen vertices and insert two adjacent unchosen vertices, retaining paired domination. Its graph \(E\) has \(2016\) edges and components of sizes \(630\) and \(54\) singletons. The large component has radius and diameter \(6\).
4. **Partner-preserving substitution:** In addition require that the six vertices shared by the old and new sets possess a perfect matching, so that three existing guard partnerships can remain fixed. Its graph \(Q\) has \(1392\) edges and components of sizes \(432,168,30\), and \(54\) singletons. The components of sizes \(432,168,30\) have respective radius/diameter pairs \((9,10),(9,10),(4,4)\).

In both pair-substitution graphs, the \(54\) isolated configurations are **exactly** the members \(S\in\mathcal P\) for which \(G[S]\cong4K_2\). Every one of these configurations nevertheless belongs to the connected token-jumping graph. Within \(Q\), the eccentricity distributions of its three nontrivial components are \(192\) at \(9\) and \(240\) at \(10\) for the \(432\)-state component; \(96\) at \(9\) and \(72\) at \(10\) for the \(168\)-state component; and all \(30\) at \(4\) for the \(30\)-state component.

## Assumptions and scope

All graphs are finite, simple and undirected. Define the vertices of \(G\) as \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), with edges
\[
\{u_iu_{i+1},\ u_iv_i,\ v_iv_{i+3}:i\in\mathbb Z/8\mathbb Z\}.
\]
In the supplied programs, \(u_i\) has label \(i\) and \(v_i\) has label \(8+i\). A vertex set \(S\) **dominates** if every vertex lies in \(S\) or has a neighbor in \(S\). It is **paired-dominating** if, in addition, the induced graph \(G[S]\) admits a perfect matching. Such sets necessarily have even cardinality. The parameter \(\gamma_{\mathrm{pr}}\) is their minimum cardinality.

The reconfiguration graphs described above have as vertices the **unlabeled vertex sets** \(S\in\mathcal P\), not their choices of perfect matchings. For distinct \(S,T\in\mathcal P\), a token jump is characterized by \(|S\setminus T|=|T\setminus S|=1\). A slide also requires adjacency between the removed and inserted vertices. An adjacent-pair substitution requires \(|S\setminus T|=|T\setminus S|=2\), with both two-vertex differences spanning edges in \(G\). A partner-preserving substitution adds the condition that \(G[S\cap T]\) has a perfect matching. This last condition is equivalent to the possibility of leaving three matched pairs unchanged while replacing the fourth pair.

Eccentricities, radii and diameters of disconnected reconfiguration graphs are always computed **within individual connected components**. Isolated vertices are excluded from nontrivial-component eccentricity tabulations; the machine certificate marks them with sentinel \(-1\).

## Proof

**Exhaustiveness of the optimum-family construction.** Every paired-dominating set \(S\) of size \(2t\) contains some perfect matching of \(G[S]\), consisting of \(t\) disjoint edges whose endpoints are exactly \(S\). Conversely, if the endpoints of \(t\) pairwise vertex-disjoint edges dominate \(G\), their union is paired-dominating. Thus an enumeration of *all* \(t\)-edge matchings, followed by an exact closed-neighborhood coverage test, produces exactly the paired-dominating \(2t\)-sets, without omission. The standalone `verify_by_matchings.py` enumerates increasing edge-index combinations for every \(t\in\{1,2,3,4\}\) and finds \(0,0,0,684\) distinct dominating endpoint sets respectively. Therefore the minimum size is \(8\), with exactly \(684\) optima.

An independent check, `verify_by_subsets.cpp`, enumerates every vertex subset of size \(2,4,6\) or \(8\), tests domination by explicit neighborhood unions, and tests existence of a perfect matching by a terminating recurrence: choose the least selected vertex and pair it with each selected neighbor in turn; the empty set is matchable. The same cardinality counts result. The recurrence has strictly smaller inputs and exhausts every possible perfect matching.

**Bipartite balance and slide obstruction.** The graph has bipartition
\[
A=\{u_i:i\equiv0\pmod2\}\cup\{v_i:i\equiv1\pmod2\},\qquad
B=\{u_i:i\equiv1\pmod2\}\cup\{v_i:i\equiv0\pmod2\}.
\]
The exhaustive optimum list contains exactly four vertices in each class, for every one of the \(684\) states, confirmed independently by both verifiers. Sliding a vertex along an edge necessarily changes these two class counts from \((4,4)\) to either \((3,5)\) or \((5,3)\). Hence no token slide can connect two optima.

**Exact transition graphs.** Index the \(684\) optimum masks in increasing binary-mask order. Enumerate every ordered vertex deletion and insertion and retain a move precisely when its destination mask belongs to the optimum list. This generates each jump edge once. For an adjacent-pair substitution, enumerate every selected graph edge and every unselected graph edge, and test the destination mask. For partner-preserving substitution, also test the six-vertex shared mask with the same exhaustive perfect-matching predicate. This definition generates every permitted transition, because any transition uniquely specifies its deleted and inserted vertex differences. The program stores each undirected edge as an increasing pair of optimum indices.

The resulting edge counts are respectively \(3504,2016,1392\). Breadth-first search from every vertex of each finite transition graph yields the connected-component orders and within-component distances in the Finding section. Breadth-first search is exact because each transition has unit length and the full transition lists have been enumerated. The independent subset-based C++ program recomputes the transitions and every source-distance eccentricity directly from pairs of optimum masks, without using the matching-generated certificate as input.

**The frozen-state characterization.** Each optimum contains a perfect matching on its eight selected vertices, so it has at least four induced edges. Exactly \(54\) states have precisely four induced edges, and in each such state the induced graph must be \(4K_2\). Complete examination of the adjacent-pair and partner-preserving transition lists shows that their zero-degree vertices coincide exactly with these \(54\) states. No other state is isolated. In particular, the induced-edge criterion is an exact characterization, not merely a sufficient condition. The token-jumping graph, independently found connected, contains all \(54\) states.

## Verification

The complete enumeration and metric certificate is `certificate.json`. It includes all \(24\) original graph edges, all \(684\) optimum vertex sets, all three edge lists, all eccentricity arrays, and the induced-edge count of every optimum. Its indexing convention and tests are specified by the two standalone sources `verify_by_matchings.py` and `verify_by_subsets.cpp`. They implement independent descriptions of the search space: disjoint-edge matchings versus arbitrary vertex subsets with a perfect-matching recurrence.

Reproduce with Python 3 and any C++17 compiler:

```sh
python3 verify_by_matchings.py regenerated_certificate.json > regenerated_python_output.txt
c++ -O2 -std=c++17 verify_by_subsets.cpp -o verify_by_subsets
./verify_by_subsets > regenerated_cpp_output.txt
cmp regenerated_certificate.json certificate.json
cmp regenerated_python_output.txt verify_by_matchings.out
cmp regenerated_cpp_output.txt verify_by_subsets.out
```

Both programs terminate on finite state spaces and contain assertions for every principal count, component structure, and metric. The proof makes no inference from a sample or partial enumeration.

## Relationship to prior work

Haynes and Slater introduced paired domination; their general results and bounds do not enumerate the optimum configurations of this particular graph. Brešar, Henning and Rall established paired-domination bounds for Cartesian products and packing relations, not the exchange spaces studied here. Wang, Xu, Yang and Lü established distance-paired-domination numbers for generalized Petersen graphs with inner steps \(1\) and \(2\); the present graph has inner step \(3\). Results on reconfiguration of ordinary dominating sets (without the induced perfect-matching requirement) do not imply this classification, and general polynomial-time reductions between movement models do not assert equality of the state spaces on a fixed graph.

The result concerns the exact relationship between the backup-matching constraint and three levels of local flexibility (individual jumps, arbitrary adjacent-pair substitution, and partnership-preserving substitution). Existing exact paired-domination results on other families or graph orders do not imply the enumerated \(684\)-state transition geometry here. This is a best-knowledge literature comparison, not an independent claim of absolute publication priority.

## Limitations

This is a finite classification of \(\operatorname{GP}(8,3)\) only. The movement rules and the distinction between a pair of adjacent vertices and an actual preserved matching must be kept explicit. There is no general theorem for other generalized Petersen graphs or arbitrary cubic bipartite graphs. Exact enumeration supplies finite proofs but no formula for an infinite family. Some relevant publisher full texts were not accessible; an unindexed exact tabulation could overlap with these results.

## References

[1] T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206, first published 7 December 1998. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.

[2] B. Brešar, M. A. Henning and D. F. Rall, *Paired-domination of Cartesian products of graphs and rainbow domination*, Electronic Notes in Discrete Mathematics 22 (2005), 233–237. DOI: 10.1016/j.endm.2005.06.059.

[3] H. Wang, X. Xu, Y. Yang and K. Lü, *On the distance paired domination of generalized Petersen graphs P(n,1) and P(n,2)*, Journal of Combinatorial Optimization 21 (2011), 481–496; online 3 September 2009. DOI: 10.1007/s10878-009-9266-1.

[4] H. L. Bodlaender, C. Groenland and C. M. F. Swennenhuis, *Parameterized Complexities of Dominating and Independent Set Reconfiguration*, IPEC 2021, Article 9. DOI: 10.4230/LIPIcs.IPEC.2021.9; arXiv:2106.15907.
