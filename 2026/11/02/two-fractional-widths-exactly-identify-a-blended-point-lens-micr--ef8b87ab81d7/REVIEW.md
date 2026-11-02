# Scientific review

## Correctness — PASS

The physical scope and all universal quantifiers are explicit in RESULT.md. The exact inverse amplification is checked by direct algebra, the two width identities use cancellation of the constant source fraction, and the strict derivative identity
\[
\partial_y\log(h_y(s)/h_y(t))=3(t-s)/[(ys+2)(yt+2)]>0
\]
for \(s<t\) proves the ratio comparison on an entire positive-measure rectangle, not a finite grid. Dominated convergence on bounded intervals away from zero supplies both endpoint ratios; strict monotonicity supplies the unique inversion, image range and minimality. The standalone checker tests forward and inverse equations across positive parameters with 75-digit decimals. No finite output is relied on as proof of the infinite quantifiers. All boundaries are one-sided and correctly open or closed.

## Originality — PASS within inspected material; independently unverified

The primary scientific comparisons are the actual texts of Woźniak–Paczyński (1997), Han (1999), and Smith et al. (2007), with arXiv/Oxford URLs in RESULT.md. Woźniak–Paczyński establish the blended light model and practical asymptotic degeneracies; Han proves forward threshold-duration relationships and dependence of inferred parameters on blending; Smith et al. study realistic survey bias and noisy fitting. Their full inspected sections do not state the peak-referenced *two*-width ratio as a global strict order invariant, the complete feasible range, or the sharp one-width insufficiency. The Han forward relation and the fact that noiseless full curves can in principle carry parameters are *not* claimed as new. published-finding corpus and published-literature searches for aliases, ratios and inverse identifiability found no identified exact covering result; those negative searches alone are not novelty certificates. An unlocated earlier note or a straightforward but unstated implication of Han remains a residual priority risk. No independent review was performed.

## Value — PASS

Blending is a central obstacle to recovering microlensing event parameters, explicitly established in the 1997 and 2007 sources. The theorem gives a sharp and natural minimal collection of three directly defined shape observables, separates structural uniqueness from numerical degeneracy, characterizes all possible observation triples, and provides a model-incompatibility inequality. The proof's strictly ordered ratio and exact domain do not follow from a single forward-width formula without a global shape comparison. This is a theoretical inverse-data statement, not a claim about observational accuracy, lens masses or field performance.

## Literature and scientific limitations

Sources: https://arxiv.org/abs/astro-ph/9702194 ; https://academic.oup.com/mnras/article/309/2/373/1029545 ; https://arxiv.org/abs/0707.0550 . The first was publicly available on 1997-02-21. This work excludes measurement noise, negative blends, finite sources, multi-lens events, parallax, variable baselines and unknown peak time. Near limiting shape-ratio values, inversion can be poorly conditioned. This review has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
