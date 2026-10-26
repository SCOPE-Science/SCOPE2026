# Three-season recovery of false-positive occupancy from pairwise moments under changing detection effort

## Finding

Consider a stationary binary occupancy process observed once at each of three consecutive seasons. Let \(X_t\in\{0,1\}\) denote true occupancy and \(Y_t\in\{0,1\}\) the reported detection for \(t\in\{0,1,2\}\). Suppose the unobserved occupancy process has strictly interior colonization and extinction probabilities \(\gamma=\Pr(X_{t+1}=1\mid X_t=0)\) and \(\varepsilon=\Pr(X_{t+1}=0\mid X_t=1)\). Write \(\pi=\gamma/(\gamma+\varepsilon)\in(0,1)\) and \(\lambda=1-\gamma-\varepsilon\ne0\). Conditional on latent states, detections are independent, with the same unknown false-positive probability \(f\in(0,1)\) at all three seasons, and season-specific true-positive detection probabilities \(f<d_t<1\).

**Theorem.** If the outer-season true-positive detection probabilities differ, \(d_0\ne d_2\), the three means \(m_t=\mathbb E[Y_t]\) and three pairwise covariances \(c_{ij}=\operatorname{Cov}(Y_i,Y_j)\), for \(ij\in\{01,12,02\}\), uniquely determine \(f,\pi,\lambda,\gamma,\varepsilon,d_0,d_1,d_2\). The exact inverse is

\[
 f=\frac{c_{01}m_2-c_{12}m_0}{c_{01}-c_{12}},\qquad
 r_{ij}=\frac{c_{ij}}{(m_i-f)(m_j-f)},
\]

\[
 \lambda=\frac{r_{02}}{r_{01}},\qquad
 \pi=\frac{r_{02}}{r_{01}^{2}+r_{02}},\qquad
 d_t=f+\frac{m_t-f}{\pi},
\]

\[
 \gamma=\pi(1-\lambda),\qquad
 \varepsilon=(1-\pi)(1-\lambda).
\]

**Sharp observation-design boundaries.** Two seasons do not identify these parameters even from their complete binary joint distribution. If \(d_0=d_2\), the first two moment orders from three seasons admit a one-parameter family of distinct interior parameter vectors in a neighborhood of every interior model with \(\lambda\ne0\). If \(\lambda=0\), even the complete three-season observed joint distribution does not identify the parameters. These are statements about population-level distributions, not noisy finite-sample estimates.

**Moment feasibility.** For observed binary means and pair covariances with \(c_{01}\ne c_{12}\), apply the displayed formulas. They arise from exactly one strictly interior model in this class if and only if the derived \(r_{01}=r_{12}\ne0\), \(r_{02}>0\), \(0<f<d_t<1\), \(0<\pi<1\), and \(0<\gamma,\varepsilon<1\) all hold, with each \(m_t-f>0\). In particular, the input moments are then exactly reproduced; no third-order moment is required. The equivalence concerns an admissible six-moment vector, not arbitrary joint distributions having that vector.

## Assumptions and scope

The hidden process is a time-homogeneous, irreducible, stationary two-state Markov chain. Its transition probabilities are strictly between zero and one. At each season there is one noisy binary survey and there are no time-correlated observation errors once the hidden states are fixed. False-positive probability is constant across the three seasons but unknown; true-positive detection probability may change, with the first and last values required to be different. Positive detection discrimination \(d_t>f\) fixes the hidden-state label. Exact moments are imagined available across a population of independent replicated sites. Neither replicates within a season nor known error rates are assumed.

The statement remains algebraically valid when \(\lambda<0\): alternating occupancy correlations simply give both consecutive covariances the same negative sign and the two-season-gap covariance a positive sign. The theorem makes no claim for nonstationary occupancy, season-dependent false-positive rates, correlated observation errors, or inference from one short site time series.

## Proof

Stationarity gives \(\mathbb E[X_t]=\pi\) and, for \(i<j\),

\[
 \operatorname{Cov}(X_i,X_j)=\pi(1-\pi)\lambda^{j-i}.
\]

Indeed, the transition law obeys \(\mathbb E[X_{t+1}-\pi\mid X_t]=\lambda(X_t-\pi)\); iterate this identity and condition on \(X_i\). Define \(\delta_t=d_t-f>0\). Conditional expectation is \(\mathbb E[Y_t\mid X_t]=f+\delta_t X_t\), and conditional independence eliminates cross-season observation-noise covariance. Therefore

\[
 m_t=f+\pi\delta_t,\qquad
 c_{ij}=\pi(1-\pi)\delta_i\delta_j\lambda^{j-i}.
\tag{1}
\]

In particular,

\[
 c_{01}-c_{12}=\pi(1-\pi)\delta_1\lambda(\delta_0-\delta_2),
\]

which is nonzero under the stated assumptions. Divide the first two covariance equations by \((m_i-f)(m_j-f)=\pi^2\delta_i\delta_j\). Their normalized values must coincide, so

\[
 \frac{c_{01}}{(m_0-f)(m_1-f)}
 =\frac{c_{12}}{(m_1-f)(m_2-f)}.
\]

Cross-multiplication gives the unique displayed expression for \(f\). With \(f\) recovered, (1) implies

\[
 r_{01}=r_{12}=\frac{1-\pi}{\pi}\lambda,
 \qquad r_{02}=\frac{1-\pi}{\pi}\lambda^2>0.
\]

Their ratios uniquely recover \(\pi\) and \(\lambda\) as displayed. The remaining parameters follow from the mean formula and the definitions of stationary distribution and the nontrivial transition eigenvalue. This also proves global uniqueness within the stipulated ordered-state parameter domain.

