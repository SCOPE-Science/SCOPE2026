# Cubic-root threshold for triple coincidences among many successor orders

## Finding
Fix an integer \(n\ge2\), choose \(r=r(n)\ge0\) independent uniform permutations of \([n]\), and interpret each permutation as the directed immediate-successor relation \(S_i\) of its linear order. No order relation itself belongs to the logical signature. Let \(K_e\) denote the number of those relations containing a given ordered arc \(e=(u,v)\) with \(u\ne v\). Define
\[
Y_{n,r}:=\sum_{u\ne v}\binom{K_{(u,v)}}3,\qquad
Z_{n,r}:=\#\{(u,v):u\ne v,\ K_{(u,v)}\ge3\},
\]
where \(\binom a3=0\) for \(a<3\).

**Theorem (triple-overlap transition).** If \(r(n)/n^{1/3}\to c\in[0,\infty)\), then
\[
Y_{n,r}\ \xrightarrow{d}\ \operatorname{Poisson}(c^3/6),
\qquad
\Pr(Y_{n,r}=Z_{n,r})\to1.
\]
For \(0<c<\infty\), with probability tending to one, all triple-overlap witnesses use pairwise disjoint ordered pairs of vertices (even as unordered endpoint sets) and pairwise disjoint triples of successor-relation indices. If \(r(n)/n^{1/3}\to\infty\), then \(\Pr(Y_{n,r}>0)\to1\); if that ratio tends to zero, the probability tends to zero.

The two-variable sentence in the varying signature \(\{S_1,\ldots,S_r\}\)
\[
\psi_r:=\exists x\,\exists y\,\bigvee_{1\le i<j<k\le r}
\bigl(S_i(x,y)\wedge S_j(x,y)\wedge S_k(x,y)\bigr)
\]
(with an empty disjunction interpreted as false) satisfies
\[
\lim_{n\to\infty}\Pr(\psi_{r(n)})=
\begin{cases}
0,&r(n)/n^{1/3}\to0,\\
1-\exp(-c^3/6),&r(n)/n^{1/3}\to c\in(0,\infty),\\
1,&r(n)/n^{1/3}\to\infty.
\end{cases}
\]
In particular, the critical number of independent successor predicates has order \(n^{1/3}\). This is a varying-signature, varying-sentence probability transition; it is **not** a fixed-signature first-order convergence law.

**Finite exact moments.** Put \(a_s=\binom r3\binom3s\binom{r-3}{3-s}\) for \(s\in\{0,1,2,3\}\), using zero for invalid binomial arguments. Then for every \(n\ge2\) and \(r\ge0\),
\[
\mathbb E Y_{n,r}=\frac{n-1}{n^2}\binom r3,
\]
\[
\mathbb E\bigl[(Y_{n,r})_2\bigr]
=n(n-1)\sum_{s=0}^{2}\frac{a_s}{n^{6-s}}
+n(n-1)^2(n-2)\sum_{s=0}^{3}
\frac{a_s}{n^{6-s}(n-1)^s},
\]
where \((t)_2=t(t-1)\). The second formula supplies a finite-size check of the supercritical variance argument.

## Assumptions and scope
The universe is a fixed labelled set \([n]\) with \(n\ge2\); each of the \(r\) orders is sampled independently and uniformly from the \(n!\) permutations. All successor arrows are directed and nonreflexive. Two arrows are the same only when their ordered endpoints agree; reversed directions are distinct. The parameter \(r(n)\) is an arbitrary sequence of nonnegative integers. There are no additional predicates, no conditioning on the relations, and no claim for dependent or nonuniform orders. The theorem's logical assertion concerns the sequence of formulas \(\psi_{r(n)}\), not a single formula in one fixed language.

## Proof
**1. Arc contraction.** For any fixed collection of \(t\) distinct prescribed directed arcs on \([n]\), a linear order can contain all of them exactly when these arcs form vertex-disjoint directed paths, allowing consecutive arcs to share a vertex. Equivalently, every vertex has at most one prescribed predecessor and successor, and the arcs contain no directed cycle. In the compatible case, collapsing each path into one block leaves \(n-t\) objects, so exactly \((n-t)!\) permutations contain the arcs. Thus their probability is
\[
\frac{(n-t)!}{n!}=\frac1{(n)_t}
=n^{-t}\bigl(1+O_t(n^{-1})\bigr).
\]
For any fixed upper bound on \(t\), the probability is at most \(C_t n^{-t}\), even in incompatible cases (whose probability is zero). In particular, any specified arc lies in a random order with probability \(1/n\).

