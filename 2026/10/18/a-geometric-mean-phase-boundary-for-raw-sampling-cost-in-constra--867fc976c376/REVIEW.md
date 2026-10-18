# Scientific review

## Correctness — PASS

The projected update on a diagonal matrix is exactly coordinate replacement; zero-residual draws are rejected and must be counted in the raw-proposal budget. The two-unpinned-row stopping time is precisely a two-coupon collection time, with disjoint monochromatic histories after every integer \(t\ge1\), giving the stated tail and expectation. The mean is strictly monotone in singular-value imbalance; comparing \(s_2/s_3\) with \(s_1/s_2\) gives the exact boundary \(s_2^2=s_1s_3\), including both strict and equality cases. In arbitrary dimension, a geometric waiting-time lower bound for sampling the smallest row and a conditional discovery-probability upper bound for all remaining rows establish a divergence in raw-work ratio. The Frobenius costs and their near-optimal ratio are direct projector calculations. The standalone exact-rational checker passed 2475 independent finite computations; no infinite assertion is based on those finite tests.

## Originality — PASS, with remaining bibliographic uncertainty

Sun et al. (arXiv:2605.29304v1), Algorithm 1, explicitly reject null draws, and Section 3.2 adopts projected Frobenius error for selection; they analyze contraction by accepted iterations, not the exact raw-draw stopping law or its tradeoff against their Frobenius selector. Lok and Rebrova (arXiv:2309.04889, original SCRK Algorithm 1 and Section 3.3.2) already established the subspace-constrained method and rank-based row selection; these are not new. Nutini et al. (UAI 2016) already exploit orthogonality to suppress unproductive Kaczmarz selections. The weighted coupon-collector tail calculation is classical. The assessed distinction is the complete three-row pin-selection phase boundary for the newer source's **explicit null-rejection** with its particular Frobenius surrogate, and the arbitrarily small relative Frobenius sacrifice with divergent raw-probe work in a controlled higher-dimensional family. Searches of the current accessible claims, mathematical research records, and relevant literature found no covering combined theorem. An equivalent earlier specialized analysis under alternative terminology cannot be excluded.

## Mathematical value — PASS

The work identifies a measurable tradeoff in the motivating method's actual sampling mechanism: its accepted-step theorem hides arbitrarily expensive repeated draws of already-solved rows. It supplies a sharp dimension-three design criterion, a concrete family with unbounded sampling overhead, and a quantitative robustness counterexample showing that even a near-optimal Frobenius constraint does not control that overhead. These address the cited algorithm's explicit surrogate and therefore are not arbitrary numerical examples or a recomputation of an existing table.

## Closest literature, risks, and limitations

The original source proves matrix-based accepted-iteration convergence and recommends the Frobenius surrogate. The earlier SCRK paper proves accepted-iteration rates and discusses approximate low-rank selection. Existing orthogonality-aware sampling avoids wasted row actions in other mechanisms. A broad coupon-collector law provides a proof ingredient, not the studied surrogate-selection classification. Remaining risk: a specialized earlier pin-selection calculation may imply this exact boundary; the 2016 orthogonality-graph paper was only inspected to the available abstract in the present review. The theorem assumes fixed independent probes with explicit rejected-draw accounting and makes no general-time complexity claim.

Self-review: passed. Independent audit: not yet performed.
