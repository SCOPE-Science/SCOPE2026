# Three four-cycle petals in the Shrikhande four-colouring Kempe quotient

## Finding
Let \(H\) be the Shrikhande graph with vertex set \((\mathbb Z/4\mathbb Z)^2\), with adjacent distinct vertices \((r,c)\), \((s,d)\) whenever \(r\ne s\), \(c\ne d\), and \(r+c\not\equiv s+d\pmod4\). Give four colours distinct names. A Kempe move interchanges two colours on one connected component of their induced two-colour subgraph. The full move graph \(\mathcal K_4(H)\) has exactly \(240\) vertices and \(1008\) edges, is connected, has radius \(4\) and diameter \(5\). Its eccentricities are \(4\) for \(168\) colourings and \(5\) for \(72\). The unordered-pair distance distribution at distances \(1,2,3,4,5\) is
\[
(1008,5400,13416,8280,576).
\]

Modulo global permutations of the four colour names, the quotient has \(10\) vertices and \(12\) edges and is **exactly three four-cycles sharing one common vertex**. The common vertex is the unique partition into four parity blocks. Its degree is \(6\); each other quotient vertex has degree \(2\). The quotient radius and diameter are respectively \(2\) and \(4\). The already known total of \(240\) named proper four-colourings is not claimed as new.

## Assumptions and scope
All graphs are simple and undirected. Colours are named elements of \(\{0,1,2,3\}\); equivalence in the quotient means global colour-name permutation, not graph automorphism. A Kempe move swaps exactly **one** connected component of the subgraph induced by a chosen pair of colours; a swap on the whole two-colour induced graph is legal as one move only when that subgraph is connected. The quotient omits loops caused by global colour permutations and suppresses parallel edges. Graph distances are ordinary shortest-path lengths.

## Proof
**(1) Independent colour classes.** The maximum size of an independent vertex set is \(4\). The complete list of independent four-sets comprises the following \(16\) sets, with all indices in \(\mathbb Z/4\mathbb Z\):
\[
R_i=\{(i,c):c\in\mathbb Z_4\},\quad C_j=\{(r,j):r\in\mathbb Z_4\},\quad S_k=\{(r,c):r+c\equiv k\pmod4\},
\]
\[
I_{e,f}=\{(r,c):r\equiv e\pmod2,\ c\equiv f\pmod2\},\quad e,f\in\{0,1\}.
\]
An exhaustive proof is supplied by both standalone programs: each inspects all \(\binom{16}{4}=1820\) subsets, checks all internal pairs against the explicitly constructed \(48\) edges, and finds precisely these sets. Both programs additionally test all \(\binom{16}{5}=4368\) five-vertex subsets and find none independent. An independent set of size greater than five would contain an independent five-set, so the independence number is exactly four. Thus every proper four-colouring, since the sixteen vertices occupy four independent classes, must partition the graph into four of these four-sets.

**(2) Exact covers and quotient.** The ten exact covers consist of the four pure partitions \(\{R_0,R_1,R_2,R_3\}\), \(\{C_0,C_1,C_2,C_3\}\), \(\{S_0,S_1,S_2,S_3\}\), \(\{I_{00},I_{01},I_{10},I_{11}\}\) and six mixed partitions. For each \(T\) in \(\{R,C,S\}\), two mixed partitions comprise its two even-indexed or two odd-indexed classes and the two complementary parity blocks. More explicitly,
\[
\begin{aligned}
M_{R,0}&=\{R_0,R_2,I_{10},I_{11}\}, &M_{R,1}&=\{R_1,R_3,I_{00},I_{01}\},\\
M_{C,0}&=\{C_0,C_2,I_{01},I_{11}\}, &M_{C,1}&=\{C_1,C_3,I_{00},I_{10}\},\\
M_{S,0}&=\{S_0,S_2,I_{01},I_{10}\}, &M_{S,1}&=\{S_1,S_3,I_{00},I_{11}\}.
\end{aligned}
\]
Every partition receives \(4!=24\) distinct names, yielding \(240\) colourings. A complete two-colour-component check shows that the distinct quotient edges are precisely \(I\!\!-M_{T,j}\) and \(M_{T,j}\!\!-T\) for \(T\in\{R,C,S\}\) and \(j\in\{0,1\}\), where \(I\) and \(T\) mean the corresponding pure partitions. Hence each \(I,M_{T,0},T,M_{T,1},I\) is a four-cycle, and distinct cycles meet only at \(I\). Both programs check the full list exhaustively using separate adjacency constructions.

