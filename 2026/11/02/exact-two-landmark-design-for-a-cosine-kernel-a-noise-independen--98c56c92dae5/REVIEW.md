# Scientific review

**Claim:** Exact global two-landmark integrated-posterior-variance design for the positive-ridge cosine kernel on the uniform circle, including the all-noise \(120^\circ\) identity and the small-noise quarter-power collision law.

## Correctness — PASS

The kernel is a three-dimensional Gram kernel. Symmetric and antisymmetric combinations of the two landmark evaluations diagonalize both the sample Gram matrix and its integrated second moment, giving an explicit scalar objective with positive denominators at positive ridge. The derivative has a single sign-changing zero or is increasing everywhere, after reduction to a strictly increasing difference of reciprocal affine functions. The positive root of a concave quadratic in the constant-mode kernel amplitude is the exact global boundary. The all-noise \(120^\circ\) identity is an exact substitution. The quarter-power law follows from a justified Taylor expansion of the explicit optimizer and the endpoint expansion of the inverse cosine. At zero ridge, the calculation uses the Moore–Penrose inverse at exact collision instead of incorrectly continuing an invertible formula through rank loss. An independently evaluated two-by-two inverse, a trigonometric integral, rational spectral identities and parameter-grid tests all passed (7,770 assertions). Finite tests complement rather than replace the analytic proof.

## Originality — PASS, qualified

The 2015 Gorodetsky–Marzouk paper develops the same general integrated-variance objective and contains numerical periodic-kernel examples, but the inspected Sections 2–4 use continuous numerical design and an infinite-rank periodic covariance, not an exact two-site rank-three phase diagram. The 2023 Hayakawa–Oberhauser–Lyons paper defines Nyström integrated residuals and establishes general randomized or refined-subspace bounds; its inspected results do not imply the exact positive-ridge optimizer. Classical trigonometric-regression Q/A/G-optimality literature addresses unregularized coefficient or response design and is not by itself a formula for two noisy GP landmarks with a particular prior covariance. The Xu–Shang 2014 full text was inaccessible, so publication-priority risk from its specialized statements remains. Other known two-sensor Fourier results concern graph frame-condition numbers or phase recovery, rather than this integrated posterior loss. No exact published formula for the boundary, noise-invariant angle or collision exponent was identified; absence in a search is not itself proof of priority.

## Value — PASS

For the simplest nontrivial periodic kernel with a constant mode and one Fourier harmonic, choosing two informative observation locations is a natural minimal fixed-budget design question. The answer is not merely a stationary point: it classifies all parameter and noise regimes, demonstrates a counterintuitive noise-independent optimal angle at the balanced constant-mode weight, and gives a nonstandard fourth-root collapse with a precise discontinuity at exactly zero noise. This distinguishes redundant noiseless measurements from near-colliding independent noisy measurements, a concrete issue for small-rank kernel design and sensor placement. The result makes no claim about higher-rank kernels or unrestricted experimental budgets.

## Literature and limits

The closest comparisons are Gorodetsky and Marzouk (2015/2016), arXiv:1503.00021, sections on posterior covariance, integrated variance and periodic examples; Hayakawa, Oberhauser and Lyons (2023), arXiv:2301.09517, sections on Nyström residual and general landmark selection; and Xu and Shang (2014), DOI:10.1007/s00184-013-0463-7, available abstract only. The third source poses an unresolved specialized-publication risk but not an identified implication of the stated ridge-specific result.

Self-review: passed. Independent audit: not yet performed.
