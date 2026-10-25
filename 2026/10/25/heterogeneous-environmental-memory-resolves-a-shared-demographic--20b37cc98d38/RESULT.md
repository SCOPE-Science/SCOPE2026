# Heterogeneous environmental memory resolves a shared demographic-filter ambiguity

## Finding
Consider two stationary log-abundance deviations with a shared demographic relaxation coefficient and site-specific, unobserved autoregressive environmental forcing. For each site alone, the full Gaussian abundance law is unchanged when its demographic and environmental coefficients are interchanged. **Two sites with different environmental coefficients nevertheless identify all demographic, environmental, and innovation-covariance parameters from their three within-site autocovariances at lags \(0,1,2\) and a single contemporaneous cross covariance.** The proof is constructive and includes repeated-root cases.

Conversely, when both environmental coefficients are equal but different from the demographic coefficient, simultaneous interchange of those two coefficients preserves the *entire joint Gaussian process law*: not even arbitrarily many censuses can distinguish the two mechanisms. In the unequal-environment regime, within-site lags \(0,1\), even supplemented with the contemporaneous cross covariance, do not identify the parameters locally when the innovation covariance matrix is strictly positive definite. Thus lag two is sharp for this specified collection of stationary moments; no necessity claim is made when additional cross-lag moments are provided.

## Assumptions and scope
For integer census times \(t\), let \(i\in\{1,2\}\), and consider the causal stationary solution of
\[
 X_{i,t}=\lambda X_{i,t-1}+E_{i,t},\qquad
 E_{i,t}=\alpha_i E_{i,t-1}+\xi_{i,t}.
\]
The coefficient \(0<\lambda<1\) is common, \(0<\alpha_i<1\), and the innovations \((\xi_{1,t},\xi_{2,t})\) are independent across time, centered jointly Gaussian with covariance matrix
\[
\Sigma=\begin{pmatrix}\sigma_1^2&\tau\\\tau&\sigma_2^2\end{pmatrix},\qquad
\sigma_i^2>0,\quad |\tau|<\sigma_1\sigma_2.
\]
Cross-site innovation correlation is allowed; there is no dispersal. The measured \(X_{i,t}\) are exact log-abundance deviations without observation error. Define \(\gamma_i(k)=\operatorname{Cov}(X_{i,t},X_{i,t-k})\), \(k=0,1,2\), and \(C=\operatorname{Cov}(X_{1,t},X_{2,t})\). Statements concern population moments, not finite-sample estimators. Gaussianity is needed for the full-law impossibility statement, not for second-moment inversion.

## Proof
**Step 1: the two hidden filters commute.** Applying the two one-step backshift factors \(L\) to each series gives
\[
(1-\lambda L)(1-\alpha_i L)X_{i,t}=\xi_{i,t}.
\]
Hence \(X_{i,t}\) obeys the stationary autoregression
\[
X_{i,t}=(\lambda+\alpha_i)X_{i,t-1}-\lambda\alpha_i X_{i,t-2}+\xi_{i,t}.
\]
The full univariate Gaussian law depends on its two poles through the *unordered* multiset \(\{\lambda,\alpha_i\}\) and the innovation variance. Exchanging the two poles is observationally invisible.

**Step 2: two lag equations recover each unordered pole pair.** Write \(r_i=\gamma_i(1)/\gamma_i(0)\) and \(q_i=\gamma_i(2)/\gamma_i(0)\). The Yule--Walker identities, including the lag-one equation, give
\[
r_i=\frac{\lambda+\alpha_i}{1+\lambda\alpha_i},\qquad
q_i=(\lambda+\alpha_i)r_i-\lambda\alpha_i.
\]
Because \(0<\lambda,\alpha_i<1\), \(0<r_i<1\) and both denominators are nonzero. Consequently the product and sum of the two poles are reconstructed as
\[
t_i=\frac{r_i^2-q_i}{1-r_i^2}=\lambda\alpha_i,
\qquad
s_i=r_i(1+t_i)=\lambda+\alpha_i.
\]
The roots of \(z^2-s_i z+t_i=0\), counted with multiplicity, give the unordered pair \(P_i=\{\lambda,\alpha_i\}\) exactly. This also covers \(\alpha_i=\lambda\), where the discriminant is zero.

**Step 3: color heterogeneity uniquely labels the common pole.** If \(\alpha_1\ne\alpha_2\), the intersection of the two unordered multisets, understood as their common numerical values, is the singleton \(\{\lambda\}\). The other roots label the two environmental coefficients. The innovation variances are recovered from the exact identity
\[
\gamma_i(0)=\frac{\sigma_i^2(1+\lambda\alpha_i)}{(1-\lambda^2)(1-\alpha_i^2)(1-\lambda\alpha_i)}.
\]
The contemporaneous cross covariance satisfies
\[
C=\frac{\tau(1-\lambda^2\alpha_1\alpha_2)}{(1-\alpha_1\alpha_2)(1-\lambda^2)(1-\lambda\alpha_1)(1-\lambda\alpha_2)}.
\]
The latter follows by summing the two stable causal filters against the cross-site white-innovation covariance, or by summing the cross-site environmental-lag covariances. Every factor multiplying \(\tau\) is positive, so the formula identifies \(\tau\) even when \(\tau=0\). This proves uniqueness of every parameter from the seven stated real moments.

