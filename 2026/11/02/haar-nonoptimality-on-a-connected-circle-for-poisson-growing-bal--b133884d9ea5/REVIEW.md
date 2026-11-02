# Scientific review

## Correctness — PASS
On the circle of circumference one, every cover time falls between the first Poisson arrival and that arrival plus one-half. The antipodal law has exact expectation \(9/4-e^{-1/4}\) by exponential thinning and the opposite-center threshold. Conditioning on the first Haar seed, the Poisson void formula gives the one-target survival \(e^{-u^2}\); two target locations at \(3/8\) and \(5/8\) yield the exact joint void exponent \(J(u)\) and a stronger inclusion–exclusion survival lower bound. Integrated alternating Taylor polynomials give the rational Haar-after-first bound \(29716847/62914560\), while \(e^{-1/4}\ge299/384\). This certifies \(61807/62914560>0\). Coupling the full-support mixture by independent recoloring of arrival marks changes mean cover time by at most \(3/4096\), leaving \(15727/62914560>0\). Exact arithmetic in `check.py` re-evaluates the polynomial coefficients and differences. The probabilistic statements are supplied by the analytic argument, not numerical tests.

## Originality — PASS, subject to historical-priority risk
Aldous, *Covering a compact space by fixed-radius or growing random balls* (arXiv:2101.12671v1, 29 January 2021, Section 4.2; ALEA 19 (2022), Section 7.1), asks whether Haar seed placements minimize mean growing-ball cover time on a compact group with translation-invariant metric; the published discussion does not give this connected-circle counterexample. The fixed-radius coupon-collector setting of Falgas-Ravry, Larsson and Markström (arXiv:1601.04455) has a different coverage mechanism. Results on finite cyclic groups do not logically settle connected compact groups. Searches across accessible mathematical research records and the relevant primary sources did not identify a covering connected-group statement. A failed search cannot establish absolute historical novelty, and broader unindexed literature is a residual risk.

## Value — PASS
The example resolves a natural optimality question in a nontrivial direction: even on the connected and homogeneous circle, symmetry of the geometry does not force uniform placement to be optimal for continuously growing randomly timed balls. The fully supported perturbation excludes explanations relying solely on a seed distribution restricted to a finite subset. Both conclusions are strict and certified with rational margins, making the boundary reproducible and usable in future structural work.

## Limitations and closest literature
No optimizer is characterized and the exact Haar expectation is not computed. The result applies to one normalized circle. The comparison to Aldous and the fixed-radius covering literature is material-specific; broad historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
