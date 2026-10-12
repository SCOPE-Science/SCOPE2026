# The PALD observation law leaks the hidden channel and cannot separate its two noise variances
## Finding
The process-augmented lifetime distribution (PALD) paper specifies an orthogonal decomposition of an \(n\)-dimensional latent exposure into an explicit measurement basis and an implicit complement. Its displayed Eq. (2.5) gives a projection-only spherical measurement law, but the Gaussian process and observation transitions of Eqs. (2.6)–(2.8), used in the posterior of Eqs. (2.14)–(2.15), imply a different observable law.

For every integer pair \(0<K<n\), let \(G\in\mathbb R^{n\times K}\) and \(B\in\mathbb R^{n\times(n-K)}\) have orthonormal columns with \(G^\top B=0\). The paper's unit-variance prior and isotropic transition specification can be written
\[
X=G\eta+B\xi,\qquad \xi\mid\eta\sim N_{n-K}(0,I),
\]
\[
r=X+\epsilon_c,\quad Z=r+\epsilon_b,\quad
\epsilon_c\sim N_n(0,\sigma_c^2 I),\quad
\epsilon_b\sim N_n(0,\sigma_b^2 I),
\]
where the Gaussian errors and \(\xi\) are independent conditionally on \(\eta\) and \(\sigma_b^2,\sigma_c^2>0\). Put \(s=\sigma_b^2+\sigma_c^2\).

**Exact observation law.** Integrating the actual transition kernels gives
\[
\boxed{Z\mid\eta\sim N_n(G\eta,s I+BB^\top).}
\]
The covariance has eigenvalue \(s\) on the explicit subspace \(\operatorname{col}(G)\), and eigenvalue \(s+1\) on the implicit subspace \(\operatorname{col}(B)\). Because both spaces have positive dimension, it is **not** a scalar multiple of the identity. This rules out equality with Eq. (2.5)'s stated measurement kernel
\[
Z\mid\eta\sim N_n(G\eta,\sigma_\epsilon^2 I)
\]
for every scalar variance \(\sigma_\epsilon^2\).

**Hidden-channel leakage.** The projected observed data satisfy
\[
B^\top Z=\xi+B^\top(\epsilon_c+\epsilon_b),
\]
and hence
\[
\boxed{\operatorname{Cov}(B^\top Z,\xi\mid\eta)=I_{n-K},}
\]
\[
\boxed{I(\xi;B^\top Z\mid\eta)=\frac{n-K}{2}\log(1+1/s)>0.}
\]
Thus the implicit channel is not absent from the measurement mechanism employed by the published posterior. This matters because the paper motivates the channel as a component missing from the observation and recoverable through survival outcomes.

**Noise-allocation equivalence.** The AFT survival term of the article depends on \(X\), not the intermediate \(r\). Consequently, with all other parameters collected into \(\vartheta\), the observable likelihood conditioned on \(X\) factors as
\[
\boxed{p(Z,t,\delta\mid X,\vartheta,\sigma_b^2,\sigma_c^2)
=p(t,\delta\mid X,\vartheta)\,\phi_n(Z;X,sI),}
\]
where \(\phi_n(\cdot;m,V)\) denotes a normalized multivariate Gaussian density. For every \(s>0\) and \(q\in(0,s)\), the allocation
\[
(\sigma_b^2,\sigma_c^2)=(q,s-q)
\]
produces the **same observed-data law**. Marginalization over latent \(X\) does not change this invariance. Thus, from these observations alone, the model cannot identify the separate process and measurement variances, notwithstanding independent proper priors or two distinct Gibbs conditional updates.

The result is one characterization of the model's induced observation law and its information content: the same unprojected Gaussian chain both retains the implicit channel and admits a continuous variance-allocation ridge.

## Assumptions and scope
The conclusion is exact for the source's specified isotropic kernels \(\Sigma_b=\sigma_b^2I_n\) and \(\Sigma_c=\sigma_c^2I_n\) with independent errors, the fixed unit-variance implicit prior \(\xi\mid\eta\sim N(0,I)\), and an AFT time-to-event kernel that depends on latent \(X\) but not on \(r\) after \(X\) is held fixed. These choices appear in the paper's Section 2.2 and joint posterior.

There must be at least one explicit and at least one implicit direction: \(0<K<n\). The independent Gaussian errors need not have equal variances, but both variances are strictly positive.

The censoring mechanism is assumed to depend on the event process and its stated covariates, not independently on the intermediate \(r\). The likelihood equivalence continues to hold for any survival response governed by \(X\) under this conditional independence assumption.

The assertion of nonidentifiability concerns the observed-data likelihood, not the existence of a proper Bayesian posterior after imposing independent inverse-Gamma priors. Prior-driven posterior preferences along an observational equivalence ridge are not likelihood identification.

## Proof
Since \(X=G\eta+B\xi\) and \(Z=X+\epsilon_c+\epsilon_b\), conditional Gaussian convolution gives
\[
E[Z\mid\eta]=G\eta,\qquad
\operatorname{Cov}(Z\mid\eta)=B\operatorname{Cov}(\xi)B^\top+(\sigma_c^2+\sigma_b^2)I_n=BB^\top+sI_n.
\]
Orthonormal complementarity implies \(BB^\top=I_n-GG^\top\), which is zero on \(\operatorname{col}(G)\) and identity on \(\operatorname{col}(B)\). Therefore the covariance eigenvalues are \(s\) (multiplicity \(K\)) and \(s+1\) (multiplicity \(n-K\)). This is nonspherical for \(0<K<n\).

