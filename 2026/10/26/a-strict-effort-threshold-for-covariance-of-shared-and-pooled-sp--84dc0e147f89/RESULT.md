# A strict effort threshold for covariance of shared and pooled species richness

## Finding

Take two independent surveys, each containing exactly \(n\ge1\) independent individuals sampled with replacement from a community of \(m\ge2\) equally abundant species. Let \(A\) and \(B\) be the sets of species detected by the respective surveys. Define shared richness \(S=|A\cap B|\) and pooled richness \(U=|A\cup B|\). Write
\[
t=\frac{m-1}{m},\qquad s=\frac{m-2}{m-1}.
\]
Then the covariance is exactly
\[
\boxed{\operatorname{Cov}(S,U)=m^2t^{2n}\big[(1-t^n)^2-t(1-s^n)^2\big].}
\tag{1}
\]

For every integer \(m\ge2\), the covariance is **strictly negative for sufficiently small positive integer survey lengths**, is **strictly positive for sufficiently large lengths**, and **changes sign exactly once** as \(n\) increases through the positive integers. It never vanishes. Precisely, define
\[
n_*(m)=\min\left\{n\in\mathbb Z_{\ge1}:\frac{1-t^n}{1-s^n}>\sqrt t\right\}.
\tag{2}
\]
The set is nonempty, \(n_*(m)\ge2\), and
\[
\boxed{\operatorname{Cov}(S,U)<0\quad(1\le n<n_*(m)),\qquad
\operatorname{Cov}(S,U)>0\quad(n\ge n_*(m)).}
\tag{3}
\]
The sharp large-community threshold satisfies
\[
\boxed{\lim_{m\to\infty}\frac{n_*(m)}m=\alpha=1.2564312086\ldots,}
\tag{4}
\]
where \(\alpha\) is the unique strictly positive solution of \(e^\alpha=1+2\alpha\).

The exact first-positive lengths at \(m=2,3,4,5,6,10\) are respectively \(2,4,5,6,8,13\). In particular, at \(m=2\) the covariance moves from \(-1/4\) for one observation per survey to \(1/64\) for two observations per survey, without changing the species distribution.

## Assumptions and scope

Each of the \(2n\) individuals is drawn independently with replacement from exactly \(m\) species of common probability \(1/m\). Surveys have equal, fixed, positive integer lengths. The sets \(A,B\) forget within-survey multiplicities but remember species identities. Covariance is under the joint repeated-sampling probability law; it is not a conditional covariance given the individual observed richness counts. The conclusion is about the unnormalised overlap count \(S\) and the unnormalised pooled count \(U\), not about the random Jaccard ratio \(S/U\).

The parameter \(s\) is zero when \(m=2\); all powers of \(s\) in the result have strictly positive exponents. No asymptotic or continuous approximation is needed for (1)--(3).

## Proof

For each species \(i\) let \(X_i\) indicate its presence in the first survey and \(Y_i\) its presence in the second survey. Put
\[
S_i=X_iY_i,\qquad U_i=X_i+Y_i-X_iY_i.
\]
Then \(S=\sum_i S_i\) and \(U=\sum_i U_i\). Define
\[
a=t^n=\Pr(X_i=0),\qquad b=\left(\frac{m-2}{m}\right)^n=\Pr(X_i=X_j=0),\quad i\ne j.
\]
Because the two surveys are independent, \(\mathbb E S_i=(1-a)^2\) and \(\mathbb E U_i=1-a^2\).

