# Independent audit — SCOPE-20260917-effa1409f1ac

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For every finite variable-length non-overlapping code and every stationary source, the length-weighted sum of codeword cylinder probabilities is at most one; for a uniform q-ary source this yields a weighted Kraft inequality and the stated fixed-alphabet average-length lower bounds, including the logarithmic-in-logarithm correction.

## Correctness

**PASS** — The proof was reconstructed directly. Two distinct codeword occurrences covering the origin either overlap without containment, forcing a forbidden proper suffix-prefix match, or one contains the other, forcing a forbidden codeword subword. Hence the offset cylinder events are pairwise disjoint, and stationarity makes each offset probability equal to the word cylinder probability. The AM-GM step, the discrete convexity identity for the sequence k q^{-k}, and the continuous convexity step for q at least 3 were checked algebraically. The conclusion is finite and exact and does not require independence or ergodicity.

## Originality

**PASS** — Best-of-knowledge originality survives for the stationary arbitrary-source formulation and its average-length consequences. The closest modern papers study the same code notion and the average-length problem but do not state this stationary occupancy inequality; the earlier generating-function framework is closely related and may recover the uniform specialization, which is therefore not treated as independent novelty by itself.

### Equivalent formulations

The uniform inequality has a close generating-function ancestor, so novelty is limited to the stationary/source-sensitive formulation and the derived fixed-alphabet average-length consequences. Evidence: The published-results search returned this record as the exact semantic match. Wang--Wang 2024 formulates the same variable-length non-overlap condition and minimum-average-length problem, but its displayed lower bound is the prefix-code entropy bound and its asymptotic theorem concerns a different large-alphabet regime. The 2022 generating-function paper supplies an avoidance framework closely related to the uniform specialization, but the searched material did not state the stationary arbitrary-source inequality.

### Broader coverage

Known maximum-cardinality results and large-alphabet average-length results address different quantifiers and do not dominate the surviving claim. Evidence: The stronger maximum-cardinality bounds with only a maximum length constraint do not imply a length-weighted stationary-source inequality or a lower bound on mean length.

### Exact database or table

This check is inapplicable to a general theorem; the search was instead used to detect equivalent published formulations. Evidence: No exact database/table is relevant because the claim is a general inequality rather than a finite census.

### Claim versus prior implication

The final originality judgment is based on the stationary/source-sensitive statement and resulting mean-length consequences, not on claiming that every displayed specialization is new. Evidence: The earlier generating-function machinery plausibly implies the uniform iid inequality after an additional argument, so that specialization alone is not used as the novelty basis. The stationary law argument and arbitrary-source cylinder-probability statement follow from disjointness of covering events and are not consequences of an iid-only generating-function identity.

## Value

**PASS** — The result addresses the explicitly studied minimum-average-length problem for variable-length non-overlapping codes. The stationary formulation is source-sensitive, and for fixed alphabet size the additional logarithmic-in-logarithm lower-order term is a mathematically motivated strengthening of the ordinary prefix-code entropy scale.

## Sources inspected

- On the maximum size of variable-length non-overlapping codes — https://arxiv.org/abs/2402.18896. NOT_COVERING for the stationary-source theorem; CLOSELY_RELATED for the average-length setting: The paper gives the ordinary prefix-code entropy lower bound and a different large-alphabet asymptotic regime.
- Q-ary non-overlapping codes: a generating function approach — https://arxiv.org/abs/2108.06934. CLOSELY_RELATED; may recover the uniform specialization but did not supply the stationary arbitrary-source formulation in inspected material: Its method counts avoidance under iid word models rather than stating the stationary occupancy inequality.
- Variable-length Non-overlapping Codes — https://arxiv.org/abs/1605.03785. residual originality risk only: No stationary weighted Kraft statement was located in the inspected material.

## Residual risks and limitations

- Older variable-length comma-free or self-synchronizing literature may contain an equivalent measure-theoretic formulation under different terminology.
- The uniform iid inequality is closely connected to prior generating-function machinery and should not be advertised as wholly independent of it.
- Originality is best-of-knowledge rather than exhaustive across older comma-free terminology.
- No computational artifact is needed; the theorem is proved by a finite disjoint-event argument.

## Disposition

**PASSED**