Multiplying the observation equation by \(B^\top\) gives \(B^\top Z=\xi+\nu\) where \(\nu\sim N_{n-K}(0,sI)\) and \(\nu\perp\xi\) conditionally on \(\eta\). The conditional cross-covariance equals \(I\). The Gaussian mutual-information identity, derived directly from the difference of differential entropies, gives
\[
I(\xi;B^\top Z\mid\eta)
=h(\xi+\nu\mid\eta)-h(\nu\mid\eta)
=\frac12\log\frac{\det((1+s)I)}{\det(sI)}
=\frac{n-K}{2}\log(1+1/s).
\]
This is strictly positive for all finite \(s>0\).

For the likelihood statement, integrate the auxiliary \(r\):
\[
\int_{\mathbb R^n}\phi_n(Z;r,\sigma_b^2I)\phi_n(r;X,\sigma_c^2I)\,dr
=\phi_n(Z;X,(\sigma_b^2+\sigma_c^2)I).
\]
The event/censoring kernel conditioned on \(X\) is independent of \(r\) under the source's AFT model. Consequently it factors out of this integral, yielding the stated likelihood depending on the pair of Gaussian variances only through their sum \(s\). Integration over \(X\) and its other latent variables preserves pointwise equality of joint likelihoods for all positive allocations of the same \(s\). Therefore the map from the two individual variances to observed-data distributions is not injective. Where regular scores exist, the two observed-data score coordinates are the same derivative with respect to \(s\); their two-parameter Fisher information matrix has rank at most one.

## Verification
A standalone numerical checker uses a concrete \(n=3\), \(K=1\) orthonormal basis and the two-dimensional complement. At \(\sigma_b^2=\sigma_c^2=1\), it verifies covariance eigenvalues \(2,3,3\), a nonzero projected cross-covariance, and
\[
I(\xi;B^\top Z\mid\eta)=\log(3/2)=0.4054651081\ldots\ \mathrm{nats}.
\]
It also compares the exact conditional multivariate Gaussian densities at two distinct allocations with the same variance sum, and checks the singular information direction. This finite arithmetic replay supplements, rather than substitutes for, the exact general proof above.

## Relationship to prior work
Liu and Niu (2026) introduce the projection-only measurement statement in Eq. (2.5), but their subsequent generative transition kernels and published joint posterior instead use the unprojected latent exposure. Their Eq. (2.8) already correctly displays the sum covariance \(\Sigma_b+\Sigma_c\) after integrating over the intermediate process. The novelty claimed here is **not** Gaussian convolution. It is the source-specific implication comparison: after imposing the same isotropic variance components actually used for inference, the induced observation law cannot have the stated projection-only measurement structure, and the two separately updated noise scales lie on a continuous observational equivalence ridge. Neither consequence is addressed by the source's claim of identifiable process-loss and observation-noise separation.

Bradley, Wikle, and Holan (2020) study structured **correlated** discrepancy errors, designing covariance relationships that differ substantially from the source's independent isotropic Gaussian chain. Their approach is not a direct parameterization of the two independent variances considered here and does not cover this 2026 equation-level contradiction. Bradley, Zhou, and Liu (2023) investigate deeper discrepancy-process models and are cited as methodological antecedents by the target article; only bibliographic and abstract-level material could be checked for that work, so its uninspected full text remains a residual comparison risk.

Focused literature searches for the target DOI, projection-only measurement law, Gaussian subspace leakage, two-convolution covariance, variance-split observational equivalence, and related identifiability terminology did not reveal a published statement correcting the target article. Absence from search results alone is not treated as a proof of novelty.

## Limitations
The result does not claim that the latent signal \(X\) is entirely unidentifiable: the survival outcomes can contain information about \(X\) and \(\xi\). What is not separately identified by this observation chain is the **allocation** of a fixed sum of two independent isotropic Gaussian error variances.

With an observed validation measurement of \(r\), repeated observations at intermediate stages, cause-dependent censoring linked to \(r\), or known nonproportional covariance templates, the identifiability question changes. Imposing a deterministic projection in the measurement kernel could remove the hidden-channel leakage but would define a different generative model and posterior.

The 2023 discrepancy-model antecedent could not be inspected beyond its public abstract and citation context. The result does not infer what any unavailable implementation used.

## References
1. X. Liu and X. Niu, “Process-augmented lifetime distributions: A generative Bayesian framework for latent structure inference in survival analysis,” *AIMS Mathematics* **11** (2026), 6804–6833. DOI: 10.3934/math.2026281.
2. J. R. Bradley, C. K. Wikle, and S. H. Holan, “Hierarchical models for spatial data with errors that are correlated with the latent process,” *Statistica Sinica* **30** (2020), 81–109. DOI: 10.5705/ss.202016.0230.
3. J. R. Bradley, S. Zhou, and X. Liu, “Deep hierarchical generalized transformation models for spatio-temporal data with discrepancy errors,” *Spatial Statistics* **55** (2023), 100749. DOI: 10.1016/j.spasta.2023.100749.
