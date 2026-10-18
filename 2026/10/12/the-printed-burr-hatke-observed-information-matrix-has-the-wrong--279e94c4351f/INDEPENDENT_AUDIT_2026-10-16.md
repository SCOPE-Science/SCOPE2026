# Independent mathematical audit

## correctness

PASS

PASS: In source progressive-censored log likelihood each alpha enters as sum log[alpha(t+1)+1] plus linear terms, hence second derivative equals minus sum[((t+1)/(alpha(t+1)+1))²]. Observed Fisher information I=-H has positive diagonal and zero mixed terms; source prints those negative Hessian entries as I. Its printed matrix is -D for D positive definite, so the delta-method variance v^T(-D)^(-1)v<0 for any nonzero reliability gradient, and literal normal/logit Wald standard errors are nonreal. Positive measurements and alpha>0 handle boundaries; alpha outside source not asserted. Independently inspected source likelihood/CI formulas and derivative and gradient script; finite stress-strength example is diagnostic only.

## originality

PASS

PASS (narrow): Source gives a general negative-Hessian definition and separate censored log likelihood, but does not state the corrected positive Burr-Hatke observed-information matrix or its negative-delta-variance implication. General Fisher information positivity is a textbook fact and is credited; source-specific mismatch is not explicitly covered. Search did not find corrigendum. Strong overlap with routine differentiation is a value risk.

## value

PASS

PASS: The source presents asymptotic normal and logit-Wald confidence intervals for censored multicomponent reliability. Every literal use of its printed information matrix yields a negative delta variance and undefined real intervals, so the corrected source-specific positive diagonal matrix is necessary to reproduce or responsibly use those reported analytical procedures. Although differentiation is elementary, the inferential consequence is substantive and the source nowhere provides the corrected matrix. Does not allege authors’ code used it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
