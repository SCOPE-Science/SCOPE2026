# The complete joint permutation character of complete-graph Hom complexes

## Finding
For each pair of integers \(2\le m<n\), write \(X_{m,n}=\operatorname{Hom}(K_m,K_n)\). Let \(\alpha\in S_m\) permute the source vertices and \(\beta\in S_n\) permute the target colors. List the cycle lengths of \(\alpha\) as \(\ell_1,\ldots,\ell_r\) and those of \(\beta\) as \(L_1,\ldots,L_s\); cycles are indexed even when lengths coincide. Put
\[
\Phi(\alpha,\beta)=\sum_{T\subseteq\{1,\ldots,r\}}(-1)^{|T|}
\prod_{k=1}^{s}\left(1-\sum_{j\in T\, :\,\ell_j\mid L_k}\ell_j\right).
\]
**Theorem.** For every such pair and permutations, the exact rational character on the top reduced homology is
\[
\operatorname{tr}\left((\alpha,\beta)\mid\widetilde H_{n-m}(X_{m,n};\mathbb Q)\right)
=(-1)^{n-m}\bigl(\Phi(\alpha,\beta)-1\bigr).
\]
The other reduced rational homology groups vanish. In particular, \(\Phi(\alpha,\beta)\) is the ordinary Lefschetz number of the simultaneous action. The representation is determined over \(\mathbb Q\) because rational representations of finite groups are semisimple and their characters determine them.

**Corollary (diagonal source-and-color quotient).** Embed \(S_3\) diagonally in \(S_3\times S_n\) by extending each source permutation to the first three target colors and fixing the remaining ones, for any \(n\ge4\). This action has a quotient with top rational Betti number
\[
\dim_{\mathbb Q}\widetilde H_{n-3}(X_{3,n}/S_3;\mathbb Q)
=\frac{2^n-3+7(-1)^{n-3}}6.
\]
Its other reduced rational Betti numbers vanish. In particular, this quotient has nonzero top rational homology for every \(n\ge4\), whereas the previously known quotient by **all** target-color permutations is rationally acyclic. The color-only quotient's acyclicity is **not** claimed as a new result here.

The character genuinely depends jointly on both actions. For example, with \(m=3\), \(n=5\), \(\alpha=(1\,2\,3)\), and \(\beta=(1\,2\,3)\) fixing the other two target colors, the trace is \(2\). With the same \(\alpha\) and the identity target permutation, the trace is \(-1\).

## Assumptions and scope
Graphs are finite, loopless, and undirected. The ordinary Babson–Kozlov polyhedral Hom complex has a cell for every ordered \(m\)-tuple \((A_1,\ldots,A_m)\) of pairwise disjoint **nonempty** subsets of \(\{1,\ldots,n\}\). Its closed cell is \(\prod_{i=1}^m\Delta^{A_i}\), and its dimension is \(\sum_i(|A_i|-1)\). The action is \((\alpha,\beta)\cdot(A_1,\ldots,A_m)=(\beta A_{\alpha^{-1}(1)},\ldots,\beta A_{\alpha^{-1}(m)})\). All homology in the theorem has rational coefficients. The hypothesis \(m<n\) ensures the space is connected and the positive homology degree is \(n-m\ge1\). The wedge-of-spheres homotopy type used below is the prior theorem of Babson–Kozlov, not part of the new result.

## Proof
**1. Character as a fixed-point Euler characteristic.** Give every cell the product-simplex affine realization. A simultaneous permutation \(g=(\alpha,\beta)\) has finite order and maps cells affinely to cells. The relative interiors of cells are disjoint. If \(x\) is fixed, its unique relative-open containing cell is globally fixed by \(g\). Conversely, within each globally fixed cell the fixed locus of its affine action is a relatively open convex polytope (or empty), and therefore an open ball. For a finite polyhedral complex the Euler characteristic is the sum of the compactly-supported Euler contributions \((-1)^d\) of these fixed relative-open strata of dimension \(d\). Equivalently, barycentrically subdividing and applying the simplicial Lefschetz formula gives
\[
L(g;X_{m,n})=\chi(X_{m,n}^{g}).
\]
The fixed-locus computation below determines the latter without a free-action hypothesis.

