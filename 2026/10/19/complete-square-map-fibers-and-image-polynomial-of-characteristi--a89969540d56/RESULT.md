# Complete square-map fibers and image polynomial of characteristic-two graphical groups

## Finding
Let \(\Gamma=(V,E)\) be any finite simple graph (isolated vertices allowed), \(n=|V|\), \(m=|E|\), and \(q=2^f\) with \(f\ge1\). Write \(G_\Gamma(\mathbb F_q)\) for the graphical group defined below. Every square in this group is central. An exact multiplicity formula is given for **every** prescribed group element, together with the number of distinct squares and the distribution of element orders.

For an edge-label vector \(y\in\mathbb F_q^E\), let \(E_y=\{e\in E:y_e\ne0\}\), and let \(W_y\subseteq V\) be the set of endpoints of \(E_y\). Write \(B_y=(W_y,E_y)\), \(R_y=V\setminus N_\Gamma[W_y]\), where \(N_\Gamma[W_y]\) is the **closed** graph neighbourhood, and let \(b_y\) denote the number of bipartite connected components of \(B_y\). Every component of \(B_y\) contains an edge.

Define the independence polynomial of a graph \(H\) by
\[
I_H(t)=\sum_{S\subseteq V(H),\,S\text{ independent}}t^{|S|}.
\]
A label vector \(y\) is **multiplicatively consistent** when, on every connected component of \(B_y\), there exist nonzero vertex values \(a_v\in\mathbb F_q^\times\) satisfying \(a_u a_v=y_{\{u,v\}}\) on its edges. This is an explicit test using a spanning tree, detailed in the proof.

**Prescribed-square fiber theorem.** The number of \(g\in G_\Gamma(\mathbb F_q)\) satisfying \(g^2=(0,y)\) is
\[
\boxed{\quad
q^m(q-1)^{b_y}I_{\Gamma[R_y]}(q-1)\quad}
\]
if \(E_y=E(\Gamma[W_y])\) and \(y\) is multiplicatively consistent, and is **zero otherwise**. For every noncentral target, the fiber is zero. In particular, every nonzero-label support must equal the full induced edge set on its endpoints. For a fixed consistent support, bipartite components each contribute \(q-1\) solutions; nonbipartite components contribute exactly one.

Define \(\mathcal W_\Gamma\) to be the vertex subsets \(W\subseteq V\) for which \(\Gamma[W]\) has no isolated vertices, including \(W=\varnothing\), and write \(b_\Gamma(W)\) for the number of its bipartite connected components. Then **the number of distinct squares** is the graph polynomial evaluation
\[
\boxed{\quad
|\{g^2:g\in G_\Gamma(\mathbb F_q)\}|=
\sum_{W\in\mathcal W_\Gamma}(q-1)^{|W|-b_\Gamma(W)}.\quad}
\]
Finally, the number of elements whose order divides two is \(q^m I_\Gamma(q-1)\), and the number of elements of order exactly four is \(q^{n+m}-q^m I_\Gamma(q-1)\). All elements have order dividing four.

