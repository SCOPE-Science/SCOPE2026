# Integral homology and rational persistence of the \(K_2\times K_3\times K_3\) forest filtration

## Finding
Let \(G=K_2\times K_3\times K_3\) be the **categorical** product: its vertex set is \(\{0,1\}\times\{0,1,2\}^2\), and distinct vertices are adjacent if and only if they differ in all three coordinates. For each integer \(d\geq0\), let \(\mathcal F_d(G)\) consist of the vertex subsets whose induced subgraph is a forest of maximum degree at most \(d\). In degree \(d=0\), this is the independence complex. The graph has 18 vertices, 36 edges, and maximum degree four, so \(\mathcal F_d(G)=\mathcal F_4(G)\) for every \(d\geq4\).

**Theorem (exact finite filtration).** Every reduced integral homology group in this filtration is free abelian. Its nonzero ranks, with all unlisted reduced groups zero, are:

| Forest degree | Nonzero reduced integral homology |
| --- | --- |
| \(d=0\) | \(\widetilde H_3\cong\mathbb Z^{14}\) |
| \(d=1\) | \(\widetilde H_5\cong\mathbb Z^{17}\) |
| \(d=2\) | \(\widetilde H_7\cong\mathbb Z^{17}\), \(\widetilde H_8\cong\mathbb Z^{36}\), \(\widetilde H_9\cong\mathbb Z^{6}\) |
| \(d=3\) | \(\widetilde H_8\cong\mathbb Z^{199}\), \(\widetilde H_9\cong\mathbb Z^{6}\) |
| \(d\geq4\) | \(\widetilde H_8\cong\mathbb Z^{217}\), \(\widetilde H_9\cong\mathbb Z^{6}\) |

The inclusions from forest degree 2 to 3 and from 3 to 4 are injective on rational homology in degrees 8 and 9. Their respective rational image ranks are \((36,6)\) and \((199,6)\) in those two degrees. Thus the complete reduced **rational** persistence barcode, with an infinite right endpoint denoted \(\infty\), is

\[
\begin{aligned}
&H_3:\quad 14[0,1),\\
&H_5:\quad 17[1,2),\\
&H_7:\quad 17[2,3),\\
&H_8:\quad 36[2,\infty)\oplus163[3,\infty)\oplus18[4,\infty),\\
&H_9:\quad 6[2,\infty).
\end{aligned}
\]

Here, for example, \(36[2,\infty)\) denotes 36 intervals born at forest degree 2 and never dying. The degree-zero barcode refers to **reduced** homology, so no persistent connected-component interval is included. The already known independence-complex case \(d=0\) is incorporated only to complete the filtration; the new information concerns positive forest degrees and the inclusion maps.

## Assumptions and scope
All simplicial chains use integral coefficients and the ordered vertex set in lexicographic coordinate order; orientations follow increasing vertex indices. All complexes contain the empty simplex for reduced homology. The forest degree is the maximum allowed degree of an **induced** acyclic subgraph, not the edge-count cutoff, and the graph product is categorical, not Cartesian. All homological assertions are for this single 18-vertex graph, at every integer \(d\geq0\). Persistence is asserted over \(\mathbb Q\); integral persistence splitting and the complete homotopy type at degree 2 are not asserted.

## Proof
**1. Exhaustive finite domain.** There are exactly \(2^{18}=262144\) vertex subsets. For a subset \(S\), take its induced adjacency masks, reject it if a vertex has induced degree greater than \(d\), and reject it if an edge joins vertices already connected in a union-find forest. The latter accepts exactly the acyclic induced subgraphs, because every edge is processed once. The resulting total face counts, **including the empty face**, at \(d=0,1,2,3,4\) are respectively 1650, 8565, 49743, 92835, and 97029. Their full dimension-by-dimension face vectors appear in `computed.json`; `verify_crosscheck.py` recomputes them by a different component-count test. Since the maximum graph degree is four, there are no later changes.

**2. Exact acyclic face matching.** In each face poset, start with all faces unpaired. Visit the 18 vertex indices in increasing order; for the current index \(i\), pair every still-unpaired face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\) whenever both remain unpaired. All pairs have codimension one. For every pair \((\lambda,\mu)\) in which \(\lambda\) has dimension \(k\), draw an arrow from \(\lambda\) to each other paired lower \(k\)-face of \(\mu\). The verifier topologically sorts this finite arrow graph **for every dimension of every filtration stage**; each is acyclic, so the pairing has no closed Forman gradient path. The empty face may be paired, as appropriate for augmented reduced chains.

The resulting critical cells, recorded by dimension with multiplicity, are
\[
\begin{array}{c|l}
 d&\text{critical dimensions and counts}\\\hline
 0&3:14\\
 1&5:17\\
 2&6:16,\ 7:33,\ 8:36,\ 9:6\\
 3&8:199,\ 9:6\\
 4&8:220,\ 9:9.
\end{array}
\]

