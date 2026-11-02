# Adjoint-rank enumeration and the vertex-arboricity threshold for radical-square-zero quiver algebras

## Finding

Let \(Q\) be any finite loopless quiver (parallel arrows allowed), \(V\) its vertices, \(E\) its arrows, and \(G\) its underlying undirected multigraph. Put \(n=|V|\), \(m=|E|\), and \(A_Q=\mathbb F_q Q/J^2\), where \(q\) is any prime power and \(J\) is the arrow ideal. For a labeling \(a:V\to\mathbb F_q\), write \(E_a=\{e\in E:a(s(e))=a(t(e))\}\); for \(S\subseteq E\), let \(k(S)\) be the number of connected components of the spanning multigraph \((V,S)\), with isolated vertices counted.

**Exact adjoint-rank distribution.** With \(\operatorname{ad}_x(y)=xy-yx\), let \(R_{Q,q}(t)=\sum_{x\in A_Q}t^{\operatorname{rank}_{\mathbb F_q}(\operatorname{ad}_x)}\). Then
\[
R_{Q,q}(t)=\sum_{a:V\to\mathbb F_q}q^{m-|E_a|}
\sum_{S\subseteq E_a}(q-1)^{|S|}
 t^{m-|E_a|+n-k(S)}. \tag{1}
\]
In particular the complete multiset of element-centralizer *cardinalities* is independent of all arrow orientations; an element counted by the summand indexed by \((a,S)\) has centralizer cardinality \(q^{|E_a|+k(S)}\). The statement does not assert equality of the centralizer subrings as sets.

**Extremal rank and vertex arboricity.** Define the monochromatic cycle-excess minimum
\[
\delta_q(G)=\min_{a:V\to\mathbb F_q}
\bigl(|E_a|-n+k(E_a)\bigr). \tag{2}
\]
Then
\[
\max_{x\in A_Q}\operatorname{rank}(\operatorname{ad}_x)=m-\delta_q(G),
\qquad \min_{x\in A_Q}|C_{A_Q}(x)|=q^{n+\delta_q(G)}. \tag{3}
\]
Therefore \(\operatorname{ad}_x:A_Q\to J/J^2\) is surjective for some \(x\) if and only if \(G\) has a coloring with \(q\) colors such that the subgraph induced by each color is a forest. For a finite *simple* graph this is equivalent to the standard vertex-arboricity inequality \(\operatorname{va}(G)\le q\). The corresponding statement for multigraphs uses forests that exclude parallel-edge cycles.

**Commuting-pair specialization.** The number of ordered commuting pairs in \(A_Q\) is
\[
\#\{(x,y)\in A_Q^2:xy=yx\}
=q^m\sum_{S\subseteq E}(q-1)^{|S|}q^{2k(S)}. \tag{4}
\]
Thus the commuting probability is \(q^{-2n-m}\sum_{S\subseteq E}(q-1)^{|S|}q^{2k(S)}\): a Fortuin–Kasteleyn (random-cluster/Tutte) specialization with cluster parameter \(q^2\) and edge parameter \(q-1\). These are formulas for each actual finite field, not an independence or uniqueness assertion.

For example, for the underlying simple graph \(K_5\), \(\delta_2(K_5)=1\) but \(\delta_3(K_5)=0\): the largest adjoint ranks over \(\mathbb F_2\) and \(\mathbb F_3\) are respectively \(9\) and \(10\), even though \(|E|=10\). The full distributions also agree for the two inequivalent orientations \(1\to2\to3\) and \(1\leftarrow2\to3\) of a three-vertex path, although their radical-square-zero quiver algebras need not be isomorphic.

## Assumptions and scope

The quiver is finite and has no loop arrows. Parallel arrows and oriented cycles are permitted: all paths of length at least two are killed in \(A_Q\). The algebra is unital and has \(n+m\) basis elements, one trivial path per vertex and one arrow per edge. No assumption is made on characteristic or on whether \(q\) is prime rather than a higher prime power. An empty edge set gives a commutative algebra and is included. The graph connectivity convention always retains all \(n\) vertices.