**Step 4: exact equality-color obstruction.** If \(\alpha_1=\alpha_2=a\ne\lambda\), both transfer functions equal \([(1-\lambda L)(1-aL)]^{-1}\). Swapping \(\lambda\) with \(a\) at both sites leaves the entire bivariate linear-filter process unchanged for the same Gaussian innovation sequence, yet it changes the named demographic coefficient. No temporal statistic can distinguish the models. If \(a=\lambda\), the sole repeated root has only one parameter value, so this swap is trivial.

**Step 5: lags \(0,1\) are insufficient for the indicated observables.** At any interior unequal-color point, fix the observed numbers \(r_i\) and vary \(\lambda'\) slightly. Define
\[
\alpha_i'=\frac{r_i-\lambda'}{1-r_i\lambda'}.
\]
For sufficiently small nonzero perturbations, these remain in \((0,1)\), unequal, and the two observed autocorrelation ratios stay fixed. Choose the new positive innovation variances using the formula in Step 3 to preserve each \(\gamma_i(0)\), then choose the new cross-innovation covariance using the displayed expression for \(C\). Strict positive definiteness of \(\Sigma\) persists by continuity. This produces an open one-parameter family sharing \(\gamma_i(0),\gamma_i(1)\) and \(C\) but having different \(\lambda\). The displayed lag-two inversion removes that ambiguity.

## Verification
An independently executable exact-rational checker (`verify.py`) reconstitutes all moment formulas, calculates pole pairs and recovered innovation covariances, and checks repeated-root and equal-color cases. Its actual output appears in `verification_output.txt`. The rational witness is \(\lambda=1/2\), \(\alpha_1=1/4\), \(\alpha_2=3/4\), \((\sigma_1^2,\sigma_2^2,\tau)=(1,4,1)\), with
\[
(\gamma_1(0),\gamma_1(1),\gamma_1(2))=(64/35,128/105,24/35),
\]
\[
(\gamma_2(0),\gamma_2(1),\gamma_2(2))=(2816/105,512/21,2144/105),\quad C=3904/1365.
\]
Substitution recovers the two root multisets \(\{1/4,1/2\}\) and \(\{1/2,3/4\}\), whose unique common root is \(1/2\). All unrestricted assertions follow algebraically; the finite checks do not serve as infinite proof.

## Relationship to prior work
Massie and colleagues (2015) analyze correlated AR(1) environmental color filtered by a common AR(1) population response and derive the *enhanced Moran effect* (their equation (7)): abundance correlation can exceed environmental correlation. Their paper works with experimentally generated environmental time series and examines forward correlations, not the parameter-identification map from site-specific abundance autocovariances. Dennis and colleagues (2006) study stochastic population state-space estimation and identifiability difficulties with process and observation noise, whereas the present theorem isolates **serially correlated latent forcing and a shared demographic pole with no measurement noise**. Knape (2008) studies estimability under measurement error, a distinct confounding mechanism. Standard AR(2) Yule--Walker recovery of an unordered pole pair is an ingredient, not a claim of new autoregressive mathematics; the combination across sites, the exact equal-color all-lag obstruction, and the minimal specified moment set constitute the assessed contribution.

## Limitations
The theorem is structural identification from exact covariances, not a finite-sample consistency or robustness guarantee. Close environmental pole values can make identification ill-conditioned despite uniqueness. Unknown measurement error, different demographic coefficients, nonlinear regulation, latent dispersal, nonstationarity, and more complicated environmental spectra are outside the proof. The lag-two sufficiency and lag-one counterexample compare only the explicitly listed moments, not every possible statistic from two census dates. A broader systems-identification theorem could imply portions of the result.

## References
- Dennis, B., Ponciano, J. M., Lele, S. R., Taper, M. L. & Staples, D. F. (2006), *Estimating Density Dependence, Process Noise, and Observation Error*, Ecological Monographs 76, 323--341, doi:10.1890/0012-9615(2006)76[323:EDDPNA]2.0.CO;2 (online 2006-08-01).
- Massie, T. M., Weithoff, G., Kuckländer, N., Gaedke, U. & Blasius, B. (2015), *Enhanced Moran effect by spatial variation in environmental autocorrelation*, Nature Communications 6, 5993, doi:10.1038/ncomms6993.
- Knape, J. (2008), *Estimability of Density Dependence in Models of Time Series Data*, Ecology 89, 2994--3000, doi:10.1890/08-0071.1.
