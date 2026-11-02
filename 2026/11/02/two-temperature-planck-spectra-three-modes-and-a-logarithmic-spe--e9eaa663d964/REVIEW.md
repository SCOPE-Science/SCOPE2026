# Scientific review

## Correctness — PASS

The exact frequency-domain Planck sum satisfies \(F_R'=f'(x)+f'(x/R)\); this exact cancellation, the unique positive Wien-frequency root, the signs of \(f''\) near zero and above five, and the exponentially dominated transition interval prove **exactly three**, not merely at least three, stationary points for all sufficiently large \(R\). All are nondegenerate by strict second-derivative signs. The Rayleigh--Jeans and Wien tails independently determine the notch balance \(x_2^2e^{-x_2}\sim2/R\), the two-logarithm location, and the peak/valley height scales. The included standard-library checker returns `VERIFY_OK checks=25` at five temperature ratios; the analytic interval decomposition is the proof for unbounded \(R\). The theorem does not specify the smallest critical temperature ratio.

## Originality — PASS on examined evidence

Khatri, Sunyaev and Chluba (arXiv:1205.2871, publicly posted 2012-05-13) analyze exact Planck mixing mainly via a small-temperature-contrast expansion and thermodynamic entropy. Their relevant sections and conclusions do not supply a large-contrast three-mode theorem, especially not the intermediate logarithmic-notch asymptotic. Hou et al. (arXiv:1808.03942) analyze a continuous power-law temperature-distribution model, rather than two discrete temperatures at the balanced area scaling. Conventional Wien-tail calculations do not control the complete exact Planck spectrum near its cold or hot peak. Published-record and prior-claim comparisons uncovered no statement implying this complete theorem; the absence of a match is not a proof of global novelty.

**Residual risk:** A specialized early study of very widely separated two-temperature Planck mixtures could contain overlapping critical-point or notch asymptotics; priority has not been independently established.

## Mathematical value — PASS

The hot-to-cold area law \(R^{-2}\) is distinguished by cancellation of the temperature-scaling prefactors in the derivative, not a numerical special case. The theorem determines a complete mode-count classification in the high-contrast regime and resolves a physically interpretable spectral notch with a non-obvious double-logarithmic displacement and intensity scale. The result applies to an infinite family of exact radiative spectra, distinguishing them from perturbative or Wien-only models; no general phase diagram or sharp finite threshold is claimed.

Self-review: passed. Independent audit: not yet performed.
