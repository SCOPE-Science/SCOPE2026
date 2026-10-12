# Exponential-inspection MRL profiles identify the positive lifetime law
## Finding
Let \(T\ge0\) be a lifetime with
\[
0<\operatorname{E}T<\infty,
\]
and let
\[
X_\lambda\sim\operatorname{Exp}(\lambda),
\qquad
\lambda>0,
\]
be independent of \(T\). Define the mean residual life under random exponential inspection by
\[
r_T(\lambda)
=
\operatorname{E}(T-X_\lambda\mid T>X_\lambda).
\]

Write
\[
p=\Pr(T>0)>0,
\]
let \(H\) denote the conditional distribution of \(T\) given \(T>0\), define
\[
\mu_+
=
\operatorname{E}(T\mid T>0),
\]
and let
\[
L_H(\lambda)
=
\operatorname{E}(e^{-\lambda T}\mid T>0)
\]
be the Laplace transform of the positive conditional law.

Then
\[
\boxed{
r_T(\lambda)
=
\frac{\mu_+}{1-L_H(\lambda)}
-
\frac1\lambda.
}
\]

The full profile therefore recovers
\[
\boxed{
\mu_+
=
\lim_{\lambda\to\infty}r_T(\lambda)
}
\]
and, for every \(\lambda>0\),
\[
\boxed{
L_H(\lambda)
=
1-
\frac{\mu_+}
{r_T(\lambda)+1/\lambda}.
}
\]

Since a probability law on \([0,\infty)\) is determined by its Laplace transform, the following sharp identification statement holds:
\[
\boxed{
r_{T_1}(\lambda)=r_{T_2}(\lambda)
\text{ for all }\lambda>0
\quad\Longleftrightarrow\quad
\mathcal L(T_1\mid T_1>0)
=
\mathcal L(T_2\mid T_2>0).
}
\]

Thus, if \(\Pr(T=0)=0\), the exponential-inspection MRL sensitivity curve determines the entire lifetime distribution. On the larger class of nonnegative lifetimes, its only blind spot is the mass at zero. For any fixed positive lifetime law \(H\), all mixtures
\[
(1-p_0)H+p_0\delta_0,
\qquad
0\le p_0<1,
\]
have exactly the same \(r_T(\lambda)\) curve.

The same cancellation is visible in the complete-data estimator from the 2026 source. Under exponential inspection its Appendix formulas imply
\[
\boxed{
\widehat r_n(\lambda)
=
\frac{\sum_{i=1}^n T_i}
{\sum_{i=1}^n(1-e^{-\lambda T_i})}
-
\frac1\lambda.
}
\]
A zero observation contributes neither to the numerator nor to the nonconstant denominator term, so adding or deleting zero observations leaves the entire empirical profile unchanged.

## Assumptions and scope
The lifetime is nonnegative and has finite, strictly positive mean. The inspection time is independent and exponentially distributed with rate \(\lambda>0\).

The identification theorem concerns the complete population profile
\[
\lambda\mapsto r_T(\lambda)
\]
over all positive rates. A finite collection of rate evaluations need not identify an unrestricted lifetime law.

The result distinguishes two notions that should not be conflated. The inspection-rate parameter itself is not identified from lifetime data when inspection times are latent; the 2026 source correctly treats \(\lambda\) as a sensitivity parameter. The new statement is instead that, if the whole mathematical sensitivity profile is known as a function of \(\lambda\), that profile identifies the positive part of the lifetime distribution.

No second moment is required.

## Proof
Condition on \(T=t\). Since \(X_\lambda\) is exponential,
\[
\Pr(X_\lambda<t)
=
1-e^{-\lambda t}.
\]
Therefore
\[
\Pr(T>X_\lambda)
=
\operatorname{E}(1-e^{-\lambda T}).
\]
Writing \(p=\Pr(T>0)\) and conditioning on positivity,
\[
\Pr(T>X_\lambda)
=
p\{1-L_H(\lambda)\}.
\]

For the numerator, conditional integration gives
\[
\operatorname{E}(T-X_\lambda)_+
=
\operatorname{E}
\left[
\int_0^T (T-x)\lambda e^{-\lambda x}\,dx
\right].
\]
For every \(t\ge0\),
\[
\int_0^t(t-x)\lambda e^{-\lambda x}\,dx
=
t-\frac{1-e^{-\lambda t}}{\lambda}.
\]
Hence
\[
\operatorname{E}(T-X_\lambda)_+
=
\operatorname{E}T
-
\frac{\operatorname{E}(1-e^{-\lambda T})}{\lambda}.
\]
Because
\[
\operatorname{E}T=p\mu_+
\]
and
\[
\operatorname{E}(1-e^{-\lambda T})
=
p\{1-L_H(\lambda)\},
\]
division by \(\Pr(T>X_\lambda)\) yields
\[
r_T(\lambda)
=
\frac{\mu_+}{1-L_H(\lambda)}
-
\frac1\lambda.
\]

