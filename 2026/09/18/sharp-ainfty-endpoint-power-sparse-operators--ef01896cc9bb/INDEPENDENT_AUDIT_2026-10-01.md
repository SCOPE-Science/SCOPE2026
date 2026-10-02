# Independent mathematical audit — 2026-10-01

## Final claim

Sharpness of the A_infinity endpoint power for sublinear sparse sums

## Correctness — PASS

PASS. The finite dyadic construction was reconstructed directly. For the nested dyadic chain, the spike weight and its dyadic maximal function make the mixed A1 characteristic exactly one. Shell-by-shell integration gives the stated Fujii-Wilson ratio, with A-infinity characteristic of linear order in N. Testing the constant function one on the deepest interval yields output size of order N to the power one-over-r, while the input L1 norm is of linear order N. The resulting weak norm lower bound has order N to the power one-over-r-minus-one, proving that no smaller uniform A-infinity power can work.

## Originality — PASS

PASS to the best of current knowledge. The exact construction and implication were compared, not just titles. The motivating Goncalves-Lorist preprint is the directly relevant primary source; indexed material states the new weak endpoint estimate and neighboring sharpness results, but full text retrieval was unavailable in this run. Semantic searches of published mathematical records returned the audited record itself as the exact match and no earlier record with the same lower-bound family or the normalization that keeps the mixed A1 characteristic equal to one. The primary-source access limitation remains an explicit residual risk.

### equivalent_formulations

Searches: sharp A_infinity endpoint power sublinear sparse operator weak L1 two weight mixed A1 r<1 Goncalves Lorist; arXiv:2609.20531 endpoint sharpness

Evidence: The published-record semantic search found the audited record as the only exact match; the motivating preprint is the directly relevant source.

Reasoning: The claim is equivalent to a lower bound for the optimal Fujii-Wilson power after normalizing the mixed A1 characteristic to one; no earlier exact formulation was located.

### broader_coverage

Searches: Goncalves Lorist sharp mixed Ap Ainfinity sparse operators 2609.20531; Nieraeth Stockdale endpoint weak-type bounds sparse

Evidence: Available indexed material supplies the upper estimate and earlier endpoint context.

Reasoning: No inspected broader theorem mechanically yields the explicit normalized lower-bound family.

### exact_database_or_table

Searches: published mathematical record semantic search exact lower-bound family

Evidence: No natural numerical database or table governs this parameterized inequality, and no earlier exact record was found.

Reasoning: The appropriate exact check is theorem/record search rather than a numerical table.

### claim_vs_prior_implication

Searches: arXiv:2609.20531v1; arXiv:2409.08921

Evidence: The accessible prior statements give upper-bound/open-problem context, not an implication forcing this lower bound.

Reasoning: The explicit lower-bound construction supplies additional information not mechanically implied by the inspected statements.

## Scientific value — PASS

PASS. This is a sharpness theorem for a newly established endpoint estimate, not an arbitrary parameter evaluation. Keeping the mixed A1 factor identically equal to one isolates the A-infinity exponent and shows that the power loss is intrinsic rather than an artifact of the upper-bound proof. The finite family is also a reusable benchmark.

## Source inspections

- **Sharp mixed A_p-A_infinity estimates for sparse operators on filtered and nonhomogeneous measure spaces** — https://arxiv.org/abs/2609.20531v1. Material read: Abstract and indexed statement material; full text retrieval was unavailable during this audit. Assessment: PLAUSIBLE_PRIMARY_SOURCE_WITH_ACCESS_LIMITATION. Evidence: Available material identifies the new endpoint estimate and neighboring sharpness discussion but does not itself expose the audited normalized lower-bound family.
- **Endpoint weak-type bounds beyond Calderon-Zygmund theory** — https://arxiv.org/abs/2409.08921. Material read: Bibliographic and indexed result context. Assessment: BACKGROUND_NOT_EXACT_COVERAGE. Evidence: It supplies earlier endpoint context rather than this sharp A-infinity-power example.

## Limitations and residual risks

The result concerns the mixed two-weight weak-L1 endpoint of the positive sparse operator for zero less than r less than one. It does not assert a matching lower bound for every operator admitting sparse domination, determine the optimal r-dependent constant, or address the distinct r equals one logarithmic endpoint. The motivating preprint is extremely recent and was not retrievable in full text during this audit.

- The motivating September 2026 preprint could not be inspected in full text in this run; an unindexed contemporaneous observation remains possible.
- The theorem proves sharpness only for the stated positive sparse operator and mixed endpoint.

## Disposition

**passed**
