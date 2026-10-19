# A cubic Cayley separation for eternal multiple-guard domination on the Pappus graph

## Finding
Let \(P\) be the eighteen-vertex Pappus incidence graph. Under the standard multiple-guard eternal-domination game, in which any number of guards may each move at most one edge after each attack, the exact parameters are
\[
\gamma(P)=5,\qquad \gamma^m_\infty(P)=6.
\]
There are exactly eighteen ordinary minimum dominating five-sets. In each of them exactly one unoccupied vertex cannot be defended while retaining five guards. These uniquely undefendable vertices are all different. There are exactly \(423\) dominating six-sets, and **every one** can defend **every** unoccupied vertex in one simultaneous legal move ending in another dominating six-set. Indeed, the number of possible destination configurations for a given six-set and attack ranges from \(25\) to \(81\). Thus all \(423\) six-sets are indefinitely winning positions. This is a cubic, vertex-transitive, nonabelian Cayley example with a strict ordinary/eternal domination gap.

## Assumptions and scope
All arithmetic in the graph definition is over \(\mathbb F_3\). Vertices are the nine points \(p_{x,y}\) and the nine nonvertical lines \(\ell_{m,b}\), indexed by \(x,y,m,b\in\mathbb F_3\). Join \(p_{x,y}\) and \(\ell_{m,b}\) exactly when \(y=mx+b\). Thus there are eighteen vertices, twenty-seven edges, and degree three everywhere. Guards occupy distinct vertices. Each attack targets a currently unoccupied vertex. In response each guard may remain stationary or move along one edge; no two guards may finish together, and at least one must arrive at the attacked vertex. The resulting placement must dominate all vertices. A placement wins eternally if it can answer every finite sequence of adaptive attacks. The parameter \(\gamma^m_\infty\) minimizes guard count among such placements. Counts concern labeled subsets of this specified graph (not colorings or arrangements of distinguishable guards).

## Proof
**Ordinary domination lower bound and all minimum placements.** Suppose \(S\) has \(k\) vertices, of which \(a\) are points and \(k-a\) are lines. Covering the unselected points and lines requires, respectively,
\[
3(k-a)\geq 9-a,\qquad 3a\geq9-(k-a).
\]
For \(k=4\), these inequalities force simultaneously \(a\leq1\) and \(a\geq3\), a contradiction. For \(k=5\), they force \(a=2\) or \(a=3\). If \(a=2\), the two chosen points must cover all six unselected lines. Hence they share no incident line, which implies they share their first coordinate \(x\). Write these points as the two members of the vertical fiber other than \(p_{x,z}\). The three selected lines must then be the remaining three lines, exactly the three lines through \(p_{x,z}\), and these do dominate every point outside the fiber. Therefore the nine possibilities are precisely
\[
S_{x,z}=\{p_{x,y}:y\ne z\}\ \cup\ \{\ell_{m,z-mx}:m\in\mathbb F_3\},\qquad x,z\in\mathbb F_3.
\]
The incidence-duality automorphism \(D:p_{x,y}\mapsto\ell_{x,-y},\ \ell_{m,b}\mapsto p_{m,-b}\) interchanges the two bipartition classes, providing the remaining nine distinct five-sets. In particular \(\gamma(P)=5\) and there are exactly eighteen minima.

**A fatal attack on every five-set.** For the representative \(S_{0,2}=\{p_{0,0},p_{0,1},\ell_{0,2},\ell_{1,2},\ell_{2,2}\}\), the attack on \(p_{0,2}\) cannot be defended by moving five guards to any of the eighteen minimum dominating sets. This is checked by the complete explicit finite enumeration below: for each destination five-set, test for a perfect matching in the bipartite graph joining each initial guard to its allowed destination vertices (the starting vertex and its three neighbors). All eighteen tests fail. The affine-incidence automorphisms
\[
F(p_{x,y})=p_{x+1,y+x},\quad F(\ell_{m,b})=\ell_{m+1,b-m-1},
\]
\[
G(p_{x,y})=p_{x,y+1},\quad G(\ell_{m,b})=\ell_{m,b+1},
\]
with \(D\) act transitively on the eighteen five-sets. Hence every minimum placement has a fatal attack. The complete examination furthermore determines exactly one fatal attack for each five-set: for \(S_{x,z}\) it is \(p_{x,z}\), and for \(D(S_{x,z})\) it is \(\ell_{x,-z}\). Thus the fatal-attacked vertices are all eighteen vertices, exactly once. No five-guard placement wins eternally.

