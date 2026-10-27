# Cyclic Markov dependence defeats a combined runs–frequency test

## Finding

Fix a nominal level \(0<\alpha<1\). Consider the following two-part procedure for testing whether a sequence of three categorical actions is independent and uniform: (i) the generalized Wald–Wolfowitz number-of-runs normal test with its plug-in conditional-count mean and variance; (ii) Pearson's three-category frequency goodness-of-fit test; reject if either test has two-sided (for runs) or upper-tail (for Pearson) nominal level \(\alpha/2\). These are the components of the strategy test in [1].

For every \(0<|\delta|<1/3\), there is a strictly positive, stationary, irreducible, aperiodic three-state Markov chain, with uniform stationary distribution, whose one-step transition probabilities modulo three are
\[
\Pr(X_{t+1}-X_t\equiv0)=\frac13,\quad
\Pr(X_{t+1}-X_t\equiv1)=\frac13+\delta,\quad
\Pr(X_{t+1}-X_t\equiv-1)=\frac13-\delta.
\]

For every sample length \(n\ge2\), its number of linear runs \(R_n\) has **exactly the same law** as for \(n\) independent uniform three-state observations:
\[
R_n\ \stackrel{\mathrm d}=\ 1+\operatorname{Bin}(n-1,2/3).
\]
The plug-in standardized runs statistic nevertheless converges to a standard normal under this dependent alternative. Let \(H_n=\sum_{j=0}^{2}(N_j-n/3)^2/(n/3)\), where \(N_j\) is the sample frequency of state \(j\). Then
\[
H_n\ \Longrightarrow\ c_\delta\,\chi^2_2,\qquad
c_\delta=\frac{1-3\delta^2}{1+3\delta^2}<1.
\]
Therefore the probability that the *combined* two-test procedure rejects this dependent alternative obeys the nontrivial bound
\[
\limsup_{n\to\infty}\Pr_\delta(\mathrm{reject})
\le \frac\alpha2+\left(\frac\alpha2\right)^{1/c_\delta}
<\alpha.
\]
In particular, its power does not approach one, even though the alternative has strong one-step directional dependence. At \(\delta=1/4\) and \(\alpha=0.05\), the upper bound is \(0.029555413\) (rounded upward).

The missing direction is directly detectable: with
\[
D_n=\sum_{t=1}^{n-1}\Bigl(\mathbf1\{X_{t+1}-X_t\equiv1\}-\mathbf1\{X_{t+1}-X_t\equiv-1\}\Bigr),
\]
we have \(D_n/(n-1)\to2\delta\) almost surely, whereas under the independent-uniform null \(D_n/(n-1)\to0\); hence the usual fixed-level standardized two-sided directional test is consistent for each nonzero \(\delta\).

## Assumptions and scope

States are \(\mathbb Z/3\mathbb Z\), the sample starts from a uniform state, and the successive step increments are independent with the probabilities above. Equivalently it is the specified stationary Markov chain. The sample is the **linear** word \((X_1,\ldots,X_n)\), not a circular word: there are \(n-1\) tested successive transitions. The null is independent uniform sampling, the alternative has fixed \(\delta\ne0\) independent of \(n\), and \(\alpha\) is fixed. The generalized runs statistic is precisely the scalar count and conditional-count normal standardization displayed in [1, Algorithm 2]; Pearson's statistic and Bonferroni combination follow [1, Algorithms 3–4]. The test concerns first-order marginal frequencies and the number of runs, not an omnibus test of all transition directions or all run lengths.

## Proof

Write \(Y_t=X_{t+1}-X_t\pmod3\). The transformation from \((X_1,Y_1,\ldots,Y_{n-1})\) to \((X_1,\ldots,X_n)\) is bijective. Under the specified chain the increments \(Y_t\) are independent and identically distributed, and independent of uniform \(X_1\). Under the independent-uniform null, the same bijection makes \(X_1,Y_1,\ldots,Y_{n-1}\) mutually independent and uniform on the three states. Consequently \(\mathbf1\{Y_t\ne0\}\) are independent Bernoulli variables of parameter \(2/3\) under *both* measures, proving the exact runs law.

Every entry of the transition matrix is strictly positive. By finite-state ergodicity, the three occupation frequencies satisfy \(N_j=n/3+O_{\Pr}(\sqrt n)\). For the generalized runs normalization in [1], set \(q_n=\sum_jN_j^2\), \(b_n=\sum_jN_j^3\). Its center and squared scale are
\[
\mu_n=\frac{n(n+1)-q_n}{n},\qquad
s_n^2=\frac{q_n[q_n+n(n+1)]-2nb_n-n^3}{n^2(n-1)}.
\]
From the occupation bounds, \(q_n=n^2/3+O_{\Pr}(n)\), \(b_n=n^3/9+O_{\Pr}(n^2)\), so \(\mu_n=2n/3+O_{\Pr}(1)\) and \(s_n^2=2n/9+o_{\Pr}(n)\). The exact binomial runs law and Slutsky's theorem give \((R_n-\mu_n)/s_n\Rightarrow N(0,1)\). Thus its two-sided rejection probability converges to \(\alpha/2\).

