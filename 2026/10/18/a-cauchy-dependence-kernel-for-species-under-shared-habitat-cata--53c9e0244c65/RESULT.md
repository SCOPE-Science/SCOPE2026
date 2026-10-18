# A Cauchy dependence kernel for species under shared habitat catastrophes

## Finding

Consider a common-reset metacommunity null model: at each habitat patch, catastrophes arrive at a homogeneous Poisson rate \(\gamma>0\) and simultaneously clear all species. Between catastrophes, different species colonize independently at fixed rates \(\lambda_i>0\), and occupied species disappear locally at rates \(\mu_i\ge0\), independently of each other. Write \(s_i=\lambda_i+\mu_i\). Observe one patch in its unique stationary regime, and write \(I_i\) for species \(i\)'s presence indicator. Let \(A\) be the time since its latest catastrophe, \(q_i(A)=\Pr(I_i=1\mid A)\), and \(L_{ij}=\operatorname{Cov}(q_i(A),q_j(A))\), the *environmentally induced* covariance matrix (not the full indicator covariance matrix).

**Theorem.** For every finite number of species and every allowed parameter choice,
\[
L_{ij}=\frac{\gamma\lambda_i\lambda_j}{(\gamma+s_i)(\gamma+s_j)(\gamma+s_i+s_j)}.
\]
After ordering species by increasing \(s_i\), all minors of \(L\) are nonnegative; a minor is strictly positive when its row and column recovery rates are separately distinct. In particular, \(\operatorname{rank}L\) equals the number of distinct recovery rates \(s_i\), even though patch age is the *only* shared random environmental variable. For \(k\) distinct recovery rates, the full determinant is
\[
\det L=\frac{\gamma^k\prod_i\lambda_i^2}{\prod_i(\gamma+s_i)^2}\,
\frac{\prod_{i<j}(s_j-s_i)^2}{\prod_{i,j}(\gamma+s_i+s_j)}>0.
\]
For distinct species \(i,j\), the observable Pearson occurrence correlation is
\[
\rho_{ij}(\gamma)=\frac{\gamma\sqrt{\lambda_i\lambda_j}}
{(\gamma+s_i+s_j)\sqrt{(\gamma+\mu_i)(\gamma+\mu_j)}}
\quad\text{and}\quad 0<\rho_{ij}(\gamma)<\frac12.
\]
The constant \(1/2\) is the sharp, unattained universal supremum. For fixed species rates, \(\rho_{ij}(\gamma)\) decreases strictly if \(\mu_i=\mu_j=0\); otherwise it has exactly one strict interior maximum, at the unique positive root of
\[
2\gamma^3+(\mu_i+\mu_j)\gamma^2-(s_i+s_j)(\mu_i+\mu_j)\gamma
-2(s_i+s_j)\mu_i\mu_j=0.
\]
For identical species rates \(\lambda_i=\lambda_j=\lambda>0\) and \(\mu_i=\mu_j=\mu>0\), this optimum is \(\gamma_*=\sqrt{2\mu(\lambda+\mu)}\), with peak correlation
\[\rho_{ij}(\gamma_*)=\frac{\lambda}{(\sqrt{2(\lambda+\mu)}+\sqrt\mu)^2}.\]
The one-half ceiling relies on exponential colonization/recovery: two noninteracting species that each deterministically recolonize a fixed time after the shared catastrophe, without local loss, have correlation exactly one at stationarity.

## Assumptions and scope

Each habitat patch is homogeneous. Catastrophe times form a Poisson process, independent of all species-specific events. At a catastrophe all occupancy indicators become zero. In between, each absent species switches to present at constant rate \(\lambda_i\), and each present species switches to absent at constant rate \(\mu_i\). All clocks are mutually independent apart from their common catastrophe times. Species do not interact. There are finitely many species, at least two to define a pairwise correlation. Rates \(\lambda_i>0\), \(\mu_i\ge0\), and \(\gamma>0\) are finite. The statement concerns the stationary distribution at a randomly chosen patch, not sample-estimation bias from a finite collection of patches.

