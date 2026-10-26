# Matching-controlled minimum faithful degree of radical-square-zero quiver algebras

## Finding

Let \(k\) be **any** field and let \(Q\) be a finite quiver, allowing loops and parallel arrows. Let \(J\) denote the arrow ideal and put \(A=kQ/J^2\). Write \(m_{uv}\) for the number of arrows from vertex \(u\) to vertex \(v\). Define the minimum faithful module degree
\[
\mu_k(A)=\min\{\dim_k M:M\text{ is a faithful finite-dimensional left }A\text{-module}\}.
\]
Let \(H\) be the set of vertices with an incoming arrow, and \(T\) the set with an outgoing arrow. For **arbitrary** arrow multiplicities, there is an exact field-independent integer optimization:
\[
\mu_k(A)=\min\left\{\sum_{v\in Q_0}\max(1,s_v+t_v):
\begin{array}{l}
s_v,t_v\in\mathbb Z_{\ge0};\quad s_v=0\ (v\notin H),\quad t_v=0\ (v\notin T),\\
s_v\ge1\ (v\in H),\quad t_v\ge1\ (v\in T),\\
t_u s_v\ge m_{uv}\quad\text{for all }u,v\in Q_0
\end{array}\right\}.
\]
In particular, when \(m_{uv}\le2\) for every ordered vertex pair, construct a bipartite graph \(D_Q\) with a left copy \(u_{\mathrm{out}}\) of each \(u\in T\), a right copy \(v_{\mathrm{in}}\) of each \(v\in H\), and an edge \(u_{\mathrm{out}}v_{\mathrm{in}}\) **exactly when** \(m_{uv}=2\). If \(\nu(D_Q)\) is its maximum matching number, then
\[
\boxed{\mu_k(A)=|Q_0|+|H\cap T|+\nu(D_Q).}
\]
This formula is valid in all characteristics, over finite and infinite fields, and also for loops and arrows in opposite directions. Optimal module decompositions can be built from any minimum vertex cover of \(D_Q\). Thus the minimum matrix size \(d\) for a unital embedding \(A\hookrightarrow M_d(k)\) is computable by bipartite matching in the two-arrow family.

A sharp compression example is the quiver with \(r\) sources and \(r\) sinks, two parallel arrows from every source to every sink, and no other arrows. Its algebra has dimension \(2r+2r^2\), but its minimum faithful module dimension is exactly \(3r\) for every field and every \(r\ge1\). This quadratic-to-linear compression is an instance of the same formula, not a separate hypothesis.

## Assumptions and scope

The vertex set \(Q_0\) is finite and nonempty, and \(Q_1\) is finite. The algebra is the unital path algebra modulo all paths of length at least two; its basis comprises the orthogonal vertex idempotents and the individual arrows. A left representation assigns a space \(M_v=e_vM\) to each vertex and a linear map \(M_u\to M_v\) to each arrow \(u\to v\); all composites of two arrow maps must vanish. A faithful representation means its algebra homomorphism to \(\operatorname{End}_k(M)\) is injective. The quantity \(\mu_k(A)\) is a *minimum dimension*, not merely a module with no faithful proper submodule or quotient. No assumption on acyclicity, the field cardinality, or the representation type is used.

## Proof

**1. Forced source and target layers.** Let \(M\) be faithful. Set \(S_v=\sum_{a:u\to v}\operatorname{im}M(a)\subseteq M_v\), and put \(s_v=\dim_k S_v\) and \(t_v=\dim_k(M_v/S_v)\). Every arrow leaving \(v\) kills \(S_v\), since any composite of two arrows represents a path in \(J^2=0\). Hence each arrow \(u\to v\) factors as a map \(M_u/S_u\to S_v\). For fixed ordered vertices \(u,v\), the \(m_{uv}\) arrow maps must be linearly independent: otherwise a nonzero element of \(e_vJe_u\) annihilates \(M\), contradicting faithfulness. Therefore
\[
m_{uv}\le\dim_k\operatorname{Hom}_k(M_u/S_u,S_v)=t_us_v.
\]
The fact that all arrows act nontrivially gives \(s_v\ge1\) on \(H\) and \(t_u\ge1\) on \(T\). Faithfulness of the nonzero vertex idempotents gives \(\dim M_v\ge1\); thus \(\dim M=\sum_v\dim M_v\ge\sum_v\max(1,s_v+t_v)\). By definition \(s_v=0\) outside \(H\). If \(v\notin T\), the quotient coordinate \(t_v\) is unnecessary for the lower-bound optimization and can be replaced by zero without affecting any product constraint; doing so can only decrease the displayed objective. Hence every faithful module yields a feasible objective no larger than its dimension.

**2. Sufficiency over any field.** Conversely, start with any integers feasible in the displayed optimization. For every nonisolated vertex let \(V_v=k^{s_v}\oplus k^{t_v}\), with distinguished summands \(S_v^0,T_v^0\); for an isolated vertex take \(V_v=k\) and let all arrows act as zero. For each ordered pair \(u,v\), choose \(m_{uv}\) **distinct matrix units** in \(\operatorname{Hom}_k(T_u^0,S_v^0)\), which is possible because \(t_us_v\ge m_{uv}\). Let those matrix units represent the separate arrows from \(u\) to \(v\), extended by zero on \(S_u^0\). Since every arrow has image in a distinguished \(S^0\) and every arrow annihilates all such subspaces, all length-two products vanish. Hence this is an \(A\)-module of the asserted dimension.

