# Graph-indexed Boolean Čech nerves carry the integral oriented-edge persistence module

## Finding
For a simple graph \(H=([n],E)\) and each integer \(n\ge1\), define
\[
X_H=\{\varnothing\}\cup\{\{i\}:i\in[n]\}\cup\{\{i,j\}:\{i,j\}\in E\}.
\]
Equip this set with Hamming distance \(d(A,B)=|A\triangle B|\). Its **intrinsic closed-radius-one Čech nerve** \(K_H\) has vertices \(X_H\), and a nonempty \(\sigma\subseteq X_H\) is a face exactly when there is \(w\in X_H\) with \(d(w,x)\le1\) for all \(x\in\sigma\).

Then
\[
K_H\simeq\bigvee_{e\in E}S^2,
\qquad
\widetilde H_k(K_H;\mathbb Z)\cong
\begin{cases}C_1(H;\mathbb Z)&k=2,\\0&k\ne2,\end{cases}
\]
where the wedge over an empty edge set is a point. Here \(C_1(H;\mathbb Z)\) is the free abelian group on oriented edges modulo \([j,i]=-[i,j]\), **not** the graph's first homology. The integral isomorphism is natural for graph isomorphisms and inclusions on the same finite vertex set.

More precisely, for each edge \(e=\{i,j\}\), with \(i<j\), the four vertices
\(\varnothing,\{i\},\{j\},e\) span the boundary of a tetrahedron (but not its interior). Orient its fundamental two-cycle by the formal boundary
\[
z_{ij}=\partial[\varnothing,\{i\},\{j\},e]
=[\{i\},\{j\},e]-[\varnothing,\{j\},e]
+[\varnothing,\{i\},e]-[\varnothing,\{i\},\{j\}].
\]
The classes \([z_{ij}]\) form a **primitive integral basis** of \(\widetilde H_2(K_H;\mathbb Z)\). For every \(E\subseteq E'\), the inclusion \(K_H\hookrightarrow K_{([n],E')}\) maps these basis classes identically. An edge-by-edge filtration therefore yields a free, injective, split degree-two integral persistence module, with one persistent generator born for every added edge.

Every automorphism \(g\in\operatorname{Aut}(H)\) acts by the signed oriented-edge permutation. Its trace equals
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(K_H;\mathbb Q)\bigr)
=\#\{\{i,j\}\in E:g(i)=i,\ g(j)=j\}
-\#\{\{i,j\}\in E:g(i)=j,\ g(j)=i\}.
\]
For \(H=K_n\), this identifies the integral \(S_n\)-module with \(\bigwedge^2\mathbb Z^n\), and the trace is \(\binom{f(g)}2-t(g)\), where \(f(g)\) and \(t(g)\) count fixed vertices and transpositions in the cycle decomposition of \(g\).

## Assumptions and scope
The vertex set is a *truncated* Boolean family of sizes zero, one and selected size-two subsets. Čech witnesses are required to belong to this same finite set \(X_H\); allowing points from an ambient continuous cube or additional Boolean subsets changes the construction. Only closed balls of radius exactly one are considered (often called Čech scale two). The graph may be disconnected or have isolated vertices. Homology uses integral simplicial chains. Naturality for edge inclusion uses the same ground set \([n]\), and for graph isomorphisms uses the induced coordinate relabeling.

## Proof
**1. Partition by the possible witness.** Write \(B\subseteq K_H\) for the union of full simplices on the closed unit balls about \(\varnothing\) and all singleton witnesses. The ball about \(\varnothing\) consists of \(\varnothing\) and all singletons. For a singleton \(\{i\}\), its ball consists of \(\varnothing,\{i\}\) and the selected pairs \(\{i,j\}\in E\) incident with \(i\). In every one of these balls \(\varnothing\) occurs, so \(B\) is the simplicial cone on the vertex \(\varnothing\). In particular it is contractible, naturally under every coordinate relabeling.

The closed ball about a selected pair \(e=\{i,j\}\) consists exactly of \(e,\{i\},\{j\}\). It therefore contributes precisely the triangle \(T_e=[\{i\},\{j\},e]\) and its faces. None of these triangles belongs to \(B\): no size-zero or size-one witness is within one of all three vertices. Their three edges do lie in \(B\): the edge of singleton vertices occurs in the ball of \(\varnothing\), while the other two occur in the respective singleton balls. Thus \(T_e\cap B=\partial T_e\). For distinct \(e,e'\), the intersection \(T_e\cap T_{e'}\) is contained in \(B\), since their distinct pair vertices prevent them sharing a two-simplex. These witness cases exhaust the faces of \(K_H\).

