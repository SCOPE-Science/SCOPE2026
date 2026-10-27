# Chromatic thresholds and exact additive-commutator fibers of radical-square-zero quiver algebras

## Finding

Let \(Q=(V,E)\) be any finite directed multigraph, permitting loops, parallel arrows, and isolated vertices. Let \(q\) be any prime power, \(A=\mathbb F_q Q/J^2\), and \(E^*\subseteq E\) the nonloop arrows. Let \(G\) be the underlying loopless simple graph of \(E^*\). For an arrow-linear target \(c=\sum_{e\in E}c_e e\) supported on \(E^*\), let \(H_c\) be the undirected simple graph on \(V\) with one edge \(\{s(e),t(e)\}\) for each nonloop arrow \(e\) with \(c_e\ne0\). Parallel arrows produce only one adjacency for coloring purposes.

**Exact target criterion and minimum length.** The additive commutator subspace equals the span of \(E^*\). For every integer \(t\ge0\), the target \(c\) is a sum of at most \(t\) additive associative commutators \([a,b]=ab-ba\) in \(A\) if and only if
\[
\boxed{\chi(H_c)\le q^{2t}.}
\]
In particular, with the convention that the zero element has length zero and that the chromatic number of an edgeless graph is one,
\[
\boxed{\ell_A(c)=\lceil\log_{q^2}\chi(H_c)\rceil,
\qquad \operatorname{cw}(A)=\lceil\log_{q^2}\chi(G)\rceil.}
\]
The second formula is the maximum minimum length over \([A,A]\). Consequently, every element of \([A,A]\) is a single commutator precisely when \(\chi(G)\le q^2\). The lengths are unbounded as the number of vertices grows over a fixed field: orient the edges of a complete graph.

**All prescribed fiber sizes.** For \(t\ge1\), let \(R_t(c)\) count ordered \(2t\)-tuples \((a_1,b_1,\dots,a_t,b_t)\in A^{2t}\) satisfying \(\sum_i[a_i,b_i]=c\). Put \(m=|E|\). Then \(R_t(c)=0\) if \(c\) has a nonzero diagonal or loop coefficient. Otherwise
\[
\boxed{R_t(c)=q^{(2t-1)m}\!
\sum_{\substack{\kappa:V\to\mathbb F_q^{2t}\\
\kappa(u)\ne\kappa(v)\text{ for every }\{u,v\}\in E(H_c)}}
q^{z_Q(\kappa)},}
\]
where \(z_Q(\kappa)=|\{e\in E:\kappa(s(e))=\kappa(t(e))\}|\) counts arrows with multiplicity, including all loops. This is a finite chromatic/Potts-type partition function, valid in all characteristics. It is unchanged under reversing arrows.

The number of targets having length at most \(t\) is
\[
\boxed{N_t(Q,q)=\sum_{S\subseteq E^*:\;\chi(V,S)\le q^{2t}}(q-1)^{|S|},}
\]
with parallel arrows retained as separate choices in the support sum; exactly-length-\(t\) targets number \(N_t-N_{t-1}\).

For example, a loopless quiver with underlying graph \(K_5\) over \(\mathbb F_2\) has commutator width exactly two: the target that assigns one to every arrow is not a single commutator, whereas every arrow target is a sum of two. This occurs already in a basic algebra of dimension fifteen (five vertices, ten arrows).

## Assumptions and scope

The algebra \(\mathbb F_q Q/J^2\) has basis comprising the vertex idempotents and individual arrows, and products of two arrows vanish. The quiver is finite and may have loops and multiple arrows; its vertex set is nonempty. The notation \([A,A]\) means the \(\mathbb F_q\)-linear span of associative commutators, not the multiplicative group-derived subgroup. Minimum length permits the empty sum for zero. The chromatic number is for an ordinary undirected graph with the full vertex set, ignoring duplicate edges. All fields considered in the counting formulas are finite.

## Proof

**1. Identify the derived subspace and coordinate map.** Write \(a=d+x\), \(b=f+y\), where \(d=\sum_v d_v e_v\), \(f=\sum_v f_v e_v\) are diagonal and \(x=\sum_e x_e e\), \(y=\sum_e y_e e\) are arrow-linear. Using \(J^2=0\) gives the independent arrow equations
\[
[a,b]_e=(d_{s(e)}-d_{t(e)})y_e-(f_{s(e)}-f_{t(e)})x_e.
\]
Every loop coefficient vanishes, as do all diagonal coefficients. Conversely, for any nonloop \(e:u\to v\), \([e_u,e]=e\), so the nonloop arrows span \([A,A]\).

**2. Necessity of proper colorings.** Suppose \(c=\sum_{i=1}^{t}[a_i,b_i]\). At each vertex \(v\) collect the \(2t\) diagonal coefficients into a vector \(\kappa(v)\in\mathbb F_q^{2t}\). If \(\kappa(u)=\kappa(v)\), then the displayed coordinate equation implies \(c_e=0\) for every arrow joining \(u\) and \(v\). Thus the vertex colors are distinct along every edge of \(H_c\), yielding a proper coloring with at most \(q^{2t}\) colors.

