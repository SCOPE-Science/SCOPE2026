# Exact transport costs for single-trial Poissonization and a quadratic collision gap

## Finding
For every integer \(d\ge1\), let \(I\) be uniform on \(\{1,\ldots,d\}\), let \(\mu_d\) be the law of the coordinate vector \(e_I\), and let \(\nu_d\) be the law of \(Y=(Y_1,\ldots,Y_d)\) with independent coordinates \(Y_i\sim\operatorname{Pois}(1/d)\). Thus the coordinate means agree and both total means equal one. Denote optimal expected \(\ell_1\) cost by \(W_{1,\ell_1}\), and optimal expected squared Euclidean cost by \(W_{2,\ell_2}^2\); these are *different cost functions*, not two notations for the same metric.

Writing \(M_d=\max_i Y_i\) and \(F_x(r)=\Pr\{\operatorname{Pois}(x)\le r\}\), both transport problems have the same explicit optimal coupling: conditional on \(Y\), choose \(I\) uniformly among the indices attaining \(M_d\). Their exact values are
\[
W_{1,\ell_1}(\mu_d,\nu_d)=\frac2e,\qquad
W_{2,\ell_2}^2(\mu_d,\nu_d)=2+\frac1d-2\,\mathbb E M_d
=2+\frac1d-2\sum_{k=1}^{\infty}\bigl(1-F_{1/d}(k-1)^d\bigr).
\]
For every finite integer \(d\ge1\), the second cost is strictly greater than \(2/e\); its exact excess is a nonnegative collision functional,
\[
W_{2,\ell_2}^2(\mu_d,\nu_d)-\frac2e
=2\,\mathbb E\!\left[\sum_{i=1}^d\binom{Y_i}{2}-(M_d-1)_+\right]>0.
\]
Despite this strict finite-dimensional gap, as \(d\to\infty\),
\[
W_{2,\ell_2}^2(\mu_d,\nu_d)
=\frac2e+\frac7{12d^2}+O(d^{-3}).
\]
The coefficient \(7/12\) is the precise leading correction; the \(d^{-1}\) term cancels.

## Assumptions and scope
Here \(d\) is any positive integer. The comparison is between exactly one categorical draw and a collection of **independent**, equally weighted Poisson variables with the same marginal means. Define \(e_i\in\mathbb R^d\) as the vector with one in coordinate \(i\) and zero elsewhere. \(\binom{r}{2}=r(r-1)/2\) for nonnegative integers \(r\), and \((z)_+=\max(z,0)\). Each transport cost is the infimum over joint laws with the specified marginals. The sum defining \(\mathbb E M_d\) converges absolutely because \(M_d\le\sum_iY_i\) and the total mean is one.

## Proof
**An admissible maximal-coordinate coupling.** The law of \(Y\) is invariant under coordinate permutations. Conditional on \(Y=y\), choose \(I\) by a uniform tie-break among the indices \(\operatorname*{arg\,max}_i y_i\). The resulting law of \(I\) is exchangeable on a finite transitive set, hence uniform. This indeed couples \(\mu_d\) and \(\nu_d\), and satisfies \(Y_I=M_d\) almost surely.

**Optimality for the two transport costs.** For every possible coupling of \(I\) and \(Y\),
\[
\|e_I-Y\|_2^2=1+\sum_{j=1}^dY_j^2-2Y_I
\ge 1+\sum_{j=1}^dY_j^2-2M_d.
\]
Equality holds under the maximal-coordinate coupling. Since \(\mathbb E Y_j^2=d^{-1}+d^{-2}\), summation gives \(\mathbb E\sum_jY_j^2=1+d^{-1}\). This proves the exact quadratic transport formula. Similarly, because all \(Y_j\) are nonnegative integers,
\[
\|e_I-Y\|_1=1+\sum_{j=1}^dY_j-2\mathbf1_{\{Y_I\ge1\}}
\ge1+\sum_{j=1}^dY_j-2\mathbf1_{\{M_d\ge1\}}.
\]
The same coupling attains equality. The total count \(N=\sum_jY_j\) is \(\operatorname{Pois}(1)\), so \(\Pr(M_d\ge1)=\Pr(N\ge1)=1-e^{-1}\). Taking expectations yields \(W_{1,\ell_1}=2/e\). Finally, the tail-sum formula for the nonnegative integer \(M_d\), combined with independence, yields its displayed series representation.

