# Geometric fixed-point homotopy of generalized Mycielskian independence complexes

## Finding
Let \(n\ge2\) and \(\ell\ge2\), and let \(X_{n,\ell}=\operatorname{Ind}(\mu_\ell(K_n))\), where the generalized Mycielskian and its label-permutation action are defined below. For every \(\sigma\in S_n\), write \(f=|\{a:\sigma(a)=a\}|\). There is an explicit simplicial model of the *geometric fixed-point space* \(|X_{n,\ell}|^{\langle\sigma\rangle}\) which simplicially collapses as follows:
\[
 |X_{n,\ell}|^{\langle\sigma\rangle}\ \simeq_s\
 \begin{cases}
 \operatorname{Ind}(\mu_\ell(K_f)),&f\ge1,\\
 \operatorname{Ind}(P_{\ell+1}),&f=0.
 \end{cases}
\]
Here \(\simeq_s\) denotes simple-homotopy equivalence, induced by the explicit vertex eliminations in the proof; \(K_1\) means the edgeless one-vertex graph. In particular, **the fixed-space homotopy type depends only on the number of fixed labels, not on the lengths or number of nontrivial cycles of \(\sigma\)**.

The resulting full integral homotopy classification is as follows. When \(f=0\), write \(\ell=3k+r\), \(r\in\{0,1,2\}\). The fixed space is contractible for \(r=0\) and is \(S^k\) for \(r\in\{1,2\}\). When \(f=1\), it is contractible. When \(f\ge2\), it is
\[
 |X_{n,\ell}|^{\langle\sigma\rangle}\simeq
 \begin{cases}
 \displaystyle\bigvee^{f(f-1)^k}S^{2k},&\ell=3k,\\
 \displaystyle\bigvee^{(f-1)^{k+1}}S^{2k+1},&\ell=3k+1\text{ or }3k+2.
 \end{cases}
\]
The derivation of the sphere multiplicities for \(f\ge2\) uses the previously established nonequivariant generalized-Mycielskian homotopy theorem. The *new statement* is the universal fixed-point reduction and its consequences for all label permutations; the cases \(\ell=0,1\), which obey the same reduction, are included only as consistency boundary cases, not as separate novelty claims.

## Assumptions and scope
For a finite simple graph \(H\), \(\operatorname{Ind}(H)\) is the simplicial complex of independent vertex sets. Here \(\mu_\ell(K_n)\) has vertices \((j,a)\) with \(j\in\{0,\ldots,\ell\}\), \(a\in\{1,\ldots,n\}\), plus an apex \(w\). There are edges \((j,a)(j+1,b)\) exactly when \(a\ne b\), edges \((\ell,a)(\ell,b)\) when \(a\ne b\), and apex edges \(w(0,a)\). All other pairs are nonedges. The permutation \(\sigma\) acts by \((j,a)\mapsto(j,\sigma(a))\) and fixes \(w\). The superscript \(\langle\sigma\rangle\) denotes actual fixed points in the geometric realization, **not** the subcomplex on fixed vertices and not the orbit-space quotient. Homotopy types and sphere wedges are integral statements, with a wedge of zero spheres understood to be a point.

## Proof
**1. An exact model for geometric fixed points.** For any finite simplicial complex \(K\) with a permutation of its vertices, partition the vertices into permutation orbits. A geometrically fixed point has barycentric coordinates constant within each orbit, and its support must be a face. Hence it corresponds uniquely to a point in the simplicial complex whose vertices are those permutation orbits that are individually faces of \(K\), with collections admitted precisely when their union is a face of \(K\). This correspondence sends each orbit-vertex to the barycenter of that orbit and is a piecewise-linear homeomorphism onto \(|K|^{\langle\sigma\rangle}\). For independence complexes, this orbit complex is \(\operatorname{Ind}(H)\) for the graph \(H\) whose vertices are internally independent graph-vertex orbits; two vertices of \(H\) are adjacent when at least one original graph edge connects their two orbit sets.

**2. Orbit graph for the present action.** Partition the labels into singleton orbits \(a\), for which \(\sigma(a)=a\), and nontrivial cycles \(C\) of length at least two. A singleton label produces an orbit-vertex \(a_j\) at every level \(0\le j\le\ell\). Each nontrivial cycle produces an orbit-vertex \(C_j\) at every level \(0\le j<\ell\), but *none at the top level*: the top level is a clique, so its multi-element cycle is not an independent orbit. The apex gives one vertex \(w\). There are no graph edges between vertices at the same level below the top. Between adjacent levels, \(a_j\) and \(b_{j+1}\) are adjacent for distinct singleton labels \(a\ne b\), every \(C_j\) is adjacent to every orbit-vertex at neighboring levels, and at the top the singleton orbit-vertices form a clique. Finally, \(w\) is adjacent to all level-zero orbit-vertices. The claim about adjacent nontrivial cycles remains true for the *same* cycle in two consecutive levels: a cycle of size at least two contains distinct labels, hence some edge crosses the two copies.

**3. A fold lemma.** If vertices \(u\ne v\) in a graph satisfy \(N(u)\subseteq N(v)\) for *open* neighborhoods, then \(u,v\) are nonadjacent, and the link of \(v\) in \(\operatorname{Ind}(H)\) is a cone with cone vertex \(u\). Pairing each face containing \(v\) but not \(u\) with that face after adjoining \(u\) is an acyclic matching and gives a sequence of elementary simplicial collapses to \(\operatorname{Ind}(H-v)\). Thus these graph neighborhood folds preserve simple homotopy. All neighborhood comparisons below remain true as orbit-vertices are deleted.

