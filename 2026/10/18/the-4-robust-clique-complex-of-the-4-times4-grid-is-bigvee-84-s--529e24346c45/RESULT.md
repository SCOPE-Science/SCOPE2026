# The \(4\)-robust clique complex of the \(4\times4\) grid is \(\bigvee^{84}S^5\)

## Finding

Let \(G=P_4\square P_4\), and write
\[
K=\operatorname{Cliq}_4(G)=\{W\subseteq V(G):\alpha(G[W])<4\},
\]
where \(\alpha(G[W])\) is the independence number of the induced subgraph. Then
\[
|K|\simeq\bigvee^{84}S^5.
\]
In particular, \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^{84}\), and all other reduced integral homology groups vanish. This is an exact finite homotopy classification, not an extrapolation in the grid dimensions or robustness parameter.

## Assumptions and scope

The graph has precisely \(16\) vertices \((r,c)\) with \(0\le r,c\le3\), indexed by \(v=4r+c\). Two vertices are adjacent precisely when their Manhattan distance is \(1\). There are \(24\) graph edges. A subset is a simplex of \(K\) if and only if it contains no independent set of four graph vertices. The empty simplex is used only in the augmented matching computation; the conclusion concerns the ordinary nonempty geometric realization.

## Proof

**Step 1: Exact face enumeration.** Encode a vertex subset as a \(16\)-bit integer mask \(S\). With \(N[v]\) the closed graph neighborhood of any vertex \(v\in S\), its independence number obeys the exact recurrence
\[
\alpha(S)=\max\{\alpha(S\setminus\{v\}),\;1+\alpha(S\setminus N[v])\},\qquad\alpha(\varnothing)=0.
\]
The recurrence follows by splitting independent sets according to whether they contain \(v\). Evaluating it for all \(2^{16}\) subsets, and retaining those with independence number at most \(3\), gives the nonempty face vector by dimension \(0\) through \(5\):
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,560,1415,1788,912).
\]
Thus the augmented face poset has \(4812\) members. Independently enumerating the \(405\) independent four-subsets and testing inclusion of each in all vertex masks reproduces exactly the same face set.

**Step 2: Explicit matching.** Begin with all \(4812\) augmented faces unmatched. For each vertex \(v=0,1,\ldots,15\), in that order, pair every still-unmatched simplex \(F\) not containing \(v\) with \(F\cup\{v\}\), provided the latter is itself a still-unmatched simplex. These pairs are disjoint codimension-one incidences. The complete enumeration yields exactly \(2364\) pairs and \(84\) unmatched faces, all of cardinality \(6\) (dimension \(5\)); the empty simplex is paired with a singleton.

**Step 3: Acyclicity certificate.** Orient every codimension-one incidence \(F\subset F\cup\{v\}\) downward, except that incidences belonging to the matching are oriented upward. The resulting directed Hasse graph has \(4812\) vertices and \(22008\) directed edges. The supplied verifier builds every edge, then applies Kahn's topological-sort algorithm. It removes all \(4812\) vertices, so the directed graph has no cycle. No sampling, rank inference, or timeout is used for this acyclicity check.

**Step 4: Homotopy conclusion.** Delete the matched empty-simplex pair and remove the empty simplex from the poset. All nonempty incidences preserve their orientations, so the restricted matching remains acyclic. It has exactly one critical vertex and \(84\) critical five-simplices, with no other critical dimensions. Forman's discrete Morse theorem yields a CW complex with one zero-cell and \(84\) five-cells. Each attaching map \(S^4\to\{*\}\) is constant, hence the CW complex is a wedge of \(84\) copies of \(S^5\), as claimed.

## Verification

Run `python3 verify_morse.py` to reconstruct all \(2^{16}\) masks, independently compare against the \(405\) forbidden independent four-subsets, build the full matching and directed Hasse graph, and check a complete topological ordering. The expected result is `VERIFY_OK` with \(4812\) augmented faces, \(2364\) pairs, \(84\) unmatched five-faces, and \(22008\) incidences.

Run `python3 verify_mod2.py` for an independent direct enumeration and binary boundary-matrix reduction. It returns reduced mod-two Betti vector \((0,0,0,0,0,84)\) and Euler characteristic \(-83\). This second computation is a corroboration; the acyclic matching establishes the integral homotopy type.

## Relationship to prior work

Filakovský (arXiv:2602.11365, first released 2026-02-11) classifies the \(k\)-robust clique complexes of rectangular grids for \(k\in\{2,3\}\) and gives an all-\(k\) theorem for square sequences built entirely through edge-gluing. The present example uses \(k=4\) and does not fall under the edge-only hypothesis: building nine squares by edge-gluing from the first square requires \(4+2(9-1)=20\) vertices, whereas this grid has only \(16\). The paper proposes a broader sphere-wedge conjecture beyond its proven cases. The computed multiplicity agrees in this particular case with \(\binom{9}{3}=84\), but no general binomial formula is claimed here.

Chandrakar, Hazra, Rout, and Singh (arXiv:2408.07646) prove total-cut homotopy classifications for \(2\times n\) grids at arbitrary cut parameter and \(3\times n\) grids at parameter \(3\); these do not determine the present \(4\times4\), parameter-\(4\) dual case. Carnero Bravo (arXiv:2602.21427) handles Cartesian products of paths for total \(2\)-cut complexes, not the parameter-\(4\) complex here. The comparison concerns theorem hypotheses and implications, not merely names.

## Limitations

The conclusion is for the single, naturally symmetric \(4\times4\) grid at robustness \(4\). It does not prove the general square-sequence conjecture, a homotopy classification of larger grids, or a formula for every \(k\). The exhaustive program verifies a finite discrete-Morse certificate, not an infinite-parameter statement. No claim is made about previously unpublished classifications.

## References

1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (2026), https://arxiv.org/abs/2602.11365.
2. H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646 (2024), https://arxiv.org/abs/2408.07646.
3. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (2026), https://arxiv.org/abs/2602.21427.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
