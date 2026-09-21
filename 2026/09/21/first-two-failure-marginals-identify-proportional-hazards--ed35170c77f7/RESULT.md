# First two unlabeled failure marginals identify heterogeneous proportional hazards

## Setting

Let \(X_1,\ldots,X_n\), \(n\ge2\), be independent component lifetimes with a common unknown proportional-hazards baseline:
\[
\Pr(X_i>t)=B(t)^{\lambda_i},\qquad \lambda_i>0,
\]
where \(B\) is a continuous strictly decreasing survival function with range \((0,1)\) on the interior of its support. Let
\[
T_1=X_{1:n},\qquad T_2=X_{2:n}
\]
be the first and second failure times, and write their marginal survival functions as \(S_1,S_2\).

Set
\[
\Lambda=\sum_{i=1}^n\lambda_i,\qquad q_i=\lambda_i/\Lambda.
\]
Only the multiset \(\{q_i\}\) can be identifiable without fixing the overall baseline scale, because replacing \((B,\lambda_i)\) by \((B^{1/c},c\lambda_i)\) leaves every component survival unchanged.

## Main theorem

The two **marginal** laws of \(T_1\) and \(T_2\) identify:

1. the unknown component count \(n\);
2. the normalized hazard multiset \(\{q_1,\ldots,q_n\}\), up to permutation;
3. the aggregate baseline survival \(B^\Lambda=S_1\).

No joint observation of \((T_1,T_2)\), component labels, or causes of failure is required.

Indeed,
\[
S_1(t)=B(t)^\Lambda,
\]
and
\[
S_2(t)=\sum_{i=1}^n B(t)^{\Lambda-\lambda_i}-(n-1)B(t)^\Lambda.
\]
Eliminating the unknown baseline through \(u=S_1(t)\) gives the baseline-free curve
\[
\boxed{
\Phi(u):=S_2\!\bigl(S_1^{-1}(u)\bigr)
=\sum_{i=1}^n u^{1-q_i}-(n-1)u,
\qquad 0<u<1.
}
\]
With \(x=-\log u\),
\[
\Phi(e^{-x})
=\sum_{i=1}^n e^{-(1-q_i)x}-(n-1)e^{-x}.
\]
This is a finite signed exponential sum. Since every \(1-q_i\) lies strictly in \((0,1)\), its representation is unique: the coefficient at exponent \(1\) is \(-(n-1)\), and the remaining exponents, counted with multiplicity, are \(1-q_i\). Thus \(n\) and the full normalized hazard multiset are identified.

Under the normalization \(\Lambda=1\), the model is therefore fully identified up to permutation: \(B=S_1\) and \(\lambda_i=q_i\).

## Exact model-class characterization

Conversely, a pair of continuous strictly decreasing survival functions \((S_1,S_2)\) arises from such an independent heterogeneous PHR system if and only if, for some integer \(n\ge2\),
\[
H(x):=S_2\!\left(S_1^{-1}(e^{-x})\right)
=\sum_{i=1}^n e^{-\alpha_i x}-(n-1)e^{-x}
\]
for exponents \(\alpha_i\in(0,1)\) satisfying
\[
\sum_{i=1}^n\alpha_i=n-1.
\]
Then \(q_i=1-\alpha_i\), \(\sum q_i=1\), and taking \(B=S_1\) yields a normalized PHR representation.

Equivalently, after grouping equal exponents, \(H\) must be a finite exponential polynomial whose positive coefficients are positive integers summing to \(n\), whose positive exponents lie in \((0,1)\), and whose sole exponent-1 term has coefficient \(-(n-1)\), with the first-moment constraint above.

## Finite local reconstruction when n is known

If \(n\) is known and \(H(x)=\Phi(e^{-x})\), then for \(r=1,\ldots,n\),
\[
H^{(r)}(0)=(-1)^r\left(\sum_{i=1}^n(1-q_i)^r-(n-1)\right).
\]
Hence the first \(n\) derivatives determine the power sums
\[
p_r:=\sum_{i=1}^n(1-q_i)^r=(n-1)+(-1)^rH^{(r)}(0).
\]
Newton's identities then recover the monic polynomial whose roots are \(1-q_i\). Thus, for known \(n\), a finite jet of the baseline-free curve already determines the normalized hazard multiset, including repeated hazards.

For example, the local curvature directly yields the hazard-concentration index:
\[
\sum_i q_i^2=1+H''(0).
\]

## Sharp insufficiency of either marginal alone

The use of both marginals is essential when the baseline is unknown.

### First failure alone

For any admissible normalized hazard vector \(q\), choosing \(B=S_1\) and \(\Lambda=1\) reproduces a prescribed first-failure survival \(S_1\). Thus \(T_1\) alone identifies neither \(n\) nor the relative hazards.

### Second failure alone

For a normalized hazard vector \(q=(q_1,\ldots,q_n)\), define
\[
\Phi_q(z)=\sum_{i=1}^n z^{1-q_i}-(n-1)z.
\]
For \(0<z<1\),
\[
\Phi_q'(z)=\sum_i(1-q_i)z^{-q_i}-(n-1)>0,
\]
because \(z^{-q_i}>1\) and \(\sum_i(1-q_i)=n-1\). Also \(\Phi_q(0)=0\) and \(\Phi_q(1)=1\). Therefore \(\Phi_q\) is a strictly increasing bijection of \([0,1]\).

Given any admissible second-failure survival \(S_2\) and **any** component count \(n\ge2\) with any positive normalized hazard vector \(q\), define
\[
B_q(t)=\Phi_q^{-1}(S_2(t)).
\]
Then \(B_q\) is a valid continuous strictly decreasing baseline survival and the resulting PHR system has exactly the prescribed \(S_2\). Thus the second-failure marginal alone also identifies neither \(n\) nor the relative hazards.