The environmental covariance \(L\) is defined by conditional mean occupancies, and must not be conflated with the raw observable covariance. In particular \(\operatorname{Cov}(I_i,I_j)=L_{ij}\) when \(i\ne j\), whereas \(\operatorname{Var}(I_i)=\mathbb E[q_i(A)(1-q_i(A))]+L_{ii}\). The total observed covariance matrix can be full rank for different reasons, including intrinsic demographic noise.

## Proof

**Stationary age and conditional occupancy.** Regeneration at the latest catastrophe implies \(A\sim\operatorname{Exp}(\gamma)\). Independently for each species, the forward two-state colonization/loss chain started empty has conditional occupancy
\[
q_i(a)=\frac{\lambda_i}{s_i}(1-e^{-s_i a}).
\]
Thus \(\mathbb E I_i=\mathbb E q_i(A)=\lambda_i/(\gamma+s_i)\), because \(\mathbb E e^{-tA}=\gamma/(\gamma+t)\). For distinct species, conditional independence gives \(\operatorname{Cov}(I_i,I_j)=\operatorname{Cov}(q_i(A),q_j(A))\). Direct expansion of this last covariance, or its Laplace-transform integral, yields
\[
L_{ij}=\frac{\lambda_i\lambda_j}{s_i s_j}\left[\frac{\gamma}{\gamma+s_i+s_j}-\frac{\gamma^2}{(\gamma+s_i)(\gamma+s_j)}\right]
=\frac{\gamma\lambda_i\lambda_j}{(\gamma+s_i)(\gamma+s_j)(\gamma+s_i+s_j)}.
\]
The same identity defines \(L_{ii}=\operatorname{Var}(q_i(A))\).

**Exact total positivity and rank.** Set \(d_i=\sqrt\gamma\lambda_i/(\gamma+s_i)>0\). Then \(L_{ij}=d_i d_j/(\gamma+s_i+s_j)\), a positive diagonal rescaling of a symmetric Cauchy matrix. The standard Cauchy determinant identity gives, for any equal-size row and column index sets \(R=(r_1<\cdots<r_h)\), \(C=(c_1<\cdots<c_h)\) ordered by increasing recovery rate,
\[
\det L_{R,C}=\gamma^h\left(\prod_{r\in R}\frac{\lambda_r}{\gamma+s_r}\right)
\left(\prod_{c\in C}\frac{\lambda_c}{\gamma+s_c}\right)
\frac{\prod_{a<b}(s_{r_b}-s_{r_a})(s_{c_b}-s_{c_a})}
{\prod_{a,b}(\gamma+s_{r_a}+s_{c_b})}.
\]
Every factor is nonnegative. It is strictly positive when rates do not repeat within either index set. In particular, selecting one index from each distinct-rate class gives a positive principal minor of size equal to the number of classes. Conversely, if \(s_i=s_j\), then \(q_i(a)/q_j(a)=\lambda_i/\lambda_j\) for every age, so the corresponding rows of \(L\) are proportional. Therefore the rank is exactly the number of distinct recovery rates. The displayed full determinant follows when all \(s_i\) are distinct.

**Pearson ceiling and sharpness.** The Bernoulli variance is \(p_i(1-p_i)=\lambda_i(\gamma+\mu_i)/(\gamma+s_i)^2\), with \(p_i=\lambda_i/(\gamma+s_i)\). Combining this with the pair covariance proves the Pearson formula. Since \(\gamma/\sqrt{(\gamma+\mu_i)(\gamma+\mu_j)}\le1\), and \(s_i+s_j\ge\lambda_i+\lambda_j\ge2\sqrt{\lambda_i\lambda_j}\),
\[
0<\rho_{ij}(\gamma)\le\frac{\sqrt{\lambda_i\lambda_j}}{\gamma+s_i+s_j}<\frac12.
\]
With \(\lambda_i=\lambda_j=1\), \(\mu_i=\mu_j=0\), and \(\gamma=1/n\), one obtains \(\rho_{ij}=n/(2n+1)\to1/2\), proving sharpness.

