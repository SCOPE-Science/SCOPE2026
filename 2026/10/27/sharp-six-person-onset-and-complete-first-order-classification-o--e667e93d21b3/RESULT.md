# Sharp six-person onset and complete first-order classification of adverse capacity effects in the Netflix game

## Finding

Consider the exact-nomination binary public-goods game. Let \(m_k(G)\) be the smallest number of account purchasers among pure Nash equilibria when all players have nominal sharing capacity \(k\ge1\). **The first connected networks for which greater sharing capacity worsens this best equilibrium have six vertices.** The complete first-order boundary consists of exactly eight nonisomorphic graphs, all with the reversal \(m_2(G)=2<m_3(G)=3\), totaling 1,330 labeled graphs out of 26,704 connected labeled graphs on six vertices. No connected graph with at most five vertices has any reversal for positive integer capacities. On six vertices the reversal can occur only at capacity two to three.

In the following canonical encoding, vertices are \(\{0,1,\ldots,5\}\). List unordered vertex pairs \((i,j)\) with \(0\le i<j\le5\) in lexicographic order, assigning them bit positions \(0,1,\ldots,14\). For an undirected labeled graph, its code is the sum of \(2^h\) over its edge positions \(h\). A graph's **canonical code** is the minimum code among all \(6!\) vertex permutations. The complete list of canonical codes and numbers of labeled graphs is:

| Canonical code | Number of edges | Labeled graphs |
| ---: | ---: | ---: |
| 121 | 5 | 90 |
| 693 | 6 | 360 |
| 127 | 7 | 180 |
| 954 | 7 | 180 |
| 639 | 8 | 60 |
| 703 | 8 | 360 |
| 1759 | 9 | 90 |
| 4060 | 9 | 10 |

The five-edge graph with code 121 is the double-star: two degree-three centers are adjacent, and each center is joined to two degree-one leaves. It is the **unique sparsest isomorphism class** in the obstruction layer. The existence of the double-star paradox was already shown in the originating study; the sharp minimality and exhaustive eight-class census are the contribution here.

## Assumptions and scope

Let \(G=(V,E)\) be a connected, finite, simple undirected graph of order \(n\ge2\). The players have binary purchasing actions. A purchaser at vertex \(v\) nominates exactly \(\kappa_k(v)=\min\{k,d_G(v)\}\) distinct neighbors. A player receives the good if it purchases or is nominated by at least one purchaser. The good has value one, purchase cost \(c\) with \(0<c<1\), and further nominations confer no additional utility. Nominating is costless, and each player chooses its own nomination list. The comparison is over *all* pure strategy Nash equilibria, not one selected equilibrium.

A buyer set \(D\subset V\), with nonbuyer complement \(P=V\setminus D\), is feasible precisely if each \(v\in D\) can nominate \(\kappa_k(v)\) distinct neighbors in \(P\) and every vertex of \(P\) receives at least one such nomination. Write \(m_k(G)=\min\{|D|:D\text{ is feasible}\}\). Existence of a feasible set is guaranteed in this game; in fact the checker exhibits one for every considered connected graph. Capacities \(k\ge n-1\) coincide with full nomination and no further capacity changes are possible.

## Proof

**Step 1: Exact graph-theoretic characterization.** In a Nash outcome every nonbuyer must be nominated, because otherwise paying cost \(c<1\) for access yields a profitable deviation. Conversely, a buyer cannot be nominated by a buyer: it could stop purchasing, retain access and save \(c>0\). Each buyer's nomination quota is mandatory, and its own utility is unaffected by its choices of nominees. Therefore, when the stated two nomination requirements hold, no individual can improve its own payoff by changing purchasing action or nomination choice. The converse holds as well. Equivalently, the selected nomination edges form a spanning bipartite \(DP\)-Nash subgraph, with exact source-side degrees and positive target-side degrees. This is the characterization in the cited source; the proof here makes its use explicit.

**Step 2: Exhaustive finite decision procedure.** Fix an ordered vertex set \(\{0,\ldots,n-1\}\). There are precisely \(2^{\binom n2}\) simple labeled graphs, indexed by the edge-bit masks. Connectivity is decided by reachability from vertex zero until closure. For each connected graph and each positive integer \(1\le k\le n-1\), test every nonempty proper buyer set \(D\). For each purchaser \(v\), enumerate all subsets of \(N_G(v)\cap P\) having cardinality exactly \(\min\{k,d_G(v)\}\). If such subsets do not exist, reject \(D\). Otherwise recursively form the exact set of unions of those nominee subsets; accept \(D\) if and only if at least one union is all of \(P\). This is a finite existential test over **every possible nomination profile**, with no sampling or heuristic inference. The minimum cardinality among accepted sets is exactly \(m_k(G)\), by Step 1.