**3. Exact signed Morse boundaries.** Let \(P_k\) be the chain projection to critical \(k\)-faces. On a critical face it is the corresponding basis element; on a face matched as *upper* it is zero. If a lower \(k\)-face \(\lambda\) is matched to its upper face \(\mu\), put \(\varepsilon=\langle\partial\mu,\lambda\rangle\in\{\pm1\}\) and define
\[
P_k(\lambda)=-\varepsilon\sum_{\rho\ne\lambda,\ \rho\subset\mu,\ \dim\rho=k}\langle\partial\mu,\rho\rangle P_k(\rho).
\]
Acyclicity makes the recursion well founded. For each critical \((k+1)\)-face, its Morse boundary is \(P_k\) applied to its signed simplicial boundary. The verifier checks the resulting integer matrices satisfy \(\partial^2=0\). All Morse boundary matrices are zero except for a matrix of integral rank 16 at forest degree 2, from Morse dimension 7 to 6, and a matrix of rank 3 at forest degree 4, from dimension 9 to 8. Both nonzero matrices admit exact sequences of respectively 16 and 3 **unit** Smith pivots leaving an all-zero residual matrix. Their Smith invariant factors are consequently all 1, proving the asserted free integral homology ranks, including the absence of hidden torsion.

**4. Inclusion ranks.** For each critical source face in dimensions 8 or 9 at forest degrees 2 and 3, the verifier constructs an explicit integer cycle in the full source simplicial chain group: it repeatedly cancels every matched lower boundary coefficient with the corresponding upper simplex, in a topological order guaranteed by the acyclic matching. It then checks the **entire signed simplicial boundary is zero**, not just the selected lower rows. Include each actual chain in the next complex and apply that next complex's exact integer Morse projection \(P\). This gives the inclusion-induced chain matrices. Ranks of the resulting vectors modulo both 1000003 and 1000000007, after quotienting by the target Morse-boundary image, are:
\[
\begin{array}{c|cc}
 \text{inclusion}&\operatorname{rank}(H_8\text{-image})&\operatorname{rank}(H_9\text{-image})\\\hline
 \mathcal F_2\hookrightarrow\mathcal F_3&36&6\\
 \mathcal F_3\hookrightarrow\mathcal F_4&199&6.
\end{array}
\]
The source groups in these degrees have exactly these ranks. For the target Morse-boundary matrices, the unit Smith pivots give the **same** rank in every characteristic. Therefore the modular computations exhibit nonzero maximal minors in the quotient and prove the corresponding ranks over \(\mathbb Q\) without probabilistic inference. Earlier transitions, and the disappearing degree-7 classes at the transition from 2 to 3, are zero by their different homological degrees. Subtracting the persisting ranks from successive Betti numbers yields the seven barcode types claimed above.

**5. Independent finite checks.** The separate `verify_crosscheck.py` uses a permuted vertex order, counts connected components and edges rather than union-find cycle tests, reverses the matching pivot order, and computes integral Smith normal forms using a separate matrix implementation. Its face counts and integral Betti groups agree at all five stages. Exact computations and finite exhaustiveness, not a sample of graph subsets, underlie the theorem.

## Verification
Run `python3 verify_forest.py` with Python 3.10 or later from the package directory. The output must agree with `computed.json`; this checker uses only the standard library. Run `python3 verify_crosscheck.py` with SymPy installed and compare its stage-wise face counts and Betti ranks with the same file. Both scripts enumerate **all** vertex subsets and check integral differential data. The signed cycle-lifting and rational inclusion-rank tests are explicitly performed by the first script. `crosscheck.txt` contains the saved output of the second script. Every required file is included in this package.

## Relationship to prior work
Carnero Bravo introduced the induced-forest filtration in 2023 and, in the public 2025 revision of *The Forest Filtration of a Graph*, gave homotopy types for several families, including \(K_2\times K_2\times K_n\), but explicitly asked for \(K_2\times K_m\times K_n\) with \(d\geq1\) (Question 44). The graph here is the first symmetric triple-product instance with both latter factors of order at least three. Antolín Camarena and Carnero Bravo separately determined \(\mathcal F_0\) for all such products; that supplies only the first barcode level. The present calculation supplies the previously unspecified positive-degree integral homology and rational persistence for the smallest case, including the six persistent ninth-homology classes and new eighth-homology births. It does not solve the published question uniformly in the parameters or determine the full degree-2 homotopy type.

## Limitations
This theorem is finite and specialized to \(K_2\times K_3\times K_3\). The three consecutive homology degrees at \(d=2\) do **not**, by themselves, establish a wedge-of-spheres homotopy decomposition; secondary attaching phenomena are not ruled out here. Persistence is classified over \(\mathbb Q\), not as a direct-sum decomposition of filtered integral modules and not uniformly over all coefficient fields. The computation is reproducible and finite, but its originality remains subject to the possibility of unindexed or unpublished equivalent calculations. No external mathematical audit is represented by these reproductions.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, initial public submission 25 July 2023; public revision 12 March 2025, especially Theorem 42, Corollary 43, and Question 44. https://arxiv.org/html/2307.13271v3
2. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, initial public submission 23 July 2023, Section 4. https://arxiv.org/html/2307.12401v2
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, for acyclic discrete Morse matching and cellular reduction.
