# Five categories are necessary for positive Good–Turing–missing-mass covariance at two draws

## Finding

For two independent observations \(X_1,X_2\) from an arbitrary finite categorical law \(p=(p_1,\ldots,p_m)\), define the realized missing mass \(U=\sum_i p_i\mathbf1\{i\notin\{X_1,X_2\}\}\) and the ordinary Good–Turing estimator \(G=N_1/2=\mathbf1\{X_1\ne X_2\}\), where \(N_1\) is the number of categories seen exactly once.

The *sharp support threshold* is five: for every law with \(2\le m\le4\) strictly positive category probabilities, \(\operatorname{Cov}(U,G)<0\). For every \(m\ge5\), strictly positive \(m\)-category laws exist with \(\operatorname{Cov}(U,G)<0\), with equality, and with \(\operatorname{Cov}(U,G)>0\). For a one-point law, the covariance is zero.

In particular, \(p=(4/5,1/20,1/20,1/20,1/20)\) gives \(\operatorname{Cov}(U,G)=1/1600>0\), whereas equal masses on \(m\) categories give \(\operatorname{Cov}(U,G)=-(m-1)/m^3<0\). Thus observing distinct labels is anti-associated with the missing mass for every nondegenerate law on at most four categories, but this relationship can reverse as soon as five categories are possible.

## Assumptions and scope

The observations are iid under a *fixed* probability vector with a finite number \(m\) of strictly positive coordinates. No Bayesian prior, asymptotics, unobserved population model, or restriction on probability magnitudes is assumed. The sample size equals two throughout. The covariance refers to repeated experiments under the same law; it is *not* a pointwise guarantee about estimation error. Adding zero-probability labels does not change the effective support.

## Proof

Put \(s_j=\sum_{i=1}^{m}p_i^j\), for \(j=2,3\). Two-draw enumeration gives
\[
\mathbb E G=1-s_2,\quad \mathbb E U=1-2s_2+s_3,\quad
\mathbb E(UG)=1-3s_2+2s_3.
\]
Indeed, if the observed labels are different, the missing mass is \(1-p_{X_1}-p_{X_2}\); otherwise \(G=0\). Consequently
\[
\boxed{\operatorname{Cov}(U,G)=(1+s_2)s_3-2s_2^2.}\tag{1}
\]
This identity is elementary and is used here as a starting point, not presented as a novel general occupancy-moment method.

To prove the nonpositive direction sharply, pad the vector with zeros to length four (when necessary), and let \(u=s_2\in[1/4,1]\). Set
\[
a=\frac{1+\sqrt{3(4u-1)}}4,\qquad b=\frac{1-a}{3}.
\]
Then \(a+3b=1\), \(a^2+3b^2=u\), and \(0\le b\le a\le1\). Every coordinate \(x=p_i\) satisfies \((1-x)^2\le3(u-x^2)\), by Cauchy–Schwarz on the other three coordinates. Therefore \(4x^2-2x+1-3u\le0\), which implies \(x\le a\).

For every \(0\le x\le a\), \((x-b)^2(x-a)\le0\). Summing this cubic inequality over the four coordinates, and using the identical first and second power sums of \((p_i)_i\) and \((a,b,b,b)\), gives
\[
s_3\le a^3+3b^3.
\]
Since the right side of (1) is strictly increasing in \(s_3\) at fixed \(s_2\), it follows that
\[
\operatorname{Cov}(U,G)\le(1+u)(a^3+3b^3)-2u^2
=\frac{2}{27}(a-1)^3(16a^2-2a+1).
\]
The quadratic is strictly positive for every real \(a\), since its discriminant is negative. If the law is not concentrated at one label, \(u<1\) and hence \(a<1\), making the bound strictly negative. If the law is concentrated at one label, both variables are constant and covariance is zero. This proves strict negativity for every law with effective support between two and four, with no numerical optimization.

For \(m=5\), the positive example in the Finding has \(s_2=13/20\) and \(s_3=41/80\); substitution into (1) gives \(1/1600\). For any larger \(m\), assign sufficiently small positive total mass to the additional labels and scale the five probabilities accordingly; by continuity of (1), positivity persists. Equal probabilities yield the displayed strictly negative expression. The simplex of strictly positive \(m\)-category laws is path connected, and covariance is continuous, so an intermediate strictly positive law has covariance zero. All three signs thus occur for every \(m\ge5\), completing the classification.

## Verification

Run `python3 check.py` from this package. The checker enumerates both observation labels with exact rational weights, compares the directly computed covariance against (1), checks strict negative covariance over a family of rational probability vectors of supports two through four, verifies the \(1/1600\) five-category witness, checks the uniform-law formula and the sharp four-coordinate polynomial factorization. It passed 2,444 exact-rational comparisons. Those finite checks corroborate, but do not replace, the preceding all-laws inequality proof.

## Relationship to prior work

The target and the Good–Turing singleton estimator are classical. Skorski, *Mean-Squared Accuracy of Good-Turing Estimator* (2021), studies worst-case estimator mean-squared error as a function of alphabet size and derives occupancy-moment expansions; this does not state or imply by its published asymptotic worst-risk optimization a sharp *covariance-sign* support threshold at sample size two. Cohen, Routtenberg, and Tong, *Non-Bayesian Parametric Missing-Mass Estimation* (arXiv:2101.04329), analyze missing-mass risk bounds and do not state this covariance cutoff. Painsky, *Generalized Good-Turing Improves Missing Mass Estimation* (public version 2021; journal 2023), studies improved missing-mass risk bounds and alphabet information; accessible abstract material does not assert the threshold. The exact general occupancy moment is not claimed as new. The present contribution is the sharp support-size classification from the power-sum extremal inequality and its positive witness.

## Limitations

The theorem concerns exactly two iid draws, and no analogous cutoff is asserted for larger samples, dependent data, or unknown varying probability vectors. The positive covariance \(1/1600\) is small, but is an exact sign reversal in a fundamental estimator–target relationship. Historical priority beyond the inspected primary text and available bibliographic evidence is not independently established; in particular the full Painsky paper was not accessible for examination. Correlation sign alone does not evaluate estimator risk or establish usefulness of a sample of size two for practical estimation.

## References

1. Maciej Skorski, *Mean-Squared Accuracy of Good-Turing Estimator*, arXiv:2104.07029v1 (first publicly posted 2021-04-14), https://arxiv.org/abs/2104.07029.
2. Amichai Cohen, Routtenberg, and Tong, *Non-Bayesian Parametric Missing-Mass Estimation* (arXiv:2101.04329), analyze missing-mass risk bounds and do not state this covariance cutoff. Painsky, *Generalized Good-Turing Improves Missing Mass Estimation*, *Journal of the American Statistical Association* 118 (2023), 1890–1899, DOI:10.1080/01621459.2021.2020658 (accepted manuscript first posted 2021-12-21).
3. Shir Cohen, Tirza Routtenberg, Lang Tong, *Non-Bayesian Parametric Missing-Mass Estimation*, arXiv:2101.04329v1 (first publicly posted 2021-01-12), https://arxiv.org/abs/2101.04329.
4. Irving J. Good, *The Population Frequencies of Species and the Estimation of Population Parameters*, *Biometrika* 40 (1953), 237–264 (background only).