**Step 3: Complete graph scan and identification of the first reversal layer.** Apply Step 2 for every graph on \(2\le n\le6\). The numbers of connected labeled graphs obtained at orders two through six are, respectively, \(1,4,38,728,26704\), an independent consistency check against the known connected-graph enumeration. None of the graphs at orders two through five has \(m_{k+1}(G)>m_k(G)\). Exactly 1,330 connected labeled six-vertex graphs have such an increase. For **each** such graph the complete capacity scan confirms that the only increase occurs at \(k=2\) to \(k=3\), and that \(m_2(G)=2\), \(m_3(G)=3\). Capacities beyond \(n-1\) add nothing, so this exhausts all positive integers.

**Step 4: Exact isomorphism quotient.** For each of the 1,330 labeled reversal graphs, form every edge-bit mask induced by all \(6!=720\) permutations and take the minimum. The resulting canonical-code frequency map is exactly the eight pairs displayed under Finding. A canonical code is invariant under relabeling. Conversely, two graphs sharing this minimum code have relabelings to the same labeled graph, hence are isomorphic. Consequently the eight frequencies are precisely the labeled orbit sizes, not merely a list of example graphs. Their sum is \(90+360+180+180+60+360+90+10=1330\). The unique class with only \(n-1=5\) edges is code \(121\). Its graph has edges \(\{01,04,05,12,13\}\), where concatenated digits denote unordered pairs. This proves its double-star identity and unique sparsity. All steps are implemented, with independent assertions, in `netflix_capacity_census.py`.

## Verification

Run `python3 netflix_capacity_census.py` with Python 3.9 or newer; no third-party packages are required. The checker performs integral, exhaustive enumeration of every connected labeled graph with orders two through six, every relevant integer capacity, every candidate buyer set, every admissible exact nominee subset, and every permutation necessary to canonicalize each observed reversal graph. Its assertions verify the graph counts, absence of smaller reversals, exact first-order reversal values, 1,330 witnesses, eight canonical classes and their multiplicities. An execution of the embedded program completed with `PASS` and printed the eight expected class counts.

This is a **finite exhaustive computation**, not an inductive theorem for unbounded graph order. The exhaustive state space is proved to cover the theorem's finite domain through the bit-mask representation and exact nomination-set correspondence in Steps 1–4. No floating-point arithmetic, external graph database, timeout inference, or extrapolation occurs.

## Relationship to prior work

Gerke, Gutin, Hwang and Neary [1] introduced the exact-capacity Netflix game and proved Nash existence. Their Example 2 already gives the same six-person double-star as a counterexample to the intuition that allowing more sharing can only help. Therefore neither the counterexample itself nor the existence of nonmonotonic efficiency is new. Their comparative-statics bounds are weaker than a classification of minimum purchaser counts over **all** graphs at the first possible order. The present contribution is the exhaustive proof that no smaller connected network permits an adverse capacity change, the exact eight isomorphism classes at the threshold, their labeled multiplicities and the uniqueness of the sparsest topology.

Gutin, Neary and Yeo [2] examine the exact-capacitated domination formulation and uniqueness/complexity of buyer sets, not the complete small-order reversal layer. Existing formulas for buyer-count spectra on specific graph families, such as balanced complete bipartite graphs, can account for some listed examples but not this all-connected-graph classification.

## Limitations

Only connected simple graphs on at most six vertices and **uniform positive integer capacities** are classified. Arbitrary heterogeneous capacities, multiplayer extensions with nonbinary provision, directed networks, and graph orders seven or higher are not addressed. The result concerns the most efficient Nash equilibrium under exact mandatory nomination and says nothing about equilibrium selection, welfare under a different payoff specification, or efficiency of all equilibria. Searches and source comparisons cannot exclude an unknown equivalent earlier classification; no independent audit or independent bibliographic validation has been performed.

## References

[1] S. Gerke, G. Gutin, S.-H. Hwang and P. R. Neary, *Public goods in networks with constraints on sharing*, arXiv:1905.01693, first public version 5 May 2019, https://arxiv.org/abs/1905.01693 (especially Example 2, Section 3.2, Section 4 and Appendix C).

[2] G. Gutin, P. R. Neary and A. Yeo, *Exact capacitated domination: on the computational complexity of uniqueness*, arXiv:2003.07106, 16 March 2020, https://arxiv.org/abs/2003.07106 (especially Sections 1–3).
