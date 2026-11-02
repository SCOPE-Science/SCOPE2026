# Review: exact closed-Hamming-neighborhood dimensions

## Correctness
PASS. The intersection-of-balls lemma and coordinate-line trace structure give a uniform upper bound of three on both dimensions. The small-parameter classification is proved using the row/column obstruction and two explicit lower-bound embeddings; the ternary adaptive witness is replayed by independent distance evaluation. The executable checks nine finite cases; the theorem for all parameters is established symbolically.

## Originality
PASS under accessible source and record comparisons. The closest 2020 primary paper establishes exact **open** neighborhood VC results and only boundedness for the **closed** version; its statements cannot be substituted because at the binary three-cube the open VC dimension is two while the closed VC dimension is three. Later work on induced Hamming subsets also treats open neighborhoods. General thicket theory does not identify these finite parameters. Semantic-record and accessible local claim searches returned no dominating equivalent theorem. Historical completeness is not established.

## Value
PASS. This yields a complete two-parameter classification of both static and online shattering for a standard distance-transitive graph family, pinpoints the only parameter where adaptive learning requires more mistakes than static shattering, and gives an inherited hereditary upper bound. The local geometry is reusable in related neighborhood-learning problems. The result is not a classification at larger radii or for arbitrary induced subgraphs.

## Closest literature and limitations
Adler--Benediktsson--Macpherson, arXiv:2007.16042 (2020, Section 4), is the most direct comparison; Bhaskar, arXiv:1702.03956 (2017), supplies general thicket theory. Housholder--Mangiapanello--Senger, arXiv:2505.14641 (2025), examines induced-subgraph open-neighborhood questions. Neither independent mathematical validation nor a comprehensive historical-priority review has been performed.

Self-review: passed. Independent audit: not yet performed.