On a single species, \(S_iU_i=S_i\), so
\[
\operatorname{Cov}(S_i,U_i)=a^2(1-a)^2.
\tag{5}
\]
For distinct species \(i\ne j\), the event that species \(i\) occurs in a given survey while species \(j\) is absent has probability \(a-b\). Therefore, again using independence between surveys,
\[
\begin{aligned}
\mathbb E(S_iU_j)&=\mathbb E S_i-\Pr(S_i=1,U_j=0)\\
&=(1-a)^2-(a-b)^2.
\end{aligned}
\]
Subtracting \(\mathbb E S_i\,\mathbb E U_j=(1-a)^2(1-a^2)\) gives
\[
\operatorname{Cov}(S_i,U_j)=a^2(1-a)^2-(a-b)^2.
\tag{6}
\]
Summing the \(m\) equal diagonal covariances and \(m(m-1)\) equal off-diagonal covariances yields
\[
\operatorname{Cov}(S,U)=m^2a^2(1-a)^2-m(m-1)(a-b)^2.
\tag{7}
\]
The sign competition also has a conditional ecological interpretation. Let \(K_A=|A|\). Conditional on the first survey, the shared count comes from detections in \(A\), while new contributions to pooled richness come from detections outside \(A\). Thus
\[
\operatorname{Cov}(\mathbb E[S\mid A],\mathbb E[U\mid A])=a(1-a)\operatorname{Var}(K_A)>0,
\]
whenever \(K_A\) is nondegenerate, whereas
\[
\mathbb E[\operatorname{Cov}(S,U\mid A)]=(b-a^2)\,\mathbb E[K_A(m-K_A)]\le0.
\]
The latter term is nonpositive because the presence indicators of different species within one survey have negative covariance \(b-a^2<0\). The exact total covariance is the sum of these opposing components; changing effort changes which dominates.

Now \(b/a=s^n\), hence (7) is (1). Since the prefactor in (1) is strictly positive, its sign is the sign of
\[
R_n^2-t,\qquad R_n=\frac{1-t^n}{1-s^n}>0.
\tag{8}
\]

We show that \(R_x\) is strictly increasing for every real \(x>0\). For \(m=2\), \(s=0\) and \(R_x=1-2^{-x}\), which is strictly increasing. For \(m\ge3\), write \(t=e^{-a_0}\), \(s=e^{-b_0}\) with \(0<a_0<b_0\). Differentiating gives
\[
\frac{d}{dx}\log R_x=\frac{a_0}{e^{a_0x}-1}-\frac{b_0}{e^{b_0x}-1}>0.
\tag{9}
\]
The strict inequality follows because for every fixed \(x>0\), the function \(z\mapsto z/(e^{xz}-1)\) is strictly decreasing for \(z>0\): its numerator after differentiation is \(e^{xz}-1-xz e^{xz}<0\), equivalently \(1-e^{-xz}<xz\). Thus \(R_x\) increases strictly.

At \(x=1\) the ratio equals \(R_1=t\), so \(R_1<\sqrt t\). As \(x\to\infty\), both powers \(t^x,s^x\) vanish and \(R_x\to1>\sqrt t\). Hence there is a unique real crossing, and the integer signs have at most one transition and at least one of each sign. Equality at an integer \(n\) would imply \(R_n=\sqrt t\). But \(R_n\) is rational, while \(\sqrt{(m-1)/m}\) is irrational for every integer \(m\ge2\): the reduced consecutive numerator and denominator cannot both be perfect squares, since consecutive nonnegative squares with difference one are only zero and one. Therefore no integer yields covariance zero. This proves (2)--(3), including strictness.

Finally fix any constant \(c>0\), and take \(n=\lfloor cm\rfloor\) as \(m\to\infty\). Elementary expansions for \(t=1-1/m\) and \(s=1-1/(m-1)\) give
\[
R_n=1-\frac{c}{m(e^c-1)}+O_c(m^{-2}),\qquad
\sqrt t=1-\frac1{2m}+O(m^{-2}).
\tag{10}
\]
Thus, for all sufficiently large \(m\), the covariance at \(n=\lfloor cm\rfloor\) is negative when \(e^c<1+2c\), and positive when \(e^c>1+2c\). The strictly convex function \(e^c-1-2c\) starts at zero with negative derivative and diverges to infinity; it therefore has exactly one positive zero \(\alpha\). For any \(0<c_-<\alpha<c_+\), monotonicity brackets \(n_*(m)\) between \(\lfloor c_-m\rfloor\) and \(\lfloor c_+m\rfloor\), up to an irrelevant unit offset for all sufficiently large \(m\). Letting \(c_-\uparrow\alpha\) and \(c_+\downarrow\alpha\) establishes (4).

