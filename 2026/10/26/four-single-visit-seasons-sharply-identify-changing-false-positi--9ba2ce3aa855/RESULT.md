# Four single-visit seasons sharply identify changing false-positive occupancy

## Finding

**Theorem (sharp four-season identification).** A stationary, irreducible binary occupancy process with nonzero temporal memory and a freely varying, informative binary observation channel in every season is uniquely determined by the joint law of **four** one-visit observations. Four means, five pair covariances and one centered triple moment give an explicit inverse for stationary occupancy, colonization, extinction, and **all eight** season-specific false-positive and true-positive probabilities. Three consecutive seasons do **not** identify the self-review, even from their **entire** observed joint distribution. These claims hold at every strictly admissible parameter vector, including negative temporal memory and stationary occupancy one half.

## Assumptions and scope

At each independently sampled site, let \(Z_t\in\{0,1\}\) denote true occupancy at seasons \(t=0,1,2,3\). It is a stationary, time-homogeneous, two-state Markov chain with
\[
\gamma=\Pr(Z_{t+1}=1\mid Z_t=0),\qquad
\varepsilon=\Pr(Z_{t+1}=0\mid Z_t=1),\qquad
0<\gamma,\varepsilon<1,\quad \gamma+\varepsilon\ne1.
\]
Write \(\pi=\gamma/(\gamma+\varepsilon)\) and \(\lambda=1-\gamma-\varepsilon\), so \(0<\pi<1\), \(-1<\lambda<1\), and \(\lambda\ne0\). There is one observation \(Y_t\in\{0,1\}\) per site per season. Conditional on the complete latent path, observations at distinct seasons are independent, and
\[
f_t=\Pr(Y_t=1\mid Z_t=0),\qquad
d_t=\Pr(Y_t=1\mid Z_t=1),\qquad 0<f_t<d_t<1.
\]
The \(f_t\) and \(d_t\) may be completely different from one season to the next. The strict ordering \(d_t>f_t\) is the scientifically meaningful calibration that fixes the occupancy-state label. Identifiability refers to the population joint distribution across indefinitely many independent sites, not estimation from one four-bit record.

Define the observed means, pair covariances, and centered triple moment by
\[
m_t=\mathbb E[Y_t],\quad c_{ij}=\mathbb E[(Y_i-m_i)(Y_j-m_j)],\quad
u_{012}=\mathbb E[(Y_0-m_0)(Y_1-m_1)(Y_2-m_2)].
\]
Only \(c_{01},c_{02},c_{12},c_{13},c_{23}\) are required; the other pair covariance and all fourth-order moments are unnecessary for reconstruction.

## Proof

Put \(A=\pi(1-\pi)\) and \(\delta_t=d_t-f_t>0\). Centering the latent state, \(W_t=Z_t-\pi\), stationarity and the Markov law give
\[
\mathbb E[W_j\mid Z_i]=\lambda^{j-i}W_i\quad(j>i),\qquad
W_t^2=A+(1-2\pi)W_t.
\]
Consequently
\[
\operatorname{Cov}(Z_i,Z_j)=A\lambda^{j-i},\qquad
\mathbb E[W_iW_jW_k]=A(1-2\pi)\lambda^{k-i}\quad(i<j<k).
\]
Because \(\mathbb E[Y_t\mid Z_t]=f_t+\delta_t Z_t\) and the seasonal observation noises are conditionally independent,
\[
\boxed{m_t=f_t+\pi\delta_t,\qquad
c_{ij}=A\delta_i\delta_j\lambda^{j-i},\qquad
\nu_{012}=A(1-2\pi)\delta_0\delta_1\delta_2\lambda^2.}
\]
Every denominator below is nonzero under the strict assumptions. Define the observable quantities
\[
R=\frac{\nu_{012}^{\,2}}{c_{01}c_{12}c_{02}},\quad
\widehat A=\frac1{4+R},\quad
\widehat\pi=\frac{1-\operatorname{sgn}(\nu_{012})\sqrt{1-4\widehat A}}2,
\]
where \(\operatorname{sgn}(0)=0\), and
\[
\widehat\lambda=\operatorname{sgn}(c_{01})
\sqrt{\frac{c_{02}c_{13}}{c_{01}c_{23}}},\qquad
\widehat\delta_1=\sqrt{\frac{c_{01}c_{12}}{\widehat A c_{02}}}.
\]
Recover the three other channel contrasts by
\[
\widehat\delta_0=\frac{c_{01}}{\widehat A\widehat\delta_1\widehat\lambda},\quad
\widehat\delta_2=\frac{c_{12}}{\widehat A\widehat\delta_1\widehat\lambda},\quad
\widehat\delta_3=\frac{c_{13}}{\widehat A\widehat\delta_1\widehat\lambda^2}.
\]
Finally
\[
\boxed{\widehat f_t=m_t-\widehat\pi\widehat\delta_t,\quad
\widehat d_t=\widehat f_t+\widehat\delta_t,\quad
\widehat\gamma=\widehat\pi(1-\widehat\lambda),\quad
\widehat\varepsilon=(1-\widehat\pi)(1-\widehat\lambda).}
\]
Indeed \(R=(1-2\pi)^2/A=1/A-4\). Since \(\delta_t>0\) and \(\lambda^2>0\), the sign of the triple moment is the sign of \(1-2\pi\), while the sign of \(c_{01}\) is the sign of \(\lambda\). Therefore the chosen square-root branches are forced, even when \(\pi=1/2\), when the triple moment vanishes. Substituting the covariance identities gives \(\widehat\lambda=\lambda\), \(\widehat\delta_1=\delta_1\), and all remaining quantities exactly. Thus any two strictly admissible parameter vectors yielding the same four-season observation law are identical.

