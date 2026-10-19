# Graphic-matroid adjoint spectra of radical-square-zero quiver algebras

## Finding

Let \(Q\) be any finite loopless quiver (parallel arrows are allowed), let \(G\) be its underlying undirected multigraph, and set \(A_Q=\mathbb F_q Q/J^2\), where \(J\) is the arrow ideal. Write \(n=|V(G)|\), \(m=|E(G)|\), and \(c\) for the number of connected components, including isolated vertices. The **adjoint-rank polynomial**
\[
 R_Q(T)=\sum_{a\in A_Q}T^{\operatorname{rank}_{\mathbb F_q}(b\mapsto ab-ba)}
\]
depends only on the cycle matroid \(M=M(G)\) and \(c\), not on the arrow directions. More precisely, with \(\mathcal F(M)\) the set of flats, \(r_M\) the matroid rank function and \(\chi_{M/F}\) the characteristic polynomial of the contraction, 
\[
 \boxed{R_Q(T)=q^c\sum_{F\in\mathcal F(M)}\chi_{M/F}(q)(qT)^{m-|F|}
 \sum_{S\subseteq F}(q-1)^{|S|}T^{r_M(S)}.}
\]
This is an exact formula for every prime power \(q\), including even characteristic.

For a **connected simple unicyclic graph** with unique cycle length \(\ell\ge3\) and \(b\ge0\) bridge edges, put \(B_q(T)=1+(q^2-1)T\). The formula simplifies to
\[
 \boxed{R_Q(T)=B_q(T)^b\left[B_q(T)^\ell+(q-1)(1-T)^\ell
       +q(q-1)^\ell(T^{\ell-1}-T^\ell)\right].}
\]
In particular, this complete rank distribution depends on a unicyclic graph only through the length of its unique cycle and number of bridges, even when its orientations and tree attachments differ.

For **every** field \(k\), every two orientations of the same finite loopless multigraph have *identical defining ideals* for the schemes of ordered pairwise-commuting \(s\)-tuples in \((kQ/J^2)^s\), for all \(s\ge2\), after identifying their vertex and arrow coordinates. In odd characteristic, the cyclic and transitive orientations of a triangle have nonisomorphic commutator Lie algebras, despite these identical commuting-tuple schemes and the common polynomial above. Thus the agreement is not merely a consequence of a Lie-algebra isomorphism.

## Assumptions and scope

All graph and quiver vertex and edge sets are finite. A loopless quiver has no arrow from a vertex to itself; several arrows may have the same unordered endpoints. The quotient \(kQ/J^2\) is unital and has vector-space basis the trivial paths \(e_v\) and individual arrows \(z_e\). The commutator Lie algebra has the same underlying vector space and bracket \([a,b]=ab-ba\).

For a multigraph \(G\), \(M(G)\) is the graphic matroid on its individual (possibly parallel) edges, and \(r_M(S)=|V|-c(V,S)\). A flat is an edge set \(F\) containing every edge whose endpoints are connected in \((V,F)\). For a matroid \(N\) of rank \(r(N)\), the characteristic polynomial normalization is
\[
 \chi_N(q)=\sum_{U\subseteq E(N)}(-1)^{|U|}q^{r(N)-r_N(U)}.
\]
The finite-field formulas treat \(q\) as the cardinality of the coefficient field, not as a formal root of unity. No looped quivers and no extension to all-arity joint-adjoint rank polynomials are asserted. For the geometric commuting-scheme statement, \(k\) can be any field.

## Proof

