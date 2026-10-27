# An effective first-order convergence law for two random successor orders

## Finding

Let \(A_n\) and \(B_n\) be independently and uniformly sampled linear orders on the same labelled \(n\)-element domain. Retain **only** their directed immediate-successor predicates \(S_A,S_B\), not the order relations. In the resulting finite relational structure \(M_n\), every first-order sentence \(\varphi\) has a limiting truth probability
\[
L_\varphi=\lim_{n\to\infty}\Pr(M_n\models\varphi).
\]
For every \(\varphi\), this probability is effectively computable, and for some effectively computable positive integer \(D_\varphi\) it belongs to \(\mathbb Q[e^{-1/D_\varphi}]\). The collection of limiting probabilities, over all sentences in this fixed two-predicate language, is dense in \([0,1]\).

More precisely, define an **admissible coloured oriented cycle** to be a connected directed multigraph whose underlying undirected multigraph is a cycle of length \(\ell\ge2\) (parallel edges are permitted for \(\ell=2\)); each arc has exactly one of the two colours \(A,B\); no monochrome subgraph has a directed cycle or an in-degree or out-degree exceeding one. Let \(\mathcal C\) contain one isomorphism representative of every such cycle. The number \(Z_{H,n}\) of occurrences of any finite family \(H\in\mathcal C\), counted as coloured oriented subgraphs (not necessarily induced), converges jointly to **independent** Poisson random variables of respective means
\[
\lambda_H=\frac{1}{|\operatorname{Aut}(H)|}.
\]
Here automorphisms preserve vertex incidences, edge colours and orientations. These cycle variables, together with four asymptotically separated deterministic successor-path endpoints, determine every limiting first-order probability by bounded-degree locality.

For \(m\ge1\), let \(H_m\) be a coherently directed cycle of length \(2m\) with colours alternating \(A,B\). Then \(|\operatorname{Aut}(H_m)|=m\), hence for every finite nonempty \(F\subseteq\mathbb N_{\ge1}\), the sentence asserting the existence of at least one \(H_m\) with \(m\in F\) has limiting probability
\[
1-\exp\!\left(-\sum_{m\in F}\frac1m\right).
\]
In particular the limiting probability of a two-vertex directed cycle \(S_A(x,y)\wedge S_B(y,x)\) is \(1-e^{-1}\); the model has a convergence law but not a zero-one law.

## Assumptions and scope

The domain is \([n]\), \(n\ge1\). Each linear order is selected uniformly among all \(n!\) orders, independently of the other. The only non-logical symbols are the two binary successor relations \(S_A,S_B\); equality is permitted. No underlying linear order, parameter, colour predicate, arbitrary additional relation or counting/modular quantifier is permitted. Every first-order formula is fixed before \(n\to\infty\); quantifier rank and number of variables may be arbitrarily large but finite. In the cycle definition, the directed multigraph retains the distinction between an \(A\)-arc and a \(B\)-arc even if they share endpoints.

## Proof

**1. Exact path-forest probability.** If a prescribed set of \(e\) directed edges forms a vertex-disjoint union of directed paths, the probability that it is contained in the successor relation of a uniform order is exactly
\[
\frac{(n-e)!}{n!}=\frac1{(n)_e},
\]
where \((n)_e=n(n-1)\cdots(n-e+1)\). Contract each prescribed path into a block: exactly \((n-e)!\) orders contain all its edges. If a prescribed one-colour edge set has a directed cycle or conflicting incoming/outgoing edges, its probability is zero. Consequently any finite admissible two-colour pattern with \(e_A,e_B\) prescribed edges has exact probability \(1/((n)_{e_A}(n)_{e_B})\), by independence of the two orders.

