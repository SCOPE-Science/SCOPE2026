# A single social tie can raise best-shot equilibrium multiplicity: exact chord placement on rings

## Finding

**Theorem (equilibrium-count and optimal-link law).** Let \(n\geq5\). There are \(n\) players, indexed cyclically by \(0,\ldots,n-1\), with an undirected contact ring and one additional link between player \(0\) and player \(d\), where \(2\leq d\leq n-2\). Each player chooses whether to provide a locally shared public good; giving the good is costly, but receiving it from oneself or any neighbor is valuable. Let \(M_{n,d}\) count the pure-strategy Nash equilibria after the link addition.

Define the integer sequences \(c_0=1,c_1=0,c_2=1\), \(P_0=3,P_1=0,P_2=2\), with
\[
c_j=c_{j-2}+c_{j-3},\qquad P_j=P_{j-2}+P_{j-3}\quad(j\geq3).
\]
Then every permitted link has the *exact* equilibrium count
\[
\boxed{M_{n,d}=P_n-c_dc_{n-d}+2c_{d-2}c_{n-d-2}.}
\]
Among all such single-link interventions, the minimum is
\[
\boxed{\min_{2\leq d\leq n-2}M_{n,d}=P_n-c_{n-3},}
\]
and is attained **if and only if** \(d\in\{3,n-3\}\) (for \(n=5\) this set comprises the two equivalent orientations of the only chord type). Thus, up to reflection, the unique most equilibrium-reducing new link spans three existing ring edges.

A counterintuitive opposite effect holds for the shorter link: for every \(n\geq6\),
\[
M_{n,2}-P_n=c_{n-4}-c_{n-5}\geq0.
\]
The inequality is strict for \(n=6\), \(n=9\), and every \(n\geq11\); equality holds precisely for \(n\in\{7,8,10\}\). Hence adding a distance-two social tie generally *increases*, rather than decreases, the number of equilibria.

Writing \(\alpha=1.324717957\ldots\) for the unique real root of \(\alpha^3=\alpha+1\), the optimal-link effect has the sharp limit
\[
\lim_{n\to\infty}\frac{\min_d M_{n,d}}{P_n}=1-\frac1{2\alpha+3}=0.822991\ldots,
\]
so the asymptotic equilibrium-multiplicity reduction is \(17.7008\ldots\%\).

## Assumptions and scope

The graph is finite, undirected, and simple. Each player \(i\) chooses \(x_i\in\{0,1\}\). For arbitrary constants \(0<c<v\), the payoff is
\[
u_i(x)=v\,\mathbf1\!\left\{x_i+\sum_{j:\,ij\in E}x_j\geq1\right\}-c x_i.
\]
The network is held fixed during play. Only **pure-strategy Nash equilibria** are counted; social welfare, dynamics, equilibrium selection and costs of adding links are not optimized. A chord is a new edge joining previously nonadjacent vertices; its clockwise separation \(d\) belongs to the stated range. No homogeneity beyond the shared positive-cost, shared-benefit best-response condition is used.

The primary object is the number of pure equilibria of this noncooperative network public-goods game under a permitted single social-tie intervention, fitting noncooperative game theory (MSC2020 91A10). The maximal-independent-set representation is a proof device and an equivalent combinatorial formulation.

## Proof

**1. Best-response equivalence.** If no neighbor provides, providing changes player \(i\)'s payoff from \(0\) to \(v-c>0\); if any neighbor provides, withdrawing changes the payoff from \(v-c\) to \(v\). Thus the unique best response is \(x_i=1\) exactly when all neighbors choose \(0\). A profile is a pure equilibrium if and only if its set of contributors is an *independent dominating set* (equivalently, a maximal independent set) of the graph.

