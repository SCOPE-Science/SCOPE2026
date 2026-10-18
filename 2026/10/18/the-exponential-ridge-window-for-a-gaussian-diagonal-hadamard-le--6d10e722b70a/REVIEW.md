# Scientific review: exponential ridge window in Gaussian-diagonal Hadamard regression

## Correctness (PASS)

For an explicit orthogonal one-column design and residual, direct multiplication of the unnormalized Hadamard columns establishes the scalar formula for the sketched ridge estimator with the specified penalty normalization. Conditional Gaussian polar coordinates determine the entire absolute-error distribution. The binomial and hypergeometric laws give the exact incidence of the singular row-sign sector; it is Cauchy for the unregularized estimator. The fixed-size ridge asymptotic follows from a one-dimensional Gaussian integral with an explicitly evaluated leading singularity. The simultaneous regularization transition follows by separating this sector from uniformly integrable nonsingular events and applying Hoeffding concentration. The proof handles the sampling-without-replacement boundary \(m=N/2\), \(m=1\), both extreme signs and all positive ridge strengths. The program `VERIFY.py` passed 2,292 finite checks of the key reductions, finite mixture laws, angular probabilities, and ridge coefficient. Those computations corroborate, rather than replace, the proof.

## Originality (PASS, bibliographic uncertainty remains)

The nearest and indispensable antecedent is Song and Zhang (2026), Section 3, equation (3), which already supplies the unregularized two-Gaussian ratio and a high-probability counterexample to Gaussian diagonal placement. That ratio is not represented here as a new discovery. The newly assessed mathematical content concerns adding a precisely normalized ridge term, computing the resulting singular-sector square-risk coefficient, proving the simultaneous critical regularization scale \(4^{-m}\), and classifying existence of all positive moments under without-replacement row selection. The antecedent's fixed-penalty-free high-probability statement does not assert or establish these regularized risk and sampling-design results. Earlier \(\ell_\infty\)-regression work by Price–Song–Woodruff (2017) and Song–Ye–Yin–Zhang (2023) concerns different sketches and high-probability bounds. Generic sketched-pseudoinverse results provide neither the rare-event decomposition nor this fixed-Hadamard, many-with-replacement-rows limit.

Searches comparing the exact estimator, its Gaussian ratio, moment thresholds, ridge regularization, possible equivalent generalized arcsine formulations, and broader sketched-regression theory did not identify a complete prior theorem. Absence from indexed literature is not a proof of priority. Residual risks include unindexed numerical-analysis notes and possible implicit calculations in discussions of singular sample covariances.

## Value (PASS)

The mean-square error of a randomized regression approximation is a natural design criterion distinct from its high-probability accuracy. In this concrete model, a rare event of probability \(2^{1-m}\) causes infinite unregularized mean-square risk no matter how large the sample count, and introducing a vanishing ridge term gives a sharp transition at \(4^{-m}\) with an explicit finite critical constant. The replacement-versus-without-replacement cutoff identifies precisely when the catastrophic event becomes combinatorially impossible. This supplies a reproducible stress test for implementation choices in structured randomized regression, not a routine renaming of a bound.

## Nearest sources and limits

- Song and Zhang, arXiv:2608.26552v1, especially Section 3 and its exact unregularized Gaussian ratio; the basis for the model but not the ridge-window theorem.
- Price, Song and Woodruff, arXiv:1705.10723, especially Sections 1 and 3; high-probability directionwise guarantees for signed SRHT.
- Song, Ye, Yin and Zhang, arXiv:2302.00248v1; coordinatewise fast regression and OCE arguments.
- *Asymptotics of the Sketched Pseudoinverse*, DOI:10.1137/22M1530264; generic implicit-ridge background rather than the present singular-row sampling law.

This finding applies only to the explicit one-parameter real regression instance, the stated Gaussian diagonal placement, the stated row-sampling schemes, and exact arithmetic. It is not a conclusion about the new balanced Gaussian-pooling scheme or about arbitrary datasets. Possible unindexed equivalent results remain a bibliographic risk.

Self-review: passed. Independent audit: not yet performed.