**2. Elementary events and mean.** Index events by a three-element set \(I\subseteq[r]\) and a directed arc \(e=(u,v)\). The event \(A_{I,e}\) says that all three orders indexed by \(I\) contain \(e\). It has probability \(n^{-3}\), and \(Y_{n,r}=\sum_{I,e}{\bf1}_{A_{I,e}}\). There are \(n(n-1)\binom r3\) elementary events, which proves the mean formula.

**3. Fixed factorial moments at criticality.** Suppose \(r/n^{1/3}\to c\in(0,\infty)\), and fix \(k\ge1\). Expand \(\mathbb E(Y_{n,r})_k\) over ordered \(k\)-tuples of distinct elementary events. Call such a tuple good when its directed arcs have pairwise disjoint endpoint sets and its order-index triples are pairwise disjoint. The good fraction tends to one because \(r,n\to\infty\). Each good tuple has exact joint probability \(n^{-3k}\), and their total contribution tends to \((c^3/6)^k\).

For distinct arcs whose endpoint sets or index triples overlap, but with no repeated arc, the number of choices is an \(O_k(n^{-1}+r^{-1})\) fraction of all candidate tuples. Arc contraction bounds each joint probability by \(C_k n^{-3k}\). Their aggregate contribution is \(o(1)\).

It remains to control repeated arcs. Partition the \(k\) events by their common directed arc. If a group contains one event, its three-index union has size \(q=3\); if it contains at least two *distinct* events, its union has size \(q\ge4\). For \(g\) groups with index-union sizes \(q_1,\ldots,q_g\), there are at most \(C_k n^{2g}r^{q_1+\cdots+q_g}\) choices. The union of their distinct arc/index incidence requirements has \(q_1+\cdots+q_g\) incidences and hence has probability at most \(C_k n^{-(q_1+\cdots+q_g)}\). Thus its contribution is bounded by a constant multiple of
\[
\prod_{j=1}^g n^2(r/n)^{q_j}.
\]
At \(r=O(n^{1/3})\), singleton groups contribute \(O(1)\), while a repeated-arc group contributes at most \(O(n^{-2/3})\). Only finitely many patterns occur for fixed \(k\), so all repeated-arc contributions vanish. Therefore
\[
\mathbb E(Y_{n,r})_k\longrightarrow(c^3/6)^k
\quad\text{for every fixed }k.
\]
The factorial-moment characterization of the Poisson distribution proves the claimed distributional limit. When \(c=0\), the expectation tends to zero and Markov's inequality gives the degenerate Poisson limit.

**4. Exact second moment and supercriticality.** For two distinct elementary events with the same arc, let their order-index triples overlap in \(s\in\{0,1,2\}\) indices. Their joint probability is \(n^{-(6-s)}\). For distinct arcs, the two arc requests can coexist in one linear order if and only if they form compatible paths. For each fixed directed arc, exactly \((n-1)(n-2)\) other directed arcs are compatible. When the index triples overlap in \(s\in\{0,1,2,3\}\) indices, the joint probability is \(n^{-(6-s)}(n-1)^{-s}\) in the compatible case, and zero otherwise. Counting index-triple pairs of overlap size \(s\) gives \(a_s\) and yields the displayed exact second factorial moment.

If \(r/n^{1/3}\to\infty\), then \(\mu_{n,r}:=\mathbb EY_{n,r}\to\infty\) and \(r\to\infty\). The exact moment formula and \(\sum_{s=0}^3a_s=\binom r3^2\) imply
\[
\frac{\operatorname{Var}(Y_{n,r})}{\mu_{n,r}^2}
=O\left(\frac1{\mu_{n,r}}+\frac1n+\frac1{r^2}
+\frac1{nr}\right)\longrightarrow0.
\]
Here the same-arc contribution divided by \(\mu_{n,r}^2\) is \(O(n^{-2}+(nr)^{-1}+r^{-2})\), while the different-compatible-arc contribution is \(\mu_{n,r}^2(1+O(n^{-1}))\). Chebyshev's inequality gives \(\Pr(Y_{n,r}=0)\to0\). Subcriticality follows from the first moment.