**2. Counts on the unmodified ring.** Ring equilibrium profiles are exactly cyclic binary words with neither two adjacent \(1\)'s nor three consecutive \(0\)'s. In particular, the successive spacings between chosen vertices are all \(2\) or \(3\). The count on the plain ring is \(P_n\), the Perrin sequence; this is also obtained by a three-state trace transfer matrix and is established in the cited cycle enumeration literature. The number of ordered compositions of an integer \(k\geq0\) into pieces of lengths \(2\) and \(3\) is \(c_k\): the empty composition counts once, there is none for \(k=1\), and the last-part recurrence gives the definition of \(c_k\).

**3. Exact effect of the added edge.** A previously valid ring equilibrium ceases to be one precisely when both chord endpoints, \(0\) and \(d\), had chosen \(1\); there are \(c_dc_{n-d}\) such words. Indeed, the clockwise path of length \(d\) and complementary path of length \(n-d\) each decompose uniquely into spacings \(2\) or \(3\), independently subject to their chosen endpoints.

Conversely, a contributor configuration that is independent on the ring but not a ring equilibrium can become an equilibrium only if the **sole** formerly undominated vertex is one of the two new-link endpoints and the other endpoint is a contributor. Suppose \(0\) contributes and \(d\) does not, with neither ring neighbor of \(d\) contributing. To dominate the two neighboring unchosen vertices \(d-1\) and \(d+1\) on the ring, \(d-2\) and \(d+2\) must contribute. The two remaining arcs, each with contributing endpoints, have lengths \(d-2\) and \(n-d-2\), respectively, and each breaks into spacings \(2\) or \(3\). This gives exactly \(c_{d-2}c_{n-d-2}\) rescued configurations. Swapping chord endpoints gives a disjoint, equally sized class. The convention \(c_0=1,c_1=0\) handles adjacent forced endpoints and incompatible short arcs correctly. These are all possibilities, proving
\[
M_{n,d}=P_n-c_dc_{n-d}+2c_{d-2}c_{n-d-2}.
\]

**4. Global and unique optimality.** Put \(m=n-d\) and define the difference from the three-step intervention,
\[
D(d,m)=c_{d+m-3}-c_dc_m+2c_{d-2}c_{m-2},\qquad d,m\geq2.
\]
It follows from the count formula and \(c_3=1,c_1=0\) that
\[
M_{n,d}-(P_n-c_{n-3})=D(d,n-d).
\]
For each fixed \(d\), the defining recurrence gives
\[
D(d,m)=D(d,m-2)+D(d,m-3)\quad(m\geq5).
\]
Direct substitution gives \(D(d,3)=0\) for all \(d\geq2\). Moreover, the two sequences \(D(d,2)\) and \(D(d,4)\), as functions of \(d\), also obey the same recurrence for \(d\geq5\), with respective first three values at \(d=2,3,4\):
\[
(D(2,2),D(3,2),D(4,2))=(1,0,2),
\]
\[
(D(2,4),D(3,4),D(4,4))=(2,0,3).
\]
Each of those sequences is nonnegative and vanishes exactly at \(d=3\): the next term is a sum of two earlier terms, so strict positivity thereafter follows from the first three terms. Induction on \(m\), starting from \(2,3,4\), now proves
\[
D(d,m)\geq0,\qquad D(d,m)=0\iff(d=3\text{ or }m=3).
\]
This proves both global minimum and all equality cases. The formal base \(d=m=2\) helps the algebraic induction but does not assert a nonexisting chord in a four-player ring.

**5. Increase for the two-step link.** Substituting \(c_2=1,c_0=1\) gives
\[
M_{n,2}-P_n=2c_{n-4}-c_{n-2}=c_{n-4}-c_{n-5}.
\]
Set \(\delta_j=c_j-c_{j-1}\) for \(j\geq2\). The recurrence for \(c\) gives \(\delta_j=\delta_{j-2}+\delta_{j-3}\) when \(j\geq5\), and the bases \((\delta_2,\delta_3,\delta_4)=(1,0,0)\). Hence \(\delta_j\geq0\), and \(\delta_j=0\) only when \(j\in\{3,4,6\}\); all \(j\geq7\) are positive. For \(n\geq6\), this yields exactly the stated exceptional sizes and strict cases.

