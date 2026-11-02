# A sharp \(2/n\) failure law for random greedy matching on crown graphs

## Finding

Let \(n\ge2\), and let \(C_n\) be the **crown graph** with bipartition \(L=\{\ell_1,\ldots,\ell_n\}\) and \(R=\{r_1,\ldots,r_n\}\), where \(\ell_i\) is adjacent to \(r_j\) if and only if \(i\ne j\). Process all \(n(n-1)\) edges in a uniformly random order, accepting an edge exactly when both endpoints are still unmatched. Let \(Q_n\) be the probability that the resulting maximal matching is not perfect, and let \(H_n=\sum_{j=1}^n 1/j\).

Then the final matching always has either \(n\) or \(n-1\) edges, and, for every \(n\ge2\),
\[
0\le \frac{2}{n+1}-Q_n\le \frac{16H_n}{n^2}.
\]
In particular,
\[
Q_n=\frac2n+O\!\left(\frac{\log n}{n^2}\right),\qquad
\lim_{n\to\infty}nQ_n=2.
\]
There is also a finite exact rational recurrence: define \(F_{1,0}=0\), \(F_{1,1}=1\), and for \(2\le k\le n\) and \(0\le r\le k\),
\[
F_{k,r}=\frac{r(r-1)F_{k-1,r-2}+2r(k-r)F_{k-1,r-1}+(k-r)^2F_{k-1,r}}{k^2-r},
\]
with zero-weight or out-of-range terms omitted. Then \(Q_n=F_{n,n}\). For example, \(Q_2=0\), \(Q_3=1/3\), and \(Q_4=Q_5=4/21\).

## Assumptions and scope

The graph is deterministic, balanced and obtained from a complete bipartite graph by removing exactly one perfect matching. All remaining edges have identical priority distribution and ties are absent. The random permutation model is equivalent to repeatedly selecting a uniformly random **currently feasible** edge and deleting both of its endpoints. The conclusion concerns the number of accepted edges, not a minimum-cost or online vertex-arrival matching algorithm. The parameter \(n\) is an integer at least \(2\).

## Proof

**1. Terminal obstruction and lumped chain.** With \(k\) unmatched vertices on each side, write \(A,B\subseteq\{1,\ldots,n\}\) for their label sets; \(|A|=|B|=k\). Let \(R_k=|A\cap B|\). There are \(k^2-R_k\) feasible edges. For \(k\ge2\), this is at least \(k(k-1)>0\), so the matching can stop prematurely only with exactly one vertex unmatched on each side, and these two vertices must have the same label. Thus \(Q_n=\Pr(R_1=1)\).

Conditional on \(R_k=r\), the ordered pair of removed labels belongs to one of three disjoint classes. Removing two distinct shared labels has count \(r(r-1)\) and sends \(r\) to \(r-2\). Removing exactly one shared label has count \(2r(k-r)\) and sends \(r\) to \(r-1\). Removing no shared label has count \((k-r)^2\) and preserves \(r\). The total is \(k^2-r\). This proves the finite recurrence and the conditional first moment
\[
\mathbb E[R_{k-1}\mid R_k=r]
=r-\frac{2r(k-1)}{k^2-r}.
\]
The initial condition is \(R_n=n\).

**2. A nearly conserved first moment.** Dividing the displayed conditional expectation by \(k(k-1)\), and subtracting \(r/[k(k+1)]\), gives the exact identity
\[
\mathbb E\!\left[\frac{R_{k-1}}{k(k-1)}\middle|R_k=r\right]
-\frac{r}{k(k+1)}
=-\frac{2r(r-1)}{k(k-1)(k+1)(k^2-r)}.
\]
Telescoping from \(k=n\) down to \(k=2\), using \(\mathbb E R_n/[n(n+1)]=1/(n+1)\) and \(\mathbb E R_1/2=Q_n/2\), yields the **exact defect identity**
\[
\frac2{n+1}-Q_n
=4\sum_{k=2}^n
\mathbb E\left[\frac{R_k(R_k-1)}{k(k-1)(k+1)(k^2-R_k)}\right]. \tag{1}
\]
Every summand is nonnegative; in particular, \(Q_n\le2/(n+1)\).