**3. Sufficiency, including parallel arrows.** Conversely, suppose that \(H_c\) has a proper coloring by the \(q^{2t}\) vectors of \(\mathbb F_q^{2t}\). Set the diagonal coefficients of \(a_i,b_i\) to the corresponding vector coordinates. For each arrow \(e:u\to v\), the target coefficient of \(\sum_i[a_i,b_i]\) is a linear functional of the \(2t\) free arrow coefficients \(x_{i,e},y_{i,e}\). Its coefficient vector consists of the signed differences of the color coordinates at \(u,v\). When \(c_e\ne0\), the proper-coloring condition makes this functional nonzero, hence onto \(\mathbb F_q\). When \(c_e=0\), choose the arrow variables zero. Distinct arrows have independent variables, including when they are parallel. Therefore the prescribed \(c\) is attained. The statement for \(t=0\) holds because \(q^0=1\) and the only zero-length target is zero.

**4. Minimum length and maximum.** A finite graph \(H_c\) is \(q^{2t}\)-colorable exactly when \(q^{2t}\ge\chi(H_c)\); Step 2 and 3 prove the length formula. Each \(H_c\) is a subgraph of \(G\), hence \(\chi(H_c)\le\chi(G)\). The full-support target with \(c_e=1\) for every nonloop arrow has \(H_c=G\), so it achieves the maximum. For an oriented complete graph on \(n\) vertices, \(\chi(G)=n\) and its width is \(\lceil\log_{q^2}n\rceil\), which is unbounded as \(n\to\infty\).

**5. Fiber formula.** For fixed vertex colors \(\kappa:V\to\mathbb F_q^{2t}\), every arrow \(e\) carries \(2t\) free arrow variables. If its two endpoint colors coincide, its commutator coefficient is forced to zero and there are \(q^{2t}\) assignments when the target coefficient is zero, or none otherwise. If the colors differ, the arrow equation is a nonzero linear equation over \(\mathbb F_q\), so every prescribed target coefficient has exactly \(q^{2t-1}\) solutions. All arrows are independent. Multiplying these factors yields \(q^{(2t-1)m+z_Q(\kappa)}\), and summing over exactly the permitted colorings gives the displayed fiber formula. A nonzero diagonal or loop target cannot occur by Step 1. Orientation reversal changes signs of the linear equations but not their ranks or solution counts.

**6. Number of targets at each length.** Every support \(S\subseteq E^*\) determines a graph \((V,S)\); there are precisely \((q-1)^{|S|}\) coefficient assignments of support exactly \(S\). Step 2–3 imply that all such targets have length at most \(t\) exactly when \(\chi(V,S)\le q^{2t}\). Sum over supports. Subtract successive cumulative counts for the exact-length distribution. This completes the proof.

## Verification

Run `python3 verify.py` with standard Python 3. The checker independently uses the original truncated-quiver multiplication, explicitly enumerates all element pairs in five small-field/quiver cases (including loops and parallel arrows), and compares every target fiber against a separate vertex-coloring count. It also exhaustively checks that \(K_4\) admits four colors, \(K_5\) does not, and \(K_5\) admits sixteen, as required over \(\mathbb F_2\). It returns `VERIFY_OK_QUIVER_CHROMATIC_COMMUTATOR_WIDTH`. These finite checks support but do not establish the theorem, whose proof is algebraic and exact.

## Relationship to prior work

The standard radical-square-zero quiver construction is classical. Adachi (2014) and Bleher–Chinburg–Huisgen-Zimmermann (2014) investigate representation-theoretic and geometric properties of these algebras; their examined statements do not identify prescribed additive commutators with proper graph colorings. A prior exact adjoint-rank enumeration for general loopless quivers yields commuting-pair totals and a coordinate bracket identity but does not determine nonzero target fibers or the minimum number of commutators per target. A published two-vertex generalized Kronecker calculation gives complete commutator fibers for that special family; the present statement supplies an all-quiver formula and a sharp chromatic threshold not present there. Finite algebra-group commutator identities concern multiplicative commutators in \(1+J\), which is abelian here because \(J^2=0\).

The fiber identity is an explicit weighted proper-coloring sum akin to a multivariate Potts partition function. It distinguishes the complete target-dependent commutator distribution from the adjoint-rank polynomial or the commuting probability, which only control portions of this distribution.

## Limitations

This result concerns associative additive commutators in quotients \(\mathbb F_q Q/J^2\), not Lie word values in unrelated algebras, group commutators, or path algebras retaining paths of length at least two. The algorithmic coloring interpretation can be costly for large graphs. An older statement in different terminology could cover the theorem; priority beyond the examined primary material is not independently established.

## References

1. T. Adachi, “Characterizing \(\tau\)-rigid-finite algebras with radical square zero,” arXiv:1401.1438v1, publicly submitted 7 January 2014; https://arxiv.org/abs/1401.1438.
2. F. M. Bleher, T. Chinburg, and B. Huisgen-Zimmermann, “The geometry of finite dimensional algebras with vanishing radical square,” arXiv:1407.3045v1, publicly submitted 11 July 2014; https://arxiv.org/abs/1407.3045.
3. A. Nasr-Isfahani, “Singular equivalence of finite dimensional algebras with radical square zero,” arXiv:1603.04191v1, publicly submitted 14 March 2016; https://arxiv.org/abs/1603.04191.
4. Z. Halasi, “On the characters and commutators of finite algebra groups,” freely accessible primary manuscript https://zhalasi.web.elte.hu/papers/01.alggrp.pdf. This concerns commutators of algebra groups, not additive commutators in the full algebra.
5. “Commutator fibers and commuting probabilities of finite Kronecker path algebras,” publicly accessible result and proof at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d (two-vertex special case).
