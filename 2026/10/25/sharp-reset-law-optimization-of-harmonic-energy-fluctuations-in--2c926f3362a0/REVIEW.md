# Scientific review

## Correctness — PASS

The proof uses the canonical nonnegative squared-CIR representation, for which regeneration at positive Poisson rate proves a unique stationary law. Two generator moment equations for the squared position give the exact stationary first and second moments for *any* independent positive reset law with finite fourth moment. Algebraic completion of the square yields a strictly positive mismatch coefficient and a strictly positive reset-law dispersion penalty. The admissible domain \(\mathbb E R^2>0\), \(\operatorname{Var}(R^2)\ge0\) gives the interior versus excluded-boundary dichotomy without further analytic regularity hypotheses. The included program samples independent stationary observations using the noncentral chi-square CIR transition and checks the main identities, but numerical agreement is not treated as a universal proof.

## Originality — PASS (qualified)

The entire original logarithmic-harmonic stationary point-reset **density** is prior art (Gültekin, arXiv:2306.08770). General renewal ideas and moment equations under randomized reset positions are also prior techniques (Olsen, arXiv:2310.04840). The claim is not either of those: it is the sharp global minimizing reset *law* for the variance of the squared position, the exact rate threshold, and both penalty terms. Gültekin's 8-page preprint was examined through its model, density derivation and discussion; it does not state the present optimization or analyze arbitrary reset distributions. Olsen's 8-page preprint was examined through Sections II–V, including Eq. (22) and the additive-OU variance Eq. (24); it covers a different noise structure and observable. Searches for logarithmic-harmonic/CIR reset-law variance optimization did not identify a directly covering theorem, but this is not a uniqueness proof. The main residual risk is unlocated optimization in the larger affine-diffusion or resetting literature.

## Mathematical value — PASS

The optimized variance is the natural fluctuation measure for the trap's quadratic energy component. The result is a complete nontrivial design classification over an *infinite-dimensional family of resetting distributions*, not a single-parameter example: randomizing the reset site has a sharp strictly positive variance cost, while a unique boundary-crossing rate separates an attained finite-location optimum from an unattained limit. The square-root approach to that boundary and exact variance penalty make the classification quantitative. This does not optimize full-potential variance or the energetic expense of the reset operation.

Self-review: passed. Independent audit: not yet performed.
