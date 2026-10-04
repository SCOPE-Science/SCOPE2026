# Exact coincidence of jackknife+ and full conformal for sample-mean prediction
## Finding
For \(n\ge2\), let the fitted predictor ignore covariates and return the sample mean. Use absolute residuals and the finite-sample quantile convention of Barber, Candès, Ramdas, and Tibshirani. Then jackknife+ and full conformal prediction are exactly the same set for every realized training sample and every \(\alpha\in(0,1)\).

Write
\[
\bar Y=\frac1n\sum_{{i=1}}^nY_i,\qquad d_i=Y_i-\bar Y,\qquad c_n=\frac{{n+1}}{{n-1}},
\]
and set
\[
j=\lfloor\alpha(n+1)\rfloor,\qquad k=\lceil(1-\alpha)(n+1)\rceil.
\]
For each training observation define
\[
\ell_i=\bar Y+\min\{{d_i,-c_nd_i\}},\qquad
u_i=\bar Y+\max\{{d_i,-c_nd_i\}}.
\]
When \(j\ge1\) and \(k\le n\), both procedures return
\[
C_{{n,\alpha}}=[\ell_{{(j)}},u_{{(k)}}],
\]
where parentheses denote order statistics. If \(j=0\), equivalently \(k=n+1\), the common set is \(\mathbb R\), matching the source convention that the upper empirical quantile is infinite when its requested order exceeds \(n\).

Therefore exchangeability gives the strengthened guarantee
\[
\Pr\{{Y_{{n+1}}\in C_{{n,\alpha}}\}}\ge1-\alpha.
\]
If the \(n+1\) absolute residuals from the augmented sample mean are almost surely distinct, then the rank is uniform and
\[
\Pr\{{Y_{{n+1}}\in C_{{n,\alpha}}\}}=
\frac{{\lceil(1-\alpha)(n+1)\rceil}}{{n+1}}.
\]
For example, at \(n=20\) and \(\alpha=0.1\), the exact distinct-residual coverage is \(19/21\approx0.9047619\), whereas the generic jackknife+ guarantee stated for arbitrary symmetric algorithms is only \(1-2\alpha=0.8\).

## Assumptions and scope
The prediction algorithm is intercept-only least squares: on any nonempty sample it returns the sample mean, independent of the covariate. The conformity score is absolute residual error. The definitions of jackknife+ and full conformal, including the \(n+1\) finite-sample quantile correction, are exactly those in Barber et al. The deterministic equality of prediction sets needs no distributional assumption. Exchangeability is used only for the coverage statement. Exact grid coverage additionally requires almost-surely distinct augmented absolute residuals; iid responses having a joint density are a sufficient condition.

No claim is made for general linear, ridge, nonlinear, or covariate-dependent regression algorithms. The result is about this natural one-parameter location submodel and the specific absolute-residual conformity score.

## Proof
Let \(\widehat\mu_{{-i}}\) be the leave-one-out mean. Since \(Y_i=\bar Y+d_i\),
\[
\widehat\mu_{{-i}}=\bar Y-\frac{{d_i}}{{n-1}},\qquad
R_i^{{\mathrm{{LOO}}}}=\left|Y_i-\widehat\mu_{{-i}}\right|=
\frac{{n}}{{n-1}}|d_i|.
\]
Hence
\[
\widehat\mu_{{-i}}-R_i^{{\mathrm{{LOO}}}}=\ell_i,
\qquad
\widehat\mu_{{-i}}+R_i^{{\mathrm{{LOO}}}}=u_i.
\]
The jackknife+ definition therefore gives lower endpoint \(\ell_{{(j)}}\) and upper endpoint \(u_{{(k)}}\), with the stated infinite-endpoint convention when \(j=0\).