For the converse, reconstruct from the candidate moments and impose the listed strict feasibility conditions. The reconstructed stationary Markov chain and conditionally independent observations reproduce all three means by construction. The equal consecutive normalized covariances and the recovered \(\pi,\lambda\) reproduce \(c_{01},c_{12}\); the gap-two identity reproduces \(c_{02}\). Thus the six-moment vector is feasible, with a unique admissible parameter vector.

For the first boundary, a binary two-season law has only two means and one covariance. There are five freely varying interior model parameters \((\pi,\lambda,f,d_0,d_1)\); indeed, choose \(f\) and \(\pi\) within a small open neighborhood, solve \(d_t=f+(m_t-f)/\pi\), and set \(\lambda=c_{01}\pi/[(1-\pi)(m_0-f)(m_1-f)]\). The resulting \(\gamma=\pi(1-\lambda)\) and \(\varepsilon=(1-\pi)(1-\lambda)\) remain interior by continuity and reproduce the entire two-bit law.

For the second boundary, when \(d_0=d_2\), equations (1) force \(m_0=m_2\), \(c_{01}=c_{12}\). Allow \(f\) to vary in an open interval about its true value. For each choice set \(u_0=m_0-f\), \(u_1=m_1-f\), \(r_{01}=c_{01}/(u_0u_1)\), \(r_{02}=c_{02}/u_0^2\), and use the same formulas to reconstruct \(\pi,\lambda,d_0,d_1,d_2,\gamma,\varepsilon\). Since all parameters are strictly interior at the original \(f\), continuity supplies a genuine interval of distinct valid models with identical moments. Finally, when \(\lambda=0\), successive latent occupancy states and hence observations are independent, so the complete observed law depends only on the three means. Different choices of \(\pi,f,d_t\) with the same means give the same entire observed process, using \(\gamma=\pi,\varepsilon=1-\pi\).

## Verification

The independent exact-rational script `verify.py` enumerates the complete hidden three-season paths and the eight observed binary patterns, evaluates means/covariances from first principles, and recomputes the inverse with `fractions.Fraction`. It tests an explicit positive-memory case and 11 further admissible cases, including negative temporal memory. It separately constructs two strictly interior models with identical six moments on the \(d_0=d_2\) boundary. The exact output is `certificate.json`.

For example, \(\pi=2/5\), \(\gamma=1/5\), \(\varepsilon=3/10\), \(f=1/10\), and \((d_0,d_1,d_2)=(3/5,4/5,7/10)\) produce \((m_0,m_1,m_2)=(3/10,19/50,17/50)\), \((c_{01},c_{12},c_{02})=(21/500,63/1250,9/500)\), and the inverse returns every parameter exactly. The proof applies to all admissible real parameter choices; the finite script confirms the algebra and boundary examples but is not used to infer the infinite statement.

## Relationship to prior work

Royle and Link (2006) introduced an occupancy model incorporating both false-positive and false-negative observation errors; the ecological measurement problem and its mixture-model setting are established. Fukaya and Royle (2013) treated noisy Markov community observations and assessed transition estimation without rapid repeat surveys using a different community-dependent mislocation error mechanism. Cole (2019) studied general hidden-Markov identifiability and a homogeneous-emission longitudinal misclassification model; her full-joint identifiability results are not a first-and-second-moment inverse for a common false-positive rate and three distinct time-varying true-positive rates. Liu and Culpepper (2025) provided broader sufficient conditions for identifying heterogeneous hidden Markov models from full joint distributions, with particular emission-repetition conditions that do not imply this three-season moment-inversion theorem for unequal outer-season rates.

The present mathematical claim is restricted to the explicit global inverse for six low-order statistics together with its exact detectability condition \(d_0\ne d_2\) and sharp failure boundary. It does not claim invention of hidden Markov estimation, false-positive occupancy models, or general three-period HMM identification. An equivalent specialized moment calculation under other terminology cannot be ruled out by the inspected sources alone.

## Limitations

Strict stationarity, positive discrimination, constant unknown false-positive rate, and change between outer-season true-positive rates are essential. Without the latter change, six low-order moments lose identification even though additional higher-order information might help. Estimation can be ill-conditioned when \(\lambda\) approaches zero or \(d_0-d_2\) approaches zero, since the inverse contains the small factors \(c_{01}\), \(c_{02}\), and \(c_{01}-c_{12}\). Statistical uncertainty, finite-sample consistency, Bayesian posteriors, missing visits, site heterogeneity, and ecological forecasting are outside this result. No independent review has been performed.

## References

1. Royle, J. A. and Link, W. A. (2006), *Generalized site occupancy models allowing for false positive and false negative errors*, Ecology 87, 835–841. DOI: 10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2. First publicly listed 2006-04-01.
2. Fukaya, K. and Royle, J. A. (2013), *Markov models for community dynamics allowing for observation error*, Ecology 94, 2670–2677. DOI: 10.1890/12-1540.1. Full-text online edition.
3. Cole, D. J. (2019), *Parameter redundancy and identifiability in hidden Markov models*, Metron 77, 105–118. DOI: 10.1007/s40300-019-00156-3. Open-access text, https://kar.kent.ac.uk/75204/.
4. Liu, Y. and Culpepper, S. (2025), *Designing Learning Intervention Studies: Identifiability of Heterogeneous Hidden Markov Models*, Psychometrika 90, 1258–1283. DOI: 10.1017/psy.2025.10024. Open-access full text.
