# Assessment of the crown-graph switch-distance finding

## Correctness — PASS

The bijection with derangements and the exact legal-transposition rule are proved directly from matching incidence. Conjugation by a common permutation on both bipartition classes acts transitively on each derangement cycle-type class and preserves the flip graph. A BFS from one representative in each class is therefore sufficient for all-pairs diameter, eccentricity spectrum, and uniqueness of the ten-step antipodes. Two independent complete implementations enumerate every derangement for each order from four to nine and agree on every class-distance histogram; the full programs and outputs accompany the finding. This is a finite exhaustive proof, restricted to those orders.

## Originality — PASS, with residual risk

Dyer–Jerrum–Müller's proved diameter-at-most-part-size theorem applies to chordal bipartite graphs, not to crowns with induced six-cycles, and provides no contrary bound or crown-specific classification. Bonamy et al. treat general four-cycle reconfiguration and tractable graph classes, not the exact nine-pair diameter and inverse-antipode incidence. Enumeration of derangements alone does not determine distances. A separately known adjacent-position transposition model is narrower than the unrestricted two-position swap induced by a crown four-cycle. No covering statement was identified in targeted searches; this is not proof of publication priority. Unindexed exact computations remain a risk.

## Mathematical value — PASS

The sharp nine-pair boundary tests whether the natural linear diameter bound established on chordal bipartite graphs survives outside that class, on one of the simplest dense bipartite graph families with a forbidden matching. The answer is a concrete finite obstruction, accompanied by a geometrically interpretable and complete classification of all extremal pairs. The claim is more informative than a bare census: all worst cases arise from inverses of disjoint three-cycles.

## Limits

No assertion for higher orders, no mixing-time statement, and no independent external validation. Computations and verification reports are supplied for direct reproduction.

Self-review: passed. Independent audit: not yet performed.
