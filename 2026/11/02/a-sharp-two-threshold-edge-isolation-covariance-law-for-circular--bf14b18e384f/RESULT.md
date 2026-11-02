# A sharp two-threshold edge–isolation covariance law for circular random geometric graphs

## Finding

Let \(n\ge2\) points be sampled independently and uniformly on the unit circle, with an edge joining each pair whose shorter circular distance is at most \(r\in(0,1/2)\). Write \(I\) for the number of isolated vertices and \(E\) for the number of edges. Define
\[
L=1-2r,\qquad q=1-\left(\frac{\max\{L-r,0\}}{L}\right)^2.
\]
For every \(n\ge2\) and \(0<r<1/2\),
\[
\boxed{\operatorname{Cov}(I,E)=n(n-1)L^{n-1}\left[-2r+\frac{n-2}{2}(q-2r)\right].}
\]
For \(2\le n\le5\), this covariance is strictly negative at every admissible radius. For \(n\ge6\) it has exactly two zeros
\[
\boxed{r_-(n)=\frac{8}{3n+10+\sqrt{(3n+10)^2-128n}}},\qquad
\boxed{r_+(n)=\frac12-\frac1n}.
\]
It is strictly positive exactly when \(r_-(n)<r<r_+(n)\), and strictly negative outside the closed interval, within \((0,1/2)\). At \(n=6\), the zeros are \(1/4\) and \(1/3\); at every \(n\ge7\), \(0<r_-<1/3<r_+<1/2\). As \(n\to\infty\), \(nr_-\to4/3\) and \(r_+=1/2-1/n\). For each fixed \(c>0\),
\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}(I,E)\bigg|_{r=c/n}
=e^{-2c}\left(\frac{3c^2}{2}-2c\right).
\]
In contrast, an Erdős–Rényi random graph with \(n\) vertices and the same edge marginal probability \(p=2r\) has \(\operatorname{Cov}(I,E)=-n(n-1)p(1-p)^{n-1}<0\). Thus the positive-dependence interval is a spatial effect.

## Assumptions and scope

The probability space is \(n\) iid uniform points in \(\mathbb R/\mathbb Z\), independently chosen with respect to normalized arclength; the model is a binomial circular random geometric graph, not a Poisson process and not a line segment with boundary. Distance is \(d(x,y)=\min\{|x-y|,1-|x-y|\}\). Equality at the distance threshold has probability zero. The statistics count labeled vertices and unordered edges of this graph. All results hold for every integer \(n\ge2\) and real radius strictly between zero and one-half. The asymptotic assertion at \(r=c/n\) requires \(n>2c\).

## Proof

Fix a distinguished vertex, say vertex 1. Its isolation event \(A_1\) occurs precisely when every other point lies outside its radius-\(r\) neighborhood, an arc of length \(2r\). Hence \(\Pr(A_1)=L^{n-1}\). Conditionally on \(A_1\) and the position of vertex 1, the other \(n-1\) points remain independent and uniformly distributed on the complementary contiguous arc of length \(L=1-2r\).

There are two types of edges when computing \(\mathbb E[E\mid A_1]\). All \(n-1\) edges incident to vertex 1 are absent. For two other points uniformly sampled on an arc of length \(L\), let \(d\) denote their ordinary linear separation along that arc. The alternate circular route has length at least \(1-L=2r>r\), so the two points are adjacent exactly when \(d\le r\). The area in a square of side \(L\) with \(d\le r\) is \(L^2-\max\{L-r,0\}^2\). Dividing by \(L^2\) gives the conditional nonincident-edge probability \(q\). Thus
\[
\mathbb E[E\mid A_1]=\binom{n-1}{2}q,
\qquad \mathbb E[E]=\binom n2 (2r).
\]
Exchangeability now gives
\[
\operatorname{Cov}(I,E)
=n\operatorname{Cov}(\mathbf1_{A_1},E)
=nL^{n-1}\left[\binom{n-1}{2}q-\binom n2(2r)\right],
\]
which is exactly the boxed covariance formula. No independence between edges is assumed.

