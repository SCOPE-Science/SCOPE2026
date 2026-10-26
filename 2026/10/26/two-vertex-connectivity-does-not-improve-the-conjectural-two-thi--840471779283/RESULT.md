# Two-vertex-connectivity does not improve the conjectural two-thirds Specht spectral constant

## Finding

For each integer \(n\ge6\), let \(G_n=K_{2,n-2}\) be the unweighted complete bipartite graph with parts of sizes \(2\) and \(n-2\). Put \(\tau_n=(2,2,1^{n-4})\), and set \(\sigma_n=(2^{n/2})\) if \(n\) is even, or \(\sigma_n=(2^{(n-1)/2},1)\) if \(n\) is odd. These are nontrivial partitions of \(n\) satisfying \(\sigma_n\unrhd\tau_n\). For the Specht-module interchange Laplacian at unit edge rates,

\[
\lambda_{\min}(G_n,\tau_n)=2n-6,\qquad
\lambda_{\min}(G_n,\sigma_n)=
\begin{cases}3n-10,&n\text{ even},\\3n-11,&n\text{ odd}.\end{cases}
\]

Consequently,

\[
\frac{\lambda_{\min}(G_n,\tau_n)}{\lambda_{\min}(G_n,\sigma_n)}
=\begin{cases}
\displaystyle\frac23+\frac{2}{3(3n-10)},&n\text{ even},\\
\displaystyle\frac23+\frac{4}{3(3n-11)},&n\text{ odd},
\end{cases}
\longrightarrow \frac23.
\]

Every \(G_n\) is bipartite and 2-vertex-connected. Therefore **2-vertex-connectivity alone cannot raise the universal constant above \(2/3\)** in the Specht spectral comparison proposed by Alon [1]. This statement establishes *only an upper bound* on the best possible universal constant for this graph class; it does **not** establish the conjectured universal lower bound.

## Assumptions and scope

For a partition \(\lambda\vdash n\), write \(V^\lambda\) for the real irreducible Specht representation of \(S_n\), and \(\rho_\lambda\) for its representation map. For a graph \(G\) with edges of unit rate define

\[
L(G,\lambda)=\sum_{\{i,j\}\in E(G)}(I-\rho_\lambda((ij))),
\qquad \lambda_{\min}(G,\lambda)=\min\operatorname{spec}L(G,\lambda).
\]

Partitions are ordered by dominance of all row-prefix sums. The graph is *2-vertex-connected* if it stays connected after deletion of any single vertex. All claims concern the exact unit-rate generator normalization above, finite integers \(n\ge6\), and the specified pair of partitions, not arbitrary graphs or edge weights.

## Proof

**Step 1 (a two-box spectral formula).** Label the size-two vertex part by \(A=\{1,2\}\) and the other part by \(B=\{3,\ldots,n\}\). Define the central transposition sum \(C(S)=\sum_{\{i,j\}\subset S}(ij)\). The crossing-edge group-algebra element is

\[
\sum_{i\in A,j\in B}(ij)=C(A\cup B)-C(A)-C(B).
\]

The transposition sum \(C(S)\) acts on a Specht representation of shape \(\gamma\vdash |S|\) by the scalar \(c(\gamma)=\sum_{(r,s)\in\gamma}(s-r)\), the sum of Young-diagram contents. Restrict \(V^\lambda\) to \(S_A\times S_B\). The Littlewood–Richardson/Pieri branching rule decomposes it into terms \(V^\alpha\otimes V^\beta\), where \(\alpha\vdash2\), \(\beta\vdash n-2\), and either \(\lambda/\beta\) is a horizontal two-strip with \(\alpha=(2)\), or a vertical two-strip with \(\alpha=(1,1)\). These terms exist with multiplicity one in each specified pair. The crossing sum acts by the scalar

\[
c(\lambda)-c(\alpha)-c(\beta)
=\sum_{(r,s)\in\lambda/\beta}(s-r)-c(\alpha).
\]

Since \(c((2))=1\), \(c((1,1))=-1\), and \(G_n\) has \(2(n-2)\) edges, it follows that

\[
\lambda_{\min}(K_{2,n-2},\lambda)
=2(n-2)-\max_{(\alpha,\beta)\text{ admissible}}
\left[\sum_{(r,s)\in\lambda/\beta}(s-r)-c(\alpha)\right].
\]

