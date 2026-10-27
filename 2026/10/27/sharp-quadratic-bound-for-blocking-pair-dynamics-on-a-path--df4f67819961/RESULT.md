# Sharp quadratic bound for blocking-pair dynamics on a path

## Finding

**Theorem.** Fix an integer \(n\ge2\). Let the acceptability graph of \(n\) agents be the path \(v_1-v_2-\cdots-v_n\). Every agent ranks its one or two acceptable neighbors strictly and ranks being unmatched below every acceptable neighbor. From **any** initial matching, repeatedly allow **any** blocking pair to form a new pair, simultaneously dissolving its previous incident pairs. Regardless of the preferences, starting matching, and choice of blocking pair at every step, the number of moves is at most
\[
\boxed{\left\lfloor\frac{n^2}{4}\right\rfloor}.
\]
For every \(n\), this bound is attained by an explicit preference profile and a sequence from the empty matching. Consequently the maximum number of moves, optimized jointly over all such profiles, initial matchings, and legal improvement histories, equals this integer. A terminal state is necessarily stable.

## Assumptions and scope

An **acceptable pair** is an edge of the simple path. A matching consists of pairwise vertex-disjoint acceptable pairs. Each vertex has an outside option of remaining unmatched, ranked last. A **blocking pair** \(\{u,v\}\) is an acceptable, presently unmatched pair for which each endpoint strictly prefers the other to its present partner (or to being unmatched). A **move** adds that edge and deletes any matching edges meeting either endpoint. All preferences are fixed throughout the dynamics; ties, side payments, and simultaneous moves are excluded. Matchings need not be perfect and can start arbitrarily.

Write \(m=n-1\), and let \(e_i=\{v_i,v_{i+1}\}\) for \(1\le i\le m\). An original-graph matching corresponds to a subset \(S\subseteq\{1,\ldots,m\}\) having no consecutive indices.

## Proof

**1. An orientation and an integer potential.** Regard the edge indices \(1,\ldots,m\) as the vertices of a *second*, auxiliary path. For each interior agent \(v_i\), orient the auxiliary link between indices \(i-1\) and \(i\) from the less-preferred incident acceptable pair toward the more-preferred one. The auxiliary orientation is a DAG because its underlying graph is a path. For each index \(j\), let
\[
w_j=\bigl|\{a\in\{1,\ldots,m\}:\text{there is a directed path }a\rightsquigarrow j\}\bigr|,
\]
where paths of length zero count. In particular, every \(w_j\) is a positive integer. Uniqueness of paths in the auxiliary path implies the recurrence
\[
w_j=1+\sum_{a\to j}w_a,
\]
where the sum is over immediately incoming auxiliary links. Indeed, the ancestor sets of distinct incoming neighbors are disjoint, since there is a unique undirected route to \(j\).

For a current matching with auxiliary index set \(S\), define
\[
\Phi(S)=\sum_{j\in S}w_j.
\]
If blocking edge \(e_j\) forms, it replaces zero, one, or two matching edges. Every replaced edge is auxiliary-adjacent to \(j\) and is less preferred than \(e_j\) by its shared agent. Thus each replaced edge has an arrow into \(j\). The recurrence yields
\[
\Delta\Phi=w_j-\sum_{a\text{ replaced}}w_a\ge1.
\]
Consequently every move increases the integer potential by at least one.

**2. Universal maximum of the potential.** Fix an arbitrary matching index set \(S\) with \(k=|S|\), and let \(U=\{1,\ldots,m\}\setminus S\). Since \(S\) has no adjacent indices, \(k\le\lfloor n/2\rfloor\). The potential counts ordered reachable pairs \((a,s)\), with \(s\in S\) and a directed auxiliary path \(a\rightsquigarrow s\). Split these pairs into: \(k\) trivial pairs \((s,s)\), \(R\) pairs with \(a\in U\), and \(T\) pairs with distinct \(a,s\in S\). Thus \(\Phi(S)=k+R+T\).

