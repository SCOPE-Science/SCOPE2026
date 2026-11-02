# Sharp bottleneck bandwidth for classically \(123\)-avoiding cyclic tours

## Finding

For every integer \(n\ge3\), a permutation \(\pi=(\pi_1,\ldots,\pi_n)\) of \(\{1,\ldots,n\}\) *classically avoids \(123\)* when no indices \(i<j<k\) satisfy \(\pi_i<\pi_j<\pi_k\). Define its cyclic jump bandwidth by
\[
B(\pi)=\max_{1\le i\le n}|\pi_{i+1}-\pi_i|,\qquad \pi_{n+1}=\pi_1.
\]
Then the exact extremal invariant is
\[
\boxed{\min_{\pi\in\operatorname{Av}_n(123)}B(\pi)
=\max\left\{2,\left\lceil\frac{n-1}{3}\right\rceil\right\}.}
\]
Equivalently, for integers \(m\ge2\) and \(n\ge3\), a classically \(123\)-avoiding ordered Hamiltonian cycle of the path power \(P_n^m\) exists if and only if \(n\le3m+1\). Here an ordered cycle has a distinguished first vertex, and avoidance is applied to that *one linear reading*, not to all cyclic rotations.

At the sharp upper-length boundary \(n=3m+1\), every qualifying permutation is rigid at its four endpoint positions:
\[
\boxed{(\pi_1,\pi_2,\pi_{n-1},\pi_n)
=(2m+1,3m+1,1,m+1).}
\]

## Assumptions and scope

Throughout, the labels are distinct integers \(1,\ldots,n\); the jump bound is on their *ordinary numerical differences*, including the return edge from last to first. A path power \(P_n^m\) has an edge between distinct labels at numerical distance at most \(m\). Pattern avoidance is classical subsequence avoidance in a fixed reading, not cyclic avoidance under every rotation and not avoidance of only consecutive triples. All assertions quantify over integers \(n\ge3\), \(m\ge2\), apart from the separate observation about \(m=1\).

## Proof

**Endpoint obstruction.** Suppose \(\pi\) avoids \(123\), and its *linear* adjacent differences are at most \(m\). Let \(a=\pi_1\). If \(a<n\), let \(j\) be the first subsequent position whose entry exceeds \(a\). Necessarily \(\pi_j=n\): if \(a<\pi_j<n\), the later occurrence of \(n\) would make an increasing triple. Every entry strictly before \(j\) is at most \(a\), so the predecessor \(\pi_{j-1}\) satisfies \(\pi_{j-1}\le a\). From the jump constraint, \(n-m\le\pi_{j-1}\le a\). The same endpoint bound is trivial if \(a=n\). Thus \(\pi_1\ge n-m\).

Reverse-complementation \(\pi_i\mapsto n+1-\pi_{n+1-i}\) preserves classical \(123\)-avoidance and absolute jumps. Applying the first bound to the reversed-complemented permutation gives \(\pi_n\le m+1\). If the return edge is also bounded by \(m\), then
\[
n-2m-1\le\pi_1-\pi_n\le m,
\]
so \(n\le3m+1\). In particular, this holds even if \(m=1\), but for \(m=1\) no Hamiltonian cycle of \(P_n^1=P_n\) exists when \(n\ge3\).

**Attainment at every allowed length.** Fix \(m\ge2\). When \(3\le n\le m+1\), take the decreasing permutation. Its largest cyclic jump is \(n-1\le m\).

Now assume \(m+2\le n\le3m+1\), set \(a=n-m\), \(b=\max\{1,n-2m\}\), and form
\[
\pi=(a,\ n,n-1,\ldots,a+1,\ a-1,a-2,\ldots,1\ \text{with }b\text{ deleted},\ b).
\]
Both displayed runs are read in decreasing order, and an empty run is allowed. This is a permutation because \(a\ge2\), \(1\le b<a\), and every label other than \(a,b\) occurs exactly once in the middle. Its middle block (after \(a\), before \(b\)) is strictly decreasing. An increasing triple therefore cannot lie in that block. Such a triple cannot start at \(a\), since all middle entries larger than \(a\) decrease and the last entry \(b<a\). Nor can it end at \(b\), since the middle entries smaller than \(b\) decrease and \(a>b\). Thus the word classically avoids \(123\).

