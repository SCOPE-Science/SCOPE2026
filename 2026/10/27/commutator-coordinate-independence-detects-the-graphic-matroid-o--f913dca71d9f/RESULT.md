# Commutator-coordinate independence detects the graphic matroid of a radical-square-zero path algebra

## Finding

Let \(Q=(V,E)\) be any finite quiver with **no oriented path of length two**, allowing isolated vertices and parallel arrows, over the finite field \(\mathbb F_q\). Let \(A=\mathbb F_qQ\). Choose \(X,Y\) independently uniformly from \(A\), and express their additive commutator in the canonical arrow basis as \([X,Y]=\sum_{e\in E}C_e e\). Let \(G\) be the underlying undirected multigraph of \(Q\).

**Independence–matroid theorem.** For every \(T\subseteq E\), the random variables \((C_e)_{e\in T}\) are mutually independent **if and only if** the multigraph \((V,T)\) is a forest. Thus the labelled coordinate-independence system of the random commutator is exactly the graphic matroid of \(G\), including parallel-edge two-circuits. This assertion holds in every finite characteristic.

**Complete prescribed-fiber theorem.** Fix \(c=(c_e)_{e\in E}\in\mathbb F_q^E\), let \(S=\{e:c_e\ne0\}\), and write \(R_Q(c)\) for the number of ordered pairs \((X,Y)\in A^2\) with \([X,Y]=\sum_e c_e e\). Then
\[
R_Q(c)=q^{|E|}\sum_{F\subseteq E\setminus S}(q-1)^{|F|}\chi_{(G/F)[S]}(q^2).
\]
Here \(G/F\) contracts the selected labelled edges \(F\), preserving all remaining edges; \((G/F)[S]\) is the spanning multigraph consisting only of the edges labelled by \(S\) after contraction; and \(\chi_H(Q_0)\) counts proper \(Q_0\)-colorings of the vertices of a finite multigraph \(H\). In particular it is zero if there is a loop. The multiplicity depends on \(c\) only through its support \(S\).

For \(c=0\), setting \(k(F)\) to the number of connected components of \((V,F)\), including isolated vertices, yields
\[
R_Q(0)=q^{|E|}\sum_{F\subseteq E}(q-1)^{|F|}q^{2k(F)}.
\]
This is a Fortuin–Kasteleyn random-cluster specialization \(q^{|E|}Z_G(q^2,q-1)\). The commuting probability is the preceding count divided by \(q^{2(|V|+|E|)}\).

If \(G\) is a forest with \(k\) components, \(m=|E|\), and \(s=|S|\), the complete fiber simplifies to
\[
R_Q(c)=q^{2k}(q^3+q^2-q)^{m-s}(q^3-q)^s.
\]
For each individual arrow the probability of zero is \(q^{-1}+q^{-2}-q^{-3}\), while the probability of any one specified nonzero field value is \(q^{-1}-q^{-3}\).

## Assumptions and scope

The quiver is finite, with no directed path of length two. Consequently every non-isolated non-source is a sink and the arrow radical satisfies \(J^2=0\). A quiver with parallel arrows is permitted; an arrow loop is not, since it would itself form a directed path of length two. All algebra elements and commutator pairs are uniformly sampled with respect to the canonical vertex-idempotent and arrow basis. The result is about these **labelled arrow coordinates**, not an invariant claimed to survive an arbitrary unlabelled algebra isomorphism or a change of radical basis. The prime-power field size \(q\ge2\) is arbitrary.

The chromatic polynomial counts vertex colorings by \(q^2\) colors; it is not the characteristic polynomial of an algebra. By a forest in a multigraph we mean a set of edges with no undirected cycles, including length-two cycles formed by parallel edges. The empty edge set is allowed; the formulas then correctly give \(R_Q(0)=q^{2|V|}\) and a vacuous independence condition.

## Proof

