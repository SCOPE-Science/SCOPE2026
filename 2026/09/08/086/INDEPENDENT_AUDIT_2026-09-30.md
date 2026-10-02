# Independent mathematical audit — 2026-09-30

## Record

First P/N classification with witnesses for Dawson (.07) and Treblecross (.007) on subdivided stars and bistars with arms<=6

## Disposition

passed

## Correctness: PASS

A fresh solver built directly from the graph-lift rules, using canonical unlabeled-tree memoization and exhaustive legal deletion moves, independently recomputed all 84 subdivided stars and 406 bistars for both games. It reproduced exactly the claimed P-counts: .07 gives 19 star and 69 bistar P-positions; .007 gives 11 star and 40 bistar P-positions. The complete star P-sets matched the record, all 28 symmetric bistars are N for .07, and the .007 symmetric-bistar P-set is exactly (0,0),(0,3),(0,6),(3,3),(3,6),(6,6).

## Originality: PASS

The primary graph-octal paper located in the search introduces octal games on graphs and states a complete resolution for game 0.33 on subdivided stars and bistars, not for .07 or .007. Heap/path sources cover Dawson and Treblecross on paths. Resultary returned the audited record as the exact graph-family hit and no competing .07/.007 star/bistar classification. Thus, best-of-knowledge evidence supports originality of this finite graph-board classification and its structural symmetric-bistar lemmas.

## Scientific value: PASS

The two games are classical octal games, the graph lift is an established natural extension, and subdivided stars/bistars are exactly the canonical first branched tree families studied in that framework. A complete finite classification with winning witnesses plus symmetric-family lemmas is a motivated boundary dataset, not an arbitrary collection of positions.

## Limitations and residual risks

- The result is a complete finite block for arms at most 6, not an all-arm theorem.
- The full arXiv HTML for the most relevant prior graph-octal paper could not be fetched in this run; its primary abstract clearly scopes the solved same-family game to 0.33.
- Only P/N outcomes and witnesses are claimed; stored Grundy values remain auxiliary.

## Sources inspected

- L. Beaudou et al., `Octal Games on Graphs: The game 0.33 on subdivided stars and bistars`, arXiv:1612.05772.
- OEIS A002187 and the Treblecross heap literature for path-only cross-check context.
- The assigned RESULT.md and game-table artifacts.

This file records a mathematical audit of the scientific claim. It is not an expert attestation or a statement about any separate verification channel.
