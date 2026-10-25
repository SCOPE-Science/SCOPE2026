# The complete octahedral symmetry character of discrete-Morse-complex homology

## Finding
Let \(O=K_{2,2,2}\) be the octahedral graph on the vertices \(\{0,\ldots,5\}\), with nonedges \(\{0,1\},\{2,3\},\{4,5\}\). Write \(\mathcal M(O)\) for the **ordinary discrete Morse complex**: its vertices are vertex–edge incidence matchings \((v,vw)\), and its simplices are acyclic collections of disjoint such incidences. The full graph automorphism group \(B_3=C_2\wr S_3\) acts on this simplicial complex.

The only nonzero reduced rational homology group is \(\widetilde H_4(\mathcal M(O);\mathbb Q)\), of dimension \(675\). Its complete \(B_3\)-module structure is
\[
\widetilde H_4(\mathcal M(O);\mathbb Q)\cong
17V_{\varnothing,(3)}\oplus29V_{\varnothing,(2,1)}\oplus14V_{\varnothing,(1,1,1)}
\oplus39V_{(1),(2)}\oplus44V_{(1),(1,1)}
\oplus45V_{(2),(1)}\oplus42V_{(1,1),(1)}
\oplus11V_{(3),\varnothing}\oplus25V_{(2,1),\varnothing}\oplus15V_{(1,1,1),\varnothing}.
\]
Here \(V_{\lambda,\mu}\) is the standard rational irreducible of the signed-permutation group \(C_2\wr S_3\) indexed by a bipartition \((\lambda,\mu)\) of \(3\): it is induced from the \(S_{|\lambda|}\times S_{|\mu|}\) Specht representation, twisted by the product of sign flips on the second block. The notation \(\varnothing\) denotes the empty partition.

The full character, indexed by the positive/negative signed cycle partitions \((\lambda^+,\lambda^-)\), is as follows. A signed cycle is **positive** if its total coordinate-flip sign is \(+1\), and **negative** otherwise.

| \((\lambda^+,\lambda^-)\) | Class size | Trace on \(\widetilde H_4\) |
|---|---:|---:|
| \((\varnothing,(1,1,1))\) | 1 | −25 |
| \((\varnothing,(2,1))\) | 6 | 1 |
| \((\varnothing,(3))\) | 8 | −1 |
| \(((1),(1,1))\) | 3 | −5 |
| \(((1),(2))\) | 6 | 1 |
| \(((1,1),(1))\) | 3 | −9 |
| \(((1,1,1),\varnothing)\) | 1 | 675 |
| \(((2),(1))\) | 6 | −15 |
| \(((2,1),\varnothing)\) | 6 | −3 |
| \(((3),\varnothing)\) | 8 | 3 |

In particular, the subspace fixed by the complete octahedral symmetry has dimension \(11\). The central inversion of the three antipodal vertex pairs has trace \(-25\), hence its \(+1\) and \(-1\) eigenspaces have dimensions \(325\) and \(350\), respectively.

## Assumptions and scope
All homology representations are over \(\mathbb Q\) and induced by the **natural simplicial** action of graph automorphisms, not by a choice of nonequivariant collapse. In the vertex numbering above, the three antipodal pairs form coordinate blocks. Elements of \(B_3\) permute blocks and may exchange the two vertices within each block. Only this finite graph and its full automorphism group are asserted; no family-wide extension is claimed.

For every ordered adjacent pair \((v,w)\), denote the incidence \((v,vw)\) by an arrow \(v\to w\). A simplex comprises arrows with at most one arrow leaving each vertex and no directed cycle. The empty simplex is included in the augmented chain complex. All chain orientations use increasing lexicographic order on the \(24\) directed arrows.

## Proof
**Step 1: finite presentation and nonequivariant homology.** There are \(12\) edges and \(24\) vertex–edge incidences. For a graph, a discrete vector field consists of incidence pairs using each vertex and graph edge at most once; an alternating closed gradient path is a directed cycle. Thus the directed-forest description in the assumptions is an exact equivalence, not a relaxation. Every arrow selection corresponds to a partial function from the six graph vertices to their four neighbors, with the option of leaving each vertex unassigned. Enumerating all \(5^6=15625\) possibilities and excluding directed cycles yields the complete face-cardinality counts
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,24,228,1072,2496,2304).
\]

An acyclic partial matching is certified using the checker file `check_octahedral_equivariant_morse.py`. Directed arrows are ordered lexicographically by tail and head and then traversed in the explicit pivot order
```
[20,19,15,7,23,12,16,8,18,10,3,2,21,4,6,13,17,5,22,1,11,0,14,9]
```
(the indices are zero-based). At each pivot, every remaining simplex lacking that arrow is paired with its coface that inserts the arrow, if both remain. The pair involving the empty simplex is instead removed from the matching, retaining its nonempty partner as a critical vertex. Exactly \(2724\) further pairs are formed. The program constructs **all \(25176\) nonempty Hasse incidence edges**, reverses exactly those in the matching, and topologically sorts the entire directed graph, verifying that no directed cycle occurs. The sole critical cells are one \(0\)-cell and \(675\) cells of dimension \(4\). The acyclic-matching theorem therefore gives the nonequivariant integral homotopy equivalence \(\mathcal M(O)\simeq\bigvee^{675} S^4\). In particular \(H_0\cong\mathbb Q\) is trivial as a representation and all positive-degree homology except \(H_4\) vanishes.

