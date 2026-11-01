# Equivariant cycle retraction and part-swap fixed loci of complete-bipartite generalized Mycielskians

## Finding
For each \(a,b\ge2\) and \(\ell\ge1\), put \(X=\operatorname{Ind}(\mu_\ell(K_{a,b}))\) and let \(H=S_a\times S_b\) permute the two vertex classes independently in every level. There is an **explicit \(H\)-equivariant piecewise-linear strong deformation retraction**
\[
 |X|\longrightarrow |X|^H\cong_{\mathrm{PL}}|\operatorname{Ind}(C_{2\ell+3})|.
\]
Thus the fixed subspace is homotopy equivalent to the entire complex, and \(H\) acts trivially on every integral homology group. Its reduced integral homology is free, with the following complete homotopy types, where \(k\ge1\) in the first case and \(k\ge0\) otherwise:
\[
 |X|^H\simeq\begin{cases}
 S^{2k}\vee S^{2k},&\ell=3k,\\
 S^{2k+1},&\ell=3k+1\ \text{or}\ \ell=3k+2.
 \end{cases}
\]
If \(a=b\), let \(\tau\) interchange the two part classes on every level and let \(W=H\rtimes\langle\tau\rangle\). The same retraction commutes with \(W\); the induced \(W/H\)-action on the cycle is its reflection fixing the apex and exchanging the ends of the opposite edge. The **full geometric fixed-point space** is
\[
 |X|^W\cong_{\mathrm{PL}}|\operatorname{Ind}(P_{\ell+1})|
 \simeq\begin{cases}
 \{\mathrm{pt}\},&\ell=3k,\\
 S^k,&\ell=3k+1\ \text{or}\ \ell=3k+2.
 \end{cases}
\]
On the unique nonzero reduced rational homology group the trace of \(\tau\) is
\[
 \operatorname{tr}(\tau_*)=\begin{cases}0,&\ell=3k,\\(-1)^{k+1},&\ell=3k+1\ \text{or}\ \ell=3k+2.\end{cases}
\]
Consequently, for \(\ell=3k\) the two-dimensional rational homology splits into one positive and one negative eigenspace; in the other two congruence classes the one-dimensional action has the indicated sign.

## Assumptions and scope
The generalized Mycielskian convention is that of Carnero Bravo, arXiv:2601.13432, §2. It has apex \(w\), level vertices \(A_j=\{(A,j,i):1\le i\le a\}\) and \(B_j=\{(B,j,i):1\le i\le b\}\) for \(0\le j\le\ell\), and *all* edges between exactly these pairs of classes:
\[
 (\{w\},A_0),\quad(\{w\},B_0),\quad
 (A_j,B_{j+1}),\quad(B_j,A_{j+1})\ (0\le j<\ell),\quad (A_\ell,B_\ell).
\]
There are no further edges, in particular none within an individual \(A_j\) or \(B_j\). Here \(\operatorname{Ind}(G)\) denotes the simplicial complex of independent graph-vertex subsets; geometric fixed points are **fixed points of the actual piecewise-linear group action**, not just vertexwise fixed simplices. The groups act simultaneously across all levels, so \(H\) has exactly the listed classes and apex as vertex orbits. The semidirect product \(W\) exists in this statement only when \(a=b\).

## Proof
**1. A general orbit-averaging lemma.** Let \(Y\) be the independence complex of a finite simple graph whose vertices are partitioned into independently permuted orbits \(O\), each of which is an independent set, and where adjacency between two distinct orbits is either complete or absent. For a point \(x\in|Y|\), write its nonnegative barycentric coordinates as \(\lambda_v(x)\). For each orbit \(O\), define \(\bar\lambda_v(x)=|O|^{-1}\sum_{u\in O}\lambda_u(x)\) for all \(v\in O\). Let \(r(x)\) have these averaged coordinates. If a simplex supporting \(x\) meets orbits \(O_1,\ldots,O_s\), no two of these orbits are adjacent in the complete-or-empty orbit graph; hence their entire union is an independent set. Therefore \(x\), \(r(x)\), and the straight-line segment between them all lie in that single simplex. The formula \(F_t(x)=(1-t)x+t r(x)\) defines a well-defined global continuous piecewise-linear homotopy. It fixes \(Y^H\) pointwise, ends in \(Y^H\), and commutes with every graph automorphism permuting these orbits. This proves an equivariant strong deformation retraction and identifies \(|Y|^H\) with the independence complex of the orbit conflict graph by the average-weight coordinates.

**2. The orbit graph is an odd cycle.** For the graph above, the \(H\)-orbits are the apex and the \(2(\ell+1)\) displayed side-and-level classes. Their orbit graph has exactly the edges in the scope definition; every vertex has degree two, and following edges from \(w\) traverses all \(2\ell+3\) orbits before returning to \(w\). Thus it is exactly \(C_{2\ell+3}\). The lemma yields both the claimed PL identification and the explicit deformation retraction; its map is \(H\)-equivariant and fixed pointwise on \(|X|^H\).

