# Exact singleton rainbow domination and optimal-function census on balanced multipartite graphs

## Finding
Let \(r\ge2\), \(m\ge1\), and \(k\ge3\) be integers, and let \(G=K_{m,\ldots,m}\) be the complete \(r\)-partite graph with \(r\) labelled vertex parts, each of size \(m\). A *singleton rainbow \(k\)-dominating function* assigns each vertex either \(0\) or one of the \(k\) named colours; every zero-labelled vertex must see all \(k\) colours among its neighbours. Its weight is the number of nonzero vertices. Denote the minimum weight by \(\widetilde\gamma_k(G)\).

**Theorem.** If \(k>(r-1)m\), then \(\widetilde\gamma_k(G)=rm\), and precisely \(k^{rm}\) minimum functions exist. If \(k\le(r-1)m\), write \(k=qm+s\) with \(0\le s<m\). Then
\[
\boxed{\widetilde\gamma_k(G)=qm+\min\{2s,m\}.}
\]
All minimum functions, with their exact number, are as follows. Here the parts and vertices are distinct and the colours are named.

* **Divisible case** \(s=0\): choose exactly \(q\) full parts, assign all \(k=qm\) colours bijectively to their vertices, and label all other vertices zero. The count is \(\binom rq k!\).
* **Double-support case** \(0<s<m\), \(2s<m\): choose exactly \(q\) full parts, assign \(qm\) distinct colours bijectively to their vertices, and for each of the remaining \(s\) colours choose exactly two distinct non-full parts and one vertex in each. All other vertices are zero. The count is \(A_{r,m,k}\) defined below.
* **Full-part case** \(0<s<m\), \(2s>m\): choose exactly \(q+1\) full parts, assign their vertices colours in such a way that every one of the \(k\) colours occurs, and label all other vertices zero. The count is \(B_{r,m,k}\) defined below.
* **Tie** \(0<s<m\), \(2s=m\): the two preceding constructions are disjoint and together give every minimum function. The count is \(A_{r,m,k}+B_{r,m,k}\).

For the exact counts let \(h=r-q\) and, for every \(s\)-tuple \((P_1,\ldots,P_s)\) of unordered two-element subsets of \([h]\), let \(d_i=|\{j:i\in P_j\}|\). Write \((m)_d=m(m-1)\cdots(m-d+1)\) for the falling factorial, with \((m)_0=1\). Define
\[
F_{h,m,s}=\sum_{(P_1,\ldots,P_s)\in\bigl(\binom{[h]}{2}\bigr)^s}\prod_{i=1}^{h}(m)_{d_i},
\]
\[
\boxed{A_{r,m,k}=\binom rq\frac{k!}{s!}F_{r-q,m,s},\qquad
 B_{r,m,k}=\binom r{q+1}\sum_{j=0}^{k}(-1)^j\binom kj(k-j)^{(q+1)m}.}
\]
These formulas give *all* optimal labelled functions, not merely a minimum weight.

## Assumptions and scope
The graph is finite, undirected and simple. Its \(r\) independent parts each have \(m\) vertices; edges join exactly vertices in different parts. The palette is \([k]\), and assigning more than one colour to a vertex is forbidden. This is the singleton model, not ordinary set-valued rainbow domination and not rainbow *total* domination. Colours are named and vertex assignments are counted without automorphism quotienting.

The assumption \(k\ge3\) isolates the new all-palette regime. The same mathematical formula is formally valid for \(k=1,2\); those low-palette cases are included in finite verification, but no novelty is claimed for them.

## Proof
Fix a function \(f\). Call a part **full** if every one of its \(m\) vertices is coloured; all other parts are **partial** and contain a zero vertex. First suppose that at least one zero vertex exists and that \(t\) parts are full. Let \(C\) denote the set of colours occurring in full parts and put \(c=|C|\le tm\). Every colour occurs somewhere, since a zero vertex must see all \(k\) colours.

**Support lemma.** Every colour outside \(C\) occurs in at least two *distinct* partial parts. Indeed, if such a colour occurred in just one partial part, a zero vertex in that same part could not see that colour outside the part. Consequently, at least \(2(k-c)\) coloured vertices lie in partial parts. The full parts contribute exactly \(tm\), so
\[
 w(f)\ge tm+2(k-c)\ge tm+2\max\{0,k-tm\}.
\tag{1}
\]
This is a lower bound without any assumption on the colouring within full parts.

If \(k>(r-1)m\), the graph's degree is less than \(k\); no vertex can be zero. Every vertex must be coloured, and each has \(k\) possible named colours, proving both assertions for this case.

Now suppose \(k\le(r-1)m\). If \(s=0\), at least \(k\) coloured vertices are needed because each colour must occur when a zero vertex exists, while the construction filling \(q\) parts bijectively uses exactly \(k\). A function of weight \(k\) cannot have \(t<q\) full parts, because (1) then gives \(w(f)\ge2k-tm>k\); it cannot have \(t>q\), because its full parts would already contribute more than \(k\). Thus \(t=q\), the full vertices carry the \(k\) colours bijectively, and all other vertices are zero. There are \(\binom rq k!\) such functions. They are feasible because every zero vertex lies outside every full part and sees all colours.

