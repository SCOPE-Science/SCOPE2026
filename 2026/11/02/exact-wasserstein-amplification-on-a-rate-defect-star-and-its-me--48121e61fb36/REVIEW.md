# Review of the rate-defect star transport theorem

## Correctness

PASS. The exact unit-edge Kantorovich--Rubinstein dual problem is the induced edge-gradient \(\ell_\infty\)-operator norm. The generator reduces to a two-dimensional mean block plus fast-leaf contrasts, with distinct positive eigenvalues. The proof displays both classes of row sums and compares them pointwise in the two possible sign regimes; the key inequality uses \(\lambda_-\le1\) and \(\Delta\le r+1\). This prevents a hidden assumption that off-diagonal entries have one fixed sign. Exact differentiation then gives the unique peak; Taylor expansion provides the uniform-in-time weak-rate peak asymptotic at fixed degree. The independent direct heat-kernel checker passed 693 supplementary assertions. No finite computation substitutes for the global comparison proof.

## Originality

PASS with historical-priority limitations. [MW] Theorem 3.8 provides the general Lipschitz/Wasserstein semigroup correspondence, not this exact star calculation. [BLLWY] Theorem 5 concerns a nonlinear Ricci flow evolving metric edge lengths rather than the fixed metric and constant jump rates here. Published and locally accessible earlier equal-rate star and slow-bond path claims were compared by implication: the former covers only the boundary \(\varepsilon=1\), while the latter has a different path topology and does not determine all-time star amplification. Searches for weighted-star heat-semigroup norms, exceptional edge rates, and logarithmic peak laws did not reveal a dominating formula. An unindexed equivalent calculation remains possible and no independent priority certification is claimed.

## Mathematical value

PASS. The exact all-time profile, exceptional-edge attainment at every time, all-rate maximizing-time formula and sharp metastable expansion give a complete quantitative response to a natural conductance defect on a branching metric graph. The fast-edge row changes sign structure with time, so sharpness cannot be inferred solely from instantaneous curvature or the equal-rate star. The result separates fixed transport geometry from heterogeneous jump kinetics and supplies a useful finite test model.

## Scope and limitations

Finite symmetric generators only; one defect rate in \((0,1]\); unit geometric edge lengths; fixed degree in the small-rate expansion. Existing general curvature estimates and related graph families are not treated as proof of novelty. The analytic derivation is the evidence for infinite parameter ranges; finite checks provide only diagnostics.

Self-review: passed. Independent audit: not yet performed.
