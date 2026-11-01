# Mathematical assessment

## Correctness — PASS

The four affine images align with the four cell endpoints precisely on the outer-slope relation \(r(k-1)=1\). Conditional uniformity on successive complete target cells proves a genuine stationary four-state Markov itinerary, not a first-step approximation. Cell masses divided by lengths give the asserted normalized density. The four-by-four resolvent, eigenvalue factorization, and bounded Poisson solution have exact symbolic proofs. Because two consecutive *regular* visits cannot both be outer, each two-step derivative exceeds one; the generating partition argument transfers finite-state mixing to the interval map. A bounded Markov-chain martingale yields the CLT. The provided standalone program was executed successfully on the actual packaged source before review: symbolic identities and 48 exact rational cases, including 720 covariance checks. Finite checks corroborate, and do not replace, the universal proof.

## Originality — PASS within inspected evidence

The original García-Grimaldo–Campos-Cantón 2021 paper introduces the four-branch family and fixed-point-free chaotic dynamics, and the 2023 FPGA paper reproduces its formula and studies numerical/hardware properties. Neither the inspected 2023 full text nor the accessible original publisher preview states the displayed stationary Markov law, full rational sign-covariance generating function, or exact vanishing diffusion coefficient. The 2023 Wang–Ding–Rhee inverse transfer-operator construction addresses generic piecewise constant densities, not this exact sign-memory result. An existing prime-three census in the *same* four-branch family covers periodic point counts on \(r(k-1)=1\), but does not imply a stationary density or its Gaussian fluctuations; a distinct reciprocal-slope result concerns eventually periodic measures instead. The full original 2021 paper remains inaccessible and prevents an exhaustive whole-paper priority determination. That risk is disclosed; no claim of independently certified novelty is made.

## Mathematical value — PASS

The parameter slice is forced by a natural geometric Markov-alignment condition, not chosen for an isolated numerical output. The complete sign-correlation generating function and Gaussian variance are exact natural statistical invariants of a family designed for fixed-point-free chaos and pseudorandom signals. The anti-correlation cancellation is structurally informative: \(\sigma_k^2=(k-1)/(k(2k-1))	o0\) even as the subdominant symbolic spectral radius tends to one. Generic Markov theory alone does not supply these source-specific coefficients or this contrasting scaling.

## Closest literature and limitations

The original 2021 publisher preview is incomplete; the 2023 full FPGA source was materially inspected. The result is stationary and model-specific. Boundary trajectories and other invariant measures need not share the stated statistics. An equivalent unindexed computation is a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
