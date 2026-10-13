# The electrode data reject the Gompertz model's exact cause–time independence
## Finding
The source assumes two independent latent Gompertz lifetimes with a common shape parameter:
\[
h_j(t)=\lambda_j e^{\theta t},
\qquad
\lambda_j>0,\quad \theta>0,\quad j=1,2.
\]
Let
\[
T=\min(X_1,X_2)
\]
be the observed failure time and let
\[
J\in\{1,2\}
\]
denote the cause attaining the minimum.

For either cause,
\[
f_{T,J=j}(t)
=
\lambda_j e^{\theta t}
\exp\!\left[
-\frac{\lambda_1+\lambda_2}{\theta}
\left(e^{\theta t}-1\right)
\right].
\]
Summing over causes gives
\[
f_T(t)
=
(\lambda_1+\lambda_2)e^{\theta t}
\exp\!\left[
-\frac{\lambda_1+\lambda_2}{\theta}
\left(e^{\theta t}-1\right)
\right].
\]
Therefore
\[
\boxed{
P(J=j\mid T=t)
=
\frac{\lambda_j}{\lambda_1+\lambda_2}
}
\]
for every \(t>0\). In particular,
\[
\boxed{J\perp T}
\]
and
\[
\boxed{
\mathcal L(T\mid J=1)
=
\mathcal L(T\mid J=2)
=
\mathcal L(T).
}
\]

The paper's cause-neutral progressive censoring does not remove this implication. Its likelihood separates the labels through
\[
\lambda_1^{D_1}\lambda_2^{D_2}
\]
while the observed-time and removal factors depend on the scales only through
\[
\lambda_1+\lambda_2.
\]
Hence, conditional on the observed failure times and the total number \(D_1\) of cause-1 failures, every placement of the \(D_1\) cause-1 labels among the failure positions has the same probability.

This produces an exact nuisance-free permutation diagnostic for the source's electrode application.

Using the 45 failures as printed in its Table 8, there are 19 Mode-E failures and 26 Mode-D failures. The Mode-E midrank sum is
\[
R_E=219,
\]
equivalently a Mann–Whitney statistic
\[
U=29.
\]
Under the common-shape model, conditioning on the 45 observed failure times and on \(D_1=19\) makes all
\[
\binom{45}{19}
=
2{,}438{,}362{,}177{,}020
\]
label assignments equally likely.

An exact dynamic-programming enumeration, retaining the tied failure time through midranks, finds
\[
44{,}812
\]
assignments whose rank-sum distance from the null mean is at least as large as the observed one. Thus the exact two-sided conditional permutation probability is
\[
\boxed{
p=
\frac{44{,}812}
{2{,}438{,}362{,}177{,}020}
=
1.8377909739\times10^{-8}.
}
\]

The source's common-shape Gompertz competing-risks model is therefore decisively rejected by the cause–time ordering in the electrode failures.

There is a second interpretive consequence. The paper separately fits distributions to the observed Mode-E and Mode-D failure times and discusses their different empirical shapes. Under the stated common-shape model, however, those two conditional failure-time distributions are exactly the same. Moreover, an observed time with label \(J=j\) is a selected minimum \(T\), not an uncensored draw from the latent marginal lifetime \(X_j\). Separate cause-wise fits therefore do not constitute goodness-of-fit checks for the latent marginal Gompertz laws used in the competing-risks construction.

## Assumptions and scope
The result concerns the source's independent two-cause Gompertz model with common shape \(\theta\).

The permutation statement conditions on the observed failure times and on the number of failures assigned to each cause. It therefore does not require estimation of \(\lambda_1\), \(\lambda_2\), or \(\theta\).

The censoring argument requires the source's cause-neutral design: removals and termination depend on observed times and the prescribed censoring scheme, not on which cause label occurred.

The exact numerical test uses the failure times and labels printed in the 2026 article's own electrode table. It does not rely on resolving discrepancies among earlier reproductions of that historical dataset.

The result does not apply to heterogeneous competing-risk models in which different causes have different time-shape functions.

## Proof
For a Gompertz latent lifetime with scale \(\lambda_j\) and common shape \(\theta\),
\[
S_j(t)
=
\exp\!\left[
-\frac{\lambda_j}{\theta}
\left(e^{\theta t}-1\right)
\right]
\]
and
\[
f_j(t)
=
\lambda_j e^{\theta t}S_j(t).
\]

