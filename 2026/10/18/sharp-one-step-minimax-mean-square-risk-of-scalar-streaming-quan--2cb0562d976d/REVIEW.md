# Scientific review

## Correctness

PASS. The exact squared-risk factor follows by conditioning on whether the update measurement is corrupted and on the binomial count of corrupted calibration measurements. In the clean-update case, \(J<k\) forces acceptance, and \(J\geq k\) allows rejection. In the corrupted-update case, \(J\leq D-k\) forces a quantile at most the clean residual and caps the accepted scalar error ratio at \(2\); if \(J>D-k\), the amplitude limit gives the sharp ratio \(B\). Each extremum is attained by an indicator-adaptive corruption assignment explicitly given in RESULT.md. Stirling and geometric binomial-tail estimates establish the \(\log B\) and \(\log\log B\) terms, with bounded lattice effects. Finite enumeration in CHECK.py corroborates, but does not substitute for, the proof.

## Originality

PASS, subject to the specified residual literature risk. The streaming Massart QRK primary source analyzes dimensions at least two and high-probability performance with an excluded catastrophic-event region. The 2025/2026 subsampled-QRK source establishes logarithmic-in-horizon failure and possible arbitrarily large outliers. Neither inspected source states or implies the complete exact scalar **unconditional** minimax risk formula together with the quarter-corruption boundary and the two-term amplitude calibration law. Published mathematical-record searches for aliases, binomial-tail forms, and mean-square envelopes found no equivalent full claim; search incompleteness and the elementary scalar specialization remain residual originality risks. The observation that enormous outliers can cause catastrophic failure is credited to earlier work and not represented as the novelty.

## Value

PASS. The precise conditional squared-risk envelope answers a practical mathematical question left open by the contrast between high-probability and mean-square convergence analyses: how large a quantile calibration batch is needed when adversarial corrupted observations have a known **relative** magnitude bound? The exact critical corruption level, discrete finite-batch evaluation, and sharp second-order amplitude budget quantify a natural reliability tradeoff. The dimension-one character is openly stated, and no higher-dimensional threshold is inferred.

## Boundaries and sources

Primary source: arXiv:2608.27968 (streaming rule and Massart adversary). Nearest precursor: arXiv:2507.15185 (subsample/high-probability catastrophe results). Foundational quantile Kaczmarz: arXiv:2009.08089. These are not independent validations of the present calculations. This work assumes exact arithmetic, independent corruption indicators, and state-relative magnitude bounds; robust multi-dimensional performance and general unbounded-amplitude unconditional guarantees are outside its scope.

Self-review: passed. Independent audit: not yet performed.
