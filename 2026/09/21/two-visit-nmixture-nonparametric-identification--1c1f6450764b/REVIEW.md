# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The detection-probability identity follows directly from three conditional moment equations:
\[
\mathbb E Y_j=p_j\mathbb EN,\quad
\mathbb E[Y_j(Y_j-1)]=p_j^2\mathbb E[N(N-1)],\quad
\mathbb E(Y_1Y_2)=p_1p_2\mathbb EN^2.
\]
Subtracting the two normalized second-moment expressions leaves exactly \(p_j\). The proof uses only the stated finite-second-moment and conditional-independence assumptions.

Once \(p_j\) is known, binomial thinning gives \(G_j(s)=F(1-p_j+p_js)\). Equality of two candidate observed marginals therefore forces their latent pgfs to agree on a nontrivial real interval inside the unit disk; analyticity then forces equality of the pgfs and of the entire latent abundance laws. The one-visit Poisson construction is a valid exact nonidentifiability family. Exact rational checks independently reproduced the moment identities for multiple finite-support abundance distributions and detection probabilities.

Adversarial checks confirmed that the formula fails in general if conditional visit independence is removed, and that the theorem must exclude zero mean, zero detection probability, and infinite second moment when using the displayed moment formula. The result is structural identification from the population law, not stable finite-sample estimation.

## Originality

**PASS, to the best of our knowledge, with a concrete residual risk.** Royle (2004) supplies the basic repeated-binomial N-mixture model. Dennis, Morgan and Ridout (2015) is the closest checked predecessor: for a mixed-Poisson abundance model with common detection probability, its Section 6 derives the equivalent estimator
\[
\tilde p=(m_1-m_2+m_{12})/m_1.
\]
That equal-\(p\) formula is explicitly excluded from the originality claim.

Guillera-Arroita, Ridout and Morgan (2012) explicitly use finite-support nonparametric abundance distributions in a related continuous-detection model, but the checked text does not give the two-visit binomial cancellation theorem or unrestricted pgf identification. Barker et al. (2018), Kéry (2018), and Madsen--Royle (2023) discuss practical or parameter identifiability for standard parametric N-mixtures and emphasize sensitivity to assumptions; the checked material does not state the arbitrary-abundance two-visit theorem.

The claimed new contribution is therefore narrowly defined as the combination of: (i) visit-specific, distribution-free recovery of \(p_j\) under an arbitrary count-valued abundance law of finite second moment; (ii) consequent identification of the entire unrestricted abundance law from a marginal pgf; and (iii) the sharp global one-visit versus two-visit structural-identification boundary.

Residual originality risk remains substantial because the proof is elementary and may have appeared under different language in older capture-count, random-binomial-size, or thinning literature. This risk is scientific rather than a correctness issue and is explicitly retained in the record.

## Value

**PASS.** The theorem cleanly separates structural identification from the parametric abundance assumptions ordinarily used to fit N-mixture models. It shows that, under the ideal closed independent-binomial observation mechanism, Poisson or negative-binomial abundance is not required for population-level identifiability once two visits are available. It also clarifies why this statement does not resolve practical robustness concerns: the assumptions on detection and closure remain strong, and full-law inversion may be badly conditioned.

The visit-specific formula and the reference-visit agreement constraints for \(T\ge3\) provide simple population diagnostics that can distinguish model structure from a chosen abundance family.

## Checked evidence

The primary theorem statements and formulas checked include Royle's repeated-count N-mixture setup; Dennis et al. (2015), especially its conditional moment equations and Section 6 moment estimator; Guillera-Arroita et al. (2012) on finite-support nonparametric abundance distributions; Barker et al. (2018) on reliability and visit-varying detection concerns; Kéry (2018) on practical identifiability screening; and Madsen--Royle (2023) on the modern N-mixture literature and identifiability concerns. Searches also covered binomial thinning, random-size binomial mixtures, nonparametric N-mixtures, repeated counts, and synonymous identifiability formulations.

## Limitations

The result is restricted to a closed population with conditionally independent binomial repeated counts, fixed visit-specific detection probabilities, positive finite mean abundance, and finite second moment. It does not allow individual-level detection heterogeneity, site-specific random detection, count inflation from repeated detection within a visit, population dynamics between visits, or residual dependence between visits. It establishes uniqueness of the population law and parameters, not statistical regularity, efficient estimation, or robust finite-sample performance. Analytic recovery of a full abundance pgf from a thinned marginal can be ill-conditioned.
