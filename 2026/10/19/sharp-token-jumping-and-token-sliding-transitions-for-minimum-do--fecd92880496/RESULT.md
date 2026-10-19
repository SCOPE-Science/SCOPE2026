# Sharp token-jumping and token-sliding transitions for minimum domination in Kneser pair graphs

## Finding

Let \(H_n=\operatorname{KG}(n,2)\), for each integer \(n\ge5\). Its vertices are the two-element subsets of \([n]\), with adjacency precisely for disjoint subsets. A dominating set is a vertex set meeting the closed neighborhood of every vertex. A *minimum* dominating set has cardinality \(\gamma(H_n)\). For the two graphs \(\mathcal J_n\) and \(\mathcal S_n\) whose vertices are the minimum dominating sets, join two sets when their symmetric difference consists of a removed vertex and an inserted vertex; in \(\mathcal S_n\), additionally require the two exchanged vertices to be adjacent in \(H_n\). Thus \(\mathcal J_n\) is token jumping and \(\mathcal S_n\) is token sliding. A single move always preserves domination and cardinality.

The following classification of minimum sets is due to Ivančo and Zelinka (1993): \(\gamma(H_n)=3\), and a minimum set, viewed as three edges of \(K_n\), is exactly a triangle or a three-edge matching. Accordingly write \(\mathcal T_n\) for its \(\binom n3\) triangle configurations and \(\mathcal M_n\) for its \(15\binom n6\) matching configurations. The contribution here is the **complete connected-component structure** of both minimum-set exchange graphs:

1. **Token jumping.** For \(n=5\), the graph is \(10K_1\); for \(n=6\), it is \(35K_1\). For every \(n\ge7\), the graph is the disjoint union of \(\binom n3\) isolated triangle vertices and **one connected** graph induced by \(\mathcal M_n\). Every matching configuration in this latter component has degree
   \[3\left(\binom{n-4}{2}-1\right).\]
2. **Token sliding.** For \(5\le n\le7\), the graph consists entirely of \(\binom n3+15\binom n6\) isolated vertices (with the convention \(\binom n6=0\) for \(n<6\)). At \(n=8\) the graph is exactly
   \[56K_1\ \sqcup\ 105K_4.\]
   For every \(n\ge9\), the graph is the disjoint union of \(\binom n3\) isolated triangle vertices and **one connected** graph induced by \(\mathcal M_n\). Every matching configuration has degree
   \[3\binom{n-6}{2}.\]

In particular, the sharp connectivity thresholds **within the matching family** are \(n=7\) for token jumping and \(n=9\) for token sliding. The triangle configurations are frozen for either rule at all orders. In contrast, for the order-eight sliding graph, all nontrivial components are cliques of size four and no two of those cliques can communicate.

The complete number of edges in the jumping graph is
\[\frac{45}{2}\binom n6\left(\binom{n-4}{2}-1\right),\]
and in the sliding graph it is
\[\frac{45}{2}\binom n6\binom{n-6}{2}.\]
(The expressions are integers; each is zero when its matching-layer degree is zero.)

## Assumptions and scope

The ground set is \([n]=\{1,\dots,n\}\) with arbitrary integer \(n\ge5\). The graph \(H_n\) is simple and finite. A vertex of \(H_n\) is identified with an unordered edge of the complete graph \(K_n\); \(H_n\)-adjacency means **edge disjointness** in \(K_n\). An optimal configuration contains exactly three distinct vertices of \(H_n\), not three vertices of \(K_n\). Configurations have no token labels; graph edges are undirected. In token sliding only the removed and inserted vertices of \(H_n\) must be adjacent. Intermediate states after a two-move simulation must themselves remain minimum dominating sets. Connectedness claims are only about the matching-induced subgraph, because triangle states are isolated.

## Proof