For \(0<r\le1/3\), \(L\ge r\) and algebra gives
\[
-2r+\frac{n-2}{2}(q-2r)
=\frac{r\,P_n(r)}{2(1-2r)^2},\qquad
P_n(r)=-4+(3n+10)r-8nr^2.
\]
For \(1/3\le r<1/2\), \(L\le r\) and \(q=1\), so the same bracket is \((n-2)/2-nr\). Since the prefactor \(n(n-1)L^{n-1}\) is always positive, signs reduce to these functions. When \(n=2\), \(P_2(r)=-4(1-2r)^2<0\). For \(n=3,4,5\), the discriminants of \(P_n\) are respectively \(-23,-28,-15\), and their leading coefficients and constant terms are negative. On the second radius regime, \((n-2)/2-nr\le(n-6)/6<0\) for \(n<6\). This proves the no-positive-regime assertion.

For \(n=6\), the roots of \(P_6\) are \(1/4\) and \(1/3\), and the second regime bracket equals \(2-6r\). Hence the strictly positive interval is \((1/4,1/3)\). For every \(n\ge7\), \(P_n(0)=-4\) and \(P_n(1/3)=(n-6)/9>0\). The downward-opening quadratic has exactly one root in \((0,1/3)\), namely the rationalized expression \(r_-(n)\) in the statement. Its other root is greater than \(1/3\) and is outside the regime where \(P_n\) applies. In the second regime the bracket is strictly decreasing with its unique zero at \(r_+(n)=1/2-1/n>1/3\); the two formulas agree at \(r=1/3\). This establishes exactly two zeros and the full sign classification.

For the lower root, \(nr_-=8n/(3n+10+\sqrt{(3n+10)^2-128n})\to4/3\). At \(r=c/n\), one has \(L^{n-1}\to e^{-2c}\) and, using \(r/L\to0\),
\[
q-2r=\frac{2r}{L}-\frac{r^2}{L^2}-2r=3r^2+O(r^3).
\]
Substitution into the exact covariance formula proves the claimed sparse-limit profile. Finally, for an independent-edge \(G(n,p)\), conditioning on isolation of vertex 1 fixes \(n-1\) incident edges to zero but leaves all other edges independent with probability \(p\), giving \(\operatorname{Cov}(I,E)=-n(n-1)p(1-p)^{n-1}\).

## Verification

The standalone program `verify.py` uses exact rational arithmetic for geometric two-point integration, both piecewise covariance formulas, finite-size sign regimes, and grid-model enumerations. It also checks the displayed sparse limit numerically; the limit itself follows analytically from the displayed expansion. Reproduce with `python3 verify.py` from a directory containing that file. The executed version completed successfully with output `VERIFY_OK 55076 checks`. Finite verification is supplemental, not a replacement for the unrestricted proof above.

## Relationship to prior work

Penrose's 2013 treatment of soft random geometric graph connectivity centers on isolated vertices and connectivity, whereas Chatterjee and Harel's 2014 paper addresses large deviations for edge counts in random geometric graphs. Zhao, Yagan and Gligor's 2015 work concerns isolation and connectivity thresholds in one-dimensional geometric graphs, while Wilsher, Dettmann and Ganesh's 2020 work studies isolated vertices in a one-dimensional soft model. These works establish relevant spatial random-graph context, but the inspected material does not establish the explicit finite-sample circular edge–isolation covariance together with its sharp two-root sign classification. The exact formula is derived directly rather than inferred from absence of a search match.

## Limitations

The results concern a fixed number of uniform points on a circle with a hard distance cutoff. They do not assert corresponding sign transitions on a segment, higher-dimensional torus, Poissonized point process, or nonuniform location distribution. Older general random geometric graph moment formulas could imply portions of the covariance identity; historical priority for the combined sharp sign theorem requires further independent literature assessment. A potentially relevant 2015 article was not available for complete full-text inspection; its available description concerns different statistics and geometry. The verification code cannot certify novelty or substitute for independent scientific review.

## References

1. Mathew D. Penrose, *Connectivity of soft random geometric graphs*, arXiv:1311.3897 (first posted 2013-11-15), https://arxiv.org/abs/1311.3897.
2. Sourav Chatterjee and Matan Harel, *Localization in random geometric graphs with too many edges*, arXiv:1401.7577 (first posted 2014-01-29), https://arxiv.org/abs/1401.7577.
3. Jun Zhao, Osman Yagan and Virgil Gligor, *A curious gap in one-dimensional geometric random graphs between connectivity and the absence of isolated node*, arXiv:1502.00404 (2015), https://arxiv.org/abs/1502.00404.
4. Michael Wilsher, Carl Dettmann and Ayalvadi Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs*, arXiv:2007.06301 (2020), https://arxiv.org/abs/2007.06301.
