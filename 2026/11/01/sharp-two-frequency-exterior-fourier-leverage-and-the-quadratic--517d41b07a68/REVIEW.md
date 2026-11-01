# Scientific review — exterior two-frequency leverage

## Correctness: PASS

The proof is reconstructible from elementary orthogonality and the reproducing kernel of the two-dimensional exponential space. The fixed-gap formula and equality cases follow from the exact norms of sine and cosine. The global bound uses an explicit strict high-gap bound, an elementary sine comparison at low gaps, and a positive second-derivative certificate for the endpoint value. Taylor expansion yields the stated positive quadratic loss. The executable supplementary checker returned 448 passed assertions at high precision. The script does not certify infinitely many gaps; the analytic proof does.

## Originality: PASS relative to inspected sources

Zhang's July 2026 full text treats the same extrapolation setting, but proves a general-order upper bound and qualitative/exponential-scale sharpness rather than the exact universal \(k=2\) constant, the fixed-gap evaluator, or the quadratic collision coefficient. Chen and Price's full text (2019, §8.3) gives polynomial/exponential upper estimates. Erdélyi's cited endpoint result is not an exact exterior pointwise statement. Searches of the mathematical results database and open literature for the exact formula, aliases, reproducing-kernel interpretation, and two-frequency gap dependence yielded no covering statement. The abstract of Borwein–Erdélyi (2000) was examined; its complete text could not be accessed, so possible equivalent older work is a genuine residual risk. Negative search results alone are not proof of novelty.

## Value: PASS

This solves a naturally motivated exactly sharp two-atom case of an active recent extrapolation problem. The quantitative result describes the worst possible price of predicting outside a sampled interval even when arbitrarily close frequencies make the coefficient representation ill-conditioned. The fixed-gap kernel and its \(d^2\)-order loss provide a precise benchmark for clustered-spectrum regression and distinguish intrinsic prediction stability from coefficient instability. Its scientific value does not rely on numerical testing.

## Scope and limitations

Only real two-frequency sums and pointwise real exterior extrapolation are treated. The coefficient of \(d^2\) is for each fixed \(x\); no uniformity as \(|x|\to\infty\) is asserted. Historical coverage risks remain, and no external audit has occurred.

Self-review: passed. Independent audit: not yet performed.
