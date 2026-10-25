# Five minimal octahedral spheres form an integral equivariant basis for the Desargues independence complex

## Finding

Let \(X=\{0,1,2,3,4\}\), and let \(D\) be the Desargues graph: its vertices are the two-element and three-element subsets of \(X\), with an edge \(A-B\) exactly when \(A\subset B\). Write \(K=\operatorname{Ind}(D)\), the ordinary independence complex. For every \(i\in X\), set

\[
M_i=\bigl\{\{A,A\cup\{i\}\}: A\in\tbinom{X\setminus\{i\}}2\bigr\},
\qquad W_i=\bigcup_{e\in M_i}e.
\]

Each \(M_i\) is an induced matching of six graph edges, so \(K[W_i]\cong(S^0)^{*6}\cong S^5\). Orient its fundamental simplicial cycle \(z_i\) by the explicit convention below. **These five are exactly the supports attaining the smallest possible cardinality (twelve) for a nonzero fifth-dimensional integral homology class.** Their classes form an **integral basis**:

\[
\widetilde H_5(K;\mathbb Z)=\mathbb Z[z_0]\oplus\cdots\oplus\mathbb Z[z_4]\cong\mathbb Z^5.
\]

For the full graph-automorphism group \(\operatorname{Aut}(D)\cong S_5\times C_2\), the natural \(S_5\) permutes these five basis elements, while the central complementation automorphism acts by \(-I_5\). Hence, as an **integral** group module,

\[
\boxed{\widetilde H_5(K;\mathbb Z)\cong_{\mathbb Z[S_5\times C_2]}
\mathbb Z[X]_{\mathrm{perm}}\boxtimes\operatorname{sgn}_{C_2}.}
\]

The previously determined nonequivariant homotopy type \(K\simeq S^4\vee\bigvee^5S^5\) is prior work, not a new claim here.

## Assumptions and scope

The two-subsets precede the three-subsets in lexicographic order; these are simplicial vertex labels \(0,\ldots,19\). Every face is an independent vertex set, represented by its twenty-bit indicator. For every cardinality, faces are ordered by the deterministic ascending-vertex insertion algorithm in `verification/verify_desargues_integral_module.py`. Orient simplices by increasing label.

List the six edges of each \(M_i\) in the ascending edge order constructed by that file, and write their ordered endpoint pairs as \((a_j,b_j)\), with each two-subset endpoint first. The oriented fundamental cycle is

\[
z_i=\sum_{\epsilon\in\{0,1\}^6}(-1)^{|\epsilon|}
[a_1^{\epsilon_1},\ldots,a_6^{\epsilon_6}],
\]

where \(a_j^0=a_j\), \(a_j^1=b_j\), and brackets are sorted into increasing simplicial-label order with the usual permutation sign. This definition yields 64 facets with coefficients \(\pm1\) in each cycle. The integral statement concerns this specific ordinary flag complex and its degree-five homology, not the matching complex or a graph-configuration space.

## Proof

**Minimum-support lemma.** Suppose a finite flag complex has a nonzero reduced degree-\(d\) homology class, for \(d\ge0\). Among the induced vertex subsets carrying a nonzero such class, choose an inclusion-minimal set \(W\). Then \(|W|\ge 2d+2\). Indeed, for each \(v\in W\), the deletion–link exact sequence sends a class not supported on \(W\setminus\{v\}\) to a nonzero class of degree \(d-1\) in the link of \(v\). For \(d\ge1\), induction implies the link has at least \(2d\) vertices. Since a nontrivial reduced-homology complex cannot be a cone, \(v\) has a nonneighbor in the flag complex's one-skeleton. Thus \(|W|\ge 2d+2\). The base case \(d=0\) follows from disconnectedness. At equality, the link of every vertex has exactly \(2d\) vertices, so each vertex has exactly one nonneighbor in the one-skeleton; the missing edges form a perfect matching and the induced complex is the boundary of the \((d+1)\)-crosspolytope. For non-minimal supports of exactly \(2d+2\) vertices, minimality holds automatically by the same lower bound.

The lemma implies that any nonzero fifth-homology class needs at least twelve vertices and that every support attaining twelve must correspond to an induced matching of six edges in \(D\). The exhaustive induced-matching enumerator in the verifier reports, for sizes one through seven, respectively,

```
30, 255, 700, 615, 42, 5, 0
```

It independently checks that the five size-six induced matchings are precisely \(M_0,\ldots,M_4\). For fixed \(i\), a two-subset \(A\) avoiding \(i\) is contained in a three-subset \(B\) of the form \(A'\cup\{i\}\) if and only if \(A=A'\). This establishes the induced-matching description and the crosspolytopal sphere geometry.

**Integral generation rather than just rational independence.** Let \(C_j\) denote reduced simplicial chains in dimension \(j\), using the ordered faces above. The relevant ranks are

\[
\operatorname{rank} C_5=1320,\quad \operatorname{rank} C_6=480,\quad
\operatorname{rank} C_7=115.
\]

The exact verifier establishes lower bounds on the integer boundary ranks by calculating modulo \(101\):

\[
\operatorname{rank}_{\mathbb F_{101}}\partial_5=932,\qquad
\operatorname{rank}_{\mathbb F_{101}}\partial_6=383,\qquad
\operatorname{rank}_{\mathbb F_{101}}\partial_7=97.
\]

The integer boundary identities \(\partial_5\partial_6=0\) and \(\partial_6\partial_7=0\) are checked, as are \(\partial_5 z_i=0\) for each \(i\). The verifier then forms the integer matrix

