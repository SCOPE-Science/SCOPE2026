# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The proof starts from equations (16)--(19) of arXiv:2609.19890 and expands both algebraic branches with N=floor(theta), theta=N+x. The cubic coefficient obtained after series reversion is identical on both branches. At quartic order the two expressions reduce to the same polynomial after reflecting the phase x -> 1-x. Exact symbolic verification is included in `artifacts/verify_asymptotics.py`, together with direct high-precision evaluation of the unexpanded formulas.

Adversarial checks included the integer phase x=0, the secondary-junction phase tending to x=1/2, both sides of the branch split, and the sign convention between the rho deficit 1-P and the boundary expansion P. The quartic phase polynomial is monotone on [0,1/2], so its cluster interval follows without an unproved extremization step.

## Originality

The primary source arXiv:2609.19890 is the first exact rho--gamma region identified in the literature search. Its Remark 2.2 gives only the quadratic endpoint expansion with an O((1-g)^3) remainder. Searches using the exact cubic constant, the quartic constants, “Spearman rho Gini gamma” together with Taylor/asymptotic/differentiability/endpoint terminology, and equivalent boundary/comonotonicity language did not locate the higher-order statements proved here.

The closest prior source is arXiv:2608.20176, whose rho--footrule transport optimizer supplies data later reused in arXiv:2609.19890. That older work is a residual originality risk because a sufficiently general unpublished or unstated high-order expansion of its optimizer could imply parts of the present calculation mechanically. No such statement was located. Accordingly the originality claim is only “to the best of our knowledge” and is restricted to the explicit rho--gamma cubic coefficient, quartic phase function, and quartic cluster interval.

No inaccessible source produced concrete evidence of prior coverage. Older concordance-region papers were inspected at abstract/result level where relevant, but not every historical paper on copula concordance was checked line by line. This leaves the ordinary residual risk of an equivalent older asymptotic formulation, although the exact rho--gamma boundary itself was only resolved in the 2026 source.

## Value

The source boundary consists of countably many algebraic pieces accumulating at comonotonicity. The result identifies exactly when that piece structure first becomes asymptotically visible: not at quadratic or cubic order, but at quartic order. The cluster interval also gives a concrete endpoint regularity obstruction that is not apparent from the source's O((1-g)^3) statement.

## Limitations

The analysis is local to the comonotonic endpoint of the rho-maximal boundary. It does not classify smoothness at every interior breakpoint, does not address empirical rank-statistic sampling laws, and does not claim independent validation.
