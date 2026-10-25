# Scientific review: nested hyperbolic zero-count covariance

## Correctness — PASS

The exact logarithmic covariance identity, Jensen differentiation and the normalized hyperbolic kernel give a finite-radius covariance integral. At distinct boundary gaps, the normalized kernel stays uniformly below one, permitting dominated mixed differentiation after angular rescaling. A positive dilogarithm series and the beta integral give the explicit absolutely convergent all-intensity series; Buckley's single-radius variance establishes the coincident-radius endpoint. An exact binomial generating function sums the intensity-two series. The polynomial identity \((1+v^2-v)^2(2-v^2)-1=-(1-v)^2(v^4+2v-1)\), monotonicity of the quartic, and strict asymptotic convergence establish the exact sign crossing. The extracted checker passes 43 numerical/symbolic tests including the finite-radius integral, known intensity-one formula and known intensity-two variance. Risks: termwise limiting formulas require fixed positive boundary-gap parameters; near the transition, finite-radius signs are not asserted.

## Originality — PASS, qualified

Buckley (2013; arXiv:1307.6674) gives the one-radius hyperbolic zero-count variance and a general log-covariance representation, but does not identify the two-radius boundary-layer kernel, its sharp intensity-two algebraic threshold or its sign reversal. Buckley–Nishry (2021; arXiv:2104.12598) concerns single-disk asymptotic limit laws; the same Gaussian analytic object does not make its one-parameter theorem imply the two-parameter sign diagram. The determinantal Peres–Virág intensity-one process has a positive nested-disk covariance, so is a genuine contrast, not direct coverage. Mor Waknin (2022; arXiv:2209.05854) concerns single-disk overcrowding. Actual semantic research-record searches for the exact quartic, aliases, boundary-gap ratios, and negative nested zero-count covariance returned no dominating matching statement; closest hits concerned different objects. An accessible earlier planar two-circle covariance claim treats a Gaussian entire function rather than this hyperbolic GAF and does not imply the result. Residual risk: a calculation of the same quantity may be implicit in more general Gaussian pair-correlation literature; the absence of a retrieved title is not a novelty proof.

## Value — PASS

The zero count in a disk is a natural linear statistic of a conformally invariant zero process. The question whether increasing nested counts can be negatively correlated is structural, particularly because the intensity-one case is determinantal and positively correlated. The theorem supplies an exact sign boundary for the first non-determinantal integer intensity, an algebraic transition in the ratio of boundary gaps, and a general-intensity negative-covariance regime. It resolves a genuinely geometric covariance question, not a relabeling or routine tabulation.

## Closest literature and limitations

Primary sources are Buckley 2013 (one-radius variance), Buckley–Nishry 2021 (one-radius limit laws, same model) and Peres–Virág 2005 (intensity-one determinantal case). The proof is complete for fixed positive boundary gaps and intensity above one, with unique threshold only at intensity two. At the precise zero of the leading term, subleading finite-radius signs are unknown. Remaining historical priority risk is an unstated equivalent deduction from broader formulas; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
