# Sharp low-budget power domination on Cartesian clique paths

## Finding

For integers \(n,L\geq3\), let \(G_{n,L}=K_n\square P_L\). The complete-graph factor gives \(L\) clique layers, each containing \(n\) vertices, with a matching between consecutive layers. A set \(S\) *power dominates* the graph if observing its closed neighborhood and then iteratively observing the unique unobserved neighbor of any observed vertex eventually observes the graph.

**Sharp low-budget characterization.** For every \(S\subseteq V(G_{n,L})\) satisfying \(|S|\leq n-2\), \(S\) power dominates if and only if at least one of these conditions holds:

1. \(S\) meets one of the endpoint layers;
2. \(S\) meets two consecutive layers.

The bound is sharp: for every \(n,L\geq3\), a set of \(n-1\) vertices all in the second layer can power dominate without satisfying either condition.

Let \(\mathcal P_{n,L}(z)=\sum_{S\text{ power dominating}}z^{|S|}\), and let \(I_{P_{L-2}}(u)\) be the ordinary independent-set polynomial of a path with \(L-2\) vertices. Then

\[
\boxed{\mathcal P_{n,L}(z)\equiv (1+z)^{nL}-I_{P_{L-2}}((1+z)^n-1)\pmod {z^{n-1}}.}
\]

The independent-set polynomial is explicit:
\[
I_{P_{L-2}}(u)=\sum_{j=0}^{\lfloor(L-1)/2\rfloor}\binom{L-1-j}{j}u^j.
\]

In particular, for every \(0\leq k\leq n-2\), the number \(p_{n,L}(k)\) of successful \(k\)-vertex sets equals
\[
\binom{nL}{k}-\sum_{j=0}^{\lfloor(L-1)/2\rfloor}\binom{L-1-j}{j}
\sum_{h=0}^j(-1)^{j-h}\binom jh\binom{nh}{k},
\]
with \(\binom ab=0\) when \(b>a\) for nonnegative integers. Thus \(p_{n,L}(0)=0\) and \(p_{n,L}(1)=2n\). For \(n\geq4\),
\[
p_{n,L}(2)=\binom{nL}{2}-\binom{n(L-2)}{2}+(L-3)n^2.
\]

The layer-sensitive statement is stronger. With \(z_t\) recording selections in layer \(t\), and \(\mathcal P_{n,L}(z_1,\ldots,z_L)\) the multivariate successful-set enumerator,
\[
\mathcal P_{n,L}(z_1,\ldots,z_L)
\equiv \prod_{t=1}^L(1+z_t)^n-
\sum_{I\subseteq\{2,\ldots,L-1\}:\,I\text{ has no consecutive elements}}
\prod_{t\in I}\big((1+z_t)^n-1\big)
\]
modulo all monomials of total degree at least \(n-1\). The empty product is \(1\). At total degree \(n-1\) this formula need not hold: the coefficient of \(z_2^{n-1}\) in the exact polynomial exceeds the coefficient of the displayed approximation by precisely \(n\).

**Sparse independent-sensor law.** Independently select each vertex with probability \(p\). Write \(a=(1-p)^n\), \(b=1-a\), and
\[
Q_{n,L}(p)=1-\sum_{j=0}^{\lfloor(L-1)/2\rfloor}\binom{L-1-j}{j}b^j a^{L-j}.
\]
Then for every \(0\leq p\leq1\),
\[
0\leq\Pr_p(S\text{ power dominates})-Q_{n,L}(p)
\leq\Pr\big(\operatorname{Bin}(nL,p)\geq n-1\big).
\]
Consequently, for fixed \(L\geq3\) and \(c\geq0\), using \(p=c/n\) for sufficiently large \(n\),
\[
\boxed{\lim_{n\to\infty}\Pr_{c/n}(S\text{ power dominates})
=1-e^{-cL}I_{P_{L-2}}(e^c-1).}
\]

## Assumptions and scope

The graph is undirected and simple. Its vertex set is \(\{(t,j):1\leq t\leq L,\ 1\leq j\leq n\}\). Distinct \((t,j)\) and \((s,i)\) are adjacent exactly when either \(s=t\) and \(i\neq j\), or \(i=j\) and \(|s-t|=1\). The initial domination step observes \(N[S]\), including \(S\). Each later forcing step permits an observed vertex to observe its unique as-yet-unobserved neighbor. All observations are monotone. The initial vertex set may be empty, and its unsuccessful status is reflected by the zero constant coefficient. The congruence is a claim about exactly the coefficients through degree \(n-2\), not about the entire polynomial.

## Proof

**1. Sufficient layer patterns.** If a seed lies in endpoint layer \(1\), the initial domination step observes every vertex of that clique. For each column, its endpoint vertex now has, outside its already observed clique, at most one unobserved neighbor, namely the corresponding vertex of layer \(2\). It can therefore force that neighbor whenever necessary. The second layer becomes fully observed. Repeat along successive matching links to reach layer \(L\). The other endpoint is symmetric. Alternatively, suppose \(S\) meets consecutive layers \(t\) and \(t+1\). Both entire clique layers are observed immediately. On the left frontier each vertex in layer \(t\) has only its neighbor in layer \(t-1\) potentially unobserved, and on the right frontier each vertex of layer \(t+1\) has only its neighbor in layer \(t+2\) potentially unobserved. Forcing propagates outward along both sides. Thus either stipulated layer pattern is sufficient for any size of \(S\).

**2. Necessary layer pattern below the cutoff.** Assume neither pattern occurs and \(|S|\leq n-2\). Every seed lies in an interior layer, and any two occupied layers are nonconsecutive. Let \(C\) be the set of column indices that contain at least one seed in any layer. Then \(|C|\leq|S|\leq n-2\), so there are at least two column indices outside \(C\). Consider the following invariant after the initial domination step and after every forcing step:

