# Locating-dominating sets of crown graphs: exact polynomial and a Poisson reliability threshold

## Finding
For every integer \(n\ge4\), consider the crown graph \(\operatorname{Cr}_n=K_{n,n}-M\), obtained by deleting a fixed perfect matching from the complete bipartite graph. Its locating-dominating polynomial, counting every locating-dominating vertex set by cardinality, is
\[
 L_n(z)=(z^2+2z)^n+n(z^2+2z)^{n-1}-2n^2z^{n-1}-2nz^n.
\]
At the two smaller boundaries, \(L_2(z)=4z^2+4z^3+z^4\) and \(L_3(z)=14z^3+15z^4+6z^5+z^6\).

For \(n\ge5\), the minimum locating-dominating cardinality is \(n-1\); the exact number of minimum sets is
\[
 n\bigl(2^{n-1}-2n\bigr).
\]
They are precisely the sets choosing one vertex from each of \(n-1\) deleted-matching pairs, omitting the remaining pair entirely, and choosing at least two vertices on each bipartition side. The minimum sizes are \(2,3,4\) for \(n=2,3,4\), with respectively \(4,14,56\) minimum configurations.

If vertices are independently selected with probability \(p\), then for \(n\ge4\), putting \(q=1-p\), the probability of locating domination is
\[
 (1-q^2)^n+nq^2(1-q^2)^{n-1}-2n^2p^{n-1}q^{n+1}-2np^nq^n.
\]
For fixed \(c\ge0\), under \(q=c/\sqrt n\) this probability tends to \((1+c^2)e^{-c^2}\). Thus the sensor-omission threshold occurs at order \(n^{-1/2}\), with a nontrivial Poisson limiting profile.

## Assumptions and scope
All graphs are finite, undirected and simple; \(n\ge2\). Label the two sides \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), with \(a_ib_j\) adjacent exactly when \(i\ne j\). For a selected set \(S\), write \(U=\{i:a_i\in S\}\), \(V=\{i:b_i\in S\}\), and \(x=n-|U\cup V|\). A locating-dominating set means that every vertex outside \(S\) has a **nonempty** open-neighborhood intersection with \(S\), and those intersections are pairwise **distinct**. Selected vertices need not be distinguished or dominated.

## Proof
For \(i\notin U\), the identifying neighborhood of \(a_i\) equals \(\{b_j:j\in V\setminus\{i\}\}\). For \(j\notin V\), that of \(b_j\) equals \(\{a_i:i\in U\setminus\{j\}\}\). Distinct nonempty signatures from opposite sides cannot coincide, since they are supported on disjoint sides. Within either side, two distinct omitted vertices have equal signatures if and only if neither of their indices occurs in the selected subset on the opposite side. Consequently signature distinctness on both sides is exactly \(x\le1\). Nonemptiness is automatic if both \(|U|\ge2\) and \(|V|\ge2\).

When \(U=\varnothing\), locating domination forces \(V=[n]\), and conversely this is sufficient for \(n\ge2\); the mirror case is analogous. When \(U=\{i\}\), nonemptiness forces \(i\in V\), while signature distinctness forces \(x\le1\). Hence \(V=[n]\) or \(V=[n]\setminus\{j\}\) for some \(j\ne i\); both are sufficient. The case \(|V|=1\) is symmetric. This exhausts the admissible profiles.

The sets with \(x\le1\), before imposing nonemptiness, are counted by
\[
 B_n(z)=(2z+z^2)^n+n(2z+z^2)^{n-1}.
\]
Indeed a deleted-matching pair contributes \(2z+z^2\) when at least one of its endpoints is selected, and an entirely omitted pair contributes \(1\); at most one pair may be omitted.

Among these profiles, the invalid cases with \(|U|\le1\) contribute \(n^2z^{n-1}+nz^n\). To see this, the \(n\) profiles with \(U=\varnothing\), \(|V|=n-1\) fail, as do \(n(n-1)\) profiles with \(U=\{i\}\), \(i\notin V\), \(|V|=n-2\), all of size \(n-1\). The remaining \(n\) invalid profiles have \(U=\{i\}\), \(V=[n]\setminus\{i\}\) and size \(n\). The valid low-support profiles are precisely those classified in the preceding paragraph. Symmetrically, invalid profiles with \(|V|\le1\) contribute the same polynomial. When \(n\ge4\), these two invalid families are disjoint because \(x\le1\) requires \(|U\cup V|\ge n-1\). Subtracting them from \(B_n(z)\) yields the claimed formula.