The action is faithful: vertex idempotents act on mutually orthogonal nonzero vertex blocks. Any linear relation among the represented idempotents and arrows, evaluated on the semisimple quotients and on sink or isolated blocks, first forces every idempotent coefficient to vanish; the remaining arrow coefficients vanish because the chosen matrix units are linearly independent within each \(\operatorname{Hom}(T_u^0,S_v^0)\), and distinct ordered pairs occupy separate blocks. No field-size or generic-position argument is involved. This proves the integer optimization formula.

**3. Matching reduction.** Suppose every \(m_{uv}\in\{0,1,2\}\). Set each active \(s_v,t_v\) initially to one and inactive coordinates to zero, giving the base dimension \(|Q_0|+|H\cap T|\). Multiplicity-one arrows already satisfy \(t_us_v\ge1\). A doubled arrow pair requires \(t_us_v\ge2\), equivalently \(t_u\ge2\) or \(s_v\ge2\). Values greater than two confer no further advantage, so any minimizing solution may be truncated to \(1\) or \(2\) on active coordinates. Upgrading \(t_u\) or \(s_v\) from one to two costs exactly one dimension. The selected upgrades meet every double-arrow edge of \(D_Q\); conversely any vertex cover supplies feasible upgrades. The minimum extra cost is therefore its minimum vertex-cover number. Because \(D_Q\) is bipartite (including when \(u=v\) in \(Q\), as its two copies remain distinct), König's matching-cover theorem identifies that number with \(\nu(D_Q)\). The optimal matrix-unit construction above completes the proof.

**4. Compression family.** For \(r\) sources and \(r\) sinks joined by two arrows in each direction from source to sink, \(H\cap T=\varnothing\) and \(D_Q=K_{r,r}\), with matching number \(r\). Thus \(\mu_k(A)=2r+r=3r\). The algebra has \(2r\) vertex basis vectors and \(2r^2\) arrow basis vectors, giving dimension \(2r+2r^2\).

## Verification

The standalone `verify.py` checks all \(3^4=81\) two-vertex quiver multiplicity matrices with entries at most two, plus 120 pseudorandom three-vertex and 60 pseudorandom four-vertex cases (261 cases total). For every case it independently exhausts the finite integer feasible region, computes maximum matching by backtracking, constructs explicit matrix-unit arrow actions, and checks dimension, arrow-map supports, linear independence and zero length-two products. It additionally tests all \(5^4=625\) two-vertex matrices with multiplicities up to four against direct integer optimization and explicit constructions. The script prints `VERIFY_OK_FAITHFUL_MATCHING 261 max2_quivers 625 max4_quivers`. These are finite consistency checks; the exact all-quiver theorem follows from the proof above and does not rely on exhaustive graph enumeration.

## Relationship to prior work

Bekkert--Drozd (initial preprint 2008) develop the representation theory and derived categories of radical-square-zero quiver algebras. They provide the general quiver framework, not the stated minimum faithful degree or a matching-cover formula. Bergman (initial preprint 2013) studies faithful modules over Artinian rings; his Theorem 11 gives a **different inequality** relating the top, socle, and bimodule socle under minimality and infinite-field hypotheses. This does not yield the exact smallest possible total dimension in the present split quiver family; moreover the present formula applies over every field. Drozd (2026) examines species correspondences and Auslander--Reiten quivers, not minimum faithful matrix sizes. Classical König matching-cover duality is an ingredient, not asserted as new.

The claim here is the simultaneous exact feasibility criterion for all arrow multiplicities and the sharp bipartite-matching specialization for at most two arrows per ordered pair. The common use of a separated or bipartite quiver in other representation-theoretic questions does not by itself establish the implication to this faithful-degree optimization. A priority risk remains that an earlier implicit quiver-module calculation or an equivalent embedding-dimension classification gives the same result.

## Limitations

The simple closed matching formula assumes at most two arrows for each **ordered pair**, though the integer optimization covers arbitrary multiplicities. The theorem gives the minimum total dimension and optimal split profiles, not a classification of all faithful modules up to isomorphism. It concerns associative unital algebra embeddings, not Lie algebra embeddings or irreducible representations. Historical-priority verification is not exhaustive, and no independent mathematical audit has been performed.

## References

1. V. Bekkert and Y. Drozd, *Derived categories for algebras with radical square zero*, arXiv:0812.4818v1, initially available 2008-12-28; introduction and Sections 1--2. https://arxiv.org/abs/0812.4818
2. G. M. Bergman, *Minimal faithful modules over Artinian rings*, arXiv:1310.5365v1, initially available 2013-10-20; Sections 1, 2, 4--5, especially Theorem 11. https://arxiv.org/abs/1310.5365
3. Y. A. Drozd, *On representations of algebras with radical square zero*, arXiv:2602.14171v1 (2026-02-15), especially introduction and Sections 1--3. https://arxiv.org/abs/2602.14171
4. D. König, *Graphen und Matrizen*, Matematikai és Fizikai Lapok **38** (1931), 116--119 (matching--cover theorem; classical background).