Independence of \(X_1\) and \(X_2\) gives
\[
f_{T,J=1}(t)
=
f_1(t)S_2(t)
\]
and
\[
f_{T,J=2}(t)
=
f_2(t)S_1(t).
\]
Substitution yields
\[
f_{T,J=j}(t)
=
\lambda_j e^{\theta t}
\exp\!\left[
-\frac{\lambda_1+\lambda_2}{\theta}
\left(e^{\theta t}-1\right)
\right].
\]
The common time-dependent factor cancels in the conditional cause probability, proving \(J\perp T\).

For progressively censored data, each observed cause label contributes one factor \(\lambda_j\); all survival contributions from units removed alive involve
\[
S_1(t)S_2(t)
=
\exp\!\left[
-\frac{\lambda_1+\lambda_2}{\theta}
\left(e^{\theta t}-1\right)
\right].
\]
Therefore, after fixing the failure times and the counts \(D_1,D_2\), the likelihood is invariant under every permutation of the cause labels across those failure times. This proves the exact conditional randomization law.

For the electrode data, double the midranks so that all ranks are integers, including the tied time. A subset-sum dynamic program counts, for each possible doubled rank sum, how many 19-element label subsets attain that sum. The observed doubled rank sum is
\[
438,
\]
whereas the null mean doubled rank sum is
\[
874.
\]
Summing counts with absolute deviation at least
\[
436
\]
gives exactly
\[
44{,}812
\]
assignments out of
\[
\binom{45}{19}.
\]

## Verification
The bundled checker has two independent components.

First, it evaluates the two cause-specific joint subdensities and the total failure-time density at several parameter choices and times, verifying numerically that
\[
f_{T,J=j}(t)/f_T(t)
=
\lambda_j/(\lambda_1+\lambda_2)
\]
to floating-point precision.

Second, it reconstructs the 45 failure times and cause labels printed in the source, computes midranks, and performs exact integer dynamic programming over all possible 19-label rank sums. It reproduces
\[
R_E=219,\qquad
U=29,\qquad
N_{\mathrm{extreme}}=44{,}812,
\]
and the exact two-sided conditional probability above.

No asymptotic approximation or fitted parameter enters the permutation calculation.

## Relationship to prior work
The source itself derives the relative risk
\[
\pi_1=\frac{\lambda_1}{\lambda_1+\lambda_2}
\]
and the estimator
\[
\widehat\pi_1=\frac{D_1}{D_1+D_2},
\]
which are consistent with the factorization above. It does not apply the stronger consequence that the cause label is independent of the observed failure time.

A closely related common-shape Weibull competing-risks analysis explicitly states
\[
D_j\sim\operatorname{Binomial}(D,\pi_j)
\]
and simulates failure causes by assigning labels after generating failure times. This confirms that label/time separation is a standard consequence of the common proportional-hazards construction. It does not perform the source-specific electrode rank test or identify the incompatibility between the 2026 paper's cause-wise empirical separation and its common-shape Gompertz model.

The closest published-result search result concerns recovery of heterogeneous proportional hazards from unlabeled first- and second-failure marginals. That problem is different: it studies identification from unlabeled system summaries, whereas the present result uses observed cause labels to obtain an exact finite-sample model diagnostic in a specific application.

Focused searches using the exact DOI, common-shape Gompertz competing risks, cause-label independence, conditional failure-time distributions, exact permutation testing, relative risk, and the electrode application did not locate this application-level diagnostic.

## Limitations
The exact test diagnoses the common-shape proportional-hazards restriction; it does not identify which alternative competing-risks model is best.

A cause-specific-shape Gompertz model or another heterogeneous model can allow cause and observed failure time to be associated.

The source table is used exactly as printed. Earlier publications of the same historical electrode experiment do not all agree on one cause label, but moving that disputed observation between causes does not remove the extreme early/late separation; this robustness is not needed for the accepted claim.

A recent or unindexed source may have made the same source-specific diagnostic outside the material examined.

## References
1. H. N. Alqifari, “Reliability analysis for an independent Gompertz competing risks model employing improved adaptive progressive Type-Ⅱ censored data,” AIMS Mathematics 11 (2026), 26026–26076. DOI: 10.3934/math.20261043.
2. A. Elshahhat and M. Nassar, “Inference of improved adaptive progressively censored competing risks data for Weibull lifetime models,” Statistical Papers 65 (2024), 1163–1196. DOI: 10.1007/s00362-023-01417-0.
3. D. R. Cox, “The analysis of exponentially distributed life-times with two types of failure,” Journal of the Royal Statistical Society, Series B 21 (1959), 411–421. DOI: 10.1111/j.2517-6161.1959.tb00349.x.
