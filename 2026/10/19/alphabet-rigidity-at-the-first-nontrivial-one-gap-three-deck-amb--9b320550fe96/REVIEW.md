# Independent mathematical audit

## correctness

PASS

Independently constructed the 39-coordinate count array for every ternary word at lengths 1–13. Choosing r increasing positions in n-r+1 slots and adding j to the j-th position (zero-indexed) bijects onto admissible choices with successive gaps at least two. Counts fit unsigned bytes, since the largest total by order at n=13 is binomial(11,3)=165. Sorting exact 39-byte keys gave injectivity at 3–12 and exactly 12 size-two runs at 13, four on each two-letter support. Class counts at n=13 were 1,594,311 total and 1,594,299 singletons. A letter map pushes forward deck coordinates by summation; given distinct deck mates, map differing letters to 0 and 1, and, if present, a third used letter to 2. The resulting distinct ternary mates contradict injectivity at 3–12, or support rigidity at 13. Singleton letter counts force identical support within a class; on a given two-letter support ternary enumeration shows exactly four doubletons. This also precludes larger classes. Taking exactly one representative from every class gives both codebook formulas. The degenerate length-two assertion holds because admissible indices are then singletons only.

## originality

PASS

Credit the published binary threshold and an ambiguity example, as well as binary classification where documented. The distinct supported contribution is the exclusion of every length-13 ambiguous pair with ternary support, giving the complete arbitrary-alphabet class census by projection. The strongest matches do not establish that statement; neither short-length injectivity nor the binary collision list is needed as a novelty claim.

## value

PASS

At the first nontrivial length where the observation loses information, proving that every collision is supported on only two symbols gives an exact confusability census at every alphabet size. This natural boundary is directly usable for finite zero-error code sizing and counting maximizers, including at q=4; it is not merely one more witness or a small unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
