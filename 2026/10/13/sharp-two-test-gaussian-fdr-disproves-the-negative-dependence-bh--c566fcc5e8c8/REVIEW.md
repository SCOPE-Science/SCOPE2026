# Self-review

## Correctness (PASS)

The complete claim is the sharp two-test supremum and explicit positive-definite Gaussian violation. Exact BH rejection-event partition yields the \(3\alpha/4\) upper bound for any joint law having a single exact-uniform null \(p\)-value. The antithetic shifted-normal construction attains equality in the singular boundary, and bounded convergence proves the lower bound as positive-definite correlations approach \(-1\). For the explicit correlation \(-99999999/100000000\), a Chebyshev-plus-normal-density argument bounds the chance of a changed alternative BH decision by \(29/5000\). Thus the FDR is at least \(317/10000\), strictly above the conjectured RHS, itself bounded above by \(30307/1088000\). Python exact-fraction checks replay these rational inequalities. No numerical simulation is used to infer an infinite or continuum assertion. Source framework: Chi--Ramdas--Wang [1, Sections 2, 3, 5, 7].

## Originality (PASS; literature risk remains)

Chi--Ramdas--Wang [1] explicitly formulate the Gaussian negative-dependence BH conjecture and provide its precise proposed function in equation (26). The published 2001 Benjamini--Yekutieli dependence correction already gives the general two-test upper bound, so that part is *not* claimed as new. The nontrivial difference is Gaussian attainability in a null/nonnull model, coupled to an explicit nonsingular counterexample to the conjecture. The closest other mathematical record concerns the Simes test with three *uniform nulls* under pairwise independence, which does not imply the present assertion. Searches for antithetic/countermonotone Gaussian BH counterexamples found no equivalent statement; an unknown prior formulation remains possible, and no independent priority audit has been performed.

## Value (PASS)

This supplies a rigorous negative resolution of an explicit open conjecture from a substantial paper on FDR control under negative dependence. It identifies a structural reason for the failure: the false-null marginal can be aligned antithetically with the BH first-stage threshold even though both Gaussian test statistics have nonpositive correlation. The sharpness result specifies the extremal finite problem rather than just presenting a numerical violation. No assertion is made about three or more hypotheses.

## Closest references and limits

[1] Chi, Ramdas, Wang, *Multiple testing under negative dependence*, arXiv:2212.09706v4, equations (11), (26), Section 7.
[2] Benjamini, Yekutieli, *The control of the false discovery rate in multiple testing under dependency*, Annals of Statistics 29 (2001), DOI:10.1214/aos/1013699998.
[3] *Sharp Simes size under pairwise independence for three uniform p-values*, mathematical record dated 2026-09-20, identifier `2026/9/20/SCOPE-sharp-simes-size-under-pairwise-independence--9fdb218c11c0`.

Self-review: passed. Independent audit: not yet performed.
