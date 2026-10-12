# Self-review

## Correctness
PASS. The proof reduces the antibody-free equilibrium equations exactly to a scalar monotone equation. Boundary cases are handled explicitly, the transverse antibody eigenvalue is read from the exact Jacobian structure, and the finite humoral-invasion threshold follows by direct substitution. The bundled verifier checks the residuals and threshold sign change on an independent representative parameter instance.

## Originality
PASS. A 2014 virus-immune paper already establishes the general concept of separate antibody-invasion thresholds, so that general idea is not claimed as new. Direct full-text comparison shows that its equations do not imply the exact HPV branch, monotone scalar reduction, or closed \(\beta_A\) formula. The 2026 source itself omits the branch, and the closest recent HPV model lacks an explicit antibody state.

## Value
PASS. The missing branch changes the equilibrium census on the nonnegative state space and forces a second biologically meaningful threshold between viral establishment and antibody establishment. It also resolves the interpretation of the source's inconsistent disease-free sensitivity formula: \(q\) and \(\omega\) do not alter the DFE next-generation threshold of the printed equations.

## Closest literature and limitations
The closest structural prior is Jiang and Wang (2014), DOI 10.3934/dcdsb.2014.19.1087, which classifies multiple immune-invasion thresholds in a different HIV/HBV system. The closest recent HPV comparison is DOI 10.1038/s41598-025-02608-5, which has no explicit antibody state. The present result does not classify the five non-antibody eigenvalues, prove a transcritical bifurcation, or re-establish global dynamics for strictly positive antibody initial data.

Self-review: passed. Independent audit: not yet performed.
