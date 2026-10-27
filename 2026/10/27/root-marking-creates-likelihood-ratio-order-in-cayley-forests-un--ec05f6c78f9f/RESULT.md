# Root marking creates likelihood-ratio order in Cayley forests; unrooted forests lose it at five vertices

## Finding
For each integer \(n\ge2\), consider two separate models of labeled forests on vertex set \([n]\), conditioned to have exactly \(k\) connected components. In the root-marked model, each tree has one distinguished vertex and every fully root-marked forest is equally likely. In the unrooted model, every unrooted forest is equally likely. Let \(S^{\mathrm R}_{n,k}\) and \(S^{\mathrm U}_{n,k}\) be the number of vertices in the component containing vertex \(1\), in the respective models.

**Likelihood-ratio order for root-marked forests.** For every \(n\ge2\) and \(1\le k<n\),
\[
S^{\mathrm R}_{n,k+1}\le_{\mathrm{lr}}S^{\mathrm R}_{n,k}.
\]
When \(2\le k\le n-2\), the ratio of mass functions is strictly decreasing over the common support \(1\le s\le n-k\). In particular, the conditional tagged-component sizes are nonincreasing in usual stochastic order and can be placed on one probability space in a simultaneous nonincreasing coupling.

**Sharp loss of likelihood-ratio comparability without root marks.** For every \(n\ge5\), the pair \(S^{\mathrm U}_{n,2}\), \(S^{\mathrm U}_{n,3}\) is incomparable in either likelihood-ratio direction. For \(n=3,4\), by contrast, \(S^{\mathrm U}_{n,3}\le_{\mathrm{lr}}S^{\mathrm U}_{n,2}\). Thus five vertices is the smallest order at which the two-to-three-component likelihood-ratio property fails in the unrooted ensemble.

For example, when \(n=5\), the probability vectors for sizes \(1,2,3,4\) are
\[
\Pr(S^{\mathrm U}_{5,2}=s)=\bigl(8/55,6/55,9/55,32/55\bigr),\qquad
\Pr(S^{\mathrm U}_{5,3}=s)=\bigl(1/3,4/15,2/5,0\bigr).
\]
The adjacent likelihood ratios increase from \(55/24\) to \(22/9\) between sizes \(1\) and \(2\), yet drop to zero at size \(4\).

## Assumptions and scope
All forests are simple, undirected, acyclic spanning graphs on the fixed labeled vertex set \([n]\), with exactly \(k\) connected components; isolated vertices count as components. A root-marked forest has precisely one distinguished root in every component, and is sampled **uniformly over the root-marked objects**, not by first sampling an unrooted forest uniformly and then marking roots. A specified unrooted forest receives a probability proportional to the product of its component sizes under the root-marked model; these probability measures are different.

For nonnegative integer-valued random variables \(X,Y\) supported on \([n]\), \(X\le_{\mathrm{lr}}Y\) means that for all \(1\le s<t\le n\), \(\Pr(X=s)\Pr(Y=t)\ge\Pr(X=t)\Pr(Y=s)\). This cross-product definition permits unequal supports. All probability comparisons here are unconditional within the specified forest ensemble and conditioned only on the fixed number of components.

