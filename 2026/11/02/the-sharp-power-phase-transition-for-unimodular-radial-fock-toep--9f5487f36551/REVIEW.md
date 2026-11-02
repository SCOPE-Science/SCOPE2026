# Scientific review: radial power-phase Fock Toeplitz transition

## Correctness: PASS
The eigenvalue formula follows from degreewise radial diagonalization with Gamma shape \(n+d\). The regime below \(\alpha=1/2\) follows from a mean-value estimate on Gamma concentration; the boundary multiplier \(e^{-1/8}\) follows from the Gaussian characteristic function and the delta method. Above the boundary, a centered Gamma cutoff with width \(k^{1/2+\varepsilon}\) and arbitrarily repeated nonstationary integration by parts gives faster-than-polynomial eigenvalue decay. Polynomial multiplicity then implies every Schatten exponent. Elementary Weyl-sum estimates and weighted summation give the circular weak limits. This is an analytic proof; 63 numerical assertions only corroborate it.

## Originality: PASS (historical-priority caveat)
Closest known prior work is Grudsky–Vasilevski's 2002 exact radial diagonalization and exponentially compact phase \(e^{i|z|^2}\), Esmeral–Maximenko's 2015 critical real symbol \(\cos|z|\), and Dewage–Ólafsson's 2021 quasi-radial eigenvalue calculus. These establish important subcases or a general framework, but the inspected statements do not imply the combined sharp threshold for every \(\alpha>0\), the complete complex circular essential spectra, the multiplicity-weighted spectral distribution, and all-Schatten conclusion for \(\alpha>1/2\). General compactness theorems can subsume isolated compactness assertions, not the entire claimed phase diagram. Related prior results on square-root tones do overlap one boundary family and are credited; search absence cannot establish novelty.

## Value: PASS
The natural geometric question is how the radial oscillation speed interacts with the \(\sqrt k\)-scale inherent in Gaussian monomial mass. The critical exponent precisely divides noncompact circular spectra from super-polynomial spectral suppression of an everywhere unimodular symbol; the exact nontrivial boundary radius and limiting eigenvalue distribution make this a structured operator-theoretic classification, rather than a change of notation or a routine numerical bound. The all-Schatten strengthening and spectral distribution are useful in Fock localization, operator ideals, and non-selfadjoint spectral approximation.

## Limitations and closest literature
The full classification holds only for the specified radial power-phase symbols in fixed finite complex dimension. It does not assert a uniform crossover scaling, general phase conditions, exact Schatten norms, or publication priority. Relevant inspected sources are Grudsky–Vasilevski (2002), Esmeral–Maximenko (2015), Dewage–Ólafsson (2021), Wu–Zheng (2021), and Fulsche (2024). Broader unsearched historical literature may contain equivalent formulations. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
