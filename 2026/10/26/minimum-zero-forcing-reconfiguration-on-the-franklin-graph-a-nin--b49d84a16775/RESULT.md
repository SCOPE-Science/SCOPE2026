# Minimum zero-forcing reconfiguration on the Franklin graph: a nine-slide detour for one jump

## Finding
Let \(F\) be the twelve-vertex Franklin graph and let \(\mathcal B\) be the family of its minimum ordinary zero-forcing sets. Then \(Z(F)=5\), the family \(\mathcal B\) contains exactly \(324\) sets, and the automorphism group of \(F\) partitions \(\mathcal B\) into exactly nine orbits, of sizes \(12,24,24,24,48,48,48,48,48\).

For the token-jumping graph \(J\), join two members of \(\mathcal B\) when they exchange one vertex. For its spanning token-sliding subgraph \(T\), require the exchanged vertices to be adjacent in \(F\). Both graphs are connected. Their exact parameters are
\[
\begin{array}{c|ccc}
 & |E| & \operatorname{rad} & \operatorname{diam}\\ \hline
J & 2910 & 5 & 5\\
T & 534 & 9 & 13
\end{array}.
\]
The token-sliding degree distribution is \(276\) vertices of degree \(3\), \(24\) of degree \(4\), and \(24\) of degree \(6\). The eccentricity distribution of \(T\) is
\[
\begin{array}{c|ccccc}
\text{eccentricity}&9&10&11&12&13\\\hline
\text{count}&24&144&60&48&48
\end{array}.
\]

The greatest token-sliding distance between configurations adjacent by a single token jump is exactly \(9\). For example, the configurations \(S=\{0,2,5,6,11\}\) and \(U=\{0,5,6,9,11\}\) are token-jump adjacent, but \(d_T(S,U)=9\). This establishes a sharp local-versus-unrestricted reconfiguration detour on a canonical cubic vertex-transitive graph.

## Assumptions and scope
All graphs are finite, undirected, simple and vertex-labeled. Put \(V(F)=\mathbb Z/12\mathbb Z\). Its edges are the cycle edges \(\{i,i+1\}\) for every residue \(i\), and the six additional chords \(\{2r,2r+5\}\) for \(0\le r<6\), with arithmetic modulo \(12\). This is the standard Franklin graph in LCF form \([5,-5]^6\). An independent second model labels the even vertices \(A_r=2r\), the odd vertices \(B_s=2s+1\), and puts \(A_rB_s\) in the graph precisely for \(s\in\{r,r-1,r+2\}\pmod 6\).

A set of initially blue vertices is an ordinary zero-forcing set if repeated application of the rule “a blue vertex having exactly one white neighbor colors that neighbor blue” colors all vertices. Minimum means cardinality \(Z(F)\). The exchange rule preserves both cardinality and the zero-forcing property at every step. \(J\) and \(T\) have the same vertex set \(\mathcal B\); graph distance is the minimum number of valid exchanges. In this result, token sliding moves a token only along an original edge to an unoccupied vertex; token jumping may exchange any two distinct vertices. All numerical assertions concern this single twelve-vertex graph, not a graph family.

## Proof
**Closure and exhaustive minimum test.** For an initial blue set \(B\), define
\[
\Phi(B)=B\cup\{w:\text{some }u\in B\text{ has }N_F(u)\setminus B=\{w\}\}.
\]
Iteration to a fixed point implements the zero-forcing rule. This is exact: an eligible force remains available unless its target has already turned blue, so applying all currently eligible forces simultaneously or taking them one at a time produces the same final closure. Adding initially blue vertices cannot destroy zero forcing. It is therefore sufficient to prove that none of the \(\binom{12}{4}=495\) four-subsets forces all vertices and to test all \(\binom{12}{5}=792\) five-subsets. Both independent algorithms enumerate these entire ranges. They obtain zero successful four-subsets and exactly \(324\) successful five-subsets. Hence \(Z(F)=5\) and \(|\mathcal B|=324\). A simple forcing witness is \(\{0,1,2,3,4\}\), with chronological forces \(2\to7,3\to10,1\to8,8\to9,7\to6,10\to11,6\to5\).

**Complete exchange construction.** For every pair of the \(324\) successful five-subsets, the first algorithm compares their intersection; the second independently generates every legal single-vertex replacement. Configurations are adjacent in \(J\) exactly when their symmetric difference consists of one removed and one inserted vertex. They are adjacent in \(T\) exactly when that pair forms an edge of \(F\). This is a complete finite enumeration of all \(\binom{324}{2}=52{,}326\) candidate pairs, not a sample. Both independently constructed adjacency graphs have respectively \(2910\) and \(534\) undirected edges. Full breadth-first searches from all \(324\) configurations reach all others. The exact eccentricities, radii and diameters follow from those searches. The unordered pair-distance histograms are recorded in the executable outputs.