**2. Classify fixed cells.** Regard a cell as a map from the target colors into \(\{0,1,\ldots,m\}\), with value \(0\) meaning an unused color, and with every source value occurring at least once. Global cell invariance under \(g\) means this map is equivariant under \(\beta\) on colors and under \(\alpha\) on the nonzero source values, with \(0\) fixed. Consider one target cycle of length \(L\). Its colors may all remain unused (one option). If any are used, they must all map into one source cycle of length \(\ell_j\). Such an equivariant assignment exists precisely when \(\ell_j\mid L\), and then has exactly \(\ell_j\) possible phases. Choices for distinct target cycles are independent until the requirement that **every** source cycle is represented is imposed. That requirement is equivalent to the nonemptiness of every source set \(A_i\), since the \(\alpha\)-orbit transports every used color through all its source vertices.

**3. Fixed-stratum dimensions.** Suppose the assignment uses exactly \(t\) target cycles and every one of the \(r\) source cycles. In a fixed point of the corresponding product cell, weights belonging to the same target color cycle are equal, and for each source cycle there is exactly one independent normalization equation on its chosen target cycles. The fixed relative-open stratum is therefore an open simplex product of dimension \(t-r\). Its contribution to \(\chi(X_{m,n}^{g})\) is \((-1)^{t-r}\). This argument also includes the case where a source or target permutation has one-cycles; no genericity assumption is needed.

**4. Sum by inclusion–exclusion.** Assigning a target cycle of length \(L_k\) to source cycle \(j\) gives \(\ell_j\) choices, together with a factor \(-1\) for having used that target cycle. The unused choice contributes \(+1\). For a selected set \(U\) of source cycles allowed to receive colors, the total signed sum over all target cycles is
\[
\prod_{k=1}^s\left(1-\sum_{j\in U:\,\ell_j\mid L_k}\ell_j\right).
\]
Inclusion–exclusion forcing every source cycle to occur, then multiplying by \((-1)^r\) to convert \((-1)^t\) to \((-1)^{t-r}\), gives
\[
\chi(X_{m,n}^{g})=(-1)^r\sum_{J\subseteq[r]}(-1)^{|J|}
\prod_{k=1}^s\left(1-\sum_{j\notin J:\,\ell_j\mid L_k}\ell_j\right)
=\Phi(\alpha,\beta),
\]
where the last equality follows on writing \(T=[r]\setminus J\). This establishes the fixed-point Euler formula for every \(m,n\) and every simultaneous permutation.

**5. Pass from Euler to the actual character.** Babson–Kozlov, Proposition 4.5, proves \(X_{m,n}\simeq\bigvee S^{n-m}\) for \(2\le m<n\). Thus the only nonzero ordinary rational homology is \(H_0\cong\mathbb Q\) with the trivial action and \(\widetilde H_{n-m}\). The Lefschetz identity reads
\[
\Phi(\alpha,\beta)=1+(-1)^{n-m}\operatorname{tr}\bigl((\alpha,\beta)\mid\widetilde H_{n-m}\bigr),
\]
which rearranges to the stated formula. No equivariance of Babson–Kozlov's chosen homotopy equivalence is needed: their **nonequivariant** homological concentration suffices.

**6. The diagonal action on three sources.** Take \(m=3\), let \(\alpha\) run through \(S_3\), and let \(\beta\) extend \(\alpha\) to the first three target colors, fixing all other colors. There are three cycle types. For the identity, Proposition 4.6 of Babson–Kozlov gives top Betti number \(2^n-3\), which is its trace. For a transposition, the source cycles have lengths \(2,1\) and the target cycles have lengths \(2,1,\ldots,1\); the formula above gives \(\Phi=2\), so the trace is \((-1)^{n-3}\). For a three-cycle, there is one source cycle of length three and one target cycle of length three, plus unused fixed colors; then \(\Phi=3\) and the trace is \(2(-1)^{n-3}\). The rational top Betti number of the diagonal quotient is the average of these character values over the six group elements:
\[
\frac16\left((2^n-3)+3(-1)^{n-3}+2\cdot2(-1)^{n-3}\right)
=\frac{2^n-3+7(-1)^{n-3}}6.
\]
For a finite group acting cellularly, barycentric subdivision followed by rational averaging identifies the homology of its quotient with invariant rational homology. Since the original complex has no other reduced rational homology, neither does this diagonal quotient. The displayed integer is positive for all \(n\ge4\), and in particular differs from the already known rational acyclicity under the full target-color group.

