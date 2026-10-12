# Self-review

## Correctness
**PASS.** Every anonymous four-candidate profile through five voters is exhausted, with exact multinomial weighting back to labeled profiles. Baldwin branches over every tied minimum, so singleton output is exactly tie-independent uniqueness. Nanson follows the inspected strict-below-average definition and returns a non-singleton state rather than inventing a winner when elimination stalls. A second explicit-ballot engine agrees on every profile. Candidate relabeling and the witness are replayed exactly.

Risk: the theorem is convention-sensitive by design and does not cover profiles resolved only by an imposed external tie-breaking order.

## Originality
**PASS.** The primary literature defines the two rules, emphasizes their close relationship, and analyzes manipulation complexity, including a four-candidate boundary for weighted Nanson manipulation. Those results do not imply a voter threshold for direct agreement of the rule outcomes. Searches by rule names, aliases, exact parameter pair, exact counts, unique-winner language, and symmetry language did not locate the \(24480/384\) census or the \(16\)-class quotient.

Risk: absence from indexed searches is not proof of bibliographic uniqueness; an unindexed small-profile computation could contain the same census.

## Value
**PASS.** Nanson and Baldwin are historically linked Condorcet-consistent Borda-elimination rules whose only procedural difference is how aggressively low-scoring candidates are removed. The smallest electorate where they force different winners without relying on tie-breaking is therefore a natural structural boundary. The complete first layer supplies more than one example: exact prevalence, anonymity reduction, winner-pair symmetry, and the full candidate-relabeling quotient.

Self-review: passed. Independent audit: not yet performed.
