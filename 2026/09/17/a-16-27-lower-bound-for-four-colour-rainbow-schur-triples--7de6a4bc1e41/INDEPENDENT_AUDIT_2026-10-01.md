# Independent mathematical audit — SCOPE-20260917-007

Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Correctness
**PASS** — The coloring and continuous density calculation were independently reconstructed with exact rational polygon integration. The nine ordered residue-pair good areas were 0; four copies of 47/144; two copies of 1/4; and two copies of 31/72, summing to 8/3. Multiplying by residue density 1/9 gives rainbow count coefficient 8/27, and dividing by the ordered Schur-pair coefficient 1/2 gives 16/27. Boundary rounding affects only O(n) pairs.

## Originality
**PASS** — The directly preceding Hegde--Kumar--Pratibha preprint develops the general k-color problem but its public record does not state this mod-3/two-cut construction or the 16/27 value. Searches for four-color rainbow Schur 16/27, aliases under anti-Ramsey Schur multiplicity, and published result indexes found no prior equivalent or stronger lower bound. A later indexed 0.553 construction is weaker than 16/27 and therefore does not cover the claim.

### Equivalent formulations
Both formulations were searched; no 16/27 or equivalent mod-3/two-threshold construction was located outside this record.

### Broader coverage
The known general framework motivates but does not mechanically imply the audited structured coloring or its stronger value.

### Exact database or table check
This supporting database evidence is not treated as a proof of novelty; novelty rests on comparison with the directly relevant general-k source.

### Claim versus prior implication
The audited construction is an additional explicit lower-bound witness rather than a specialization of an inspected stronger theorem.

## Value
**PASS** — The k=4 anti-Ramsey Schur problem is a natural highlighted case of an active multiplicity question, and 16/27 is a substantial explicit asymptotic lower bound obtained by a transparent structured coloring. It is not an arbitrary finite computation.

## Source inspections
- **A somewhat sure note on an un-Schur problem** (https://arxiv.org/abs/2609.18474): NO ACCESSIBLE STRONGER FOUR-COLOR STATEMENT. Primary arXiv abstract, author research-page abstract, and bibliographic record; direct PDF retrieval was unavailable in this audit. The source explicitly studies general k and states its 3-color bounds; no 16/27 four-color statement was found in accessible material.

## Residual risks
- The full text of arXiv:2609.18474 could not be fetched through the current web path; its abstract confirms general-k treatment but does not expose every four-color formula. This is a residual originality risk.
- The result is only a lower bound; no optimality of the coloring or exact four-color asymptotic constant is claimed.

The accompanying JSON file records the four structured originality checks, source inspections, checked sources, and residual risks.