**Step 2: signed simplicial Lefschetz traces.** For each signed permutation \(g\in B_3\), let \(t_k(g)\) be the trace on augmented simplicial chains generated by forests with exactly \(k\) arrows, where \(k\) runs from \(0\) to \(5\). The empty face contributes \(t_0(g)=1\). A nonempty forest contributes only if its arrow set is invariant under \(g\), and then contributes the sign of the permutation induced by \(g\) on its **ordered** arrow set. Thus the trace is computed by the finite formula
\[
t_k(g)=\sum_{\substack{|F|=k\\ gF=F}}\operatorname{sgn}(g|_F).
\]
The alternating trace identity on the augmented chain complex and the homology concentration established in Step 1 give
\[
\chi_4(g)=-\sum_{k=0}^{5}(-1)^k t_k(g).
\]
The checker evaluates this for every one of the \(6\cdot2^3=48\) signed permutations. It verifies that all values agree within each of the ten conjugacy classes. The resulting complete character table is displayed in the Finding section.

**Step 3: irreducible decomposition.** For a bipartition \((\alpha,\beta)\) of \(3\), an element \(g=(p,\epsilon)\) consists of an axis permutation \(p\in S_3\) and three signs \(\epsilon_i\in\{\pm1\}\). Write \(\chi^{\nu}\) for the ordinary symmetric-group irreducible character indexed by \(\nu\). Induction from the subgroup preserving an axis subset of size \(|\beta|\) gives the exact character formula
\[
\chi_{\alpha,\beta}(p,\epsilon)=
\sum_{\substack{S\subseteq\{0,1,2\}\\|S|=|\beta|,\;p(S)=S}}
\left(\prod_{i\in S}\epsilon_i\right)
\chi^\alpha(p|_{S^c})\chi^\beta(p|_S).
\]
The code evaluates all ten such irreducible characters using the exact tables of \(S_0,S_1,S_2,S_3\), verifies their pairwise inner products are \(\delta_{\alpha\gamma}\delta_{\beta\delta}\), and computes multiplicities from
\[
m_{\alpha,\beta}=\frac1{48}\sum_{g\in B_3}\chi_4(g)\chi_{\alpha,\beta}(g).
\]
All multiplicities are nonnegative integers and are precisely those listed in the Finding. Reconstructing the character of every group element from the decomposition reproduces all \(48\) traces; the sum of irreducible dimensions is \(675\).

Averaging the character gives \(\dim H_4^{B_3}=\frac1{48}\sum_g\chi_4(g)=11\). Central inversion has signed cycle type \((\varnothing,(1,1,1))\); its trace \(-25\) and the dimension \(675\) yield the two stated inversion eigendimensions.

## Verification
Run `python3 check_octahedral_equivariant_morse.py` with Python 3 and no external packages. The checker constructs the complete complex from arrow assignments, tests all Hasse incidences and matching acyclicity, verifies all \(48\) graph symmetries send faces to faces, computes signed Lefschetz traces, checks conjugacy invariance and irreducible orthogonality, and reconstructs every value from the multiplicity list. The successful replay prints `ALL EXACT CHECKS PASS` and the two tables above. This is a finite exhaustive computation **combined with** the standard algebraic-topological discrete Morse and Lefschetz theorems; it is not a numerical sampling argument. See `VERIFICATION.md` for check scope.

## Relationship to prior work
Celoria and Yerolemou [1] treat the Chari–Joswig Morse complex, its rooted-forest formulation, and filtered matchings; their inspected paper does not calculate the \(B_3\)-homology character of the octahedral example. Yerolemou and Nanda [2] provide a general framework for equivariant Morse theory, but the inspected results concern equivariant homotopy reconstruction, not a specific \(B_3\)-character computation. The published explicit calculation [3] already establishes the **nonequivariant** \(675\)-sphere wedge for this same octahedral Morse complex, with exactly the same face vector. That homotopy statement, pivot construction, and Betti number are acknowledged prior facts, **not claimed as new** here. The added result is the complete rational character on the existing \(675\)-dimensional homology group, including all ten irreducible multiplicities and the inversion/fixed-space dimensions. A published octahedral *matching* complex representation [4] concerns a different simplicial complex and cannot imply this discrete-Morse-complex character. General representation theory supplies the character-decomposition method, not the \(48\) graph-specific signed face traces.

## Limitations
The result is rational, not an integral equivariant lattice classification. The acyclic matching need not respect the octahedral symmetry; it is used solely to prove homology concentration, after which the homology action is recovered directly from the original equivariant simplicial chains. The calculation is specific to \(K_{2,2,2}\). Although the nearest accessible primary sources and published computations were compared materially, an unindexed prior character table or a hidden equivalent formula remains a residual originality risk. No independent mathematical audit is claimed.

## References
1. D. Celoria and N. Yerolemou, *Filtered matchings and simplicial complexes*, arXiv:2011.02015v1 (first public 2020-11-03), *Australasian Journal of Combinatorics* **82** (2022), 335–352; full text https://ajc.maths.uq.edu.au/pdf/82/ajc_v82_p335.pdf.
2. N. Yerolemou and V. Nanda, *Morse Theory for Complexes of Groups*, arXiv:2203.00539v1 (2022-03-01), https://arxiv.org/pdf/2203.00539.
3. *The octahedral graph Morse complex is a wedge of \(675\) four-spheres*, published mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-octahedral-graph-morse-complex-is-a-wedge-of-675-four-sphere--5d292e60a1a7; the prior nonequivariant assertion and complete face vector are explicitly credited.
4. *The full octahedral symmetry representation of the matching complex*, published mathematical record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-full-octahedral-symmetry-representation-of-the-matching-comp--c700eceb52bb; this is a different underlying complex.
