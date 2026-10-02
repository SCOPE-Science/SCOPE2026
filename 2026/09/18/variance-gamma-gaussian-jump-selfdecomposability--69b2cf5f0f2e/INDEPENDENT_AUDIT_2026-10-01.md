# Independent mathematical audit — 2026-10-01

## Final claim

Exact self-decomposability threshold for Gaussian compound-Poisson perturbations of symmetric variance-gamma laws

## Correctness — PASS

PASS. The self-decomposability test was reconstructed from the canonical Levy density. Adding the Gaussian compound-Poisson component changes the positive-side canonical function to the sum of an exponential term and a Gaussian term. Its derivative is automatically negative beyond one jump standard deviation and gives a one-variable threshold inside that interval. After scaling, the threshold function has a unique minimizer because its logarithmic derivative is strictly increasing. The stated critical activity follows. Envelope differentiation gives the unique optimal scale ratio and the maximum activity, and the endpoint expansions are consistent with the minimizer equation. Independently, the background-driving characteristic-function criterion of Wang and Yin produces the same nonnegativity inequality and the stated jump density.

## Originality — PASS

PASS to the best of current knowledge. Wang and Yin's full 2026 paper supplies a general symmetric self-decomposability/background-driving criterion, but it does not treat variance-gamma laws with Gaussian compound-Poisson shocks. The standard canonical-density criterion likewise reduces the question to monotonicity but does not state the optimized threshold, Goldilocks scale window, maximal activity, or explicit critical tangency for this family. Targeted literature and published-record searches found no earlier exact phase diagram.

### equivalent_formulations

Searches: variance gamma Gaussian compound Poisson self-decomposability threshold; background driving law variance gamma Gaussian jumps

Evidence: The exact published-record search returned the audited record; the closest current primary criterion is Wang-Yin's general symmetric characterization.

Reasoning: The derivative-monotonicity and background-driving formulations agree, but neither inspected source gives the audited closed phase diagram.

### broader_coverage

Searches: class L canonical Levy density criterion; Wang-Yin self-decomposability criterion; weak variance generalized gamma convolution self-decomposability

Evidence: General theory supplies the test and background-driving representation, not the optimized Gaussian-jump parameter boundary.

Reasoning: Obtaining the unique minimizer, optimal scale and global two-boundary phase window requires a family-specific analysis beyond the general criterion.

### exact_database_or_table

Searches: published mathematical record semantic search for Gaussian-jump variance-gamma self-decomposability threshold

Evidence: No earlier exact threshold table or record was located.

Reasoning: The relevant object is a continuous parameter phase diagram rather than a standard database row.

### claim_vs_prior_implication

Searches: Wang-Yin Theorem 1.3; variance-gamma self-decomposability literature; compound-Poisson variance-gamma model literature

Evidence: The prior results identify general criteria and related models but do not mechanically state the family-specific optimum or critical activity.

Reasoning: The audited theorem adds a nontrivial global optimization and exact parameter classification.

## Scientific value — PASS

PASS. The result gives a complete exact boundary inside a natural infinitely divisible perturbation family, identifies a unique optimal jump scale, and exposes the nonlocal stability of class L under vanishing finite-activity shocks. These are motivated structural facts about a standard distribution family rather than an arbitrary numerical slice.

## Source inspections

- **Min Wang and Sheng Yin, Self-decomposability of alpha-Cauchy distributions** — https://arxiv.org/abs/2609.18536. Material read: Full nine-page preprint, including Theorem 1.3 and its proof via the background-driving Levy process. Assessment: GENERAL_CRITERION_NOT_EXACT_COVERAGE. Evidence: The paper proves a general characteristic-function criterion and applies it to alpha-Cauchy laws; it does not analyze the audited variance-gamma plus Gaussian compound-Poisson family.
- **Buchmann, Lu and Madan, Self-decomposability of weak variance generalised gamma convolutions** — https://doi.org/10.1016/j.spa.2019.02.012. Material read: Published theorem and bibliographic context. Assessment: RELATED_FAMILY_NOT_EXACT_COVERAGE. Evidence: The work concerns weak variance generalized gamma convolutions rather than the finite-activity Gaussian perturbation threshold audited here.

## Limitations and residual risks

The explicit phase diagram is one-dimensional and symmetric, for centered Gaussian compound-Poisson perturbations of centered symmetric variance-gamma laws. The general derivative criterion is classical and is not claimed as a separate contribution. Older class-L and convolution-factor literature under different terminology remains a residual originality risk.

- Older class-L or convolution-factor literature under different terminology may contain a related special case.
- The theorem is restricted to the centered symmetric one-dimensional family.

## Disposition

**passed**
