# Scientific review: causal exponential-difference scale spectra

## Correctness

**PASS.** The normalization is reconstructed from the elementary identity \(\langle h_a,h_b\rangle=1/(a+b)\). A four-term factorization gives the exact Gram coefficients, including the diagonal value one and positivity at every offset. The logarithmic change of variables is unitary, and the Mellin transform yields the stated Gamma factor and its hyperbolic-secant modulus. Poisson aliasing has the required \(1/L\) factor. Positivity of the resulting continuous symbol proves Riesz stability and Fejér concentration proves optimality of the minimum and maximum. The two-range argument near \(\theta=\pi\) gives the sharp dense-scale minimum without assuming the fixed-ratio minimizer. Exact-rational checks and spectral comparisons replay successfully. These checks are supplementary to the analytic proof.

## Originality

**PASS under inspected evidence.** Pedersen--Lindeberg--Gerstoft (arXiv:2609.17201, Sections 4.3 and 5.1) give the causal difference-of-exponentials filter and frequency-wise filter-bank bounds, and introduce finite interchannel Gram matrices. They do not state the normalized infinite-dilation Gram symbol, its Riesz constants, or the essential-singularity condition-number law. Lindeberg's earlier scale-normalization discussion (arXiv:2510.05834, Sections 2.8 and 3.2) concerns causal constructions and scale covariance, not this spectral minimum. General Mellin and translation theory can supply a method but does not itself give the explicit \(64\pi\) coefficient. Related published results about translated exponential sampling and unrelated Gabor frame bounds concern different operators and do not imply the claim. Historical implicit coverage cannot be excluded completely.

## Value

**PASS.** Adjacent causal exponential integrators are a concrete primitive for logarithmically spaced time-frequency channels. The theorem gives exact spectral control of their normalized scale coefficient system for every \(c>1\), and proves that denser scale placement causes an essentially exponential conditioning penalty \(\sim L^2e^{\pi^2/L}/64\). This quantifies a design tradeoff that cannot be read off from single-channel bandwidths or norms. It is a structural stability result rather than a single arbitrary numerical example.

## Scientific boundaries

No claim is made that the unshifted dilates are a frame for the full time-domain space. Their Gram/Riesz bounds differ from bounds for signal analysis by a filterbank with all temporal translations. For individual fixed ratios the minimum is specified by an explicit positive periodic symbol; the proof does not classify its exact minimizing angle. The dense-scale leading terms are exact asymptotics, not uniform-in-scale finite-channel formulas. Possible older equivalent Mellin identities remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
