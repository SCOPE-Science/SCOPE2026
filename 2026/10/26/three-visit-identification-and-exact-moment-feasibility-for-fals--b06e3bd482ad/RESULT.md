# Three-visit identification and exact moment feasibility for false-positive abundance counts

## Finding

Consider repeated unmarked counts of a closed population with Poisson abundance, independent per-animal Bernoulli detection, and independently generated Poisson false detections. **Three surveys identify the abundance mean, every visit-specific true-detection probability, and every visit-specific false-count mean from just seven population moments; two surveys do not identify them even from the entire observed joint distribution.** The seven moments have an explicit necessary-and-sufficient feasibility region. First- and second-order moments alone remain insufficient even with arbitrarily many surveys.

For three surveys let \(\mu_i=\mathbb E[Y_i]\), \(C_{ij}=\operatorname{Cov}(Y_i,Y_j)\), and \(T=\mathbb E[(Y_1-\mu_1)(Y_2-\mu_2)(Y_3-\mu_3)]\). If the model has \(\lambda>0\), \(0<p_i<1\), and \(\phi_i\geq0\), then

\[
\boxed{p_1=\frac{T}{C_{23}},\quad p_2=\frac{T}{C_{13}},\quad p_3=\frac{T}{C_{12}},\qquad
\lambda=\frac{C_{12}C_{13}C_{23}}{T^2}.}
\]

The false-positive rates are identified by

\[
\boxed{\phi_1=\mu_1-\frac{C_{12}C_{13}}{T},\quad
\phi_2=\mu_2-\frac{C_{12}C_{23}}{T},\quad
\phi_3=\mu_3-\frac{C_{13}C_{23}}{T}.}
\]

Conversely, a real seven-tuple \((\mu_1,\mu_2,\mu_3,C_{12},C_{13},C_{23},T)\) occurs as these population moments under the stated model **if and only if**

\[
C_{12},C_{13},C_{23}>0,\qquad 0<T<\min\{C_{12},C_{13},C_{23}\},
\]
\[
\mu_1T\ge C_{12}C_{13},\quad \mu_2T\ge C_{12}C_{23},\quad \mu_3T\ge C_{13}C_{23}.
\]

The non-strict last inequalities include models with zero false-positive intensity. This describes the exact population-moment image, **not** a distribution-free characterization of all count laws or a finite-sample estimator.

## Assumptions and scope

A site has latent population \(N\sim\operatorname{Poisson}(\lambda)\), with \(\lambda>0\). At visit \(i\), each of the \(N\) individuals is detected independently with probability \(p_i\in(0,1)\); the Bernoulli trials are mutually independent across individuals and visits given \(N\). In addition, \(F_i\sim\operatorname{Poisson}(\phi_i)\), where \(\phi_i\ge0\), is the count of spurious detections, independent across visits and independent of \(N\) and the genuine detections. The observed count is the number of genuine detections plus \(F_i\). Identifiability refers to the population-level joint law for independent sites with these shared parameters and exactly the same closed-population model. Visits may have different detection and false-positive rates. Observed counts may exceed true abundance because of false detections. Every displayed identification and feasibility assertion is for the stated interior detection regime, rather than at \(p_i=0\), \(p_i=1\), or \(\lambda=0\).

## Proof

**Joint probability-generating function.** Set \(u_i=z_i-1\). Conditional on \(N\), the genuine detections have joint generating function \(\prod_i(1+p_iu_i)^N\). The Poisson mixing identity and independent false detections give, for any positive integer \(m\) of visits,

\[
G(z_1,\ldots,z_m)=\exp\left\{\lambda\left[\prod_{i=1}^m(1+p_iu_i)-1\right]+\sum_{i=1}^m\phi_i u_i\right\}.
\]

In particular, the logarithm is multi-affine in the variables \(u_i\). Its coefficients for distinct indices are \(\mu_i=\lambda p_i+\phi_i\), \(C_{ij}=\lambda p_ip_j\), and, for three visits, \(T=\lambda p_1p_2p_3\). Here differentiation of the ordinary cumulant-generating function at the origin confirms that the coefficient of \(u_1u_2u_3\) equals the third centered cross-moment, not an approximation or a factorial-moment substitute. The three positive pair covariances and positive triple moment immediately yield the displayed inverse. Therefore the parameter map is injective and hence the complete three-visit joint law is identifying.

**Feasibility.** Necessity of the displayed inequalities follows from \(0<p_i<1\), \(\phi_i\ge0\), and the preceding equations. Conversely, from any seven numbers satisfying them, define \(p_i,\lambda,\phi_i\) by the inverse formulas. The three strict inequalities on \(T\) yield \(0<p_i<1\); the three remaining inequalities yield \(\phi_i\ge0\). All parameters are admissible, and substitution recovers exactly the seven stipulated moments. This proves sufficiency without supposing that an arbitrary pre-existing law with those moments belongs to the model.

**Two visits are insufficient even with the full law.** For two visits the exact logarithmic generating function is

\[
\log G(z_1,z_2)=\mu_1u_1+\mu_2u_2+C_{12}u_1u_2.
\]

Thus the *entire observed joint distribution* depends on only those three quantities. The two admissible parameter sets

\[
(\lambda,p_1,p_2,\phi_1,\phi_2)
=(3,1/3,1/2,1/5,1/4)
\]

and

\[
(\lambda,p_1,p_2,\phi_1,\phi_2)
=(5/2,2/5,1/2,1/5,1/2)
\]

