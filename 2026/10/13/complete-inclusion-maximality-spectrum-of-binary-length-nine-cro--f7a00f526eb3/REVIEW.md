# Scientific review

## Correctness — PASS

For every binary nine-word code the no-overlap condition is equivalent to being a clique in the compatibility graph on unbordered words; inclusion maximality is maximal-clique status. This establishes the exact finite search domain (148 vertices, 3080 edges). The recursive pivot enumeration is complete and nonduplicating, and each emitted set is directly retested for maximality. The separate bitset and string/set implementations generate identical sorted catalogues of 62,280 codes, with matching size histogram; the digest of the full seven-megabyte plain-text catalogue is `ebacd3ecd51b08c10b05e462a3496200ca3261b0840a0a3351910af91436ecd3`. Complementation/reversal close every orbit and all orbits have size four. No assertion for other block lengths is inferred.

## Originality — PASS

Bilotta–Pergola–Pinzani (arXiv:1112.3168) and Barcucci et al. (arXiv:1410.4710) construct particular non-expandable sets. Chee et al. (arXiv:1209.0236) and Blackburn (arXiv:1303.1026) study extremal sizes and bounds, including the exceptional length-nine case. Qin–Chen–Luo (arXiv:2309.08915) classify non-expandability for particular explicit code families. Inspected sections do not supply the full global inclusion-maximality polynomial or its free symmetry-action classification. The top-size coefficient is included as a component of the enumerator, not separately claimed as a discovery. An unindexed prior exhaustive catalogue remains possible.

## Value — PASS

The exact size distribution of inclusion-maximal codes measures which greedily saturated synchronization designs can occur and how sharply their sizes can differ from the known optimum. At the historically exceptional binary block length nine, the answer distinguishes one-word terminal designs from the 14-word optimum, rules out terminal sizes two and three, and gives the complete cardinality and symmetry distributions. This is a natural complete finite classification rather than an arbitrary threshold experiment.

## Limits

The result is restricted to binary length-nine non-overlapping codes. Finite exhaustive proofs depend on precisely reproduced code paths, checked here; no all-length theorem, bit-error guarantee, priority certificate, or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
