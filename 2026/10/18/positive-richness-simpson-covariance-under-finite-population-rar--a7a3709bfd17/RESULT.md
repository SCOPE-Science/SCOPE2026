# Positive richness–Simpson covariance under finite-population rarefaction

## Finding

Uniform rarefaction from a finite, completely enumerated community creates a universal, quantitatively bounded positive covariance between observed species richness and unbiased sample Gini–Simpson diversity. This extends the covariance question from independently drawn categorical observations to fixed-size sampling *without replacement*, with an exact equality classification at census saturation.

**Theorem.** Let \(N\ge2\) distinguishable individuals form \(s\ge1\) species with positive integer abundances \(a_1,\ldots,a_s\) summing to \(N\). For each \(m\in\{2,\ldots,N\}\), select uniformly one \(m\)-element subset. Write \(K_m\) for the number of represented species and
\[
\widehat G_m=\binom m2^{-1}\sum_{\{u,v\}\subseteq\mathrm{sample}}\mathbf1\{u\text{ and }v\text{ belong to different species}\}.
\]
Set \(Q=\sum_i a_i^2\), \(S=Q-N\), \(t=Q/N\), and \(F_m=(N)_{\underline m}=N(N-1)\cdots(N-m+1)\). Define
\[
w_i=\begin{cases}(N-a_i-2)_{\underline{m-2}},&N-a_i\ge m,\\0,&N-a_i<m.\end{cases}
\]
The convention in the second case applies also when \(m=2\). Then
\[
\boxed{\operatorname{Cov}(K_m,\widehat G_m)=
\frac{\sum_i a_iw_i\bigl[S(2N-a_i-1)-N(N-1)(a_i-1)\bigr]}{F_mN(N-1)}.}
\tag{1}
\]
More strongly, with \(B=S+N(N-1)>0\),
\[
\boxed{\operatorname{Cov}(K_m,\widehat G_m)
=\frac{(t-1)(N-t)}{F_m(N-1)}\sum_i a_iw_i
+\frac{B}{F_mN^2(N-1)}\sum_{i<j}a_ia_j(a_i-a_j)(w_j-w_i)\ge0,}
\tag{2}
\]
where the abundances are indexed in nonincreasing order \(a_1\ge\cdots\ge a_s\). Consequently the first term of (2) is a sharp explicit lower bound. The correction is exactly zero for equally abundant species, and the bound is then attained.

The covariance is **strictly positive exactly when** the community has at least two species, at least one species with abundance greater than one, and \(m\le N-\min_i a_i\). In every other case it is zero. These conditions include all boundary populations and all sampling depths from two through the complete census.

## Assumptions and scope

All individuals are labeled, and the sampling law is uniform over size-\(m\) subsets without replacement; the fixed abundance profile is regarded as known. Species identification is perfect. The function \(\widehat G_m\) is the pairwise-difference proportion, an unbiased estimator of the **finite-census** Gini–Simpson index
\[
G_{\rm census}=1-\frac{\sum_i a_i(a_i-1)}{N(N-1)}=1-\frac S{N(N-1)}.
\]
This finite-population index differs from the with-replacement index \(1-\sum_i(a_i/N)^2\); the distinction is essential to the theorem. A falling factorial is zero when its nonnegative length exceeds the available number of factors. In the definition of \(w_i\), the feasibility condition \(N-a_i\ge m\) takes priority.

## Proof

Fix one species \(i\), and let \(I_i\) be the indicator that it appears in the random sample. Put \(q_i=\Pr(I_i=0)=\binom{N-a_i}{m}/\binom Nm\). Let \(D\) denote the finite-census pairwise-difference probability and \(D_{-i}\) the corresponding probability among the \(N-a_i\) individuals outside species \(i\), if a sample of size \(m\) excluding it is feasible. By exchangeability of pairs within uniformly selected subsets,
\[
\mathbb E\widehat G_m=D,
\qquad
\mathbb E(\widehat G_m\mid I_i=0)=D_{-i}.
\]
Since \(I_i=1-\mathbf1_{\{I_i=0\}}\), direct conditioning yields
\[
\operatorname{Cov}(I_i,\widehat G_m)=q_i(D-D_{-i}).
\tag{3}
\]
If \(q_i=0\), this covariance is zero regardless of whether \(D_{-i}\) is defined. Otherwise \(N-a_i\ge m\ge2\), and
\[
D=1-\frac{S}{N(N-1)},\qquad
D_{-i}=1-\frac{S-a_i(a_i-1)}{(N-a_i)(N-a_i-1)}.
\]
Substitution into (3), cancellation of the first two factors of \((N-a_i)_{\underline m}\), and summation of \(K_m=\sum_iI_i\) prove (1), including cases in which species \(i\) cannot be absent.

