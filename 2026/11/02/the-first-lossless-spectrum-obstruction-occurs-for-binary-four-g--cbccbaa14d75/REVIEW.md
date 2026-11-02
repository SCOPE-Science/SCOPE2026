# Scientific review

## Correctness — PASS

A binary \(k\)-gram is an edge of the order-\((k-1)\) de Bruijn graph. A word with exact set \(S\) corresponds to a directed walk traversing precisely the edges \(S\) at least once; a word without repetitions corresponds to an Euler trail. Breadth-first closure of the finite vertex/seen-edge-mask state space exhaustively enumerates feasible support masks even for arbitrarily long walks. A separately implemented SCC-condensation criterion yields identical complete feasible sets for both window sizes. A second finite-state closure disallowing repeated edges enumerates precisely the trail masks. Counts, cardinality distributions, minimal obstruction support sets, and explicit witnesses are reproduced by the embedded program; additional direct word enumeration independently reproduces all \(121\) binary three-gram supports.

## Originality — PASS, with residual risk

Alanko–Pérez-López gives graph-based distinct \(k\)-mer counting, not the count of which subsets of fixed binary \(k\)-grams are realizable spectra or the lossless fraction. Chukhin et al. introduce \(k\)-spectra and the overlap graph in the context of greedy superstring ratios, not the exact complete binary three-/four-gram incidence census. Actual indexed searches on equivalent terminologies and the accessible claim history did not identify these same numbers, sharp threshold, or two minimal obstructions. Search failure is not publication-priority proof; unindexed enumerations remain possible.

## Mathematical value — PASS

This exact finite classification resolves the first window length where a feasible distinct-factor presence profile fails to have an Euler-trail realization. It shows a qualitative transition at length four (\(3310\) of \(5921\) feasible supports require repetitions) and gives a pair of smallest constructive obstructions. Separating presence-only from multiplicity-aware reconstruction is directly motivated by de Bruijn assembly and short-superstring problems. The complete reproducible tables provide benchmark inputs for exact-spectrum reconstruction algorithms.

## Boundaries

Fixed binary alphabet and window lengths three and four only. Independent mathematical and exhaustive publication-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