**(3) Named distance classification.** For each of the \(240\) named colourings, inspect all six colour pairs, compute connected components in each induced two-colour graph, and add its resulting exchanges. The first program constructs the Kempe adjacency lists directly. The second instead independently recognizes legal exchanges among all \(\binom{240}{2}=28680\) pairs of named colourings. Both obtain \(1008\) unordered edges and full connectivity. Breadth-first search from each named colouring gives exactly \(168\) eccentricities \(4\) and \(72\) eccentricities \(5\), with the displayed complete pair-distance distribution. Since each program enumerates every configuration and every legal move rather than sampling them, this finite procedure proves the exact graph invariants. The \(72\) peripheral colourings are exactly the \(24\) name assignments to each of the pure \(R\), \(C\), and \(S\) partitions; the other \(168\) are central. The degree distribution is \(216\) of degree \(8\) and \(24\) of degree \(12\), with the latter corresponding to the pure parity-block partition.

## Verification
Run `python3 verify_cayley.py` and `python3 verify_latin.py` with Python 3 and no external packages. Both enumerate all states and independently construct moves; both assert the counts, eccentricities, distance histogram and quotient. The two graph models are respectively the Cayley difference-set model and the cyclic Latin-square complement. The second program also checks the explicit graph isomorphism mapping Cayley lexicographic vertex indices \(0,1,\ldots,15\) to Latin-model indices \((0,5,10,15,9,14,3,4,2,7,8,13,11,12,1,6)\). The first prints `CAYLEY_KEMPE_PASS`; the second prints `LATIN_PAIRWISE_KEMPE_PASS`. Their finite exhaustive checks establish exactly the finite claims here; no general theorem on graph families is inferred.

## Relationship to prior work
The cyclic Latin-square complement representation of the Shrikhande graph is classical (Cameron, 2010; Brouwer's graph tables). OEIS A158792 has recorded \(240\) named proper four-colourings in its historical public record since at least June 1, 2010, so that count is not new. Wanless (2004) studies cycle-switch graphs on *isotopy or main classes of Latin squares*, not the Kempe graph of four-colourings of their complementary Latin-square graph. Chakraborty, Feghali and Mahmoud (2024) prove a general Kempe-equivalence theorem for lists of at least the degree size on certain graphs, a hypothesis not met here by four colours on the six-regular Shrikhande graph. The exact ten-vertex three-petal quotient and the complete named metric are the claimed refinements.

## Limitations
This theorem concerns this single graph and this precise Kempe move. Its assertion of originality is conditional on the accessible literature comparison and does not rule out an unindexed equivalent older computation. It does not supply an asymptotic mixing-time result or treat other colour palettes, and the exact enumerations, not the chromatic polynomial alone, certify the metric. No independent scholarly validation is represented.

## References
1. OEIS, A158792, "Number of n-colorings of the Shrikhande graph," https://oeis.org/A158792 ; historical initial public record https://oeis.org/history?seq=A158792&start=10 (June 1, 2010).
2. P. J. Cameron, "The Shrikhande graph," August 26, 2010, https://cameroncounts.wordpress.com/2010/08/26/the-shrikhande-graph/ .
3. I. M. Wanless, "Cycle Switches in Latin Squares," *Graphs and Combinatorics* 20 (2004), 545–570, https://users.monash.edu.au/~iwanless/papers/cycleswapgr.GC.pdf .
4. D. Chakraborty, C. Feghali, R. Mahmoud, "Kempe equivalent list colorings revisited," *Journal of Graph Theory* 107 (2024), 410–418, https://doi.org/10.1002/jgt.23142 .
5. A. E. Brouwer, "Shrikhande," https://jaanos.github.io/tables/graphs/Shrikhande.html .