For the nonnegative decomposition, note \(S=N(t-1)\) and establish by expansion
\[
S(2N-a_i-1)-N(N-1)(a_i-1)
=N(t-1)(N-t)+B(t-a_i).
\tag{4}
\]
Write \(A=\sum_i a_iw_i\). Using \(Nt=\sum_i a_i^2\) and \(N=\sum_i a_i\), a symmetric expansion gives
\[
N\sum_i a_iw_i(t-a_i)
=\sum_{i<j}a_ia_j(a_i-a_j)(w_j-w_i).
\tag{5}
\]
If \(a_i\ge a_j\), then \(N-a_i\le N-a_j\), and consequently \(w_i\le w_j\), including thresholded zero terms. Every summand on the right of (5) is nonnegative. Because \(1\le t\le N\) (the lower equality is exactly an all-singleton population and the upper equality is exactly a one-species population), equations (1), (4), and (5) prove (2).

For strictness, when \(1<t<N\) the first factor \((t-1)(N-t)\) is strictly positive. The sum \(A\) is positive exactly when at least one species is absent with positive probability at depth \(m\), equivalently \(m\le N-\min_i a_i\). Hence (2) is strictly positive precisely under the stated three conditions. If \(t=1\) (all singletons), every sample contains exactly \(m\) species and \(\widehat G_m=1\), so the covariance is zero. If \(t=N\) (one species), both statistics are constant. If \(m>N-\min_i a_i\), no species can be absent, so \(K_m=s\) is constant. This proves the converse and completes all boundary cases.

Finally, if all \(a_i\) are equal, then all \(w_i\) are equal and the second term of (2) vanishes. The first term is thus an attained lower bound for every feasible equal-abundance census, including positive nondegenerate cases.

## Verification

The standalone program `verify_rarefaction_covariance.py` uses only Python's standard library and exact integer or rational arithmetic; run it with `python verify_rarefaction_covariance.py`. It independently computes \(\operatorname{Cov}(K_m,\widehat G_m)\) in three ways: enumeration of all labeled \(m\)-subsets; multivariate-hypergeometric enumeration of abundance-count vectors; and the closed formula and lower bound above. It enumerates all positive-integer abundance profiles for \(2\le N\le12\), hence **270 profiles and 2,375 profile–sample-size pairs**. All three formulas, the nonnegative lower bound, and the exact strict-versus-zero classification agree in all cases. The associated `verification_certificate.json` records 1,891 strict-positive cases and 484 zero cases. These finite checks support but do not replace the all-\(N\) proof.

## Relationship to prior work

Barbour develops the occupied-box count in iid occupancy schemes, and Källberg, Leonenko, and Seleznjev study pair-coincidence \(U\)-statistics in independent categorical sampling. The public mathematical finding *Universal positive covariance of sample richness and unbiased Gini–Simpson diversity* (published-finding corpus, 2026) proves positive covariance and an exact formula for iid draws with replacement. None of those results automatically supplies the finite-population law (1): with-replacement and without-replacement pair probabilities, absence probabilities, and equality cases differ. In particular, the iid covariance is strictly positive for all sample sizes under any nondegenerate categorical law, whereas the finite-census covariance here becomes zero when richness saturates.

Colwell and collaborators (2012) provide a comprehensive individual-based rarefaction framework, including the finite-population (hypergeometric) model and variance of richness. Their accessible full article concentrates on richness and its sampling uncertainty, rather than the covariance of richness with pairwise-difference diversity. Nipperess and Matsen (2012 preprint) treat clade-detection covariances for phylogenetic diversity, a different joint statistic. The present theorem is a mixed richness–Simpson covariance identity and sharp sign/equality law specifically for uniform finite-population samples.

## Limitations

The theorem concerns a fixed, known finite census and uniform equal-probability sampling without replacement. It does not establish a stochastic association order, nonuniform inclusion probabilities, imperfect detection, spatially clustered sampling, or an unknown-population inference procedure. Literature comparisons are necessarily incomplete; an equivalent older derivation under occupancy, ecological diversity, or survey-sampling terminology remains possible. The full text of the early Heck–van Belle–Simberloff rarefaction article could not be inspected in this research assessment; its accessible bibliographic record describes univariate rarefaction, but that alone cannot rule out an equivalent in its detailed development. Independent scientific review and additional bibliographic confirmation remain outstanding.

## References

1. A. D. Barbour, *Univariate approximations in the infinite occupancy scheme*, arXiv:0902.0879, first public version 2009-02-05, https://arxiv.org/abs/0902.0879.
2. D. Källberg, N. Leonenko, and O. Seleznjev, *Statistical Inference for Rényi Entropy Functionals*, arXiv:1103.4977, first public version 2011-03-25, https://arxiv.org/abs/1103.4977.
3. R. K. Colwell et al., *Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages*, Journal of Plant Ecology 5 (2012), 3–21, DOI:10.1093/jpe/rtr044, author-hosted full text https://www.robertkcolwell.org/publications/6855.pdf.
4. D. A. Nipperess and F. A. Matsen, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552, first posted 2012-08-31, https://arxiv.org/abs/1208.6552.
5. A. D. Heck, G. van Belle, and D. Simberloff, *Explicit calculation of the rarefaction diversity measurement and the determination of sufficient sample size*, Ecology 56 (1975), DOI:10.2307/1934716. Full technical text not inspected.
6. *Universal positive covariance of sample richness and unbiased Gini–Simpson diversity*, public published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-universal-positive-covariance-of-sample-richness-and-unbiased-gi--e84114bd4ba0.
