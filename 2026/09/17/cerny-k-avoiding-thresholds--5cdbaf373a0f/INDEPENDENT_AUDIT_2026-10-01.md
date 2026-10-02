# Independent scientific audit — SCOPE-20260917-5cdbaf373a0f

Audited at: 2026-10-01T05:14:16.390825Z

Disposition: **passed**

## Correctness — PASS

The inverse actions are correct. In a shortest inverse path, a preimage under b that fixes the current target can be deleted, and a b-preimage that enlarges it can also be deleted because subsequent preimages preserve inclusion; therefore every retained b-step deletes exactly state n-1 and exactly k such deletions are required. Any nonempty proper cyclic target has an occupied-to-empty boundary that can be rotated to the deleting edge in at most n-1 rotations, proving the universal kn upper bound. For the consecutive block B_k, the unique boundary first reaches the deleting edge only after n-1 rotations, and deletion returns exactly B_{k-1}, giving the matching recurrence. Any other k-set has another boundary allowing the first deletion at least one symbol sooner, proving uniqueness. Independent breadth-first search through n=9 reproduced every threshold and unique maximizer; the repository verifier extends the same finite check through n=11, but the infinite theorem rests on the analytic boundary proof.

## Originality — PASS

Ferens-Szykuła-Vorel introduced the k-avoiding threshold and explicitly recorded the n=4 values 4,8,12. Ferens-Szykuła's 2026 complete-reachability paper states that Černý automata meet Don's reaching bound by subset cardinality, but reaching a particular complement is stronger than merely ending inside that complement, so it does not imply the audited avoiding lower bound for k between one and n-2. Searches did not locate the all-n, all-k avoiding formula or the unique hardest target before this record.

### Equivalent formulations

No equivalent all-n/all-k formulation was located.

### Broader coverage

The prior reaching result is related but does not dominate the avoiding problem; the audited inverse-boundary argument rules out precisely that shortcut for B_k.

### Exact database or table

No independent table/general theorem was found beyond small n=4 data.

### Claim versus prior implication

The new lower bound requires the normal-form and boundary argument; it is not a corollary of known reaching thresholds.

## Value — PASS

An exact closed formula for every subset size in the canonical Černý family, together with the unique worst target, is a natural benchmark for avoiding-threshold theory and directly clarifies the distinction between subset reaching and subset avoidance. It is neither an arbitrary tiny case nor a mere renaming.

## Sources inspected

- Lower Bounds on Avoiding Thresholds — https://doi.org/10.4230/LIPIcs.MFCS.2021.46. PARTIAL_COVERAGE: Contains the full n=4 instance, not the general kn formula or unique maximizer.
- Recognizing Completely Reachable Automata in Quadratic Time — https://doi.org/10.1145/3798283. RELATED_NOT_COVERING: States that Černý automata meet Don's reaching upper bound by subset size but does not convert equality-reaching into exact avoiding thresholds.

## Checked sources

- https://doi.org/10.4230/LIPIcs.MFCS.2021.46
- https://doi.org/10.1145/3798283
- https://doi.org/10.37236/5616
- Resultary exact formula search

## Residual risks

- Older circular/one-contracting automata literature could encode an equivalent total-extension statement without k-avoiding terminology.
- The n=4 instance and k=1 case are explicitly prior and are not counted as the novel part.

## Limitations

- The n=4 thresholds and isolated k=1 behavior are prior results; novelty is the general all-n/all-k theorem and uniqueness refinement.
- The finite breadth-first searches are checks only; the theorem is proved by the inverse-action argument.