**Step 1: the already-known minimum-set classification.** For completeness we reproduce the simple criterion from Ivančo--Zelinka (1993, Theorem 1), and do not claim it as new. Every pair of distinct selected edges of \(K_n\) fails to dominate \(H_n\): take one endpoint from each edge outside their overlap, obtaining an unselected edge intersecting both. If three selected edges are pairwise disjoint, any other edge of \(K_n\) meets at most two, so their vertices dominate. If they are the three edges on a common triple of vertices, any edge meeting all three is one of those three, so they also dominate. Conversely, for three selected edges with a pair sharing a vertex, consider their third edge. If the three form a triangle we are done. Otherwise an unselected edge meeting all three exists: for a three-star take the center and a vertex outside its four used vertices (possible as \(n\ge5\)); if the third edge avoids the center take the center with an endpoint of the third edge not already giving one of the original edges; the path and disconnected-pair cases supply such an endpoint (or equivalently the explicit case analysis in Ivančo--Zelinka, Theorem 1). Consequently the only optimal configurations are triangles and three-matchings. There are \(\binom n3\) triangles and \(\binom n6(6-1)!!=15\binom n6\) three-matchings.

**Step 2: isolated triangles.** Two distinct triangles in \(K_n\) cannot share two edges: any two edges of a triangle fix the third. A triangle cannot share two edges with a matching: its two shared edges would meet. Since any exchange of one vertex in a three-set preserves two selected edges, no triangle configuration has a jumping neighbor. Sliding is a subgraph of jumping, so triangles are isolated there too.

**Step 3: exact local degrees on matchings.** Fix a matching \(M\) consisting of three pairwise disjoint edges of \(K_n\), and select one of its three edges \(e\) for replacement. The other two edges occupy four endpoints, leaving \(n-4\) free endpoints. Under jumping, every new edge among these \(n-4\) endpoints except the old \(e\) works; thus there are \(\binom{n-4}{2}-1\) choices for each of three distinct removed edges. Under sliding in \(H_n\), the new edge must be disjoint also from \(e\), so both endpoints must be among the \(n-6\) unmatched vertices, giving \(\binom{n-6}{2}\) choices per removed edge. Different removed edges lead to different neighboring three-matchings. This proves regular degrees and, by the handshake lemma, both edge formulas.

**Step 4: jumping connectedness of matchings whenever \(n\ge7\).** In a size-three matching, at least one ground vertex is unmatched. We show how to insert each edge of any target matching, retaining any target edges already installed. Suppose \(uv\) is a target edge not yet present; because target edges form a matching, neither endpoint lies on a previously fixed edge. If both are unmatched, replace one unfixed matching edge by \(uv\). If precisely one is unmatched, replace the unfixed edge containing the other endpoint by \(uv\). If both lie on different unfixed matching edges \(ua\) and \(vb\), choose any currently unmatched ground vertex \(w\), replace \(ua\) by \(wa\), then replace \(vb\) by \(uv\). These are legal jumping moves and do not disturb fixed target edges. If \(uv\) is already selected, keep it. Iterating over the three target edges reaches the target matching; this argument works with exactly one unmatched vertex. Hence the jumping matching graph is connected for all \(n\ge7\). At \(n=6\) every three-matching is perfect and Step 3 gives degree zero. For \(n=5\) no such matching exists.

**Step 5: sliding at the small boundary.** Step 3 makes all matching vertices isolated at \(n=6,7\). At \(n=8\), every matching uses six of the eight ground vertices and has exactly one pair of unmatched vertices. Any sliding move replaces a selected pair with the pair of previously unmatched vertices. Therefore it preserves the partition of all eight ground vertices into four unordered pairs, while changing which one of the four pairs is unselected. Conversely, all four choices of the omitted pair are mutually reachable in one sliding move. The number of partitions of eight labeled elements into four pairs is \((8-1)!!=105\), giving precisely \(105K_4\). Together with \(\binom83=56\) triangle isolates this proves the claimed decomposition.

