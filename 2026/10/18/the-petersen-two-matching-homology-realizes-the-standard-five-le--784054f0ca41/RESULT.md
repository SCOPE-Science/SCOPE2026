# The Petersen two-matching homology realizes the standard five-letter module

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Its vertices are the ten two-element subsets of \([5]\), with two vertices adjacent exactly when they are disjoint. Let \(K=M_2(P)\) be its two-matching complex: vertices of \(K\) are the fifteen edges of \(P\), and a subset of edges is a simplex if each vertex of \(P\) is incident to at most two chosen edges. Permuting \([5]\) induces a natural action of \(S_5\) on \(K\).

**The rational top-homology representation is the four-dimensional standard representation:**
\[
\widetilde H_7(K;\mathbb Q)\ \cong_{\mathbb Q[S_5]}\
\left\{(a_1,\ldots,a_5)\in\mathbb Q^5:\ \sum_{i=1}^5 a_i=0\right\}.
\]
All other reduced rational homology groups vanish. Equivalently, every \(g\in S_5\) has homological trace
\[
\operatorname{tr}\bigl(g_*\mid\widetilde H_7(K;\mathbb Q)\bigr)
=\#\{i\in[5]:g(i)=i\}-1.
\]

This also completely determines the **reduced rational homology of every subgroup quotient**. For any subgroup \(H\le S_5\), let \(c(H)\) be the number of orbits of \(H\) on the original five points. Then
\[
\widetilde H_j(|K|/H;\mathbb Q)\cong
\begin{cases}
\mathbb Q^{\,c(H)-1},&j=7,\\
0,&j\ne7.
\end{cases}
\]
In particular, transitive subgroups give rationally acyclic quotients, while a subgroup fixing one point and acting transitively on the other four gives one rational seven-dimensional class.

## Assumptions and scope

The simplicial complex is the ordinary bounded-degree-two matching complex, not the perfect-matching complex, ordinary degree-one matching complex, or two-independence complex. All fifteen graph edges are separate labeled vertices of \(K\); the empty face is included in the augmented chain complex. The topological quotient means the geometric realization modulo the finite group action, not the orbit set of abstract faces. Homology and representations in the new claim use \(\mathbb Q\). The underlying nonequivariant homotopy type \(K\simeq\bigvee^4S^7\) is already a published result and is reverified here solely as a premise.

Because \(P\) is triangle-free, every triangle of its line graph \(L(P)\) consists of three graph edges incident to the same Petersen vertex. Thus there is an exact identification \(K=\mathsf{CF}_3(L(P))\); the conclusion can equally be read as an equivariant statement for this three-clique-free complex.

## Proof

**1. Finite topological premise, independently reconstructed.** Number the ten graph vertices by lexicographic order of the two-subsets of \([5]\), and number the fifteen graph edges by lexicographic order of their endpoint pairs. Exhaustively list all nonempty edge masks whose ten vertex degrees are at most two. There are \(10{,}869\) simplices with the complete face vector
\[
(f_0,\ldots,f_9)=(15,105,445,1245,2358,2985,2400,1095,215,6).
\]
Perform repeated element toggles in edge order: at step \(e\), pair every remaining face \(F\) not containing \(e\) with \(F\cup\{e\}\) whenever both are present, and remove the two faces from the remaining poset. The explicit finite algorithm yields \(5{,}432\) disjoint cover pairs and exactly five unmatched faces: one vertex and four seven-dimensional faces.

A cover-edge certificate checks all \(63{,}780\) nonempty-face Hasse incidences, directing unmatched covers downward and matched covers upward. A complete directed topological ordering consumes all \(10{,}869\) poset vertices. Thus the matching is acyclic, not merely numerically plausible. By discrete Morse theory, \(K\) has a CW model with one zero-cell and four seven-cells and no other cells, hence \(K\simeq\bigvee^4 S^7\). This agrees with the separately published nonequivariant classification.

**2. Exact equivariant Lefschetz formula.** For \(g\in S_5\), let \(\mathcal O_g\) denote the orbits of \(g\) on the fifteen graph edges. Every \(g\)-invariant simplex is precisely a union of some \(\mathscr S\subseteq\mathcal O_g\) satisfying the degree-at-most-two condition. Write \(U(\mathscr S)=\bigcup_{O\in\mathscr S}O\) and \(k=|\mathscr S|\) and let \(m\) be its total number of chosen graph edges. The permutation of the simplex's \(m\) vertices has sign \((-1)^{m-k}\), because its cycles are the chosen edge-orbits. Its contribution to the reduced simplicial Lefschetz sum is therefore
\[
(-1)^{m-1}(-1)^{m-k}=(-1)^{k+1}.
\]
This formula includes the empty face, whose augmented contribution is \(-1\). Consequently,
\[
\widetilde L(g)=-\sum_{\substack{\mathscr S\subseteq\mathcal O_g\\
U(\mathscr S)\text{ admissible}}}(-1)^{|\mathscr S|}.
\]
Since reduced rational homology is concentrated in degree seven, \(\widetilde L(g)=-\operatorname{tr}(g_*\mid\widetilde H_7)\). Thus the desired character is the alternating admissible edge-orbit-subset count.