Consequently the pair \((S_1,S_2)\) gives a sharp sufficiency phenomenon: either marginal separately is completely nonidentifying for heterogeneity under an unrestricted common baseline, while the two together identify all relative component hazards and the component count.

## Example

Take three exponential components with rates \((1,2,4)\). Then
\[
S_1(t)=e^{-7t},
\]
\[
S_2(t)=e^{-6t}+e^{-5t}+e^{-3t}-2e^{-7t}.
\]
Eliminating \(t\) gives
\[
\Phi(u)=u^{6/7}+u^{5/7}+u^{3/7}-2u.
\]
The positive exponents reveal \(\{1-q_i\}=\{6/7,5/7,3/7\}\), hence \(\{q_i\}=\{1/7,2/7,4/7\}\), while the coefficient \(-2\) on \(u\) reveals \(n=3\).

## Proof of uniqueness

The only nontrivial identification step is uniqueness of a finite exponential representation. Suppose
\[
\sum_{j=1}^m c_j e^{-\beta_j x}=0\qquad(x\ge0),
\]
with distinct \(\beta_1<\cdots<\beta_m\). Multiplying by \(e^{\beta_1 x}\) and sending \(x\to\infty\) gives \(c_1=0\). Repeating recursively gives \(c_j=0\) for every \(j\). Hence two finite exponential sums agreeing on \([0,\infty)\) have the same exponents and coefficients after grouping repeated exponents. Applying this to the baseline-free curve proves the main identification claim.

## Relation to prior work

The distribution theory and stochastic comparison of heterogeneous PHR order statistics are classical and are not claimed as new. Pledger and Proschan (1971) initiated comparison results for heterogeneous order statistics and spacings; later reviews describe their PHR results and the large stochastic-order literature that followed. Zhao, Li and Balakrishnan (2009) study likelihood-ratio ordering of the second order statistic for heterogeneous exponential samples. Kochar (2022) gives dependence comparisons for order statistics and explicitly extends them to the PHR model by transforming with the cumulative baseline hazard.

Parametric inference from black-box system lifetimes is also prior art and is not claimed here. Work on masked system data estimates heterogeneous exponential component rates under richer observation schemes, and current `kofn` software demonstrates likelihood-based estimation of heterogeneous exponential component rates from system-lifetime data in fixed parametric models. These known-baseline/parametric settings differ from the unknown-baseline identification question here.

Navarro and Spizzichino (2010) study relations between order-statistic copulas and parent marginal distributions for heterogeneous samples. Recent identification work using two order statistics also exists in unrelated econometric measurement-error and auction settings. None of the checked sources supplied the baseline-elimination identity above together with the semiparametric identification/nonidentification classification.

The contribution claimed here, **to the best of our knowledge**, is the exact semiparametric statement that the two *unlabeled marginal* failure-time laws \((T_1,T_2)\) identify the unknown component count and all relative PHR multipliers under an arbitrary common baseline, together with the converse model characterization, finite-derivative reconstruction for known \(n\), and the sharp result that either marginal alone is completely nonidentifying.

## Limitations

The theorem assumes independent components, a common proportional-hazards baseline, strictly positive multipliers, and continuous strictly monotone baseline survival. It is a population-level identifiability result, not an estimator or finite-sample guarantee. Recovering closely spaced exponential exponents can be numerically ill-conditioned, so exact identification does not imply stable estimation. Component labels are not identifiable, only the multiplier multiset. Absolute hazard scale is deliberately not identifiable without normalizing the baseline. Dependence, censoring, baseline misspecification, measurement error, ties, and zero-hazard components are not treated.

The 1971 Pledger--Proschan chapter was not available for complete theorem-by-theorem inspection, and older masked-reliability or inverse-system literature may use different terminology for an equivalent specialization. This remains the principal originality risk.

## Reproducibility

`artifacts/verify_identification.py` uses only the Python standard library. It exactly reconstructs the three-component normalized hazards via Newton identities, numerically verifies the baseline-free identity, checks strict monotonicity of representative \(\Phi_q\), and reproduces the same second-failure marginal using a different component count and hazard profile by changing the unknown baseline. Expected output is in `artifacts/VERIFICATION.txt`.

## References

1. G. Pledger and F. Proschan, “Comparisons of order statistics and of spacings from heterogeneous distributions,” in *Optimizing Methods in Statistics*, 1971, pp. 89–113.
2. S. Kochar, “Stochastic Comparisons of Order Statistics and Spacings: A Review,” *International Scholarly Research Notices* (2012), 839473. https://doi.org/10.5402/2012/839473
3. P. Zhao, X. Li and N. Balakrishnan, “Likelihood ratio order of the second order statistic from independent heterogeneous exponential random variables,” *Journal of Multivariate Analysis* 100 (2009), 952–962. https://doi.org/10.1016/j.jmva.2008.09.010
4. S. Kochar, “Dependence comparisons of order statistics in the proportional hazards model,” *Probability in the Engineering and Informational Sciences* 37 (2023), 730–736. https://doi.org/10.1017/S0269964822000146
5. Z. Tan, “Estimation of exponential component reliability from uncertain life data in series and parallel systems,” *Reliability Engineering & System Safety* 92 (2007), 223–230. https://doi.org/10.1016/j.ress.2005.12.010
6. J. Navarro and F. Spizzichino, “On the relationships between copulas of order statistics and marginal distributions,” *Statistics & Probability Letters* 80 (2010), 473–479. https://doi.org/10.1016/j.spl.2009.11.025
7. `kofn` package documentation, “Exponential Parallel Systems: Closed-Form MLE via Inclusion-Exclusion,” documentation built 2026-06-19. https://rdrr.io/cran/kofn/f/vignettes/exponential-parallel.Rmd