## Proof

Choose the standard vertex idempotents \(e_v\) and arrows \(\alpha_e\), with multiplication \(e_{s(e)}\alpha_e=\alpha_e=\alpha_e e_{t(e)}\) and all arrow–arrow products zero. An element is uniquely \(x=\sum_v a_v e_v+\sum_e x_e\alpha_e\). For arbitrary \(y=\sum_v b_v e_v+\sum_e y_e\alpha_e\), direct multiplication gives
\[
[x,y]_e=(a_{s(e)}-a_{t(e)})y_e-(b_{s(e)}-b_{t(e)})x_e, \tag{5}
\]
with zero vertex-idempotent coordinates. This formula holds in characteristic two as written.

Fix \(x\) and put \(E_a=\{e:a_{s(e)}=a_{t(e)}\}\). On each of the \(m-|E_a|\) nonmonochromatic arrows, the coefficient of \(y_e\) in (5) is nonzero, so these output coordinates contribute independent rank-one directions; they may also absorb any effect from the variables \(b_v\). On monochromatic arrows the \(y_e\) coefficients vanish. Retain only the subset \(S=\{e\in E_a:x_e\ne0\}\). After rescaling the nonzero coordinates \(x_e\), the residual map from \(b\in\mathbb F_q^V\) is the oriented vertex-edge incidence map of \((V,S)\). Its rank is \(n-k(S)\) over every field: choosing a spanning forest gives independent differences along its edges, while differences along every remaining edge lie in their span. Consequently
\[
\operatorname{rank}(\operatorname{ad}_x)=m-|E_a|+n-k(S). \tag{6}
\]
For fixed \(a\) and \(S\), every coordinate outside \(E_a\) is free (\(q^{m-|E_a|}\) choices); coordinates on \(S\) are nonzero (\((q-1)^{|S|}\) choices); and those on \(E_a\setminus S\) vanish. Summing these mutually exclusive possibilities proves (1), including all boundary cases. Since the kernel of the adjoint map is the centralizer, rank–nullity also gives the indicated centralizer cardinality.

For fixed \(a\), the rank in (6) is maximized by taking \(S\) to span every connected component of \(E_a\), for example \(S=E_a\) with all monochromatic coefficients nonzero. It is then
\[
m-|E_a|+n-k(E_a)=m-(|E_a|-n+k(E_a)).
\]
The parenthesized quantity is the cycle-space dimension (nullity) of the monochromatic spanning multigraph. Minimizing it proves (2)–(3). It is zero exactly when \(E_a\) is acyclic, equivalently when every monochromatic induced subgraph is a forest. This proves the vertex-arboricity criterion. In particular, \(K_5\) requires three color classes to put at most two vertices in each induced clique; with two colors, the optimal class sizes are \(3\) and \(2\), giving one monochromatic cycle.

Lastly, sum \(q^{n+m-\operatorname{rank}(\operatorname{ad}_x)}=q^{|E_a|+k(S)}\) over (1). This produces \(q^m\sum_a\sum_{S\subseteq E_a}(q-1)^{|S|}q^{k(S)}\). Interchange sums. A fixed edge set \(S\) is monochromatic under exactly \(q^{k(S)}\) vertex labelings \(a\), proving (4). The formula is independent of the arrow orientations because (1) depends only on endpoint equalities and connected components.

## Verification

The included standalone `verify.py` implements field arithmetic for \(q=2,3,4\), constructs each radical-square-zero algebra by multiplying the basis idempotents and arrows, forms the complete adjoint matrix of each element, and obtains its rank by Gaussian elimination. This *direct* enumeration is compared to an independent subset-graph count from (1), and the commuting-pair totals are cross-checked against the subset sum (4). It does not infer infinite correctness from the enumerations.

