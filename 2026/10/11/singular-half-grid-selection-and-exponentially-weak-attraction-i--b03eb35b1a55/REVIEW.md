# Scientific review: singular half-grid selection in EOS maps

## Correctness

**PASS.** For fixed coprime \(k,n\), the half-grid \((j+1/2)/n\) has exactly two sites at minimum distance \(1/(2n)\) from the smoothing layer. The cycle's return displacement is the sum of signed logistic tails. Bracketing at \(\pm e^{-a/(4n)}\) proves existence and contraction on the chosen outer-lap itinerary. The exact periodicity sum, reflection symmetry \(g_a(-x)=1-g_a(x)\), and a derivative lower bound force the two nearest sites to sum to \(O(e^{-a/n}/a)\). Transport of the signed tail corrections gives the stated \(\pm\tfrac12e^{-a/(2n)}\) profile; the two nearest logistic derivatives give the sharp multiplier. The numerical script checks five rational cases but is not a proof of the asymptotic statement.

## Originality

**PASS within the inspected literature, with residual risk.** Bielawski et al., arXiv:2411.01495v1, Theorem 3.3 proves existence and almost-everywhere attraction for fixed rational rotation, while Sections 4–5 give large-steepness conditions and an approximate truncated-map explanation of numerator-independence. They do not give the half-grid first-order displacement or the exact return-multiplier asymptotic, and Section 5 disclaims rigorous quantitative bounds for its bifurcation comparison. Chotibut et al., arXiv:1807.06831v1, Theorem 3.9 treats the symmetric period-two case and Theorem 3.11 large-parameter chaos for asymmetric cases, not a general-denominator asymptotic of the attracting cycle's local derivative. Related smooth-rotation and attracting-cycle records were searched by model, multiplier, singular limit, and near-neutral Floquet aliases. Unindexed or older equivalent calculations remain possible; this is not independent novelty certification.

## Mathematical value

**PASS.** The motivating problem concerns how continuous interval maps retain rotation-like attracting dynamics as their smoothing becomes singular. Merely proving attraction leaves its strength undetermined. The exact decay \(1-\Lambda_a\sim2a e^{-a/(2n)}\) shows that the limiting highly attracting-looking orbit instead loses its local spectral gap exponentially, with a denominator-dependent scale but numerator-independent leading coefficient. The full first-order position profile resolves how the numerator persists in orbit geometry. These facts are natural for understanding long transients in the published population and learning-map models; they do not assert global hitting-time bounds.

## Closest literature and limits

[1] Bielawski et al., *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, Sections 2–5, November 3, 2024. [2] Chotibut et al., *Family of chaotic maps from game theory*, arXiv:1807.06831v1, Sections 2–3, July 18, 2018. The result fixes \(n,k\) first and lets \(a\) diverge. It does not classify all higher-period repelling cycles, give a threshold in \(a\), or establish global convergence-time estimates.

Same-model review: passed. Independent audit: not yet performed.
