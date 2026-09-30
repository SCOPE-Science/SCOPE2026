# Independent Audit — Two visits identify a nonparametric closed binomial N-mixture

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `99c02b3af274e5949fb83f43ad853fc63e4b0c07`  
**Audited current source tree:** `99c02b3af274e5949fb83f43ad853fc63e4b0c07`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment inventory snapshot, so the audited source tree remains exactly the assigned tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Conditional binomial factorial moments give a_j=p_j E[N], b_j=p_j^2 E[N(N-1)], and c=p_1p_2 E[N^2]. Hence c/a_2-b_1/a_1=p_1 and symmetrically for p_2, with no distributional assumption on N beyond the stated finite moments. Once either p_j is known, G_j(s)=F(1-p_j+p_js) determines the latent pgf F on a nontrivial real interval inside the open unit disk; analyticity and the identity theorem then uniquely determine F and all probabilities P(N=n). The one-visit Poisson-thinning counterexample is valid and proves global nonidentifiability with one visit. I independently checked the moment formulas exactly on underdispersed and overdispersed finite-support latent laws with unequal rational p_1,p_2.

## Originality — PASS

PASS, narrowly scoped. Dennis--Morgan--Ridout (2015) already give the equivalent equal-detection moment formula within mixed-Poisson/negative-binomial N-mixture models, so that specialization receives no novelty credit. Royle's foundational formulation and standard binomial-thinning pgf identities are also prior. Targeted searches did not locate the submitted distribution-free theorem for arbitrary count-valued abundance, unequal visit-specific p_1,p_2, and subsequent identification of the entire unrestricted latent law from two visits, nor the sharp one-versus-two structural threshold. Because the cancellation is elementary, older random-size-binomial or capture-count literature remains a residual priority risk.

## Scientific value — PASS

PASS. The result isolates a clean structural fact beneath parametric N-mixture fitting: two conditionally independent visits suffice at the population-law level even without a Poisson, negative-binomial, mixed-Poisson, or finite-support abundance model. The explicit overidentifying restrictions for three or more visits are useful model diagnostics. The record appropriately distinguishes structural identification from stable finite-sample recovery.

## Independent checks

- Re-derived all first and second factorial-moment identities directly from conditional binomial moments.
- Checked the unequal-p formulas with exact rational arithmetic on two distinct finite-support abundance laws; the recovered p_1,p_2 matched exactly.
- Rechecked the pgf identity-theorem argument, including p_j=1, where the observed interval is (0,1).
- Rechecked the one-visit Poisson thinning family N~Poisson(lambda/p) as an exact continuum of observationally equivalent parameterizations.
- Compared with Royle (2004) and the open Dennis--Morgan--Ridout (2015) account, which assumes parametric mixing and already contains the equal-p moment estimator but not the full arbitrary-law theorem located here.
- Targeted searches across N-mixture identifiability, binomial thinning, repeated counts, and nonparametric abundance models found no exact covering theorem.
- Inspected the package verification artifact (73 exact checks passed) but relied on an independent derivation rather than that artifact for the verdict.
- GitHub compare reports no changed files under the assigned path from inventory to current main; the assigned/current tree SHA is unchanged and the audit markers remain absent.

## Limitations

- The theorem assumes closure, conditional independence of visits, common visit-specific detection probabilities, positive finite mean abundance, and finite second moment.
- Analytic-continuation identification can be severely ill-conditioned and does not by itself supply a robust nonparametric estimator.
- The equal-detection moment formula is prior work; originality is only the unrestricted-law/unequal-visit identification theorem and sharp threshold.

## Evidence and references

- https://doi.org/10.1111/j.0006-341X.2004.00142.x
- https://doi.org/10.1111/biom.12246
- https://doi.org/10.1111/biom.12734
- https://doi.org/10.1002/wics.1625
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/two-visit-nmixture-nonparametric-identification--1c1f6450764b

This guarded change set changes only the independent-audit channel in `VERIFICATION.md`; the Lean-verification and expert-attestation channels remain exactly as previously recorded.
