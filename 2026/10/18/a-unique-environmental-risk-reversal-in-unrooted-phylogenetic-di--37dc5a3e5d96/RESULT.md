# A unique environmental-risk reversal in unrooted phylogenetic diversity

## Finding
Let \(T\) be any finite unrooted phylogenetic tree with \(n\ge3\) taxon-labelled leaves, no unlabelled degree-two vertices, and strictly positive edge lengths \(\ell_e\). Each leaf survives independently with the same probability \(p\in(0,1)\). Define \(U_T(p)\) as the expected length of the minimal subtree connecting the surviving leaves, with diversity zero if fewer than two survive.

**Theorem (universal single-inflection and sharp size bound).** There is exactly one \(p_T\in(0,1)\) such that
\[
U_T''(p)>0\quad(0<p<p_T),\qquad U_T''(p_T)=0,\qquad U_T''(p)<0\quad(p_T<p<1).
\]
Moreover,
\[
0<p_T\le \frac{2}{n},
\]
with equality if and only if \(T\) is a star. For any non-star tree, \(p_T<2/n\). The theorem holds without binary, ultrametric, integer-length, or equal-edge-length assumptions.

**Consequence for common environmental variability.** Suppose a random environmental state \(P\in(0,1)\) is drawn, after which the leaves survive conditionally independently with probability \(P\). Write \(\bar p=\mathbb E[P]\). If \(P\) is nonconstant and supported inside \((0,p_T)\), then
\[
\mathbb E[U_T(P)]>U_T(\bar p).
\]
If \(P\) is nonconstant and supported inside \((p_T,1)\), the inequality is reversed. The right-hand side is the expected unrooted diversity under independent survival with the same individual-leaf marginal \(\bar p\). For distributions straddling \(p_T\), no universal inequality is asserted.

In contrast, rooted phylogenetic diversity (the minimal subtree connecting surviving leaves **and the designated root**) has a concave mean as a function of common survival probability. Its expected value cannot increase under a mean-preserving environmental fluctuation; the decrease is strict when some positive-length rooted edge subtends at least two leaves and \(P\) is nonconstant.

## Assumptions and scope
The tree is finite, connected, acyclic, and has exactly \(n\ge3\) labelled taxa at its leaves. A strictly positive real length is assigned to every edge; internal vertices may have degree greater than three. Removing edge \(e\) partitions the taxon set into sizes \(a_e,b_e\in\{1,\dots,n-1\}\) with \(a_e+b_e=n\). Conditional independence applies **after** conditioning on \(P\), not unconditionally. The result concerns the expected unrooted Faith-type phylogenetic diversity of a surviving taxon subset, not its realised distribution or a phylogenetic tree sampled anew. At \(p=0\) and \(p=1\), the strict second-derivative statements are replaced by their one-sided limits.

## Proof
**1. Edge-inclusion identity.** An edge belongs to the minimal subtree joining the surviving leaves exactly when at least one survivor lies on **each** side of its split. Let \(q=1-p\). Independence therefore gives
\[
U_T(p)=\sum_{e\in E(T)}\ell_e\left(1-q^{a_e}-q^{b_e}+q^n\right).
\tag{1}
\]
This is the classical unrooted expected-diversity edge formula, not claimed to be new. Differentiating twice with respect to \(p\), with \(L=\sum_e\ell_e\), yields
\[
U_T''(p)=n(n-1)Lq^{n-2}-\sum_e\ell_e\left[a_e(a_e-1)q^{a_e-2}+b_e(b_e-1)q^{b_e-2}\right].
\tag{2}
\]
Terms with coefficient zero are interpreted as zero, so no negative-power ambiguity occurs in (2).

**2. Exactly one curvature reversal.** On \(0<q<1\), divide (2) by the positive \(q^{n-2}\). The resulting function is
\[
H(q)=n(n-1)L-\sum_e\ell_e\left[a_e(a_e-1)q^{-b_e}+b_e(b_e-1)q^{-a_e}\right].
\tag{3}
\]
Every edge has at least one split side containing two taxa, because \(n\ge3\). Therefore
\[
H'(q)=\sum_e\ell_e\left[a_e(a_e-1)b_eq^{-b_e-1}+b_e(b_e-1)a_eq^{-a_e-1}\right]>0.
\]
As \(q\downarrow0\), at least one positive-coefficient negative power diverges, so \(H(q)\to-\infty\). At \(q=1\), use \(n(n-1)-a(a-1)-b(b-1)=2ab\) to obtain
\[
H(1)=2\sum_e\ell_e a_eb_e>0.
\]
Strict monotonicity and continuity give exactly one zero \(q_T\in(0,1)\). Since \(q=1-p\), define \(p_T=1-q_T\); the three asserted curvature signs follow with the stated orientation.

**3. Sharp upper bound.** Put \(q_0=(n-2)/n\). For each split \(a+b=n\), Bernoulli's inequality applied to \(q_0^{-1}=1+2/(n-2)\) gives
\[
a(a-1)q_0^{-b}+b(b-1)q_0^{-a}
\ge a(a-1)\left(1+\frac{2b}{n-2}\right)+b(b-1)\left(1+\frac{2a}{n-2}\right)=n(n-1).
\]
For a pendant split \((a,b)=(1,n-1)\), equality holds. If both sides have at least two leaves, strict Bernoulli inequality holds because the positive coefficients multiply powers with exponents at least two. Summing with positive edge lengths gives \(H(q_0)\le0\), strictly if an edge has at least two leaves on each side. As \(H\) increases and \(H(q_T)=0\), it follows that \(q_T\ge q_0\), and hence \(p_T\le2/n\). Every edge of a star makes a pendant split, proving equality for stars. In a phylogenetic tree without degree-two unlabelled vertices, every non-star has an internal edge with at least two labelled leaves on either side, proving strict inequality.

