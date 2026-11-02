# Joint Gaussian record–descent fluctuations under linear record bias

## Finding
For fixed \(\lambda>0\), let \(\pi_n\) be a permutation of \(\{1,\ldots,n\}\) sampled with weight \((\lambda n)^{R_n}\), where \(R_n\) counts left-to-right maxima. Write \(D_n=\#\{i<n:\pi_n(i)>\pi_n(i+1)\}\). Then
\[
\frac{1}{\sqrt n}\begin{pmatrix}R_n-\mathbb ER_n\\D_n-\mathbb ED_n\end{pmatrix}
\ \Longrightarrow\ \mathcal N_2(0,\Sigma_\lambda),
\quad
\Sigma_\lambda=\begin{pmatrix}
\lambda\log(1+1/\lambda)-\frac{\lambda}{1+\lambda}&-\frac{\lambda}{2(1+\lambda)^2}\\
-\frac{\lambda}{2(1+\lambda)^2}&\frac{6\lambda^2+4\lambda+1}{12(1+\lambda)^3}
\end{pmatrix}.
\]
The covariance matrix is strictly positive definite. Thus the centered, order-\(\sqrt n\) record and descent fluctuations remain *correlated*, with a strictly negative limiting correlation, rather than becoming independent. For example, at \(\lambda=1\) the limiting correlation is approximately \(-0.84024338\).

The exact finite-size identity
\[
\operatorname{Cov}_{n,\theta}(R_n,D_n)=-\frac{\theta n(n-1)}{2(\theta+n-1)^2}
\]
holds whenever \(n\ge2\) and \(\theta>0\). The exact covariance follows by differentiating an already-known descent expectation; the claimed contribution is the joint fluctuation law and explicit variance structure in the linear-tilt regime.

## Assumptions and scope
For any \(n\ge1\) and \(\theta>0\), the probability of \(\pi\in S_n\) is
\[
\Pr_{n,\theta}(\pi)=\frac{\theta^{R(\pi)}}{\theta(\theta+1)\cdots(\theta+n-1)}.
\]
A position \(i\) is a left-to-right maximum if its value exceeds all values at preceding positions. A descent at \(i<n\) means \(\pi(i)>\pi(i+1)\). The asymptotic result assumes exactly \(\theta_n=\lambda n\) with fixed \(\lambda>0\) as \(n\to\infty\). No claim is made here for a parameter tending to zero or infinity with \(n\), for other permutation biases, or for quantitative normal approximation rates.

## Proof
**1. Independent ranks.** Define \(U_i\) to be the rank of \(\pi(i)\) among \(\pi(1),\ldots,\pi(i)\), counted from the smallest. The map \(\pi\mapsto(U_1,\ldots,U_n)\) is bijective. Each \(U_i\) is independent and
\[
\Pr(U_i=k)=\frac{1}{\theta+i-1}\quad(1\le k<i),
\qquad \Pr(U_i=i)=\frac{\theta}{\theta+i-1}.
\]
Write \(B_i=\mathbf1_{\{U_i=i\}}\) and \(X_i=\mathbf1_{\{U_{i+1}\le U_i\}}\) for \(1\le i<n\). Then \(R_n=\sum_{i=1}^nB_i\), \(D_n=\sum_{i=1}^{n-1}X_i\), and the two-dimensional array of local summands \((B_i,X_i)\) (with \(X_n=0\)) is 1-dependent.

**2. Exact first and second moments.** Directly summing over the independent ranks gives
\[
 r_i=\Pr(B_i=1)=\frac{\theta}{\theta+i-1},\qquad
 p_i=\Pr(X_i=1)=\frac{i(2\theta+i-1)}{2(\theta+i-1)(\theta+i)},
\]
\[
 j_i=\Pr(X_i=X_{i+1}=1)
 =\frac{i(i+1)(3\theta+i-1)}{6(\theta+i-1)(\theta+i)(\theta+i+1)}.
\]
The last formula follows by conditioning on \(U_{i+1}=k\le U_i\) and observing that \(\Pr(U_{i+2}\le k)=k/(\theta+i+1)\). Since nonadjacent descent indicators are independent,
\[
 \operatorname{Var}(R_n)=\sum_{i=1}^n r_i(1-r_i),\qquad
 \operatorname{Var}(D_n)=\sum_{i=1}^{n-1}p_i(1-p_i)
 +2\sum_{i=1}^{n-2}(j_i-p_ip_{i+1}).
\]
In particular the established expectation is \(\mathbb ED_n=n(n-1)/[2(\theta+n-1)]\). Exponential-tilt differentiation yields
\[
 \operatorname{Cov}(R_n,D_n)=\theta\frac{\partial}{\partial\theta}\mathbb ED_n
 =-\frac{\theta n(n-1)}{2(\theta+n-1)^2}.
\]
The exact record expectation is \(\mathbb ER_n=\sum_{i=1}^n\theta/(\theta+i-1)\).

**3. Limiting covariance.** Let \(\theta=\lambda n\) and \(i/n\to t\in[0,1]\). Put \(q(t)=\lambda/(\lambda+t)\). Uniformly in the indices,
\[
 r_i\to q(t),\qquad p_i\to p(t)=\frac{1-q(t)^2}{2},\qquad
 j_i\to j(t)=\frac{(1-q(t))^2(1+2q(t))}{6}.
\]
Riemann sums and the exact cross-covariance therefore give
\[
 \lim_{n\to\infty}\frac{\operatorname{Var}(R_n)}n
 =\int_0^1q(t)(1-q(t))\,dt
 =\lambda\log(1+1/\lambda)-\frac\lambda{1+\lambda},
\]
\[
 \lim_{n\to\infty}\frac{\operatorname{Var}(D_n)}n
 =\int_0^1\big[p(t)(1-p(t))+2(j(t)-p(t)^2)\big]dt
 =\frac{6\lambda^2+4\lambda+1}{12(1+\lambda)^3},
\]
\[
 \lim_{n\to\infty}\frac{\operatorname{Cov}(R_n,D_n)}n
 =-\frac{\lambda}{2(1+\lambda)^2}.
\]
The displayed descent integrand is also \((1-q)(9q^3+q^2+q+1)/12\), which is nonnegative and nonzero on \((0,1]\).

**4. Strict nondegeneracy.** Fix real numbers \(a,b\) not both zero and condition on all rank variables except every third \(U_i\) for \(i\in[n/3,2n/3]\). Each remaining \(U_i\) independently affects only its record indicator and the two incident descent indicators. With probability bounded below in terms of \(\lambda\), the neighboring ranks satisfy \(U_{i-1}\in[i/4,i/3]\) and \(U_{i+1}\in[2i/3,3i/4]\). Conditional on such neighbors, three rank choices for \(U_i\), each having probability bounded below, produce the pairs
\[
 (B_i,X_{i-1}+X_i)=(0,1),\ (0,0),\ (1,1):
\]
respectively, choose \(U_i<i/4\), \(i/3<U_i<2i/3\), and \(U_i=i\). For sufficiently large \(n\), the intervals contain linearly many admissible ranks. The three corresponding values of \(aB_i+b(X_{i-1}+X_i)\) are \(b,0,a+b\), so their conditional variance is bounded below by \(c_\lambda(a^2+b^2)\) for some \(c_\lambda>0\). Summing across linearly many disjoint index neighborhoods and applying total variance shows
\[
 \operatorname{Var}(aR_n+bD_n)\ge c'_\lambda n(a^2+b^2).
\]
Thus every nonzero quadratic form of \(\Sigma_\lambda\) is strictly positive.

**5. Bivariate normal convergence.** For any fixed \((a,b)\), the centered local summands in \(aR_n+bD_n\) are uniformly bounded and 1-dependent. Separate the index interval into blocks of length \(m_n=\lfloor n^{1/4}\rfloor\), omitting one separator index between blocks. The remaining block sums are independent. Their absolute values are \(O(m_n)=o(\sqrt n)\); the omitted centered terms have variance \(O(n/m_n)=o(n)\) by 1-dependence. Consequently the independent triangular-array Lindeberg theorem applies, with limiting variance \((a,b)\Sigma_\lambda(a,b)^\mathsf T\). The negligible separators and Cramér–Wold theorem give the claimed joint Gaussian limit.

## Verification
A standalone exact-rational Python checker, included as `checker.py`, independently enumerates weighted permutations for sizes \(2\le n\le7\) and four positive rational tilts. It compares directly enumerated expectations, variances, adjacent-descent pair probabilities and mixed covariance with all formulas above. It additionally checks the proposed limiting variances and covariance numerically for three linear-bias ratios at three larger sizes. The checker reports **318 exact identities and asymptotic probes passed**, from **23,648 weighted-permutation enumerations**. The symbolic identity for the limiting descent variance was also integrated separately. Finite checks corroborate but do not prove the unbounded-\(n\) theorem; the proof is above.

## Relationship to prior work
Bouvel, Nicaud and Pivoteau (first arXiv version 2024-09-03) define this record bias, give the independent insertion-rank construction and exact record and descent means, and prove marginal Gaussian limits specifically for **fixed** \(\theta\). Their \(\theta=\lambda n\) study determines first-order expectations and the permuton limit, not the joint order-\(\sqrt n\) record–descent fluctuations established here. The earlier Auger et al. (2016) manuscript likewise gives expectation identities. Féray (2013) treats pattern statistics under Ewens measures with fixed bias; through Foata this gives background for fixed-bias one-dimensional results, not the present linear-bias joint covariance. Borodin–Diaconis–Fulman (2010) study one-dependent descent processes and Gaussian limits in the uniform/Mallows families, without the record-biased triangular law. Butler (2023) discusses joint Stirling–Euler–Mahonian distribution identities for permutation statistics, providing finite-distribution combinatorial context but not the stated linear-tilt bivariate Gaussian formula. The exact mean and the derivative-derived exact covariance are acknowledged deductions from earlier known formulas, not separately claimed discoveries.

## Limitations
The parameter ratio \(\lambda\) must remain fixed and strictly positive. This does not give a local limit theorem, a quantitative convergence rate, an invariance principle, the limiting covariance with inversions, or a statement for all variable-parameter regimes. A general bounded 1-dependent-array CLT is standard; what is asserted as an added result here is its application with the explicit two-statistic covariance and strict residual correlation at linear record bias. This self-review is not independent validation. Unidentified equivalent prior asymptotics remain a historical-priority risk.

## References
1. M. Bouvel, C. Nicaud and C. Pivoteau, *Record-biased permutations and their permuton limit*, arXiv:2409.01692v1 (2024-09-03), especially Sections 3.2, 4.1, 4.2, 4.3 and 5; https://arxiv.org/abs/2409.01692 . Published *Combinatorics, Probability and Computing* (2026), primary MSC2020 60C05.
2. N. Auger, M. Bouvel, C. Nicaud and C. Pivoteau, *Analysis of Algorithms for Permutations Biased by Their Number of Records*, arXiv:1605.02905 (2016); https://arxiv.org/abs/1605.02905 .
3. V. Féray, *Asymptotics of some statistics in Ewens random permutations*, arXiv:1201.2157 (2013 publication); https://arxiv.org/abs/1201.2157 .
4. A. Borodin, P. Diaconis and J. Fulman, *On adding a list of numbers (and other one-dependent determinantal processes)*, arXiv:0904.3740 (2009); https://arxiv.org/abs/0904.3740 .
5. F. Butler, *Stirling-Euler-Mahonian Triples of Permutation Statistics*, arXiv:2305.11273v1 (2023-05-18); https://arxiv.org/abs/2305.11273 .
