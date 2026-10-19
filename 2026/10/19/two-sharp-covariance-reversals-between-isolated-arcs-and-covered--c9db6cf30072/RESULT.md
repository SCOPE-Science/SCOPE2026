# Two sharp covariance reversals between isolated arcs and covered circumference

## Finding
Fix an integer \(n\ge5\). Independently and uniformly locate \(n\) directed arcs, each of common clockwise length \(a\in(0,1/2)\), on a circle of circumference one. Let \(C_n(a)\) be their union length. Let \(J_n(a)\) count arcs that have no overlap with any other arc (equivalently, singleton connected components of the arc-overlap graph).

**Exact covariance.** Put \(b=(1-2a)_+\) and \(c=(1-3a)_+\). Then
\[
F_n(a):=\operatorname{Cov}(J_n(a),C_n(a))
=n b^{n-1}(1-a)^n-2b^n-(n-2)c^n.
\]
There exist precisely two roots \(a_{n,-}\in(0,1/3)\) and \(a_{n,+}\in(1/3,1/2)\) of \(F_n\). Their signs, for every real \(a\) in the stated range, are
\[
F_n(a)>0\quad(0<a<a_{n,-}\text{ or }a_{n,+}<a<1/2),
\qquad F_n(a)<0\quad(a_{n,-}<a<a_{n,+}).
\]
At either root the covariance is exactly zero; these are the only interior zeros.

**Transition scales.** Let \(\lambda_*\) be the unique strictly positive solution of \(e^\lambda=1+\lambda+\lambda^2\), numerically \(\lambda_*\approx1.793282132900598\). Then
\[
\lim_{n\to\infty} n a_{n,-}=\lambda_*,
\qquad \frac{\tfrac12-a_{n,+}}{n 2^{-n-2}}\longrightarrow1.
\]
These describe two very different finite-size thresholds: an order-\(1/n\) first transition and an exponentially thin second transition near half the circumference.

## Assumptions and scope
The arcs are distinguishable only for indexing; their left endpoints are iid uniform modulo one, and each arc proceeds clockwise. Tangencies occur with probability zero and have no effect on the statements. The total measure \(C_n(a)\) is geometric union length, not a sum of arc lengths. An arc is isolated if it intersects no other arc, not merely if its endpoint is uncovered. The result is specific to fixed arc length, a fixed number of arcs, and \(n\ge5\). It does not assert an analogous law for heterogeneous lengths, random arc counts, or higher-dimensional coverage.

## Proof
Order arc starting points cyclically. Let \(S_1,\ldots,S_n\) be consecutive clockwise spacings, with indices modulo \(n\). Their vector is uniform on the standard simplex, hence Dirichlet with all parameters one. For \(0<a<1/2\), an arc is isolated exactly when both adjacent spacings exceed \(a\); therefore
\[
J_n(a)=\sum_{i=1}^n \mathbf1\{S_{i-1}>a,\ S_i>a\}.
\]
The uncovered length and covered length are
\[
U_n(a)=\sum_{j=1}^n(S_j-a)_+,\qquad C_n(a)=1-U_n(a).
\]
Shifting any fixed set of \(k\) distinct spacing coordinates by \(a\) in a uniform simplex gives probability \((1-ka)_+^{n-1}\). The first moment of one shifted coordinate on that event is \((1-ka)_+^n/n\). Thus
\[
\mathbb E J_n=n(1-2a)_+^{n-1},\quad
\mathbb E U_n=(1-a)^n,
\]
\[
\mathbb E[J_nU_n]=2(1-2a)_+^n+(n-2)(1-3a)_+^n.
\]
These identities prove the asserted exact covariance by \(\operatorname{Cov}(J_n,C_n)=-\operatorname{Cov}(J_n,U_n)\).

For the zero count below \(1/3\), divide the covariance by \((1-2a)^n>0\) and write
\[
t=\frac{1-3a}{1-2a}\in(0,1),\qquad
G_n(t)=n\frac{(2-t)^n}{(3-2t)^{n-1}}-2-(n-2)t^n.
\]
The variable \(t\) decreases continuously from one to zero as \(a\) increases from zero to \(1/3\). Differentiation gives
\[
G_n'(t)=n(n-2)t^{n-1}\bigl(Q_n(t)-1\bigr),\qquad
Q_n(t)=\frac{(2-t)^{n-1}(n-4+2t)}{(n-2)t^{n-1}(3-2t)^n}.
\]
For \(n\ge5\), \(Q_n(t)>0\). Direct differentiation gives
\[
(\log Q_n)''=(n-1)\left(\frac1{t^2}-\frac1{(2-t)^2}\right)
+\frac{4n}{(3-2t)^2}-\frac4{(n-4+2t)^2}>0
\quad(0<t<1).
\]
Indeed, when \(n\ge6\) the positive second fraction exceeds the magnitude of the negative final fraction, since \(4n/(3-2t)^2\ge4n/9>1\ge4/(n-4+2t)^2\). When \(n=5\), on \(0<t\le1/8\) the first positive term exceeds the last negative term; on \(1/8\le t<1\) the inequality \(5(1+2t)^2\ge(3-2t)^2\) makes the positive second fraction at least the magnitude of the last one. The first term is positive throughout.

