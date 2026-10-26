# Scientific review

## Correctness — PASS

All three run lengths are arbitrary positive integers, and the selected sets are two-element subsets of ordinary one-indexed positions. The single-letter factors force at least two positions, and unique boundary factors force the exhaustive pair shapes for middle-run length at least two. In the singleton-middle-run case, every factor containing a one crosses the unique one; all remaining factors are zero powers, so precisely a position in a longest zero run is required. Every possible factor type is explicitly checked in the proof. The generating function follows from two finite-parameter rational sums, and the uniqueness and mean limits from exact composition counts and the order-three pole. An independent finite implementation enumerates 2,744 parameter triples and checks 38 aggregate coefficients and 38 uniqueness counts; finite tests are supplementary, not infinite proof.

## Originality — PASS, with residual risk

Direct scientific database checks for the three-run optimum-pair classification, equivalent count formula, length enumerator and unique/mean gap returned special-family studies (Thue–Morse, pseudostandard binary families, length-12 census) and no equivalent unrestricted three-run formula. The available mathematical publications classify **four-run** words with an actual fourth positive run, not this complete three-run case, so the present theorem is not stated as a corollary of an inspected prior claim. The 2019 combinatorial paper and the 2026 morphic-word paper were examined for their factor definition and multiplicity theorems; neither inspected discussion states or directly covers these three-run formulas. Indexed records are incomplete, so unindexed three-run coverage remains possible. General-purpose per-word verification algorithms also provide a way to compute examples, not the structural three-parameter theorem.

## Mathematical value — PASS

The theorem resolves an infinite natural family of exact smallest-attractor classifications, including **all minimizers**, and the generating function computes exact total multiplicity at every length. The large discrepancy between almost-sure uniqueness and a mean of \(5/2\) identifies an interpretable rare-family contribution. This answers a motivated multiplicity question beyond minimum size or isolated finite computations, with a reproducible proof.

## Limitations

The word family has exactly three binary runs and is noncyclic; the mean is conditional on this family. An equivalent unindexed result remains a novelty risk. Only self-review has been performed.

Self-review: passed. Independent audit: not yet performed.
