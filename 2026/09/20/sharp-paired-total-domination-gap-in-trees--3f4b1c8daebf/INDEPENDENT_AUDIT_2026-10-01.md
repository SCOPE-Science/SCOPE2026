# Independent mathematical audit — Sharp paired-total domination gap in trees

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — The established support-vertex inequality gives the basic gap bound. The odd equality case follows from forced support vertices, parity of paired domination, and the fact that adjacent supports would create a smaller paired set. For even order, the saturated support case is exactly a corona; pairing through a maximum matching of its core gives the exact formula for paired domination, and equality forces a star core. In the one-fewer-support case, parity and the forced-support argument imply an independent support set and a universal extra total-dominating vertex, which yields the second extremal family. These arguments cover all orders and the stated small exceptions.

## Originality

**PASS** — The fixed-order maximum gap and complete parity-sensitive extremal classification were not found in the inspected literature. The 2004 source supplies the key support-sensitive upper bound, and the 2022 tree paper supplies modern paired-domination structure and the subdivided-star benchmark, but neither inspected source states the order-only gap theorem or its full equality classification.

### Equivalent formulations

Searches/sources: Resultary semantic query: paired domination total domination tree fixed order maximum gap extremal trees; Chellali–Haynes 2004 DOI 10.1080/09728600.2004.12088782; Gorzkowska et al. 2022 DOI 10.1007/s00373-022-02542-7.

Evidence: The 2004 indexed material states the support-sensitive inequality used in the proof. The 2022 full text records paired domination facts for subdivided stars and proves different upper bounds. No exact fixed-order gap classification appeared in the Resultary search.

The audited theorem sharpens the support-sensitive inequality into an exact order-only extremum and classifies all equality cases.

### Broader coverage

Searches/sources: 2020 Paired Domination in Graphs survey chapter; 2022 Paired Domination in Trees full text; 2026 linear algorithm/asymptotic-normality preprint.

Evidence: The accessible 2022 full paper treats independence, packing and degree bounds, not the gap to total domination. The 2026 preprint concerns computation and random-tree asymptotics.

No inspected broader paired-domination theorem was shown to imply the complete gap classification.

### Exact database or table

Searches/sources: Resultary exact/semantic search for paired-minus-total domination gap at fixed tree order.

Evidence: The audited record was the exact matching hit; nearby records concern different domination parameters.

No tabulated invariant is involved; theorem-record search is the relevant exact check.

### Claim versus prior implication

Searches/sources: Can the 2004 support bound alone force the odd/even equality families?; Can the 2022 subdivided-star observation force the even extremals?.

Evidence: The support bound gives only the first numerical ceiling and leaves a saturated even case requiring the corona matching identity. The 2022 benchmark gives one family but not the order-only maximum or the two-family even classification.

Substantial equality-case reasoning beyond the prior inequality is necessary.

### Source inspections

- **Total and paired-domination numbers of a tree** — ACCESS_RISK.
  Identifier: https://doi.org/10.1080/09728600.2004.12088782
  Trigger: direct source of the support-sensitive inequality
  Material read: indexed theorem/abstract material and accessible search excerpt; open publisher access failed and the authorized institutional attempt returned no verified PDF
  Method: open web plus authorized institutional attempt
  Evidence: The accessible material confirms the inequality used, but whole-document overlap with the final classification could not be ruled out.
- **Paired Domination in Trees** — RELATED_NOT_COVERING.
  Identifier: https://doi.org/10.1007/s00373-022-02542-7
  Trigger: modern full treatment of paired domination in trees
  Material read: full open-access HTML, including known-results section and main structural bounds
  Method: lawful open-access full text
  Evidence: It includes the subdivided-star paired-domination value but does not state the fixed-order gap theorem.
- **Paired domination in trees: A linear algorithm and asymptotic normality** — DIFFERENT_DIRECTION.
  Identifier: https://arxiv.org/abs/2505.17672
  Trigger: recent primary work on paired domination in trees
  Material read: abstract and bibliographic material
  Method: lawful open-access metadata
  Evidence: It addresses algorithms and random-tree asymptotics.

Residual originality risks:
- The 2004 paper and the 2020 survey chapter were not available in complete verified full text; a differently phrased equality corollary remains the main originality risk.

## Scientific value

**PASS** — The result gives the exact extremal gap for every tree order and a complete equality classification with a genuine odd/even structural split. That is a natural extremal graph-theoretic classification, not merely a numerical consequence of the support bound.

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to RESULT.md or SLOGAN.txt is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
