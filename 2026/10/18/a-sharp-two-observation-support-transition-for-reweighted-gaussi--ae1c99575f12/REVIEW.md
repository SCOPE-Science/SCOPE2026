# Scientific review

## Correctness

**PASS.** The theorem's singleton part is equivalent to the precise sharp Kearns--Saul Bernoulli moment-generating-function bound with its uniqueness-of-nonzero-contact statement. The supporting primary source is Schlemm (2014, Theorem 1.1 and proof, arXiv:1405.4496v1). The Gaussian-mixture dual is derived directly. A two-Gaussian sensitivity function has at most two local maxima: its critical-point equation has at most three roots by an explicitly differentiated log-ratio. Strict concavity of the fitted logarithms and linear independence of the two kernel columns establish the optimizer's uniqueness, including at critical dual contact. The nonlocal onset follows by weak compactness and the limiting pair of nondegenerate sensitivity maxima; normalized independent Gamma weights give a Beta distribution and the claimed exact interval probability. The file `verify.py` ran successfully with 29,849 finite diagnostic checks; these are not substituted for an infinite proof.

## Originality

**PASS, qualified.** Full relevant primary texts were examined: Jiang (2026, arXiv:2610.01088v1, introduction/main results on randomly reweighted NPMLEs), Schlemm (2014, arXiv:1405.4496v1, Bernoulli exponential moment lemma), and Polyanskiy--Sellke (2025, unrestricted Gaussian location NPMLE and general sensitivity stationarity). They supply the motivating weighted optimization, the nonstandard sharp inequality, and the classical stationarity theory respectively, but do not state the combined exact two-observation phase diagram and Beta-weight support-count law. Semantic record and targeted phrase searches found no mathematical implication covering this exact conclusion; absence of search hits does not prove absolute novelty. Older or unindexed exact two-observation NPMLE calculations remain the principal priority risk.

## Mathematical value

**PASS.** This is a complete natural finite-sample instance of the recently studied reweighted Gaussian NPMLE, not an arbitrary numerical parameter slice. It determines exactly when reweighting destroys or retains a second support point; it separates the first global dual contact from the later local-curvature change; and it gives the explicit Beta probability of the support-size transition for the Gamma weights used in the motivating framework. The asymmetric onset additionally has a vanishing-mass atom at a nonzero limiting distance, unlike the continuous equal-weight case. No large-sample sparsity improvement is claimed.

## Closest literature and limits

Jiang's 2026 theorem concerns polylogarithmic sparsity in a large-sample random-reweighting regime. Schlemm's 2014 theorem already gives the sharp Bernoulli exponential-moment constant and its strict equality case. Polyanskiy and Sellke 2025 give general NPMLE sensitivity conditions and recall known unweighted one-dimensional uniqueness. This contribution is an exact finite-dimensional synthesis and boundary classification, not any of those original theorems. Independent priority and mathematical validation have not been performed. The finite diagnostic grids are not exhaustive certificates.

Self-review: passed. Independent audit: not yet performed.