When \(n=3\), the two invalid families intersect in exactly six profiles with \(U\) and \(V\) distinct singleton index sets; their generating contribution \(6z^2\) must be restored. This gives the asserted \(L_3(z)\). When \(n=2\), the crown graph is two disjoint edges; every locating-dominating set chooses at least one endpoint of each edge, yielding \(L_2(z)=(2z+z^2)^2\).

For \(n\ge5\), the smallest exponent in \(B_n(z)\) is \(n-1\), with coefficient \(n2^{n-1}\). Subtraction leaves \(n(2^{n-1}-2n)>0\), proving the minimum and exact count. The profile interpretation shows that a minimum set uses one vertex in each of \(n-1\) matched pairs, with the selected vertices occurring at least twice on each side; of the \(2^{n-1}\) binary side choices, precisely \(2n\) have one side occupied at most once.

For the probabilistic claim, the number of completely omitted matching pairs under independent vertex-selection probability \(p\) is binomial with parameters \(n\) and \(q^2\). Its probabilities of zero and one omissions are the first two summands in the displayed reliability formula. The only extra failures are exactly the two invalid profile families, whose probability weights are \(2n^2p^{n-1}q^{n+1}\) and \(2np^nq^n\). Under \(q=c/\sqrt n\) their sum tends to zero, while the binomial count tends to a Poisson distribution of mean \(c^2\). Therefore the reliability limit is \(\Pr(\operatorname{Poisson}(c^2)\le1)=(1+c^2)e^{-c^2}\). Moreover, if \(\sqrt n q\to0\) reliability tends to one, while if \(\sqrt n q\to\infty\) it tends to zero, using the bound by the probability of at most one completely omitted pair.

## Verification
A standalone standard-library program, `verify.py`, independently constructs the original adjacency relation and enumerates every vertex subset for each \(2\le n\le9\). It checks nonempty pairwise distinct open-neighborhood signatures directly, compares the resulting complete coefficient tables against the stated polynomial, and independently checks the stated profile criterion. All comparisons passed. Integer coefficient and minimum-multiplicity calculations were additionally repeated for \(5\le n\le200\). These finite tests are corroboration, not a proof of the unbounded claims.

## Relationship to prior work
Hernando, Mora and Pelayo (2017) develop locating domination for bipartite graphs and their complements, studying minimum cardinalities and comparison bounds; their inspected manuscript does not enumerate all locating-dominating sets of crown graphs. Bousquet, Deschamps, Lehtilä and Parreau (2022) study directed variants and complexity, but their inspected treatment does not provide this enumerator. Chakraborty, Foucaud, Henning and Laihonen (2026) study partitioning into dominating and locating-dominating sets and the half-order problem, rather than this distribution. Existing exact edge-metric bases for crown graphs concern distances to **edges**, not distinct nonempty open-neighborhood signatures of unselected **vertices**; the predicates are not interchangeable. The known edge-metric bases number \(n2^{n-1}\) at size \(n-1\), whereas the present locating-dominating sets of that size number \(n(2^{n-1}-2n)\), excluding precisely the \(2n^2\) configurations with fewer than two selected vertices on one side. The claimed advance is the full polynomial and its reliability limit, not the original definition of locating domination or general complexity theorems.

## Limitations
No independent mathematical audit has been performed. The all-parameter proof is elementary and explicit, but a prior unpublished or unindexed crown-graph locating-domination enumeration could establish the same result; public-source searches cannot establish unique publication priority. Finite exhaustive tests cover only the sizes stated above. The probabilistic conclusion assumes independent vertex selection with equal probability and does not address correlated sensor failures.

## References
1. C. Hernando, M. Mora and I. M. Pelayo, *Locating domination in bipartite graphs and their complements*, arXiv:1711.01951v1 (2017-11-03), https://arxiv.org/abs/1711.01951.
2. N. Bousquet, Q. Deschamps, T. Lehtilä and A. Parreau, *Locating-dominating sets: From graphs to oriented graphs*, arXiv:2112.01910v1 (2021-12-03), https://arxiv.org/abs/2112.01910.
3. D. Chakraborty, F. Foucaud, M. A. Henning and T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, Electronic Journal of Combinatorics **33** (2026), #P1.51, https://doi.org/10.37236/14049.
4. *Edge metric bases of crown graphs*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8 (full published RESULT.md inspected).