are distinct but both give \(\mu_1=6/5\), \(\mu_2=7/4\), and \(C_{12}=1/2\). In fact, allowing \(p_1\) to vary through a sufficiently small interval while fixing \(\lambda p_1=1\), \(p_2=1/2\), and the observed means yields a continuum of strictly interior observationally equivalent parameters. One visit is plainly also insufficient. Therefore three visits are the sharp minimum for identifying the entire parameter vector in this model.

**Pair moments are insufficient at any number of visits.** For any \(m\ge2\) and an admissible parameter set, choose \(s>1\) sufficiently close to one so that \(sp_i<1\) for every \(i\), and set

\[
\lambda'=\lambda/s^2,\qquad p_i'=s p_i,\qquad
\phi_i'=\phi_i+\lambda p_i(1-1/s).
\]

The transformed parameters are admissible and distinct; every marginal mean and pair covariance remains unchanged, whereas every cross-cumulant on three distinct visits is multiplied by \(s\). Consequently no amount of pair-moment information alone resolves the false-detection versus true-abundance scale ambiguity.

**One compact law.** For three visits, the same generating-function identity specializes to

\[
\log G(z_1,z_2,z_3)=\sum_i\mu_i u_i+\sum_{i<j}C_{ij}u_iu_j+Tu_1u_2u_3.
\]

Hence the seven moments determine the *entire* three-visit count law within the model, not merely its parameters.

## Verification

The standalone script `artifacts/check.py` uses exact rational arithmetic. It generates the independent Poisson shock rates for the seven nonempty survey subsets, obtains mixed cross-cumulants directly from those rates, and reconstructs parameters from their moments. It checks \(3456\) rational parameter tuples, including boundaries with \(\phi_i=0\), and compares the complete two-visit shock-rate vectors for the explicit nonidentifiable pair. It also tests the first-two-moment-preserving scale transformation, while independently verifying that the third cross-cumulant changes. Its deterministic output is `artifacts/certificate.json`.

For example, \(\lambda=5/2\), \((p_1,p_2,p_3)=(1/4,2/5,3/7)\), and \((\phi_1,\phi_2,\phi_3)=(1/3,2/7,1/6)\) give

\[
(\mu_1,\mu_2,\mu_3)=(23/24,9/7,26/21),\qquad
(C_{12},C_{13},C_{23})=(1/4,15/56,3/7),\qquad T=3/28.
\]

All fractions and identities are exact. This finite verification supplements the proof; it does not establish the universal quantifiers.

## Relationship to prior work

Royle (2004) introduced the repeated-count binomial N-mixture framework with a latent abundance law. Dennis, Morgan and Ridout (2015), particularly Sections 2, 3.1 and 6.1, provided multivariate-Poisson representations and moment analysis for the standard model without additive independent false-positive counts. A published theorem on two-visit nonparametric closed binomial N-mixtures identifies detection probabilities without false detections; its full text was compared and does not imply two-visit identification here once the visit-specific Poisson background intensities are unknown.

Corcoran, Denman and Hamilton (2020) documented spurious automated wildlife counts and difficulties with existing N-mixture fitting. Clement, Royle and Mixan (2022), Sections 2.2–2.3, studied a different count mechanism involving Poisson *per-individual encounter* intensities and species misclassification, with a proposed exogenous false-positive extension. Neither inspected model gives the present independent *Bernoulli* per-individual detection with visit-specific additive Poisson false counts, its exact seven-moment inverse, its feasibility inequalities, and its sharp two/three-visit contrast.

The result is related to the classical independent-Poisson shock decomposition of multivariate counts. In that broader representation, general subset rates are identified by the count law; the content established here is the parameter and moment-image inversion for this ecological contamination subfamily together with its survey and moment-order boundaries. The argument is elementary once this generating function is available, and an equivalent formulation in broader multivariate-Poisson or capture-count literature remains a serious originality risk.

## Limitations

The theorem is about **structural** identifiability from exact population moments. It gives no claim of small-sample stability, accurate abundance estimation when \(T\) is near zero, finite-sample confidence coverage, or ecological realism beyond the assumptions. Its inversion can be ill-conditioned as cross-cumulants vanish. It excludes heterogeneity in per-animal detection, temporal dependence of false detections, imperfect closure, overcounting the same individual within one visit, and non-Poisson abundance. It makes no equivalence claim for the Poisson-per-individual-encounter model and makes no claim of independent external validation or exhaustive literature novelty.

## References

1. J. A. Royle, “N-Mixture Models for Estimating Population Size from Spatially Replicated Counts,” *Biometrics* 60 (2004), 108–115. Published online 11 March 2004. DOI: 10.1111/j.0006-341X.2004.00142.x.
2. E. B. Dennis, B. J. T. Morgan and M. S. Ridout, “Computational Aspects of N-Mixture Models,” *Biometrics* 71 (2015), 237–246. Published online 14 October 2014. DOI: 10.1111/biom.12246.
3. E. Corcoran, S. Denman and G. Hamilton, “New technologies in the mix: Assessing N-mixture models for abundance estimation using automated detection data from drone surveys,” *Ecology and Evolution* 10 (2020), 8176–8185. DOI: 10.1002/ece3.6522.
4. M. J. Clement, J. A. Royle and R. J. Mixan, “Estimating occupancy from autonomous recording unit data in the presence of misclassifications and detection heterogeneity,” *Methods in Ecology and Evolution* 13 (2022), 1719–1729. DOI: 10.1111/2041-210X.13895.
5. “Two visits identify a nonparametric closed binomial N-mixture,” published mathematical research record, 21 September 2026; full scientific statement compared for the distinct no-false-detections assumption.