## Assumptions and scope
Number vertices as \(V=\{1,\ldots,n\}\) and orient every edge by its smaller endpoint. The group has underlying set \(\mathbb F_q^V\times\mathbb F_q^E\) and multiplication
\[
(x,z)(x',z')=(x+x',\ z+z'+(x_i x'_j)_{\{i,j\}\in E,\ i<j}).
\]
The displayed operation is associative because the cross-term is bilinear. It has identity \((0,0)\), inverses, and central subgroup \(\{(0,z):z\in\mathbb F_q^E\}\); this is an equivalent presentation of the graphical groups in Rossmann's work. All claims apply to all finite simple graphs, including disconnected graphs and the empty edge set, and to all powers of two \(q\). The theorem does not extend unaltered to odd characteristic.

The distinction between **central subgroup** and full group centre matters when \(\Gamma\) has isolated vertices: a central target \((x,y)\) with \(x\ne0\) still has zero square roots. Thus the theorem specifies the exact target, not only centrality.

## Proof
**1. Square map.** Bilinearity gives, in characteristic two,
\[
(x,z)^2=(0,(x_i x_j)_{\{i,j\}\in E,i<j}).
\]
The central coordinate \(z\) is arbitrary and contributes a uniform factor \(q^m\). Hence the prescribed fiber equals \(q^m\) times the number of solutions of the edge-product system \(x_i x_j=y_{\{i,j\}}\). This already proves that all squares lie in the stated central subgroup and that all fourth powers are the identity.

**2. Forced nonzero and zero vertices.** An edge with nonzero label forces both endpoints to have nonzero vertex values, so every vertex of \(W_y\) is nonzero. If an edge of \(\Gamma[W_y]\) had label zero, its two forced-nonzero endpoints would give a contradiction. Thus \(E_y=E(\Gamma[W_y])\) is necessary. Every vertex outside \(W_y\) adjacent to \(W_y\) must be zero, since its incident edge has label zero. The remaining unrestricted vertices are precisely \(R_y=V\setminus N_\Gamma[W_y]\). Their nonzero support must be an independent vertex set of \(\Gamma[R_y]\), because all remaining edge labels vanish. Conversely, every such independent set and every assignment of nonzero values to its vertices extends with zero values elsewhere outside \(W_y\). Hence the contribution from the free vertices is exactly \(I_{\Gamma[R_y]}(q-1)\).

**3. A complete label-consistency test.** Let \(H\) be a connected component of \(B_y\) and choose a spanning tree rooted at \(r\). Pick an arbitrary nonzero root value \(a\) and propagate along every tree edge by \(x_v=y_{\{u,v\}}/x_u\). For each vertex \(v\), the resulting expression has form \(x_v=c_v a^{\epsilon_v}\), where \(\epsilon_v=(-1)^{\operatorname{dist}_T(r,v)}\) and \(c_v\in\mathbb F_q^\times\) is determined by the tree edge labels. A nontree edge \(\{u,v\}\) is satisfied exactly when
\[
 a^{\epsilon_u+\epsilon_v}=y_{\{u,v\}}/(c_uc_v).
\]
When \(\epsilon_u+\epsilon_v=0\), this demands that the right side be one. When the sum is \(2\) or \(-2\), the condition fixes \(a\) uniquely because \(|\mathbb F_q^\times|=q-1\) is odd, so squaring is a bijection. All such constraints must agree. This is a finite, explicit test for any edge labelling, with no implicit existence oracle.

**4. Multiplicities on the nonzero support.** The edge-product map
\[
\phi_H:(\mathbb F_q^\times)^{V(H)}\longrightarrow(\mathbb F_q^\times)^{E(H)},\qquad
(x_v)_v\longmapsto(x_ux_v)_{\{u,v\}} 
\]
is a homomorphism of abelian multiplicative groups. Its kernel on a connected graph is determined by \(x_u x_v=1\) along each edge. On a bipartite component the values alternate between an arbitrary scalar \(a\) and its inverse, giving exactly \(q-1\) kernel elements. On a nonbipartite component an odd cycle forces \(a=a^{-1}\), hence \(a^2=1\). In a group of odd order this forces \(a=1\), and the kernel has size one. Therefore a consistent label has \(q-1\) lifts on each bipartite component and one on each nonbipartite component. Combining independent components, free vertices, and central coordinates proves the displayed fiber theorem.

**5. Image size.** For a square with nonzero edge labels, the endpoint set \(W\) of those edges is uniquely determined by the resulting edge vector and \(\Gamma[W]\) has no isolated vertices. Conversely, take any \(W\in\mathcal W_\Gamma\) and any label vector in the image of \(\phi_{\Gamma[W]}\). Set all vertex values outside \(W\) to zero. This realizes an edge vector whose support is exactly \(E(\Gamma[W])\), hence whose endpoint set is exactly \(W\). For this \(W\), the image of the product map on its connected components has cardinality
\[
 \frac{(q-1)^{|W|}}{(q-1)^{b_\Gamma(W)}}=(q-1)^{|W|-b_\Gamma(W)}.
\]
Different endpoint sets give disjoint edge-vector families. Summation proves the distinct-square formula, including \(W=\varnothing\), which accounts for zero.

**6. Element orders.** A group element squares to the identity exactly when all its edge products vanish, that is, exactly when its nonzero vertex support is independent. Such supports contribute \(I_\Gamma(q-1)\) possibilities, and the central coordinates contribute \(q^m\). Every other element has nonidentity square but fourth power identity, hence has order exactly four. This proves both order counts.

## Verification
A standalone pure-Python program, `checker.py`, implements finite-field multiplication in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), enumerates **all** vertex vectors and all edge-label targets in twenty-four graph/field cases, and compares every target's exact count to an independently structured component-and-independent-set calculation. The program also compares the number of distinct square images against the graph-polynomial formula, checks the identity fiber against the independence polynomial, and directly checks the displayed group-square law for a range of complete group elements. Its successful final message is `ALL_EXACT_SQUARE_FIBER_CHECKS_PASSED 24`.

The nine test graphs include edgeless graphs, single edges, paths, triangles, four-cycles, complete four-vertex graphs, mixed components, and five-cycles. The largest independent full-target census examines all \(4096\) targets for a complete four-vertex graph over \(\mathbb F_4\); tests over \(\mathbb F_8\) include triangles and four-cycles. The proof, not the finite tests, establishes the theorem for arbitrary graphs and finite fields of characteristic two.

For example, for the triangle graph and \(q=4\), its group has \(4^6=4096\) elements. There are \(4^3(1+3(4-1))=640\) square roots of the identity; exactly \(37\) distinct square targets occur. Of these, one is zero, nine have a single nonzero edge, and twenty-seven have all three edges nonzero. Their respective square-root fiber sizes are \(640\), \(192\), and \(64\); the weighted sum is \(640+9\cdot192+27\cdot64=4096\).

For the four-cycle over \(\mathbb F_4\), the \(3^4=81\) all-nonzero edge-label assignments contain only \(3^3=27\) realizable square targets: an alternating-product equality around the even cycle excludes the remaining fifty-four. Each realizable all-nonzero target has \(4^4\cdot3=768\) roots, showing why label consistency is essential and why a zero-target count alone is insufficient.

## Relationship to prior work
Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (arXiv:2107.05564, first publicly available 2021-07-12; Bull. Lond. Math. Soc. 2022), provides the graphical-group construction and a general conjugacy-class-size distribution. The present formula concerns the square **word map** and prescribed central targets, not conjugacy-class enumeration. The derivation uses the explicitly stated group presentation; the group itself is not new.

Youming Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation* (arXiv:2408.09963, 2024-08-19), connects graph independence with isotropic subspaces and abelian subgroups of class-two groups, principally via the odd-characteristic exponent-prime correspondence. Its enumerated objects are subspaces and abelian subgroups, not prescribed-square fibers in even characteristic. The graph independence polynomial is classical and not claimed as an invention here.

General square-root questions for finite groups and standard cyclic-group edge-label propagation are background, not attributed as new. This result gives a graph-uniform complete fiber and square-image computation for a specified family. Conjugacy class sizes alone do not entail a square-map distribution: groups can have identical class-size multisets but different involution counts.

## Limitations
Originality is assessed relative to the specifically inspected sources and available scientific searches, not proved by absence of search matches. An unindexed treatment of class-two characteristic-two group square maps or edge-product algebraic torus maps might already imply part or all of the formulas. This priority risk requires independent literature review. The formula is complete for the given group family and target coordinates but does not classify square fibers for arbitrary class-two groups, for odd characteristic, or for nonsimple graphs with loops. Tests use finite graph and field examples, not an exhaustive survey of all inputs in the theorem's infinite domain. No independent mathematical audit has been performed.

## References
1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first posted 2021-07-12; *Bulletin of the London Mathematical Society* **54** (2022), 1923–1943. https://arxiv.org/abs/2107.05564 ; https://doi.org/10.1112/blms.12665.
2. Y. Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963, first posted 2024-08-19. https://arxiv.org/abs/2408.09963.
3. M. S. Lucido and M. R. Pournaki, *Elements with Square Roots in Finite Groups*, background comparison of the square-word problem in other group families; see https://www.researchgate.net/publication/263906876_Elements_with_Square_Roots_in_Finite_Groups (paper accessible on the cited page; not used as a premise).
