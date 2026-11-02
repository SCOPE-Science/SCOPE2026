# Scientific review: directional lag correlations under partial resetting

## Correctness — PASS

The proof fixes the complete stochastic model, noise normalization, lag orientation and all positivity quantifiers. A quadratic Lyapunov inequality and synchronous coupling establish stationary existence and uniqueness. The reset-sensitive second-moment generator gives exact stationary covariance and conditional linear evolution yields the forward lag matrix. The strictly negative asymmetry, unique lag extremum and two inverse mappings are explicit algebraic consequences with no limiting assumptions. The bundled standard-library code independently verified 575 finite exact-rational and matrix-exponential consistency checks. Finite checks do not substitute for proof.

## Originality — PASS (qualified best knowledge)

The base model and stationary equal-time moments belong to Santra and Das (arXiv:2603.17027, 2026). They are not presented as new. The evaluated claim is the exact signed directional **two-time** covariance, its unique delay peak, and identification of both physical rate parameters from either cross-lag derivatives or probe-only covariance data. An earlier potentially overlapping coupled-bath selective-reset model is Goswami (arXiv:2412.19564), for which only the abstract/model description was accessible, leaving a priority risk. Another close source, Biswas et al. (arXiv:2412.09260), derives scalar two-time probe correlations in a separately renewed viscoelastic setting. Comparisons with relevant published material did not identify an equivalent theorem, but complete continuous text of the identical-model source and the potentially relevant 2025 source could not be inspected. General linear-generator covariance techniques might imply portions of this narrow result and independent priority review remains outstanding.

## Value — PASS

The direction and optimal lag of probe–bath correlation quantify broken temporal ordering under selective resetting. Both exact inverse reconstructions address the physically motivated question of inferring the reset rate and hidden viscoelastic relaxation time, including from probe-only data. The motivation is structural and measurement-oriented, rather than an arbitrary numerical special case. The derivation does not assert optimal estimation under sampling noise, full entropy production, or broader nonlinear bath models.

## Scope and remaining risks

The result requires instantaneous homogeneous Poisson probe resetting, equilibrium noise with known scale, one linearly coupled bath coordinate, positive finite \(r\) and \(\gamma\), and stationary observation. Access to the complete uninterrupted source article and an independent priority assessment remain outstanding. The cited classical matrix-semigroup method is not asserted to be new.

Self-review: passed. Independent audit: not yet performed.