\[
B=[\partial_6\mid z_0\ z_1\ z_2\ z_3\ z_4],
\]

with 1320 rows, 485 columns. `verification/CERTIFICATE.json` gives 388 explicit distinct row indices and 388 distinct column indices, including all five appended cycles. The selected \(388\times388\) integer submatrix has **exact determinant \(-1\)**, verified by 388 successive integer unit pivots with no division by nonunits. Therefore the lattice \(L=\operatorname{im}\partial_6+\sum_i\mathbb Z z_i\) is primitive in \(C_5\), with rank 388.

The matrix rank inequalities now force

\[
\operatorname{rank}_{\mathbb Q}\partial_5=932,\qquad
\operatorname{rank}_{\mathbb Q}\partial_6=383.
\]

For the first, \(L\subseteq\ker\partial_5\) implies \(\operatorname{rank}\partial_5\le1320-388=932\). For the second, \(\operatorname{im}\partial_7\subseteq\ker\partial_6\) and \(\operatorname{rank}\partial_7\ge97\) give \(\operatorname{rank}\partial_6\le480-97=383\). The finite-field results give the reverse inequalities. Since \(\ker\partial_5\) is a primitive rank-388 sublattice of \(C_5\) containing the primitive rank-388 lattice \(L\), they coincide. Since \(\operatorname{rank}\operatorname{im}\partial_6=383\), the five classes provide an integral basis of the quotient \(\ker\partial_5/\operatorname{im}\partial_6\).

**Full symmetry action.** The permutations of \(X\) and the complementation map \(A\mapsto X\setminus A\) generate commuting automorphisms of \(D\). They exhaust its automorphism group: an automorphism preserving the bipartition acts on two-subsets and preserves whether pairs share a three-subset neighbor, thereby preserving the triangular graph \(J(5,2)\). Its five maximum four-cliques are exactly the stars of the five elements of \(X\), forcing an \(S_5\)-permutation. Three-subset images are then forced by their sets of two-subset neighbors. A bipartition-swapping automorphism is complementation composed with one preserving it. For \(\pi\in S_5\), the induced permutation of the six two-subsets of \(X\setminus\{i\}\) is even; hence \(\pi z_i=z_{\pi(i)}\). Complementation reverses each of six matching edges while permuting those edges as three transpositions, giving \(\iota z_i=-z_i\). The verifier checks these identities as equalities of signed integral simplicial chains for all 240 transformations.

## Verification

Using Python 3 standard library only, from this package root run:

```
python3 -I verification/verify_desargues_integral_module.py
```

The program reconstructs all 6212 independence faces including the empty face, all 30 edges and all induced matchings through size seven, all relevant integer simplicial boundaries, the five signed 64-term sphere cycles, the exact 388-pivot unit determinant certificate, the mod-101 rank bounds, and every natural symmetry action. It terminates with `VERIFY_OK_DESARGUES_FIVE_MINIMAL_SPHERES_INTEGRAL_S5_C2_MODULE` on success. The certificate's indices refer only to the face and column orders defined by the verifier.

## Relationship to prior work

Published calculations have already established the nonequivariant Desargues independence-complex homotopy type \(S^4\vee\bigvee^5S^5\), including complete finite Morse proofs. That homotopy equivalence is not the present contribution: it does not identify geometric minimum-support cycle representatives, prove that five specified such classes form an **integral** basis, or determine their signed action under all graph automorphisms. Engström's independence-complex methods, Barmak's general star-cluster suspension, and Tsukuda's general incidence-graph formula concern broader homotopy constructions and do not directly imply this integral geometric module. The linear-strand Betti calculations for the edge ideal of bipartite Kneser graphs address different algebraic invariants. Exact claim-to-implication comparisons are documented in `AUDIT.json`.

## Limitations

The theorem describes only the ordinary independence complex of the named twenty-vertex graph; it does not classify all generalized Petersen graphs or all bipartite Kneser graphs. The topological minimum-support lemma is general, but the five-object classification and unimodular certificate are exact finite computations for this graph. No claim about an integral group representation in degree four is made. The literature comparison cannot rule out independent equivalent work in inaccessible or unindexed sources. This work has undergone only self-review, not an independent mathematical audit.

## References

1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, first public 2005-08-08. https://arxiv.org/abs/math/0508148
2. C. A. Athanasiadis, *Some combinatorial properties of flag simplicial pseudomanifolds and spheres*, arXiv:0807.4369v1, first public 2008-07-28. https://arxiv.org/abs/0807.4369
3. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02. https://arxiv.org/abs/1007.0418
4. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics **12** (2017), 28–46, Corollary 5.3. https://cdm.ucalgary.ca/article/download/62277/46773/178118
5. A. Kumar, P. Singh, R. Verma, *Certain homological invariants of bipartite Kneser graphs*, arXiv:2105.06144v1. https://arxiv.org/abs/2105.06144
6. *The Desargues graph independence complex is \(S^{4}\vee\bigvee^{5}S^{5}\)*, indexed mathematical result, published October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-graph-independence-complex-is-s-4-vee-bigvee-5-s-5--ca55f3b9deba
7. *Independence complex of the Desargues graph is \(S^4\vee\bigvee^5 S^5\)*, indexed mathematical result, published October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-independence-complex-of-the-desargues-graph-is-s-4-vee-bigvee-5--f3b1cf10aadb