**2. Independent cycle process.** Fix finitely many isomorphism classes \(H\in\mathcal C\) and nonnegative integers \(t_H\). Consider the mixed factorial moment of the counts \(Z_{H,n}\). For selections of pairwise vertex-disjoint cycle embeddings, write \(v=\sum_H t_H|V(H)|\) and \(a=\sum_Ht_H e_A(H)\), \(b=\sum_Ht_H e_B(H)\). Each cycle has as many edges as vertices, so \(a+b=v\). The disjoint-embedding contribution is exactly
\[
\frac{(n)_v}{(n)_a(n)_b}\prod_H |\operatorname{Aut}(H)|^{-t_H}
\ \longrightarrow\ \prod_H\lambda_H^{t_H}.
\]
For overlapping **distinct** cycle occurrences, the union has strictly more coloured arcs than vertices. Indeed two distinct cycles cannot share their entire edge sets, and adjoining one cycle to another along a nonempty overlap creates positive excess; iteration proves the assertion for any non-disjoint family. With a fixed number of pattern vertices and edges, there are \(O(n^v)\) labelled unions on \(v\) vertices and each feasible union has probability \(O(n^{-e})\), \(e\ge v+1\). Thus the total overlapping contribution is \(O(n^{-1})\). Every mixed factorial moment therefore converges to that of independent \(\operatorname{Poisson}(\lambda_H)\) variables. The multivariate factorial-moment criterion proves joint convergence.

**3. The local structure.** Form the Gaifman multigraph by forgetting the directions of the coloured arcs, but retain the full direction/colour labels for logical neighbourhood types. Its Gaifman degree is at most four. For any fixed radius \(R\), the start and end of each order give four endpoints; with probability tending to one they are distinct, at mutual distance greater than \(2R\), and have acyclic \(2R\)-neighbourhoods. The bounded exploration around these four vertices exposes only \(O_R(1)\) successor slots, each with collision probability \(O_R(1/n)\). Away from endpoints, every vertex locally has one predecessor and one successor of each colour.

Any non-tree radius-\(R\) neighbourhood contains a cycle of length at most \(2R+1\) in the underlying coloured multigraph. The expected number of such cycles is bounded independently of \(n\), by step 2 and the exact first-moment formula. Every bounded-size pattern containing two distinct cycles has more coloured edges than vertices, so the probability that any such two cycles occur at distance at most \(2R\) tends to zero. The same holds for a short cycle within distance \(2R\) of any endpoint. Therefore, with probability tending to one, every exceptional radius-\(R\) neighbourhood is generated by exactly one of: a single isolated endpoint, or a single admissible cycle of length at most \(2R+1\) completed at unused in/out colour slots by finite pieces of the regular four-port directed tree. All remaining vertices have the same generic radius-\(R\) tree neighbourhood, and their count tends to infinity in probability.

For each fixed \(R\), the vector of **truncated counts** of all radius-\(R\) neighbourhood types is therefore, up to an event of probability tending to zero, a deterministic function of the four separated endpoints and the finitely many \(Z_{H,n}\) with \(|V(H)|\le2R+1\). Every possible exceptional count is a finite integer linear combination of these cycle counts and the fixed endpoint contributions, with negative terms unnecessary; the generic tree type has a count exceeding every fixed threshold with high probability. This establishes convergence in distribution of the complete vector of truncated local-type counts.

**4. First-order convergence and effectivity.** By the effective bounded-degree Hanf theorem, from the quantifier rank of \(\varphi\) one can compute a radius \(R\) and a truncation threshold \(T\) such that truth of \(\varphi\) is determined by the numbers of radius-\(R\) neighbourhood types, each truncated at \(T\). Step 3 yields convergence. Moreover one can enumerate the finite admissible cycle types up to length \(2R+1\), compute their coloured automorphism groups, the deterministic local-type contributions and the finite truth table for the possible truncated count vectors. Every vector in the support is attained for sufficiently large finite structures, so brute-force finite representatives also give a terminating method for that truth table. A Poisson variable of rational mean \(\lambda\) has truncated probabilities \(e^{-\lambda}\lambda^j/j!\) for \(j<T\) and \(1-e^{-\lambda}\sum_{j<T}\lambda^j/j!\) for the saturated state. Taking a common denominator \(D_\varphi\) of the finitely many \(\lambda_H\), each cell probability and hence \(L_\varphi\) belongs to \(\mathbb Q[e^{-1/D_\varphi}]\).