Also \(Q_n(t)\to\infty\) as \(t\downarrow0\), \(Q_n(1)=1\), and \((\log Q_n)'(1)=2(n-1)/(n-2)>0\). Strict convexity of \(\log Q_n\) therefore implies that \(Q_n=1\) has exactly one solution in \((0,1)\), besides the endpoint one. Consequently \(G_n\) first strictly increases and then strictly decreases on \((0,1)\). The endpoint values satisfy
\[
G_n(0)=3n(2/3)^n-2<0,\qquad G_n(1)=0,
\]
where the strict inequality holds at \(n=5\) and persists because the sequence \(3n(2/3)^n\) decreases thereafter. Since \(G_n'(t)<0\) near one, \(G_n(t)>0\) just to its left. There is therefore exactly one zero of \(G_n\) in \((0,1)\), with the claimed covariance signs below \(1/3\).

On \(1/3\le a<1/2\), the third covariance term vanishes and its sign equals the sign of
\[
H_n(a)=\frac{n(1-a)^n}{1-2a}-2.
\]
The positive term \((1-a)^n/(1-2a)\) strictly decreases until \(a=(n-2)/(2(n-1))>1/3\), and then strictly increases to infinity. Since \(H_n(1/3)=3n(2/3)^n-2<0\), it crosses zero exactly once above \(1/3\), proving the complete two-switch sign pattern.

For the first scale set \(a=\lambda/n\). Elementary logarithmic expansion, uniform on compact subsets of \(\lambda>0\), yields
\[
F_n(\lambda/n)\longrightarrow
2e^{-3\lambda}(1+\lambda+\lambda^2-e^\lambda).
\]
The expression in parentheses is positive for sufficiently small positive \(\lambda\), crosses zero once at \(\lambda_*\), and is negative thereafter. To verify uniqueness, its second derivative is \(2-e^\lambda\), decreasing through zero exactly once, so its first derivative and then the function each cross zero exactly once after the origin. The already proved uniqueness of \(a_{n,-}\) gives \(na_{n,-}\to\lambda_*\).

For the second scale put \(\varepsilon_n=1-2a_{n,+}\). The zero equation becomes
\[
\varepsilon_n=\frac{n}{2^{n+1}}(1+\varepsilon_n)^n.
\]
For all sufficiently large \(n\), evaluating the two sides at \(\varepsilon=n/2^{n+1}\) and twice that value brackets the small solution. Hence \(\varepsilon_n=O(n2^{-n})\) and substitution into the equation gives \(\varepsilon_n\sim n2^{-n-1}\), as claimed.

## Verification
The companion `verify.py` checks exact rational covariance identities over multiple sizes and thresholds, compares with independent uniform-simplex lattice quadrature, and locates the predicted transition roots numerically with high-precision decimal arithmetic. These finite checks are supplementary; the infinite-range claims follow from the preceding simplex calculation and strict-convexity argument.

Selected roots are \((a_{5,-},a_{5,+})\approx(0.3255321282,0.4125462668)\), \((a_{10,-},a_{10,+})\approx(0.1632241910,0.4974301716)\), and \((a_{20,-},a_{20,+})\approx(0.0852596699,0.4999952307)\).

## Relationship to prior work
Moriarty, Marchesi, and Metcalfe (2007) consider the same fixed-length circular coverage model, but bound the distribution of the *number of uncovered gaps*, rather than its covariance with the number of isolated arcs. Huffer (1988) examines joint moments of uncovered length and uncovered-gap count for random arcs. In the present notation the gap count is \(B=\sum_i\mathbf1\{S_i>a\}\), whereas \(J=\sum_i\mathbf1\{S_{i-1}>a,S_i>a\}\) depends on adjacency; at fixed \(B\) it can vary. Thus the above mixed moment and its two sign transitions are not consequences of the stated gap-count marginals or the joint law of \((B,U)\) alone. Classical coverage literature supplies the geometric motivation and simplex framework, not an identified statement of this phase diagram. Historical priority remains subject to further independent verification, particularly because Huffer's full paper was not available for material comparison.

## Limitations
The proof establishes finite-\(n\) covariance and first-order positions of two thresholds, not independence at covariance zeros and not the joint distribution of isolation and coverage. There is no claim of independence, generalization beyond the given regime, or novelty certification. Although older relevant abstracts and bibliographic records were accessible, one high-relevance complete historical article could not be inspected; implicit earlier coverage remains possible.

## References
- J. Moriarty, J. R. Marchesi, and A. Metcalfe, *Bounds on the distribution of the number of gaps when circles and lines are covered by fragments*, BMC Bioinformatics 8:70 (2007), first publicly dated 2007-03-02. https://pmc.ncbi.nlm.nih.gov/articles/PMC1821341/.
- F. W. Huffer, *Some results concerning random arcs on the circle*, Journal of Applied Probability 25 (1988), 833–838, doi:10.1017/S0021900200041644; Stanford preprint report SOL ONR 392 (June 1987). https://statistics.stanford.edu/technical-reports/some-results-concerning-random-arcs-circle.
- A. F. Siegel, *Random arcs on the circle*, Journal of Applied Probability 15 (1978), 774–789, doi:10.2307/3213433 (bibliographic metadata and abstract).
- L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability 21 (1984), 558–566 (bibliographic metadata and abstract).
