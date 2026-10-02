# Independent mathematical audit — SCOPE-20260921-1c1f6450764b
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
In a closed two-visit binomial N-mixture with arbitrary nonnegative-integer abundance law having finite second moment and visit-specific \(p_1,p_2\in(0,1]\), the joint law of the two counts identifies \(p_1,p_2\), the mean abundance, and the entire abundance distribution; one visit is globally nonidentifying, while additional visits yield overidentifying restrictions.

## Correctness
Status: **PASS**.

The moment inversion is exact. If \(a_j=E Y_j\), \(b_j=E[Y_j(Y_j-1)]\), and \(c=E[Y_1Y_2]\), then conditional binomial factorial moments give \(a_j=p_j\mu\), \(b_j=p_j^2E[N(N-1)]\), and \(c=p_1p_2E[N^2]\). Subtracting \(E[N(N-1)]=E[N^2]-E[N]\) yields \(p_1=c/a_2-b_1/a_1\) and the symmetric formula for \(p_2\). A fresh exact-rational test on a non-Poisson latent law reproduced both detection probabilities. Once one \(p_j\) is known, the observed pgf is \(G_j(s)=F(1-p_j+p_js)\); knowledge on an interval inside the unit disk determines the analytic pgf \(F\) uniquely. The one-visit Poisson-thinning alias is a valid global counterexample.

## Originality
Status: **PASS**.

Dennis–Morgan–Ridout’s full accepted manuscript was inspected. It assumes a parametric Poisson or mixed-Poisson abundance family and a common detection probability; its Section 6 derives moment estimators in that restricted setting. The audited theorem instead allows an arbitrary abundance law and visit-specific detection probabilities and then proves full-law identification by pgf analyticity. Searches of N-mixture identifiability, binomial thinning, and capture-recapture mixture literature found parametric or heterogeneity-identifiability results, but no theorem implying this two-replicate nonparametric closed-mixture statement. The one-visit failure is known background and is not claimed as new.

### Equivalent formulations
- Search/source: Published-record semantic query: nonparametric closed binomial N-mixture two visits identify detection probability arbitrary abundance pgf.
- Search/source: E. B. Dennis, B. J. T. Morgan, M. S. Ridout, Computational aspects of N-mixture models, Biometrics 71 (2015), 237–246, DOI:10.1111/biom.12246.
- Evidence: No inspected exact source or database entry states the audited final claim in an equivalent formulation.
- Reasoning: Dennis–Morgan–Ridout’s full accepted manuscript was inspected. It assumes a parametric Poisson or mixed-Poisson abundance family and a common detection probability; its Section 6 derives moment estimators in that restricted setting. The audited theorem instead allows an arbitrary abundance law and visit-specific detection probabilities and then proves full-law identification by pgf analyticity. Searches of N-mixture identifiability, binomial thinning, and capture-recapture mixture literature found parametric or heterogeneity-identifiability results, but no theorem implying this two-replicate nonparametric closed-mixture statement. The one-visit failure is known background and is not claimed as new.

### Broader coverage
- Search/source: E. B. Dennis, B. J. T. Morgan, M. S. Ridout, Computational aspects of N-mixture models, Biometrics 71 (2015), 237–246, DOI:10.1111/biom.12246.
- Search/source: J. A. Royle, N-mixture models for estimating population size from spatially replicated counts, Biometrics 60 (2004), 108–115.
- Search/source: H. Holzmann, A. Munk, W. Zucchini, On identifiability in capture-recapture models, Biometrics 62 (2006), 934–936.
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: Dennis–Morgan–Ridout’s full accepted manuscript was inspected. It assumes a parametric Poisson or mixed-Poisson abundance family and a common detection probability; its Section 6 derives moment estimators in that restricted setting. The audited theorem instead allows an arbitrary abundance law and visit-specific detection probabilities and then proves full-law identification by pgf analyticity. Searches of N-mixture identifiability, binomial thinning, and capture-recapture mixture literature found parametric or heterogeneity-identifiability results, but no theorem implying this two-replicate nonparametric closed-mixture statement. The one-visit failure is known background and is not claimed as new.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No decisive exact database/table coverage was found; where the claim is theorem-level, the primary literature comparison is the controlling check.
- Reasoning: Dennis–Morgan–Ridout’s full accepted manuscript was inspected. It assumes a parametric Poisson or mixed-Poisson abundance family and a common detection probability; its Section 6 derives moment estimators in that restricted setting. The audited theorem instead allows an arbitrary abundance law and visit-specific detection probabilities and then proves full-law identification by pgf analyticity. Searches of N-mixture identifiability, binomial thinning, and capture-recapture mixture literature found parametric or heterogeneity-identifiability results, but no theorem implying this two-replicate nonparametric closed-mixture statement. The one-visit failure is known background and is not claimed as new.

### Claim versus prior implication
- Search/source: E. B. Dennis, B. J. T. Morgan, M. S. Ridout, Computational aspects of N-mixture models, Biometrics 71 (2015), 237–246, DOI:10.1111/biom.12246.
- Search/source: J. A. Royle, N-mixture models for estimating population size from spatially replicated counts, Biometrics 60 (2004), 108–115.
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: The inspected prior statements do not mechanically imply the audited final claim; the additional argument identified in the correctness reconstruction is substantive enough for this claim.

### Primary-source inspections
- **Computational aspects of N-mixture models** (DOI:10.1111/biom.12246; Kent accepted manuscript): trigger — closest primary source for repeated-count moment identifiability; material read — full lawful accepted-manuscript PDF, especially model setup, Poisson equivalence, and Section 6 moment equations and estimators; method — institutional open-access full-text inspection; assessment — PARTIAL_PARAMETRIC_COVERAGE; evidence — The paper derives moment formulas for common \(p\) under Poisson/mixed-Poisson abundance; it does not state arbitrary-law two-visit full identification with visit-specific detection.
- **On identifiability in capture-recapture models** (DOI:10.1111/j.1541-0420.2006.00637_1.x): trigger — plausible broader nonparametric identifiability source; material read — abstract and bibliographic context; method — publisher/PubMed inspection; assessment — DIFFERENT_MIXING_PROBLEM; evidence — The paper studies mixing over capture probabilities and identifiable subfamilies, not the latent-abundance binomial-thinning model audited here.

## Scientific value
Status: **PASS**.

Whether two replicated counts suffice without a parametric abundance law is a natural structural identifiability question in a widely used latent-count model. The theorem gives a sharp replication threshold and an explicit population-level recovery map, so it is more than a routine numerical exercise despite the short moment algebra.

## Checked sources
- E. B. Dennis, B. J. T. Morgan, M. S. Ridout, Computational aspects of N-mixture models, Biometrics 71 (2015), 237–246, DOI:10.1111/biom.12246.
- J. A. Royle, N-mixture models for estimating population size from spatially replicated counts, Biometrics 60 (2004), 108–115.
- H. Holzmann, A. Munk, W. Zucchini, On identifiability in capture-recapture models, Biometrics 62 (2006), 934–936.
- Published-record semantic query: nonparametric closed binomial N-mixture two visits identify detection probability arbitrary abundance pgf.

## Limitations and residual risks
- Finite second moment and strictly positive detection probabilities are used by the stated moment inversion.
- The theorem is a population identifiability result, not a finite-sample stability or estimation-rate theorem.
- Older thinning or repeated-measurement literature could contain an equivalent abstract theorem; targeted searches did not find one.

This audit reports the mathematical assessment only. It is not a formal proof-assistant certificate or a guarantee of priority.
