# Scientific review

## Correctness — PASS

The random-state definition agrees with the motivating Kaczmarz momentum update at \(\beta=0\). Averaging the two explicitly constructed real \(4\times4\) state matrices yields reflection-even and reflection-odd covariance blocks of sizes six and four. Their two zero-momentum characteristic polynomials give a simple leading eigenvalue for every \(0<c<1\). Differentiating its exact characteristic polynomial gives the stated strictly negative derivative; differentiating twice gives the sharp weak-coherence coefficient. The orthogonal obstruction follows from a directly derived scalar three-moment cubic with a real root strictly above \(1/2\). Analytic perturbation and positivity of the leading observable justify the claimed root rate for all nonzero deterministic starts near zero momentum. The implicit-function theorem, odd-sector spectral gap, and compactness plus strict orthogonal slowdown prove global uniqueness of the weak-coherence optimal momentum. Independent re-expansion and 285 deterministic checker assertions passed. Finite testing is not substituted for proof.

## Originality — PASS, with residual risk

The original article proves signed directional mean formulas and raises Euclidean-norm behavior as a separate question; it does not calculate the exact nonorthogonal two-row squared-error derivative or the weak-coherence global optimum. An earlier orthonormal KGSM classification establishes a stability frontier, but expressly does not classify nonorthogonal row pairs. The existing diagonal-row work extends mean-square stability to unequal probabilities without the row-coherence variable. Published cyclic two-row Kaczmarz work addresses deterministic row order and overrelaxation, not iid squared-error momentum rates. The minibatch heavy-ball analysis provides general estimates, not this exact pointwise first derivative and quartic optimality law. The checked sources do not imply the final statement; equivalent older formulations in stochastic heavy-ball or random-matrix perturbation theory remain possible, and independence of priority is not certified.

## Value — PASS

The result settles a motivated squared-norm question in the smallest nonorthogonal system where row geometry matters. It identifies an exact structural contrast: positive momentum is detrimental at orthogonality but beneficial for every fixed positive coherence. The sharp \(c^2\) momentum and \(c^4\) rate laws provide a meaningful benchmark for designing and diagnosing stochastic momentum on weakly coupled linear systems. It is more than a stability-sign check because it supplies a normalized full second-moment operator, exact geometry sensitivity, and a proved unique global optimizer in a singular weak-coherence regime.

## Scope and uncertainty

Exact arithmetic, two real independent normalized rows, iid equal row probabilities, consistent equations, unsmoothed momentum, zero velocity. No higher-dimensional, noisy, smoothed, general-coherence optimal-parameter, or almost-sure theorem is asserted. Some less searchable historical equivalences may remain; independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