**4. At least one fixed label.** Fix any singleton label \(a\). For every nontrivial label cycle \(C\) and every level \(j<\ell\), the orbit-graph neighborhoods satisfy
\[
N(a_j)\subseteq N(C_j).
\]
Indeed, the fixed-label vertex \(a_j\) sees the apex when \(j=0\), the nontrivial orbit-vertices at adjacent levels, and all fixed-label vertices of adjacent levels whose labels differ from \(a\). The vertex \(C_j\) sees all these, and additionally sees the fixed label \(a\) at adjacent levels. It also sees each nontrivial cycle at adjacent levels even when it is the same cycle. The fold lemma therefore deletes every \(C_j\), for every cycle and level. The graph that remains is exactly \(\mu_\ell(K_f)\) on the \(f\) fixed labels and \(w\). This gives the first simple-homotopy equivalence without any restriction on the remaining cycle lengths.

**5. No fixed labels.** If \(f=0\), all admitted orbit-vertices are the nontrivial cycles \(C_j\) at levels \(j<\ell\), together with \(w\). Every two vertices at one level have identical open neighborhoods, and each pair of consecutive levels is joined completely bipartitely. Repeatedly applying the fold lemma leaves a single orbit-vertex \(u_j\) at each level and \(w\), with precisely the path edges \(wu_0,u_0u_1,\ldots,u_{\ell-2}u_{\ell-1}\). Thus the resulting complex is \(\operatorname{Ind}(P_{\ell+1})\). For \(m\ge4\), deletion of the second vertex of \(P_m\) leaves the first vertex isolated and therefore gives a contractible independence complex; the link of that second vertex is \(\operatorname{Ind}(P_{m-3})\). The vertex-deletion cofibration gives \(\operatorname{Ind}(P_m)\simeq\Sigma\operatorname{Ind}(P_{m-3})\). The initial cases are \(\operatorname{Ind}(P_1)\) contractible and \(\operatorname{Ind}(P_2)\simeq\operatorname{Ind}(P_3)\simeq S^0\). Induction proves exactly the asserted mod-three sphere/contractibility formula.

**6. Explicit homotopy classification for fixed labels.** If \(f\ge2\), the nonequivariant homotopy theorem for \(\mu_\ell(K_f)\) (Carnero Bravo, Corollary 7, also Goyal--Shukla--Singh) yields the displayed sphere-wedge multiplicities. For \(f=1\), the graph has only the edge \(w(0,1)\), and its other \(\ell\) vertices are isolated: its independence complex is a cone for \(\ell\ge1\). This proves the entire classification. The boundary cases \(\ell=0,1\) follow by the same orbit argument but are not needed for the new parameter range.

## Verification
The included pure-Python `verify.py` reconstructs the generalized Mycielskian graph and the admissible vertex-orbit graph directly. It performs all neighborhood-inclusion assertions and compares every final folded graph against the claimed smaller generalized Mycielskian or path across **117** permutation/level pairs. For **37** sufficiently small cases it also independently enumerates invariant oriented faces of the original complex and computes signed reduced Lefschetz sums, matching the established homology-character arithmetic. Finally it calculates complete mod-two boundary-matrix homology for **28** small path and reduced-generalized-Mycielskian complexes. Execute `python3 verify.py`; its recorded output is in `verify_stdout.txt`. These finite calculations check the implementation and selected instances; the infinite theorem follows from the general fold proof above, not from finite extrapolation.

## Relationship to prior work
Goyal--Shukla--Singh (2019) and Carnero Bravo (first public 2026-01-19) calculate the ordinary homotopy types of generalized Mycielskian independence complexes. A published mathematical result entitled *The symmetric-group homology modules of generalized Mycielskians of complete graphs* determines their rational \(S_n\)-characters from the number of fixed labels. Those results can give Lefschetz numbers, but do **not** directly identify the geometric fixed-point homotopy type or the explicit simple-homotopy collapses proved here. In particular, equal Lefschetz numbers do not imply equal fixed-point homotopy types. The previously treated ordinary one-step Mycielskian is a special boundary case; the new assertion concerns all generalized depths \(\ell\ge2\).

## Limitations
No claim is made that the original full complexes are equivariantly homotopy equivalent for permutations with equal fixed-label counts; the result classifies individual geometric fixed-point spaces. No integral \(S_n\)-module or equivariant stable homotopy type is determined. Simple-homotopy equivalence is proved through a finite orbit-barycentric simplicial model; there is no asserted canonical homeomorphism from the fixed space to the smaller complex. The 2026 and 2019 works supply previously known nonequivariant wedge multiplicities. An unindexed equivalent fixed-point reduction cannot be excluded by searches alone.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1, first public 2026-01-19; revised v2, Corollary 7 and Theorem 5. https://arxiv.org/html/2601.13432v2
2. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), Section 4 and Theorem 4.12. https://arxiv.org/html/1905.06926v1
3. *The symmetric-group homology modules of generalized Mycielskians of complete graphs*, published mathematical research record, identifier `a69c919d2b95`, full RESULT.md inspected (2026). Rational character result only; no geometric fixed-point homotopy classification is asserted.