For each distinct reachable pair \((s,t)\in S\times S\), let \(u\) be the immediate predecessor of \(t\) on the unique directed path from \(s\) to \(t\). The index \(u\notin S\), because \(u\) is adjacent to the selected index \(t\) and \(S\) is independent. The arrow \(u\to t\) points away from \(s\), hence \(u\not\rightsquigarrow s\). Associate to \((s,t)\) the **nonreachable** ordered pair \((u,s)\in U\times S\). This map is injective: for fixed \(s\), distinct targets \(t\) on the same side of \(s\) give distinct predecessors \(u\), while targets on opposite sides give predecessors on opposite sides of \(s\). The second coordinate retains \(s\). Therefore the number of nonreachable pairs in \(U\times S\) is at least \(T\), so
\[
T\le |U|k-R,
\qquad
\Phi(S)=k+R+T\le k+k(m-k)=k(n-k).
\]
The arithmetic inequality \(k(n-k)\le\lfloor n^2/4\rfloor\) gives \(0\le\Phi(S)\le\lfloor n^2/4\rfloor\) for every matching and every orientation. Since each move increases \(\Phi\) by at least one, no history can contain more than \(\lfloor n^2/4\rfloor\) moves, whatever its initial state.

**3. Sharp histories.** Let every interior agent strictly prefer its *left* neighbor over its right neighbor; endpoint agents have their sole acceptable neighbor. Start with the empty matching. For each integer \(q\) from \(0\) through \(\lfloor n/2\rfloor-1\), execute, in order, the moves on
\[
e_{n-1},e_{n-2},\ldots,e_{2q+1}.
\]
Inductively, immediately before this phase the matching contains exactly \(e_1,e_3,\ldots,e_{2q-1}\). Its first move joins the two rightmost free vertices. Each subsequent move shifts the currently rightmost newly formed pair one step left; the common vertex strictly prefers its new left neighbor, and the other endpoint is unmatched. At the end of the phase the newly parked pair is \(e_{2q+1}\), disjoint from all previously parked pairs. Hence every move is blocking, and phase \(q\) makes \(n-2q-1\) moves. Summing these positive phase lengths yields
\[
\sum_{q=0}^{\lfloor n/2\rfloor-1}(n-2q-1)
=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
This proves equality and completes the proof. \(\square\)

## Verification

The standalone Python program `verify.py` (standard library only) enumerates all strict preference profiles and all matchings for path sizes \(2\le n\le11\), constructs every directed legal-move arc, verifies strict increase of the reachability potential and the universal potential ceiling, and computes the longest possible history by dynamic programming. For each tested size the computed maximum equals the theorem's exact value. It also constructs the sharp histories and verifies each move for every \(2\le n\le80\). All arithmetic is exact. Run `python verify.py`. These finite tests corroborate but do not replace the general proof above.

## Relationship to prior work

Fanelli and Moscardelli, *Approximately Stable Matching* (ECAI 2025 proceedings, publisher's verified online release August 25, 2026), introduce general blocking-pair dynamics on acceptability graphs. Their Theorem 4 proves convergence for every forest and bounds each agent's participation by \(n^2/4\); their stated resulting bound for the *total number of moves* is \(n^3/8\). Their Theorem 5 exhibits a branching-tree example in which one central agent participates quadratically many times. Neither statement supplies the exact path-wide total-move maximum. The present result improves the forest-derived total bound to the sharp \(\lfloor n^2/4\rfloor\) for paths, simultaneously for every possible improvement sequence.

Garg and Hu, *Improved Paths to Stability for the Stable Marriage Problem* (arXiv:2007.07121, 2020/2023), obtain an \(O(n^2)\) **chosen path to stability** in a more general bipartite market; that existential guarantee does not bound *all* legal improvement sequences. The exact path total-count statement is not implied by the published description of that result. Static stable-matching existence on paths is also weaker than a uniform sharp upper bound on arbitrary histories.

## Limitations

The result assumes one path as the acceptability graph, strict and time-invariant preferences, unmatched last, and sequential pair formation that discards previous partners. It does not claim a matching-size guarantee, a universal quadratic bound for arbitrary trees, a bound for simultaneous updates, or novelty for previously known forest convergence. Publication priority remains subject to discovery of unindexed or differently phrased equivalent path-dynamics results. Computational checks are finite and establish no infinite theorem independently.

## References

1. A. Fanelli and L. Moscardelli, *Approximately Stable Matching*, ECAI 2025 proceedings, DOI: 10.3233/FAIA251234; full text at https://journals.sagepub.com/doi/full/10.3233/FAIA251234 (publisher first published online August 25, 2026), particularly Theorems 4–5 and Section 5.
2. V. K. Garg and C. Hu, *Improved Paths to Stability for the Stable Marriage Problem*, arXiv:2007.07121 (first submitted July 14, 2020; version 2 May 16, 2023), https://arxiv.org/abs/2007.07121.
