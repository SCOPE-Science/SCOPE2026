# Self-review

## Correctness — PASS

The claim reconstructs the Gamma construction with precisely specified shapes, normalization, positivity, finite concentration, and fixed-proportions limits. Conditioning on independent normalized Gamma directions derives the entire cross-covariance matrix. The Beta second moment and conditional variance establish the exact strictly signed bias. An explicit Gamma CDF comparison yields the exponential race at low concentration; the independent Dirichlet directions collapse to simplex vertices, giving the full limiting categorical coupling. Chebyshev and boundedness give the high-concentration correlation limit. The exact identities were reproduced by the supplied finite checker as a standalone program; finite diagnostics do not prove the continuum results.

## Originality — PASS with priority risk

The closest research is Trick, Jäkel and Rothkopf (arXiv:2104.08069), with the Gamma/Dirichlet model and exact covariance, and Trick, Rothkopf and Jäkel (METRON 2023, DOI:10.1007/s40300-023-00247-2), which explicitly leaves the accuracy of its equal-margin linear rule open. The new global one-sided error formula, the two sharp concentration endpoints, and the categorical joint limit are not stated or implied by a stronger theorem in their inspected texts. Their exact covariance formula is a starting identity, not an accepted statement of the new asymptotics. Companion classifier-fusion literature and relevant public research-record matches concern different claims. The complete 2004 Magnussen article was inaccessible (only abstract available), so an earlier equivalent statement cannot be excluded; neither search absence nor metadata constitutes a novelty certificate.

## Value — PASS

The result settles a well-identified calibration question for the natural equal-marginal proportional-sharing family. It shows the linear proxy always errs in the same direction and has a nonvanishing relative error at low concentration, while the rare-concentration law explains that error by an exact shared-category/independent-category mixture. The simplex-dimensional covariance factor and categorical coupling extend the binary understanding without claiming a general model-sized classification.

## Limits

Proportional shared shapes and identical Dirichlet margins are essential. No claim is made for unequal marginals, nonproportional sharing, monotonicity in concentration, uniform error bounds, or total-variation convergence to a singular measure. Full bibliographic priority remains independently unconfirmed.

Self-review: passed. Independent audit: not yet performed.