**Three-season impossibility (every interior point).** Retain seasons \(0,1,2\) of any admissible model. Select \(\lambda'\ne\lambda\), arbitrarily close to \(\lambda\) with the same sign. Keep \(\pi'=\pi\) and set
\[
\delta'_0=\delta_0\frac\lambda{\lambda'},\qquad
\delta'_1=\delta_1,\qquad
\delta'_2=\delta_2\frac\lambda{\lambda'},\qquad
f'_t=m_t-\pi\delta'_t,\qquad d'_t=f'_t+\delta'_t.
\]
Define \(\gamma'=\pi(1-\lambda')\) and \(\varepsilon'=(1-\pi)(1-\lambda')\). Strictness and continuity ensure every nearby \(\lambda'\) produces valid transition and observation probabilities. Direct substitution into the moment identities preserves all three means, all three pair covariances, and the centered triple moment: in each case the powers of \(\lambda'\) cancel against the adjusted contrasts. These seven quantities determine all seven nontrivial probabilities of a three-bit law by inclusion-exclusion. Hence two distinct admissible models have the **same full three-season law**, and a continuous one-parameter family does so near every interior point. Two or fewer seasons cannot identify either, by marginalization. This proves sharp minimality.

## Verification

Run `python verification.py` in a directory containing `verification.py`; the standard-library-only script writes `certificate.json` with deterministic exact rational results. The packaged certificate was generated by this script and checked against its regeneration. All \(16\) observed outcomes were enumerated for each of four parameter choices \((\pi,\lambda)\): \((2/5,1/2)\), \((3/5,-1/3)\), \((1/2,2/5)\), and \((1/3,-1/4)\), using \(f=(1/10,1/8,1/6,1/12)\) and \(d=(4/5,3/4,5/6,2/3)\). Each reconstructed exactly. A distinct three-season parameter vector with \(\pi=2/5\), \(\lambda=3/5\), \(f=(11/75,1/8,19/90)\), \(d=(73/100,3/4,23/30)\) exactly reproduces all eight observation-history probabilities from the original \(\lambda=1/2\) model. Arithmetic uses `fractions.Fraction`; no floating-point comparisons occur. Finite checks are corroboration; the general proof above is analytical.

## Relationship to prior work

MacKenzie et al. (2003) develop dynamic occupancy and colonization/extinction inference with robust within-season repeated detection visits, rather than one visit and freely varying false-positive errors. Royle and Link (2006) introduce both false-positive and false-negative occupancy errors for an effectively closed occupancy state with identically distributed replicate observations; their full model and label ordering provide foundational motivation but no four-season time-varying inversion. Fukaya and Royle (2013) handle temporal ecological state transitions and observation error with modeled error rates, not an unconstrained distinct channel in each of four seasons and this explicit identification boundary. Ferguson et al. (2015) use confirmed records or informative priors for heterogeneous misclassification; Doser and Stoudt (2024) study single-visit designs with false positives excluded. Liu and Culpepper (2025) prove identifiability conditions for broader heterogeneous hidden Markov models; their stated sufficient conditions for general emission matrices require a neighboring repeated emission matrix, which is not imposed here. Thus the present claim is a specialized exact theorem for a stationary *binary* latent process under informative seasonal channels; it does not purport to solve the general heterogeneous HMM problem.

## Limitations

Stationarity, homogeneous latent transition probabilities, strict \(d_t>f_t\), conditional independence, and \(\lambda\ne0\) are essential to this theorem. If \(\lambda=0\), the latent states are independent over time and the observations are independent Bernoulli variables, so freely varying channels prevent identification regardless of the number of seasons. At boundary emission channels with \(d_t=f_t\), the required nonzero covariance divisions fail. Four seasons establish structural population-level identification only; estimation with finitely many independent sites can be arbitrarily ill-conditioned when temporal memory or the channel contrasts approach zero. No confidence intervals, robust finite-sample procedure, nonstationary extension, or claim of empirical applicability without diagnostics is established. Older identifiability results under alternate HMM parameterizations remain a bibliographic comparison risk pending independent literature review.

## References

1. MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G., and Franklin, A. B. (2003). *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*. Ecology 84, 2200–2207. DOI: 10.1890/02-3090 (first published 2003-08-01).
2. Royle, J. A. and Link, W. A. (2006). *Generalized site occupancy models allowing for false positive and false negative errors*. Ecology 87, 835–841. DOI: 10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2. Open full text: https://www.uvm.edu/~tdonovan/Occupancy%20Exercises/Exercise12/Royle_Link_2006.pdf.
3. Fukaya, K. and Royle, J. A. (2013). *Markov models for community dynamics allowing for observation error*. Ecology 94, 2670–2677. DOI: 10.1890/12-1540.1.
4. Ferguson, P. F. B., Conroy, M. J., and Hepinstall-Cymerman, J. (2015). *Occupancy models for data with false positive and false negative errors and heterogeneity across sites and surveys*. Methods in Ecology and Evolution 6, 1395–1406. DOI: 10.1111/2041-210X.12442.
5. Doser, J. W. and Stoudt, S. (2024; first online 2023-12-26). *“Fractional replication” in single-visit multi-season occupancy models: Impacts of spatiotemporal autocorrelation on identifiability*. Methods in Ecology and Evolution 15, 358–372. DOI: 10.1111/2041-210X.14275.
6. Liu, Y. and Culpepper, S. (2025). *Designing Learning Intervention Studies: Identifiability of Heterogeneous Hidden Markov Models*. Psychometrika 90, 1258–1283. DOI: 10.1017/psy.2025.10024 (open full text).