**3. All conjugacy classes.** The seven classes of \(S_5\) give the following exhaustive exact table. The third column was computed from admissible edge-orbit unions; the last column counts fixed original points.

| Cycle type of \(g\) | Edge-orbits | Homology trace | Fixed original points |
| --- | ---: | ---: | ---: |
| \(1^5\) | 15 | 4 | 5 |
| \(2\,1^3\) | 9 | 2 | 3 |
| \(2^2\,1\) | 9 | 0 | 1 |
| \(3\,1^2\) | 5 | 1 | 2 |
| \(3\,2\) | 3 | -1 | 0 |
| \(4\,1\) | 5 | 0 | 1 |
| \(5\) | 3 | -1 | 0 |

For an independent arithmetic route, the verifier scans each individual simplex, tests setwise invariance, determines the sign of the induced vertex permutation by inversion parity, and evaluates the augmented signed Lefschetz trace directly. These results equal the edge-orbit method in all seven classes.

The character \((4,2,0,1,-1,0,-1)\) equals the permutation character of the five-point action minus the trivial character. The character theorem for representations of finite groups in characteristic zero identifies the rational representation with the displayed standard module.

**4. Subgroup quotients.** Barycentric subdivision removes inversions in the finite simplicial group action. Over \(\mathbb Q\), the quotient chain complex computes the invariant simplicial chains, and averaging over \(H\) commutes with homology. Hence \(\widetilde H_*(|K|/H;\mathbb Q)\cong\widetilde H_*(K;\mathbb Q)^H\). The dimension of \(H\)-invariants in the five-point permutation module is \(c(H)\), one dimension for each point-orbit; quotienting out its trivial line leaves \(c(H)-1\). All other reduced degrees remain zero.

## Verification

Run `python3 verification/verify_character.py` using only the Python standard library. It reconstructs the full face poset from the Petersen graph, verifies all \(5{,}432\) elementary Morse pairs, and tests acyclicity over every one of the \(63{,}780\) cover relations by a complete topological sort. For each conjugacy type, it computes the alternating orbit sum and independently computes the signed trace on all invariant simplices. Both agree exactly with the five-point standard character. The complete deterministic output is in `verification/verification_output.txt`. The certificate is a finite exhaustive proof for this fixed simplicial complex; it is not an extrapolation from sampling.

## Relationship to prior work

Vega's work introduces two-matching complexes and repeated-toggle discrete Morse methods. Singh's higher-matching paper concerns complete and complete-bipartite graph families. Ghosh and Selvaraja's February 2026 work develops three-clique-free complexes, with shellability theorems under graph hypotheses not satisfied by the Petersen line graph. A published October 2026 result already establishes the exact nonequivariant homotopy type \(M_2(P)\simeq\bigvee^4S^7\); this premise is **not** claimed as new.

The contribution here is the exact rational \(S_5\)-representation and the homology classification of all subgroup quotients. A four-dimensional homology group alone does not determine its \(S_5\)-action: for instance, sign-twisting or taking sums of smaller representations could have the same rank. The signed fixed-simplex calculation distinguishes these possibilities. Targeted mathematical-database, published-result, and primary-literature comparisons found no statement already determining this character or the resulting quotient ranks.

## Limitations

The result does not identify the integral \(\mathbb Z[S_5]\)-lattice, integral torsion of quotient spaces, higher homotopy groups of quotients, or analogous representations for larger Kneser graphs. The finite checker verifies the explicitly stated claims for the one canonical graph, but cannot establish uniqueness among all possible prior publications. An unindexed equivariant calculation or general theorem specializing to this complex remains a residual overlap risk.

## References

1. Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406, initially public September 23, 2019, https://arxiv.org/abs/1909.10406.
2. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, initially public June 24, 2020, https://arxiv.org/abs/2006.13632.
3. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, initially public February 10, 2026, https://arxiv.org/html/2602.09623v1.
4. *The Petersen 2-matching complex is a wedge of four 7-spheres*, published published-finding corpus finding dated October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-petersen-2-matching-complex-is-a-wedge-of-four-7-spheres--c0442780c8c1.
