# Scientific review: depth-three neighborhood shattering in threshold graphs

## Correctness — PASS

The rank-one/two/three recursion is an exact restatement of complete binary-tree shattering for finite *distinct* hypotheses; duplicate graph-neighborhood rows are removed. Every depth-three witness uses at most eight distinct centers and seven query vertices, so a minimal induced threshold obstruction has at most fifteen vertices. The creation-word encoding covers every threshold graph up to that order. Two separately implemented complete enumerations return identical order-by-order counts and exactly four deletion-minimal creation words, with distinct degree sequences. A third procedure constructs and checks eight leaf paths for each obstruction. The proof applies for arbitrarily large threshold graphs by the fifteen-vertex reduction. Its numerical input is a genuinely exhaustive finite certificate, not a statistical sample.

## Originality — PASS with residual risk

The closest graph-neighborhood literature studies static VC dimension, while the closest Littlestone literature gives general closure bounds. Neither inspected primary source states or entails an exact *induced-obstruction classification* for open-neighborhood Littlestone dimension three in threshold graphs. Searches also considered the synonymous tree-shattering rank, Shelah rank, stability terminology, and nearby threshold-graph identifying-code and zero-forcing results. No matching prior theorem or database table was identified. This supports a best-knowledge originality judgment, not absolute priority: unindexed or inaccessible literature could remain, especially under alternative terminology.

## Value — PASS

The four forbidden induced graphs provide an exact hereditary characterization of the first nontrivial adaptive-shattering threshold in an infinite, canonical graph class. The finite list gives a constant-size obstruction test, identifies sharp first possible order eight, and exhibits a strict VC-versus-Littlestone separation even for the restrictive threshold family. The number fifteen is forced by the eight hypothesis leaves plus seven queries in a depth-three tree; the numerical enumeration is not an arbitrary isolated census.

## Relationship and limits

Adler–Benediktsson–Macpherson (2020) treats VC dimension of open graph neighborhoods on Johnson and Hamming graphs. Ghazi–Golowich–Kumar–Manurangsi (2021) proves general Littlestone closure bounds. Coudert–Csikós–Ducoffe–Viennot (2024) computes closed-neighborhood VC dimension. These do not yield this threshold-graph forbidden-obstruction theorem. The result does not classify dimensions four and above, and priority could be affected by unidentified earlier work. Exact finite enumeration and witness files are provided for reproduction.

Self-review: passed. Independent audit: not yet performed.