The maximum is over all \(\beta\vdash n-2\) contained in \(\lambda\), subject to the named strip condition. An empty branch makes no contribution.

**Step 2 (the lower partition).** In \(\tau_n=(2,2,1^{n-4})\), the two highest box contents are \(1\) and \(0\), so every legal score in Step 1 is at most \(2\). Removing boxes \((1,2)\) and \((2,2)\) is a legal vertical two-strip with content sum \(1\), yielding score \(2\). Hence \(\lambda_{\min}(G_n,\tau_n)=2(n-2)-2=2n-6\).

**Step 3 (the upper partition).** Write \(n=2m\) for even \(n\). From \(\sigma_n=(2^m)\), two corner removals making a partition can remove either both boxes of the final row, or the column-two boxes in the final two rows. The former horizontal strip gives score \(2-n\); the latter vertical strip gives \(6-n\). Thus the maximal score is \(6-n\) and the minimum eigenvalue is \(3n-10\).

For odd \(n=2m+1\), \(\sigma_n=(2^m,1)\). The admissible deletions are the column-two boxes of the last two rows of length two (vertical score \(7-n\)), or the bottom singleton and the column-two box of the preceding row (vertical score \(4-n\), horizontal score \(2-n\)). Thus the maximal score is \(7-n\) and the minimum eigenvalue is \(3n-11\). These enumerations remain valid at the smallest stated values of \(n\).

**Step 4 (graph and dominance).** Removing any one vertex from \(K_{2,n-2}\) leaves either \(K_{1,n-2}\) or \(K_{2,n-3}\), each connected for \(n\ge6\); hence it is 2-vertex-connected. Its bipartition makes it bipartite. Both \(\sigma_n\) and \(\tau_n\) begin with two rows of length two, and every subsequent row of \(\sigma_n\) has length at least the corresponding row of \(\tau_n\) until \(\sigma_n\) ends. Their total sizes agree, proving \(\sigma_n\unrhd\tau_n\). Divide the eigenvalues and pass to the limit to obtain the displayed ratios.

## Verification

The accompanying `verify.py` independently implements two checks: (i) exhaustive two-box Pieri branching for each integer \(6\le n\le20\), using only integer diagram/content arithmetic; and (ii) construction of the actual orthogonal seminormal Specht representations of adjacent transpositions, composition into crossing transpositions, and numerical diagonalization of the full Laplacian for \(6\le n\le10\). The tests reproduce all stated eigenvalues. Execute `python verify.py` with Python 3 and NumPy; it includes assertions and reports dimensions and spectral minima. Such finite checks corroborate but do not replace the general Pieri proof.

## Relationship to prior work

Alon [1] conjectures a universal ratio lower bound \(2/3\) for dominance-comparable nontrivial Specht representations, proves it for quasi-complete graphs, and gives **star-graph** equality examples (Theorem 4.5). A star has a cut vertex; the present example belongs to the structurally different class of 2-vertex-connected bipartite graphs, and its ratio approaches \(2/3\) as the size grows. Although complete bipartite graphs are natural classical graphs, the cited sources do not state this graph-class sharpness obstruction. Alon and Kozma [2] study Aldous-order comparisons and related star examples; their results do not imply the displayed two-part exact minima. The argument uses standard symmetric-group content and Pieri branching facts and does not claim those techniques as new.

## Limitations

The theorem does not prove the universal conjectural inequality, and the ratios are strictly larger than \(2/3\) for each finite graph in this family; only their limit attains \(2/3\). The finding therefore rules out a *stronger size-independent constant*, not an additive finite-size improvement or a condition such as 3-vertex-connectivity. Unlocated literature on complete-bipartite interchange representations could contain these exact evaluations; independent priority verification is still warranted. These are mathematical proofs with finite computational corroboration, not an independently certified theorem.

## References

[1] Gil Alon, *Spectral comparison on Specht modules and mixing of the interchange process*, arXiv:2610.22151v1 (first public 2026-10-15), especially Conjecture 1.5 and Theorems 4.4–4.5, https://arxiv.org/html/2610.22151v1.

[2] Gil Alon and Gady Kozma, *Ordering the representations of Sn using the interchange process*, arXiv:1003.1710v2, https://arxiv.org/abs/1003.1710.