**Unique disturbance optimum.** Let \(S=s_i+s_j\) and define
\[
h(\gamma)=\gamma\frac{d}{d\gamma}\log\rho_{ij}
=\frac{S}{\gamma+S}-\frac12\left(\frac{\gamma}{\gamma+\mu_i}+\frac{\gamma}{\gamma+\mu_j}\right).
\]
If at least one local extinction rate is positive, then \(h\) is strictly decreasing, with \(h(0+)\in\{1/2,1\}\) and \(h(+\infty)=-1\). It consequently has exactly one positive zero, and the correlation increases before and decreases after that zero. Clearing strictly positive denominators yields the cubic stated in the theorem. If both local rates vanish, \(\rho_{ij}(\gamma)=\sqrt{\lambda_i\lambda_j}/(\gamma+\lambda_i+\lambda_j)\), strictly decreasing. With identical rates and \(\mu>0\), the cubic factors, yielding the square-root optimum and peak formula.

**Recovery-law boundary.** With the same Poisson catastrophes but a deterministic recolonization delay \(\tau>0\) and no independent local losses, let both species recover separately (deterministically) at age \(\tau\). Their indicators are both \(\mathbf 1_{\{A\ge\tau\}}\). The nondegenerate common Bernoulli variable has success probability \(e^{-\gamma\tau}\in(0,1)\), hence their Pearson correlation is exactly one. No interspecies biological interaction is involved. This demonstrates that the one-half ceiling is a diagnostic *only* for exponential individual recolonization/loss clocks, not for arbitrary recovery laws.

## Verification

The standalone `verify.py` implements an independent four-state stationary continuous-time Markov-generator calculation using exact rational Gaussian elimination and compares its two-species marginals and covariance with the age-mixture formulas for 360 sets of rational parameters (1,080 equality checks). It checks the sharp half bound at the same points. A second exact calculation tests 3,801 ordered Cauchy minor identities with up to six species, including positivity and rank loss under repeated recovery rates. The code also checks 54 derivative-shape parameter combinations and the exact sharpness family. The recorded certificate is `certificate.json`, generated by `python verify.py`. These finite checks corroborate but do not replace the unrestricted proof.

## Relationship to prior work

Hastings (2003) develops metapopulation persistence with patch-age-dependent disturbances. Hamelin and collaborators (2019) show how common host mortality induces positive co-infection associations even without biological interaction. Calcagno and collaborators (2022) give a broad metacommunity framework and an age-mixture covariance identity for noninteracting species under shared patch disturbance. Their general positive-dependence phenomenon and conditional-age approach are acknowledged, not claimed as new. The Cauchy minor/rank classification for exponential recovery, the sharp Pearson half ceiling, the unique hazard optimum (including heterogeneous local extinction), and the explicit nonexponential sharp boundary are the specific conclusions established here. The Cauchy determinant identity itself is classical and is not claimed as new.

## Limitations

This is a theorem for a deliberately restricted homogeneous reset and independent exponential recovery model. The model has a single shared catastrophe clock, fixed parameters across sites, no species interactions, independent local demographic transitions, and stationary sampling. Heterogeneous habitat qualities, age-dependent catastrophes, colonization coupling, and nonexponential recovery can violate its sharp correlation ceiling. Correlation exceeding one-half rejects this restricted null model, **not** the entire class of noninteracting ecological explanations, and it does not by itself establish causal interaction. Latent environmental covariance rank is not the rank of the raw observed indicator covariance. Earlier mathematical treatments of the same null model may contain equivalent representations; an independent bibliographic audit has not been performed.

## References

- Hastings, A. (2003). “Metapopulation persistence with age-dependent disturbance or succession.” *Science* 301: 1525–1526. DOI: 10.1126/science.1087570. Published 2003-09-12.
- Leibold, M. A., et al. (2004). “The metacommunity concept: a framework for multi-scale community ecology.” *Ecology Letters* 7: 601–613. DOI: 10.1111/j.1461-0248.2004.00608.x. First published 2004-06-04.
- Hamelin, F. M., et al. (2019). “Coinfections by noninteracting pathogens are not independent and require new tests of interaction.” *PLOS Biology* 17: e3000551. DOI: 10.1371/journal.pbio.3000551.
- Calcagno, V., et al. (2022). “Metacommunity dynamics and the detection of species associations in co-occurrence analyses: Why patch disturbance matters.” *Functional Ecology*. DOI: 10.1111/1365-2435.14047.
- Cauchy's double alternant determinant identity (classical matrix identity, used here only as a proof tool).