**Six-guard upper bound and completeness of finite verification.** Enumerate the \(\binom{18}{6}=18{,}564\) labeled six-subsets, retaining those whose closed neighborhoods cover every vertex. Exactly \(423\) remain. For every ordered pair of retained configurations \((A,B)\), test whether there exists an injective assignment of the six positions of \(A\) to the six positions of \(B\), each assignment staying put or traversing a single graph edge. One verifier enumerates injections recursively; the other uses a dynamic program on the subsets of six destination positions. The two algorithms and different graph constructions give the same counts: \(72{,}891\) legal ordered configuration shifts, \(5{,}076=423(18-6)\) configuration/attack pairs, and **zero** attacks without a legal destination containing the attacked vertex. Each attack has between \(25\) and \(81\) distinct valid destination configurations. For any attack at any six-set, one such destination is another six-set in the same class, to which the same property applies. Induction on attack-sequence length therefore supplies an indefinitely winning defense with six guards. Combined with the preceding lower bound, this proves \(\gamma^m_\infty(P)=6\).

**Vertex-transitive nonabelian Cayley property.** The displayed maps \(F,G,D\) preserve incidence, satisfy \(F^3=G^3=D^2=1\), \(FG=GF\), \(DFD=GF\), and \(DGD=G^{-1}\). They generate a nonabelian eighteen-element group acting regularly on all eighteen vertices: \(F,G\) act regularly on each nine-vertex bipartition class and \(D\) interchanges the classes. Thus \(P\) is a cubic nonabelian Cayley graph. No claim of minimum possible order or degree among all such counterexamples is made.

## Verification
Run `python3 verify_incidence.py` and `python3 verify_lcf.py` with Python 3 and the standard library. The first uses the finite affine-incidence definition, enumeration of subsets, and recursive collision-free guard moves. The second constructs the independently labeled Pappus graph using the LCF sequence `[5,7,-7,7,-7,-5]` repeated three times and tests guard moves by destination-subset dynamic programming. Their recorded standard outputs are `verify_incidence.out` and `verify_lcf.out`. Both implementations independently reproduce all stated configurations, shift counts, attack counts, and extremes. The finite certificate is exhaustive because it iterates all six-subsets, both possible sizes at the lower bound, all legal attacked vertices of each configuration, and all six-position legal move assignments; it is not statistical sampling. The graph's abstract identification with the named Pappus graph follows from the two specified standard representations; the proof of the quantified graph/game result can independently use the affine incidence definition alone.

## Relationship to prior work
Goddard, S. M. Hedetniemi and S. T. Hedetniemi introduced multiple-guard eternal security and asserted a general Cayley-graph equality in their 2005 treatment. The latter universal assertion was explicitly refuted by Braga, de Souza and Lee (2016), who gave a different eighteen-vertex **degree-six** Cayley example. That earlier counterexample does not provide the cubic Pappus value, the eighteen explicit fatal attacks, or the complete \(423\)-configuration winning class. Pushpam and Navamani (2015) computed eternal security parameters for circulants, generalized Petersen graphs, binary trees and caterpillars; their listed graph classes are distinct from the Pappus incidence graph. Here the contribution is a structurally defined cubic Cayley example and a complete robust defensive-state classification. The 2005 erroneous general equality is not used as a valid theorem.

## Limitations
The upper-bound part uses exact exhaustive finite computation, with two independent algorithms and complete source code, rather than a short purely symbolic strategy. The proof is for the precise multiple-guard model and the given graph, not a classification of all cubic Cayley graphs or an order-minimality claim. Published papers and searchable scholarly records were checked for covering claims, but unindexed equivalent results may exist. The 2015 publisher PDF returned a retrieval error during inspection; its journal abstract and accessible bibliographic material were compared, but it was not represented as fully read. Independent external validation has not been performed.

## References
1. W. Goddard, S. M. Hedetniemi, S. T. Hedetniemi, “Eternal security in graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 52 (2005), 169–180. https://combinatorialpress.com/article/jcmcc/Volume%20052/vol-052-paper%2015.pdf
2. A. Braga, C. C. de Souza, O. Lee, “A note on the paper ‘Eternal security in graphs’,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 96 (2016), 13–22. https://combinatorialpress.com/article/jcmcc/Volume%20096/vol-096-paper%202.pdf
3. P. R. Leely Pushpam and G. Navamani, “Eternal \(m\)-security in certain classes of graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 92 (2015), 25–38. https://combinatorialpress.com/jcmcc-articles/volume-092/
4. Pappus graph: standard LCF description `[5,7,-7,7,-7,-5]` repeated three times. The two exact adjacency constructions appear in the accompanying code.