**4. Environmental and rooted interpretations.** Strict convexity/concavity of \(U_T\) on the two intervals, combined with strict Jensen's inequality, proves the two environmental comparisons. Conditionally independent leaf survival with random common \(P\) preserves each marginal survival probability \(\bar p\) and induces positive pairwise survival covariance \(\operatorname{Var}(P)\). For rooted diversity let \(k_e\ge1\) be the number of descendants of rooted edge \(e\). Its expected value is
\[
R_T(p)=\sum_e\ell_e\left(1-(1-p)^{k_e}\right),\qquad
R_T''(p)=-\sum_e\ell_e k_e(k_e-1)(1-p)^{k_e-2}\le0.
\]
Strictness occurs as stated. This completes the proof.

**Exact illustration.** For a four-tip quartet whose four pendant edges have length \(1\) and whose unique internal edge has length \(2\), (1) becomes
\[
U_T(p)=6-4q-4q^2-4q^3+6q^4,\qquad q=1-p.
\]
Thus \(U_T''(p)=72q^2-24q-8\) and
\[
p_T=\frac{5-\sqrt5}{6}<\frac12.
\]
For a four-tip star of arbitrary positive pendant lengths, \(p_T=1/2\). These examples show that internal structure can move the reversal but cannot move it beyond the universal bound.

## Verification
The included standalone program `verify_pd_curvature.py` uses Python standard-library exact rational arithmetic. It independently enumerates **every surviving-leaf subset** for six weighted stars (three through eight tips), one weighted four-tip quartet, and one weighted five-tip binary tree, then reconstructs the full expected-diversity polynomial without calling (1). For all eight trees it checks coefficientwise identity with (1), endpoint curvature, the bound at \(p=2/n\), and two exact two-environment Jensen examples. It additionally verifies the exact quartet polynomial and two rational curvature values. Run `python3 verify_pd_curvature.py` from the package directory. Finite checks are reproducibility aids and do not establish the universal theorem; steps 1–4 above do so analytically.

## Relationship to prior work
Faller, Pardi, and Steel (2008), §5, equations (12)–(14), establish the general edge-inclusion and expectation formula for unrooted phylogenetic diversity under independent extinction, and study its distribution and asymptotic normality. The present claim **does not** claim a new expectation formula. Its contribution is the unique global inflection point for **every** positive-length unrooted tree, the sharp \(2/n\) bound and equality case, and the resulting sign reversal under a common stochastic environment. Their §5 does not state these curvature or environmental-comparison results.

Nipperess et al. (2013) derive mean/variance under fixed-size rarefaction, a different sampling dependence; O'Dwyer, Kembel, and Green (2012) treat sampling-based phylogenetic diversity in ecological communities. Faller and Steel (2012) establish a comparison for **root-anchored** diversity under a particular trait-dependent extinction model: their formula involves descendant clades of a designated root, and cannot imply the reversed sign possible for unrooted diversity under a shared environmental variable. Steel, Mimoto, and Mooers (2007) concern individual-taxon marginal conservation indices rather than curvature of total expected unrooted diversity.

Prior research on pairwise conservation interactions in unrooted trees studies discrete second differences with respect to protecting two named taxa. That result does not yield uniqueness of the **sum of all mixed derivatives** along the diagonal survival-probability curve or the \(2/n\) bound. Shared use of the classical edge formula is acknowledged.

## Limitations
The model assumes identical taxon survival probability conditional on a single common environmental variable. Heterogeneous conditional probabilities, correlated extinctions beyond this mixture, taxon-specific responses to environment, and alternative diversity metrics are not covered. The reversal is about **expected unrooted phylogenetic diversity**, not extinction risk of any particular species, and does not show an environmental fluctuation always helps or always hurts when its support crosses \(p_T\). The known general expectation formula makes the result a structural consequence of established theory, not an independent new model. No claim of historical uniqueness beyond the literature and research records inspected is made; equivalent formulations could remain unindexed.

## References
1. Faller, B., Pardi, F., and Steel, M. (2008), *Distribution of phylogenetic diversity under random extinction*, Journal of Theoretical Biology **251**, 286–296, DOI 10.1016/j.jtbi.2007.11.034, preprint arXiv:0708.0425 (first posted 2007-08-02). Especially §5, equations (12)–(14).
2. Steel, M., Mimoto, A., and Mooers, A. Ø. (2007), *Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity*, Evolutionary Bioinformatics **3**, 237–244, DOI 10.1177/117693430700300024.
3. Faller, B., and Steel, M. (2012), *Trait-Dependent Extinction Leads to Greater Expected Biodiversity Loss*, SIAM Journal on Discrete Mathematics **26**, 472–481, DOI 10.1137/090776743; preprint arXiv:0911.3441.
4. Nipperess, D. A., and Matsen, F. A. IV (2013), *The mean and variance of phylogenetic diversity under rarefaction*, Methods in Ecology and Evolution, DOI 10.1111/2041-210X.12042.
5. O'Dwyer, J. P., Kembel, S. W., and Green, J. L. (2012), *Phylogenetic Diversity Theory Sheds Light on the Structure of Microbial Communities*, PLOS Computational Biology **8**, e1002832, DOI 10.1371/journal.pcbi.1002832.
