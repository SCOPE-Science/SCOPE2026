# Arbitrarily many variance peaks under homogeneous phylogenetic extinction

## Finding
For every integer \(m\ge 1\) there exists a finite rooted, fully binary phylogenetic tree \(T\), with a positive length on **every** edge, for which the variance \(V_T(p)\) of rooted phylogenetic diversity after independent, identically distributed survival of each leaf with probability \(p\) has at least \(m\) **distinct strict local maxima** in \(0<p<1\). Thus there is no universal bound on the number of risk-variance peaks, even though the expected rooted diversity is nondecreasing and concave in \(p\).

In particular, an explicit fully binary, positive-length tree with 100,514 leaves has at least three distinct strict interior variance peaks. The proof of arbitrarily many peaks is analytic; the large finite example is additionally certified by outward-rounded numerical interval calculations and a uniform perturbation bound.

## Assumptions and scope
Let \(T\) be a finite rooted binary tree with labeled leaves and with strictly positive edge lengths \(\ell_e\). Each leaf survives independently with the same probability \(p\in(0,1)\). If \(S_p\) is the surviving leaf set, define rooted phylogenetic diversity by
\[
X_T(p)=\sum_{e\in E(T)}\ell_e\,\mathbf 1\{S_p\text{ contains a leaf below }e\}.
\]
The rooted origin is fixed; an empty survivor set has diversity zero. Set \(V_T(p)=\operatorname{Var}(X_T(p))\). No claim concerns unrooted diversity, correlated survival, a fixed-size rarefaction sample, ultrametric branch lengths, or typical phylogenetic trees.

