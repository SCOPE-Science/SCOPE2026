# Exact two-statistic Gaussian power law for alternating multinomial alternatives

## Finding

For each *even* integer \(n\ge2\), let \(X=(X_1,\ldots,X_n)\) have a multinomial distribution with \(N\) trials and bin probabilities
\[
p_{j,N,n}=\frac{1+\kappa n^{1/4}(-1)^j/\sqrt N}{n},\qquad 1\le j\le n,
\]
where \(\kappa\ge0\) is fixed and \(N\) is sufficiently large that all probabilities are positive. Define the noncyclic discrete total variation and the Pearson statistic by
\[
D_{N,n}=\sum_{j=1}^{n-1}|X_{j+1}-X_j|,\qquad
P_{N,n}=\sum_{j=1}^n\frac{(X_j-N/n)^2}{N/n}.
\]
Set
\[
\sigma^2=\frac83+\frac{4(\sqrt3-3)}{\pi}>0,\qquad
\rho=\frac{\sqrt2}{\sigma\sqrt\pi}\in(0,1).
\]
With \(Z^D_{N,n}=(D_{N,n}/\sqrt N-2(n-1)/\sqrt{\pi n})/\sigma\) and \(Z^P_{N,n}=(P_{N,n}-(n-1))/\sqrt{2n}\), we prove the **iterated limit**: first take \(N\to\infty\) with fixed even \(n\), and then take even \(n\to\infty\). The limiting joint law is
\[
\begin{pmatrix}Z^D_{N,n}\\Z^P_{N,n}\end{pmatrix}
\Longrightarrow
\mathcal N_2\!\left(
\kappa^2\begin{pmatrix}2/(\sigma\sqrt\pi)\\1/\sqrt2\end{pmatrix},
\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}
\right).
\]
In particular, one-sided tests separately rejecting at a standard-normal critical value \(z_{1-q}\) have limiting power
\[
1-\Phi\!\left(z_{1-q}-\frac{2\kappa^2}{\sigma\sqrt\pi}\right)
\quad\text{and}\quad
1-\Phi\!\left(z_{1-q}-\frac{\kappa^2}{\sqrt2}\right)
\]
for asymptotic size \(q\in(0,1)\). The **ratio of squared standardized Gaussian-shift coefficients** is exactly
\[
\frac{8}{\pi\sigma^2}=2.420001086449548\ldots.
\]
This coefficient ratio is not asserted to be a conventional Pitman efficiency under an unspecified common sample-size scaling.

The joint law yields a further, somewhat counterintuitive consequence. Among one-sided tests whose statistic is a fixed nonzero linear combination of the two standardized coordinates, the best Gaussian mean-to-standard-deviation ratio is attained (uniquely up to a positive constant) by
\[
Z^{\mathrm{joint}}_{N,n}
=\frac{\rho Z^D_{N,n}+(1-2\rho^2)Z^P_{N,n}}{\sqrt{1-\rho^2}},
\]
which has limiting variance one and mean \(\kappa^2/\sqrt{2(1-\rho^2)}\). Since \(1-2\rho^2<0\), the optimizing coefficient on Pearson's statistic is **negative**, even though each statistic alone has a positive mean shift. This is optimal only within the stated two-dimensional linear family, not among all possible tests of a known comb contrast.

## Assumptions and scope

The histogram bins are ordered; the statistic is the noncyclic sum of adjacent absolute differences. The number of bins is even. The \(N\to\infty\) limit is taken at every fixed even \(n\), so multinomial central limit theory applies with a fixed dimension. The subsequent \(n\to\infty\) limit is along even integers and holds for each fixed \(\kappa\ge0\). In particular, no simultaneous-growth condition on \(N\) and \(n\) is established. Known-period signed-contrast tests can outperform both statistics and are outside the stated optimality claim.

## Proof