**5. Unique isolated witnesses at criticality.** Under \(r=O(n^{1/3})\), the expected number of ordered arcs present in four or more orders, counted with four-index multiplicity, is \(n(n-1)\binom r4 n^{-4}=O(n^{-2/3})\). Hence \(Y=Z\) with high probability. For \(c>0\), the expected number of pairs of distinct triple events using the same arc is \(O(r^6/n^4+r^5/n^3+r^4/n^2)=o(1)\). Among events with different arcs, the expected number of pairs sharing a vertex is \(O(r^6/n^3)=o(1)\), and the expected number sharing an order index is \(O(r^5/n^2)=o(1)\). These estimates use the uniform arc-contraction bound and count only the indicated overlaps; incompatible arc requests contribute zero. Markov's inequality proves the isolation statement. For \(c=0\), there are no witnesses with high probability.

**6. Logical equivalence.** The sentence \(\psi_r\) is true exactly when an arc belongs to at least three successor relations, namely when \(Z>0\), which is equivalent deterministically to \(Y>0\). The Poisson and zero/one regimes give the three displayed probabilities.

## Verification
Run `python3 check.py` from the directory containing the accompanying `check.py` (Python 3 standard library only). The script enumerates every directed arc set of size at most three on universes of size two through five and verifies the arc-contraction count for every prescribed set. It then enumerates all tuples of \(r\) orders for \((n,r)=(3,3),(3,4),(4,3),(4,4)\), evaluating \(Y\) and the exact first two factorial-moment identities with rational arithmetic. It also checks deterministically that \(Y>0\) if and only if \(Z>0\) on those finite instances. The final status line is `TRIPLE_SUCCESSOR_CHECK_OK`. This finite enumeration corroborates only the finite identities; the asymptotic statements rely on the proof above.

## Relationship to prior work
Michaliszyn and Witkowski (2026, arXiv:2610.09758) and Jeż, Michaliszyn and Witkowski (2026, arXiv:2610.19943) establish algorithmic results for two-variable logic with arbitrary input-dependent numbers of successor relations. Their stated objects permit exactly the overlapping directed adjacencies considered here, but their documented conclusions are satisfiability algorithms and bounds, not random-model threshold probabilities. The latter 2026 source's accessible full-text HTML was inspected, including its introduction, representation of successor bundles, and conclusion.

Bender and Canfield (1999) prove Poisson approximation for edges simultaneously common to a *fixed* number of randomly embedded sparse graphs, under stated sparsity hypotheses. Their Theorem 1 and proof were inspected. It is related to the fixed-triple input but does not itself deliver the Poisson transition for an **increasing** family of sampled directed paths with a triple chosen from that family, nor the stated uniform finite moments or disjointness property. Classical multiple-birthday laws apply to independent allocations into bins; the edges within each randomly embedded Hamiltonian path are not independent bin selections.

The known fixed-number-of-orders limit for signed pairwise overlaps is a different statistic and does not imply the changing-number-of-orders threefold event. The current proof computes new joint overlap interactions directly. This is a best-knowledge comparison rather than proof of absolute historical priority.

## Limitations
The model uses independent uniform linear orders and directed immediate successors, not arbitrary directed graphs, Mallows permutations, or relations obtained from correlated orders. The asymptotic Poisson law does not hold with fixed \(r\) as a nondegenerate limit (its mean then tends to zero). The isolation assertion applies at the critical scale, not generally in the supercritical regime. The logical signature and sentence grow with \(n\): no fixed-language full first-order convergence theorem is claimed. The highly relevant 2026 source arXiv:2610.09758 was accessible at abstract level only; a more general older theorem for dependent multiple coincidences could potentially subsume parts of the result. Independent mathematical audit has not been performed.

## References
1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758 (first public 2026-10-07), https://arxiv.org/abs/2610.09758.
2. A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943 (first public 2026-10-14), https://arxiv.org/abs/2610.19943; accessible full-text rendering https://www.paperpeel.com/paper/2610.19943.
3. E. A. Bender and E. R. Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, Electronic Journal of Combinatorics 6 (1999), R36, https://doi.org/10.37236/1468.
4. R. Arratia, S. Garibaldi and J. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process*, Random Structures & Algorithms 48 (2016), 480–502, https://doi.org/10.1002/rsa.20591.
