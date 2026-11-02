# Review of exact closed Hamming-ball support profiles

## Correctness
**PASS.** The statement explicitly fixes all integer dimensions and alphabet sizes and uses inclusive radius one. The ball-intersection lemma restricts every candidate triple to three disjoint shapes; explicit center witnesses prove sufficiency, the alphabet-size obstruction is exact, and direct counting without duplicate centers produces the closed coefficients. Four-point impossibility follows from the structure of intersections with coordinate groups. A standalone independent trace enumerator matched the formula on sixteen parameter pairs, including exceptional boundaries. Finite experiments are not treated as a substitute for the universal proof.

## Originality
**PASS within inspected sources, with historical-priority risk.** The closest direct previous result is the known closed-neighborhood VC/Littlestone dimension classification for Hamming graphs. It establishes only the largest support size, not the counts or full characterization of supports; the new coefficientwise formula is not a corollary of dimension alone. Adler–Benediktsson–Macpherson (2020) focus on *open* neighborhoods; their Hamming section proves bounds and gives sample shattered triples, not a census of *closed* neighborhoods. Coudert–Csikós–Ducoffe–Viennot (2024) offer general closed-neighborhood VC algorithms and bounds, without this parametric enumeration. No exact matching enumeration was located among the inspected sources or in targeted published-record searches. A differently named combinatorial enumeration may nevertheless exist.

## Mathematical value
**PASS.** A dimension-three statement cannot distinguish support counts, while the exact shattering polynomial gives every cardinality and explains sharp small-alphabet transitions in the natural class of error-radius-one Hamming balls. The three geometric types produce a non-obvious simplification to one factored cubic coefficient. The invariant is directly motivated by finite VC sampling and graph-neighborhood trace complexity; no larger downstream theorem is asserted or needed.

## Limitations
Only full Hamming graphs at inclusive radius one are covered; larger radii, arbitrary induced subgraphs, and adaptive learning dimensions are not treated. Priority remains vulnerable to equivalent formulations under coding-theoretic terminology. These limits do not affect the demonstrated formula.

Self-review: passed. Independent audit: not yet performed.