**1. Gaussian reduction at fixed dimension.** Let \(G_1,\ldots,G_n\) be independent standard normal variables, \(\overline G=n^{-1}\sum_jG_j\), and write \(\epsilon_j=(-1)^j\). The triangular multinomial central limit theorem and the deterministic mean shift give
\[
\frac{X_j-N/n}{\sqrt N}\Longrightarrow
\frac{G_j-\overline G}{\sqrt n}+\kappa n^{-3/4}\epsilon_j.
\]
Since \(\sum_j\epsilon_j=0\) for even \(n\), both the covariance and deterministic shift match the multinomial constraint. The continuous mapping theorem therefore gives the joint fixed-\(n\) limits
\[
A_n(\kappa)=\frac1{\sqrt n}\sum_{j=1}^{n-1}
\left|G_{j+1}-G_j+2\kappa n^{-1/4}(-1)^{j+1}\right|,
\]
\[
B_n(\kappa)=\sum_{j=1}^n
\bigl(G_j-\overline G+\kappa n^{-1/4}\epsilon_j\bigr)^2
\]
for \(D_{N,n}/\sqrt N\) and \(P_{N,n}\), respectively. This reduction requires no approximation uniform in \(n\).

**2. The null stationary one-dependent array.** Put \(W_j=G_{j+1}-G_j\) and \(H_j=|W_j|-2/\sqrt\pi\). Each \(W_j\) has variance two; adjacent pairs have correlation \(-1/2\); nonadjacent pairs are independent. The standard bivariate-normal absolute-product identity yields
\[
\operatorname{Var}|W_j|=2-\frac4\pi,\qquad
\operatorname{Cov}(|W_j|,|W_{j+1}|)=
\frac13+\frac{2\sqrt3-4}{\pi}.
\]
The long-run variance of the stationary one-dependent sequence \((H_j)\) is consequently
\[
\operatorname{Var}(H_1)+2\operatorname{Cov}(H_1,H_2)
=\frac83+\frac{4(\sqrt3-3)}{\pi}=\sigma^2.
\]
For a direct cross-covariance calculation, condition on \(W=G_2-G_1\). Gaussian regression gives
\[
\mathbb E[G_1^2-1\mid W]=W^2/4-1/2.
\]
Since \(\mathbb E|W|=2/\sqrt\pi\) and \(\mathbb E|W|^3=8/\sqrt\pi\),
\[
\operatorname{Cov}(|G_2-G_1|,G_1^2-1)=\frac1{\sqrt\pi},
\]
and the same identity holds for \(G_2\). Therefore each interior edge contributes \(2/\sqrt\pi\) to the covariance of the absolute-edge sum and the sum of centered squares, all other terms being independent. The joint one-dependent central limit theorem applies to
\[
\left(n^{-1/2}\sum_{j<n}H_j,\ (2n)^{-1/2}\sum_{j\le n}(G_j^2-1)\right)
\]
and gives marginal variances \(\sigma^2,1\) and covariance \(\sqrt2/\sqrt\pi\). The finite endpoint omission is negligible. Dividing the first coordinate by \(\sigma\) gives correlation \(\rho=\sqrt2/(\sigma\sqrt\pi)\).

**3. The alternating perturbation.** Write \(a_n=2\kappa n^{-1/4}\). The evenness of the centered Gaussian law makes all edge expectations equal to \(m(a_n)=\mathbb E|W_1+a_n|\). Since its density at zero is \(1/(2\sqrt\pi)\), Taylor expansion (or the explicit folded-normal formula) gives
\[
m(a)=\frac2{\sqrt\pi}+\frac{a^2}{2\sqrt\pi}+O(a^4)
\quad(a\to0).
\]
Thus
\[
\frac{n-1}{\sqrt n}\bigl(m(a_n)-m(0)\bigr)
\longrightarrow\frac{2\kappa^2}{\sqrt\pi}.
\]
Let \(U_j=|W_j+(-1)^{j+1}a_n|-|W_j|\). Then \(|U_j|\le a_n\). The centered \(U_j\)'s are one-dependent, so
\[
\operatorname{Var}\left(\frac1{\sqrt n}\sum_{j<n}(U_j-\mathbb EU_j)\right)
\le C a_n^2\to0
\]
for an absolute constant \(C\), by Cauchy-Schwarz and the bounded dependency range. The local perturbation therefore changes only the limiting mean of the first Gaussian coordinate.

For Pearson's limit, expand exactly using \(\sum\epsilon_j=0\):
\[
B_n(\kappa)=\sum_{j=1}^n(G_j-\overline G)^2
+2\kappa n^{-1/4}\sum_{j=1}^n\epsilon_jG_j
+\kappa^2\sqrt n.
\]
The first term equals \(\sum_jG_j^2-n\overline G^2\). After centering by \(n-1\) and scaling by \(\sqrt{2n}\), the term \(1-n\overline G^2\) is \(o_P(1)\), the centered random linear term is \(O_P(n^{-1/4})\), and the deterministic shift tends to \(\kappa^2/\sqrt2\). Combining with the joint null array limit proves the asserted joint Gaussian law.