**Step 1 — exact coordinate commutator.** Write
\[
X=\sum_{v\in V}a_ve_v+\sum_{e\in E}x_ee,
\qquad
Y=\sum_{v\in V}b_ve_v+\sum_{e\in E}y_ee.
\]
The path-algebra multiplication satisfies \(e_ue=e\) and \(ee_v=e\) if \(e:u\to v\), and products of two arrows vanish. Therefore vertex-idempotent coefficients cancel in the additive commutator; for each arrow \(e:u\to v\),
\[
C_e=(a_u-a_v)y_e-(b_u-b_v)x_e.
\]
Set the independent uniform two-coordinate vertex labels \(z_v=(a_v,b_v)\in\mathbb F_q^2\). Conditional on all vertex labels, distinct arrows use independent pairs \((x_e,y_e)\). If \(z_u=z_v\), then \(C_e=0\) deterministically and each prescribed zero value has \(q^2\) lifts of the arrow coefficients. If \(z_u\ne z_v\), the arrow-coordinate map to \(\mathbb F_q\) is a nonzero linear functional, hence surjective, and every prescribed value has exactly \(q\) lifts.

**Step 2 — prescribed-fiber formula.** For a fixed target support \(S\), every edge in \(S\) must join two differently labelled vertices, and contributes \(q\) arrow-coefficient lifts. Every edge outside \(S\) contributes \(q^2\) lifts for equal vertex labels and \(q\) for distinct labels. Writing \(m=|E|\) therefore gives the exact finite sum
\[
R_Q(c)=q^m\sum_{z\in(\mathbb F_q^2)^V}
\prod_{e=uv\in S}{\bf1}_{z_u\ne z_v}
\prod_{e=uv\notin S}\bigl(1+(q-1){\bf1}_{z_u=z_v}\bigr).
\]
Expand the second product over \(F\subseteq E\setminus S\). The indicator conditions require each endpoint of every edge in \(F\) to have the same label, so assignments factor through the connected components of \((V,F)\), namely vertices of \(G/F\). The remaining inequalities on \(S\) are precisely proper \(q^2\)-colorings of \((G/F)[S]\). If an edge in \(S\) is collapsed to a loop, no such coloring exists. This proves the complete formula, including the dependence only on support. For \(S=\varnothing\), proper coloring constraints vanish and their count is \((q^2)^{k(F)}\), proving the Fortuin–Kasteleyn specialization.

**Step 3 — independent arrow sets in forests.** Fix \(T\subseteq E\) that is a forest. On each component of \((V,T)\), choose one root. The linear change of variables from all vertex labels \((z_v)\) to one root label per component together with all edge differences \((z_u-z_v)_{e\in T}\) is a bijection over \(\mathbb F_q^2\), because a tree has unique paths. Thus the \(T\)-indexed differences are mutually independent and uniform on \(\mathbb F_q^2\). The independent arrow-coefficient pairs \((x_e,y_e)\) then imply the corresponding \(C_e\)'s are mutually independent, irrespective of arrows outside \(T\).

**Step 4 — every cycle forces dependence.** For an arbitrary \(T\subseteq E\), conditioning on vertex labels and using the zero probabilities from Step 1 gives
\[
\Pr(C_e=0\ \forall e\in T)
=q^{-|T|}\sum_{F\subseteq T}(q-1)^{|F|}q^{-2r(F)},
\quad r(F)=|V|-k(F).
\]
Indeed each edge has conditional zero probability \(q^{-1}[1+(q-1){\bf1}_{z_u=z_v}]\), and imposing all equality constraints for edges in \(F\) has probability \(q^{-2r(F)}\). Taking \(|T|=1\), every coordinate has marginal zero probability
\[
p_0=q^{-1}\bigl(1+(q-1)q^{-2}\bigr)=q^{-1}+q^{-2}-q^{-3}.
\]
If these \(|T|\) variables were mutually independent, their joint zero event would have probability
\[
p_0^{|T|}=q^{-|T|}\sum_{F\subseteq T}(q-1)^{|F|}q^{-2|F|}.
\]
For every \(F\), the graphic rank satisfies \(r(F)\le |F|\), with equality precisely for forests. Every summand is nonnegative and \(q-1>0\). If \(T\) contains a cycle, choose a cyclic \(F\subseteq T\): its term makes the actual joint-zero probability **strictly larger** than the product of its marginals; no other term can cancel. Thus mutual independence fails. Steps 3 and 4 establish the if-and-only-if statement and the graphic-matroid reconstruction.