**Step 1: the commutator rows.** Fix an arrow \(e:u\to v\) and define the vertex functional \(\alpha_e(d)=d_u-d_v\), where \(d=\sum_xd_xe_x\). For arbitrary \(a=d+z\) and \(a'=d'+z'\) the radical-square-zero multiplication gives
\[
 [a,a']_e=\alpha_e(d)z'_e-\alpha_e(d')z_e.
\]
The sign of \(\alpha_e\) changes when the arrow is reversed. The commutator always lies in the span of the arrows; the source and target conventions only affect a consistent overall sign.

**Step 2: a rank formula for each element.** Fix \(a=d+z\). Let \(F(d)=\{e:\alpha_e(d)=0\}\), and let \(S(d,z)=\{e\in F(d):z_e\ne0\}\). In the linear map \(\operatorname{ad}_a:A_Q\to A_Q\), an arrow-basis input produces a diagonal entry \(\alpha_e(d)\) in arrow row \(e\). Thus rows outside \(F(d)\) supply \(m-|F(d)|\) independent pivots and can be eliminated. In the remaining rows, the columns indexed by vertices form an oriented incidence matrix, with row \(e\) multiplied by the nonzero scalar \(z_e\) exactly when \(e\in S(d,z)\). The rank of any oriented incidence matrix over any field equals its graphic matroid rank, by the spanning-forest minor and telescoping-along-cycles arguments. Therefore
\[
 \boxed{\operatorname{rank}(\operatorname{ad}_{d+z})=m-|F(d)|+r_M(S(d,z)).}
\]
This argument is valid in characteristic two and for parallel edges.

**Step 3: colorings and flats.** The edge set \(F(d)\) is a flat: equality of vertex colors propagates along a monochromatic path. Conversely, for a flat \(F\), the assignments \(d\) with \(F(d)=F\) are precisely the proper \(q\)-colorings of the contracted graph \(G/F\). There are \(q^c\chi_{M/F}(q)\) such assignments, by inclusion-exclusion on the noncontracted edges; contraction preserves the number \(c\) of graph components. For each such assignment, the coordinates \(z_e\) on \(E\setminus F\) are arbitrary, giving \(q^{m-|F|}\) choices; on \(F\), specifying the nonzero support \(S\subseteq F\) gives \((q-1)^{|S|}\) choices. Insert Step 2 into the polynomial and sum over flats. This proves the displayed matroid formula and orientation independence.

**Step 4: a single cycle.** For a connected graph with one cycle of length \(\ell\), the \(b\) bridge-edge differences \(d_u-d_v\) can be chosen independently. Each bridge, together with its arrow coordinate, contributes \(B_q(T)=1+(q^2-1)T\); this follows from Step 2 because bridge rows never belong to a graphic circuit.

On the cycle the \(\ell\) signed vertex differences \(\delta_e\) satisfy one relation \(\sum_e\epsilon_e\delta_e=0\), with every \(\epsilon_e\in\{1,-1\}\), and every admissible difference vector has exactly \(q\) vertex potentials. Temporarily assign rank contribution one to each edge for which its pair \((\delta_e,z_e)\) is nonzero. Additive-character orthogonality applied to the single relation gives
\[
 \sum_{\delta,z}\! T^{|\{e:(\delta_e,z_e)\ne(0,0)\}|}
 =B_q(T)^\ell+(q-1)(1-T)^\ell.
\]
Indeed the zero character has one-edge sum \(B_q(T)\), while each nonzero character has one-edge sum \(1-T\). The temporary rank overcounts by exactly one only if *all* cycle differences are zero and *all* cycle arrow coordinates are nonzero: the full cycle has incidence rank \(\ell-1\), not \(\ell\). There are precisely \(q(q-1)^\ell\) such configurations. Replace their contribution \(T^\ell\) by \(T^{\ell-1}\), and multiply by the independent bridge factor. The unicyclic formula follows.

**Step 5: commuting schemes and a nonisomorphism witness.** For an ordered tuple \((a_i)\), each pairwise commutator coordinate is
\[
 [a_i,a_j]_e=\alpha_e(d_i)z_{j,e}-\alpha_e(d_j)z_{i,e}.
\]
Reversing any arrow negates the corresponding polynomials, and replacing generators of an ideal by their negatives leaves the *ideal itself* unchanged. This proves equality of all pairwise-commuting scheme ideals at every arity, over arbitrary fields.

For the directed three-cycle, the three nonzero weights of the abelian quotient acting on the characteristic derived ideal \(J=[A_Q,A_Q]\) have the unique dependence \(\alpha_1+\alpha_2+\alpha_3=0\). For an acyclic (transitive) orientation of the same triangle, the corresponding dependence, after numbering, is \(\beta_1+\beta_2-\beta_3=0\). In odd characteristic the respective one-dimensional relation spaces are not related by a permutation and common scalar. An isomorphism of the commutator Lie algebras would preserve their derived ideals and intertwine the quotient actions, hence would linearly identify the multisets of simultaneous one-dimensional weights; their relation vectors would have to agree up to permutation. This is impossible. The triangle orientations thus have nonisomorphic commutator Lie algebras in every odd characteristic, although their commuting schemes and rank polynomials coincide.

## Verification

The standalone program `verify.py` builds the commutator linear map directly from multiplication matrices and independently evaluates the flat/graphic-rank formula. It exhaustively verifies 17 finite prime-field graph-and-orientation cases, including triangles in two orientations, four-cycles in two orientations, a unicyclic triangle with a bridge, a tree, a diamond, \(K_4\), and parallel arrows. It separately verifies the cycle and bridge-factor formulas in the listed cases. Run with `python verify.py`; success ends with `VERIFY_OK`. Counts for a triangle at \(q=3\) are \((3,18,222,486)\) in adjoint ranks \(0,1,2,3\), for each orientation.

These finite checks are corroboration, not the proof of the all-prime-power, all-graph statement. The proof above verifies the incidence-rank and cycle-correction mechanisms for arbitrary parameters.

## Relationship to prior work

Adachi's work on radical-square-zero algebras [1] uses separated quivers to characterize representation-theoretic finiteness. Bleher–Chinburg–Huisgen-Zimmermann [2] classify irreducible components of module varieties for radical-square-zero algebras. Both establish the importance of the same algebra family, but their stated theorems address module theory rather than the distribution of ranks of inner derivations.

Dutta–Basnet–Nath [3] develop commuting probabilities, bounds and isoclinism invariance for finite rings; those general results do not provide the matroid-flat polynomial or its unicyclic specialization. Gawell–Richey Xantcha [4] study centers and Hochschild cohomology for quadratic quiver quotients, a different invariant. The graphic rank and characteristic-polynomial identities employed above are standard facts from graph and matroid theory; their use here is not claimed as independently new.

Published graph-algebra calculations for forest cases and specific Kronecker quivers account for special consequences, but neither provides the general graph-matroid flat formula or the exact correction for a genuine cycle. The algebraic-group conjugacy formula for certain unicyclic incidence algebras concerns a different group invariant and does not imply the present adjoint-rank classification. All-arity commuting-scheme coincidences for almost-abelian Lie algebras cover some small graph configurations but do not imply the formula for arbitrary graphic matroids or the triangular-cycle weight obstruction.

## Limitations

The general rank distribution is for one adjoint operator at a time, not for joint-adjoint maps of higher arity. Equality of commuting schemes is proved only for reorientations of the *same* underlying edge-labeled graph, not asserted for arbitrary graphs sharing a cycle matroid. The triangle nonisomorphism claim requires odd characteristic. No classification of every isomorphism type of these commutator Lie algebras is claimed. Originality is assessed against identified accessible mathematical sources, not certified absolutely; stronger unlocated literature remains possible.

## References

[1] T. Adachi, *Characterizing \(\tau\)-rigid-finite algebras with radical square zero*, arXiv:1401.1438v1, first publicly posted 7 January 2014. https://arxiv.org/abs/1401.1438

[2] F. M. Bleher, T. Chinburg and B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045v1, 11 July 2014. https://arxiv.org/abs/1407.3045

[3] J. Dutta, D. K. Basnet and R. K. Nath, *On commuting probability of finite rings*, arXiv:1510.08211v1, 28 October 2015. https://arxiv.org/abs/1510.08211

[4] E. Gawell and Q. Richey Xantcha, *Centers of partly (anti-)commutative quiver algebras and finite generation of the Hochschild cohomology ring*, arXiv:1504.00582v1, 2 April 2015. https://arxiv.org/abs/1504.00582