## Proof
**1. Independent clade skeleton.** Choose \(r\) disjoint clades containing \(k_j\ge2\) leaves and assign their incoming stem edges positive lengths \(L_j\); temporarily let every other edge have length zero. A surviving tip from clade \(j\) activates its stem, giving a Bernoulli variable \(B_j\) of probability \(q_j(p)=1-(1-p)^{k_j}\). The variables are independent because the clades are disjoint. Therefore the skeleton's variance and its derivative are
\[
V_0(p)=\sum_{j=1}^r L_j^2 f_{k_j}(p),\qquad f_k(p)=(1-p)^k-(1-p)^{2k},
\]
\[
V'_0(p)=\sum_{j=1}^r L_j^2 k(1-p)^{k-1}\bigl(2(1-p)^k-1\bigr).
\]
At \(p_k^+=1/(4k)\), Bernoulli's inequality gives \((1-p_k^+)^k\ge3/4\), so \(f'_k(p_k^+)>0\). At \(p_k^-=1/k\), the inequality \((1-1/k)^k<e^{-1}<1/2\) gives \(f'_k(p_k^-)<0\). Thus one isolated clade has a positive-to-negative derivative interval.

**2. Add arbitrarily finer risk scales.** Suppose finitely many distinct scale intervals have strict positive derivative at their left endpoints and strict negative derivative at their right endpoints. Introduce a new disjoint clade of size \(k\), with stem length \(L_k=k^{-1/4}\), choosing \(k\) sufficiently large. Its derivative contribution equals \(k^{-1/2}f'_k(p)\). At \(p=c/k\), \(c\in\{1/4,1\}\), we have
\[
\lim_{k\to\infty}\frac{k^{-1/2}f'_k(c/k)}{\sqrt{k}}
=e^{-c}(2e^{-c}-1),
\]
which is positive for \(c=1/4\) and negative for \(c=1\). The derivatives of the previously chosen finite sum remain bounded as \(p\to0\), so for large \(k\) the new term imposes the required opposite signs at \(1/(4k)\) and \(1/k\). Meanwhile at every previously fixed endpoint \(p>0\), the new derivative tends to zero exponentially fast with \(k\); hence all old signs remain strict. Choose \(k\) large enough that the new interval lies strictly to the left of every old interval. Starting with one clade, induction produces as many pairwise disjoint positive-to-negative derivative intervals as desired.

A polynomial with \(V'_0(a)>0\) and \(V'_0(b)<0\) must attain a maximum inside \((a,b)\); since \(V_0\) is a nonconstant polynomial, at least one such interior maximum is strict. The disjoint intervals ensure distinct maxima.

**3. Enforce the binary, strictly positive tree constraints.** Join the disjoint clades in any rooted binary arrangement and refine each clade to a rooted binary subtree. Keep the specified incoming stem lengths; assign a common small \(\varepsilon>0\) to all other edges. For each fixed \(p\), all moments of \(X_T(p)\), and their \(p\)-derivatives, are polynomials in \(p\) and the finitely many edge lengths. Consequently the finite collection of strict derivative signs persists for sufficiently small \(\varepsilon>0\). This yields a strictly positive-length, rooted fully binary tree with the required \(m\) distinct strict maxima.

**4. Explicit three-peak certificate.** Take disjoint clades with numbers of tips \((2,512,100000)\) and incoming stem lengths \((1,1/4,1/16)\). Refine them to full rooted binary trees; connect their roots in any rooted binary arrangement, preserving the three designated incoming stems. Give every other edge the length \(\varepsilon=10^{-18}\). The total number of tips is \(n=100514\), the sum of the long stem lengths is \(L=21/16\), and the total length of the remaining \(2n-5\) edges is \(\eta=(2n-5)10^{-18}\).

At the endpoints of each interval \([1/(4k),1/k]\) for \(k=2,512,100000\), outward-rounded interval evaluation of the **exact** skeleton derivative yields positive left signs and negative right signs. Its smallest signed magnitude is at least \(1/2\). The effect of assigning positive lengths to the other edges is bounded uniformly as follows. Write \(Y=X+Z\), where \(X\) is the skeleton diversity, \(0\le X\le L\), and \(Z\) is the contribution from the newly positive edges, \(0\le Z\le\eta\). For any statistic \(g\) of \(n\) independent survival indicators whose range has width at most \(R\), the independent-Bernoulli derivative identity implies
\[
\left|\frac{d}{dp}\mathbb E_p[g]\right|\le nR.
\]
Apply this to \(Y^2-X^2\), whose range has width at most \(2L\eta+\eta^2\), and to the difference of the squared means. Using \(\left|\mathbb E'_p X\right|\le nL\) and \(\left|\mathbb E'_p Z\right|\le n\eta\) gives
\[
\sup_{0\le p\le1}\left|V'_Y(p)-V'_X(p)\right|
\le6nL\eta+3n\eta^2<1.60\times10^{-7}<1/2.
\]
Thus all six derivative signs survive, proving at least three strict local maxima in disjoint intervals of the genuinely positive-length binary tree.

For comparison, the expected rooted diversity is
\[
\mathbb E_p X_T=\sum_e\ell_e\bigl(1-(1-p)^{d_e}\bigr),
\]
where \(d_e\) counts descendant tips of edge \(e\). Each summand is nondecreasing and concave, so these properties hold for every such tree's expected diversity. The expectation identity is classical and is not a new contribution.

## Verification
The attached standard-library Python file `verify.py` checks the independent-clade variance identity by exact exhaustive enumeration on a five-leaf skeleton, evaluates the six explicit derivative witnesses using 48-digit outward-rounded decimal intervals, and checks the global positive-edge perturbation bound with exact rational arithmetic. Execute `python3 verify.py`. The unrestricted-many-peaks induction is proved above and is not inferred from those finite calculations.

## Relationship to prior work
Faller, Pardi, and Steel (2007/2008) treat the distribution of rooted future phylogenetic diversity under independent or heterogeneous extinction and give an edge-based variance formula. Their Section 2 supplies the appropriate starting framework, but the present claim concerns **arbitrarily many interior maxima of variance as a single common leaf-survival probability varies**, with positive edge lengths and binary topology. Nipperess and Matsen (2013) provide mean/variance formulas for **fixed-size rarefaction**, a distinct probability model. These methods cover the relevant moments but neither inspected text states or implies the unbounded-modal-complexity construction by a quoted result. The novelty comparison is not exhaustive and might miss an equivalent theorem phrased as multi-scale Bernoulli variance or extinction-risk nonunimodality.

## Limitations
Existence is obtained with separated clade-size scales and possibly very short internal edges; the construction is not asserted to be ultrametric, robust under large branch-length perturbations, or representative of empirical phylogenies. The explicit 100,514-tip example certifies three peaks but does not claim they are the only peaks. The theorem concerns total **rooted diversity variance** under homogeneous independent leaf survival, not mean conservation benefit, and does not imply a practical recommendation for selecting reserves or extinction probabilities.

## References
1. Faller, B., Pardi, F., and Steel, M. (2008), "Distribution of phylogenetic diversity under random extinction", *Journal of Theoretical Biology* 251, 286–296; first public preprint 2007-08-02, arXiv:0708.0425, https://arxiv.org/abs/0708.0425; DOI 10.1016/j.jtbi.2007.11.034.
2. Nipperess, D. A., and Matsen, F. A. IV (2013), "The mean and variance of phylogenetic diversity under rarefaction", *Methods in Ecology and Evolution* 4, 566–572, DOI 10.1111/2041-210X.12042.
3. Steel, M., Wicke, K., and Mooers, A. (2026), "Properties of biodiversity indices that incorporate future extinction risk", arXiv:2602.16059 (contextual comparison; not used for the proof).
