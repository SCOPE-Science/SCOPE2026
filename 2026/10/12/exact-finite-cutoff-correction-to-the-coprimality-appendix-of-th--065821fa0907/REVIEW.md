# Review: Exact finite-cutoff correction to the coprimality appendix of the continuous-variable Shor algorithm

## Correctness
PASS. Both exact counting formulas are immediate consequences of Möbius inversion. The counterexamples are exact, and the limiting formula follows from periodic reduced-residue density, dominated convergence with a \(d^{-2}\) majorant, and the absolutely convergent Euler product. The attached checker independently matches the formulas to brute-force counting on a grid and reproduces all three counterexamples.

## Originality
PASS. The final anchor source retains the finite propositions. The inspected same-author follow-up and broad hidden-subgroup review do not contain the source-specific correction. Focused searches by identifier, proposition wording, aliases, coprimality constant, and erratum language found no implication-equivalent result. The closest search results concern generic coprimality or Euler-product problems rather than this appendix.

## Value
PASS. These finite probability lemmas are explicitly used to motivate the source's rational-period repetition estimate. The correction is therefore mathematically consequential: it removes an unsupported finite-uniform guarantee, provides exact replacement formulas, and identifies the valid fixed-parameter asymptotic regime.

## Closest literature and limitations
The anchor paper is necessarily the closest prior work because it contains the statements being corrected. The same-author hidden-subgroup follow-up is algorithmically related but does not supply the correction in the inspected portions. This result does not model physical noise or prove what exact discrete law a finite-resolution continuous measurement produces. An unindexed erratum remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
