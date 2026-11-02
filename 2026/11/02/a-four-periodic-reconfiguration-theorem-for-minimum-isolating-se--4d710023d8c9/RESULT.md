# A four-periodic reconfiguration theorem for minimum isolating sets on cycles

## Finding

For each integer \(n\ge5\), let \(C_n\) be the labelled simple cycle on \(\mathbb Z/n\mathbb Z\). A subset \(S\) is *isolating* if the vertices outside its closed neighborhood induce no edge. Let \(\mathcal I_n\) be the graph whose vertices are all *minimum-cardinality* isolating sets; two are adjacent when exactly one selected vertex is replaced by exactly one unselected vertex and the new set is also minimum isolating.

Put \(k=\lceil n/4\rceil\) and \(r=4k-n\in\{0,1,2,3\}\). Then

\[
|V(\mathcal I_n)|=\frac nk\binom{k+r-1}{r},\qquad
\deg_{\mathcal I_n}(S)=2r\quad\text{for every }S,\qquad
|E(\mathcal I_n)|=r|V(\mathcal I_n)|.
\]

If \(r=0\), then \(\mathcal I_n\) consists of four isolated vertices. If \(r>0\), then \(\mathcal I_n\) is connected. If \(r=1\), then more precisely \(\mathcal I_n\cong C_n\), so its diameter is \(\lfloor n/2\rfloor\). Thus connectivity and degree are exactly four-periodic: for positive residues modulo four the degrees are respectively \(6,4,2\), and for residue zero the graph is edgeless. The exceptional smaller cycle \(C_4\) has four singleton isolating sets and its replacement graph is \(K_4\); it is excluded from the degree assertion.

An explicit encoding is also obtained: each chosen vertex is followed clockwise by a gap of length \(4-a_i\), where \(a_i\ge0\) and the total deficit is \(\sum_i a_i=r\). Every legal replacement redistributes \(t\ge1\) deficit units between the two gaps incident to one chosen vertex, without changing the circular order of chosen vertices. This completely describes the exchange edges.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled, and vertex arithmetic is modulo \(n\). A closed neighborhood is \(N[S]=S\cup\bigcup_{v\in S}N(v)\); isolation means \(C_n[V(C_n)\setminus N[S]]\) is edgeless. A one-vertex replacement means that for two distinct sets \(S,T\), \(|S\setminus T|=|T\setminus S|=1\). There are no restrictions on the distance along the cycle between the removed and inserted vertices. All assertions above quantify over every integer \(n\ge5\), not just enumerated examples.

## Proof