## Verification

Run `python3 artifacts/verify_overlap.py` using Python 3.8 or later from the package root. The checker builds exact histograms of detected-species subsets by enumerating every ordered single-survey sequence, then evaluates the two-survey product distribution exactly. It calculates covariance directly from the first and mixed moments of \(S\) and \(U\), without using (1) for that part. It compares direct enumerations with (1) for all \(2\le m\le6\), \(1\le n\le5\): 25 independent exact rational matches. A separate grid checks formula (1), the ratio test, the lack of integer zeros, and unique strict sign transitions for all \(2\le m\le50\), through ten lengths beyond the first positive one. Four small values are asserted exactly. `artifacts/VERIFICATION.txt` contains output from executing this packaged checker.

These bounded computations neither prove strict monotonicity for every community size nor establish the asymptotic constant; those are analytic conclusions above.

## Relationship to prior work

Chao, Chazdon, Colwell, and Shen (2005, first public online date 2004-12-17) formalise shared versus unique observed species and the incidence Jaccard index based on their ratio. Their full text develops similarity measures and estimators for potentially unequal, undersampled ecological assemblages; it does not state the covariance (1) or the strict effort transition (3). Colwell and collaborators (2012, first online 2012-01-12) derive means and unconditional variances of individual species-richness rarefaction statistics in multinomial and related models. Their inspected treatment addresses one-sample richness and comparisons of estimation curves, not the cross-covariance of intersection and union counts from independent equal-source surveys.

Related finite occupancy identities imply the elementary absent-species probabilities used in this proof. A published study entitled *A one-switch covariance law for occupancy richness and frequency counts* concerns \(\operatorname{Cov}(K,K_r)\) within a single occupancy experiment, where \(K_r\) counts species observed exactly \(r\) times; its sign switch is across frequency class \(r\), not across effort \(n\) in two independent surveys. The published results on consecutive species-discovery indicators and the precision matrix of occupied-box indicators likewise concern different observables. No claim is made that the elementary indicator formula itself is outside classical occupancy theory; the comparison concerns the complete sign transition and the sharp scaling of its location for \(\operatorname{Cov}(S,U)\).

## Limitations

The equal-abundance and independent with-replacement assumptions are essential. With unequal species probabilities, different species have different empty probabilities and the single scalar comparison (8) no longer follows. Dependence between the two surveys, shared finite sampling without replacement, unequal effort lengths, or imperfect detection are not covered. Nothing here establishes the covariance sign or monotonicity of a Jaccard ratio, nor the inferential precision attainable from finite ecological replicates. Covariance approaches zero when exhaustive sampling makes both richness measurements nearly deterministic. The main remaining originality risk is an equivalent formula in older occupancy and two-sample richness literature under other terminology; a negative literature search is not a proof of novelty.

## References

1. A. Chao, R. L. Chazdon, R. K. Colwell, and T.-J. Shen, “A new statistical approach for assessing similarity of species composition with incidence and abundance data,” *Ecology Letters* 8 (2005), 148–159, DOI 10.1111/j.1461-0248.2004.00707.x. First online 2004-12-17. Full author-hosted text: https://www.robertkcolwell.org/publications/7597.pdf.
2. R. K. Colwell, A. Chao, N. J. Gotelli, S.-Y. Lin, C. X. Mao, R. L. Chazdon, and J. T. Longino, “Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages,” *Journal of Plant Ecology* 5 (2012), 3–21, DOI 10.1093/jpe/rtr044. First online 2012-01-12. Author-hosted text at https://www.robertkcolwell.org/publications/6855-models-and-estimators-linking-individual-based-and-sample-based-rarefaction-extrapolation-and-comparison-of-assemblages.
3. “A one-switch covariance law for occupancy richness and frequency counts,” public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
4. “Exact missing-mass covariance identity and sign reversal for successive species discoveries,” public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-successive-species-discovery-covariance-missing-mass--4b975bda1dac.
5. “Occupied-box indicators have a strictly positive precision matrix,” public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-occupied-box-indicators-have-a-strictly-positive-precision-matri--0606274d4166.