**Positive collision identity.** Separate the \(k=1\) summand: \(\mathbb E M_d=1-e^{-1}+\mathbb E(M_d-1)_+\). Because \(\mathbb E\sum_i\binom{Y_i}{2}=1/(2d)\), subtracting \(2/e\) from the exact cost produces
\[
\frac1d-2\mathbb E(M_d-1)_+
=2\mathbb E\left[\sum_i\binom{Y_i}{2}-(M_d-1)_+\right].
\]
Pointwise, \(\sum_i\binom{Y_i}{2}\ge\binom{M_d}{2}\ge(M_d-1)_+\). These inequalities hold for each nonnegative integer configuration. They are strict on the positive-probability event \(\{Y_1\ge3\}\), proving the global strict gap for every finite \(d\).

**Asymptotic correction.** Put \(x=1/d\), so \(d=x^{-1}\) tends through positive integers. Independence gives
\[
\Pr(M_d\ge2)=1-\bigl[e^{-x}(1+x)\bigr]^{1/x}
=\frac x2-\frac{11x^2}{24}+O(x^3),
\]
using \(\log(1+x)-x=-x^2/2+x^3/3+O(x^4)\). Moreover, the one-coordinate Poisson tail at three equals \(x^3/6+O(x^4)\), so
\[
\Pr(M_d\ge3)=\frac{x^2}{6}+O(x^3).
\]
The remaining tail is uniformly controlled by the fourth factorial moment:
\[
\sum_{k\ge4}\Pr(M_d\ge k)
\le d\,\mathbb E(Y_1-3)_+
\le d\,\mathbb E\binom{Y_1}{4}=\frac{x^3}{24}.
\]
Therefore \(\mathbb E(M_d-1)_+=x/2-7x^2/24+O(x^3)\). Substitution into \(W_{2,\ell_2}^2=2/e+x-2\mathbb E(M_d-1)_+\) proves the claimed \(7x^2/12\) term, with its cancellation of the linear term. No numerical step is used to justify the limit.

## Verification
The standalone \(\texttt{verify.py}\) numerically evaluates the maximum-tail formula for eight dimensions. It independently solves finite **truncated** transport linear programs for dimensions one, two and three, comparing their optima with the corresponding maximum-coordinate couplings, and checks the requisite small-\(x\) coefficients by exact symbolic series. Truncation and floating-point solver tolerances are explicitly bounded as diagnostics, not presented as an infinite-dimensional proof. Reproduce from this directory with \(\texttt{python verify.py}\); dependencies are Python, NumPy, SciPy and SymPy. The all-dimensional result is the analytic argument above.

## Relationship to prior work
Pianoforte and Turin, first publicly available on 2021-05-04, treat multivariate Poisson approximation of Bernoulli-vector sums. Their Theorem 1.1 and Section 3.1 (particularly Corollary 3.1) bound the first-order Wasserstein distance under \(\ell_1\) cost; they do not assert the model-specific exact squared \(\ell_2\) transport cost, maximal-coordinate coupling, or \(7/12\) correction. The present example is in their Bernoulli-vector/Poisson domain, but addresses a **different** transport objective with an exact answer. Deheuvels and Pfeifer (1988) treat multivariate Poissonization with sharp total-variation estimates, but not the squared Euclidean transport metric. Novak's 2019 discussion principally concerns Poisson approximation accuracy in total variation; generic optimal-transport existence results, such as Rüschendorf's, do not directly supply this discrete occupancy-tail asymptotic.

## Limitations
The exact quadratic formula uses one categorical draw and uniform coordinate probabilities; it does not apply as stated to multiple categorical draws or unequal cell probabilities. It supplies neither Wasserstein rates for many-trial Poisson approximation nor a universal law for arbitrary transport costs. Prior semidiscrete-transport and occupancy literature might contain an equivalent special case under different terminology. The finite computations do not establish the limiting theorem.

## References
1. F. Pianoforte and R. Turin, *Multivariate Poisson and Poisson process approximations with applications to Bernoulli sums and U-statistics*, arXiv:2105.01599 (first public preprint: 2021-05-04); *Journal of Applied Probability* 60 (2023), 223–240, DOI:10.1017/jpr.2022.33.
2. S. Y. Novak, *On the accuracy of Poisson approximation*, *Extremes* 22 (2019), 729–748, DOI:10.1007/s10687-019-00350-6.
3. P. Deheuvels and D. Pfeifer, *Poisson Approximations of Multinomial Distributions and Point Processes*, *Journal of Multivariate Analysis* 25 (1988), 65–89, DOI:10.1016/0047-259X(88)90153-4.
4. L. Rüschendorf, *The Wasserstein distance and approximation theorems*, *Probability Theory and Related Fields* 70 (1985), 117–129, DOI:10.1007/BF00532240.
