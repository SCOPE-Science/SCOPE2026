# Review of the length-31 cyclic Hamming read-weight classification

## Correctness — PASS

Every code is defined as a precisely indexed kernel of the field-power parity-check matrix; the six eligible primitive polynomials are exhaustively identified. `verify.py` computes all eighteen complete integer coefficient arrays by prefix-conditioned syndrome-state transfer counting. `crosscheck.py` obtains the same eighteen arrays through a different signed Fourier-character transfer, and directly exhausts the complete binary word spaces at field degrees three and four. The verifiers check all code sizes, reciprocal equalities, three pairwise-distinct spectrum types, and uniform-projection first moments. These exact finite checks reconstruct the entire proof's arithmetic, rather than relying on output logs or partial samples. The claim does not assert any unproved asymptotic result.

## Originality — PASS, with remaining priority risk

The principal source-level comparisons are (i) Ma–Luo 2019 Section 4, which gives b-symbol enumerators for dimension-five simplex codes, *not* their dimension-26 Hamming duals; (ii) Liu–Pan 2021 Section 7, which gives generalized support-weight matrices for two smaller, lexicographically indexed Hamming examples but not this complete cyclic length-31 spectrum classification; and (iii) Shi–Özbudak–Solé 2021, Sections IV–V, which supplies bounds for arbitrary cyclic codes, an exact single-nonzero-coset family inapplicable to dimension-26 Hamming codes, and an enumerator stability theorem only for read lengths at least the code dimension. The 2023 complete enumerator theorem for semiprimitive *irreducible cyclic codes* concerns codes with irreducible parity-check polynomials, whereas each code here has a degree-five irreducible generator polynomial and degree-26 reducible parity-check polynomial. An indexed result about pair-weight *generation profiles* of cyclic Hamming codes does not count individual codewords at each read weight. No identical table or stronger published statement implying this exact three-way length-31 classification was located. A historically unindexed finite table or overlooked specialized codeweight result remains a priority risk.

## Value — PASS

This is a complete classification of a natural family at the first binary Hamming length with three reciprocal primitive-polynomial pairs. All six codes have identical ordinary Hamming weight enumerators and minimum distance; the complete cyclic read-weight spectra distinguish their coordinate embeddings in the metric relevant to overlapping reads. This finite classification supplies reproducible multiplicity benchmarks, which minimum read distance alone cannot provide. It is not an arbitrary parameter slice or a routine renaming of an existing enumerator: it resolves the first nontrivial choice of primitive polynomial with distinct read-weight types.

## Scientific limitations

Only six primitive binary cyclic length-31 realizations and three read lengths are classified. No general formula for all primitive-code lengths, all permutations or independently established historical priority is claimed. The certificate is reproducible arithmetic and self-review, not an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