## Proof
**1. Root-marked enumerators.** Let \(R_{n,k}\) count rooted forests with \(k\) components on \([n]\), and set \(R_{0,0}=1\) and \(R_{m,j}=0\) for inadmissible indices. By adjoining an auxiliary vertex \(0\) and assigning weight \(z\) to each edge incident with \(0\), the weighted matrix-tree theorem on this enlarged complete graph yields
\[
\sum_{k=1}^n R_{n,k}z^k=z(n+z)^{n-1},\qquad
R_{n,k}=\binom{n-1}{k-1}n^{n-k}.
\]
Indeed its reduced Laplacian is \((n+z)I_n-J_n\), whose eigenvalues are \(z\) once and \(n+z\) with multiplicity \(n-1\). Removing vertex \(0\) from a spanning tree identifies exactly the roots of the resulting forest. On a fixed \(s\)-element set there are \(s^{s-1}\) rooted trees, including one when \(s=1\). Consequently
\[
\Pr(S^{\mathrm R}_{n,k}=s)
=\frac{\binom{n-1}{s-1}s^{s-1}R_{n-s,k-1}}{R_{n,k}},
\qquad 1\le s\le n-k+1.
\]
For \(2\le k\le n-2\) and \(1\le s\le n-k\), division gives
\[
\frac{\Pr(S^{\mathrm R}_{n,k+1}=s)}{\Pr(S^{\mathrm R}_{n,k}=s)}
=\frac{kn}{(k-1)(n-k)}\left(1-\frac{k-1}{n-s}\right).
\]
This is strictly decreasing in \(s\). The upper endpoint \(s=n-k+1\), supported only by \(S^{\mathrm R}_{n,k}\), contributes a zero ratio, so all likelihood-ratio cross inequalities hold. For \(k=1\), \(S^{\mathrm R}_{n,1}=n\) surely; for \(k=n-1\), \(S^{\mathrm R}_{n,n}=1\) surely. These cases also satisfy the claimed likelihood-ratio order. The implication from likelihood-ratio order to stochastic order follows by a single-crossing argument. A simultaneous coupling is obtained by using the same uniform random variable in the inverse distribution functions for the finite sequence \(k=1,\ldots,n\).

**2. Unrooted counting and a two-component identity.** Write \(F_{n,k}\) for the number of unrooted forests on \([n]\) with \(k\) components, with \(F_{0,0}=1\) and other inadmissible indices zero. Cayley's formula gives \(t_s=s^{s-2}\) unrooted labeled trees of size \(s\), including \(t_1=1\). Decomposing at the component of vertex \(1\),
\[
F_{n,k}=\sum_{s=1}^{n-k+1}\binom{n-1}{s-1}t_sF_{n-s,k-1},\qquad
\Pr(S^{\mathrm U}_{n,k}=s)=\frac{\binom{n-1}{s-1}t_sF_{n-s,k-1}}{F_{n,k}}.
\]
Here \(F_{m,1}=m^{m-2}\) for all \(m\ge2\) and \(F_{1,1}=1\). The exact two-component count is
\[
F_{m,2}=\frac{(m-1)(m+6)}{2}\,m^{m-4}\quad(m\ge2).
\]
To prove this identity, let \(T(z)\) be the exponential generating function of rooted labeled trees, satisfying \(T=ze^T\). The unrooted-tree generating function is \(B(z)=T(z)-T(z)^2/2\), and \(F_{m,2}=m![z^m]B(z)^2/2\). Lagrange inversion supplies \([z^m]T(z)^j=\frac jm\frac{m^{m-j}}{(m-j)!}\) for \(1\le j\le m\); substituting the expansion \(B^2=T^2-T^3+T^4/4\) and simplifying proves the displayed count, including \(m=2,3\) by direct substitution.

Define \(H_m=F_{m,2}/F_{m,1}\). For \(m\ge2\),
\[
H_m=\frac{(m-1)(m+6)}{2m^2},\qquad
H_m-H_{m+1}=\frac{(m-2)(5m+3)}{2m^2(m+1)^2}.
\]
In particular \(H_2=H_3=1\), while \(H_m\) is strictly decreasing for every \(m\ge3\).

**3. Exactly where unrooted likelihood-ratio order fails.** Put \(p_s=\Pr(S^{\mathrm U}_{n,2}=s)\) and \(q_s=\Pr(S^{\mathrm U}_{n,3}=s)\). For \(1\le s\le n-2\), the counting formulas yield
\[
\frac{q_s}{p_s}=\frac{F_{n,2}}{F_{n,3}}H_{n-s}.
\]
For every \(n\ge5\), since \(n-2\ge3\), the strict inequality \(H_{n-2}>H_{n-1}\) proves \(q_2/p_2>q_1/p_1\). Hence \(S^{\mathrm U}_{n,3}\not\le_{\mathrm{lr}}S^{\mathrm U}_{n,2}\). In the other direction, \(p_{n-1}>0\) but \(q_{n-1}=0\), while \(q_1>0\); the cross-product test with sizes \(1<n-1\) proves \(S^{\mathrm U}_{n,2}\not\le_{\mathrm{lr}}S^{\mathrm U}_{n,3}\).

