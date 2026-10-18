# Self-review

## Correctness — PASS

The exact radial mean-exit integral uses the generator with diffusion intensity \(D\). From this kernel, a monotone integral proves strict mean-time decay in all dimensions \(d\ge2\). A nontrivial one-crossing argument for the Dawson kernel proves a unique finite one-dimensional maximum. The planar formula follows from the exact exponential kernel and has the displayed sharp endpoint asymptotic. The independent `verify.py` numerical checks are supplementary, not a proof of universal statements.

## Originality — PASS, qualified

The closest **same-object** paper is Chemnitz, Engel and Koltai (2026), Example 2.1, which already obtains the sign of the first small-noise response in every dimension; its Remark 2.4 notes that such a derivative cannot settle the full positive-noise range. Kersting and collaborators (2022), Theorem 4, already provide the general integral formula. These results and their implications are excluded from the originality claim. No covering published claim for the unique global noise optimum together with all-noise higher-dimensional monotonicity and the sharp planar exponentially small deficit was identified during the inspected comparisons. Older works developing Ornstein–Uhlenbeck exit formulas (Graczyk–Jakubowski 2008; Grebenkov 2014) were not fully read and may provide broader implications. Independent priority verification is still outstanding.

## Mathematical value — PASS

The complete optimization diagram resolves a natural question specifically left open by a first-order stochastic-inertia computation: whether the mean escape delay persists or turns around at finite noise, and whether zero first derivative in dimension two hides any effect. The answer provides a unique optimum in dimension one, a uniform strict inequality for all positive noise in higher dimensions, and an exponentially small critical planar law. It is a self-contained structural result for the same natural observable, not a generic formula restatement.

## Scope and limitations

Fixed positive initial radius, constant isotropic diffusion, outward linear drift and a spherical absorbing boundary. The existing formula and first-order response belong to cited prior work. Numeric verification is finite and independent external assessment was not performed.

Self-review: passed. Independent audit: not yet performed.