For the frequency statistic, let \(V_t=e_{X_t}-(1,1,1)^\mathsf T/3\). On the two-dimensional zero-sum subspace, the transition operator is a real skew-symmetric rotation with eigenvalues \(\pm i\sqrt3\delta\); in particular its square equals \(-3\delta^2\) times the identity. It follows by summing lag covariances (odd lags contribute zero to the symmetric covariance; even lags contribute successive powers of \(-3\delta^2\)) that the long-run covariance of \(n^{-1/2}\sum_tV_t\) is
\[
\Sigma_\delta=\frac{c_\delta}{3}\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}3\right),\qquad
c_\delta=1+2\sum_{k\ge1}(-3\delta^2)^k
=\frac{1-3\delta^2}{1+3\delta^2}.
\]
This geometric series converges absolutely. The finite-state additive-functional central limit theorem applies (alternatively, solve the finite Poisson equation to obtain bounded martingale differences and invoke the martingale CLT), yielding \(n^{-1/2}\sum_tV_t\Rightarrow N(0,\Sigma_\delta)\). Since \(H_n=3\|n^{-1/2}\sum_tV_t\|^2\), it converges to \(c_\delta\chi^2_2\).

The survival function of \(\chi^2_2\) is \(x\mapsto e^{-x/2}\). Its upper \(\alpha/2\) quantile is \(-2\log(\alpha/2)\). Therefore the second test's rejection probability converges to \((\alpha/2)^{1/c_\delta}\). The union bound proves the claimed combined-test bound, with a strict inequality because \(0<c_\delta<1\). No independence assumption between the two test statistics is needed.

Finally define \(Z_t=\mathbf1\{Y_t=1\}-\mathbf1\{Y_t=-1\}\). They are bounded and i.i.d. with \(\mathbb EZ_t=2\delta\), so the strong law gives the asserted directional consistency. Under the null \(\operatorname{Var}(Z_t)=2/3\); a null-calibrated test based on \(D_n/\sqrt{2(n-1)/3}\) therefore has asymptotic standard-normal calibration and diverges in magnitude under every fixed nonzero \(\delta\). This proves the comparison.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to enumerate all \(3^n\) state sequences for \(2\le n\le8\) at \(\delta=1/4\). It checks that the number of runs has the binomial law, the direction score has mean \((n-1)/2\), and Pearson's finite-sample mean equals the independent spectral-lag calculation \(2+(4/n)\sum_{2k<n}(n-2k)(-3\delta^2)^k\). All 68 assertions passed on the delivered program. These finite checks corroborate, but do not prove, the asymptotic assertions; those follow from the analytic argument above.

## Relationship to prior work

Ganzfried's *Nonparametric Strategy Test* [1] constructs the two-stage runs/chi-square test and combines it with Bonferroni correction; its rock–paper–scissors application motivates a concrete three-category analysis. The present result applies that displayed procedure to a stationary cyclic Markov alternative and gives an exact runs-law identity, a strict null-variance deflation for the frequency statistic, and a quantitative bound on the resulting power. The algorithms and their source do not state this cyclic alternative or power bound in the inspected treatment. Whittle's classical transition-total distribution and covariance program [2] concerns the distribution of Markov transition counts; it does not, as evidenced by its accessible abstract, resolve the behavior of this specific two-test decision procedure. Generalized run-length-process tests are different from the scalar total-run-count test here [3]. These distinctions are mathematical scope comparisons, not a claim of exhaustive historical uniqueness.

## Limitations

The result concerns the specified uniform-marginal three-state cyclic family, not all stationary Markov alternatives or every test of independence. The upper bound is not claimed to equal the combined test's exact limiting power: its two component statistics may be dependent. The chi-square asymptotic uses a finite-state Markov CLT; the exact run-count identity holds at every finite sample size. The paper [1] uses a normal approximation, so small-sample rejection probabilities are not covered by the asymptotic bound. Full historical priority is not independently established. The source paper describes the proposed procedure; the present analysis does not assert that its authors claimed universal consistency.

## References

[1] S. Ganzfried, *Nonparametric Strategy Test*, arXiv:2312.10695, first posted 2023-12-17 (version inspected: v5, 2024-10-07), especially Algorithms 2–4. https://arxiv.org/pdf/2312.10695 . Subsequently published, DOI:10.32473/flairs.38.1.138635.

[2] P. Whittle, *Some Distribution and Moment Formulae for the Markov Chain*, Journal of the Royal Statistical Society, Series B, 17(2), 235–242 (1955), DOI:10.1111/j.2517-6161.1955.tb00197.x. The available abstract was inspected, not the full paper.

[3] *Generalized Runs Tests for the IID Assumption*, earlier working manuscript accessible at https://paperzz.com/doc/7095382/generalized-runs-tests-for-the-iid-assumption . Only its publicly searchable text was inspected; its generalized run-length-process test is not the scalar test in [1].