**Step 5 — forest closed form.** If \(G\) is a forest with \(k\) connected components, the bijection from vertex labels to the \(k\) root labels and all \(m\) edge differences gives \(q^{2k}\) choices of roots. For a single edge, summing over its difference and arrow coefficient pair yields \(q^2+(q^2-1)q=q^3+q^2-q\) assignments to force commutator coordinate zero, or \((q^2-1)q=q^3-q\) assignments for each prescribed nonzero value. Taking the product over edges proves the final formula. Dividing by the \(q^4\) total possibilities per edge gives the stated coordinate probabilities.

All statements are finite exact identities and require no limiting argument.

## Verification

Run `python3 check_commutator_matroid.py` with Python 3 and no third-party dependencies. The checker creates path-algebra multiplication independently of the proof's coordinate formula, exhaustively enumerates each ordered pair of algebra elements, and constructs each commutator vector. It compares every prescribed fiber against an independently implemented edge-contraction and proper-coloring expansion. It tests the forest-versus-cycle independence criterion for every subset of arrows by exact integer cross-multiplication, avoiding floating point comparisons.

Thirteen small configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) passed, including an undirected four-cycle, parallel arrows, stars, disconnected forests, and nonprime characteristic-two fields. A total of \(238{,}274\) ordered pairs was directly enumerated. The ending sentinel is `ALL_GRAPH_COMMUTATOR_CHECKS_PASSED 13 238274`. Exhaustive finite tests corroborate the general proof but do not prove it for unbounded quiver size or arbitrary prime powers.

## Relationship to prior work

Dutta, Basnet and Nath (2018) study zero-commutator probabilities in finite rings, especially through counts of distinct centralizers. Their results do not prescribe all commutator coordinates of general square-zero quiver path algebras or recover a graphic matroid. The previously published result *Commutator fibers and commuting probabilities of finite Kronecker path algebras* treats the **two-vertex, parallel-arrow** case. Its exact commutator fibers and commuting probability are **already covered** in that case and are not separately claimed as new; its result does not supply the forest-versus-cycle dependence theorem or the arbitrary multi-vertex chromatic-fiber formula. Green and Schroll (2023), despite the title *The Commuting Algebra*, study a quotient of a path algebra by differences of parallel paths, not these random additive commutators. Sokal (2005) develops the well-known Fortuin–Kasteleyn/Potts and chromatic polynomial framework, which is an explicitly credited counting ingredient.

The contribution assessed here is the exact independence matroid of random commutator coordinates, together with the support-resolved full-fiber formula for arbitrary finite quivers having no oriented path of length two. Unlike a total commuting-pair count, the full law records dependencies along all cycles and the precise multiplicity of every commutator vector. The no-directed-length-two restriction is essential to this arrow-local argument. Prior published work was compared by theorem implication, not just title matching.

## Limitations

The theorem is proved only when the quiver has no oriented path of length two. It does not assert the same law for algebras with nonzero products of arrows. The independence matroid is attached to **specified labelled arrow coordinates** in a canonical quiver presentation; no algebra-isomorphism invariant is claimed for arbitrary radical bases. The zero-commutator formula by itself is a known type of Potts identity once the elementary bilinear reduction is made. The stronger full-fiber and graphic-matroid assertions may have undiscovered equivalent formulations in finite-algebra, graphical-model, or bilinear random-field literature. Primary literature and record searches are not a uniqueness certificate; no independent audit has been performed.

## References

1. J. Dutta, D. K. Basnet, and R. K. Nath, *Commuting probabilities of \(n\)-centralizer finite rings*, arXiv:1803.04111v1, public 12 March 2018. Primary MSC 16U70 and 16U80.
2. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169v1, public 16 February 2023. Primary MSC 16P10.
3. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1, public 25 March 2005; *Surveys in Combinatorics 2005*, 173–226.
4. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, publicly accessible mathematical result, October 2026. Its two-vertex result is a covered special case and explicitly excluded from the originality claim.
