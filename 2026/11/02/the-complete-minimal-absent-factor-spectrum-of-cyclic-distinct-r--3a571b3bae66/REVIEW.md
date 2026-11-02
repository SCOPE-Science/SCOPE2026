# Scientific review: exact antidictionary of cyclic distinct-run powers

## Correctness

**PASS.** The factor-language proof gives a complete local antidictionary for the two-sided periodic word: only non-successor unequal bigrams, overlong runs, and shortened internal runs are possible primitive obstructions. Every periodic factor of length at most \((k-1)|P|+1\) occurs in the finite power. Any additional minimal absent factor forces its longest proper prefix and suffix to occur only at opposite endpoints; their shared interior is a border of \(P^k\). The period block has different first and last letters, hence no proper border and shortest period \(|P|\); the border bound forces a single missing word. The disjoint-union count and length polynomial then follow. A separately constructed literal-factor verifier matches the proposed sets in 147 exhaustive parameter cases and checks 2,104 minimal absent words; this finite corroboration is not substituted for the all-parameter proof.

## Originality

**PASS, with residual bibliographic risk.** The closest material inspected includes the complete circular-word article of Fici, Restivo and Rizzo (arXiv:1707.04450), the full HTML of Charalampopoulos et al. (arXiv:1806.02718), and the mathematical text of Akagi et al. (arXiv:2202.13591). The first two give general circular minimal-forbidden-factor theory and algorithms; the third organizes minimal absent words through run-length encoding and gives generic bounds and reporting structures. The new claim is not the known distinct-letter circular special case, nor a general minimal-absent-word algorithm: it is a full exact set and length spectrum for arbitrary positive run lengths and at least two copies of an ordered distinct-run period, with a unique changing endpoint word. Search comparisons did not identify a direct stronger statement. An uncatalogued specialization or a theorem directly implying this formula could still exist.

Earlier exact absent-word results on short binary run families concern two-letter linear strings or scattered subsequences and neither contain nor imply this multi-letter cyclic-periodic antidictionary; the proof does not use them.

## Value

**PASS.** Minimal absent factors are the canonical antidictionary of a finite string and support exact negative-pattern representations. Here the explicit family has length growing with the repetition exponent, yet its **number** is independent of that exponent; the sole moving factor and the full length spectrum quantify a sharp boundary effect between circular and finite words. The complete classification is uniform over unbounded alphabet size, arbitrary run lengths, and all powers \(k\ge2\). It is structurally more informative than a generic output-sensitive reporting algorithm or a small-instance census.

## Limitations and closest literature

The result is restricted to cyclic periods in which all letters are distinct and each occupies one run; neither the binary case nor arbitrary repeated-letter periods are settled. The general MAW-language identity and circular comparisons in arXiv:1707.04450 and arXiv:1806.02718 are known, as is the run-length-encoding framework in arXiv:2202.13591. The full claimed spectrum is established by the proof here, not by assuming novelty from a failed search. No independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