## Verification
A standalone standard-library Python verifier, `verify_hom_character.py`, independently enumerates the original product-simplex cells: for each color, either omit it or assign it to one source vertex; reject assignments with an empty source set. For each simultaneous permutation it sums signed traces on all invariant original cells, including the orientation sign induced by reordering factors and target vertices. It compares this independent cellular trace with \(\Phi\).

The verifier checks every group element for \((m,n)=(2,3),(2,4),(3,4),(3,5),(4,5)\), and selected additional target permutations for \((3,6)\). It also checks identity traces against the known Babson–Kozlov Betti-number formula and checks the new diagonal three-source quotient average for four values of the target-color count. The computation is **not** treated as proof of the all-parameter theorem; that is supplied above by the fixed-point cell analysis.

Run with `python3 verify_hom_character.py`. No third-party packages or downloaded data are needed. The file prints `VERIFY_OK_COMPLETE_GRAPH_HOM_CHARACTER` only after all assertions pass.

## Relationship to prior work
Babson and Kozlov's *Complexes of graph homomorphisms* (2003 preprint, Proposition 4.5 and Proposition 4.6) proves the underlying wedge-of-spheres homotopy type and its **ungraded Betti number**. Their numerical formula coincides with the identity-character specialization here; it does not supply the simultaneous character at nonidentity source and target permutations. A previously recorded target-color-only character and the rational acyclicity of the full color-quotient are also not new. They are strictly the special case with the source permutation equal to the identity, and do not determine the mixed-cycle traces or the diagonal quotient calculated here. Their paper also considers a source-vertex involution in a chromatic-obstruction context. Dochtermann and Schultz (2009) develop an equivariant test-graph framework and universality of source-permutation actions; Thansri (2010) compares symmetric-equivariant Hom and box complexes; Matsushita (2015) treats homotopy-theoretic descriptions of graph Hom complexes. These tools are structurally related, but the specifically stated **joint** cycle-divisibility trace formula and the diagonal source-color quotient conclusion are not asserted in the primary sections inspected.

## Limitations
The theorem concerns the **ordinary** Hom complex for complete source and target graphs, \(2\le m<n\), and rational homology. The diagonal-quotient corollary determines rational Betti numbers only; it does not prove an integral homology or homotopy classification. It does not identify integral \(S_m\times S_n\)-modules, provide equivariant wedge decompositions, or extend to general source/target graphs. Previously published nonequivariant sphere counts are not novel. An equivalent character formula under other representations or terminology could exist in unindexed literature; publication priority is not independently established. An apparently relevant student exposition *Homology of Hom Complexes* (2012) was not available in full text during this comparison and remains a bibliographic risk, rather than being asserted not to cover the result.

## References
1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first posted 2003-10-05), esp. §4.3, Proposition 4.5 and Proposition 4.6. https://arxiv.org/abs/math/0310056
2. A. Dochtermann and C. Schultz, *Topology of Hom complexes and test graphs for bounding chromatic number*, arXiv:0907.5079 (2009), esp. Introduction and §6 on symmetric actions. https://arxiv.org/abs/0907.5079
3. T. Thansri, *Simple \(S_r\)-homotopy types of Hom complexes and box complexes associated to \(r\)-graphs*, arXiv:1004.0583 (2010), Introduction and setup. https://arxiv.org/abs/1004.0583
4. T. Matsushita, *Homotopy Types of the Hom Complexes of Graphs*, arXiv:1509.03855 (2015), Introduction and equivariant context. https://arxiv.org/abs/1509.03855
5. M. Sanchez, *Homology of Hom Complexes*, Rose-Hulman Undergraduate Mathematics Journal (2012), available bibliographic record but inaccessible full text: https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1098&context=rhumj
