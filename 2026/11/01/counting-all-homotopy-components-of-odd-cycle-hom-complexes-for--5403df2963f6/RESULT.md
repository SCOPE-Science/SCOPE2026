# Counting all homotopy components of odd-cycle Hom complexes for generalized theta graphs

## Finding
For an odd integer \(q\ge5\) and integers \(r\ge3\), \(L_1,\ldots,L_r\ge2\), write \(\Theta(L_1,\ldots,L_r)\) for the graph comprising \(r\) internally vertex-disjoint paths of the prescribed edge lengths, with common distinct endpoints \(a,b\). The ordinary Lovász graph-homomorphism complex satisfies an explicit complete homotopy classification, including its empty case.

For \(w=(w_2,\ldots,w_r)\in\mathbb Z^{r-1}\), define \(T_w\) to be the set of integers \(s\) satisfying
\[
  s\equiv L_1\pmod 2,\quad |s|\le L_1,\qquad
  |s+qw_i|\le L_i,\quad s+qw_i\equiv L_i\pmod 2\quad(2\le i\le r).
\]
Let \(t_w=|T_w|\), and define the finite integers
\[
  c=\#\{w:t_w\ge2\},\qquad p=q\,\#\{w:t_w=1\}.
\]
Then
\[
\operatorname{Hom}(\Theta(L_1,\ldots,L_r),C_q)
\simeq\left(\coprod_{j=1}^{c}S^1\right)\coprod\left(\coprod_{j=1}^{p}\{\mathrm{pt}\}\right).
\]
In particular, the components are indexed by their integral relative winding vector, with one circle for each winding vector permitting at least two common path displacements, but exactly \(q\) contractible components for each vector permitting only one displacement.

For example, \(\operatorname{Hom}(\Theta(3,4,6),C_5)\simeq(S^1\sqcup S^1)\sqcup(\coprod_{j=1}^{10}\{\mathrm{pt}\})\). This is a simultaneous occurrence of essential circular and frozen contractible components for a natural three-path network.

## Assumptions and scope
All graphs are finite, simple and loopless. The paths have disjoint internal vertices and share exactly two distinct endpoints; there are no extra edges. The codomain cycle has odd length at least five. \(\operatorname{Hom}(G,H)\) is the standard prodsimplicial CW complex whose vertices are graph homomorphisms \(G\to H\), with one-dimensional adjacency given by recoloring a single vertex while maintaining the graph-homomorphism condition. Empty coproductions are empty spaces. A path is oriented from \(a\) to \(b\) solely to define signs.

The interval test is finite: since \(|s|\le L_1\), every feasible \(w_i\) obeys \(|qw_i|\le L_1+L_i\). The formula is algorithmically explicit without enumeration of all vertex colorings or CW cells. A graph with exactly two parallel paths is a cycle and is not claimed as an additional result.

## Proof
**Step 1 — Signed walks and winding invariance.** Identify the vertices of \(C_q\) with \(\mathbb Z/q\mathbb Z\). For a homomorphism \(f\), record the signed increment \(+1\) or \(-1\) along every oriented edge of the \(i\)-th path; this sign is unique because \(q\ge5\). Let \(s_i\) be the sum along that path. Necessarily, \(|s_i|\le L_i\), \(s_i\equiv L_i\pmod2\), and \(s_i\equiv f(b)-f(a)\pmod q\). Hence the integers \(w_i=(s_i-s_1)/q\) exist and \(s_1\in T_w\).

Conversely, any \(w\) and \(s\in T_w\) specify feasible signed path sums \(s_1=s\) and \(s_i=s+qw_i\). Choose an arbitrary color of \(a\); independent choices of signed walks having those sums give graph homomorphisms, since the paths have disjoint interiors and common terminal colors agree modulo \(q\).

A valid single-vertex recoloring changes its color by \(\pm2\pmod q\), because all its neighbors have the same color and the two available colors are distance two apart on \(C_q\). Recoloring an internal path vertex interchanges a consecutive \((+1,-1)\) pair with \((-1,+1)\), leaving the corresponding \(s_i\) unchanged. Recoloring the initial or final common terminal changes every signed sum by the same \(\pm2\). Thus all relative winding coordinates \(w_i\) remain invariant along each edge and, therefore, on every connected component.

**Step 2 — Connectivity at fixed terminal phase and displacement.** Fix \(w\), \(s\in T_w\) and \(f(a)\in\mathbb Z/q\mathbb Z\). On each path, every signed sequence with the prescribed sum is reachable from every other by adjacent exchanges of opposite signs; an exchange is a valid recoloring of the intermediate vertex because its two neighbors coincide in \(C_q\). The exchanges on different paths are independent. Hence all graph homomorphisms with these three fixed data are connected in the one-skeleton.