Now test a candidate response \(y\), and write \(x=y-\bar Y\). The mean of the augmented \(n+1\) observations is
\[
\widehat\mu^y=\bar Y+\frac{x}{n+1}.
\]
The candidate residual and the \(i\)-th training residual are
\[
r_*(y)=\frac{n}{n+1}|x|,
\qquad
r_i(y)=\left|d_i-\frac{x}{n+1}\right|.
\]
Multiplying the squared-residual difference by \((n+1)^2\) gives the exact factorization
\[
((n+1)d_i-x)^2-n^2x^2
=(n+1)(n-1)(d_i-x)(x+c_nd_i).
\]
Thus \(r_*(y)\le r_i(y)\) if and only if
\[
x\in[\min\{{d_i,-c_nd_i\}},\max\{{d_i,-c_nd_i\}}],
\]
or equivalently \(y\in[\ell_i,u_i]\).

Full conformal includes \(y\) exactly when the test residual does not exceed the \(k\)-th smallest training residual. For \(k\le n\), this is equivalent to at least
\[
n-k+1=\lfloor\alpha(n+1)\rfloor=j
\]
of the intervals \([\ell_i,u_i]\) containing \(y\). Every such interval contains \(\bar Y\). Consequently the set of points covered by at least \(j\) of them is the single interval
\[
[\ell_{{(j)}},u_{{(n-j+1)}}].
\]
The complementary integer identity \(n-j+1=k\) completes the samplewise equality with jackknife+. If \(j=0\), full conformal accepts every \(y\), again agreeing with jackknife+.

For coverage, exchangeability of the augmented sample gives the usual full-conformal lower bound. If all \(n+1\) augmented absolute residuals are distinct, the test residual's rank is uniform on \(\{{1,\ldots,n+1\}}\). The common set contains the test point exactly for ranks at most \(k\), yielding exact probability \(k/(n+1)\).

## Verification
The accompanying exact-arithmetic verifier checks the leave-one-out endpoint identities, the residual-difference factorization, and direct full-conformal membership against jackknife+ membership on every cell separated by all algebraic breakpoints for several rational samples and levels. It also checks the low-\(\alpha\) infinite-interval convention and exhausts a five-point exchangeable orbit with distinct augmented residuals, obtaining the predicted rank count. The verifier reports `VERIFY_OK`.

The proof itself is symbolic and does not depend on numerical experiments. Computation is used only as a replayable consistency check.

## Relationship to prior work
Barber, Candès, Ramdas, and Tibshirani define jackknife+ and full conformal separately. Their jackknife+ interval uses leave-one-out predictions shifted by leave-one-out residuals, while full conformal augments the data by each candidate response and compares its residual with the training residual quantile. Their general table gives jackknife+ the assumption-free guarantee \(1-2\alpha\) and full conformal the guarantee \(1-\alpha\), and discusses full conformal as typically much more computationally expensive.

The exact identity above is a special structural property of the sample-mean predictor: the candidate-versus-training residual comparisons factor into intervals that all share the training mean. The inspected primary source does not state a sample-mean, intercept-only, or location-model specialization. Later literature on relationships among conformal, cross-conformal, and jackknife methods discusses generic or asymptotic equivalences; that does not imply this finite-sample deterministic identity or the exact coverage grid.

## Limitations
The equality is not asserted beyond intercept-only least squares with absolute residuals. Different conformity scores can destroy the common-center interval structure, and covariate-dependent fits generally need not admit the factorization used here. The strengthened coverage remains marginal under exchangeability, not conditional on a fixed training sample. Exact grid coverage requires no residual ties; with ties the deterministic equality still holds but only the standard conservative coverage conclusion is asserted.

A literature search cannot prove absolute novelty. The strongest residual risk is an unlocated folklore or specialized conformal-prediction note deriving the same intercept-only identity. No such statement appeared in the inspected direct paper or in searches for the same objects, aliases, and equivalence language.

## References
1. R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani, “Predictive inference with the jackknife+,” *Annals of Statistics* 49(1), 486–507 (2021). arXiv:1905.02928; DOI:10.1214/20-AOS1965.
2. J. Lei, M. G'Sell, A. Rinaldo, R. J. Tibshirani, and L. Wasserman, “Distribution-Free Predictive Inference for Regression,” *Journal of the American Statistical Association* 113(523), 1094–1111 (2018). arXiv:1604.04173; DOI:10.1080/01621459.2017.1307116.
3. N. Amann, “Conditional validity and a fast approximation formula of full conformal prediction sets,” arXiv:2508.05272 (2025).
