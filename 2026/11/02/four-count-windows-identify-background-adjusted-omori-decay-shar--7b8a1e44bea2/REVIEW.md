# Scientific review

## Correctness (PASS)

For arbitrary four chronologically disjoint nonzero-width windows, equal expected counts of two curves give four distinct real zeros by the integral mean value property. Differencing two positive background-adjusted power laws gives a derivative whose zero equation is a fixed horizontal section of a function with at most one turning point. Hence four zeros force identical parameters. The same result for three windows with known background follows from direct comparison of two shifted powers. The nonzero four-column and reduced three-/two-column Jacobians are proved by multiplying derivatives by a positive power, reducing root counts to a function whose second derivative has at most one zero. The implicit function theorem proves the necessary local ambiguity with fewer windows. The exact three-crossing witness and numeric quadrature/Jacobian checks agree with the proof. Numerical tests do not replace the continuous proof.

## Originality (PASS, provisional)

The full-text 2015 study by Gardonio et al. models post-Tohoku intensity as a constant background plus shifted Omori power law. The 2012 Holschneider et al. full text examines parameter uncertainty in the three-parameter version, while Ogata's 1983 primary paper presents likelihood estimation of the three-parameter model and discusses interval counting. These papers motivate the fitted intensity, but their inspected sections do not give the sharp global identification of all four parameters from four arbitrary **expected-count bins**, the known-background three-bin threshold, or the exact maximal number of crossings. Finite-dimensional Chebyshev and variation-diminishing theory may supply a general theorem implying these conclusions, even though no exact covering formulation was found in targeted searches. Independent historical-priority review remains appropriate.

## Value (PASS)

Seismicity is reported over observation windows, with baseline earthquakes superimposed on triggered aftershocks. The theorem gives the minimum number of independent exact bin expectations needed to disentangle background, productivity, onset offset and decay exponent, under arbitrary irregular monitoring windows. It supplies a sharp baseline-known versus baseline-unknown distinction, plus local nonsingularity and an explicit three-intersection ambiguity witness. This answers a natural structural experimental-design question rather than merely counting parameters; the underlying count-to-crossing argument is valid for arbitrary windows. The result does **not** recommend fitting four actual random counts without uncertainty quantification.

## Closest literature, scope, and outstanding verification

Gardonio et al. (2015), DOI 10.1002/2014JB011798, Section 2, supplies the background-adjusted aftershock rate used here. Holschneider et al. (2012), DOI 10.1029/2011JB009054, treats Bayesian uncertainty in the baseline-free rate. Ogata (1983), DOI 10.4294/jpe1952.31.115, studies likelihood estimation for the baseline-free Omori intensity, not the four-parameter finite-bin result. The latter was inspected in accessible PDF text; an attempted page-image retrieval timed out. Residual risks are unlocated general zero-count results and poor practical conditioning; neither is claimed resolved.

Self-review: passed. Independent audit: not yet performed.