For fixed \(w\), the set \(T_w\) is the intersection of integer intervals with a common parity constraint. It is therefore either empty or a full arithmetic progression of step two. If consecutive \(s,s+2\in T_w\), every corresponding path sum \(s_i\) is strictly smaller than its upper limit \(L_i\); by internal exchanges one can position a negative last step on *every* path. Recoloring \(b\) by \(+2\) then changes all \(s_i\) to \(s_i+2\) while keeping \(f(a)\) fixed. At displacement \(s+2\), all path sums exceed their lower limits, so one can put a positive first step on each path and recolor \(a\) by \(+2\), which simultaneously decreases each signed path sum by two and changes \(f(a)\) by \(+2\). Thus a two-move sequence based on adjacent feasible displacements advances the initial color by two while returning to \(s\). Because \(q\) is odd, repeated increments by two visit every color of \(a\).

Consequently, when \(t_w\ge2\), *all* homomorphisms with winding vector \(w\) belong to one connected component. If \(t_w=1\), neither terminal can be recolored: a terminal recoloring would give a different feasible displacement \(s\pm2\). Internal recolorings preserve the initial color; hence the \(q\) possible colors of \(a\) give exactly \(q\) connected components at this winding vector. These cases exhaust all homomorphisms.

**Step 3 — Distinguishing circles from contractible components.** For any graph homomorphism to \(C_q\), orient a source edge toward increasing color \(+1\pmod q\). Theorem 5.1 of Fujii–Iwamasa–Kimura–Nozaki–Suzuki (arXiv:2408.04802, Section 5) establishes that the connected component of the Hom complex is contractible if this orientation has a directed cycle, and otherwise has homotopy type \(S^1\). This published theorem supplies the component-type implication, not the new component-count formula.

Every simple cycle of the generalized theta graph consists of two complete terminal-to-terminal branches. Accordingly, the orientation contains a directed cycle exactly when one path is entirely \(+1\)-directed from \(a\) to \(b\) and a distinct path is entirely \(-1\)-directed. Equivalently, for its path sums, some \(s_i=L_i\) and a distinct \(s_j=-L_j\). With \(w\) fixed, the interval constraints on \(s\) have lower endpoints \(-L_i-qw_i\) and upper endpoints \(L_i-qw_i\), all in the same admissible parity class whenever \(T_w\neq\varnothing\). Therefore \(T_w\) has exactly one element if and only if the maximum of the lower endpoints equals the minimum of the upper endpoints, meaning precisely that at least one path attains its lower endpoint and another its upper endpoint. Since \(L_i\ge2\), these are distinct paths. This is exactly the directed-cycle criterion. Thus the \(q\) components with \(t_w=1\) are contractible, while the single component with \(t_w\ge2\) is a circle. The asserted disjoint homotopy decomposition follows.

## Verification
The accompanying standalone standard-library Python checker, `theta_hom_checker.py`, constructs graph homomorphisms independently as signed walks, builds their single-vertex recoloring graph, enumerates cubical cells from compatible independent flips, computes componentwise Euler characteristics, and compares connected-component counts with the interval formula. It exhaustively tests nineteen examples for odd target lengths \(5,7,9\) and three- or four-branch networks, totaling 6,950 graph homomorphisms and 51,624 enumerated CW cells. Every case matches the predicted circle/point count and Euler characteristic. The run prints `ALL_PARALLEL_PATH_HOM_CASES_PASS cases=19 colorings=6950 cells=51624`.

The finite calculations are corroboration, not the proof of the quantified theorem. The proof uses the complete winding-connectivity argument and the cited published Hom-component criterion.

## Relationship to prior work
Čukić and Kozlov (arXiv:math/0408015) enumerated components for Hom complexes *between cycles*, corresponding to two-branch source graphs. Fujii and collaborators (arXiv:2408.04802) proved that for a connected source and cyclic target every component is a point or circle, and supplied the directed-cycle test used in Step 3. Their general component criterion alone does not state how many components of each type occur for the multi-branch theta family. Their square-free-codomain sequel (arXiv:2412.19039) extends general type determination and algorithmic methods but likewise does not explicitly give this all-length winding-vector count. Wrochna (arXiv:1408.2812) treats homomorphism reconfiguration more generally; a constructive reachability algorithm is distinguishable from a closed parameter count for this family.

The new claim is *only* the uniform integer-interval count and its proof for multi-branch theta graphs; it does not claim novelty for the general point-or-circle dichotomy, directed-cycle criterion, or the cycle-source special case.

## Limitations
The formula requires odd \(q\ge5\) and branch lengths at least two. No claims are made for even cycles, triangles as targets, graphs with additional cross-branch edges, or topological invariants of equivariant symmetry actions. Full bibliographic uniqueness is not certified; an equivalent formulation in unindexed work or a previously implicit count in more general reconfiguration literature remains possible. The theorem depends explicitly on the published point-or-circle criterion for cyclic targets, while its integer classification and connectivity arguments are self-contained.

## References
1. S. Fujii, Y. Iwamasa, K. Kimura, Y. Nozaki, and A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802, first posted 2024-08-09. https://arxiv.org/abs/2408.04802.
2. S. Fujii, K. Kimura, and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039, first posted 2024-12-26. https://arxiv.org/abs/2412.19039.
3. S. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015, first posted 2004-08-02. https://arxiv.org/abs/math/0408015.
4. M. Wrochna, *Homomorphism reconfiguration via homotopy*, arXiv:1408.2812, first posted 2014. https://arxiv.org/abs/1408.2812.