**Step 6: sliding connectedness when \(n\ge9\).** We simulate every jumping move of Step 4 using at most two legal sliding moves. For a jump replacing \(e=ab\) with an edge \(f\) disjoint from \(e\), the jump itself is a slide in \(H_n\). Otherwise \(f\) shares exactly one endpoint with \(e\), say \(f=az\) with \(z\) currently unmatched. Since \(n-6\ge3\), choose two distinct currently unmatched vertices \(x,y\) other than \(z\). First replace \(ab\) by \(xy\): this is a slide and leaves a matching. Next replace \(xy\) by \(az\): this is also a slide, because the edges are disjoint, and it returns the other two matching edges unchanged. The intermediate configuration remains a three-matching and hence minimum dominating by Step 1. Every jumping path therefore lifts to a sliding path. Step 4 establishes connectedness for all \(n\ge9\).

The six steps exhaust all \(n\ge5\), and each component and degree assertion follows. \(\square\)

## Verification

Two separately structured standalone programs are supplied. `verify_direct.py` constructs all vertices of \(H_n\), computes every closed neighborhood, tests all three-subsets for domination without invoking the structural classification, and constructs the token-jumping and token-sliding exchange graphs with breadth-first component enumeration for \(5\le n\le10\). `verify_constructive.cpp` instead constructs the two classified optimum families directly, checks that every constructed configuration dominates, reconstructs each exchange graph, and checks its claimed degree and components for \(5\le n\le11\). Build and run with

```sh
python3 verify_direct.py > direct_output.json
g++ -std=c++17 -O2 verify_constructive.cpp -o verifier
./verifier > constructive_output.txt
```

The exact embedded output files are from successful runs; no external packages beyond the Python standard library and a C++17 compiler are used. The programs verify the finite boundary cases and provide independent checks on the formulas. The **proof for all integers** \(n\ge5\) is Steps 1--6, not an inference from numerical experiments.

## Relationship to prior work

Ivančo and Zelinka (1993, Theorem 1, pp. 147--148) already determined the domination number and the complete triangle/matching classification for \(\operatorname{KG}(n,2)\). Nothing about that classification is asserted as new here. Fricke, Hedetniemi, Hedetniemi and Hutson (2011) introduced minimum-dominating-set \(\gamma\)-graphs under adjacent token exchange, and Suzuki, Mouawad and Nishimura (2014) studied the distinct token-addition/removal model with a cardinality allowance. Cornet and Torres (2023/2024) explicitly cite the Ivančo--Zelinka classification and investigate tuple domination, not the two exchange-graph decompositions here. The added content is the sharp, three-stage sliding transition (frozen matchings, \(K_4\) components, then connected matchings), paired with the earlier jumping threshold and exact regularity formulas.

The statement is not implied by the minimum-set classification alone without an additional analysis of legal exchanges. It also differs from token sliding of arbitrary independent sets of the same Kneser graph: a minimum dominating set need not be independent, and imposing domination changes the admissible configurations. In particular, the minimum dominating triangles are immobile even though the independent-set reconfiguration problem admits other intermediate configurations.

## Limitations

The result does not determine exact diameters of the nontrivial connected components for general \(n\), nor their Hamiltonicity. It concerns exactly minimum cardinality and **single-vertex** exchanges; multi-vertex simultaneous exchanges or moves allowed to pass through nonoptimal states are different models. The known 1993 classification is a premise with its proof reproduced for completeness. Literature searching cannot rule out an unindexed equivalent exchange classification; independent priority review remains outstanding. The exhaustive check covers bounded orders only, while the quantified statements rest on the combinatorial argument above.

## References

- J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica **118** (1993), 147--152, Theorem 1, DOI: `10.21136/MB.1993.126050`. Open primary text: `https://dml.cz/bitstream/handle/10338.dmlcz/126050/MathBohem_118-1993-2_3.pdf`.
- G. H. Fricke, S. M. Hedetniemi, S. T. Hedetniemi and K. R. Hutson, *γ-Graphs of Graphs*, Discussiones Mathematicae Graph Theory **31** (2011), 517--531, DOI: `10.7151/dmgt.1562`.
- A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:`1401.5714`, first version posted 2014-01-22; available at `https://arxiv.org/pdf/1401.5714`.
- M. G. Cornet and P. Torres, *k-tuple domination on Kneser graphs*, arXiv:`2308.15603` (2023; revised 2024), notably the discussion after Lemma 10 and Theorem 11; available at `https://arxiv.org/pdf/2308.15603`.