**5. Density.** The alternating cycles \(H_m\) have exactly \(m\) colour-and-orientation-preserving cyclic rotations and no reflections, so \(\lambda_{H_m}=1/m\). Distinct such cycles have asymptotically independent counts. Their existence sentences yield \(1-\exp(-\sum_{m\in F}1/m)\) for every finite \(F\). Given \(x\in(0,1)\), put \(t=-\log(1-x)\). Consecutive sums of reciprocals beginning beyond an arbitrarily large index approximate \(t\) from above with arbitrarily small overshoot, because \(\sum_{m\ge1}1/m=\infty\) and individual terms tend to zero. Continuity of \(1-e^{-t}\) proves density; \(0\) and \(1\) are limiting endpoints.

## Verification

The standalone standard-library checker `check_successor_local_law.py` exhaustively enumerates all ordered pairs of independent labelled linear orders for \(2\le n\le6\), altogether \(533416\) pairs. It verifies twenty exact finite-ensemble mean identities for: opposite two-cycles, same-direction parallel pairs, coherent \(A,B,B\) three-cycles, and alternating \(A,B,A,B\) four-cycles. The means agree respectively with \((n-1)/n\), \((n-1)/n\), \((n)_3/((n)_1(n)_2)\), and \((n)_4/(2(n)_2^2)\), using zero when a pattern is too large. Execution ends with `SUCCESSOR_LOCAL_EXACT_OK 533416 20`. These are exact finite corroborations, not substitutes for the factorial-moment and locality proofs.

## Relationship to prior work

The 2026 paper of Jeż, Michaliszyn and Witkowski establishes finite satisfiability and size bounds for two-variable logic with arbitrarily many linear-order successors; it poses a different decision problem with formula-dependent model existence, not a uniform random-measure convergence theorem. The distinction between full linear-order language and the successor reduct is substantive: Foy and Woods established failure of a first-order convergence law for uniformly random pairs of **full** orders, discussed and extended in Müller, Skerman and Verstraaten (2023). The theorem here proves convergence once the nonlocal order predicates are discarded, despite retaining both successors. The 2020 expressibility study of Albert, Bouvel and Féray analyzes permutations represented by two full orders or by one bijection, not this two-successor reduct. McKay, Wormald and Wysocka establish Poisson short-cycle limits for uncoloured uniform random regular graphs; Haber and Krivelevich study first-order logic over undirected random regular graphs. Their models are not pairs of independent directed spanning paths, and their statements do not supply the four endpoint contributions or coloured cycle intensities used here. Classical path contraction, Poisson factorial moments and Hanf locality are credited as background tools. Previously known rank-two logical limit types for independent random successors cover only depth two and do not imply the unrestricted first-order claim.

## Limitations

The result does not establish a convergence law for the two **full** order relations (in fact the analogous law fails), for arbitrary extra predicates, for varying quantifier rank, or for monadic second-order logic. No uniform convergence rate in formula complexity is asserted. The finite checker does not prove the asymptotic theorem. Historical-priority uncertainty remains: a sufficiently general existing theorem for coloured random permutation configurations might imply the same first-order specialization, although no directly covering source was identified in the comparisons recorded here. Independent verification has not been carried out.

## References

1. A. Jeż, J. Michaliszyn, P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943, first released 2026-10-14. https://arxiv.org/abs/2610.19943
2. T. Müller, F. Skerman, T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148, 2023. https://arxiv.org/abs/2302.10148
3. M. Albert, M. Bouvel, V. Féray, *Two first-order logics of permutations*, J. Combin. Theory Ser. A **171** (2020), 105158. https://doi.org/10.1016/j.jcta.2019.105158
4. B. D. McKay, N. C. Wormald, B. Wysocka, *Short Cycles in Random Regular Graphs*, Electron. J. Combin. **11** (2004), R66. https://doi.org/10.37236/1819
5. S. Haber, M. Krivelevich, *The logic of random regular graphs*, J. Combin. **1** (2010), 389–440. https://doi.org/10.4310/JOC.2010.v1.n4.a3
6. Foy and Woods, *Probabilities of sentences about two linear orderings* (1990), as cited in reference 2.
7. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004; bounded-degree Hanf locality.