Eight configurations were exhaustively checked: a single arrow over \(\mathbb F_2\); both forward-path and fork orientations of a three-vertex path over \(\mathbb F_2\); the fork over \(\mathbb F_4\); a triangle over \(\mathbb F_3\); a pair of parallel arrows over \(\mathbb F_3\); and \(K_4,K_5\) over \(\mathbb F_2\). The largest check tested every one of the \(32,768\) elements of the \(K_5\) algebra, with rank multiplicities \((2,20,110,460,1616,960,4320,11200,8960,5120)\) in ranks \(0\) through \(9\). The program terminates with `VERIFY_OK 8 direct exhaustive configurations`. Formula-only counting for \(K_5\) over \(\mathbb F_3\) gives \(2,361,960\) elements of full rank \(10\), consistent with its three-color induced-forest partition.

## Relationship to prior work

Dutta, Basnet and Nath (2018, arXiv:1803.04111) study finite rings with a small number of distinct element-centralizers, with formulas for cases with at most seven centralizers. Their complete theorem concerns centralizer-count classes, and gives no general radical-square-zero quiver rank distribution or vertex-arboricity characterization.

Green and Schroll (2023, arXiv:2302.08169) study a different construction called the *commuting algebra*, formed by quotienting path algebras using relations between parallel paths. Their full-text results on that quotient's structure do not determine the element-centralizer cardinalities of \(\mathbb F_qQ/J^2\). The distinction between a *commuting algebra* and *commuting pairs of elements of an algebra* matters.

Dutta, Basnet and Nath (2023) study finite rings with a small number of distinct centralizers and derive commuting probabilities in such classes. Their results for rings with at most seven centralizers do not imply the all-quiver distribution (1). Shumyatsky and Vannacci (2023, arXiv:2307.12633) give structural bounds from the commuting probability, not its exact value on these quiver algebras.

Abdelgadir, Mellit and Rodriguez-Villegas (2019, arXiv:1910.01633) relate another specialization of the Tutte polynomial to one-dimensional quiver representations and toric Nakajima varieties. The specialization in (4) concerns commuting pairs in a radical-square-zero path algebra and is not their Kac-polynomial identity. The Fortuin–Kasteleyn identity itself is classical and is not claimed as new. The publicly indexed result *Commutator fibers and commuting probabilities of finite Kronecker path algebras* already handles the special case of two vertices with parallel arrows; (4) includes its commuting probability as a special case but (1) and the extremal vertex-arboricity criterion hold for arbitrary finite loopless quivers.

## Limitations

No formula is claimed for path algebras in which nonzero paths of length two survive, or for quivers with loop arrows. The theorem classifies centralizer *sizes*, not isomorphism types of centralizer algebras, their distinct set-theoretic centralizers, or simultaneous commutator fibers. General graph-polynomial and square-zero-algebra identities could conceivably imply an equivalent statement under different terminology; publication priority is not independently certified. The computational tests cover only the listed finite configurations. Mathematical verification is internal, not independent auditing.

## References

1. J. Dutta, D. K. Basnet and R. K. Nath, *Commuting probabilities of \(n\)-centralizer finite rings*, arXiv:1803.04111v1, first public version 12 March 2018. https://arxiv.org/abs/1803.04111
2. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169, first version 16 February 2023. https://arxiv.org/abs/2302.08169
3. J. Dutta, D. K. Basnet and R. K. Nath, *Characterization and commuting probability of \(n\)-centralizer finite rings*, Proyecciones 42 (2023), 1489–1498. DOI:10.22199/issn.0717-6279-5440.
4. P. Shumyatsky and M. Vannacci, *Commuting and product-zero probability in finite rings*, arXiv:2307.12633, 24 July 2023. https://arxiv.org/abs/2307.12633
5. T. Abdelgadir, A. Mellit and F. Rodriguez-Villegas, *The Tutte polynomial and toric Nakajima quiver varieties*, arXiv:1910.01633, 3 October 2019. https://arxiv.org/abs/1910.01633
6. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, Surveys in Combinatorics 2005, 173–226. https://arxiv.org/abs/math/0503607
7. Public research record: *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d
