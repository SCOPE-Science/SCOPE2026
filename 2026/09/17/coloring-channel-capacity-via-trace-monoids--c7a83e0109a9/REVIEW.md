# same-model review

## Status

Reported status: `SAME_MODEL_REVIEW_PASS`.

This is a same-model review, not independent validation or peer review.

## Correctness — PASS

The proof was stress-tested at the structural and finite-enumeration levels.

The central identification is checked in both directions. Adjacent swaps of letters never jointly observed by a channel preserve every projection. Conversely, equality of all channel projections fixes the relative order of every pair of labelled occurrences carrying dependent letters; equal-output words are therefore linear extensions of the same dependence poset and differ only by swaps of incomparable, hence independent, letters. This is exactly the trace/history-monoid congruence.

The standard trace-monoid growth identity then gives `G(z)=1/mu(z)`. The commuting graph is the complement of the pairs graph, so its cliques are precisely independent sets of the pairs graph; this matches the polynomial used in the claim. Goldwurm--Santini's minimum-modulus-root theorem justifies taking the reciprocal smallest positive root as the exponential growth constant.

Unused alphabet symbols were checked separately: they only allow padding, so length-n outputs are partial sums of visible trace counts. Their isolated vertices add `(1-z)` factors to the full pairs-graph polynomial and do not change the exponential rate.

The cycle root derivation was checked algebraically and against exhaustive output enumeration for small lengths. The supplied verifier confirms exact finite counts for several channel families, the unused-symbol case, and cycles C3 through C7.

## Originality — PASS, to the best of our knowledge

The underlying trace/history-monoid theory is classical and is not claimed as original. The potentially new step is its application to coloring-channel output equivalence and capacity.

The closest directly relevant source found is Yu--Schwartz, arXiv:2604.08234v1 (2026). It proves that coloring-channel capacity depends only on the pairs graph, gives exact capacities for several families, and explicitly states that it does not have a closed-form cycle capacity; at alphabet size four the four-cycle remains bounded but unresolved. Searches of that paper found no trace-monoid, history-monoid, commutation-monoid, or Cartier--Foata formulation.

The earlier Bariffi--Wachter-Zeh--Yaakobi coloring-channel paper, arXiv:2508.02229 / ISIT 2025, was also checked as the model source; no trace/history-monoid application was found.

External searches through 2026-09-17 included combinations of:

- `coloring channels` + `trace monoid`;
- `coloring channel` + `history monoid`;
- `coloring channels` + `Cartier-Foata`;
- `coloring channels` + `independence polynomial`;
- cycle-capacity searches around arXiv:2604.08234 and the exact constant `2+sqrt(2)`.

No public source applying the classical trace-monoid growth theorem to coloring-channel capacity was found. Repository overlap searches also found no existing SCOPE record under trace-monoid/history-monoid/coloring-channel terminology before publication.

### Access and residual-risk limitations

M. W. Shields, *Concurrent Machines* (The Computer Journal 28(5), 1985) was identified as the classical history-monoid source, but its full article was subscription-inaccessible for this review; only bibliographic metadata and abstract were inspected. This could affect attribution or the precise historical formulation of the generic projection theorem, but it cannot directly contain the coloring-channel application introduced four decades later.

Classical trace-monoid results are also distributed across monographs such as *The Book of Traces*; not every chapter was exhaustively inspected. The record deliberately treats those structural results as prior art rather than novelty.

A contemporaneous, unindexed, or later-version 2026 note could independently make the same coloring-channel/trace observation. No concrete evidence of such coverage was found. Originality is therefore only to the best of our knowledge.

## Value — PASS

The result does more than improve one numerical bound. It converts the entire coloring-channel capacity problem into a standard graph polynomial/root computation. It yields exact finite output generating functions when all symbols are visible, exact capacity for arbitrary pairs graphs, and as an immediate corollary resolves the cycle family that Yu--Schwartz explicitly left open. For the four-cycle it sharpens an interval to the exact value `log_4(2+sqrt(2))`.

The mechanism is reusable: any future structural information about signed independence/clique polynomials transfers directly to coloring-channel capacities.

## Review disclaimer

This record is a SCOPE Phase II same-model review. It is not independent verification, expert attestation, formal proof checking, or a guarantee of scholarly priority.

## Recorded review qualifications

> **Review status: SCOPE Phase II same-model review.** Correctness, originality, and value were assessed by the same-model review, not an independent reviewer. Originality is qualified to the best of our knowledge.