The jump from \(a\) to \(n\) is exactly \(m\). Adjacent jumps internal to the descending block are either one or two: the only skipped labels are \(a,b\). The jump into the final \(b\) is at most \(\max\{2,b-1\}\), and the closing jump is \(a-b\). If \(n\le2m+1\), then \(b=1\) and \(a-b=n-m-1\le m\). If \(n\ge2m+2\), then \(b=n-2m\le m+1\), and \(a-b=m\). Every jump is at most \(m\), using \(m\ge2\). This proves feasibility for all \(n\le3m+1\), matching the obstruction.

**Four-position rigidity.** Let \(n=3m+1\) and let a feasible \(\pi\) be given. The inequalities above and the closing-edge bound force \(\pi_1=2m+1\) and \(\pi_n=m+1\). In the endpoint argument, the first entry larger than \(\pi_1\) must be \(n\). Its predecessor must be at least \(n-m=\pi_1\), but all entries preceding that first exceedance are at most \(\pi_1\). Hence that predecessor is the unique first-position value \(\pi_1\), so \(\pi_2=n\). Apply the same argument to the reverse-complement to get \(\pi_{n-1}=1\). The rigidity assertion follows.

For fixed \(n\ge3\), the obstruction, construction, and the impossibility at \(m=1\) yield exactly the displayed minimum cyclic bandwidth.

## Verification

The standalone file `verify_cyclic_jump.py` independently tests the result using two finite methods. A cubic triple search examines every classical \(123\)-avoiding permutation for \(3\le n\le9\), computes its actual cyclic bandwidth, and confirms the optimum. A separate prefix-growth enumerator checks *all* boundary permutations for \(m=2,3,4\), finding respectively \(1,4,35\) labelled examples and confirming all four forced boundary positions. Finally, the explicit construction is evaluated for \(2418\) parameter pairs with \(2\le m\le40\) and \(3\le n\le3m+1\), checking exact label use, cyclic jumps, and classical avoidance. Running `python3 verify_cyclic_jump.py` prints `VERIFY_OK`. The arbitrary-length theorem follows from the proof above; none of the finite checks is used as an infinite certificate.

## Relationship to prior work

Nadler, *123-Avoiding Permutations with an Adjacency Constraint* (2026), proves a stronger reverse-diagonal localization result and explicitly identifies the *linear* bounded-adjacency class with constrained Hamiltonian **paths** in \(P_n^m\). The endpoint obstruction above is already an elementary consequence of that localization; this observation and the bound \(n\le3m+1\) are not asserted to be independent discoveries. The contribution here is the exact *closed-tour* feasibility threshold, constructive attainment for every allowed parameter pair, optimization over the jump bound, and four-position rigidity at the boundary.

Vella (2003) and Domagalski et al. (2021) consider pattern avoidance in rotationally defined cyclic permutations. Ehrenborg (2013/2016) considers avoiding *consecutive* patterns cyclically. Those conventions differ from classical avoidance in a distinguished linear reading with an added numerical wrap-edge constraint. OEIS A232864 similarly records cyclic consecutive-pattern avoidance, not the present extremal invariant. Searches for synonymous formulations did not establish an earlier all-parameter equivalence; the historical-priority assessment is provisional.

## Limitations

A different rotation of the same tour can contain a classical \(123\) pattern even if its distinguished reading avoids one. No assertion is made about rotation-invariant avoidance, enumeration of all admissible tours, optimal tours for other forbidden patterns, or general host graphs. The rigidity statement concerns only the four specified endpoint positions at the saturated bound; it does not classify every interior ordering. Independent mathematical assessment and complete historical-priority certification have not been performed.

## References

1. N. Nadler, *123-Avoiding Permutations with an Adjacency Constraint*, arXiv:2610.02526, first submitted 2026-10-01. https://arxiv.org/abs/2610.02526
2. A. Vella, *Pattern Avoidance in Permutations: Linear and Cyclic Orders*, Electronic Journal of Combinatorics 10 (2003), R18. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i2r18
3. R. Domagalski, J. Liang, Q. Minnich, B. E. Sagan, J. Schmidt, and A. Sietsema, *Cyclic Pattern Containment and Avoidance*, arXiv:2106.02534 (2021). https://arxiv.org/abs/2106.02534
4. R. Ehrenborg, *Cyclically Consecutive Permutation Avoidance*, arXiv:1312.2051 (2013); SIAM Journal on Discrete Mathematics 30 (2016), 1385–1390. https://arxiv.org/abs/1312.2051
5. OEIS A232864, number of permutations avoiding the *cyclic consecutive* pattern \(123\). https://oeis.org/A232864