Suppose henceforth \(0<s<m\). Since \(k\le(r-1)m\), we have \(q\le r-2\). If \(t\le q\), inequality (1) gives \(w(f)\ge2k-tm\ge qm+2s\); if \(t\ge q+1\), the full parts give \(w(f)\ge(q+1)m\). A function with no zeros has weight \(rm\), which is larger than either candidate. Thus
\[
 w(f)\ge qm+\min\{2s,m\}. \tag{2}
\]
Both bounds are attainable. For the first, fill \(q\) parts bijectively with \(qm\) colours. Place one occurrence of each of the remaining \(s\) colours into each of two other parts, in different vertices. Because \(s<m\), these latter parts retain zeros. Every zero vertex sees every colour: the \(qm\) colours occur in full parts outside it, and each remaining colour has an occurrence in another partial part. This uses \(qm+2s\) coloured vertices. For the second, fill \(q+1\) parts so that all \(k\) colours occur, possible since \((q+1)m\ge k\); leave the other parts blank. This uses \((q+1)m\) coloured vertices and is feasible. Equation (2) is therefore sharp.

To classify equality, assume \(2s<m\). Equality in (2) forces \(t=q\) (any larger \(t\) costs at least \((q+1)m\), any smaller costs strictly more than \(qm+2s\)). Equality in (1) forces all \(qm\) full-part vertices to carry distinct colours, and each of the remaining \(s\) colours to occur *exactly twice* outside full parts. The support lemma forces those occurrences into distinct partial parts, leaving no other coloured vertices. Conversely every assignment of the stated kind is feasible. If \(2s>m\), equality forces \(t=q+1\) and no other coloured vertices, with every colour present in those full parts; conversely all such assignments are feasible. At \(2s=m\), equality allows precisely these two disjoint cases. This proves the complete classification.

For the double-support count, choose \(q\) full parts in \(\binom rq\) ways and bijectively assign \(qm\) of the \(k\) colours to their vertices in \(k!/s!\) ways. The remaining \(s\) named colours each choose an unordered pair of distinct non-full parts. If part \(i\) is chosen by \(d_i\) colours, the labelled colours can be placed at distinct vertices in \((m)_{d_i}\) ways. Summing products over all ordered \(s\)-tuples of part-pairs gives \(F_{h,m,s}\). Since \(d_i\le s<m\), no chosen partial part becomes full. This proves \(A_{r,m,k}\).

For the full-part count, choose the \(q+1\) parts and assign their \((q+1)m\) distinct vertices surjectively onto the \(k\) named colours. Inclusion-exclusion over missing colours gives \(\sum_{j=0}^{k}(-1)^j\binom kj(k-j)^{(q+1)m}\) assignments. This proves \(B_{r,m,k}\) and finishes the theorem.

## Verification
The included standalone `verify.py` enumerates all functions \(V(G)\to\{0,1,\ldots,k\}\) in 29 small parameter cases and independently tests the literal open-neighbourhood requirement on every zero vertex. It compares both the minimum weight and the complete *number of minimum functions* with a separately implemented finite formula. The exact run prints `VERIFY_OK cases=29 exhaustive_labelings=2921552`. A nontrivial example is \(r=3,m=3,k=4\), for which the minimum is \(5\) and there are exactly \(648\) named minimum functions. The checker also evaluates four larger symbolic formula examples, but does not enumerate their entire assignment spaces. These are finite checks; the proof above establishes the unrestricted result.

Run with a standard Python 3 interpreter: `python verify.py`.

## Relationship to prior work
Lange (arXiv:2610.06906, first submitted 2026-10-01) studies the same **singleton** rainbow \(k\)-domination model on regular graphs, proving structural bounds, computational complexity, and exact results for cycles, Möbius ladders, prisms and certain generalized Petersen graphs. The inspected definitions, bounds, exact-family statements, conclusion, and relevant appendix passages do not state a balanced complete-multipartite minimum-function classification or all-optima count; a whole-text search found no mention of the multipartite family. The bounds are not by themselves the stated residue-dependent exact formula.

Kuzman (arXiv:1907.08430) investigates ordinary, **set-valued** rainbow domination of regular graphs. Even where that work discusses complete bipartite graphs, its functions can place several colours on one vertex, so its extremal constructions do not imply this singleton theorem. The earlier published complete-multipartite 2-rainbow enumerator (published-finding corpus record ending `7f7bcd9e9b58`) permits the label \(\{1,2\}\), treats only two colours, and supplies the low-palette scalar minimum. Thus the two-colour special case is not presented as new. Prior work on ordinary domination of complete multipartite graphs similarly covers the one-colour case rather than this result.

For every \(k\ge3\), the theorem supplies the exact minimum, all optimizing functions and their labelled count, including the modular choice between duplicating residual colours and fully colouring another part.

## Limitations
The graph must be balanced complete multipartite. Arbitrary unequal part sizes introduce a nontrivial optimization over the capacities of whole parts, and are not classified here. The formulas count only *minimum* singleton rainbow-dominating functions, not all functions of every weight. The counting expression \(F_{h,m,s}\) may require exponentially many summands if evaluated directly. Although specific related works and a published-record search were examined, equivalent results could occur in terminology not identified by these searches.

## References
1. Piotr Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1, first public 2026-10-01. https://arxiv.org/abs/2610.06906
2. Boštjan Kuzman, *On \(k\)-rainbow domination in regular graphs*, arXiv:1907.08430, first public 2019-07-19. https://arxiv.org/abs/1907.08430
3. J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics 14 (2026), article 2917. https://doi.org/10.3390/math14162917
4. S. Hussain, A. Khan, and Y. Zhang, *On Resolvability- and Domination-Related Parameters of Complete Multipartite Graphs*, Mathematics 10 (2022), article 1815. https://doi.org/10.3390/math10111815
5. *All 2-rainbow dominating functions of complete multipartite graphs*, published published-finding corpus research record `7f7bcd9e9b58`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-2-rainbow-dominating-functions-of-complete-multipartite-grap--7f7bcd9e9b58