Under \(H\), \(T>0\) almost surely. Dominated convergence gives
\[
L_H(\lambda)\to0
\qquad
(\lambda\to\infty).
\]
It follows that
\[
r_T(\lambda)\to\mu_+.
\]
Solving the preceding display for \(L_H(\lambda)\) yields the reconstruction formula.

If two profiles coincide, their limits give the same \(\mu_+\), and the reconstruction formula gives equal Laplace transforms on \((0,\infty)\). Laplace-transform uniqueness then gives equality of their conditional positive laws.

Conversely, if the conditional positive laws agree, then both \(\mu_+\) and \(L_H\) agree, so the profiles agree. The probability \(p=\Pr(T>0)\) cancels completely, proving the zero-mass nonidentifiability statement.

## Verification
The included checker uses the positive two-point law
\[
\Pr(T=1\mid T>0)=0.3,
\qquad
\Pr(T=4\mid T>0)=0.7.
\]
Its positive conditional mean is
\[
\mu_+=3.1.
\]

For several rates, the checker constructs \(r_T(\lambda)\) from the exact formula and then reconstructs
\[
L_H(\lambda)
=
0.3e^{-\lambda}+0.7e^{-4\lambda}
\]
from the profile. Agreement is checked to numerical precision.

The checker next forms zero-inflated versions having positive-mass probabilities \(0.2\), \(0.8\), and \(1\). Direct computation from the unconditional numerator and denominator gives the same \(r_T(\lambda)\) at every tested rate.

Finally, it verifies the complete-data identity for samples containing zeros and confirms that deleting those zero observations leaves the empirical profile unchanged.

The numerical checks are reproducibility aids; identification and nonidentification are proved analytically above.

## Relationship to prior work
The 2026 latent-inspection paper develops estimation and inference for
\[
\operatorname{E}(T-X\mid T>X)
\]
and treats an exponential inspection model as a practically important monitoring mechanism. It derives explicit complete-data and censored-data formulas, proves consistency and asymptotic normality, and interprets
\[
\lambda\mapsto r_T(\lambda)
\]
as a sensitivity profile across plausible monitoring intensities.

The 2025 paper of Asadi and Berred studies mean residual life at random age as a distributional functional. It gives general integral and conditional-expectation representations, connections to variability measures, and stochastic comparison results. In particular, it represents the random-age mean residual life as an average of the ordinary MRL under the conditional inspection-age distribution. It does not give the exponential-rate Laplace inversion or the zero-mass equivalence class described here.

Classical characterization work establishes that ordinary fixed-age MRL-related functions can characterize a lifetime distribution. That does not imply the present result, because the observable here is one scalar random-age MRL for each inspection rate rather than the ordinary MRL indexed by deterministic age.

Focused searches using random-age MRL, exponential inspection, Laplace-transform inversion, identification, conditional positive lifetime laws, and zero-mass aliases did not locate a covering result.

## Limitations
Knowledge of the profile at finitely many inspection rates is not enough to identify a fully nonparametric lifetime distribution.

The profile does not identify \(\Pr(T=0)\); this is an exact impossibility, not an estimation defect.

For right-censored data observed only to a finite horizon, the source itself restricts inference to an identifiable observation horizon. The population identification theorem here does not remove censoring-induced information loss.

A very recent or unindexed result could independently contain the same profile inversion.

## References
1. T. Manshi, “Semi-parametric distributional inference for mean residual life with latent random inspection,” AIMS Mathematics 11 (2026), 28502–28546. DOI: 10.3934/math.20261136.
2. M. Asadi and A. Berred, “The mean residual life at random age and its connection to variability measures,” Probability in the Engineering and Informational Sciences 39 (2025), 326–343. DOI: 10.1017/S026996482400010X.
3. R. C. Gupta and S. N. U. A. Kirmani, “Some Characterization of Distributions by Functions of Failure Rate and Mean Residual Life,” Communications in Statistics—Theory and Methods 33 (2004), 3115–3131. DOI: 10.1081/STA-200039060.
