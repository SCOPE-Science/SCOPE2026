# Same-model review

## Correctness
PASS. The Gaussian covariance calculation gives independent \(U\) and \(V\), and standardization yields the exact product formula for joint selection and rejection. Reparameterizing by \(\theta=\arctan\tau\) makes the Fisher-information fractions \(\cos^2\theta\) and \(\sin^2\theta\). The proof reconstructs the first and second derivatives of the log objective and uses the strict decrease of \(h(x)=\phi(x)/\Phi(x)\) to establish a unique interior optimum. The \(\tau_*>1\) conclusion follows from the derivative at \(\pi/4\), and the weak-signal limit follows directly from the root equation. The bundled verifier reproduces all reported numerical values.

## Originality
PASS with residual literature risk. Targeted literature-database searches for Gaussian data fission, one-sided screening/confirmation, inverse-Mills optimality, and Cox-style split allocation found no equivalent SCOPE finding. The full text of García Rasines and Young was inspected: it gives the Gaussian \(U,V\) decomposition, the information split, and says the representation offers a possible way to select randomization variance, but it does not state this scalar product objective or its optimizer. Leiner et al. supply the broader fission framework rather than this tuning law. Tian and Taylor analyze randomized selective inference rather than independent confirmation. Cox (1975) is the main unresolved older risk: its abstract promises recommendations for split proportions in a many-normal-means problem, but accessible material did not expose the article's formulas and the full text could not be inspected.

## Value
PASS. Choosing the fission noise level is a central design decision because it transfers Fisher information between selection and confirmation. The theorem gives a complete answer for a canonical scalar benchmark and exposes a non-obvious asymmetry: conventional significance thresholds make equal information splitting strictly suboptimal for every positive signal. The local \(13.0\%/87.0\%\) information split at \(\alpha=0.05\) is a natural, signal-free benchmark, while exact null-boundary invariance shows the improvement is not bought by increasing the boundary-null joint rejection probability.

## Closest literature and limitations
The closest inspected source is García Rasines and Young (arXiv:2102.02159 / *Biometrika* 2023), especially their Gaussian decomposition and information-averaging section. Leiner et al. (arXiv:2112.11079) provide the data-fission formulation. Tian and Taylor (arXiv:1507.06739) are a broader randomized-response predecessor. Cox (1975) is a plausible older allocation predecessor but was available only at abstract level in this review. The theorem is limited to a scalar known-variance Gaussian model and the specified screen/confirm objective.

Same-model review: passed. Independent audit: not yet performed.