> In every layer containing no seed, each vertex whose column lies outside \(C\) remains unobserved.

Initially an unoccupied layer can be observed only through matching edges from adjacent seeded layers, so every observed vertex there has a column in \(C\). To preserve the invariant, examine any observed vertex. If it lies in an unoccupied layer, its column belongs to \(C\) and it has at least two still-unobserved clique neighbors outside \(C\). It cannot force any vertex. If it lies in an occupied layer, its clique is fully observed from the domination step. Because that layer is interior and both adjacent layers are unoccupied, an observed vertex with column outside \(C\) has two unobserved matching neighbors, one on each side, so it cannot force. A vertex of column in \(C\) in an occupied layer can force, at most, a matching neighbor in a column of \(C\), which does not violate the invariant. Hence the invariant is preserved. Endpoint layers contain no seeds and retain unobserved vertices outside \(C\); propagation cannot finish. This proves necessity.

**3. Sharpness.** Place \(n-1\) seeds in the second layer, omitting one column \(j_*\). Initially all of layer \(2\), plus \(n-1\) vertices in layer \(1\), are observed. Every observed layer-\(1\) vertex can force its missing clique neighbor \((1,j_*)\), since its matching neighbor in layer \(2\) is already observed. Then the first layer is full. With two consecutive complete layers available, Step 1 applies to finish observation in all later layers. Nevertheless the seed set occupies no endpoint or consecutive layers. Exactly \(n-1\) is therefore the first possible cardinality at which the characterization fails.

**4. Counting.** For \(k\leq n-2\), failure is equivalent to an empty endpoint pair and an independent pattern of occupied interior layers. There are \(\binom{L-1-j}{j}\) independent choices of exactly \(j\) vertices in a path on \(L-2\) layers. For each chosen layer, the generating function of nonempty subsets of its \(n\) vertices is \((1+z)^n-1\). This gives the asserted failed-set polynomial, coefficientwise through degree \(n-2\). Subtracting from \((1+z)^{nL}\) gives the first displayed congruence; expanding \(((1+z)^n-1)^j\) by the binomial theorem gives the coefficient formula. Replacing \(z\) by layer-specific indeterminates proves the multivariate statement. At degree \(n-1\), exactly \(\binom{n}{n-1}=n\) sets concentrated in layer \(2\) are successful by Step 3, although the layer-pattern approximation excludes them, establishing the claimed sharp coefficient discrepancy.

**5. Reliability.** The sufficient layer-pattern event has probability \(Q_{n,L}(p)\): all endpoint layers must be empty for its complement, and the occupied interior layers must form an independent subset \(I\), whose exact probability is \(b^{|I|}a^{L-|I|}\). Any successful set not counted by that event has cardinality at least \(n-1\), by Step 2. This proves the sandwich bound. With \(p=c/n\) and fixed \(L\), the number of selected vertices is binomial with mean \(Lc\); its probability of reaching \(n-1\) tends to zero (for example by a factorial-moment bound). Also \(a=(1-c/n)^n\to e^{-c}\) and \(b\to1-e^{-c}\). Passing to the limit yields the displayed expression.

## Verification

The standalone file `verify.py` reconstructs all edges directly from the graph definition and implements the power-domination process by repeated unique-neighbor propagation. For every \(3\leq n\leq6\) and \(3\leq L\leq7\), it exhaustively checks every vertex subset of cardinality at most \(n-2\) against the layer-pattern criterion, compares the exact low-degree counting coefficients with the independence-polynomial formula, and verifies the \(n-1\)-seed sharpness construction. This is **257,426 checked subsets across 20 dimension pairs**, all passed. Run `python verify.py` with a standard Python interpreter. The universal statement is proved above; the finite checks are only corroboration and do not certify infinitely many instances.

## Relationship to prior work

Power domination is the standard observation-and-propagation process of electrical-network monitoring. Koh and Soh analyze its Cartesian products and note that a single appropriately placed vertex suffices for the complete-graph-by-path family; that minimum-value observation is not claimed as new here. Brimkov, Patel, Suriyanarayana, and Teich introduce the power domination polynomial and provide formulas for several graph families, including paths, complete graphs, cycles, and threshold graphs, together with general decomposition properties. Their inspected results do not give the present coefficient window for Cartesian clique paths. Anderson, Kuenzel, and Schuerger give bounds for power domination on Cartesian products, including a Vizing-like inequality and failed-power-domination partitions. Those bounds do not determine the successful-set layer patterns, the low-degree coefficient formula, or the sparse-sensor limit. The new claim is the sharp all-set low-budget structural classification with its counting and reliability consequences, not the known fact that the minimum power domination number is one.

## Limitations

For cardinalities at least \(n-1\), the endpoint/consecutive-layer condition remains sufficient but need not be necessary; the expression in the theorem is not asserted to give higher coefficients. The Bernoulli formula is asymptotically exact only for fixed \(L\) in the regime \(p=c/n\); the explicit bound handles arbitrary finite \(n,L,p\). Literature-priority risk remains for unindexed or differently formulated descriptions of this Cartesian product. No independent mathematical audit has been performed.

## References

1. S. E. Anderson, K. Kuenzel, H. Schuerger, *Graphs which satisfy a Vizing-like bound for power domination of Cartesian products*, arXiv:2209.03930v1, publicly submitted 2022-09-08. https://arxiv.org/abs/2209.03930
2. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, publicly submitted 2018-05-28. https://arxiv.org/abs/1805.10984
3. K. M. Koh, K. W. Soh, *Power domination of the cartesian product of graphs*, AKCE International Journal of Graphs and Combinatorics 13 (2016), 22–30, doi:10.1016/j.akcej.2016.02.004.