**6. Asymptotic effect.** The generating function is \(\sum_{j\geq0}c_jz^j=(1-z^2-z^3)^{-1}\). Its dominant positive simple pole is \(z=1/\alpha\) and the two other roots have larger modulus, giving
\[
c_j\sim\frac{\alpha^{j+3}}{2\alpha+3}.
\]
The Perrin sequence is the sum of the \(j\)-th powers of the three roots of \(t^3-t-1\), so \(P_n\sim\alpha^n\). Consequently \(c_{n-3}/P_n\to(2\alpha+3)^{-1}\). The claimed limiting fraction follows.

## Verification

Run `python3 check.py` with Python 3.9 or later. The checker independently enumerates all \(2^n\) binary profiles for **every** permissible chord of each ring size \(5\leq n\leq17\), using each player's payoff-equivalent best-response condition rather than the formula, and compares the count. It also verifies the exact global minimizing distances, the two-step-link identity for \(6\leq n\leq1300\), the positive difference certificate on a large integer grid, the two-variable recurrence certificate, and asymptotic ratios. The successfully replayed checker reports `VERIFY_OK assertions=21353`.

These finite checks do **not** prove the universal assertions. The proof is the decomposition and the nonnegative double recurrence above. Example: a twelve-player ring has \(P_{12}=29\) equilibria; a two-step chord gives \(30\), while a three-step chord gives the optimal \(24\).

## Relationship to prior work

Dall'Asta, Pin and Ramezanpour (first posted February 18, 2010) establish precisely this locally provided binary public-goods game and its correspondence between pure equilibria and maximal independent sets. Their planner changes players' incentives while treating network structure as exogenous; their results do not enumerate link-distance-dependent equilibrium counts on an augmented ring. Bisdorff and Marichal (first posted January 23, 2007) establish the Perrin count and more refined orbit enumerations **for the unaugmented cycle**, not a cycle with an extra chord. This is the baseline needed in the proof, not an independently novel claim. Bramoullé and Kranton (2007) investigate provision incentives and welfare changes from social links, not the exact count and uniquely minimizing chord across all sizes. Sagan and Vatter (2006) give extremal counts over much broader graph classes under a cycle-rank constraint; such upper-bound extremal results do not supply the exact value for each chord length.

The contribution asserted here is the explicit one-link gain-and-loss formula, its global optimizing chord, and the equilibrium-multiplicity increase caused by a shorter link. No independent historical-priority certification is claimed; a result under another terminology for chorded-cycle independent domination could predate the present statement.

## Limitations

This is a deterministic, finite, binary-action game with nonnegative local spillovers and no equilibrium selection mechanism. Counting equilibria does not rank them by welfare, predict which are reached, or justify modifying any real network. The ring assumption, one new edge, and identical best-response pattern are essential to the simple closed formula. The displayed asymptotic reduction refers to the **number of pure equilibria**, not to average public-good participation or welfare. Formal priority beyond the inspected primary articles and indexed mathematical records is unverified.

## References

1. L. Dall'Asta, P. Pin and A. Ramezanpour, *Optimal equilibria of the best shot game*, arXiv:1002.3572, first public February 18, 2010. https://arxiv.org/abs/1002.3572 ; full text https://arxiv.org/html/1002.3572 .
2. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647, first public January 23, 2007; *Journal of Integer Sequences* 11 (2008). https://arxiv.org/html/math/0701647v2 .
3. Y. Bramoullé and R. Kranton, *Public goods in networks*, *Journal of Economic Theory* 135 (2007), 478–494. https://doi.org/10.1016/j.jet.2006.06.006 .
4. B. E. Sagan and V. R. Vatter, *Maximal and maximum independent sets in graphs with at most r cycles*, *Journal of Graph Theory* 53 (2006), 283–314. https://doi.org/10.1002/jgt.20186 .
5. OEIS A001608, *Perrin sequence*, including the cycle maximal-independent-set interpretation. https://oeis.org/A001608 .
