# Same-model review

## Correctness
PASS. The claim was reconstructed from the published weighted-conformal infinity mass. The Gaussian likelihood-ratio representation, subcritical maximum comparison, supercritical fractional-moment bound, and critical truncation calculation jointly prove all three regimes. The critical identities are exact, and the argument separates analytic proof from supplementary computational checks.

## Originality
PASS. The closest direct source, Tibshirani et al. (arXiv:1904.06019), defines the weighted infinity atom and exponential tilting but does not state the growing-shift phase law. Chatterjee and Diaconis (arXiv:1511.01437) give the broader \(\exp(D_{\mathrm{KL}})\) importance-sampling sample-size scale and a source-weight degeneracy diagnostic; that prior coverage is explicitly excluded from the novelty claim. The surviving statement is the weighted-conformal independent-target atom law and, in particular, the exact critical \(1/2\) limit. A recent training-conditional weighted-conformal paper (arXiv:2609.33456) studies different coverage and clipping functionals. Targeted published-finding corpus searches found no equivalent statement. Residual risk remains from specialized lognormal triangular-array literature under different terminology.

## Value
PASS. The result identifies when exact weighted conformal prediction becomes vacuous because the test-point infinity atom consumes the miscoverage budget. The phase boundary \(D_{\mathrm{KL}}(Q_n\|P)=\log n\) is operationally interpretable, while the critical \(1/2\) law is a precise boundary phenomenon not supplied by generic importance-sampling order results.

## Limitations and closest literature
The theorem assumes a one-dimensional unit-variance Gaussian shift, known weights, fixed \(\alpha\), and finite calibration scores. It does not classify second-order critical windows or clipped/estimated weights. Generic KL-scale importance-sampling cutoff results are broader in model class but do not imply the exact conformal critical law stated here.

Same-model review: passed. Independent audit: not yet performed.