**Isolation and gaps.** An edge \(\{i,i+1\}\) survives after deleting \(N[S]\) exactly when \(S\) is disjoint from the four consecutive vertices \(\{i-1,i,i+1,i+2\}\). Hence \(S\) is isolating if and only if there is no cyclic run of four unselected vertices. For a nonempty \(S\), list its \(k'\) vertices in clockwise order and let \(d_1,\ldots,d_{k'}\) be the positive clockwise spacings between successive selected vertices. The preceding condition is equivalent to \(d_i\le4\) for all \(i\). In particular \(n=\sum_i d_i\le4k'\), so \(|S|\ge\lceil n/4\rceil\). Conversely, distributing \(n\) positions into \(k=\lceil n/4\rceil\) successive positive gaps of length at most four produces an isolating set of size \(k\). Thus the known cycle isolation number is \(k\).

**Counting all minima.** Fix a minimum set. Its positive gap lengths are \(d_i=4-a_i\) with \(a_i\ge0\) and \(\sum_i a_i=4k-n=r\le3\). Conversely every weak composition \((a_1,\ldots,a_k)\) of \(r\), with an initial labelled selected vertex, constructs a minimum set. No upper bound on \(a_i\) needs to be imposed since \(r\le3\), so all gaps remain positive. Counting pairs (minimum set, distinguished selected vertex) in the two ways gives

\[
k|V(\mathcal I_n)|=n\binom{k+r-1}{r}.
\]

**All legal exchanges and degree.** For \(n\ge5\) we have \(k\ge2\). Remove a selected vertex \(x\) and denote the clockwise gaps immediately before and after it by \(d_-\) and \(d_+\). Without \(x\), those two gaps merge to a gap of length \(L=d_-+d_+=8-a_--a_+\). Since \(a_-+a_+\le r\le3\), this length is at least five. Unless the new vertex lies inside this merged gap, it remains too long for isolation. A new vertex inside the merged gap makes two positive gaps \(u\) and \(L-u\), both at most four, exactly when \(L-4\le u\le4\). There are \(9-L=1+a_-+a_+\) possible insertion sites, one of which is the original vertex \(x\). Consequently exactly \(a_-+a_+\) genuine replacements delete \(x\). Each adjacent exchange has a unique removed vertex, so summing over selected vertices yields

\[
\deg_{\mathcal I_n}(S)=\sum_{i=1}^k(a_{i-1}+a_i)=2r.
\]

The same interval argument works when \(k=2\): after deleting one selected vertex, the other is both the predecessor and successor around the full cyclic interval. The enumeration remains exact. The edge count follows from the handshake lemma.

**Connectivity.** Suppose \(r>0\). Moving a chosen vertex clockwise by one position transfers one deficit unit from the immediately preceding gap to the immediately succeeding gap. Such a move is permitted whenever the preceding gap contains at least one deficit unit: the source deficit decreases, the destination deficit increases, and since the total deficit is at most three neither new gap can become nonpositive. Similarly, the reverse move transfers a unit in the opposite direction. Hence successive unit moves can transform any weak composition of \(r\) into any other along the cyclic list of \(k\) gaps, retaining the circular identities of the selected vertices.

Moreover, starting from any gap containing a deficit unit, move its following selected vertex one step clockwise, then the next selected vertex, and so on around the entire cycle, ending with the originally preceding one. The deficit unit travels once around the gaps and returns to its starting gap. Each selected vertex has moved exactly one position clockwise, so the final set is the global translation \(S+1\), with unchanged ordered gap vector. Repeating permits every global translation. Given any two sets, align their ordered deficit vectors using unit transfers and then align the labelled initial selected vertex using these global translations. Thus all minima lie in one connected component.

If \(r=0\), every gap is exactly four; the counting formula gives exactly four sets and the degree computation gives zero. If \(r=1\), the connected graph has exactly \(n\) vertices and is two-regular, so it is the simple cycle \(C_n\). This completes the proof.

## Verification

Two independent executable checks accompany this result. `check_direct.py` constructs the closed neighborhoods directly, exhaustively enumerates all minimum isolating subsets for each \(5\le n\le22\), builds the complete one-vertex replacement graph, and checks every vertex degree, component, total count and edge count. It separately checks \(n=4\). `check_gaps.py` builds subsets from independent weak-composition encodings for every \(5\le n\le54\); it checks enumerated sizes throughout, and reconstructs adjacency, degrees and connectivity for \(5\le n\le38\). The first checker applies the original graph-theoretic definition; the second applies the gap constraints. Both execute using Python's standard library only. Their finite tests corroborate but are not substituted for the all-parameter proof.

## Relationship to prior work

Caro and Hansberg, *Partial domination—the isolation number of a graph* (first public arXiv version 2015-04-30, arXiv:1504.08055), define isolation and explicitly state \(\iota(C_n)=\lceil n/4\rceil\) in Example 2.1. The minimum size is therefore **not new**. The work does not determine the number of minimum isolating sets, their replacement degrees or connectedness.

Mynhardt and Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey* (arXiv:2003.05956, 2020), discuss single-vertex replacement and slide reconfiguration of **dominating sets**, including the jump \(\gamma\)-graph model. The present graph instead consists of minimum *isolating* sets, which can leave undominated isolated vertices, and its one-step exchanges allow nonadjacent replacement. General domination reconfiguration statements do not imply the result here.

Boyer and Goddard, *Disjoint Isolating Sets and Graphs with Maximum Isolation Number* (arXiv:2401.03933, 2024), prove existence of disjoint isolating sets and characterize equality in a general order bound. Their cycle three-partition discussion is different from enumeration and mobility of *all minima*.

The result is also distinct from the known cycle graph on inclusion-maximal independent sets: an isolating set need not be independent, and the permitted gap lengths and optimum sizes are different. The central novelty asserted here is the **complete minimum-solution count, regular-degree theorem and sharp connectivity dichotomy** for isolating sets. Searches and source inspection cannot rule out every historical equivalent under vertex-edge domination terminology.

## Limitations

No formula is claimed for the diameter of the connected residue-one or residue-two families, for nonminimum isolating sets, or for arbitrary graphs. The result is derived by elementary cyclic-gap arguments and is not presented as a consequence of computational enumeration. No independent external review has been performed. Published or unindexed equivalent formulations remain a residual originality risk.

## References

1. Y. Caro and A. Hansberg, *Partial domination—the isolation number of a graph*, arXiv:1504.08055, first public 2015-04-30. https://arxiv.org/abs/1504.08055
2. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956, first public 2020-03-12. https://arxiv.org/abs/2003.05956
3. G. Boyer and W. Goddard, *Disjoint Isolating Sets and Graphs with Maximum Isolation Number*, arXiv:2401.03933, first public 2024-01-08. https://arxiv.org/abs/2401.03933