**3. A second-factorial-moment contraction.** Given \(R_k=r\ge2\), choose two distinct shared labels. They both remain shared after the next accepted edge precisely when neither label is selected. The number of feasible edges avoiding both labels is \((k-2)^2-(r-2)\). Thus
\[
\mathbb E[(R_{k-1})_2\mid R_k=r]
=(r)_2\frac{(k-2)^2-(r-2)}{k^2-r},
\qquad (x)_2=x(x-1).
\]
For \(2\le r\le k\) the displayed ratio is decreasing in \(r\). Its value at \(r=2\) satisfies
\[
\frac{(k-2)^2}{k^2-2}\le
\left(\frac{k-1}{k}\right)^4,\qquad k\ge2.
\]
Indeed, after multiplying through by the positive denominators, this is exactly the polynomial inequality \(4k^3-11k^2+8k-2\ge0\), which holds at \(k=2\) and is increasing thereafter. The formula is also trivial when \(r=0,1\). Iteration from \(R_n=n\) therefore gives
\[
\mathbb E[(R_k)_2]\le n(n-1)\left(\frac{k}{n}\right)^4\le\frac{k^4}{n^2}
\qquad (1\le k\le n). \tag{2}
\]

**4. Uniform bound and limit.** Since \(R_k\le k\), one has \(k^2-R_k\ge k(k-1)\) for \(k\ge2\). Applying (2) term by term in (1) yields
\[
0\le\frac2{n+1}-Q_n
\le\frac4{n^2}\sum_{k=2}^n\frac{k^2}{(k-1)^2(k+1)}
\le\frac{16}{n^2}\sum_{k=2}^n\frac1{k+1}
\le\frac{16H_n}{n^2}.
\]
This proves all stated inequalities, and \(H_n=O(\log n)\) gives the asymptotic result. No asymptotic independence assumption or finite-size extrapolation is required.

## Verification

Run `python3 checker.py` with Python 3. The standalone checker independently implements: (i) the exact rational chain on overlap counts for sizes \(2\) through \(10\); (ii) a separate bit-mask dynamic program over actual unmatched vertex subsets for sizes \(2\) through \(6\); (iii) direct enumeration of all \(6!\) eligible edge permutations for size \(3\); (iv) integer checks of the factorial contraction inequality; and (v) numerical evaluations through size \(2000\). These calculations verify finite instances but do not replace the all-size proof above. The checker has no nonstandard Python dependencies.

## Relationship to prior work

Random greedy matching in which the next edge is selected uniformly from the feasible edges is classical; see Dyer and Frieze (1991). Arnosti (2021) gives a precise RANDOM-EDGE definition and average-case algorithm comparisons when the bipartite **edge set is random**. Tang, Wu and Zhang (2019/2023) give worst-case approximation guarantees for different randomized greedy algorithms in the oblivious matching setting. Neither of those identified results implies the displayed exact crown-graph deficiency probability or its sharp \(2/n\) coefficient: the present edge set is fixed, the output is nearly perfect, and the statistic is a rare-event probability rather than an approximation ratio.

A uniform random matching of \(n-1\) pairs in the *undeleted* complete bipartite graph leaves a uniformly random pair of unmatched labels; their coincidence probability is \(1/n\). That is only a comparison benchmark, not the crown-graph process: forbidden-edge avoidance changes the final coincidence constant from \(1\) to \(2\). No exhaustive assertion of historical priority is made.

## Limitations

The result is limited to the exact one-factor-deleted balanced complete bipartite family and the uniform random-edge greedy algorithm. It does not give a corresponding constant for multiple deleted matchings, arbitrary forbidden-edge patterns, or vertex-order greedy matching. The error bound is explicit but its numerical constant is not optimized. The originality assessment is literature-search-based rather than an independent exhaustive priority proof.

## References

- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150, first published online November 2, 2021. https://doi.org/10.1287/stsy.2021.0082
- Z. G. Tang, X. Wu, Y. Zhang, *Towards a Better Understanding of Randomized Greedy Matching*, first posted July 11, 2019, arXiv:1907.05135; subsequently published as *Toward a Better Understanding of Randomized Greedy Matching*, Journal of the ACM 70 (2023), article 39. https://arxiv.org/abs/1907.05135
- M. E. Dyer and A. M. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104
