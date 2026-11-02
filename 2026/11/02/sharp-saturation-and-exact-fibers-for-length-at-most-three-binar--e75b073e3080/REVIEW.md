# Scientific review of short binary composition-read fibers

## Correctness

**PASS.** Each word of weight \(w\) corresponds bijectively to a nonnegative \((w+1)\)-tuple of zero gaps. Increasing a gap that already contains at least two zeros adds only zero-grade windows of lengths two and three. Capping gaps at two therefore preserves every positive-grade observation, and stars and bars proves the exact inverse-fiber formula. The sharp threshold follows because every truncated tuple having a gap capped at two is realizable at length \(3w+2\), whereas the all-two signature with \(3w\) one-grade triples is impossible at length \(3w+1\). For weight three, the fully enumerated finite certificate partitions 65 capped vectors into 29 distinct signatures, all with length-eleven witnesses; smaller lengths are exhausted separately. The verifier tested 106 full inverse-fiber distributions independently through length 18, including both equality of profile keys and individual preimage counts.

## Originality

**PASS, qualified.** Ye and Elishco (arXiv:2208.14963, Section VIII) define the precise length-limited composition channel, construct coding families, and explicitly leave capacity questions for further study; they do not derive the present capped-gap inverse-fiber formula or sharp fixed-weight saturation. The closest related results identify binary length-two composition profiles at all weights, length-limited composition profiles for exactly two markers, or single-length three-window composition profiles, none of which supplies the joint length-two-plus-three fibers for every fixed weight. An explicit eleven-symbol collision pair for the three-window profile splits when two-window counts are added. Yang and Chen (arXiv:2411.03776) instead observe prefixes and suffixes of every possible length. Searches under local-pattern, Parikh-spectrum, and short-mass-spectrum terminology found no matching complete statement, but an unindexed equivalence cannot be excluded.

## Mathematical value

**PASS.** The motivating literature explicitly asks for capacity information in length-limited fragment models. The result supplies exact sizes of *all* reconstruction ambiguity classes, an effective exact-capacity algorithm at every length and sparse weight, a universal sharp saturation length, and a closed complete three-marker capacity profile. The bound demonstrates that lengthening a constant-weight source eventually does not add any distinguishable fragment profiles, an exact information-loss phenomenon rather than an ad hoc finite census.

## Scientific limits and closest literature

The theorem is for binary indexed linear words, complete overlapping multiplicity-preserving fragment compositions, maximum fragment length three, and a known weight. It does not address cyclic reads, missing observations, long fragments, or error correction. Related earlier models with all substring lengths or with only prefix/suffix information are not equivalent. Public priority remains subject to a broader specialist literature check; the scientific review is not independent external validation.

Self-review: passed. Independent audit: not yet performed.
