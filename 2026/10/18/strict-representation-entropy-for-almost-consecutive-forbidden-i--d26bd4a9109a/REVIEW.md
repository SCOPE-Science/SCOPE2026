# Scientific review

## Correctness: PASS
The exact recurrence for legal index-set counts is established by partitioning according to the largest selected index, with the crucial \(2c<k\) separation checked. A primitive finite-state transfer proves the simplicity and dominance of the count root. The eventual greedy recurrence has a primitive companion, so its own root governs the terms. Evaluating the count polynomial at the greedy root proves a strict entropy gap, and a fixed-index truncation sandwich proves the exact exponential order of representation multiplicity. The fixed-\(c\) large-\(k\) asymptotic follows by differentiating the count polynomial near the greedy root and using Lambert's \(W\) relation. Exact finite checks independently corroborate recurrence indexing and selected mean counts; they are not substitutes for the proof.

## Originality: PASS within inspected evidence
The closest primary work (Dantas e Moura et al., arXiv:2210.10577v2) already establishes both recurrences and identifies the average-multiplicity problem. Its Section 4 presents a conditional root-dominance scenario; the present claim proves the strict root inequality uniformly, verifies root dominance structurally, and supplies the sharp fixed-\(c\) parameter asymptotic. The 2016 Fibonacci quilt theorem (Catral et al., arXiv:1606.09312v2) does not directly cover these forbidden index sets. Targeted mathematical searches found no exact broader result. An unindexed equivalent treatment remains possible.

## Mathematical value: PASS
The theorem supplies the missing guaranteed exponential regime in an infinite family explicitly motivated by the originating paper's Question 5. The exact growth constant and asymptotic decay of its logarithm refine a conditional heuristic into a quantitative classification.

## Scope and risks
The main theorem assumes the greedy recurrence, with independently sourced unconditional families \(c=1,k\ge11\) and sufficiently large \(k\) at every fixed \(c\). It does not assert the recurrence for every small \(k,c\), determine the exact multiplicative asymptotic prefactor, or establish independent validation. Earlier recurrence facts belong to the cited authors.

Self-review: passed. Independent audit: not yet performed.
