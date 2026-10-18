# Scientific review: covariance-matched active-dimer fourth cumulants

## Correctness — PASS

The state spaces, stationarity, independent Brownian terms, and positive parameters are explicit. The Gaussian driver and telegraph driver share the same two-time covariance but have different ordered four-time moment laws. Full subtraction of all three Gaussian-pair products yields strictly positive four-point cumulant kernels for each driver; their pointwise difference is strictly positive. Integration over all 24 chronological label orders, with the factor for separating the outer two gaps, proves the finite-time strict ordering. Exponential domination permits the exact long-time limits, and elementary simplex moments prove the short-time exponents. The complete mean-square displacement and matching source-defined entropy-production rate follow from the stated covariance and the cited microscopic decomposition.

An independently derived conditional-Gaussian variance calculation with a finite-time midpoint discretization was used to check the analytic fourth cumulants. The accompanying standalone checker passed 61 assertions, including 24-permutation symbolic integration, exact four-time moments, discrete covariance-matrix checks in both driver models, numerical continuous-time quadrature, and rate comparisons for three positive parameter sets. The all-parameter result does not depend on finite sampling.

## Originality — PASS (self-review)

The closest paper is Cocconi, Alston and Bertrand, arXiv:2304.07738v1 (2023-04-16). Its full 16-page public manuscript, including supplementary sections on both stiffness-noise models, was examined. It establishes the model, two-time MSD, and source-defined entropy-production rate, and the relevant equations agree under covariance matching. No evaluated fourth-displacement cumulant, all-positive-time ordering, short-time exponent contrast, or long-time fourth-cumulant ratio was found in that text. The result is therefore not claimed to discover the model or its second-order/EPR formulas.

Lemaitre et al., arXiv:2208.02780v1, were compared through their full public HTML text, sections 2–4 and the model discussion. Their long-time non-Gaussian mixture mechanisms use distributed speeds or diffusivities across particles rather than stationary covariance-matched Gaussian and telegraph interaction forcing. Accessible historical claims concerning correlated-telegraph dimers and other covariance-masked harmonic processes were also checked for statement-level overlap; they address second-moment stability or different fourth-order observables, not this exact all-lag comparison.

General Wick identities could in principle be specialized by other authors to obtain parts of these expressions. A relevant undiscovered equivalent formula, or unpublished treatments of this same model, remains a priority risk. Database-search nonmatches are not proof of novelty. This status is a same-model appraisal, not a claim of independent certification.

## Scientific value — PASS

The study's observable choice is motivated directly by an identifiable gap: complete MSD and average entropy production cannot distinguish two experimentally interpretable stiffness-fluctuation laws once their two-time covariances match. Their full fourth-displacement cumulants do distinguish them at *every* lag. The exact long-time ratio quantifies how strongly the mechanisms differ at slow and fast asymmetry switching, while the short-time exponents \(t^4\) and \(t^5\) provide a second structural distinction. The result supplies a tractable benchmark for non-Gaussian active transport that is neither a parameter renaming nor an arbitrary finite sample of settings.

## Closest literature and limits

Cocconi–Alston–Bertrand (2023), arXiv:2304.07738v1, provides the precise model and all earlier MSD/entropy formulas. Lemaitre–Sokolov–Metzler–Chechkin (2022), arXiv:2208.02780v1, supplies distinct non-Gaussian active-particle context. Restrictions are harmonic coupling, perfect anticorrelation or synchronized opposite-sign fluctuations, stationary and independent internal drivers, independent Brownian center-of-mass noise, no steric interactions, and fourth displacement cumulants rather than complete trajectories. No finite-sample estimation theorem or alternate entropy accounting is asserted.

Self-review: passed. Independent audit: not yet performed.