**2. Quotient and homotopy type.** Collapsing \(B\) to one point gives a canonical quotient
\[
|K_H|/|B|\cong\bigvee_{e\in E}|T_e|/|\partial T_e|
\cong\bigvee_{e\in E}S^2.
\]
The inclusion of the nonempty contractible simplicial subcomplex \(B\) is a cofibration. Therefore its quotient map is a homotopy equivalence. This proves the full homotopy type, including the empty-edge case.

**3. Primitive integral generators.** The relative chain complex \(C_*(K_H,B;\mathbb Z)\) is free on the triangles \(T_e\), all in degree two, with zero differential. The long exact sequence of \((K_H,B)\) and contractibility of \(B\) identify \(\widetilde H_2(K_H;\mathbb Z)\) canonically with \(H_2(K_H,B;\mathbb Z)=\bigoplus_{e\in E}\mathbb Z[T_e]\); every other reduced integral homology group vanishes. The displayed oriented tetrahedral boundaries \(z_{ij}\) are actual cycles because all four of their faces lie in \(K_H\). Under the relative quotient \([z_{ij}]\) maps to \([T_e]\) with coefficient \(+1\), so these integral classes form a full primitive basis, not just rationally independent classes.

**4. Equivariance and filtrations.** Coordinate relabeling preserves the empty set, singleton witnesses and selected-pair witnesses, and sends \(T_{ij}\) to \(T_{g(i)g(j)}\). Since an orientation of this relative triangle begins with its two singleton vertices, reversing their order contributes \(-1\). The canonical relative identification consequently agrees with the *oriented* graph edge module over \(\mathbb Z\). In an edge inclusion \(E\subseteq E'\), the cone subcomplex and all old triangular generators include naturally in the larger construction. Naturality of relative homology proves that the induced homology map is the standard primitive coordinate inclusion of the free edge lattices. The action formula follows. For the complete graph the map \([i,j]\mapsto e_i\wedge e_j\) yields \(C_1(K_n;\mathbb Z)\cong\bigwedge^2\mathbb Z^n\).

## Verification
A standalone standard-library checker, `verify.py`, independently enumerates the intrinsic unit-ball nerve for 121 finite graph instances. It verifies the cone structure and the exact relative two-triangle presentation in all 121 cases, independently computes mod-two reduced homology in 115 cases, and checks 293 signed simplicial Lefschetz traces against the oriented-edge character for graph automorphisms. Run `python3 verify.py`; all four `PASS` assertions must appear. These finite tests corroborate, but do not replace, the all-graph proof given above.

## Relationship to prior work
Biswas, *Čech complexes for finite sets* (arXiv:2609.32786v1, 26 September 2026), especially Lemma 4.1 and §4.4, shows that adding consecutive two-element Boolean vertices produces one new two-sphere in the nonequivariant homotopy type. In particular the known complete weight-two truncation has \(\binom n2\) spheres. That special-case sphere count is **not** claimed to be new here. The additional statement established here is an **arbitrary graph-indexed** natural object with its **primitive integral oriented-edge module**, automorphism signs, and split persistence under arbitrary edge insertion. The canonical relative-cycle proof provides those features without selecting a cardinality reverse-lexicographic order.

Adams, Shukla and Singh, *Čech complexes of hypercube graphs* (arXiv:2212.05871), study the full Boolean hypercube graph's intrinsic Čech nerve. A full hypercube has all Boolean weight levels, unlike \(X_H\), so its equivariant rational homology formulas do not imply the integral graph-indexed filtered statement here.

## Limitations
The homotopy-type formula alone for the complete-edge case follows from Biswas and is not the novelty claim. The orientation-lattice description is for the selected weight-at-most-two Boolean subspace at radius one. It does not classify its behavior at other radii, under adding weight-three points, or for arbitrary ambient-metric Čech witnesses. The finite verifier does not prove infinite parameters; correctness of those cases relies on the relative cell proof. Novelty is assessed against inspected literature, not independently certified, and equivalent unindexed work may exist.

## References
1. A. Biswas, *Čech complexes for finite sets*, arXiv:2609.32786v1 (first public 2026-09-26), especially Lemma 4.1 and §4.4. https://arxiv.org/abs/2609.32786
2. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871v1 (first public 2022-12-12), especially Theorem 4.1. https://arxiv.org/abs/2212.05871
