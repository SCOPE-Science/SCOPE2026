# Scientific review: circular Zimin conjugacy transport

## Correctness — PASS

The theorem applies to literal distinct-letter Zimin words, circular windows of length no greater than the previous-rank word, and conjugacy of window strings. Its proof partitions windows using the uniquely occurring new central letter. Avoiding windows reproduce precisely the preceding circular factor classes. Marker windows are rotated to their unique new-letter position and identified with concatenations of ruler-word prefixes and reversed prefixes. Adjacent representatives coincide exactly between successive multiples of the largest power of two dividing the length; the explicit sampled-position argument distinguishes every nonadjacent block. This closes a possible collision gap that a local adjacency argument alone would not resolve. The all-rank proof is finite and exact for each rank; explicit checker comparisons through rank seven corroborate it. No unproved computer-assisted infinite step is used.

## Originality — PASS, with historical-priority risk

The exact claim was compared against source-specific and alias searches for Zimin cyclic or circular factors, conjugacy or necklace classes, two-adic/ruler structure, and odd-part rank increments. In Cassaigne–Fici–Sciortino–Zamboni (arXiv:1402.5843), the general cyclic-complexity language is developed for infinite finite-alphabet words; the full accessible article's theorems concern other word families, not this finite Zimin transport. In Rytter–Shur (arXiv:1409.8235), the inspected full text concerns Zimin-pattern detection and related Fibonacci factors. An accessible comparison of earlier mathematical claims included a Zimin circular even-Parikh witness theorem, a Zimin unbordered-factor classification, and Zimin Lyndon-factor and suffix-array results; none implies the exact circular conjugacy partition or its odd-part increments. Searches returned no established equivalent or stronger result. This supports a best-knowledge originality judgment, not a claim of exhaustive priority verification.

## Value — PASS

Cyclic conjugacy is an established natural factor-complexity invariant, while Zimin words are canonical recursively nested avoidance patterns and the ruler sequence makes their higher-letter distribution explicitly arithmetical. The theorem classifies **all** new necklace classes at every admissible window length and every rank, including the exact indices of merged windows, rather than giving just another table of small-rank values. Its odd-part slope yields an exact eventual affine rank law at each fixed length. The calculation exposes a structural link between palindromic recursive words, circular factor conjugacy, and two-adic valuation; it is not simply relabeling a known formula.

## Source comparisons and limitations

- arXiv:1402.5843: introduction, definitions, theorem statements and family-specific sections were inspected as accessible article text; finite Zimin words and rank-to-rank odd-part transports are outside the verified theorem scope.
- arXiv:1409.8235v1: abstract, introduction and the article's algorithmic/combinatorial sections were inspected; the paper's Zimin result concerns pattern matching, not conjugacy of circular windows.
- Closest previous claims reviewed for implication: Zimin circular even-Parikh boundary words, contiguous unbordered factors, Lyndon factors, and suffix arrays; none classifies the general conjugacy classes of all circular windows.
- Residual risk: undiscovered older source or equivalent result under alternate terminology; independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
