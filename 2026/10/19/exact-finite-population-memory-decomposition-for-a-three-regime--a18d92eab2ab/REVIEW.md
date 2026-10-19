# Scientific review

## Correctness — PASS

The statement covers the finite continuous-time count/environment generator with parameters and boundary cases explicitly specified in RESULT.md. The derivation uses the environmental generator's exact two eigendirections, a cross-moment identity, the exact voter-count quadratic variation, an algebraic stationary variance equation, and a closed two-time regression. Positivity of the size correction follows from the strictly positive microscopic variance-rate function under the stationary infinite-population pullback. The packaged standard-library checker independently constructs 30 finite generators in rational arithmetic and verifies 210 covariance derivatives; all pass. This finite evidence supports, but does not replace, the proof.

## Originality — PASS, subject to priority risk

Caligiuri–Galla (arXiv:2305.19096, full 20-page manuscript inspected, including Sec. V B and Appendices A/B) define the same finite voter model and three-regime switching but treat full stationary densities through PDMP numerics and intrinsic-noise approximations. Their statements do not cover the exact all-finite-size two-time covariance nor the exact positive inverse-linear variance correction. Hufton et al. (arXiv:1512.00785, introductory model and methodology inspected) examine environment-dependent linear birth–death systems using linear-noise approximations, not these exact bounded voter rates. Earlier network voter covariance studies and trichotomous forcing work share ingredients but do not imply this specific theorem as stated in inspected material. Exact spectral filtering itself is standard; priority is asserted only for the finite-voter exact correction. A general exact moment-closure result elsewhere might imply this specialization, so independent priority checking remains advisable.

## Value — PASS

The 2023 motivating paper explicitly treats multiregime stationary densities numerically. The exact correction \(\kappa/(Nc+q)\) identifies how population size modifies variance and every time-lag correlation even when the full stationary distribution is unavailable, and separates demographic relaxation from two environmental timescales without a large-\(N\) approximation. This gives analytically useful finite-population fluctuation benchmarks for stochastic opinion models, not an arbitrary parameter slice or numerical recomputation.

## Limitations

The precise all-to-all, autonomous environment assumptions are essential. Other switching generators and heterogeneous networks are not covered. The result is a self-review, not a claim of independent scientific verification or established publication priority.

Self-review: passed. Independent audit: not yet performed.