**Automorphisms.** Every graph automorphism is a bijection of the twelve vertices that preserves the explicitly listed adjacency relation. A connected, adjacency-pruned backtracking enumeration constructs all such bijections and finds exactly \(48\). Acting on the \(324\) minimum forcing sets partitions them into nine orbits. The complete orbit representatives and their sizes, token-slide degrees and token-slide eccentricities, checked by breadth-first search, are:

| Representative \(S\subseteq\{0,\ldots,11\}\) | Orbit size | Slide degree | Slide eccentricity |
|---|---:|---:|---:|
| \(\{0,1,2,3,4\}\) | 48 | 3 | 13 |
| \(\{0,1,2,4,7\}\) | 48 | 3 | 10 |
| \(\{0,1,2,4,9\}\) | 48 | 3 | 11 |
| \(\{0,1,2,4,11\}\) | 48 | 3 | 12 |
| \(\{0,1,2,5,6\}\) | 48 | 3 | 10 |
| \(\{0,1,3,4,9\}\) | 24 | 6 | 10 |
| \(\{0,2,5,6,9\}\) | 24 | 4 | 9 |
| \(\{0,2,5,6,11\}\) | 12 | 3 | 11 |
| \(\{0,2,5,7,8\}\) | 24 | 3 | 10 |

These orbit sizes add to \(324\); slide eccentricity and degree are invariant under automorphisms. The independent all-source searches also give the same global extremal values without relying on orbit reduction.

**Sharp one-jump detour.** The pair \(S=\{0,2,5,6,11\}\), \(U=\{0,5,6,9,11\}\) differs only by replacing \(2\) with \(9\), so it forms one edge of \(J\). A valid nine-slide sequence is
\[
\begin{gathered}
\{0,2,5,6,11\},\ \{0,2,5,7,11\},\ \{0,2,5,6,7\},\\
\{0,3,5,6,7\},\ \{0,3,5,6,8\},\ \{0,3,5,8,11\},\\
\{0,4,5,8,11\},\ \{0,4,5,9,11\},\ \{0,4,6,9,11\},\\
\{0,5,6,9,11\}.
\end{gathered}
\]
Each successive pair is among the exhaustively verified token-slide edges. Breadth-first search from \(S\) first reaches \(U\) at layer \(9\), proving that fewer than nine slides cannot suffice. The programs repeat this comparison for every token-jump edge and find no greater slide distance, proving sharpness.

## Verification
Run with any standard Python 3 installation, in one directory, without dependencies or data files:

```
python3 verify_lcf.py
python3 verify_bipartite.py
python3 verify_orbits.py
```

The companion exact standard-output records are `verify_lcf_output.json`, `verify_bipartite_output.json`, and `verify_orbits_output.json`. `verify_lcf.py` uses the LCF graph, a bitmask implementation of parallel forcing, unordered pair comparisons and all-source graph searches. `verify_bipartite.py` independently constructs the bipartite graph, uses serial one-at-a-time forcing, generates all legal replacements, and runs independent breadth-first searches. It agrees on every common count, both complete pair-distance histograms, all eccentricity counts and the nine-slide witness. `verify_orbits.py` implements an adjacency-preserving automorphism backtracker and checks all nine orbits and their local geometry. The programs assert the critical results before printing. All three programs were executed from their packaged paths, and their recorded output was compared to their current execution output.

## Relationship to prior work
The ordinary zero-forcing process and its relation to minimum rank were developed in the foundational literature, including Barioli and collaborators (arXiv:1003.2028; first posted 2010-03-10 UTC). Geneson, Haas and Hogben (arXiv:2009.00220, 2020) introduced the minimum zero-forcing-set token-jumping graph and prove general structural results, particularly on forests and constructed families. Bong and collaborators (arXiv:2501.03642, 2025) treat token sliding and exchange, primarily for PSD and skew forcing, alongside general comparisons. None of the inspected statements yields the Franklin graph's specific complete minimum-set census, orbit classification, exchange diameters or sharp nine-slide detour. Standard Franklin graph descriptions and its aliases (six-crossed prism and Knödel graph) are given in MathWorld. An absence of matching indexed results is not a claim of universal novelty.

## Limitations
The theorem is finite and specific to the explicitly presented Franklin graph. Its exactness rests on exhaustive, fully included computation; the scripts give a reproducible finite proof, not a closed-form parametrization for a broader graph family. The literature comparison does not eliminate possible unindexed or unpublished equivalent enumerations. No independent external validation or publication-priority certification has been performed.

## References
1. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028 (2010), https://arxiv.org/abs/1003.2028 .
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020), https://arxiv.org/abs/2009.00220 .
3. N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642 (2025), https://arxiv.org/abs/2501.03642 .
4. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html .
5. E. W. Weisstein, *Knödel Graph*, MathWorld, https://mathworld.wolfram.com/KnoedelGraph.html .
