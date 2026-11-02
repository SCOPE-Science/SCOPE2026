# Review of the graph-ball online-dimension theorem

## Correctness

PASS. In a triangle- and four-cycle-free graph, distinct closed radius-one balls intersect in at most two vertices. Connectedness and order at least three exclude duplicate balls. These facts force the first positive-query version space to have online depth at most two, yielding global Littlestone dimension at most three. The exact first-positive depth-two criterion is degree at least three; the exact first-negative depth-two criterion is the two-sided neighborhood cardinality inequality. Their conjunction at the root proves the asserted equivalence for every graph in scope. A three-query VC-shattering contradiction and constructions for paths, cycles and branching graphs prove VC dimension two. An explicit eight-vertex tree satisfies the online criterion, and counting its eight terminal hypotheses proves minimum order. The verifier scripts independently tested the recurrence, the criterion and the witness.

## Originality

PASS under accessible comparisons; no assertion of definitive historical priority. The original 2020 Benediktsson–Macpherson–Adler paper treats static open-neighborhood VC dimensions/densities for Johnson and Hamming graphs and does not give an online closed-ball criterion for all girth-at-least-five graphs. The older Bousquet–Thomassé work studies static graph-ball VC dimension, and its minor-exclusion bound already covers the static tree upper bound; that covered portion is credited. Accessible published-result comparisons did not reveal the complete online theorem. Other neighborhood results concern open neighborhoods of line graphs or of Hamming/Johnson graphs, which neither identifies this graph family nor implies the closed-ball exact local criterion. Alternative terminology could conceal a pre-existing equivalent theorem.

## Value

PASS. The theorem exactly classifies an online learnability invariant on the unrestricted family of finite connected graphs with no triangles and quadrilaterals, using a local computable obstruction rather than exponential decision-tree search. It distinguishes the stable VC dimension two from an attainable extra adaptive round, establishes its minimum graph order and includes all trees. This is a complete natural-class classification, not a numerically selected special example.

## Closest literature and limitations

B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (2020); N. Bousquet and S. Thomassé, *VC-dimension and Erdős–Pósa property*, arXiv:1412.1793 (2014). The theorem is limited to closed radius-one balls of connected triangle- and four-cycle-free graphs. Complete historical coverage and external independent verification remain unestablished.

Self-review: passed. Independent audit: not yet performed.