**4. Power and linear optimization.** A Gaussian coordinate with unit variance and mean \(c\kappa^2\) exceeds \(z_{1-q}\) with probability \(1-\Phi(z_{1-q}-c\kappa^2)\). The two mean coefficients give the displayed squared-shift ratio. Write \(m=(\sqrt2\rho,1/\sqrt2)^\top\) and \(\Sigma=\bigl(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\bigr)\). The Cauchy-Schwarz inequality in the \(\Sigma\)-inner product proves that any nonzero weight vector \(w\) obeys
\[
\frac{w^\top m}{\sqrt{w^\top\Sigma w}}
\le\sqrt{m^\top\Sigma^{-1}m}
=\frac1{\sqrt{2(1-\rho^2)}}.
\]
Equality holds precisely for positive multiples of \(\Sigma^{-1}m\), proportional to \((\rho,1-2\rho^2)\). Numerically \(\rho=0.777817633904\ldots\), and \(2\rho^2>1\), which establishes the sign assertion.

## Verification

The accompanying standalone standard-library Python file `verification/verify.py` recomputes the closed constants, folded-normal mean expansion, and covariance identities and performs a seeded Gaussian-limit simulation. The saved output records the observed values and tolerances. Simulation is corroborative: the proof of every infinite-limit assertion is the analytic argument above. Execute `python verification/verify.py` in an environment with Python 3.10 or newer; no additional packages or external files are required.

## Relationship to prior work

Banić and Elezović's May 31, 2026 *Comb Test* article introduced the ordered-bin test and documented empirical advantages against alternating deviations, but did not derive this growing-bin Gaussian-shift limit. Their October 9, 2026 Part 1 paper explicitly says it proves no power result, and computes the null mean. Their October 12, 2026 Part 2 paper computes the null variance and links it to classical normal mean-moving-range results; that already covers the variance ingredient, which is **not claimed as new**. The distinctive assertion here is the **joint law under specified shrinking alternating alternatives**, including the cross-statistic covariance in that regime, exact relative standardized shifts, and the sign-reversing optimal two-statistic combination. Hoel's and Kamat's classical Gaussian mean-range theory may subsume ingredients of the null covariance, but does not itself specify the multinomial comb-alternative limit. Beirlant and Györfi (1994) analyzed powers of \(\ell_p\) norms of **cellwise errors from uniformity**; their statistics do not use adjacent absolute differences and their fixed-density perturbation assumptions differ from the current period-two bin-scale regime.

## Limitations

The limits are explicitly **iterated**; the theorem supplies no bound uniform over jointly growing \(n,N\). The coefficient ratio is not a universal relative sample-size efficiency, nor does it compare the tests for smooth, localized, or different-period alternatives. The optimally combined score is optimal only among linear combinations of these two statistics in the displayed bivariate Gaussian experiment, not against an oracle using the known alternating direction. Classical Gaussian covariance formulas and alternative-parameter conventions introduce literature-priority risk; the cited works were compared by their mathematical content, but exhaustive historical uniqueness is not certified. Independent audit has not been performed.

## References

1. N. Banić and N. Elezović, *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation*, first public May 31, 2026, arXiv:2606.01465, https://arxiv.org/abs/2606.01465.
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, first public October 9, 2026, arXiv:2610.13366, https://arxiv.org/abs/2610.13366.
3. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 2: variance under the uniform null*, first public October 12, 2026, arXiv:2610.17046, https://arxiv.org/abs/2610.17046.
4. P. G. Hoel, *The efficiency of the mean moving range*, Annals of Mathematical Statistics 17 (1946), 475–482.
5. A. R. Kamat, *On the mean successive difference and its ratio to the root mean square*, Biometrika 40 (1953), 116–127.
6. J. Beirlant and L. Györfi, *Pitman efficiencies of \(L_p\)-goodness-of-fit tests*, Kybernetika 30 (1994), 223–232, https://dml.cz/dmlcz/125168.