For \(n=4\), the common-support ratio is constant because \(H_2=H_3=1\), and then drops to zero on the larger support of \(S^{\mathrm U}_{4,2}\); hence the two-to-three comparison is decreasing in likelihood-ratio order. For \(n=3\), \(S^{\mathrm U}_{3,3}=1\) surely. Therefore \(n=5\) is minimal. Directly using the forest recurrence at \(n=5\) gives \(F_{5,2}=110\), \(F_{5,3}=45\) and the rational distributions stated above. This completes the proof.

## Verification
The companion `verify_forest_orders.py` uses exact Python integers and fractions. It independently enumerates every acyclic edge subset on up to six labeled vertices and computes both models by direct component-root-product weighting; it then compares these counts against the closed formulas. It also tests rooted likelihood-ratio inequalities through \(n=41\), the two-component count identity and consecutive differences through \(m=84\), and unrooted two-to-three-component incomparability through \(n=54\). The executable passed 391,322 exact assertions. This finite verification supplements, but does not replace, the preceding unrestricted analytic proof.

## Relationship to prior work
Pitman, *Coalescent Random Forests* (1999), already proves the root-marked count and explicit tagged-component distribution, and constructs a monotone deletion/refinement coupling across component counts (Theorem 4 and Corollary 10). Thus the enumerator and *usual stochastic monotonicity* in the root-marked model are **previously known**, not claimed as original. The new claim assessed here is the stronger **likelihood-ratio order**, together with the all-order unrooted **failure of that same strong order** at a sharp five-vertex boundary. Pitman's unrooted projection of his coupling has component-size-product bias, and does **not** sample unrooted forests uniformly.

Janson's 2011 account describes component-weighted allocation laws for rooted and unrooted labeled forests. Kassel–Kenyon–Wu (2015) study moment and inclusion properties of two-component forests. Tang–Zhang (2026) analyze fixed-component forest *edge* correlations and the dependence of *edge marginal probabilities* on component count. These statements do not directly imply or state the tagged-component likelihood-ratio comparison. An earlier source on random forest component-size asymptotics by Łuczak–Pittel is relevant but its full text was not accessible in this review. The novelty assessment is provisional pending independent literature verification, especially against general total-positivity results.

## Limitations
The theorem concerns the complete underlying graph and two precise probability measures; arbitrary graphs and heterogeneous edge weights are not covered. The unrooted result proves **likelihood-ratio incomparability**, not incomparability in ordinary stochastic order. A monotone coupling is **not** new in the root-marked case. No independent scientific audit has been performed. The unavailable complete Łuczak–Pittel text and possible implications of classical total-positivity literature create residual historical-priority uncertainty.

## References
1. Jim Pitman, *Coalescent Random Forests*, Journal of Combinatorial Theory A **85** (1999), 165–193; technical report 457, University of California, Berkeley, dated 1996-09-01. https://statistics.berkeley.edu/tech-reports/457 ; full article https://www.stat.berkeley.edu/~pitman/457.pdf . Especially Theorem 4, equations (5), (30), and Corollary 10.
2. Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510 (initial version 2011-12-02), Sections 11.6–11.7. https://arxiv.org/abs/1112.0510 .
3. Adrien Kassel, Richard Kenyon and Wei Wu, *Random two-component spanning forests*, Annales de l'Institut Henri Poincaré B **51** (2015), 1457–1464. https://doi.org/10.1214/14-AIHP625 .
4. Pengfei Tang and Zibo Zhang, *Pairwise Negative Correlation for Uniform Spanning Subgraphs of the Complete Graph*, arXiv:2603.10738, Part II, version 2026-10-09. https://arxiv.org/abs/2603.10738 .
5. Tomasz Łuczak and Boris Pittel, *Components of Random Forests*, article DOI https://doi.org/10.1017/S0963548300000067 . The accessible publisher abstract was inspected, but the full text was unavailable and no result from the full text is presumed.