**3. Balanced part interchange.** When \(a=b\), the swap \(\tau\) exchanges \(A_j\) and \(B_j\) and fixes \(w\). It permutes \(H\)-orbits, so the averaging homotopy commutes with \(\tau\). In the odd-cycle orbit graph, \(\tau\) is reflection across \(w\) and the opposite edge \(A_\ell B_\ell\). Under all of \(W\), the vertex orbits are \(\{w\}\) and \(A_j\cup B_j\). The top orbit is not independent because it contains all edges joining \(A_\ell\) to \(B_\ell\), so its barycentric coordinate must vanish at fixed points. For every \(0\le j<\ell\), the merged orbit is independent. Among these admissible orbits the only conflicts are \(w\) against the level-zero orbit and successive level orbits against one another. Their conflict graph is precisely a path on \(\ell+1\) vertices. Averaging over \(W\)-orbits establishes the claimed PL identification of the genuine geometric \(W\)-fixed locus.

**4. Homotopy and characters.** The standard path-and-cycle independence-complex recurrences yield \(\operatorname{Ind}(P_{3k})\simeq S^{k-1}\), \(\operatorname{Ind}(P_{3k+1})\simeq\{\mathrm{pt}\}\), and \(\operatorname{Ind}(P_{3k+2})\simeq S^k\) (for valid positive orders); and \(\operatorname{Ind}(C_{3q})\simeq S^{q-1}\vee S^{q-1}\), \(\operatorname{Ind}(C_{3q+1})\simeq S^{q-1}\), \(\operatorname{Ind}(C_{3q+2})\simeq S^q\). The cycle formulas are displayed in Carnero Bravo, §3, and follow from the usual three-step vertex deletion recurrences. Substituting \(2\ell+3\) and \(\ell+1\) proves every homotopy statement, including the integral homology ranks.

The straight-line deformation is \(W\)-equivariant, so the full action on the original top homology factors through \(W/H\cong C_2\). For a finite-order simplicial action the reduced Lefschetz number equals the reduced Euler characteristic of its geometric fixed locus (equivalently, evaluate signed fixed simplices in an invariant subdivision). Here the only reduced homology degree is \(2k\) with rank two if \(\ell=3k\), or \(2k+1\) with rank one otherwise. In the first case the fixed space is contractible, yielding trace zero; in the other cases its fixed space is \(S^k\), whose reduced Euler characteristic is \((-1)^k\). Dividing by \((-1)^{2k+1}\) yields trace \((-1)^{k+1}\). A rational involution of trace zero on a rank-two space has one eigenvalue of each sign. All assertions follow.

## Verification
Run `python3 check_mycie.py` with Python 3 and no third-party dependencies. In the supplied independent finite checker, the original graph is reconstructed directly from the side/level edges; it then computes both orbit graphs from the original edge set and tests adjacency and orbit stability, homology modulo two, and signed fixed-simplex Lefschetz sums. The checker returns `PASS 108 orbit graphs, 18 homology cases, 8 signed swap character checks`. This includes \(a,b\in\{1,2,3\}\) (the theorem requires at least two), \(1\le\ell\le9\) for the orbit tests, independent mod-two checks through selected values \(\ell\le10\), and signed swap traces through \(\ell\le8\). These finite checks are neither a proof for all parameters nor a certificate of independent expert validation; the proof above is the all-parameter argument.

## Relationship to prior work
Carnero Bravo (2026), Theorem 5 and Proposition 10, determines **nonequivariant** homotopy types of generalized Mycielskian independence complexes from base-graph independence complexes; his proposition applies to bipartite base graphs. Goyal, Shukla and Singh (2019/2021) determine **nonequivariant** types for generalized Mycielskians of complete graphs. The standard topology of path and cycle independence complexes supplies the final recursive homotopy types. None of these statements specifies an equivariant strong deformation retraction onto the genuine group-fixed subspace, the complete part-swap fixed-locus model for complete bipartite base graphs, or the homology character of the part interchange. The orbit-averaging construction uses elementary false-twin graph structure; that generic principle is not presented as independently new, and equivalence through other unindexed equivariant blow-up results is a residual originality risk.

## Limitations
The result treats complete bipartite base graphs and the stated side-permutation groups; for the part swap it assumes equal part sizes. It makes no claim about arbitrary non-bipartite base graphs or arbitrary automorphism subgroups, nor about a diagonal integral eigenspace splitting in the rank-two case. The strong deformation proof is an explicit equivariant topological argument; numerical checks cover only finite parameters. Prior generic twin-blow-up literature might imply portions of the construction; equivalent unindexed work cannot be excluded. Independent mathematical validation has not been performed.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1 (first public 2026-01-19), §§2–3, Theorem 5 and Proposition 10; https://arxiv.org/abs/2601.13432.
2. Shuchita Goyal, Samir Shukla and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019); *Contributions to Discrete Mathematics* **16** (2021), Theorem 4.12; https://arxiv.org/abs/1905.06926.
3. The path/cycle independence-complex homotopy recurrences are summarized with citations in Carnero Bravo (2026), §§2–3.
