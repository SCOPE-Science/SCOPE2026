# Independent audit — 2026-10-01

## Final claim

For every positive stage partition, the MSARP expected-error product factor \(\prod_i(k_i+1)\) is worst-case sharp as a supremum, including for actual orthogonal CSS error, and singleton staging can approach a \(2^d/(d+1)\) expected-error ratio relative to one-shot ARP on the same final subspace.

## Correctness — PASS

The codimension-one projection-DPP identity was re-derived from \(VV^T=I-zz^T\). The explicit two-stage expectation follows exactly from conditional omission probabilities. The recursive null-vector extension multiplies the preceding supremum in the small-tail limit. Independently replaying the orthogonal CSS construction verified the formula \(1/(z_j^2+\delta^2(1-z_j^2))\) for every omitted coordinate in a fresh numerical example, so the transfer from the oblique surrogate is genuine.

## Originality — PASS

Best-of-knowledge originality passes. The accessible source description gives multistage guarantees but does not state unconditional all-stage product sharpness, the orthogonal-CSS transfer, or the exponential staged-versus-one-shot separation; no earlier Resultary record with those conclusions was located.

### Equivalent formulations

Searches: Resultary: multistage adaptive randomized pivoting conditional DPP product sharpness nested worst case; arXiv:2609.20556

Evidence: The assigned record is the first exact-topic 2026-09-18 hit; two essentially matching Resultary records are dated 2026-09-19. The source abstract describes MSARP and expected-error guarantees, not a matching lower construction.

Reasoning: Conditional one-stage equality and an unconditional product upper bound do not imply that a single nested distribution asymptotically realizes the whole product.

### Broader coverage

Searches: classical volume-sampling sharpness; one-shot ARP bounds; Grigori-Xue multistage upper bounds

Evidence: Classical results cover one-shot factors; the new construction concerns nested irrevocable conditional sampling and actual CSS error.

Reasoning: One-shot lower bounds do not dominate the multistage product claim.

### Exact database or table

Searches: Resultary exact product-factor sharpness; staged-versus-one-shot exponential separation

Evidence: No pre-2026-09-18 exact table/theorem was found; later 2026-09-19 records repeat the phenomenon.

Reasoning: The later duplicates support reproducibility but are not prior coverage.

### Claim versus prior implication

Searches: arXiv:2609.20556 abstract; conditional DPP one-stage equality versus general product sharpness

Evidence: The accessible source material establishes the problem and upper guarantees but does not state that the bound is attained for every stage partition.

Reasoning: An additional nested codimension-one construction is required to obtain the final lower bound.

### Source inspections

- **Incremental Column Subset Selection via Conditional Determinantal Point Processes** (https://arxiv.org/abs/2609.20556): Confirms the multistage algorithm and guarantees but leaves residual risk about details not visible in the abstract. Material read: Abstract and bibliographic metadata; full text could not be retrieved in this run. Method: Primary-source abstract inspection plus authorized-access attempt. Evidence: No accessible abstract statement gives unconditional product sharpness.

Checked sources: Grigori and Xue, Incremental Column Subset Selection via Conditional Determinantal Point Processes, arXiv:2609.20556; Cortinovis and Kressner, Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation; Assigned exact verifier and fresh independent codimension-one projection replay; Resultary search for multistage ARP product sharpness

Residual risks: The source preprint is extremely recent and its full text was not retrievable in this run; its public abstract does not advertise product-factor sharpness. Later 2026-09-19 records independently state essentially the same sharpness, so simultaneous follow-up risk remains.

## Scientific value — PASS

Showing that the potentially exponential multistage factor is a real worst-case phenomenon, and quantifying its rare-event mechanism and gap from one-shot selection on the same final subspace, is a natural and useful boundary result for an incremental randomized algorithm.

## Limitations

- Worst-case supremum through increasingly imbalanced leverage scores; no average-case or high-probability claim. Orthogonal-CSS sharpness uses a small trailing singular-value limit.

## Conclusion

The final claim passes correctness, originality and scientific-value review.
